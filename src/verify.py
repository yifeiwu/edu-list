#!/usr/bin/env python3
"""Verify pipeline — the rate-limit-safe half.

Validates websites ONE domain at a time (each site hit once, homepage only,
polite UA + delay), so it never hammers any single host and can run more
frequently than curation. Order per run:
  1. Drain NEW items from the pending queue (FIFO).
  2. If budget remains: re-verify existing rows — small piggyback batch when
     new domains were validated, else the full oldest-N batch.

Run: python src/verify.py --config config.yaml --limit 800
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.store import (  # noqa: E402
    load_all, load_pending, load_state, save_pending, save_state,
    save_touched, today_iso, write_index,
)
from src.util import classify_type  # noqa: E402
from src.validate import validate_site  # noqa: E402


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}] {msg}",
          flush=True)


def load_cfg(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def check(domain: str, name: str, iso: str, multisrc: bool, vcfg: dict) -> tuple[str, dict]:
    res = validate_site(f"https://{domain}", domain, iso,
                        vcfg["timeout"], vcfg["ua"], vcfg["max_bytes"],
                        multisource=multisrc, politeness=vcfg["polite"])
    # Locked rule: non-2xx is ALWAYS Inaccessible regardless of score.
    active = (res["status"] == "Active"
              and 200 <= int(res.get("code", 0)) < 300
              and res.get("confidence", 0) >= vcfg["threshold"])
    return ("Active" if active else "Inaccessible"), res


def run_verify(*, cfg: dict, state: dict, by_domain: dict, buckets: dict,
               pending: list[dict], limit: int = 0, new_only: bool = False,
               reverify_only: bool = False, deadline: float) -> dict:
    run = cfg.get("run", {})
    v = cfg.get("verify", {}) or {}
    vcfg = {
        "timeout": int(cfg.get("validation", {}).get("timeout_seconds", 10)),
        "max_bytes": int(cfg.get("validation", {}).get("max_bytes", 32768)),
        "ua": cfg.get("validation", {}).get("user_agent", "edu-domains-bot/1.0"),
        "threshold": int(cfg.get("validation", {}).get("active_threshold", 50)),
        "polite": float(cfg.get("validation", {}).get("politeness_delay_seconds", 0.4)),
    }
    max_val = limit or int(v.get("max_validations", run.get("max_validations", 600)))
    max_new = int(v.get("max_new_per_run", run.get("max_new_per_run", 500)))
    batch_no_new = int(v.get("verify_batch_no_new", run.get("verify_batch_no_new", 500)))
    batch_with_new = int(v.get("verify_batch_with_new",
                               run.get("verify_batch_with_new", 100)))
    archive_after = int(run.get("archive_after_failures", 6))
    archive_skip = int(run.get("archive_skip_days", 90))

    failures = state.setdefault("detail", {})
    failcounts = state.setdefault("failures", {})
    touched: set[str] = set()
    validated = added = reverified = 0

    # 1) Drain pending queue (FIFO).
    if not reverify_only:
        n = 0
        while pending and n < max_new and validated < max_val \
                and time.time() < deadline:
            c = pending.pop(0)
            d = c["domain"]
            if d in by_domain:
                continue  # validated by an overlapping run; drop duplicate
            iso = c.get("iso2", "XX")
            multisrc = ";" in (c.get("source", ""))
            status, res = check(d, c.get("name", d), iso, multisrc, vcfg)
            row = {"school_name": c.get("name") or d, "web_domain": d,
                   "type": classify_type(c.get("name", ""), d,
                                         c.get("type_hint", "")),
                   "last_visited": today_iso(), "status": status,
                   "sources": c.get("source", "")}
            buckets.setdefault(iso, []).append(row)
            by_domain[d] = (iso, row)
            touched.add(iso)
            failures[d] = {"confidence": res.get("confidence", 0),
                           "reason": res.get("reason", ""),
                           "code": res.get("code", 0)}
            failcounts[d] = 0 if status == "Active" \
                else int(failcounts.get(d, 0)) + 1
            validated += 1
            n += 1
            if status == "Active":
                added += 1
            if validated % 50 == 0:
                log(f"  validated {validated}: {d} -> {status} ({res.get('reason')})")

    # 2) Re-verify existing rows.
    new_found = validated > 0
    if not new_only and validated < max_val and time.time() < deadline:
        batch = batch_with_new if new_found else batch_no_new
        log(f"{'New validated — piggyback' if new_found else 'Queue empty — full'} "
            f"re-verify of oldest {batch}")
        today = dt.date.today()
        cands: list[tuple[int, str]] = []
        for d, (iso, row) in by_domain.items():
            try:
                age = (today - dt.date.fromisoformat(
                    row.get("last_visited", "2000-01-01"))).days
            except ValueError:
                age = 9999
            if int(failcounts.get(d, 0)) >= archive_after and age < archive_skip:
                continue  # archived chronic failure; keep row, skip checks
            cands.append((age, d))
        cands.sort(reverse=True)
        for _, d in cands[:batch]:
            if validated >= max_val or time.time() > deadline:
                break
            iso, row = by_domain[d]
            multisrc = ";" in (row.get("sources", ""))
            status, res = check(d, row["school_name"], iso, multisrc, vcfg)
            row["last_visited"] = today_iso()
            row["status"] = status
            failures[d] = {"confidence": res.get("confidence", 0),
                           "reason": res.get("reason", ""),
                           "code": res.get("code", 0)}
            failcounts[d] = 0 if status == "Active" \
                else int(failcounts.get(d, 0)) + 1
            touched.add(iso)
            validated += 1
            reverified += 1

    return {"validated": validated, "added_active": added,
            "reverified": reverified, "touched": touched,
            "pending_left": len(pending)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate queued + existing school websites.")
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--limit", type=int, default=0,
                    help="Max validations (0 = use config).")
    ap.add_argument("--new-only", action="store_true",
                    help="Only drain pending queue, skip re-verification.")
    ap.add_argument("--reverify-only", action="store_true",
                    help="Skip pending queue, only re-verify existing rows.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_cfg(Path(args.config))
    run = cfg.get("run", {})
    out = cfg.get("output", {})
    countries_dir = ROOT / out.get("countries_dir", "data/countries")
    index_path = ROOT / out.get("index_path", "data/countries/INDEX.md")
    state_path = ROOT / cfg.get("state_path", "state/state.json")
    pending_path = state_path.parent / "pending.json"

    state = load_state(state_path)
    by_domain, buckets = load_all(countries_dir)
    pending = load_pending(pending_path)
    log(f"Loaded {len(by_domain)} domains, {len(pending)} pending")

    deadline = time.time() + int(run.get("max_seconds", 2700))
    stats = run_verify(cfg=cfg, state=state, by_domain=by_domain,
                       buckets=buckets, pending=pending, limit=args.limit,
                       new_only=args.new_only, reverify_only=args.reverify_only,
                       deadline=deadline)

    if args.dry_run:
        log(f"DRY-RUN: validated={stats['validated']} "
            f"added_active={stats['added_active']} "
            f"reverified={stats['reverified']} "
            f"pending_left={stats['pending_left']}")
        return 0
    save_touched(countries_dir, buckets, stats["touched"])
    _, buckets_now = load_all(countries_dir)
    write_index(index_path, buckets_now)
    save_pending(pending_path, pending)
    save_state(state_path, state)
    log(f"Done. validated={stats['validated']} "
        f"added_active={stats['added_active']} "
        f"reverified={stats['reverified']} touched={sorted(stats['touched'])} "
        f"pending_left={stats['pending_left']} total={len(by_domain)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
