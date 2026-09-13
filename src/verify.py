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
import collections
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
    resolve_user_agent,
    save_runtime,
)
from src.geo import merge_suffix_map  # noqa: E402
from src.store import purge_blocklisted, today_iso  # noqa: E402
from src.util import (  # noqa: E402
    classify_type, country_from_suffix, is_service_host, union_sources,
)
from src.validate import validate_site  # noqa: E402
from src.whois_check import years_registered as _domain_age  # noqa: E402


def check(domain: str, name: str, iso: str, multisrc: bool, vcfg: dict) -> tuple[str, dict]:
    res = validate_site(f"https://{domain}", domain, iso,
                        vcfg["timeout"], vcfg["ua"], vcfg["max_bytes"],
                        multisource=multisrc, politeness=vcfg["polite"],
                        active_threshold=vcfg["threshold"],
                        retries=vcfg.get("retries", 1),
                        retry_backoff=vcfg.get("backoff", 1.0))
    # Locked rule: non-2xx is ALWAYS Inaccessible regardless of score.
    # validate_site already enforces threshold, but re-check here so a
    # config change takes effect even if the scorer defaults drift.
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
        "ua": resolve_user_agent(cfg),
        "threshold": int(cfg.get("validation", {}).get("active_threshold", 50)),
        "polite": float(cfg.get("validation", {}).get("politeness_delay_seconds", 0.4)),
        "retries": int(cfg.get("validation", {}).get("retries", 1)),
        "backoff": float(cfg.get("validation", {}).get("retry_backoff_seconds", 1.0)),
    }
    max_val = limit or int(v.get("max_validations", run.get("max_validations", 600)))
    max_new = int(v.get("max_new_per_run", run.get("max_new_per_run", 500)))
    batch_no_new = int(v.get("verify_batch_no_new", run.get("verify_batch_no_new", 500)))
    batch_with_new = int(v.get("verify_batch_with_new",
                               run.get("verify_batch_with_new", 100)))
    archive_after = int(run.get("archive_after_failures", 6))
    archive_skip = int(run.get("archive_skip_days", 90))

    blocklist = {str(b).lower().strip(".") for b in cfg.get("blocklist", []) if b}
    # Honor opt-outs before any network work.
    purged = purge_blocklisted(by_domain, buckets, state, blocklist)
    touched: set[str] = set(purged)
    # Drop blocklisted candidates from the queue without validating them.
    if blocklist:
        pending[:] = [c for c in pending
                      if str(c.get("domain", "")).lower() not in blocklist]

    failures = state.setdefault("detail", {})
    failcounts = state.setdefault("failures", {})
    moved_map = state.setdefault("moved", {})
    age_cache = state.setdefault("domain_age", {})
    validated = added = reverified = 0
    suffix_map = merge_suffix_map(cfg.get("suffix_country", {}))

    def _age(domain: str) -> str:
        try:
            years = _domain_age(domain, timeout=8, cache=age_cache)
        except Exception:
            years = None
        return "" if years is None else str(years)

    def _record_new(domain, name, iso, type_hint, source):
        """Validate + write a row for a not-yet-known domain."""
        nonlocal validated, added
        multisrc = ";" in (source or "")
        status, res = check(domain, name, iso, multisrc, vcfg)
        age = _age(domain)
        row = {"school_name": name or domain, "web_domain": domain,
               "type": classify_type(name or "", domain, type_hint or ""),
               "last_visited": today_iso(), "status": status,
               "sources": source,
               "years_registered": age}
        buckets.setdefault(iso, []).append(row)
        by_domain[domain] = (iso, row)
        touched.add(iso)
        failures[domain] = {"confidence": res.get("confidence", 0),
                            "reason": res.get("reason", ""),
                            "code": res.get("code", 0)}
        failcounts[domain] = 0 if status == "Active" \
            else int(failcounts.get(domain, 0)) + 1
        if res.get("moved_to"):
            moved_map[domain] = res["moved_to"]
        else:
            moved_map.pop(domain, None)
        validated += 1
        if status == "Active":
            added += 1
        return status, res

    def _handle_move(old, target, name, iso, type_hint, max_hops: int = 5):
        """Old domain now lives at `target`: cite/queue it, and validate
        the full redirect chain immediately within budget (up to max_hops,
        loop-safe — chains longer than that re-queue for the next run).
        Service-host targets (webmail/LMS) are never given their own row:
        the old row's moved-to pointer is record enough."""
        visited = {old}
        cur_old, cur_target = old, target
        cur_name, cur_iso, cur_hint = name, iso, type_hint
        for _ in range(max_hops):
            if cur_target in by_domain:
                _, trow = by_domain[cur_target]
                merged = union_sources(trow.get("sources", ""), f"redirect:{cur_old}")
                if merged != trow.get("sources", ""):
                    trow["sources"] = merged
                    touched.add(by_domain[cur_target][0])
                visited.add(cur_target)
                # Follow through known pointers: A->B->C where B already
                # validated as moved-to:C should resolve C in the same run.
                nxt = moved_map.get(cur_target)
                if nxt and nxt not in visited and nxt not in by_domain \
                        and not any(e["domain"] == nxt for e in pending):
                    visited.add(cur_target)
                    cur_old, cur_target = cur_target, nxt
                    cur_iso = country_from_suffix(nxt, suffix_map) or cur_iso
                    continue
                break
            found_pending = False
            for e in pending:
                if e["domain"] == cur_target:
                    e["source"] = union_sources(e.get("source", ""),
                                                f"redirect:{cur_old}")
                    found_pending = True
                    break
            if found_pending:
                visited.add(cur_target)
                break
            if is_service_host(cur_target):
                return
            if cur_target in visited:
                # Self-loop guard (should not happen; _moved_to filters
                # same-site, but be safe).
                break
            visited.add(cur_target)
            tiso = country_from_suffix(cur_target, suffix_map) or cur_iso
            if validated < max_val and time.time() < deadline:
                st, rs = _record_new(cur_target, cur_name or cur_target, tiso,
                                     cur_hint or "", f"redirect:{cur_old}")
                log(f"  follow move {cur_old} -> {cur_target} => {st} ({rs.get('reason')})")
                t2 = rs.get("moved_to")
                if t2 and t2 not in visited and t2 != cur_target \
                        and t2 not in by_domain \
                        and not any(e["domain"] == t2 for e in pending):
                    cur_old, cur_target = cur_target, t2
                    cur_iso = country_from_suffix(t2, suffix_map) or tiso
                    continue
                if t2 and t2 not in visited and (
                        t2 in by_domain or any(e["domain"] == t2 for e in pending)):
                    # One more loop iteration to merge the citation.
                    cur_old, cur_target = cur_target, t2
                    continue
                break
            else:
                pending.append({"name": cur_name or cur_target,
                                "url": f"https://{cur_target}",
                                "domain": cur_target, "iso2": tiso,
                                "type_hint": cur_hint or "",
                                "source": f"redirect:{cur_old}"})
                break

    def _mark_moved(d, row, target, res, prev_fc):
        """The fetched content belonged to another host: this row is a
        pointer, never the site — force Inaccessible + chase the target."""
        row["last_visited"] = today_iso()
        row["status"] = "Inaccessible"
        failures[d] = {"confidence": res.get("confidence", 0),
                       "reason": f"moved-to:{target}",
                       "code": res.get("code", 0)}
        # Moved pointers use the same archive pacing as failures (they never
        # become Active) but are tracked separately for visibility.
        failcounts[d] = prev_fc + 1
        moved_map[d] = target
        touched.add(by_domain[d][0])
        _handle_move(d, target, row.get("school_name", d),
                     by_domain[d][0], row.get("type", ""))

    # 1) Drain pending queue (FIFO, O(1) via deque).
    if not reverify_only:
        queue: collections.deque = collections.deque(pending)
        pending.clear()
        n = 0
        skipped_dupes = 0
        while queue and n < max_new and validated < max_val \
                and time.time() < deadline:
            c = queue.popleft()
            d = c.get("domain", "")
            if not d or d in by_domain:
                skipped_dupes += 1
                continue  # validated by an overlapping run; drop duplicate
            iso = c.get("iso2", "XX") or "XX"
            prev_fc = int(failcounts.get(d, 0))
            status, res = _record_new(d, c.get("name", d), iso,
                                      c.get("type_hint", ""),
                                      c.get("source", ""))
            n += 1
            mv = res.get("moved_to")
            if mv and mv != d:
                _mark_moved(d, by_domain[d][1], mv, res, prev_fc)
            if validated % 50 == 0:
                log(f"  validated {validated}: {d} -> {status} ({res.get('reason')})")
        # Unprocessed tail goes back, preserving FIFO order.
        pending.extend(queue)

    # 2) Re-verify existing rows.
    new_found = validated > 0
    if not new_only and validated < max_val and time.time() < deadline:
        batch = batch_with_new if new_found else batch_no_new
        log(f"{'New validated — piggyback' if new_found else 'Queue empty — full'} "
            f"re-verify of oldest {batch}")
        today = dt.datetime.now(dt.timezone.utc).date()
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
            prev_fc = int(failcounts.get(d, 0))
            status, res = check(d, row["school_name"], iso, multisrc, vcfg)
            mv = res.get("moved_to")
            if mv and mv != d:
                _mark_moved(d, row, mv, res, prev_fc)
            else:
                row["last_visited"] = today_iso()
                row["status"] = status
                if not row.get("years_registered"):
                    row["years_registered"] = _age(d)
                failures[d] = {"confidence": res.get("confidence", 0),
                               "reason": res.get("reason", ""),
                               "code": res.get("code", 0)}
                failcounts[d] = 0 if status == "Active" else prev_fc + 1
                moved_map.pop(d, None)
                touched.add(iso)
            validated += 1
            reverified += 1

    return {"validated": validated, "added_active": added,
            "reverified": reverified, "touched": touched,
            "pending_left": len(pending)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate queued + existing school websites.")
    ap.add_argument("--config", default=str(CLI_ROOT / "config.yaml"))
    ap.add_argument("--limit", type=int, default=0,
                    help="Max validations (0 = use config).")
    ap.add_argument("--new-only", action="store_true",
                    help="Only drain pending queue, skip re-verification.")
    ap.add_argument("--reverify-only", action="store_true",
                    help="Skip pending queue, only re-verify existing rows.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-network", action="store_true",
                    help="Skip website fetches (for tests/offline).")
    args = ap.parse_args()

    cfg = load_cfg(Path(args.config))
    if not args.dry_run and not args.no_network:
        assert_configured_contact(cfg)
    run = cfg.get("run", {})
    paths = resolve_paths(cfg)
    countries_dir = paths["countries_dir"]
    index_path = paths["index_path"]
    state_path = paths["state_path"]
    pending_path = paths["pending_path"]

    state, by_domain, buckets, pending = load_runtime(
        state_path, countries_dir, pending_path)
    log(f"Loaded {len(by_domain)} domains, {len(pending)} pending")

    if args.no_network:
        log("NO-NETWORK: skipping validation, reporting state only")
        log(f"DRY-RUN: validated=0 added_active=0 "
            f"reverified=0 pending_left={len(pending)}")
        return 0

    limit = args.limit
    if args.dry_run and not limit:
        limit = 5
        log("DRY-RUN: capping validations at 5 (pass --limit to override)")

    apply_contact(cfg)
    deadline = time.time() + int(run.get("max_seconds", 2700))
    stats = run_verify(cfg=cfg, state=state, by_domain=by_domain,
                       buckets=buckets, pending=pending, limit=limit,
                       new_only=args.new_only, reverify_only=args.reverify_only,
                       deadline=deadline)

    if args.dry_run:
        log(f"DRY-RUN: validated={stats['validated']} "
            f"added_active={stats['added_active']} "
            f"reverified={stats['reverified']} "
            f"pending_left={stats['pending_left']}")
        return 0
    state["last_verify"] = {
        "at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "validated": stats["validated"],
        "added_active": stats["added_active"],
        "reverified": stats["reverified"],
        "pending_left": stats["pending_left"],
    }
    save_runtime(countries_dir=countries_dir, buckets=buckets,
                 touched=stats["touched"], index_path=index_path,
                 pending_path=pending_path, pending=pending,
                 state_path=state_path, state=state,
                 archive_after=int(run.get("archive_after_failures", 6)))
    log(f"Done. validated={stats['validated']} "
        f"added_active={stats['added_active']} "
        f"reverified={stats['reverified']} touched={sorted(stats['touched'])} "
        f"pending_left={stats['pending_left']} total={len(by_domain)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
