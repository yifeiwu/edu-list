#!/usr/bin/env python3
"""Legacy all-in-one entrypoint: curate (discover) then verify, sequentially.

Prefer the split pipelines in production:
  - src/curate.py  (hourly at :00; upstream sources, rate-limit-sensitive)
  - src/verify.py   (hourly at :30; individual websites, distributed load)

This wrapper preserves the old `python src/crawl.py` behavior for local runs.
It delegates to run_curate/run_verify (single implementation, no fork).
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.cli_common import (  # noqa: E402
    ROOT as CLI_ROOT,
    apply_contact,
    assert_configured_contact,
    load_cfg,
    load_runtime,
    log,
    resolve_paths,
    save_runtime,
)
from src.curate import run_curate  # noqa: E402
from src.verify import run_verify  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description="Curate then verify (legacy all-in-one).")
    ap.add_argument("--config", default=str(CLI_ROOT / "config.yaml"))
    ap.add_argument("--sources", default=str(CLI_ROOT / "sources.yaml"))
    ap.add_argument("--limit", type=int, default=0,
                    help="Max verifications (0 = use config).")
    ap.add_argument("--source", default="", help="Force one discovery source id")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-network", action="store_true",
                    help="Skip all network fetches (for tests/offline).")
    args = ap.parse_args()

    cfg = load_cfg(Path(args.config))
    src_cfg = load_cfg(Path(args.sources))
    if not args.dry_run and not args.no_network:
        assert_configured_contact(cfg)
    run = cfg.get("run", {})
    paths = resolve_paths(cfg)

    state, by_domain, buckets, pending = load_runtime(
        paths["state_path"], paths["countries_dir"], paths["pending_path"])
    log(f"Loaded {len(by_domain)} domains, {len(pending)} pending")

    if args.no_network:
        log("NO-NETWORK: skipping curate+verify network work")
        return 0

    apply_contact(cfg, src_cfg)
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
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    state["last_curate"] = {"at": now, "raw": cstats["raw"],
                            "new": cstats["new"],
                            "recited": cstats["recited"],
                            "unmapped": cstats.get("unmapped", 0),
                            "skipped_service": cstats.get("skipped_service", 0)}
    state["last_verify"] = {"at": now, "validated": vstats["validated"],
                            "added_active": vstats["added_active"],
                            "reverified": vstats["reverified"],
                            "pending_left": vstats["pending_left"]}
    save_runtime(countries_dir=paths["countries_dir"], buckets=buckets,
                 touched=touched, index_path=paths["index_path"],
                 pending_path=paths["pending_path"], pending=pending,
                 state_path=paths["state_path"], state=state,
                 archive_after=int(run.get("archive_after_failures", 6)))
    log(f"Done. validated={vstats['validated']} "
        f"added_active={vstats['added_active']} "
        f"reverified={vstats['reverified']} touched={sorted(touched)} "
        f"pending_left={vstats['pending_left']} total={len(by_domain)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
