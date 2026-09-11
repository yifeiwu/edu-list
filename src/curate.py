#!/usr/bin/env python3
"""Curate (discovery) pipeline — the rate-limit-sensitive half.

Fetches 1-2 rotating upstream sources (Wikidata, Overpass, ROR, crt.sh, …),
normalizes candidates and appends NEW domains to the pending queue
(`state/pending.json`). Already-known domains just get their `sources`
column unioned (re-citation). Performs NO website validation.

Run: python src/curate.py --config config.yaml --sources sources.yaml
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

from src import discover  # noqa: E402
from src.store import (  # noqa: E402
    load_all, load_pending, load_state, migrate_legacy, save_pending,
    save_state, save_touched, write_index,
)
from src.util import (  # noqa: E402
    country_from_suffix, normalize_domain, union_sources,
)

ADAPTERS = {
    "hipo": lambda u, s, n, t: discover.discover_hipo(u, s, n, t),
    "ror": lambda u, s, n, t: discover.discover_ror(u, s, n, t),
    "openalex": lambda u, s, n, t: discover.discover_openalex(u, s, n, t),
    "wikidata": lambda u, s, n, t: discover.discover_wikidata(u, s, n, t),
    "eter": lambda u, s, n, t: discover.discover_csv_generic(u, s, n, "eter", t),
    "scorecard": lambda u, s, n, t: discover.discover_scorecard(u, s, n, t),
    "gias": lambda u, s, n, t: discover.discover_csv_generic(u, s, n, "gias", t),
    "france-annuaire": lambda u, s, n, t: discover.discover_france_annuaire(u, s, n, t),
    "france-sup": lambda u, s, n, t: discover.discover_csv_generic(u, s, n, "france-sup", t),
    "ugc-in": lambda u, s, n, t: discover.discover_ugc(u, s, n, t),
    "osm": lambda u, s, n, t: discover.discover_osm(u, s, n, t),
    "giga": lambda u, s, n, t: discover.discover_stub(u, s, n, "giga"),
    "crtsh": lambda u, s, n, t: discover.discover_crtsh(u, s, n, t),
    "whed": lambda u, s, n, t: discover.discover_whed(u, s, n, t),
    "edudirectory": lambda u, s, n, t: discover.discover_stub(u, s, n, "edudirectory"),
    "commoncrawl": lambda u, s, n, t: discover.discover_commoncrawl(u, s, n, t),
}


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}] {msg}",
          flush=True)


def load_cfg(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def pick_sources(sources: list[dict], state: dict, k12: bool,
                 forced: str = "") -> list[dict]:
    if forced:
        return [s for s in sources if s["id"] == forced]
    enabled = [s for s in sources
               if s.get("enabled") and (k12 or s["id"] not in
               ("gias", "osm", "giga"))]
    if not enabled:
        return []
    idx = int(state.get("next_idx", 0))
    # 2 sources per run: throughput without hammering any single upstream.
    picks = [enabled[(idx + i) % len(enabled)] for i in range(min(2, len(enabled)))]
    state["next_idx"] = (idx + len(picks)) % len(enabled)
    return picks


def run_curate(*, cfg: dict, src_cfg: dict, state: dict,
               by_domain: dict, buckets: dict, pending: list[dict],
               forced: str = "", deadline: float) -> dict:
    """Mutates state/by_domain/buckets/pending. Returns stats."""
    suffix_map = cfg.get("suffix_country", {})
    blocklist = set(cfg.get("blocklist", []))
    k12 = bool(cfg.get("k12_enabled", False))
    timeout = int(cfg.get("validation", {}).get("timeout_seconds", 10))
    max_pending = int(cfg.get("run", {}).get("max_pending", 8000))

    pending_idx = {e["domain"]: i for i, e in enumerate(pending)}
    touched: set[str] = set()
    raw, new, recited = 0, 0, 0

    for src in pick_sources(src_cfg.get("sources", []), state, k12, forced):
        sid = src["id"]
        fn = ADAPTERS.get(sid)
        if not fn:
            continue
        log(f"Discover: {sid} (per_run {src.get('per_run')})…")
        try:
            cands = fn(src.get("url", ""), state,
                       int(src.get("per_run", 300)), timeout) or []
        except Exception as e:  # never fail a run on one source
            log(f"  {sid} error: {type(e).__name__}, skipping")
            continue
        log(f"  -> {len(cands)} raw candidates")
        raw += len(cands)
        for c in cands:
            d = normalize_domain(c.get("url", ""))
            if not d or d in blocklist:
                continue
            iso = (c.get("iso2") or "").upper()
            if len(iso) != 2:
                iso = country_from_suffix(d, suffix_map) or "XX"
            if d in by_domain:
                # Re-citation of a validated row: union sources, no re-queue.
                iso0, row0 = by_domain[d]
                merged = union_sources(row0.get("sources", ""), c.get("source", ""))
                if merged != row0.get("sources", ""):
                    row0["sources"] = merged
                    touched.add(iso0)
                    recited += 1
            elif d in pending_idx:
                prev = pending[pending_idx[d]]
                prev["source"] = union_sources(prev.get("source", ""),
                                              c.get("source", ""))
                if len(c.get("name", "")) > len(prev.get("name", "")):
                    prev["name"] = c["name"]
            else:
                if len(pending) >= max_pending:
                    log(f"  pending full ({max_pending}), deferring rest")
                    break
                pending.append({
                    "name": c.get("name") or d,
                    "url": c.get("url", ""),
                    "domain": d,
                    "iso2": iso,
                    "type_hint": c.get("type_hint", ""),
                    "source": c.get("source", ""),
                })
                pending_idx[d] = len(pending) - 1
                new += 1
            time.sleep(0.02)
        if time.time() > deadline:
            break

    return {"raw": raw, "new": new, "recited": recited, "touched": touched}


def main() -> int:
    ap = argparse.ArgumentParser(description="Discover new school domains (no validation).")
    ap.add_argument("--config", default=str(ROOT / "config.yaml"))
    ap.add_argument("--sources", default=str(ROOT / "sources.yaml"))
    ap.add_argument("--source", default="", help="Force one discovery source id")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_cfg(Path(args.config))
    src_cfg = load_cfg(Path(args.sources))
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
    stats = run_curate(cfg=cfg, src_cfg=src_cfg, state=state,
                       by_domain=by_domain, buckets=buckets, pending=pending,
                       forced=args.source, deadline=deadline)

    if args.dry_run:
        log(f"DRY-RUN: raw={stats['raw']} new_queued={stats['new']} "
            f"recited={stats['recited']}")
        return 0
    save_touched(countries_dir, buckets, stats["touched"])
    _, buckets_now = load_all(countries_dir)
    write_index(index_path, buckets_now)
    save_pending(pending_path, pending)
    save_state(state_path, state)
    log(f"Done. raw={stats['raw']} new_queued={stats['new']} "
        f"recited={stats['recited']} pending_total={len(pending)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
