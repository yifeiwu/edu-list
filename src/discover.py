"""Discovery adapters — one function per source, all free-tier safe.

Every adapter: (cfg, state, per_run, timeout) -> list[Candidate].
Candidate: {name, url, iso2, type_hint, source}
All failures return [] (never crash a run). Cursors persist in state["cursors"].
"""
from __future__ import annotations

import csv
import io
import json
import re
import time
import zipfile

import requests

UA = {"User-Agent": "edu-domains-bot/1.0 (github-actions; educational-research)"}

# A few country boxes for OSM rotation (expand in sources.yaml later).
OSM_BOXES = [
    ("GB-London", 51.2, -0.6, 51.7, 0.3),
    ("US-NYC", 40.4, -74.3, 41.0, -73.6),
    ("FR-Paris", 48.7, 2.2, 49.0, 2.6),
    ("IN-Delhi", 28.4, 76.9, 28.9, 77.4),
]
CRTSH_SUFFIXES = ["edu.ng", "ac.uk", "edu.br", "edu.mx", "ac.in", "edu.in",
                  "ac.za", "edu.pk", "edu.ph", "edu.eg", "ac.ke", "edu.gh"]
WHED_COUNTRIES = ["Senegal", "Ghana", "Kenya", "Peru", "Vietnam", "Morocco"]


def _get(url, timeout=30, params=None, headers=None, stream=False):
    h = dict(UA)
    if headers:
        h.update(headers)
    return requests.get(url, params=params, headers=h, timeout=timeout, stream=stream)


def discover_hipo(url, state, per_run, timeout=30):
    off = int(state.get("cursors", {}).get("hipo_offset", 0))
    try:
        r = _get(url, timeout)
        if r.status_code != 200:
            return []
        data = r.json()
    except Exception:
        return []
    chunk = data[off:off + per_run]
    state.setdefault("cursors", {})["hipo_offset"] = (off + len(chunk)) % max(len(data), 1)
    out = []
    tag = time.strftime("%Y-%m-%d")
    for e in chunk:
        iso = (e.get("alpha_two_code") or "").upper()
        for d in (e.get("domains") or [])[:2]:
            out.append({"name": e.get("name", d), "url": f"https://{d}",
                        "iso2": iso, "type_hint": "university",
                        "source": f"hipo:{tag}"})
    return out


def discover_ror(url, state, per_run, timeout=30):
    page = int(state.get("cursors", {}).get("ror_page", 1))
    try:
        r = _get(url, timeout, params={"filter": "types:Education",
                                       "page": page, "size": min(per_run, 100)},
                 headers={"Accept": "application/json"})
        if r.status_code != 200:
            return []
        items = r.json().get("items", [])
    except Exception:
        return []
    if not items:
        state.setdefault("cursors", {})["ror_page"] = 1
        return []
    state.setdefault("cursors", {})["ror_page"] = page + 1
    out = []
    for it in items[:per_run]:
        links = (it.get("links") or {})
        web = links.get("website") or (it.get("links") if isinstance(it.get("links"), str) else "")
        if isinstance(web, list):
            web = web[0] if web else ""
        if not web:
            continue
        locs = it.get("locations") or []
        iso = ""
        if locs and isinstance(locs[0], dict):
            geo = locs[0].get("geonames_details") or {}
            iso = (geo.get("country_code") or locs[0].get("country_code") or "")
        out.append({"name": it.get("name", web), "url": web,
                    "iso2": iso.upper()[:2], "type_hint": "university",
                    "source": f"ror:api-p{page}"})
    return out


def discover_openalex(url, state, per_run, timeout=30):
    page = int(state.get("cursors", {}).get("openalex_page", 1))
    try:
        r = _get(url, timeout, params={
            "filter": "type:education",
            "select": "id,display_name,country_code,type,homepage_url,ror",
            "per_page": min(per_run, 200), "page": page,
            "mailto": "edu-domains-bot@example.com"}, headers={"Accept": "application/json"})
        if r.status_code != 200:
            return []
        results = r.json().get("results", [])
    except Exception:
        return []
    if not results:
        state.setdefault("cursors", {})["openalex_page"] = 1
        return []
    state.setdefault("cursors", {})["openalex_page"] = page + 1
    out = []
    for e in results[:per_run]:
        web = e.get("homepage_url") or ""
        if not web:
            continue
        out.append({"name": e.get("display_name", web), "url": web,
                    "iso2": (e.get("country_code") or "").upper(),
                    "type_hint": "university",
                    "source": f"openalex:page{page}"})
    return out


def discover_wikidata(url, state, per_run, timeout=40):
    off = int(state.get("cursors", {}).get("wikidata_offset", 0))
    q = (f"SELECT ?item ?itemLabel ?website ?iso WHERE {{ "
         f"VALUES ?type {{ wd:Q3918 wd:Q38723 wd:Q2385804 }} "
         f"?item wdt:P31 ?type . ?item wdt:P856 ?website . "
         f"OPTIONAL {{ ?item wdt:P17 ?c . ?c wdt:P297 ?iso . }} "
         f"SERVICE wikibase:label {{ bd:serviceParam wikibase:language \"en\". }} }} "
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
        state.setdefault("cursors", {})["wikidata_offset"] = 0
        return []
    state.setdefault("cursors", {})["wikidata_offset"] = off + len(bindings)
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


def discover_csv_generic(url, state, per_run, source_id, timeout=60,
                         name_cols=("name", "school_name", "INSTNM", "nom"),
                         url_cols=("website", "web", "url", "SCHURL", "school_url",
                                   "site", "site_web", "View Website"),
                         iso_cols=("iso2", "country_code", "alpha_two_code", "pays")):
    """Best-effort CSV fetch (ETER/GIAS/FR-sup). Skips gracefully if unconfigured."""
    if not url:
        return []
    try:
        r = _get(url, timeout, stream=True)
        if r.status_code != 200:
            return []
        # Cap download to ~25MB to stay in free-tier.
        buf = io.BytesIO()
        for i, chunk in enumerate(r.iter_content(65536)):
            buf.write(chunk)
            if buf.tell() > 25_000_000:
                break
        buf.seek(0)
        text = buf.read().decode("utf-8", errors="replace")
    except Exception:
        return []
    try:
        rows = list(csv.DictReader(text.splitlines()))
    except Exception:
        return []
    out = []
    for row in rows[: per_run * 4]:
        low = {k.lower(): v for k, v in row.items()}
        name = next((low.get(c.lower(), "") for c in name_cols if low.get(c.lower())), "")
        web = next((low.get(c.lower(), "") for c in url_cols if low.get(c.lower())), "")
        iso = next((low.get(c.lower(), "") for c in iso_cols if low.get(c.lower())), "")
        if web and ("http" in web or "." in web):
            out.append({"name": name or web, "url": web,
                        "iso2": (iso or "").upper()[:2],
                        "type_hint": "university" if source_id in ("eter", "france-sup") else "k-12",
                        "source": f"{source_id}:{time.strftime('%Y-%m-%d')}"})
        if len(out) >= per_run:
            break
    return out


def discover_scorecard(url, state, per_run, timeout=120):
    if not url:
        return []
    try:
        r = _get(url, timeout)
        if r.status_code != 200 or not r.content[:2] == b"PK":
            return []
        zf = zipfile.ZipFile(io.BytesIO(r.content))
        # Pick the most recent institution-level csv inside.
        names = [n for n in zf.namelist() if n.lower().endswith(".csv")]
        if not names:
            return []
        names.sort()
        with zf.open(names[-1]) as f:
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
    off = int(state.get("cursors", {}).get("scorecard_offset", 0))
    chunk = rows[off:off + per_run * 2]
    state.setdefault("cursors", {})["scorecard_offset"] = (off + len(chunk)) % max(len(rows), 1)
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
    off = int(state.get("cursors", {}).get("france_offset", 0))
    try:
        r = _get(url, timeout, params={"limit": min(per_run, 100), "offset": off})
        if r.status_code != 200:
            return []
        recs = r.json().get("results", [])
    except Exception:
        return []
    if not recs:
        state.setdefault("cursors", {})["france_offset"] = 0
        return []
    state.setdefault("cursors", {})["france_offset"] = off + len(recs)
    out = []
    for rec in recs:
        f = rec.get("record", rec) if isinstance(rec, dict) else {}
        if isinstance(rec, dict) and "fields" in rec:
            f = rec["fields"]
        web = f.get("site_web") or f.get("site") or f.get("url") or ""
        name = f.get("nom_etablissement") or f.get("nom") or web
        if web and "." in str(web):
            out.append({"name": name, "url": str(web), "iso2": "FR",
                        "type_hint": "k-12",
                        "source": f"fr-annuaire:{time.strftime('%Y-%m-%d')}"})
    return out


def discover_ugc(url, state, per_run, timeout=30):
    # Polite: 1 index page per run, parse "View Website" hrefs.
    try:
        r = _get(url, timeout)
        if r.status_code != 200:
            return []
        hrefs = re.findall(r'href="([^"]+)"[^>]*>\s*View Website', r.text, re.I)
        names = re.findall(r"<td[^>]*>([^<]{4,120})</td>", r.text)
    except Exception:
        return []
    out = []
    for i, h in enumerate(hrefs[:per_run]):
        if h.startswith("/"):
            h = "https://www.ugc.gov.in" + h
        # UGC links often route via redirector; keep host if resolvable later.
        m = re.search(r"(https?%3A%2F%2F[^&\"']+|https?://[^\"'&\\s]+)", h, re.I)
        web = m.group(1) if m else h
        if "%3A" in web:
            try:
                import urllib.parse as up
                web = up.unquote(web)
            except Exception:
                pass
        if "." in web and "ugc.gov.in" not in web:
            out.append({"name": names[i] if i < len(names) else web,
                        "url": web, "iso2": "IN", "type_hint": "university",
                        "source": f"ugc-in:{time.strftime('%Y-%m-%d')}"})
    return out


def discover_osm(url, state, per_run, timeout=60):
    idx = int(state.get("cursors", {}).get("osm_idx", 0))
    label, s, w, n, e = OSM_BOXES[idx % len(OSM_BOXES)]
    state.setdefault("cursors", {})["osm_idx"] = idx + 1
    q = (f'[out:json][timeout:40];(node["amenity"~"school|college|university"]'
         f'["website"]({s},{w},{n},{e});way["amenity"~"school|college|university"]'
         f'["website"]({s},{w},{n},{e}););out tags {min(per_run,200)};')
    try:
        r = requests.post(url, data={"data": q}, headers=dict(UA), timeout=timeout)
        if r.status_code != 200:
            return []
        els = r.json().get("elements", [])
    except Exception:
        return []
    out = []
    for el in els[:per_run]:
        t = el.get("tags", {})
        web = t.get("website") or t.get("contact:website") or ""
        name = t.get("name", web)
        if web and "." in web:
            kind = t.get("amenity", "school")
            out.append({"name": name, "url": web, "iso2": "",
                        "type_hint": "k-12" if kind == "school" else "university",
                        "source": f"osm:{label}"})
    return out


def discover_crtsh(url, state, per_run, timeout=40):
    idx = int(state.get("cursors", {}).get("crtsh_idx", 0))
    suffix = CRTSH_SUFFIXES[idx % len(CRTSH_SUFFIXES)]
    state.setdefault("cursors", {})["crtsh_idx"] = idx + 1
    try:
        r = _get("https://crt.sh/", timeout,
                 params={"q": f"%.{suffix}", "output": "json"})
        if r.status_code != 200:
            return []
        data = r.json()
    except Exception:
        return []
    seen, out = set(), []
    for e in data:
        nv = e.get("name_value", "") or e.get("common_name", "")
        for line in str(nv).splitlines():
            d = line.strip().lower().removeprefix("*.")
            if d.endswith("." + suffix) and d not in seen and " " not in d:
                seen.add(d)
                out.append({"name": d, "url": f"https://{d}", "iso2": "",
                            "type_hint": "", "source": f"crtsh:{suffix}"})
                if len(out) >= per_run:
                    return out
    return out


def discover_whed(url, state, per_run, timeout=30):
    # Polite gap-filler: list page for one rotating country, then <=per_run
    # detail pages. Cites Global WHED IDs; respects ToS (no bulk copy).
    idx = int(state.get("cursors", {}).get("whed_idx", 0))
    country = WHED_COUNTRIES[idx % len(WHED_COUNTRIES)]
    state.setdefault("cursors", {})["whed_idx"] = idx + 1
    try:
        r = _get("https://whed.net/results_institutions.php",
                 timeout, params={"Chp1": country})
        if r.status_code != 200:
            return []
        # Prefer real detail links carrying the ID over bare ID regexes.
        hrefs = re.findall(r'href="([^"]*(?:detail_institution|institution)[^"]*)"',
                           r.text, re.I)
        ids = []
        for h in hrefs:
            m = re.search(r"(IAU-\d{6})", h)
            if m and m.group(1) not in ids:
                ids.append((m.group(1), h))
        if not ids:
            for gid in re.findall(r"(IAU-\d{6})", r.text):
                if gid not in [i for i, _ in ids]:
                    ids.append((gid, ""))
        ids = ids[:per_run]
    except Exception:
        return []
    out, seen = [], set()
    for gid, href in ids:
        if gid in seen:
            continue
        seen.add(gid)
        time.sleep(1)
        try:
            if href.startswith("/"):
                href = "https://whed.net" + href
            detail_url = href if href.startswith("http") else (
                "https://whed.net/detail_institution.php")
            params = None if href.startswith("http") else {"Jzgk": gid}
            d = _get(detail_url, timeout, params=params)
            if d.status_code != 200:
                continue
            m = re.search(r'href="(https?://[^"]+)"[^>]*>\s*(?:Website|www\.)', d.text, re.I)
            if not m:
                m = re.search(r"(https?://[A-Za-z0-9_.\-~:/?#@!$&'()*+,;=%]+)", d.text)
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


def discover_commoncrawl(url, state, per_run, timeout=30):
    suffixes = ["edu", "ac.uk", "edu.au", "ac.in"]
    idx = int(state.get("cursors", {}).get("cc_idx", 0))
    suffix = suffixes[idx % len(suffixes)]
    state.setdefault("cursors", {})["cc_idx"] = idx + 1
    try:
        info = _get("https://index.commoncrawl.org/collinfo.json", timeout).json()
        index = info[0]["id"]
        r = _get(f"https://index.commoncrawl.org/{index}-index", timeout,
                 params={"url": f"*.{suffix}", "output": "json",
                         "filter": ["status:200", "mime:text/html"],
                         "collapse": "urlkey", "limit": min(per_run, 500)})
        if r.status_code != 200:
            return []
        out, seen = [], set()
        for line in r.text.splitlines():
            try:
                u = json.loads(line).get("url", "")
                import urllib.parse as up
                h = (up.urlparse(u).hostname or "").lower().removeprefix("www.")
                if h and h not in seen and "." in h:
                    seen.add(h)
                    out.append({"name": h, "url": f"https://{h}", "iso2": "",
                                "type_hint": "", "source": f"commoncrawl:{index}"})
            except Exception:
                continue
        return out[:per_run]
    except Exception:
        return []


# Stubs: configured later (K-12 deferred or third-party ToS-gated).
def discover_stub(url, state, per_run, source_id=""):
    return []
