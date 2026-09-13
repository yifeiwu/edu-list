"""Exa second-opinion for dissimilar cross-domain redirects.

Background: ``validate_site`` treats any cross-domain move (different
registrable base, e.g. ``rhul.ac.uk -> royalholloway.ac.uk``) as a pointer:
the old domain is ``Inaccessible`` (``moved-to:<new>``) and the target is
validated as its own row. Local homepage heuristics can still misjudge the
*target* — a JS-heavy portal may score low-confidence, or a parking page may
slip through — so when the redirect is "quite different" from the source we
ask Exa (https://exa.ai) whether the final domain hosts a real institution
site or just parking.

Design constraints (free-tier safe, offline-safe):
- Pure ``requests`` client — no new dependency (no ``exa-py``).
- Only called for *dissimilar* redirects (different registrable base via
  :func:`is_dissimilar_redirect`). Same-site hops (apex<->www, http->https,
  subpath) never touch Exa.
- Disabled when no API key is configured. Key resolution: ``EXA_API_KEY``
  env var wins, then ``validation.exa_api_key`` / ``exa.api_key`` in config.
- Budget-capped per run (``validation.exa_max_calls_per_run``, default 20)
  and cached in ``state["exa_cache"]`` (90-day TTL) — enforced by the caller
  (``verify.py``); this module also offers :func:`cached_verify` for reuse.
- Any transport/API failure returns ``verified=None`` (inconclusive) so Exa
  can never crash a run; local verdict stands.
"""
from __future__ import annotations

import datetime as dt
import os
import re
import urllib.parse as urlparse

import requests

from .util import PARKING_RES, keywords_for_country, registrable_base, same_site

EXA_SEARCH_URL = "https://api.exa.ai/search"

# Cache TTL mirrors whois_check negative-cache pacing: re-check quarterly.
EXA_CACHE_TTL_DAYS = 90

_PARKING_RE_C = [re.compile(p, re.I) for p in PARKING_RES]
_EXTRA_PARKING_PHRASES = (
    "buy this domain",
    "domain for sale",
    "parked free",
    "sedo.com",
    "godaddy",
    "domain parking",
    "this site is parked",
)


def resolve_api_key(cfg: dict | None = None) -> str | None:
    """Exa API key: ``EXA_API_KEY`` env wins, then config file."""
    env = (os.environ.get("EXA_API_KEY") or "").strip()
    if env and "example" not in env.lower() and "your" not in env.lower():
        return env
    cfg = cfg or {}
    for section in ("validation", "exa"):
        sec = cfg.get(section) or {}
        if isinstance(sec, dict):
            for k in ("exa_api_key", "api_key"):
                v = str(sec.get(k) or "").strip()
                if v and "example" not in v.lower() and "YOUR" not in v:
                    return v
    top = str(cfg.get("exa_api_key") or "").strip()
    if top:
        return top
    return None


def exa_config_from_cfg(cfg: dict | None = None) -> dict:
    """Runtime Exa settings from config + env (cheap, no network)."""
    cfg = cfg or {}
    v = cfg.get("validation", {}) or {}
    exa_section = cfg.get("exa", {}) or {}
    enabled = v.get("exa_enabled", exa_section.get("enabled", True))
    return {
        "enabled": bool(enabled),
        "api_key": resolve_api_key(cfg),
        "timeout": int(v.get("exa_timeout_seconds",
                             exa_section.get("timeout_seconds", 15))),
        "num_results": int(v.get("exa_num_results",
                                 exa_section.get("num_results", 5))),
        "search_type": str(v.get("exa_search_type",
                                 exa_section.get("search_type", "fast"))),
        "max_calls_per_run": int(v.get("exa_max_calls_per_run",
                                       exa_section.get("max_calls_per_run", 20))),
    }


def is_dissimilar_redirect(source: str, target: str) -> bool:
    """True when a redirect target is "quite different" from the source.

    Defined as: different registrable base (``same_site`` is False).
    Same-site hops (apex<->www, http->https, subdomain->apex on the same
    base, subpaths) return False and never trigger an Exa call.
    """
    s = (source or "").lower().strip(".").removeprefix("www.")
    t = (target or "").lower().strip(".").removeprefix("www.")
    if not s or not t or "." not in t:
        return False
    if s == t:
        return False
    try:
        return not same_site(s, t)
    except Exception:
        return registrable_base(s) != registrable_base(t)


def build_query(school_name: str = "", target_domain: str = "",
                country_iso: str = "") -> str:
    """Natural-language Exa query biasing toward the institution's homepage."""
    name = (school_name or "").strip()
    if name and name.lower() != (target_domain or "").lower():
        return f"{name} official website university school"
    if target_domain:
        return f"{target_domain} official university school website"
    return f"official university school website {country_iso or ''}".strip()


def search_exa(target_domain: str, query: str, api_key: str,
               timeout: int = 15, num_results: int = 5,
               search_type: str = "fast") -> dict | None:
    """POST one Exa search constrained to ``target_domain``.

    Returns the decoded JSON payload, or None on any failure (transport,
    non-200, invalid JSON). Callers treat None as inconclusive.
    """
    target = (target_domain or "").lower().strip(".").removeprefix("www.")
    if not target or not api_key:
        return None
    body = {
        "query": query or build_query(target_domain=target),
        "type": search_type or "fast",
        "numResults": max(1, min(int(num_results or 5), 10)),
        "includeDomains": [target],
        "contents": {
            "text": {"maxCharacters": 4000},
            "highlights": True,
        },
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "Authorization": f"Bearer {api_key}",
    }
    try:
        r = requests.post(EXA_SEARCH_URL, json=body, headers=headers,
                          timeout=timeout)
        if r.status_code != 200:
            return None
        payload = r.json()
        return payload if isinstance(payload, dict) else None
    except Exception:
        return None


def _result_texts(payload: dict) -> list[tuple[str, str]]:
    """(title+snippet+text blob, url) pairs for every returned result."""
    out: list[tuple[str, str]] = []
    try:
        results = payload.get("results", []) or []
    except Exception:
        return out
    for res in results:
        if not isinstance(res, dict):
            continue
        url = str(res.get("url", "") or "")
        parts = [
            str(res.get("title", "") or ""),
            str(res.get("snippet", "") or ""),
            str(res.get("summary", "") or ""),
        ]
        text = res.get("text", "")
        if isinstance(text, dict):
            text = text.get("content", "") or text.get("text", "")
        parts.append(str(text or ""))
        highlights = res.get("highlights", []) or res.get("highlight", []) or []
        if isinstance(highlights, list):
            parts.extend(str(h) for h in highlights if h)
        elif highlights:
            parts.append(str(highlights))
        out.append((" ".join(p for p in parts if p), url))
    return out


def interpret_results(payload: dict | None, target_domain: str,
                      country_iso: str = "",
                      school_name: str = "") -> dict:
    """Map an Exa payload to ``{verified, reason, evidence}``.

    - ``verified=True`` (``exa-verified``): Exa indexes the domain with
      institution-like content (school-name tokens or edu keywords, or
      substantial non-parking text).
    - ``verified=False`` (``exa-parking``): indexed content matches parking
      phrases — the final site is a parking page, not a school.
    - ``verified=None``: inconclusive (API error, or domain not indexed).
      The local verdict stands; never gates status.
    """
    target = (target_domain or "").lower().strip(".")
    if payload is None:
        return {"verified": None, "reason": "exa-error",
                "evidence": []}
    blobs = _result_texts(payload)
    # Keep only results actually served from the target's registrable base
    # (includeDomains already filters; this is a safety net).
    kept = []
    for blob, url in blobs:
        try:
            host = (urlparse.urlparse(url).hostname or "").lower()
        except Exception:
            host = ""
        if not host:
            # No URL to attribute — still usable as weak evidence.
            kept.append((blob, url))
        elif target and (host == target or host.endswith("." + target)
                         or same_site(host, target)):
            kept.append((blob, url))
    if not kept:
        return {"verified": None, "reason": "exa-no-results", "evidence": []}
    evidence = [u for _, u in kept[:3] if u]
    combined = " ".join(b for b, _ in kept).lower()
    if any(p in combined for p in _EXTRA_PARKING_PHRASES) or any(
            rx.search(combined) for rx in _PARKING_RE_C):
        return {"verified": False, "reason": "exa-parking",
                "evidence": evidence}
    # School-name tokens (e.g. "royal holloway") or per-country edu keywords
    # in Exa's indexed text confirm a real institution site.
    name_toks = [t.lower() for t in re.split(r"[^a-z0-9]+", school_name or "")
                 if len(t) >= 4]
    if any(t in combined for t in name_toks):
        return {"verified": True, "reason": "exa-verified",
                "evidence": evidence}
    kws = [k.lower() for k in keywords_for_country(country_iso or "")]
    if any(k in combined for k in kws):
        return {"verified": True, "reason": "exa-verified",
                "evidence": evidence}
    # Indexed with real copy but no keyword hit (e.g. non-English portal
    # missing from our keyword set): still evidence the domain is a live
    # site rather than parking — but stay inconclusive so local scoring
    # decides, with the evidence recorded.
    substantial = any(len(b.split()) >= 40 for b, _ in kept)
    if substantial:
        return {"verified": True, "reason": "exa-verified:indexed",
                "evidence": evidence}
    return {"verified": None, "reason": "exa-inconclusive",
            "evidence": evidence}


def verify_redirect_target(source: str, target: str, school_name: str = "",
                           country_iso: str = "", api_key: str = "",
                           timeout: int = 15, num_results: int = 5,
                           search_type: str = "fast") -> dict:
    """One-shot Exa check that a dissimilar redirect target is real.

    Returns ``{verified, reason, evidence}``; ``verified`` is True (real
    institution site), False (parking), or None (skipped/inconclusive —
    same-site, missing key, or API failure).
    """
    if not is_dissimilar_redirect(source, target):
        return {"verified": None, "reason": "exa-skipped:same-site",
                "evidence": []}
    if not (api_key or "").strip():
        return {"verified": None, "reason": "exa-skipped:no-key",
                "evidence": []}
    query = build_query(school_name, target, country_iso)
    payload = search_exa(target, query, api_key, timeout=timeout,
                         num_results=num_results, search_type=search_type)
    return interpret_results(payload, target, country_iso, school_name)


def _cache_expired(entry: dict, today: dt.date) -> bool:
    ts = str((entry or {}).get("ts", "") or "")
    if not ts:
        return True
    try:
        day = dt.date.fromisoformat(ts[:10])
    except ValueError:
        return True
    return (today - day).days >= EXA_CACHE_TTL_DAYS


def cached_verify(source: str, target: str, school_name: str = "",
                  country_iso: str = "", cache: dict | None = None,
                  api_key: str = "", timeout: int = 15,
                  num_results: int = 5,
                  search_type: str = "fast") -> dict | None:
    """Budget-friendly wrapper: per-target cache (90d TTL), None on skip.

    Returns None when the redirect is same-site (no Exa needed) or no API
    key is configured — so callers can distinguish "no opinion" from an
    actual ``{verified, ...}`` verdict. Cache key is the normalized target
    domain (verification is about the final site, shared by all sources).
    """
    if not is_dissimilar_redirect(source, target):
        return None
    if not (api_key or "").strip():
        return None
    key = (target or "").lower().strip(".").removeprefix("www.")
    today = dt.date.today()
    if cache is not None and key in cache:
        raw = cache[key]
        if isinstance(raw, dict) and "verified" in raw:
            if raw.get("verified") is None:
                # Negative/inconclusive entries expire like WHOIS misses.
                if not _cache_expired(raw, today):
                    return raw
            else:
                try:
                    day = dt.date.fromisoformat(str(raw.get("ts", today.isoformat()))[:10])
                    if (today - day).days < EXA_CACHE_TTL_DAYS:
                        return raw
                except ValueError:
                    pass
    verdict = verify_redirect_target(source, target, school_name, country_iso,
                                     api_key, timeout, num_results,
                                     search_type)
    if cache is not None:
        try:
            cache[key] = {"verified": verdict.get("verified"),
                          "reason": verdict.get("reason", ""),
                          "evidence": list(verdict.get("evidence", []) or [])[:3],
                          "ts": today.isoformat()}
        except Exception:
            pass
    return verdict
