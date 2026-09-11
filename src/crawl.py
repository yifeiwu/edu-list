#!/usr/bin/env python3
"""Legacy all-in-one entrypoint: curate (discover) then verify, sequentially.

Prefer the split pipelines in production:
  - src/curate.py  (daily; upstream sources, rate-limit-sensitive)
  - src/verify.py   (2x daily; individual websites, distributed load)

This wrapper preserves the old `python src/crawl.py` behavior for local runs.
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

from src.curate import run_curate  # noqa: E402
from src.store import (  # noqa: E402
    load_all, load_pending, load_state, migrate_legacy, save_pending,
    save_state, save_touched, write_index,
)
from src.verify import run_verify  # noqa: E402


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}] {msg}",
          flush=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Curate then verify (legacy all-in-one).")
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--sources", default=str(ROOT / "sources.yaml"))
    ap.add_argument("--limit", type=int, default=0,
                    help="Max verifications (0 = use config).")
    ap.add_argument("--source", default="", help="Force one discovery source id")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    with open(args.sources, encoding="utf-8") as f:
        src_cfg = yaml.safe_load(f) or {}
    run = cfg.get("run", {})
    out = cfg.get("output", {})
    countries_dir = ROOT / out.get("countries_dir", "data/countries")
    index_path = ROOT / out.get("index_path", "data/countries/INDEX.md")
    state_path = ROOT / cfg.get("state_path", "state/state.json")
    pending_path = state_path.parent / "pending.json"

    state = load_state(state_path)
    if not args.dry_run:
        migrated = migrate_legacy(ROOT / "data" / "institutions.csv", countries_dir)
        if migrated:
            log(f"Migrated {migrated} legacy rows into {countries_dir}")
    by_domain, buckets = load_all(countries_dir)
    pending = load_pending(pending_path)
    log(f"Loaded {len(by_domain)} domains, {len(pending)} pending")

    deadline = time.time() + int(run.get("max_seconds", 2700))

    cstats = run_curate(cfg=cfg, src_cfg=src_cfg, state=state,
                        by_domain=by_domain, buckets=buckets, pending=pending,
                        forced=args.source, deadline=deadline)
    log(f"Curate: raw={cstats['raw']} new_queued={cstats['new']} "
        f"recited={cstats['recited']}")

    vstats = run_verify(cfg=cfg, state=state, by_domain=by_domain,
                        buckets=buckets, pending=pending, limit=args.limit,
                        deadline=deadline)
    touched = set(cstats["touched"]) | set(vstats["touched"])

    if args.dry_run:
        log(f"DRY-RUN: validated={vstats['validated']} "
            f"added_active={vstats['added_active']} "
            f"reverified={vstats['reverified']}")
        return 0
    save_touched(countries_dir, buckets, touched)
    _, buckets_now = load_all(countries_dir)
    write_index(index_path, buckets_now)
    save_pending(pending_path, pending)
    save_state(state_path, state)
    log(f"Done. validated={vstats['validated']} "
        f"added_active={vstats['added_active']} "
        f"reverified={vstats['reverified']} touched={sorted(touched)} "
        f"pending_left={vstats['pending_left']} total={len(by_domain)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
