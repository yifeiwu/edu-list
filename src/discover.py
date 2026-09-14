"""Discovery adapters — one function per source, all free-tier safe.

Every adapter: (url, state, per_run, timeout) -> list[Candidate].
Candidate: {name, url, iso2, type_hint, source}
All failures return [] (never crash a run). Cursors persist in state["cursors"].

Dormant adapters (ugc-in, crt.sh, Common Crawl, ETER/GIAS/FR-sup/Giga,
edudirectory) were deleted: they were blocked (403/WAF), timed out
(502/504 on wildcard scans), or had no stable bulk URL. See SOURCES.md.
"""
from __future__ import annotations

import csv
import io
import re
import time
import zipfile

import requests

UA = {"User-Agent": "edu-domains-bot/1.0 (github-actions; educational-research)"}

# OSM rotation boxes: one bbox per session (quota-sensitive). Override per
# source via sources.yaml `boxes: [[label,s,w,n,e], ...]`.
OSM_BOXES = [
    ("GB-London", 51.2, -0.6, 51.7, 0.3),
    ("US-NYC", 40.4, -74.3, 41.0, -73.6),
    ("FR-Paris", 48.7, 2.2, 49.0, 2.6),
    ("IN-Delhi", 28.4, 76.9, 28.9, 77.4),
    ("NG-Lagos", 6.3, 3.0, 6.7, 3.6),
    ("BR-Saopaulo", -23.7, -46.8, -23.4, -46.4),
    ("ID-Jakarta", -6.4, 106.6, -6.0, 107.1),
    ("EG-Cairo", 29.8, 31.0, 30.2, 31.5),
    ("PH-Manila", 14.4, 120.9, 14.8, 121.1),
    ("ID-Surabaya", -7.4, 112.6, -7.1, 112.9),
]
WHED_COUNTRIES = ["Senegal", "Ghana", "Kenya", "Peru", "Vietnam", "Morocco",
                  "India", "Philippines", "Indonesia"]

# Contact default lives in cli_common (single identity); re-exported here
# for backwards compatibility with existing imports/tests.
from src.cli_common import DEFAULT_MAILTO  # noqa: F401,E402
from src.geo import DEQAR_COUNTRY_ISO  # noqa: F401,E402  (single source in geo.py)


def _get(url, timeout=30, params=None, headers=None, stream=False,
         tries: int = 3, sleep_fn=None):
    """GET with retries on transient statuses (429/502/503/504).

    Raises the last exception / returns last response to the caller; adapters
    catch everything and return [] so one source never fails a run.
    """
    _sleep = sleep_fn or time.sleep
    h = dict(UA)
    if headers:
        h.update(headers)
    last_exc = None
    for attempt in range(tries):
        try:
            r = requests.get(url, params=params, headers=h,
                             timeout=timeout, stream=stream)
            if r.status_code in (429, 502, 503, 504) and attempt < tries - 1:
                wait = min(2 ** attempt, 8)
                try:
                    ra = r.headers.get("Retry-After")
                    if ra and str(ra).strip().isdigit():
                        wait = min(int(ra), 30)
                except Exception:
                    pass
                try:
                    _sleep(wait)
                except Exception:
                    pass
                continue
            return r
        except requests.RequestException as e:
            last_exc = e
            if attempt < tries - 1:
                try:
                    _sleep(min(2 ** attempt, 8))
                except Exception:
                    pass
                continue
            raise
    if last_exc is not None:
        raise last_exc
    raise RuntimeError("unreachable _get")


def _cursor(state: dict, key: str, default: int = 0) -> int:
    try:
        return int(state.get("cursors", {}).get(key, default))
    except Exception:
        return default


def _set_cursor(state: dict, key: str, value: int) -> None:
    state.setdefault("cursors", {})[key] = value


def _advance_circular(state: dict, key: str, off: int, consumed: int,
                      total: int) -> None:
    """Advance a circular file offset: (off + consumed) % total.

    `off` is the offset just consumed, `consumed` the slice length actually
    read, `total` the row count. No-op when total <= 0. Keeps cursors bounded
    and rotation even across sessions.
    """
    if total <= 0:
        _set_cursor(state, key, 0)
        return
    try:
        base = int(off) % total
    except Exception:
        base = 0
    _set_cursor(state, key, (base + max(int(consumed), 0)) % total)


def _next_rotation(state: dict, key: str, length: int) -> int:
    """Bounded round-robin index: return cur % length, advance (idx+1) % length.

    Previously `osm_idx`/`whed_idx` grew unbounded in state.json; modulo
    keeps them small while preserving rotation order for existing states.
    """
    if length <= 0:
        return 0
    idx = _cursor(state, key, 0)
    try:
        cur = int(idx) % length
    except Exception:
        cur = 0
        idx = 0
    _set_cursor(state, key, (idx + 1) % length)
    return cur


def discover_hipo(url, state, per_run, timeout=30):
    off = _cursor(state, "hipo_offset", 0)
    try:
        r = _get(url, timeout)
        if r.status_code != 200:
            return []
        data = r.json()
        if not isinstance(data, list):
            return []
    except Exception:
        return []
    chunk = data[off:off + per_run]
    _advance_circular(state, "hipo_offset", off, len(chunk), len(data))
    out = []
    tag = time.strftime("%Y-%m-%d")
    for e in chunk:
        if not isinstance(e, dict):
            continue
        iso = (e.get("alpha_two_code") or "").upper()
        for d in (e.get("domains") or [])[:2]:
            if d and "." in str(d):
                out.append({"name": e.get("name", d), "url": f"https://{d}",
                            "iso2": iso, "type_hint": "university",
                            "source": f"hipo:{tag}"})
    return out


def discover_ror(url, state, per_run, timeout=30):
    # ROR v1 API: fixed 20 results/page; filter=types:Education selects
    # research-active education orgs. Walk enough pages to honor per_run.
    page = _cursor(state, "ror_page", 1) or 1
    pages_needed = min(max((per_run + 19) // 20, 1), 15)
    out = []
    for _ in range(pages_needed):
        try:
            r = _get(url, timeout, params={"filter": "types:Education",
                                           "page": page},
                     headers={"Accept": "application/json"})
            if r.status_code != 200:
                break
            items = r.json().get("items", [])
        except Exception:
            break
        if not items:
            page = 1
            break
        page += 1
        for it in items:
            web = ""
            for ln in (it.get("links") or []):
                if isinstance(ln, dict) and ln.get("type") == "website" \
                        and ln.get("value"):
                    web = ln["value"]
                    break
            if not web:
                continue
            name = ""
            names = it.get("names") or []
            for nm in names:
                if "ror_display" in (nm.get("types") or []):
                    name = nm.get("value", "")
                    break
            if not name:
                for nm in names:
                    if "label" in (nm.get("types") or []):
                        name = nm.get("value", "")
                        break
            locs = it.get("locations") or []
            iso = ""
            if locs and isinstance(locs[0], dict):
                geo = locs[0].get("geonames_details") or {}
                iso = (geo.get("country_code") or "")
            out.append({"name": name or web, "url": web,
                        "iso2": iso.upper()[:2], "type_hint": "university",
                        "source": f"ror:api-p{page - 1}"})
            if len(out) >= per_run:
                break
        if len(out) >= per_run:
            break
    _set_cursor(state, "ror_page", page)
    return out


def discover_openalex(url, state, per_run, timeout=30, mailto: str = ""):
    contact = mailto or DEFAULT_MAILTO
    page = _cursor(state, "openalex_page", 1) or 1
    out: list = []
    remaining = per_run
    # OpenAlex caps per_page at 200; walk pages until per_run is met.
    for _ in range(5):
        if remaining <= 0:
            break
        try:
            r = _get(url, timeout, params={
                "filter": "type:education",
                "select": "id,display_name,country_code,type,homepage_url,ror",
                "per_page": min(remaining, 200), "page": page,
                "mailto": contact}, headers={"Accept": "application/json"})
            if r.status_code != 200:
                return out
            results = r.json().get("results", [])
        except Exception:
            return out
        if not results:
            _set_cursor(state, "openalex_page", 1)
            return out
        _set_cursor(state, "openalex_page", page + 1)
        page += 1
        for e in results[:remaining]:
            web = e.get("homepage_url") or ""
            if not web:
                continue
            out.append({"name": e.get("display_name", web), "url": web,
                        "iso2": (e.get("country_code") or "").upper(),
                        "type_hint": "university",
                        "source": f"openalex:page{page - 1}"})
        remaining = per_run - len(out)
    return out


def discover_wikidata(url, state, per_run, timeout=40):
    off = _cursor(state, "wikidata_offset", 0)
    q = (f"SELECT ?item ?itemLabel ?website ?iso WHERE {{ "
         f"VALUES ?type {{ wd:Q3918 wd:Q38723 wd:Q2385804 }} "
         f"?item wdt:P31 ?type . ?item wdt:P856 ?website . "
         f"OPTIONAL {{ ?item wdt:P17 ?c . ?c wdt:P297 ?iso . }} "
         f"SERVICE wikibase:label {{ bd:serviceParam wikibase:language \"en\". }} }} "
         f"ORDER BY ?item "
         f"LIMIT {min(per_run, 300)} OFFSET {off}")
    try:
        r = _get(url, timeout, params={"query": q, "format": "json"},
                 headers={"Accept": "application/sparql-results+json"})
        if r.status_code != 200:
            return []
        bindings = r.json().get("results", {}).get("bindings", [])
    except Exception:
        return []
    if not bindings:
        _set_cursor(state, "wikidata_offset", 0)
        return []
    _set_cursor(state, "wikidata_offset", off + len(bindings))
    out = []
    for b in bindings:
        web = b.get("website", {}).get("value", "")
        name = b.get("itemLabel", {}).get("value", "")
        iso = b.get("iso", {}).get("value", "").upper()
        if web and name and not name.startswith("Q"):
            out.append({"name": name, "url": web, "iso2": iso,
                        "type_hint": "university",
                        "source": "wikidata:P856"})
    return out


def _resolve_scorecard_zip(configured_url: str, state: dict, timeout: int = 30) -> str:
    """Resolve the dated Scorecard zip URL, caching for 24h to avoid scraping
    the data page on every run."""
    now = time.time()
    cached = state.get("cursors", {}).get("scorecard_zip_url", "")
    ts = float(state.get("cursors", {}).get("scorecard_zip_ts", 0) or 0)
    if cached and (now - ts) < 86400:
        return cached
    zip_url = configured_url
    try:
        page = _get("https://collegescorecard.ed.gov/data", 30)
        if page.status_code == 200:
            m = re.search(
                r'(https://ed-public-download\.scorecard\.network/downloads/'
                r'Most-Recent-Cohorts-Institution_[^"\']*\.zip)', page.text)
            if m:
                zip_url = m.group(1)
    except Exception:
        pass
    if zip_url:
        state.setdefault("cursors", {})["scorecard_zip_url"] = zip_url
        state.setdefault("cursors", {})["scorecard_zip_ts"] = now
    return zip_url


def discover_scorecard(url, state, per_run, timeout=120):
    # Bulk "Most Recent Institution-Level Data" zip (~23MB, 6k US schools,
    # INSTURL column). The download URL is dated per release, so resolve it
    # from the data page (cached 24h); fall back to the configured URL.
    zip_url = _resolve_scorecard_zip(url, state)
    if not zip_url:
        return []
    try:
        r = _get(zip_url, timeout, stream=True)
        if r.status_code != 200:
            return []
        # Stream with a 40MB cap to stay in free-tier.
        buf = io.BytesIO()
        size = 0
        for chunk in r.iter_content(65536):
            if not chunk:
                continue
            buf.write(chunk)
            size += len(chunk)
            if size > 40_000_000:
                break
        content = buf.getvalue()
        if content[:2] != b"PK":
            return []
        zf = zipfile.ZipFile(io.BytesIO(content))
        names = [n for n in zf.namelist()
                 if n.lower().endswith(".csv") and "__MACOSX" not in n]
        if not names:
            return []
        names.sort(key=lambda n: (0 if "institution" in n.lower() else 1, n))
        with zf.open(names[0]) as f:
            text = f.read().decode("utf-8", errors="replace")
        rows = list(csv.DictReader(text.splitlines()))
    except Exception:
        return []
    if not rows:
        return []
    cols = {c.lower(): c for c in rows[0].keys()}
    name_c = next((cols[c] for c in cols if c in ("instnm", "school.name", "name")), None)
    url_c = next((cols[c] for c in cols if "url" in c or "web" in c or "schurl" in c), None)
    if not url_c:
        return []
    off = _cursor(state, "scorecard_offset", 0)
    chunk = rows[off:off + per_run * 2]
    if rows:
        _advance_circular(state, "scorecard_offset", off, len(chunk), len(rows))
    out = []
    for row in chunk:
        web = (row.get(url_c) or "").strip()
        if web and "." in web:
            out.append({"name": row.get(name_c, web) if name_c else web,
                        "url": web, "iso2": "US", "type_hint": "university",
                        "source": f"scorecard:{time.strftime('%Y-%m')}"})
        if len(out) >= per_run:
            break
    return out


def discover_france_annuaire(url, state, per_run, timeout=30):
    # ODS Explore API v2.1 returns flat records (max 100/page). Walk pages
    # until per_run is met. `web` holds the site and is often null, so
    # filter server-side to website-having rows only.
    off = _cursor(state, "france_offset", 0)
    out = []
    remaining = per_run
    for _ in range(5):
        if remaining <= 0:
            break
        try:
            r = _get(url, timeout, params={"limit": min(remaining, 100),
                                           "offset": off,
                                           "where": "web is not null"})
            if r.status_code != 200:
                return out
            recs = r.json().get("results", [])
        except Exception:
            return out
        if not recs:
            _set_cursor(state, "france_offset", 0)
            return out
        _set_cursor(state, "france_offset", off + len(recs))
        off += len(recs)
        for rec in recs:
            f = rec.get("fields", rec) if isinstance(rec, dict) else {}
            if not isinstance(f, dict):
                continue
            web = f.get("web") or f.get("site_web") or f.get("site") or ""
            name = f.get("nom_etablissement") or f.get("nom") or web
            if web and "." in str(web):
                out.append({"name": name, "url": str(web), "iso2": "FR",
                            "type_hint": "k-12",
                            "source": f"fr-annuaire:{time.strftime('%Y-%m-%d')}"})
        remaining = per_run - len(out)
        # Only stop early when the API signals exhaustion (empty page).
        # A short page (<100) can still precede more rows when filtered
        # server-side, so keep paging until per_run or empty.
    return out


def discover_osm(url, state, per_run, timeout=60, boxes=None):
    _boxes = boxes or OSM_BOXES
    idx = _next_rotation(state, "osm_idx", len(_boxes))
    label, s, w, n, e = _boxes[idx % len(_boxes)]
    q = (f'[out:json][timeout:40];(node["amenity"~"school|college|university"]'
         f'["website"]({s},{w},{n},{e});way["amenity"~"school|college|university"]'
         f'["website"]({s},{w},{n},{e}););out tags {min(per_run,200)};')
    els: list = []
    for attempt in range(3):
        try:
            rr = requests.post(url, data={"data": q}, headers=dict(UA),
                               timeout=timeout)
            if rr.status_code in (429, 502, 504):
                time.sleep(min(2 ** attempt, 4))
                continue
            if rr.status_code != 200:
                return []
            els = rr.json().get("elements", [])
            break
        except Exception:
            try:
                time.sleep(2)
            except Exception:
                pass
    out = []
    for el in els[:per_run]:
        t = el.get("tags", {}) if isinstance(el, dict) else {}
        web = t.get("website") or t.get("contact:website") or ""
        name = t.get("name", web)
        if web and "." in web:
            kind = t.get("amenity", "school")
            out.append({"name": name, "url": web, "iso2": "",
                        "type_hint": "k-12" if kind == "school" else "university",
                        "source": f"osm:{label}"})
    return out


def discover_whed(url, state, per_run, timeout=30):
    # Polite gap-filler: list page for one rotating country, then <=per_run
    # detail pages. Detail links carry opaque tokens (NOT the IAU id), so zip
    # them with the ids in page order; the site shows the official website
    # after a "WWW:" label. Cites Global WHED IDs; respects ToS (no bulk copy).
    idx = _next_rotation(state, "whed_idx", len(WHED_COUNTRIES))
    country = WHED_COUNTRIES[idx % len(WHED_COUNTRIES)]
    try:
        r = _get("https://whed.net/results_institutions.php",
                 timeout, params={"Chp1": country})
        if r.status_code != 200:
            return []
        ids = re.findall(r"(IAU-\d{6})", r.text)
        hrefs = re.findall(r'href="([^"]*detail_institution[^"]*)"',
                           r.text, re.I)
        # Align by order; if counts mismatch, fall back to id-only (the
        # detail URL pattern below still resolves).
        pairs = list(zip(ids, hrefs))[:per_run] or \
            [(gid, "") for gid in ids[:per_run]]
        if len(ids) != len(hrefs):
            pairs = [(gid, href if i < len(hrefs) else "")
                     for i, (gid, href) in enumerate(pairs)]
    except Exception:
        return []
    out, seen = [], set()
    for gid, href in pairs:
        if gid in seen:
            continue
        seen.add(gid)
        time.sleep(1)
        try:
            if href.startswith("/"):
                href = "https://whed.net" + href
            detail_url = href if href.startswith("http") else (
                f"https://whed.net/institutions/{gid}")
            d = _get(detail_url, timeout)
            if d.status_code != 200:
                continue
            m = re.search(
                r'WWW:</span>\s*<span[^>]*>\s*<a[^>]+href="(https?://[^"]+)"',
                d.text, re.I)
            if not m:
                m = re.search(
                    r'<a[^>]+href="(https?://[^"]+)"[^>]*>\s*https?://',
                    d.text, re.I)
            web = m.group(1) if m else ""
            nm = re.search(r"<h[12][^>]*>([^<]{4,140})<", d.text)
            if web and "." in web and "whed.net" not in web:
                out.append({"name": nm.group(1).strip() if nm else gid,
                            "url": web, "iso2": "",
                            "type_hint": "university", "source": f"whed:{gid}"})
        except Exception:
            continue
        if len(out) >= per_run:
            break
    return out


def discover_dotgov(url, state, per_run, timeout=60):
    # CISA .gov zone list (CC0, daily): filter the 72 "School district"
    # domains. Small file — full scan each session, dedupe handles repeats.
    try:
        r = _get(url or "https://raw.githubusercontent.com/cisagov/"
                 "dotgov-data/main/current-full.csv", timeout)
        if r.status_code != 200:
            return []
        rows = list(csv.DictReader(r.text.splitlines()))
    except Exception:
        return []
    out = []
    for row in rows:
        if (row.get("Domain type") or "").strip().lower() != "school district":
            continue
        dom = (row.get("Domain name") or "").strip().lower()
        name = (row.get("Organization name") or "").strip() or dom
        if dom and "." in dom:
            out.append({"name": name, "url": f"https://{dom}", "iso2": "US",
                        "type_hint": "k-12",
                        "source": f"dotgov:{time.strftime('%Y-%m-%d')}"})
        if len(out) >= per_run:
            break
    return out


def discover_cricos(url, state, per_run, timeout=120,
                    package_id: str = "e5ae7059-bfa8-4fa4-a5c0-c13cf3520193",
                    resource_name: str = "CRICOS Institutions.csv"):
    # Australian CRICOS register via data.gov.au CKAN (CC-BY 2.5 AU):
    # resolve the resource dynamically (name/format match).
    try:
        pkg = _get("https://data.gov.au/data/api/3/action/package_show",
                   30, params={"id": package_id})
        if pkg.status_code != 200:
            return []
        res = pkg.json().get("result", {}).get("resources", [])
        csv_url = ""
        for x in res:
            if (x.get("name") or "") == resource_name \
                    and (x.get("format") or "").upper() == "CSV":
                csv_url = x.get("url", "")
                break
        if not csv_url:
            return []
        r = _get(csv_url, timeout)
        if r.status_code != 200:
            return []
        rows = list(csv.DictReader(
            r.text.replace("\ufeff", "").splitlines()))
    except Exception:
        return []
    off = _cursor(state, "cricos_offset", 0)
    chunk = rows[off:off + per_run * 2] if rows else []
    if rows:
        _advance_circular(state, "cricos_offset", off, len(chunk), len(rows))
    out = []
    for row in chunk:
        web = (row.get("Website") or "").strip()
        name = (row.get("Institution Name") or "").strip() \
            or (row.get("Trading Name") or "").strip() or web
        if web and "." in web:
            out.append({"name": name, "url": web, "iso2": "AU",
                        "type_hint": "",
                        "source": f"cricos:{time.strftime('%Y-%m-%d')}"})
        if len(out) >= per_run:
            break
    return out


NUC_PAGES = [
    ("federal", "https://www.nuc.edu.ng/nigerian-univerisities/"
                "federal-univeristies"),
    ("state", "https://www.nuc.edu.ng/nigerian-univerisities/"
              "state-univerisity"),
    ("private", "https://www.nuc.edu.ng/nigerian-univerisities/"
                "private-univeristies"),
]


def discover_nuc_ng(url, state, per_run, timeout=60):
    # Nigeria NUC lists (~300 universities) with WEBSITE ADDRESS tables.
    # NOTE: the live site uses misspelled slugs ("univerisities" etc) — keep
    # them as-is; correcting the spelling 404s.
    out = []
    pages = NUC_PAGES
    if url and "nuc.edu.ng" not in (url or ""):
        pass  # configured URL is informational; slugs above are canonical
    for tag, page_url in pages:
        try:
            r = _get(page_url, timeout)
            if r.status_code != 200:
                continue
            tables = re.findall(r"<table.*?</table>", r.text, re.I | re.S)
            for t in tables:
                # Require a header mentioning website to avoid parsing
                # unrelated tables on the page.
                if not re.search(r"websit|url|domain", t, re.I):
                    continue
                for row in re.findall(r"<tr.*?>(.*?)</tr>", t, re.I | re.S):
                    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in
                             re.findall(r"<t[dh].*?>(.*?)</t[dh]>", row,
                                        re.I | re.S)]
                    if len(cells) < 4:
                        continue
                    name, web = cells[1], cells[3]
                    m = re.search(r"https?://[^\s\"'<>]+", web)
                    if m:
                        web = m.group(0).rstrip(".,;)")
                    if name and web and "." in web:
                        out.append({"name": name, "url": web, "iso2": "NG",
                                    "type_hint": "university",
                                    "source": f"nuc-ng:{tag}"})
                    if len(out) >= per_run:
                        return out
        except Exception:
            continue
        time.sleep(1)
    return out


def discover_nz_schools(url, state, per_run, timeout=60,
                        resource_id: str = "4b292323-9fcc-41f8-814b-3c7b19cf14b3"):
    # NZ Schools Directory via catalogue.data.govt.nz CKAN datastore
    # (CC-BY 4.0): Org_Name + URL columns, paged by offset cursor.
    off = _cursor(state, "nz_offset", 0)
    try:
        r = _get("https://catalogue.data.govt.nz/api/3/action/"
                 "datastore_search", timeout,
                 params={"resource_id": resource_id,
                         "limit": min(per_run, 500), "offset": off})
        if r.status_code != 200:
            return []
        res = r.json().get("result", {})
        recs = res.get("records", [])
        total = res.get("total", 0)
    except Exception:
        return []
    if recs and total:
        _advance_circular(state, "nz_offset", off, len(recs), total)
    out = []
    for rec in recs:
        if not isinstance(rec, dict):
            continue
        web = str(rec.get("URL") or "").strip()
        name = str(rec.get("Org_Name") or "").strip() or web
        if web and "." in web:
            out.append({"name": name, "url": web, "iso2": "NZ",
                        "type_hint": "k-12",
                        "source": f"nz-schools:{time.strftime('%Y-%m-%d')}"})
    return out


def discover_deqar(url, state, per_run, timeout=60):
    # DEQAR daily institutions CSV (~3MB, PDDL public domain):
    # country (English name), name_primary, website_link, deqar_id.
    # Offset cursor over data rows; small file, full fetch each session.
    csv_url = url or "https://backend.deqar.eu/static/daily-csv/deqar-institutions.csv"
    try:
        r = _get(csv_url, timeout)
        if r.status_code != 200:
            return []
        rows = list(csv.DictReader(r.text.splitlines()))
    except Exception:
        return []
    if not rows:
        return []
    off = _cursor(state, "deqar_offset", 0)
    chunk = rows[off:off + per_run * 2]
    _advance_circular(state, "deqar_offset", off, len(chunk), len(rows))
    out = []
    for row in chunk:
        web = (row.get("website_link") or "").strip()
        name = (row.get("name_primary") or "").strip() or web
        iso = DEQAR_COUNTRY_ISO.get((row.get("country") or "").strip(), "")
        if web and "." in web:
            out.append({"name": name, "url": web, "iso2": iso,
                        "type_hint": "university",
                        "source": f"deqar:{time.strftime('%Y-%m-%d')}"})
        if len(out) >= per_run:
            break
    return out


def _resolve_ipeds_zip(configured_url: str, state: dict) -> str:
    """IPEDS HD file is year-stamped (HD2024.zip); roll back up to 2 years
    when the configured year 404s after the annual release cycle."""
    now = time.time()
    cached = state.get("cursors", {}).get("ipeds_zip_url", "")
    ts = float(state.get("cursors", {}).get("ipeds_zip_ts", 0) or 0)
    if cached and (now - ts) < 86400:
        return cached
    cands = [configured_url] if configured_url else []
    m = re.search(r"HD(\d{4})\.zip", configured_url or "", re.I)
    if m:
        year = int(m.group(1))
        for y in (year - 1, year - 2):
            cands.append(re.sub(r"HD\d{4}\.zip", f"HD{y}.zip",
                                configured_url, flags=re.I))
    zip_url = ""
    for u in cands:
        try:
            r = _get(u, 30, stream=True)
            if r.status_code == 200:
                zip_url = u
                break
        except Exception:
            continue
    if zip_url:
        state.setdefault("cursors", {})["ipeds_zip_url"] = zip_url
        state.setdefault("cursors", {})["ipeds_zip_ts"] = now
        return zip_url
    return configured_url


def discover_ipeds(url, state, per_run, timeout=120):
    # NCES IPEDS HD directory zip (~1MB, US public domain):
    # INSTNM (name) + WEBADDR (website). Offset cursor over data rows.
    zip_url = _resolve_ipeds_zip(
        url or "https://nces.ed.gov/ipeds/datacenter/data/HD2024.zip", state)
    if not zip_url:
        return []
    try:
        r = _get(zip_url, timeout, stream=True)
        if r.status_code != 200:
            return []
        buf = io.BytesIO()
        size = 0
        for chunk in r.iter_content(65536):
            if not chunk:
                continue
            buf.write(chunk)
            size += len(chunk)
            if size > 40_000_000:
                break
        content = buf.getvalue()
        if content[:2] != b"PK":
            return []
        zf = zipfile.ZipFile(io.BytesIO(content))
        names = [n for n in zf.namelist()
                 if n.lower().endswith(".csv") and "__MACOSX" not in n]
        if not names:
            return []
        names.sort(key=lambda n: (0 if n.lower().startswith("hd") else 1, n))
        with zf.open(names[0]) as f:
            text = f.read().decode("utf-8", errors="replace")
        rows = list(csv.DictReader(text.splitlines()))
    except Exception:
        return []
    if not rows:
        return []
    cols = {c.lower(): c for c in rows[0].keys()}
    name_c = cols.get("instnm")
    url_c = cols.get("webaddr")
    if not name_c or not url_c:
        return []
    off = _cursor(state, "ipeds_offset", 0)
    chunk = rows[off:off + per_run * 2]
    _advance_circular(state, "ipeds_offset", off, len(chunk), len(rows))
    out = []
    for row in chunk:
        web = (row.get(url_c) or "").strip()
        name = (row.get(name_c) or "").strip() or web
        if web and "." in web:
            out.append({"name": name, "url": web, "iso2": "US",
                        "type_hint": "university",
                        "source": f"ipeds:{time.strftime('%Y-%m')}"})
        if len(out) >= per_run:
            break
    return out
