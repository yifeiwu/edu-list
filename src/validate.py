"""Validation v2: homepage-only, free-tier safe.

Rules (strict-TLS revision + Exa fallback rescue):
- Final HTTP status non-2xx (after redirects) => Inaccessible, unless Exa
  fallback independently verifies the same domain as the institution
  (bot-block / WAF false-positive) — then Active with `+exa-verified`.
  Moved pointers (non-2xx with a cross-domain `moved_to`) are never rescued;
  the pointer is chased instead.
- TLS errors (expired/self-signed/broken chain) => Inaccessible on the same
  domain (strict TLS, never rescued to Active). Exa may still supply a
  *different* canonical domain, reported as `moved_to` so the caller can
  update the domain.
- Transient transport failures (ConnectionError/Timeout) are retried once
  with backoff; persistent failures => Inaccessible, unless Exa verifies the
  same domain (rescue) or finds a replacement domain (move).
- Social-only / builder-placeholder / service-host => Inaccessible, never
  rescued and never replaced via Exa.
- Parking / soft-404 / empty => Inaccessible locally; Exa may rescue
  soft-404/block-page and empty-body to Active, or supply a replacement
  domain for parked pages (reported as `moved_to`).
- Educational-identity gate: without any educational signal in the fetched
  metadata (schema.org edu type, the school's own name, or per-country edu
  keywords), the page is not the institution's website — even with HTTP 200
  and substantial copy (lapsed-domain takeovers serve those). Capped below
  Active as `non-educational-content`; Exa may still rescue with genuine edu
  evidence or supply a replacement domain.
- Else score content signals; confidence >= threshold => Active. Below
  threshold (low-confidence) => Inaccessible, unless Exa verifies (rescue).
- Cross-domain moves (HTTP redirect or meta-refresh to a different
  registrable base) are reported as `moved_to` so the caller can mark the
  old domain `moved-to:<new>` and validate the target as its own row
  (rebrands like unochapeco.edu.br -> uno.edu.br must not be misattributed).
  Same-site redirects (apex<->www, http->https, subpath) are NOT moves.
- Exa second-opinion (optional): when a move target is *dissimilar*
  (different registrable base, e.g. rhul.ac.uk -> royalholloway.ac.uk) an
  injected `exa_verify_fn` can confirm the final site is a real institution
  vs parking. The old domain stays a pointer (never Active); the verdict is
  recorded as `exa` + `+exa-verified`/`+exa-parking` reason suffix. When a
  known redirect target is validated with `redirect_from` set, an
  `exa-verified` verdict can rescue an otherwise low-confidence page to
  Active, and an `exa-parking` verdict demotes a local Active to
  Inaccessible. Without a key / offline the hook is None and behavior is
  unchanged.
- Exa fallback rescue (optional `exa_fallback_fn(domain, school, iso)` ->
  `{verified, reason, evidence, candidate?}`): consulted on failure paths
  (fetch-errors, non-2xx without a move, empty-body, soft-404, low-
  confidence). `verified is True` rescues the same domain to Active;
  `candidate` (a different, Exa-verified domain) is reported as `moved_to`
  so the caller can update the domain. Any error / None / inconclusive
  keeps the local Inaccessible verdict.

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

try:  # optional: only needed when Exa second-opinion is wired in
    from .exa_check import is_dissimilar_redirect
except Exception:  # noqa: BLE001 - offline-safe fallback
    def is_dissimilar_redirect(source: str, target: str) -> bool:  # type: ignore[no-redef]
        try:
            return not same_site(source or "", target or "") and source != target
        except Exception:
            return False

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


LANG_RE = re.compile(
    r'<html[^>]*\blang=["\']?([a-zA-Z]{2,3}(?:-[a-zA-Z0-9]{2,8})?)'
    r'(?:["\'\s>/]|$)',
    re.I)


def _page_lang(html: str) -> str:
    """Homepage language from the <html lang> attribute (lowercased BCP47).

    Only the document head is scanned (the tag precedes all content).
    Returns "" when absent — published as the `language` CSV column.
    """
    m = LANG_RE.search((html or "")[:2000])
    if not m:
        return ""
    return m.group(1).lower()


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


def _consult_exa(source: str, target: str | None, school_name: str,
                 country_iso: str,
                 exa_verify_fn: Callable[..., dict | None] | None) -> dict | None:
    """Safely ask Exa about a dissimilar redirect target (None = no opinion).

    `exa_verify_fn(source, target, school_name, country_iso)` must return
    `{verified: True|False|None, reason, evidence?}` or None. Same-site
    redirects never consult Exa. Any error => None (local verdict stands).
    """
    if not exa_verify_fn or not source or not target:
        return None
    try:
        if not is_dissimilar_redirect(source, target):
            return None
    except Exception:
        return None
    try:
        try:
            verdict = exa_verify_fn(source, target, school_name or "",
                                    country_iso or "")
        except TypeError:
            # Back-compat for 2-arg test doubles.
            verdict = exa_verify_fn(source, target)  # type: ignore[call-arg]
    except Exception:
        return None
    return verdict if isinstance(verdict, dict) else None


def _exa_suffix(verdict: dict | None) -> str:
    """Reason suffix for a decisive Exa verdict, else '' (keep reasons stable)."""
    if not isinstance(verdict, dict):
        return ""
    if verdict.get("verified") is True:
        reason = str(verdict.get("reason", "exa-verified") or "exa-verified")
        return "+" + (reason if reason.startswith("exa-") else "exa-verified")
    if verdict.get("verified") is False:
        reason = str(verdict.get("reason", "exa-parking") or "exa-parking")
        return "+" + (reason if reason.startswith("exa-") else "exa-parking")
    return ""


def _consult_exa_fallback(domain: str, school_name: str, country_iso: str,
                          exa_fallback_fn: Callable[..., dict | None] | None
                          ) -> dict | None:
    """Safely ask the Exa fallback hook (None = no opinion / skipped).

    `exa_fallback_fn(domain, school_name, country_iso)` must return
    `{verified: True|False|None, reason, evidence?, candidate?}` or None.
    Any error => None (local verdict stands).
    """
    if not exa_fallback_fn or not domain:
        return None
    try:
        verdict = exa_fallback_fn(domain, school_name or "",
                                  country_iso or "")
    except TypeError:
        # Wrong arity test doubles / legacy hooks — treat as no opinion.
        return None
    except Exception:
        return None
    return verdict if isinstance(verdict, dict) else None


def _fallback_candidate_target(domain: str, verdict: dict | None) -> str | None:
    """Normalized dissimilar replacement domain from a fallback verdict."""
    if not isinstance(verdict, dict):
        return None
    cand = (verdict.get("candidate") or verdict.get("domain")
            or verdict.get("moved_to") or "")
    cand = str(cand or "").lower().strip().strip(".").removeprefix("www.")
    if not cand or "." not in cand:
        return None
    norm = normalize_domain(cand)
    if not norm:
        return None
    try:
        if is_social_or_builder(norm) or is_service_host(norm):
            return None
        # Require a genuinely different registrable base (not www/apex).
        if same_site(domain or "", norm):
            return None
        return norm
    except Exception:
        return None


def _apply_exa_fallback(domain: str, school_name: str, country_iso: str,
                        exa_fallback_fn: Callable[..., dict | None] | None,
                        *, local_reason: str, local_code: int,
                        local_final: str,
                        active_threshold: int,
                        allow_rescue_same: bool = True) -> dict | None:
    """Try Exa fallback rescue / domain-update for a failure path.

    Returns a full result dict on rescue (Active) or replacement
    (Inaccessible + moved_to), else None (keep the local verdict).
    """
    verdict = _consult_exa_fallback(domain, school_name, country_iso,
                                    exa_fallback_fn)
    if verdict is None:
        return None
    # 1) Replacement domain wins: report a move pointer so the caller can
    # update the domain (chase + validate the target as its own row).
    target = _fallback_candidate_target(domain, verdict)
    if target:
        suffix = _exa_suffix({"verified": True,
                              "reason": verdict.get("reason") or "exa-discovered"})
        # Normalize suffix label for discovery (exa-verified -> exa-discovered
        # only when the hook didn't already say so).
        reason_core = str(verdict.get("reason", "") or "")
        if "discover" not in reason_core and "exa-" not in reason_core:
            suffix = "+exa-discovered"
        elif suffix == "+exa-verified":
            suffix = "+exa-discovered"
        return {"status": "Inaccessible", "confidence": 10,
                "reason": f"moved-to:{target}{suffix}", "code": local_code,
                "final_domain": local_final or domain, "moved_to": target,
                "exa": verdict}
    # 2) Same-domain rescue (bot-block / network false-positive).
    if allow_rescue_same and verdict.get("verified") is True:
        suffix = _exa_suffix(verdict) or "+exa-verified"
        return {"status": "Active",
                "confidence": max(int(active_threshold), 50),
                "reason": f"{local_reason}{suffix}", "code": local_code,
                "final_domain": local_final or domain, "moved_to": None,
                "exa": verdict}
    return None


def validate_site(url: str, domain: str, country_iso: str, timeout: int,
                  user_agent: str, max_bytes: int,
                  multisource: bool = False,
                  politeness: float = 0.4,
                  active_threshold: int = 50,
                  sleep_fn: Callable[[float], None] | None = None,
                  retries: int = 1,
                  retry_backoff: float = 1.0,
                  school_name: str = "",
                  redirect_from: str | None = None,
                  exa_verify_fn: Callable[..., dict | None] | None = None,
                  exa_fallback_fn: Callable[..., dict | None] | None = None) -> dict:
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
    lang = ""  # homepage language; parsed once HTML is available below
    try:
        parts = urlparse.urlparse(url if "://" in url else "https://" + url)
        host = parts.hostname or domain
        scheme = parts.scheme or "https"
        home = f"{scheme}://{host}/"
    except Exception:
        fb = _apply_exa_fallback(domain, school_name, country_iso,
                                 exa_fallback_fn, local_reason="bad-url",
                                 local_code=0, local_final=domain,
                                 active_threshold=active_threshold,
                                 allow_rescue_same=False)
        if fb is not None:
            return fb
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "bad-url", "code": 0, "final_domain": domain,
                "moved_to": None, "language": lang}

    if is_social_or_builder(domain):
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "social-only/placeholder", "code": 0,
                "final_domain": domain, "moved_to": None, "language": lang}
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
                local_reason = f"fetch-error:{kind}"
                fb = _apply_exa_fallback(domain, school_name, country_iso,
                                         exa_fallback_fn,
                                         local_reason=local_reason,
                                         local_code=0, local_final=domain,
                                         active_threshold=active_threshold)
                if fb is not None:
                    return fb
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": local_reason, "code": 0,
                        "final_domain": domain, "moved_to": None, "language": lang}
            _backoff()
            continue
        except requests.RequestException as e:
            _polite()
            kind = type(e).__name__
            local_reason = f"fetch-error:{kind}"
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn,
                                     local_reason=local_reason,
                                     local_code=0, local_final=domain,
                                     active_threshold=active_threshold)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": local_reason, "code": 0,
                    "final_domain": domain, "moved_to": None, "language": lang}
        except Exception as e:  # noqa: BLE001 - boundary guard
            _polite()
            kind = type(e).__name__
            local_reason = f"fetch-error:{kind}"
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn,
                                     local_reason=local_reason,
                                     local_code=0, local_final=domain,
                                     active_threshold=active_threshold)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": local_reason, "code": 0,
                    "final_domain": domain, "moved_to": None, "language": lang}
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
                fb = _apply_exa_fallback(domain, school_name, country_iso,
                                         exa_fallback_fn,
                                         local_reason="fetch-error:SSLError",
                                         local_code=0, local_final=domain,
                                         active_threshold=active_threshold,
                                         allow_rescue_same=False)
                if fb is not None:
                    return fb
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": "fetch-error:SSLError", "code": 0,
                        "final_domain": domain, "moved_to": None, "language": lang}
            except requests.RequestException as e2:
                _polite()
                local_reason = f"fetch-error:{type(e2).__name__}"
                fb = _apply_exa_fallback(domain, school_name, country_iso,
                                         exa_fallback_fn,
                                         local_reason=local_reason,
                                         local_code=0, local_final=domain,
                                         active_threshold=active_threshold)
                if fb is not None:
                    return fb
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": local_reason,
                        "code": 0, "final_domain": domain, "moved_to": None, "language": lang}
            except Exception as e2:  # noqa: BLE001 - boundary guard
                _polite()
                local_reason = f"fetch-error:{type(e2).__name__}"
                fb = _apply_exa_fallback(domain, school_name, country_iso,
                                         exa_fallback_fn,
                                         local_reason=local_reason,
                                         local_code=0, local_final=domain,
                                         active_threshold=active_threshold)
                if fb is not None:
                    return fb
                return {"status": "Inaccessible", "confidence": 0,
                        "reason": local_reason,
                        "code": 0, "final_domain": domain, "moved_to": None, "language": lang}
        else:
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn,
                                     local_reason=f"fetch-error:{ssl_kind}",
                                     local_code=0, local_final=domain,
                                     active_threshold=active_threshold,
                                     allow_rescue_same=False)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 0,
                    "reason": f"fetch-error:{ssl_kind}",
                    "code": 0, "final_domain": domain, "moved_to": None, "language": lang}
    if g is None:
        fb = _apply_exa_fallback(domain, school_name, country_iso,
                                 exa_fallback_fn,
                                 local_reason="fetch-error:ConnectionError",
                                 local_code=0, local_final=domain,
                                 active_threshold=active_threshold)
        if fb is not None:
            return fb
        return {"status": "Inaccessible", "confidence": 0,
                "reason": "fetch-error:ConnectionError", "code": 0,
                "final_domain": domain, "moved_to": None, "language": lang}
    # Fetch chain done: g is a real response from here on.
    try:
        code = g.status_code
        final_host = (urlparse.urlparse(g.url).hostname or domain).lower()
        final_host = final_host.strip(".").removeprefix("www.")
        moved = _moved_to(domain, final_host)
        ctype = g.headers.get("Content-Type", "text/html")
        if code < 200 or code >= 300:
            _polite()
            if moved:
                # HTTP redirect chain already found the new home — chase it.
                return {"status": "Inaccessible", "confidence": 5,
                        "reason": f"http-{code}", "code": code,
                        "final_domain": final_host, "moved_to": moved, "language": lang}
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn,
                                     local_reason=f"http-{code}",
                                     local_code=code,
                                     local_final=final_host,
                                     active_threshold=active_threshold)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"http-{code}", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
        if "html" not in ctype.lower():
            _polite()
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"non-html:{ctype[:40]}", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
        # Redirect landing on a social/parked host is not the school's site.
        if moved and is_social_or_builder(moved):
            _polite()
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": f"moved-to-social:{moved}", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
        full_text = _read_limited(g, FULL_SCAN_MAX)
        html = full_text[:max_bytes] if full_text else ""
        lang = _page_lang(html)
        _polite()
    finally:
        try:
            g.close()
        except Exception:
            pass

    if not html or len(html.strip()) < 200:
        if moved:
            return {"status": "Inaccessible", "confidence": 5,
                    "reason": "empty-body", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
        fb = _apply_exa_fallback(domain, school_name, country_iso,
                                 exa_fallback_fn, local_reason="empty-body",
                                 local_code=code, local_final=final_host,
                                 active_threshold=active_threshold)
        if fb is not None:
            return fb
        return {"status": "Inaccessible", "confidence": 5,
                "reason": "empty-body", "code": code,
                "final_domain": final_host, "moved_to": moved, "language": lang}

    # Meta-refresh hop to another host: same as an HTTP move (requests does
    # not follow these). Don't score the placeholder page as the school.
    mm = META_REFRESH_RE.search(html[:8000])
    if mm:
        target = normalize_domain(mm.group(1).strip().strip("'\""))
        if target and not same_site(target, domain):
            if is_social_or_builder(target):
                return {"status": "Inaccessible", "confidence": 5,
                        "reason": f"moved-to-social:{target}", "code": code,
                        "final_domain": final_host, "moved_to": target, "language": lang}
            exa_v = _consult_exa(domain, target, school_name, country_iso,
                                 exa_verify_fn)
            suffix = _exa_suffix(exa_v)
            out: dict = {"status": "Inaccessible", "confidence": 10,
                         "reason": f"moved-meta:{target}{suffix}", "code": code,
                         "final_domain": final_host, "moved_to": target, "language": lang}
            if exa_v is not None:
                out["exa"] = exa_v
            return out

    low = html.lower()
    title, h1, visible = _visible(html)
    vlow = visible.lower()

    for rx in SOFT404_RE_C:
        if rx.search(vlow) or rx.search(low[:2000]):
            if moved:
                return {"status": "Inaccessible", "confidence": 10,
                        "reason": "soft-404/block-page", "code": code,
                        "final_domain": final_host, "moved_to": moved, "language": lang}
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn,
                                     local_reason="soft-404/block-page",
                                     local_code=code,
                                     local_final=final_host,
                                     active_threshold=active_threshold)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "soft-404/block-page", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
    for rx in PARKING_RE_C:
        if rx.search(vlow) or rx.search(low[:4000]):
            if moved:
                return {"status": "Inaccessible", "confidence": 10,
                        "reason": "parking", "code": code,
                        "final_domain": final_host, "moved_to": moved, "language": lang}
            # Parked: never rescue same-domain, but Exa may know the real home.
            fb = _apply_exa_fallback(domain, school_name, country_iso,
                                     exa_fallback_fn, local_reason="parking",
                                     local_code=code,
                                     local_final=final_host,
                                     active_threshold=active_threshold,
                                     allow_rescue_same=False)
            if fb is not None:
                return fb
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "parking", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
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
        if moved:
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "parking-linkfarm", "code": code,
                    "final_domain": final_host, "moved_to": moved, "language": lang}
        # Linkfarm: never rescue same-domain, but Exa may know the real home.
        fb = _apply_exa_fallback(domain, school_name, country_iso,
                                 exa_fallback_fn,
                                 local_reason="parking-linkfarm",
                                 local_code=code, local_final=final_host,
                                 active_threshold=active_threshold,
                                 allow_rescue_same=False)
        if fb is not None:
            return fb
        return {"status": "Inaccessible", "confidence": 10,
                "reason": "parking-linkfarm", "code": code,
                "final_domain": final_host, "moved_to": moved, "language": lang}

    conf, reasons = 20, ["http-2xx-html"]  # reachable baseline
    if multisource:
        conf += 30
        reasons.append("multi-source")
    schema_hit = bool(SCHEMA_RE.search(html))
    if schema_hit:
        conf += 25
        reasons.append("schema.org-edu")
    # Keyword search must cover the whole body: modern portal/SPAs bury all
    # visible strings at the end of huge <head> bundles, past any slice.
    kws = keywords_for_country(country_iso)
    body_low = full_text.lower()
    hay = (vlow + " " + low[:4000])
    kw_hit = any(k in hay for k in kws) or any(k in body_low for k in kws)
    if kw_hit:
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

    # Educational-identity gate (lapsed-domain takeover protection): the page
    # only counts as the institution's website when its metadata still shows
    # educational signals — a schema.org edu type, the school's own name, or
    # per-country edu keywords. Structure/volume/trust bonuses alone
    # (multi-source, substantial copy, academic suffix) must never promote a
    # takeover (e.g. a betting operator serving HTTP 200 on an expired
    # college domain) to Active. Without edu signals the row stays
    # Inaccessible; Exa may still rescue it with genuine edu evidence or
    # supply the school's replacement domain via discovery.
    name_toks = [t.lower() for t in re.split(r"[^a-z0-9]+", school_name or "")
                 if len(t) >= 4]
    has_edu_signal = (
        schema_hit
        or kw_hit
        or any(t in hay or t in body_low for t in name_toks)
    )
    if not has_edu_signal:
        conf = min(conf, 40)
        reasons.append("non-educational-content")

    # Base for move-target comparison (registrable, for stable reason suffix).
    if moved:
        reasons.append(f"moved-to:{registrable_base(moved)}"
                       if registrable_base(moved) != moved
                       else f"moved-to:{moved}")
    # Exa verdicts (dissimilar redirects only; None when skipped/offline).
    # For pointers (moved) this annotates the OLD domain; for known redirect
    # targets (redirect_from) it can rescue/demote below.
    exa_move_verdict = (_consult_exa(domain, moved, school_name, country_iso,
                                     exa_verify_fn) if moved else None)
    exa_target_verdict = (
        _consult_exa(redirect_from or "", domain, school_name, country_iso,
                     exa_verify_fn)
        if (redirect_from and not moved) else None)
    # Service endpoints (webmail, LMS, meeting links) are never the
    # institution's website: force Inaccessible regardless of threshold so a
    # lowered `active_threshold` can never promote them (see spotcheck
    # `mail2.sysu.edu.cn Active` regression).
    if is_service_host(domain) or (moved and is_service_host(moved)):
        conf = min(conf, 40)
        reasons.append("service-host")
        suffix = _exa_suffix(exa_move_verdict or exa_target_verdict)
        if suffix:
            reasons.append(suffix.lstrip("+"))
        out_svc: dict = {
            "status": "Inaccessible", "confidence": conf,
            "reason": "low-confidence:" + "+".join(reasons), "code": code,
            "final_domain": final_host, "moved_to": moved, "language": lang}
        if (exa_move_verdict or exa_target_verdict) is not None:
            out_svc["exa"] = exa_move_verdict or exa_target_verdict
        return out_svc
    # Cross-domain moves are pointers, never the site itself: the old domain
    # is Inaccessible here; the caller (`verify._mark_moved`/`_handle_move`)
    # records the pointer and validates the target as its own row. This
    # matches meta-refresh handling above and avoids Active+moved rows that
    # previously leaked into spotcheck logs.
    if moved:
        conf = min(conf, 40)
        suffix = _exa_suffix(exa_move_verdict)
        if suffix:
            reasons.append(suffix.lstrip("+"))
        out_mv: dict = {"status": "Inaccessible", "confidence": conf,
                        "reason": "+".join(reasons), "code": code,
                        "final_domain": final_host, "moved_to": moved, "language": lang}
        if exa_move_verdict is not None:
            out_mv["exa"] = exa_move_verdict
        return out_mv
    # Known redirect target reached via a dissimilar hop (e.g. royalholloway
    # validated after rhul.ac.uk -> royalholloway.ac.uk): Exa arbitrates when
    # local heuristics are uncertain. Hard parking/soft-404 already returned
    # above, so only low-confidence rescue vs Active demotion apply here —
    # and service-hosts never promote (handled above).
    if exa_target_verdict is not None:
        verified = exa_target_verdict.get("verified")
        suffix = _exa_suffix(exa_target_verdict)
        if verified is True and conf < active_threshold:
            # Rescue: local heuristics thin (JS shell / bot-block) but Exa
            # independently indexes the final domain as the institution.
            reasons.append(suffix.lstrip("+") or "exa-verified")
            conf = min(max(conf, active_threshold), 100)
            return {"status": "Active", "confidence": conf,
                    "reason": "+".join(reasons), "code": code,
                    "final_domain": final_host, "moved_to": moved,
                    "exa": exa_target_verdict}
        if verified is False and conf >= active_threshold:
            # Demote: local scoring passed but Exa sees parking content.
            if suffix:
                reasons.append(suffix.lstrip("+"))
            conf = min(conf, 40)
            return {"status": "Inaccessible", "confidence": conf,
                    "reason": "low-confidence:" + "+".join(reasons),
                    "code": code,
                    "final_domain": final_host, "moved_to": moved,
                    "exa": exa_target_verdict}
        # Corroboration (already-Active + exa-verified, already-low +
        # exa-parking) or inconclusive: keep local verdict, record evidence.
        if suffix:
            reasons.append(suffix.lstrip("+"))
        if conf >= active_threshold:
            conf = min(conf, 100)
            return {"status": "Active", "confidence": conf,
                    "reason": "+".join(reasons), "code": code,
                    "final_domain": final_host, "moved_to": moved,
                    "exa": exa_target_verdict}
        return {"status": "Inaccessible", "confidence": conf,
                "reason": "low-confidence:" + "+".join(reasons), "code": code,
                "final_domain": final_host, "moved_to": moved,
                "exa": exa_target_verdict}
    conf = min(conf, 100)
    if conf >= active_threshold:
        return {"status": "Active", "confidence": conf,
                "reason": "+".join(reasons), "code": code,
                "final_domain": final_host, "moved_to": moved, "language": lang}
    low_reason = "low-confidence:" + "+".join(reasons)
    fb = _apply_exa_fallback(domain, school_name, country_iso,
                             exa_fallback_fn, local_reason=low_reason,
                             local_code=code, local_final=final_host,
                             active_threshold=active_threshold)
    if fb is not None:
        return fb
    return {"status": "Inaccessible", "confidence": conf,
            "reason": low_reason, "code": code,
            "final_domain": final_host, "moved_to": moved, "language": lang}
