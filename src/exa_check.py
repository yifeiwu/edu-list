"""Exa second-opinion for dissimilar cross-domain redirects + fallback rescue.

Background: ``validate_site`` treats any cross-domain move (different
registrable base, e.g. ``rhul.ac.uk -> royalholloway.ac.uk``) as a pointer:
the old domain is ``Inaccessible`` (``moved-to:<new>``) and the target is
validated as its own row. Local homepage heuristics can still misjudge the
*target* — a JS-heavy portal may score low-confidence, or a parking page may
slip through — so when the redirect is "quite different" from the source we
ask Exa (https://exa.ai) whether the final domain hosts a real institution
site or just parking.

Fallback rescue (bot-block / network failures): when a direct fetch fails
(403, connection/timeout, empty-body, soft-404, low-confidence) Exa can
rescue the row — if Exa independently indexes the same domain as the
institution, the row becomes ``Active`` instead of ``Inaccessible``; if Exa
finds a different canonical domain for the same school, the row reports
``moved_to`` so the caller can update the domain (chase + re-validate the
target). Social/builder placeholders and service-hosts (webmail/LMS) are
never rescued; TLS errors never rescue same-domain (strict TLS) but may
still discover a replacement domain.

Design constraints (free-tier safe, offline-safe):
- Pure ``requests`` client — no new dependency (no ``exa-py``).
- Redirect second-opinion only for *dissimilar* redirects (different
  registrable base via :func:`is_dissimilar_redirect`). Same-site hops
  (apex<->www, http->https, subpath) never touch Exa via that path.
- Fallback rescue/discovery is opt-in per call (``exa_fallback_fn``) and
  shares the caller's budget + 90d cache.
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

from .util import (
    PARKING_RES,
    is_service_host,
    is_social_or_builder,
    keywords_for_country,
    normalize_domain,
    registrable_base,
    same_site,
)

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
    # Fallback rescue (bot-block/network -> Exa self-verify + discovery).
    # Defaults ON when the main switch is ON, separately killable via
    # validation.exa_rescue_enabled=false.
    rescue_enabled = v.get("exa_rescue_enabled",
                           exa_section.get("rescue_enabled", enabled))
    return {
        "enabled": bool(enabled),
        "rescue_enabled": bool(rescue_enabled),
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
      institution-like content (school-name tokens or edu keywords).
    - ``verified=False`` (``exa-parking``): indexed content matches parking
      phrases — the final site is a parking page, not a school.
    - ``verified=None``: inconclusive (API error, domain not indexed, or
      indexed with copy that shows no educational signal — e.g. a
      lapsed-domain takeover serving unrelated commercial content).
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
    # Indexed with copy that shows no educational signal (e.g. a
    # lapsed-domain takeover serving unrelated commercial content, or a
    # non-English portal missing from our keyword set): stay inconclusive so
    # word-count alone can never verify a non-educational site — the local
    # verdict stands, with the evidence recorded.
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


# --- fallback rescue + discovery (bot-block / network failures) ------------

def search_general(query: str, api_key: str, timeout: int = 15,
                   num_results: int = 5,
                   search_type: str = "fast") -> dict | None:
    """Unconstrained Exa search (no includeDomains) for domain discovery.

    Returns the decoded JSON payload, or None on any failure. Callers treat
    None as inconclusive.
    """
    if not (query or "").strip() or not (api_key or "").strip():
        return None
    body = {
        "query": query,
        "type": search_type or "fast",
        "numResults": max(1, min(int(num_results or 5), 10)),
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


def verify_domain(domain: str, school_name: str = "",
                  country_iso: str = "", api_key: str = "",
                  timeout: int = 15, num_results: int = 5,
                  search_type: str = "fast") -> dict:
    """Self-check: does Exa index ``domain`` as the institution's site?

    Same as :func:`verify_redirect_target` but without the dissimilar gate —
    used to rescue bot-blocked / network-failed fetches. Returns
    ``{verified, reason, evidence}``; ``verified`` None on skip/failure.
    """
    target = (domain or "").lower().strip(".").removeprefix("www.")
    if not target or "." not in target:
        return {"verified": None, "reason": "exa-skipped:bad-domain",
                "evidence": []}
    if not (api_key or "").strip():
        return {"verified": None, "reason": "exa-skipped:no-key",
                "evidence": []}
    query = build_query(school_name, target, country_iso)
    payload = search_exa(target, query, api_key, timeout=timeout,
                         num_results=num_results, search_type=search_type)
    return interpret_results(payload, target, country_iso, school_name)


def extract_candidate_domain(payload: dict | None,
                             exclude_domain: str = "") -> tuple[str | None, list[str]]:
    """Pick the most-cited registrable host from an unconstrained payload.

    Filters social/builder/service-hosts and the source domain itself.
    Returns ``(candidate_or_None, evidence_urls[:3])``.
    """
    if not isinstance(payload, dict):
        return None, []
    excl = (exclude_domain or "").lower().strip(".").removeprefix("www.")
    counts: dict[str, int] = {}
    first_url: dict[str, str] = {}
    try:
        results = payload.get("results", []) or []
    except Exception:
        return None, []
    for res in results:
        if not isinstance(res, dict):
            continue
        url = str(res.get("url", "") or "")
        try:
            host = (urlparse.urlparse(url).hostname or "").lower().strip(".")
        except Exception:
            continue
        norm = normalize_domain(host or "")
        if not norm:
            continue
        try:
            if excl and (norm == excl or same_site(norm, excl)):
                continue
            if is_social_or_builder(norm) or is_service_host(norm):
                continue
        except Exception:
            continue
        counts[norm] = counts.get(norm, 0) + 1
        if norm not in first_url and url:
            first_url[norm] = url
    if not counts:
        return None, []
    # Most-cited wins; ties break toward academic suffixes, then shortest.
    def _rank(d: str) -> tuple:
        from .util import is_academic_suffix as _acad
        try:
            acad = _acad(d)
        except Exception:
            acad = False
        return (-counts[d], not acad, len(d), d)
    best = sorted(counts, key=_rank)[0]
    ev = [first_url[best]] if best in first_url else []
    return best, ev


def discover_domain(school_name: str = "", country_iso: str = "",
                    exclude_domain: str = "", api_key: str = "",
                    timeout: int = 15, num_results: int = 5,
                    search_type: str = "fast") -> dict:
    """Find a different canonical domain for the school via Exa.

    Returns ``{domain, verified, reason, evidence}`` where ``domain`` is the
    candidate (or None) and ``verified`` mirrors
    :func:`interpret_results` against that candidate using the same payload
    (no second API call). Inconclusive when no usable candidate exists.
    """
    if not (api_key or "").strip():
        return {"domain": None, "verified": None,
                "reason": "exa-skipped:no-key", "evidence": []}
    query = build_query(school_name, "", country_iso)
    payload = search_general(query, api_key, timeout=timeout,
                             num_results=num_results,
                             search_type=search_type)
    if payload is None:
        return {"domain": None, "verified": None, "reason": "exa-error",
                "evidence": []}
    cand, ev = extract_candidate_domain(payload, exclude_domain)
    if not cand:
        return {"domain": None, "verified": None,
                "reason": "exa-no-results", "evidence": []}
    verdict = interpret_results(payload, cand, country_iso, school_name)
    return {"domain": cand, "verified": verdict.get("verified"),
            "reason": verdict.get("reason", ""), "evidence": ev}


def _cache_get(cache: dict | None, key: str) -> dict | None:
    """Return a fresh cached verdict or None (miss/expired/wrong shape)."""
    if cache is None:
        return None
    try:
        raw = cache.get(key)
    except Exception:
        return None
    if not isinstance(raw, dict) or "verified" not in raw:
        return None
    try:
        day = dt.date.fromisoformat(str(raw.get("ts", ""))[:10])
    except ValueError:
        return None
    if (dt.date.today() - day).days >= EXA_CACHE_TTL_DAYS:
        return None
    return raw


def _cache_put(cache: dict | None, key: str, verdict: dict) -> None:
    if cache is None:
        return
    try:
        cache[key] = {"verified": verdict.get("verified"),
                      "reason": verdict.get("reason", ""),
                      "evidence": list(verdict.get("evidence", []) or [])[:3],
                      "ts": dt.date.today().isoformat()}
    except Exception:
        pass


def cached_verify_self(domain: str, school_name: str = "",
                       country_iso: str = "", cache: dict | None = None,
                       api_key: str = "", timeout: int = 15,
                       num_results: int = 5,
                       search_type: str = "fast") -> dict | None:
    """Cached self-verify (no dissimilar gate). None only when no key."""
    if not (api_key or "").strip():
        return None
    key = (domain or "").lower().strip(".").removeprefix("www.")
    if not key:
        return None
    hit = _cache_get(cache, key)
    if hit is not None:
        return hit
    verdict = verify_domain(domain, school_name, country_iso, api_key,
                            timeout, num_results, search_type)
    _cache_put(cache, key, verdict)
    return verdict


def cached_discover(school_name: str = "", country_iso: str = "",
                    exclude_domain: str = "", cache: dict | None = None,
                    api_key: str = "", timeout: int = 15,
                    num_results: int = 5,
                    search_type: str = "fast") -> dict | None:
    """Cached discovery. None only when no key; else the discover dict."""
    if not (api_key or "").strip():
        return None
    key = ("discover:" + (exclude_domain or "").lower().strip(".")
           .removeprefix("www."))
    hit = _cache_get(cache, key)
    # Discovery cache stores {"verified":..., "reason":..., "evidence":...,
    # "domain":...} — reuse only when it carries a domain verdict.
    if hit is not None and "domain" in hit:
        return hit
    out = discover_domain(school_name, country_iso, exclude_domain, api_key,
                          timeout, num_results, search_type)
    if cache is not None:
        try:
            cache[key] = {"verified": out.get("verified"),
                          "reason": out.get("reason", ""),
                          "evidence": list(out.get("evidence", []) or [])[:3],
                          "domain": out.get("domain"),
                          "ts": dt.date.today().isoformat()}
        except Exception:
            pass
    return out


def fallback_check(domain: str, school_name: str = "",
                   country_iso: str = "", cache: dict | None = None,
                   api_key: str = "", timeout: int = 15,
                   num_results: int = 5,
                   search_type: str = "fast",
                   allow_discovery: bool = True) -> dict | None:
    """One-shot fallback: self-verify, then discovery for a replacement.

    Returns ``{verified, reason, evidence, candidate}`` where ``candidate``
    is a different verified domain (or None). ``verified`` True means Exa
    indexes the *same* domain as the institution. Inconclusive (None
    verdict / verified None + no candidate) means keep the local verdict.
    Never raises; API failures yield inconclusive.
    """
    try:
        if not (api_key or "").strip():
            return None
        self_v = cached_verify_self(domain, school_name, country_iso,
                                    cache=cache, api_key=api_key,
                                    timeout=timeout, num_results=num_results,
                                    search_type=search_type)
        if isinstance(self_v, dict) and self_v.get("verified") is True:
            return {"verified": True, "reason": self_v.get("reason", ""),
                    "evidence": list(self_v.get("evidence", []) or []),
                    "candidate": None}
        if isinstance(self_v, dict) and self_v.get("verified") is False:
            # Definitively parking on the same domain — do not rescue, but
            # discovery may still find the real home (handled below).
            pass
        if not allow_discovery:
            return self_v if isinstance(self_v, dict) else None
        disc = cached_discover(school_name, country_iso, domain,
                               cache=cache, api_key=api_key, timeout=timeout,
                               num_results=num_results,
                               search_type=search_type)
        if isinstance(disc, dict) and disc.get("domain"):
            cand = disc.get("domain")
            try:
                dissimilar = is_dissimilar_redirect(domain or "", cand or "")
            except Exception:
                dissimilar = (cand or "").lower() != (domain or "").lower()
            if dissimilar and disc.get("verified") is True:
                return {"verified": None,
                        "reason": disc.get("reason", ""),
                        "evidence": list(disc.get("evidence", []) or []),
                        "candidate": cand}
        # No rescue, no replacement — surface the self verdict (may be
        # parking/inconclusive) so callers can record evidence.
        if isinstance(self_v, dict):
            return {"verified": self_v.get("verified"),
                    "reason": self_v.get("reason", ""),
                    "evidence": list(self_v.get("evidence", []) or []),
                    "candidate": None}
        return None
    except Exception:
        return None
