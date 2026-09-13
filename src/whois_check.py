"""WHOIS-via-RDAP registration-age check (stdlib + requests only).

Why RDAP, not port-43 WHOIS: RDAP returns structured JSON with a
machine-readable `registration` event, while WHOIS text needs per-registry
parsing and many ccTLD servers throttle aggressively. Authoritative server
per TLD comes from the IANA bootstrap file (cached per process); rdap.org
is the fallback aggregator.

Best-effort by design: any failure (no RDAP service, redacted data,
timeout, rate-limit) returns None and the CSV keeps an empty
`years_registered` cell. It NEVER flips Active/Inaccessible — age is
informational curation data, not a validity gate.
"""
from __future__ import annotations

import datetime as dt
import re
import socket

import requests

UA = {"User-Agent": "edu-domains-bot/1.0 (github-actions; educational-research)",
      "Accept": "application/rdap+json, application/json"}

IANA_BOOTSTRAP = "https://data.iana.org/rdap/dns.json"
RDAP_FALLBACK = "https://rdap.org/domain/"

# Port-43 WHOIS servers for academic zones with no usable RDAP
# (.edu has no RDAP at all; Nominet's RDAP 404s many .uk domains).
WHOIS_PORT43 = {
    "edu": "whois.educause.edu",
    "uk": "whois.nic.uk",
}

_DATE_FORMATS = (
    "%d-%b-%Y", "%d-%b-%Y %H:%M:%S", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%d %H:%M:%S", "%d/%m/%Y", "%m-%d-%Y", "%Y.%m.%d", "%d.%m.%Y",
    "%Y/%m/%d", "%b %d %Y", "%d %b %Y",
)
_WHOIS_DATE_RES = (
    r"Domain record activated\s*:\s*(.+)",
    r"Creation Date\s*:?\s*(.+)",
    r"Created\s*(?:on|date)?\s*:?\s*(.+)",
    r"Registered on\s*:?\s*(.+)",
    r"Registration Time\s*:?\s*(.+)",
    r"Domain Registration Date\s*:?\s*(.+)",
)

_bootstrap: dict | None = None


def _get_bootstrap(timeout: int = 20) -> dict:
    global _bootstrap
    if _bootstrap is None:
        r = requests.get(IANA_BOOTSTRAP, headers={"User-Agent": UA["User-Agent"]},
                         timeout=timeout)
        r.raise_for_status()
        _bootstrap = r.json()
    return _bootstrap


def rdap_base_for(domain: str, timeout: int = 20) -> str | None:
    """Authoritative RDAP base URL for the domain's TLD (longest match)."""
    d = (domain or "").lower().strip(".")
    try:
        services = _get_bootstrap(timeout).get("services", [])
    except Exception:
        return None
    best: str | None = None
    best_len = -1
    for tlds, urls in services:
        if not urls:
            continue
        for t in tlds:
            t = t.lower()
            if (d == t or d.endswith("." + t)) and len(t) > best_len:
                base = urls[0]
                if not base.endswith("/"):
                    base += "/"
                best, best_len = base, len(t)
    return best


def parse_registration_date(rdap_obj: dict) -> dt.date | None:
    """Extract the `registration` event date from an RDAP response."""
    try:
        for ev in (rdap_obj or {}).get("events", []) or []:
            if str(ev.get("eventAction", "")).lower() == "registration":
                val = ev.get("eventDate", "")
                if val:
                    return dt.datetime.fromisoformat(
                        str(val).replace("Z", "+00:00")).date()
    except Exception:
        pass
    return None


def registration_date(domain: str, timeout: int = 8) -> dt.date | None:
    """Domain creation date: authoritative RDAP, rdap.org, then port-43."""
    d = (domain or "").lower().strip(".")
    if not d or "." not in d:
        return None
    urls = []
    base = rdap_base_for(d, timeout)
    if base:
        urls.append(f"{base}domain/{d}")
    urls.append(f"{RDAP_FALLBACK}{d}")
    for u in urls:
        try:
            r = requests.get(u, headers=UA, timeout=timeout)
            if r.status_code != 200:
                continue
            found = parse_registration_date(r.json())
            if found:
                return found
        except Exception:
            continue
    # Last resort: port-43 WHOIS for zones without usable RDAP.
    tld = d.rsplit(".", 1)[-1]
    server = WHOIS_PORT43.get(tld)
    if server:
        text = whois_text(server, d, timeout)
        if text:
            return parse_creation_date_whois(text)
    return None


def whois_text(server: str, domain: str, timeout: int = 8) -> str:
    """Raw port-43 WHOIS response ("" on any failure)."""
    try:
        with socket.create_connection((server, 43), timeout=timeout) as s:
            s.settimeout(timeout)
            s.sendall((domain + "\r\n").encode("ascii"))
            try:
                s.shutdown(socket.SHUT_WR)
            except OSError:
                pass
            chunks = []
            while True:
                b = s.recv(65536)
                if not b:
                    break
                chunks.append(b)
                if sum(map(len, chunks)) > 65536:
                    break
        return b"".join(chunks).decode("utf-8", errors="replace")
    except Exception:
        return ""


def _parse_date(value: str) -> dt.date | None:
    v = re.sub(r"\s*\(.*\)\s*$", "", (value or "").strip())
    v = re.sub(r"\.\d+(?=[+-]\d{2}:?\d{2}|Z?$)", "", v)  # fractional seconds
    try:
        return dt.datetime.fromisoformat(v.replace("Z", "+00:00")).date()
    except Exception:
        pass
    for fmt in _DATE_FORMATS:
        try:
            return dt.datetime.strptime(v, fmt).date()
        except Exception:
            continue
    m = re.search(r"(\d{4}-\d{2}-\d{2})", v)
    if m:
        try:
            return dt.date.fromisoformat(m.group(1))
        except Exception:
            return None
    return None


def parse_creation_date_whois(text: str) -> dt.date | None:
    """Creation date from WHOIS text via labeled-pattern battery."""
    for pat in _WHOIS_DATE_RES:
        m = re.search(pat, text or "", re.I | re.M)
        if m:
            found = _parse_date(m.group(1))
            if found:
                return found
    return None


def whole_years_since(reg: dt.date, today: dt.date) -> int | None:
    """Calendar whole years from `reg` to `today` (leap-aware)."""
    if reg is None or today is None or reg > today:
        return None
    years = today.year - reg.year
    if (today.month, today.day) < (reg.month, reg.day):
        years -= 1
    return max(years, 0)


NEGATIVE_CACHE_TTL_DAYS = 90


def _negative_cache_expired(entry: dict, today: dt.date) -> bool:
    """True when a timestamped negative-cache entry is older than TTL."""
    ts = str(entry.get("ts", "") or entry.get("failed_at", "") or "")
    if not ts:
        return True  # legacy untimestamped miss: retry once, then timestamp
    try:
        failed = dt.date.fromisoformat(ts[:10])
    except ValueError:
        return True
    return (today - failed).days >= NEGATIVE_CACHE_TTL_DAYS


def years_registered(domain: str, timeout: int = 8,
                     today: dt.date | None = None,
                     cache: dict | None = None) -> int | None:
    """Whole years since registration, or None when unknowable.

    When `cache` (state["domain_age"]) is given, ISO registration dates are
    reused across runs to avoid repeated RDAP/WHOIS lookups. Misses are
    negative-cached as `{"reg": "", "ts": "YYYY-MM-DD"}` and retried after
    `NEGATIVE_CACHE_TTL_DAYS` (90d). Legacy `""` misses are treated as
    expired so they retry once and upgrade to the timestamped form.
    """
    d = (domain or "").lower().strip(".")
    if not d or "." not in d:
        return None
    today = today or dt.date.today()
    if cache is not None and d in cache:
        raw = cache[d]
        if isinstance(raw, dict):
            iso = raw.get("reg", "")
            if iso:
                try:
                    return whole_years_since(dt.date.fromisoformat(iso), today)
                except ValueError:
                    pass
                # Corrupt positive entry: fall through to fresh lookup.
            elif not _negative_cache_expired(raw, today):
                return None
            # Expired (or legacy untimestamped) miss: fall through to retry.
        elif isinstance(raw, str) and raw:
            try:
                return whole_years_since(dt.date.fromisoformat(raw), today)
            except ValueError:
                pass
            # Corrupt string entry: fall through to fresh lookup.
        elif raw == "":
            # Legacy bare-string miss: always retry (then timestamp it).
            pass
        else:
            return None
    reg = registration_date(domain, timeout)
    if reg is None:
        if cache is not None:
            cache[d] = {"reg": "", "ts": today.isoformat()}
        return None
    if cache is not None:
        cache[d] = reg.isoformat()
    return whole_years_since(reg, today or dt.date.today())
