"""Validation v2: homepage-only, free-tier safe.

Rules (locked spec):
- Final HTTP status non-2xx (after redirects) => Inaccessible. No exceptions.
- Social-only / builder-placeholder => Inaccessible (not a real website).
- Parking / soft-404 / empty => Inaccessible.
- Else score content signals; confidence >= threshold => Active.

Returns a dict with status, confidence, reason, codes for state tracking.
CSV keeps only (school_name,web_domain,type,last_visited,status,sources).
"""
from __future__ import annotations

import re
import time
import urllib.parse as urlparse

import requests

from .util import (
    CANONICAL_RE, H1_RE, ICON_RE, PARKING_RES, SCHEMA_RE, SOFT404_RES,
    TAG_RE, TITLE_RE, is_social_or_builder, keywords_for_country,
)

PARKING_RE_C = [re.compile(p, re.I) for p in PARKING_RES]
SOFT404_RE_C = [re.compile(p, re.I) for p in SOFT404_RES]
STRUCTURAL_RES = [re.compile(p, re.I) for p in
                  [r"/admissions", r"/academics", r"/facult", r"/programmes?",
                   r"/courses?", r"/contact", r"©\s*20\d{2}", r"all rights reserved"]]


def _visible(html: str) -> tuple[str, str, str]:
    m_t = TITLE_RE.search(html or "")
    m_h = H1_RE.search(html or "")
    title = TAG_RE.sub(" ", m_t.group(1)).strip() if m_t else ""
    h1 = TAG_RE.sub(" ", m_h.group(1)).strip() if m_h else ""
    return title, h1, (title + " " + h1).strip()


def validate_site(url: str, domain: str, country_iso: str, timeout: int,
                  user_agent: str, max_bytes: int,
                  multisource: bool = False,
                  politeness: float = 0.4) -> dict:
    headers = {"User-Agent": user_agent, "Accept": "text/html,*/*"}
    try:
        parts = urlparse.urlparse(url if "://" in url else "https://" + url)
        host = parts.hostname or domain
        scheme = parts.scheme or "https"
        home = f"{scheme}://{host}/"
    except Exception:
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "bad-url", "code": 0, "final_domain": domain}

    if is_social_or_builder(domain):
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "social-only/placeholder", "code": 0,
                "final_domain": domain}
    try:
        g = requests.get(home, headers=headers, timeout=timeout,
                         allow_redirects=True)
        code = g.status_code
        final_host = (urlparse.urlparse(g.url).hostname or domain).lower()
        final_host = final_host.removeprefix("www.")
        ctype = g.headers.get("Content-Type", "text/html")
        if code < 200 or code >= 300:
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"http-{code}", "code": code,
                    "final_domain": final_host}
        if "html" not in ctype.lower():
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"non-html:{ctype[:40]}", "code": code,
                    "final_domain": final_host}
        # Redirect landing on a social/parked host is not the school's site.
        if final_host != domain and is_social_or_builder(final_host):
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"redirect-to-social:{final_host}", "code": code,
                    "final_domain": final_host}
        html = g.text[:max_bytes] if g.text else ""
        time.sleep(politeness)
    except requests.RequestException as e:
        kind = type(e).__name__
        return {"status": "Inaccessible", "confidence": 0,
                "reason": f"fetch-error:{kind}", "code": 0,
                "final_domain": domain}

    if not html or len(html.strip()) < 200:
        return {"status": "Inaccessible", "confidence": 5,
                "reason": "empty-body", "code": code, "final_domain": final_host}

    low = html.lower()
    title, h1, visible = _visible(html)
    vlow = visible.lower()

    for rx in SOFT404_RE_C:
        if rx.search(vlow) or rx.search(low[:2000]):
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "soft-404/block-page", "code": code,
                    "final_domain": final_host}
    for rx in PARKING_RE_C:
        if rx.search(vlow) or rx.search(low[:4000]):
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "parking", "code": code, "final_domain": final_host}
    # Parking heuristic: almost all text is links + lots of external refs.
    text = TAG_RE.sub(" ", html)
    words = text.split()
    links = re.findall(r"<a\s", html, re.I)
    if len(words) < 120 and len(links) > 25:
        return {"status": "Inaccessible", "confidence": 10,
                "reason": "parking-linkfarm", "code": code,
                "final_domain": final_host}

    conf, reasons = 20, ["http-2xx-html"]  # reachable baseline
    if multisource:
        conf += 30
        reasons.append("multi-source")
    if SCHEMA_RE.search(html):
        conf += 25
        reasons.append("schema.org-edu")
    kws = keywords_for_country(country_iso)
    hay = (vlow + " " + low[:4000])
    if any(k in hay for k in kws):
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
    elif domain.endswith(".edu") or ".ac." in domain or domain.endswith(".sch.uk"):
        conf += 10
        reasons.append("trusted-suffix")

    conf = min(conf, 100)
    if conf >= 50:
        return {"status": "Active", "confidence": conf,
                "reason": "+".join(reasons), "code": code,
                "final_domain": final_host}
    return {"status": "Inaccessible", "confidence": conf,
            "reason": "low-confidence:" + "+".join(reasons), "code": code,
            "final_domain": final_host}
