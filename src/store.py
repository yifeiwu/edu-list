"""Per-country CSV store + run state.

CSV schema (locked): school_name,web_domain,type,last_visited,status,sources
- web_domain: canonical registrable host, sorted within each file.
- sources: ';'-separated union of citations, first-seen order.
- status: Active | Inaccessible (non-2xx always Inaccessible).
- last_visited: YYYY-MM-DD of last check (new or re-verify).

Internal quality tracking (NOT in CSV) lives in state/state.json:
  failures: {domain: consecutive Inaccessible count}
  confidence/reason: last validation detail per domain.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
from pathlib import Path

from .util import normalize_domain, union_sources

FIELDS = ["school_name", "web_domain", "type", "last_visited", "status", "sources"]


def today_iso() -> str:
    return dt.date.today().isoformat()


def load_state(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"cursors": {}, "next_idx": 0, "failures": {}, "detail": {},
            "last_run": "", "per_country_last_discovery": {}}


def save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    state["last_run"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    path.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def migrate_legacy(legacy_csv: Path, countries_dir: Path) -> int:
    """One-off: split data/institutions.csv (old 7-col schema) into countries/."""
    if not legacy_csv.exists():
        return 0
    if any(countries_dir.glob("*.csv")):
        return 0
    moved = 0
    try:
        rows = list(csv.DictReader(legacy_csv.read_text(encoding="utf-8").splitlines()))
    except Exception:
        return 0
    buckets: dict[str, list[dict]] = {}
    for r in rows:
        d = normalize_domain(r.get("domain", ""))
        if not d:
            continue
        cc = (r.get("country") or "").strip().upper()
        cc = cc if len(cc) == 2 else {"US": "US", "GB": "GB"}.get(cc, "XX")
        buckets.setdefault(cc, []).append({
            "school_name": r.get("name") or d,
            "web_domain": d,
            "type": {"university": "university/college", "college": "university/college",
                     "school": "k-12"}.get((r.get("type") or "").lower(), "other"),
            "last_visited": r.get("last_checked") or today_iso(),
            "status": "Active",
            "sources": r.get("source") or "legacy",
        })
        moved += 1
    for cc, lst in buckets.items():
        _write_country(countries_dir, cc, lst)
    return moved


def _country_path(countries_dir: Path, iso2: str) -> Path:
    iso = (iso2 or "XX").upper()
    if len(iso) != 2 or not iso.isalpha():
        iso = "XX"
    return countries_dir / f"{iso}.csv"


def _write_country(countries_dir: Path, iso2: str, rows: list[dict]) -> None:
    countries_dir.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: r["web_domain"])
    with open(_country_path(countries_dir, iso2), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)


def load_all(countries_dir: Path) -> tuple[dict[str, tuple[str, dict]], dict[str, list[dict]]]:
    """Returns (by_domain {domain: (iso2, row)}, buckets {iso2: [rows]})."""
    by_domain: dict[str, tuple[str, dict]] = {}
    buckets: dict[str, list[dict]] = {}
    if not countries_dir.exists():
        return by_domain, buckets
    for csv_path in sorted(countries_dir.glob("*.csv")):
        iso = csv_path.stem.upper()
        try:
            with open(csv_path, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    d = (row.get("web_domain") or "").strip().lower()
                    if not d:
                        continue
                    clean = {k: row.get(k, "") for k in FIELDS}
                    clean["web_domain"] = d
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


def write_index(index_path: Path, buckets: dict[str, list[dict]]) -> None:
    lines = ["# Institutions by country", "",
             "| country | total | Active | Inaccessible |",
             "|---|---|---|---|"]
    for iso in sorted(buckets):
        rows = buckets[iso]
        a = sum(1 for r in rows if r.get("status") == "Active")
        lines.append(f"| {iso} | {len(rows)} | {a} | {len(rows) - a} |")
    total = sum(len(v) for v in buckets.values())
    lines += ["", f"Total domains: {total}. Schema: `school_name,web_domain,type,last_visited,status,sources`."]
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
            pass
    return []


def save_pending(path: Path, items: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(items, indent=1, sort_keys=True), encoding="utf-8")
