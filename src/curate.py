#!/usr/bin/env python3
"""Curate (discovery) pipeline — the rate-limit-sensitive half.

Hits EVERY enabled upstream source once per session (each capped by its
`sources.yaml` per_run), normalizes candidates and appends NEW domains to
the pending queue (`state/pending.json`). Already-known domains just get
their `sources` column unioned (re-citation). Performs NO website validation.

Service-host endpoints (webmail/LMS/meeting) are never queued: they can
never validate Active and would only waste verify budget.

Run: python src/curate.py --config config.yaml --sources sources.yaml
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src import discover  # noqa: E402
from src.cli_common import (  # noqa: E402
    ROOT as CLI_ROOT,
    apply_contact,
    assert_configured_contact,
    load_cfg,
    load_runtime,
    log,
    resolve_mailto,
    resolve_paths,
    resolve_user_agent,
    save_runtime,
)
from src.geo import merge_suffix_map  # noqa: E402
from src.store import purge_blocklisted  # noqa: E402
from src.util import (  # noqa: E402
    country_from_suffix, is_service_host, normalize_domain, union_sources,
)

# Re-export for backwards compat (tests import curate.log etc).
__all__ = ["ADAPTERS", "K12_SOURCES", "pick_sources", "run_curate", "main",
           "log", "load_cfg", "assert_configured_contact"]

# Active adapters only. Dormant sources (ugc-in, crtsh, commoncrawl,
# eter/gias/france-sup/giga/edudirectory) were deleted — see SOURCES.md.
# Untyped callables with mixed arity (openalex takes optional mailto).
ADAPTERS: dict = {
    "hipo": lambda src, s: discover.discover_hipo(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 30)),
    "ror": lambda src, s: discover.discover_ror(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 30)),
    "openalex": lambda src, s, mailto="": discover.discover_openalex(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 30),
        mailto=str(src.get("mailto", "") or mailto or discover.DEFAULT_MAILTO)),
    "wikidata": lambda src, s: discover.discover_wikidata(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 60)),
    "scorecard": lambda src, s: discover.discover_scorecard(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 120)),
    "france-annuaire": lambda src, s: discover.discover_france_annuaire(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 40)),
    "osm": lambda src, s: discover.discover_osm(
        src.get("url", ""), s, int(src.get("per_run", 200)),
        int(src.get("timeout_seconds") or 90),
        boxes=src.get("boxes")),
    "whed": lambda src, s: discover.discover_whed(
        src.get("url", ""), s, int(src.get("per_run", 10)),
        int(src.get("timeout_seconds") or 60)),
    "dotgov": lambda src, s: discover.discover_dotgov(
        src.get("url", ""), s, int(src.get("per_run", 100)),
        int(src.get("timeout_seconds") or 60)),
    "cricos": lambda src, s: discover.discover_cricos(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 120),
        package_id=str(src.get("package_id") or
                       "e5ae7059-bfa8-4fa4-a5c0-c13cf3520193"),
        resource_name=str(src.get("resource_name") or "CRICOS Institutions.csv")),
    "nuc-ng": lambda src, s: discover.discover_nuc_ng(
        src.get("url", ""), s, int(src.get("per_run", 400)),
        int(src.get("timeout_seconds") or 60)),
    "nz-schools": lambda src, s: discover.discover_nz_schools(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 60),
        resource_id=str(src.get("resource_id") or
                        "4b292323-9fcc-41f8-814b-3c7b19cf14b3")),
    "deqar": lambda src, s: discover.discover_deqar(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 60)),
    "ipeds": lambda src, s: discover.discover_ipeds(
        src.get("url", ""), s, int(src.get("per_run", 300)),
        int(src.get("timeout_seconds") or 120)),
    "eter": lambda src, s: discover.discover_eter(
        src.get("url", ""), s, int(src.get("per_run", 100)),
        int(src.get("timeout_seconds") or 180)),
}

# Sources that primarily yield K-12 rows; skipped when k12_enabled is false.
K12_SOURCES = frozenset({"france-annuaire", "osm", "dotgov", "nz-schools"})


def pick_sources(sources: list[dict], k12: bool,
                 forced: str = "") -> list[dict]:
    if forced:
        found = [s for s in sources if s.get("id") == forced]
        if not found:
            raise SystemExit(f"unknown --source {forced!r}")
        return found
    # Hit EVERY enabled source each session, each capped by its `per_run`.
    # Coverage still advances session-to-session via per-adapter cursors
    # (offsets/pages/suffix rotation in state). Deadline guard in run_curate
    # stops early if the session overruns; cursors already persisted per
    # adapter keep the next session consistent.
    return [s for s in sources
            if s.get("enabled") and s.get("id") in ADAPTERS
            and (k12 or s.get("id") not in K12_SOURCES)]


def _call_adapter(sid: str, fn, src: dict, state: dict, mailto: str):
    # Only openalex uses the resolved contact; others take (src, state).
    if sid == "openalex":
        try:
            return fn(src, state, mailto) or []
        except TypeError:  # pragma: no cover — legacy 2-arg mock
            return fn(src, state) or []
    return fn(src, state) or []


def run_curate(*, cfg: dict, src_cfg: dict, state: dict,
               by_domain: dict, buckets: dict, pending: list[dict],
               forced: str = "", deadline: float) -> dict:
    """Mutates state/by_domain/buckets/pending. Returns stats."""
    # Single contact identity: config UA wins, discover/whois follow.
    ua = resolve_user_agent(cfg)
    if ua:
        discover.UA = {"User-Agent": ua}
    try:
        from src import whois_check as _whois

        _whois.UA = {"User-Agent": ua,
                     "Accept": "application/rdap+json, application/json"}
    except Exception:
        pass
    mailto = resolve_mailto(cfg, src_cfg, ua)
    suffix_map = merge_suffix_map(cfg.get("suffix_country", {}))
    blocklist = {str(b).lower().strip(".") for b in cfg.get("blocklist", []) if b}
    k12 = bool(cfg.get("k12_enabled", False))
    max_pending = int(cfg.get("run", {}).get("max_pending", 8000))

    # Purge blocklisted rows first (opt-out honored on next run).
    purged = purge_blocklisted(by_domain, buckets, state, blocklist)
    touched: set[str] = set(purged)

    # Drop service-host endpoints already queued by older runs: they can
    # never become Active (validate forces Inaccessible) and only burn
    # verify budget (0.4s politeness + 10s timeout each).
    before = len(pending)
    pending[:] = [e for e in pending
                  if not is_service_host(str(e.get("domain", "")).lower())]
    skipped_service = before - len(pending)
    if skipped_service:
        log(f"  dropped {skipped_service} queued service-host(s) (never Active)")

    pending_idx = {e["domain"]: i for i, e in enumerate(pending)}
    raw, new, recited, unmapped = 0, 0, 0, 0
    skipped_new_service = 0

    for src in pick_sources(src_cfg.get("sources", []), k12, forced):
        sid = src.get("id", "")
        fn = ADAPTERS.get(sid)
        if not fn:
            log(f"Discover: {sid} has no adapter, skipping")
            continue
        log(f"Discover: {sid} (per_run {src.get('per_run')})…")
        try:
            cands = _call_adapter(sid, fn, src, state, mailto)
        except SystemExit:
            raise
        except Exception as e:  # never fail a run on one source
            log(f"  {sid} error: {type(e).__name__}: {e}, skipping")
            continue
        log(f"  -> {len(cands)} raw candidates")
        raw += len(cands)
        for c in cands:
            d = normalize_domain(c.get("url", ""))
            if not d or d in blocklist:
                continue
            if is_service_host(d):
                skipped_new_service += 1
                continue
            iso = (c.get("iso2") or "").upper()
            if len(iso) != 2 or not iso.isalpha():
                iso = country_from_suffix(d, suffix_map) or "XX"
            if iso == "XX":
                unmapped += 1
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
        if time.time() > deadline:
            log("  deadline reached, stopping discovery")
            break

    return {"raw": raw, "new": new, "recited": recited, "touched": touched,
            "unmapped": unmapped, "skipped_service": skipped_new_service}


def main() -> int:
    ap = argparse.ArgumentParser(description="Discover new school domains (no validation).")
    ap.add_argument("--config", default=str(CLI_ROOT / "config.yaml"))
    ap.add_argument("--sources", default=str(CLI_ROOT / "sources.yaml"))
    ap.add_argument("--source", default="", help="Force one discovery source id")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-network", action="store_true",
                    help="Skip upstream fetches (for tests/offline).")
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
        log("NO-NETWORK: skipping discovery, reporting queue state only")
        log(f"DRY-RUN: raw=0 new_queued=0 recited=0 pending_total={len(pending)}")
        return 0

    # Resolve contact early so even dry-run discovery uses one identity.
    apply_contact(cfg, src_cfg)
    deadline = time.time() + int(run.get("max_seconds", 2700))
    stats = run_curate(cfg=cfg, src_cfg=src_cfg, state=state,
                       by_domain=by_domain, buckets=buckets, pending=pending,
                       forced=args.source, deadline=deadline)

    if args.dry_run:
        log(f"DRY-RUN: raw={stats['raw']} new_queued={stats['new']} "
            f"recited={stats['recited']} unmapped={stats.get('unmapped', 0)} "
            f"skipped_service={stats.get('skipped_service', 0)}")
        return 0
    state["last_curate"] = {
        "at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "raw": stats["raw"], "new": stats["new"],
        "recited": stats["recited"],
        "unmapped": stats.get("unmapped", 0),
        "skipped_service": stats.get("skipped_service", 0),
    }
    save_runtime(countries_dir=paths["countries_dir"], buckets=buckets,
                 touched=stats["touched"], index_path=paths["index_path"],
                 pending_path=paths["pending_path"], pending=pending,
                 state_path=paths["state_path"], state=state,
                 archive_after=int(run.get("archive_after_failures", 6)))
    if stats.get("unmapped", 0):
        log(f"NOTE: {stats['unmapped']} candidates fell back to XX "
            f"(no source ISO + no suffix match) — see XX.csv for review")
    log(f"Done. raw={stats['raw']} new_queued={stats['new']} "
        f"recited={stats['recited']} pending_total={len(pending)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
