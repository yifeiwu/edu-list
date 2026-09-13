"""Validation v2: homepage-only, free-tier safe.

Rules (locked spec, strict-TLS revision):
- Final HTTP status non-2xx (after redirects) => Inaccessible. No exceptions.
- TLS errors (expired/self-signed/broken chain) => Inaccessible. Every
  legitimate institution is expected to serve valid TLS; we no longer fall
  back to verify=False.
- Transient transport failures (ConnectionError/Timeout) are retried once
  with backoff; persistent failures => Inaccessible.
- Social-only / builder-placeholder => Inaccessible (not a real website).
- Parking / soft-404 / empty => Inaccessible.
- Else score content signals; confidence >= threshold => Active.
- Cross-domain moves (HTTP redirect or meta-refresh to a different
  registrable base) are reported as `moved_to` so the caller can mark the
  old domain `moved-to:<new>` and validate the target as its own row
  (rebrands like unochapeco.edu.br -> uno.edu.br must not be misattributed).
  Same-site redirects (apex<->www, http->https, subpath) are NOT moves.

Returns a dict with status, confidence, reason, codes for state tracking.
CSV keeps only (school_name,web_domain,type,last_visited,status,sources).
"""
from __future__ import annotations

import re
import time
import urllib.parse as urlparse
from collections.abc import Callable

import requests

from .util import (
    CANONICAL_RE, H1_RE, ICON_RE, PARKING_RES, SCHEMA_RE, SOFT404_RES,
    TAG_RE, TITLE_RE, is_academic_suffix, is_service_host,
    is_social_or_builder, keywords_for_country, normalize_domain,
    registrable_base, same_site,
)

PARKING_RE_C = [re.compile(p, re.I) for p in PARKING_RES]
SOFT404_RE_C = [re.compile(p, re.I) for p in SOFT404_RES]
STRUCTURAL_RES = [re.compile(p, re.I) for p in
                  [r"/admissions", r"/academics", r"/facult", r"/programmes?",
                   r"/courses?", r"/contact", r"©\s*20\d{2}", r"all rights reserved"]]
META_REFRESH_RE = re.compile(
    r'<meta[^>]+http-equiv=["\']?refresh["\']?[^>]*'
    r'content=["\']?\s*\d+\s*;\s*url=(.*?)(?:["\'\s>]|$)',
    re.I | re.S)
NOSCRIPT_RE = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.I | re.S)
# Keyword/visible-text signals scan up to 1MB of body (plain substring search
# + two linear tag-strips, milliseconds) to cover JS-bundled portals whose
# strings sit at the end of huge <head> blocks. Pattern-heavy checks stay on
# the slice. Downloads are capped at the same bound via streaming.
FULL_SCAN_MAX = 1000000


def _visible(html: str) -> tuple[str, str, str]:
    m_t = TITLE_RE.search(html or "")
    m_h = H1_RE.search(html or "")
    title = TAG_RE.sub(" ", m_t.group(1)).strip() if m_t else ""
    h1 = TAG_RE.sub(" ", m_h.group(1)).strip() if m_h else ""
    return title, h1, (title + " " + h1).strip()


def _moved_to(domain: str, final_host: str | None) -> str | None:
    """Registrable host the site moved to, or None if effectively same site.

    Same registrable base (apex<->www, http->https, case) is NOT a move.
    Subdomain->apex on the same base (student.X -> X) is also not a move;
    the fetched content still belongs to this institution.
    """
    if not final_host or "." not in final_host:
        return None
    fh = final_host.lower().strip(".").removeprefix("www.")
    dom = domain.lower().strip(".").removeprefix("www.")
    if fh == dom:
        return None
    if normalize_domain(fh) is None:
        return None
    if same_site(dom, fh):
        return None
    # Report the registrable-normalized target host (lowercased, no www).
    return fh


def _read_limited(resp: requests.Response, limit: int) -> str:
    """Read at most `limit` chars of response body via streaming."""
    chunks: list[bytes] = []
    size = 0
    try:
        for chunk in resp.iter_content(chunk_size=32768):
            if not chunk:
                continue
            chunks.append(chunk)
            size += len(chunk)
            if size >= limit:
                break
    except Exception:
        pass
    raw = b"".join(chunks)[:limit]
    enc = resp.encoding or "utf-8"
    try:
        return raw.decode(enc, errors="replace")
    except Exception:
        return raw.decode("utf-8", errors="replace")


def validate_site(url: str, domain: str, country_iso: str, timeout: int,
                  user_agent: str, max_bytes: int,
                  multisource: bool = False,
                  politeness: float = 0.4,
                  active_threshold: int = 50,
                  sleep_fn: Callable[[float], None] | None = None,
                  retries: int = 1,
                  retry_backoff: float = 1.0) -> dict:
    _sleep = sleep_fn or time.sleep

    def _polite() -> None:
        if politeness and politeness > 0:
            try:
                _sleep(politeness)
            except Exception:
                pass

    def _backoff() -> None:
        if retry_backoff and retry_backoff > 0:
            try:
                _sleep(retry_backoff)
            except Exception:
                pass

    headers = {"User-Agent": user_agent, "Accept": "text/html,*/*",
               "Accept-Language": "en;q=0.8"}
    try:
        parts = urlparse.urlparse(url if "://" in url else "https://" + url)
        host = parts.hostname or domain
        scheme = parts.scheme or "https"
        home = f"{scheme}://{host}/"
    except Exception:
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "bad-url", "code": 0, "final_domain": domain,
                "moved_to": None}

    if is_social_or_builder(domain):
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "social-only/placeholder", "code": 0,
                "final_domain": domain, "moved_to": None}
    # Single immediate retry for transient transport failures
    # (ConnectionError/Timeout, e.g. reset, DNS blip, read timeout).
    # SSLError is NOT transient (strict TLS) and HTTP error statuses are
    # valid responses — neither is retried here.
    g = None
    ssl_error = None
    for attempt in range(max(int(retries), 0) + 1):
        try:
            g = requests.get(home, headers=headers, timeout=timeout,
                             allow_redirects=True, stream=True)
            ssl_error = None
            break
        except requests.exceptions.SSLError as e:
            ssl_error = e
            break
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout) as e:
            _polite()
            if attempt >= max(int(retries), 0):
                kind = type(e).__name__
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": f"fetch-error:{kind}", "code": 0,
                        "final_domain": domain, "moved_to": None}
            _backoff()
            continue
        except requests.RequestException as e:
            _polite()
            kind = type(e).__name__
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": f"fetch-error:{kind}", "code": 0,
                    "final_domain": domain, "moved_to": None}
        except Exception as e:  # noqa: BLE001 - boundary guard
            _polite()
            kind = type(e).__name__
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": f"fetch-error:{kind}", "code": 0,
                    "final_domain": domain, "moved_to": None}
    if ssl_error is not None:
        # Strict TLS: broken/expired/self-signed chains are Inaccessible.
        # Legitimate institutions serve valid TLS; unverified fetches risk
        # MITM and misattribution, so we never fall back to verify=False.
        # One www-variant retry covers apex-vs-www cert mismatches.
        ssl_kind = type(ssl_error).__name__
        _polite()
        bare = host.lower().removeprefix("www.")
        if not host.lower().startswith("www."):
            try:
                g = requests.get(f"{scheme}://www.{bare}/", headers=headers,
                                 timeout=timeout, allow_redirects=True,
                                 stream=True)
            except requests.exceptions.SSLError:
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": "fetch-error:SSLError", "code": 0,
                        "final_domain": domain, "moved_to": None}
            except requests.RequestException as e2:
                _polite()
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": f"fetch-error:{type(e2).__name__}",
                        "code": 0, "final_domain": domain, "moved_to": None}
            except Exception as e2:  # noqa: BLE001 - boundary guard
                _polite()
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": f"fetch-error:{type(e2).__name__}",
                        "code": 0, "final_domain": domain, "moved_to": None}
        else:
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": f"fetch-error:{ssl_kind}",
                    "code": 0, "final_domain": domain, "moved_to": None}
    if g is None:
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "fetch-error:ConnectionError", "code": 0,
                "final_domain": domain, "moved_to": None}
    # Fetch chain done: g is a real response from here on.
    try:
        code = g.status_code
        final_host = (urlparse.urlparse(g.url).hostname or domain).lower()
        final_host = final_host.strip(".").removeprefix("www.")
        moved = _moved_to(domain, final_host)
        ctype = g.headers.get("Content-Type", "text/html")
        if code < 200 or code >= 300:
            _polite()
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"http-{code}", "code": code,
                    "final_domain": final_host, "moved_to": moved}
        if "html" not in ctype.lower():
            _polite()
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"non-html:{ctype[:40]}", "code": code,
                    "final_domain": final_host, "moved_to": moved}
        # Redirect landing on a social/parked host is not the school's site.
        if moved and is_social_or_builder(moved):
            _polite()
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"moved-to-social:{moved}", "code": code,
                    "final_domain": final_host, "moved_to": moved}
        full_text = _read_limited(g, FULL_SCAN_MAX)
        html = full_text[:max_bytes] if full_text else ""
        _polite()
    finally:
        try:
            g.close()
        except Exception:
            pass

    if not html or len(html.strip()) < 200:
        return {"status": "Inaccessible", "confidence": 5,
                "reason": "empty-body", "code": code,
                "final_domain": final_host, "moved_to": moved}

    # Meta-refresh hop to another host: same as an HTTP move (requests does
    # not follow these). Don't score the placeholder page as the school.
    mm = META_REFRESH_RE.search(html[:8000])
    if mm:
        target = normalize_domain(mm.group(1).strip().strip("'\""))
        if target and not same_site(target, domain):
            if is_social_or_builder(target):
                return {"status": "Inaccessible", "confidence": 5,
                        "reason": f"moved-to-social:{target}", "code": code,
                        "final_domain": final_host, "moved_to": target}
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": f"moved-meta:{target}", "code": code,
                    "final_domain": final_host, "moved_to": target}

    low = html.lower()
    title, h1, visible = _visible(html)
    vlow = visible.lower()

    for rx in SOFT404_RE_C:
        if rx.search(vlow) or rx.search(low[:2000]):
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "soft-404/block-page", "code": code,
                    "final_domain": final_host, "moved_to": moved}
    for rx in PARKING_RE_C:
        if rx.search(vlow) or rx.search(low[:4000]):
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "parking", "code": code,
                    "final_domain": final_host, "moved_to": moved}
    # Parking heuristic: almost all text is links + lots of external refs.
    # Exempted when title/H1 already declares an educational institution —
    # real portals open with link-heavy navs too (e.g. 115 words / 41 links
    # in Stanford's first 32KB). Parked pages never reach here anyway:
    # the parking check above returns first.
    text = TAG_RE.sub(" ", html)
    words = text.split()
    links = re.findall(r"<a\s", html, re.I)
    if len(words) < 120 and len(links) > 25 and not any(
            k in vlow for k in keywords_for_country(country_iso)):
        return {"status": "Inaccessible", "confidence": 10,
                "reason": "parking-linkfarm", "code": code,
                "final_domain": final_host, "moved_to": moved}

    conf, reasons = 20, ["http-2xx-html"]  # reachable baseline
    if multisource:
        conf += 30
        reasons.append("multi-source")
    if SCHEMA_RE.search(html):
        conf += 25
        reasons.append("schema.org-edu")
    # Keyword search must cover the whole body: modern portal/SPAs bury all
    # visible strings at the end of huge <head> bundles, past any slice.
    kws = keywords_for_country(country_iso)
    body_low = full_text.lower()
    hay = (vlow + " " + low[:4000])
    if any(k in hay for k in kws) or any(k in body_low for k in kws):
        conf += 20
        reasons.append("edu-keywords")
    struct_hits = sum(1 for rx in STRUCTURAL_RES if rx.search(html))
    if CANONICAL_RE.search(html):
        struct_hits += 1
    if ICON_RE.search(html):
        struct_hits += 1
    if struct_hits >= 2:
        conf += 10
        reasons.append("structure")
    elif is_academic_suffix(domain):
        conf += 10
        reasons.append("trusted-suffix")
    # Substantial real copy (scripts/styles stripped): portals render lots
    # of text even when title/H1 are generic. Parking landings are thin or
    # linkfarms (filtered above), so this rarely misfires — and discovery
    # provenance (ministry lists, ROR, …) already ties the domain to a school.
    # (Skipped when hard parking phrases appear anywhere in the body.)
    vis_words = TAG_RE.sub(
        " ", NOSCRIPT_RE.sub(" ", full_text)).split()
    if len(vis_words) >= 300 and not any(
            p in body_low for p in
            ("buy this domain", "domain for sale", "parked free",
             "sedo.com", "godaddy", "domain parking", "this site is parked")):
        conf += 10
        reasons.append("substantial-content")

    # Base for move-target comparison (registrable, for stable reason suffix).
    if moved:
        reasons.append(f"moved-to:{registrable_base(moved)}"
                       if registrable_base(moved) != moved
                       else f"moved-to:{moved}")
    # Service endpoints (webmail, LMS, meeting links) are never the
    # institution's website: force Inaccessible regardless of threshold so a
    # lowered `active_threshold` can never promote them (see spotcheck
    # `mail2.sysu.edu.cn Active` regression).
    if is_service_host(domain) or (moved and is_service_host(moved)):
        conf = min(conf, 40)
        reasons.append("service-host")
        return {"status": "Inaccessible", "confidence": conf,
                "reason": "low-confidence:" + "+".join(reasons), "code": code,
                "final_domain": final_host, "moved_to": moved}
    # Cross-domain moves are pointers, never the site itself: the old domain
    # is Inaccessible here; the caller (`verify._mark_moved`/`_handle_move`)
    # records the pointer and validates the target as its own row. This
    # matches meta-refresh handling above and avoids Active+moved rows that
    # previously leaked into spotcheck logs.
    if moved:
        conf = min(conf, 40)
        return {"status": "Inaccessible", "confidence": conf,
                "reason": "+".join(reasons), "code": code,
                "final_domain": final_host, "moved_to": moved}
    conf = min(conf, 100)
    if conf >= active_threshold:
        return {"status": "Active", "confidence": conf,
                "reason": "+".join(reasons), "code": code,
                "final_domain": final_host, "moved_to": moved}
    return {"status": "Inaccessible", "confidence": conf,
            "reason": "low-confidence:" + "+".join(reasons), "code": code,
            "final_domain": final_host, "moved_to": moved}
