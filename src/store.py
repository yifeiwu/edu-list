"""Per-country CSV store + run state.

CSV schema: school_name,web_domain,type,last_visited,status,sources,years_registered
- web_domain: canonical registrable host, sorted within each file.
- sources: ';'-separated union of citations, first-seen order.
- status: Active | Inaccessible (non-2xx always Inaccessible).
- last_visited: YYYY-MM-DD of last check (new or re-verify, UTC).
- years_registered: whole years since domain registration (RDAP/WHOIS),
  "" when unknown. Informational only — never gates status.

Internal quality tracking (NOT in CSV) lives in state/state.json:
  failures: {domain: consecutive Inaccessible count}
  moved: {domain: target} for cross-domain pointers (excluded from archive math)
  confidence/reason: last validation detail per domain.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import tempfile
from pathlib import Path

FIELDS = ["school_name", "web_domain", "type", "last_visited", "status",
          "sources", "years_registered"]
VALID_STATUS = {"Active", "Inaccessible"}
VALID_TYPES = {"k-12", "university/college", "other"}


def today_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).date().isoformat()


def _atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp-")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except Exception:
            pass
        raise


def _scrub_stale_reasons(detail: dict) -> None:
    """Drop pre-strict-TLS `tls-unverified` fragments from persisted reasons."""
    for info in (detail or {}).values():
        if not isinstance(info, dict):
            continue
        reason = str(info.get("reason", ""))
        if "tls-unverified" not in reason:
            continue
        parts = [p for p in reason.split("+") if p and p != "tls-unverified"]
        info["reason"] = "+".join(parts) or "http-2xx-html"


def load_state(path: Path) -> dict:
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("cursors", {})
                data.setdefault("failures", {})
                data.setdefault("detail", {})
                data.setdefault("moved", {})
                data.setdefault("domain_age", {})
                data.setdefault("last_run", "")
                # Drop legacy keys from early schema versions.
                data.pop("next_idx", None)
                data.pop("per_country_last_discovery", None)
                _scrub_stale_reasons(data.get("detail", {}))
                return data
        except Exception:
            # Corrupt state: keep a backup, start fresh (never crash a run).
            try:
                path.rename(path.with_suffix(".corrupt.json"))
            except Exception:
                pass
    return {"cursors": {}, "failures": {}, "detail": {}, "moved": {},
            "domain_age": {}, "last_run": ""}


def save_state(path: Path, state: dict) -> None:
    state.pop("next_idx", None)
    state.pop("per_country_last_discovery", None)
    state["last_run"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    _atomic_write_text(path, json.dumps(state, indent=2, sort_keys=True))


def _country_path(countries_dir: Path, iso2: str) -> Path:
    iso = (iso2 or "XX").upper()
    if len(iso) != 2 or not iso.isalpha():
        iso = "XX"
    return countries_dir / f"{iso}.csv"


def _write_country(countries_dir: Path, iso2: str, rows: list[dict]) -> None:
    countries_dir.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: r["web_domain"])
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS)
    w.writeheader()
    for r in rows:
        w.writerow({k: r.get(k, "") for k in FIELDS})
    _atomic_write_text(_country_path(countries_dir, iso2), buf.getvalue())


def load_all(countries_dir: Path) -> tuple[dict[str, tuple[str, dict]], dict[str, list[dict]]]:
    """Returns (by_domain {domain: (iso2, row)}, buckets {iso2: [rows]})."""
    by_domain: dict[str, tuple[str, dict]] = {}
    buckets: dict[str, list[dict]] = {}
    if not countries_dir.exists():
        return by_domain, buckets
    for csv_path in sorted(countries_dir.glob("*.csv")):
        iso = csv_path.stem.upper()
        if len(iso) != 2 or not iso.isalpha():
            continue
        try:
            with open(csv_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:
                    continue
                for row in reader:
                    d = (row.get("web_domain") or "").strip().lower()
                    if not d:
                        continue
                    # `or ""` keeps pre-years_registered CSVs loading cleanly.
                    clean = {k: (row.get(k) or "") for k in FIELDS}
                    clean["web_domain"] = d
                    if clean.get("status") not in VALID_STATUS:
                        continue
                    if clean.get("type") not in VALID_TYPES:
                        clean["type"] = "other"
                    try:
                        if clean.get("last_visited"):
                            dt.date.fromisoformat(clean["last_visited"])
                    except ValueError:
                        clean["last_visited"] = "2000-01-01"
                    buckets.setdefault(iso, []).append(clean)
                    if d not in by_domain:
                        by_domain[d] = (iso, clean)
        except Exception:
            continue
    return by_domain, buckets


def save_touched(countries_dir: Path, buckets: dict[str, list[dict]],
                 touched: set[str]) -> None:
    for iso in touched:
        _write_country(countries_dir, iso, buckets.get(iso, []))


def purge_blocklisted(by_domain: dict, buckets: dict, state: dict,
                      blocklist: set[str]) -> set[str]:
    """Remove blocklisted domains from buckets/by_domain/state.

    Returns touched country codes so callers rewrite only affected files.
    """
    if not blocklist:
        return set()
    bl = {b.lower().strip(".") for b in blocklist if b}
    touched: set[str] = set()
    for d in [k for k in by_domain if k.lower() in bl]:
        iso, _row = by_domain.pop(d)
        touched.add(iso)
        if iso in buckets:
            buckets[iso] = [r for r in buckets[iso] if r.get("web_domain") != d]
        for key in ("failures", "detail", "moved", "domain_age"):
            try:
                state.get(key, {}).pop(d, None)
            except Exception:
                pass
    return touched


def write_index(index_path: Path, buckets: dict[str, list[dict]]) -> None:
    lines = ["# Institutions by country", "",
             "| country | total | Active | Inaccessible |",
             "|---|---|---|---|"]
    for iso in sorted(buckets):
        rows = buckets[iso]
        a = sum(1 for r in rows if r.get("status") == "Active")
        lines.append(f"| {iso} | {len(rows)} | {a} | {len(rows) - a} |")
    total = sum(len(v) for v in buckets.values())
    lines += ["", f"Total domains: {total}. Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`."]
    _atomic_write_text(index_path, "\n".join(lines) + "\n")


# --- Pending queue -----------------------------------------------------------
# Newly discovered, not-yet-validated candidates live here (NOT in the CSVs).
# Entry: {name, url, domain, iso2, type_hint, source} with `source` already
# `;`-unioned across every discovery that cited it.

def load_pending(path: Path) -> list[dict]:
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return [e for e in data if isinstance(e, dict) and e.get("domain")]
        except Exception:
            try:
                path.rename(path.with_suffix(".corrupt.json"))
            except Exception:
                pass
    return []


def save_pending(path: Path, items: list[dict]) -> None:
    _atomic_write_text(path, json.dumps(items, indent=1, sort_keys=True))
