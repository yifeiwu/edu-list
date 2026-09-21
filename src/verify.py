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
    deadline_for,
    init_runtime,
    log,
    resolve_user_agent,
    save_runtime,
)
from src.exa_check import (  # noqa: E402
    EXA_CACHE_TTL_DAYS,
    cached_discover,
    cached_verify,
    cached_verify_self,
    exa_config_from_cfg,
    is_dissimilar_redirect,
)
from src.geo import merge_suffix_map  # noqa: E402
from src.store import purge_blocklisted, today_iso  # noqa: E402
from src.util import (  # noqa: E402
    classify_type, country_from_suffix, is_service_host, union_sources,
)
from src.validate import validate_site  # noqa: E402
from src.whois_check import years_registered as _domain_age  # noqa: E402


def _redirect_from_source(source: str) -> str | None:
    """Immediate predecessor from a `redirect:<old>` provenance chain."""
    for chunk in reversed((source or "").split(";")):
        c = chunk.strip()
        if c.lower().startswith("redirect:"):
            cand = c.split(":", 1)[1].strip().lower().strip(".")
            if cand:
                return cand
    return None


def check(domain: str, name: str, iso: str, multisrc: bool, vcfg: dict,
          redirect_from: str | None = None,
          exa_verify_fn=None, exa_fallback_fn=None) -> tuple[str, dict]:
    res = validate_site(f"https://{domain}", domain, iso,
                        vcfg["timeout"], vcfg["ua"], vcfg["max_bytes"],
                        multisource=multisrc, politeness=vcfg["polite"],
                        active_threshold=vcfg["threshold"],
                        retries=vcfg.get("retries", 1),
                        retry_backoff=vcfg.get("backoff", 1.0),
                        school_name=name or "",
                        redirect_from=redirect_from,
                        exa_verify_fn=exa_verify_fn,
                        exa_fallback_fn=exa_fallback_fn)
    # Non-2xx is Inaccessible — except an Exa fallback rescue, where Exa
    # independently indexes the same domain as the institution (bot-block /
    # WAF false-positive). Moved pointers are never Active (chased instead).
    if res.get("moved_to"):
        return "Inaccessible", res
    exa = res.get("exa")
    if (res["status"] == "Active" and isinstance(exa, dict)
            and exa.get("verified") is True
            and "+exa-" in str(res.get("reason", ""))):
        return "Active", res
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
    exa_cache = state.setdefault("exa_cache", {})
    exa_cfg = exa_config_from_cfg(cfg)
    exa_calls = 0
    validated = added = reverified = 0
    suffix_map = merge_suffix_map(cfg.get("suffix_country", {}))

    def _exa_hook(source: str, target: str, school_name: str = "",
                  country_iso: str = "") -> dict | None:
        """Budget-capped, cached Exa second-opinion for dissimilar moves.

        Returns None when Exa is disabled/unconfigured, the hop is
        same-site, the verdict is cached, or the per-run budget is spent —
        so Exa can never block or crash verification. Cache hits never
        consume budget; only actual API attempts count.
        """
        nonlocal exa_calls
        try:
            if not exa_cfg.get("enabled"):
                return None
            if not exa_cfg.get("api_key"):
                return None
            if not is_dissimilar_redirect(source or "", target or ""):
                return None
        except Exception:
            return None
        key = (target or "").lower().strip(".").removeprefix("www.")
        try:
            import datetime as _dt
            raw = exa_cache.get(key)
            if isinstance(raw, dict) and "verified" in raw:
                ts = str(raw.get("ts", "") or "")
                try:
                    day = _dt.date.fromisoformat(ts[:10])
                    if (_dt.date.today() - day).days < EXA_CACHE_TTL_DAYS:
                        return raw
                except ValueError:
                    pass
        except Exception:
            pass
        try:
            budget = int(exa_cfg.get("max_calls_per_run", 20))
        except Exception:
            budget = 20
        if exa_calls >= budget:
            return None
        exa_calls += 1
        try:
            return cached_verify(source, target, school_name, country_iso,
                                 cache=exa_cache,
                                 api_key=exa_cfg.get("api_key") or "",
                                 timeout=int(exa_cfg.get("timeout", 15)),
                                 num_results=int(exa_cfg.get("num_results", 5)),
                                 search_type=str(exa_cfg.get("search_type",
                                                             "fast")))
        except Exception:
            return None

    def _exa_fallback_hook(domain: str, school_name: str = "",
                           country_iso: str = "") -> dict | None:
        """Budget-capped Exa fallback: rescue bot-blocks, update domain.

        Returns ``{verified, reason, evidence, candidate?}`` or None (no
        opinion / disabled / budget spent). Each API-backed step consumes
        one unit of ``exa_calls`` (self-verify, then discovery only if the
        same domain wasn't rescued and budget remains); cache hits are
        free. Never raises.
        """
        nonlocal exa_calls
        try:
            if not exa_cfg.get("enabled"):
                return None
            if not exa_cfg.get("rescue_enabled", True):
                return None
            if not exa_cfg.get("api_key"):
                return None
            if not (domain or "").strip():
                return None
        except Exception:
            return None
        try:
            budget = int(exa_cfg.get("max_calls_per_run", 20))
        except Exception:
            budget = 20
        api_key = str(exa_cfg.get("api_key") or "")
        timeout = int(exa_cfg.get("timeout", 15))
        num_results = int(exa_cfg.get("num_results", 5))
        search_type = str(exa_cfg.get("search_type", "fast"))
        # Step 1: self-verify the same domain.
        if exa_calls >= budget:
            return None
        exa_calls += 1
        try:
            self_v = cached_verify_self(domain, school_name, country_iso,
                                        cache=exa_cache, api_key=api_key,
                                        timeout=timeout,
                                        num_results=num_results,
                                        search_type=search_type)
        except Exception:
            return None
        if isinstance(self_v, dict) and self_v.get("verified") is True:
            return {"verified": True, "reason": self_v.get("reason", ""),
                    "evidence": list(self_v.get("evidence", []) or []),
                    "candidate": None}
        # Step 2: discover a replacement domain (only when same-domain
        # wasn't rescued and budget remains).
        if exa_calls >= budget:
            if isinstance(self_v, dict):
                return {"verified": self_v.get("verified"),
                        "reason": self_v.get("reason", ""),
                        "evidence": list(self_v.get("evidence", []) or []),
                        "candidate": None}
            return None
        exa_calls += 1
        try:
            disc = cached_discover(school_name, country_iso, domain,
                                   cache=exa_cache, api_key=api_key,
                                   timeout=timeout, num_results=num_results,
                                   search_type=search_type)
        except Exception:
            disc = None
        if isinstance(disc, dict) and disc.get("domain"):
            cand = disc.get("domain")
            try:
                dissimilar = is_dissimilar_redirect(domain or "", cand or "")
            except Exception:
                dissimilar = (str(cand or "").lower()
                              != (domain or "").lower())
            if dissimilar and disc.get("verified") is True:
                return {"verified": None,
                        "reason": disc.get("reason", ""),
                        "evidence": list(disc.get("evidence", []) or []),
                        "candidate": cand}
        if isinstance(self_v, dict):
            return {"verified": self_v.get("verified"),
                    "reason": self_v.get("reason", ""),
                    "evidence": list(self_v.get("evidence", []) or []),
                    "candidate": None}
        return None

    def _age(domain: str) -> str:
        try:
            years = _domain_age(domain, timeout=8, cache=age_cache)
        except Exception:
            years = None
        return "" if years is None else str(years)

    def _row_extra(res: dict, domain: str) -> dict:
        """New CSV columns from a validation result (stored as text).

        Mirrors `store.FIELDS` tail: confidence, reason, final_domain,
        language. Missing keys (e.g. Exa-rescue paths without local HTML)
        fall back to "" (language) or the checked domain (final_domain).
        """
        return {
            "confidence": str(res.get("confidence", "")),
            "reason": str(res.get("reason", "")),
            "final_domain": str(res.get("final_domain", "") or domain),
            "language": str(res.get("language", "")),
        }

    def _record_new(domain, name, iso, type_hint, source):
        """Validate + write a row for a not-yet-known domain."""
        nonlocal validated, added
        multisrc = ";" in (source or "")
        redirect_from = _redirect_from_source(source or "")
        status, res = check(domain, name, iso, multisrc, vcfg,
                            redirect_from=redirect_from,
                            exa_verify_fn=_exa_hook,
                            exa_fallback_fn=_exa_fallback_hook)
        age = _age(domain)
        row = {"school_name": name or domain, "web_domain": domain,
               "type": classify_type(name or "", domain, type_hint or ""),
               "last_visited": today_iso(), "status": status,
               "sources": source,
               "years_registered": age,
               **_row_extra(res, domain)}
        buckets.setdefault(iso, []).append(row)
        by_domain[domain] = (iso, row)
        touched.add(iso)
        failures[domain] = {"confidence": res.get("confidence", 0),
                            "reason": res.get("reason", ""),
                            "code": res.get("code", 0)}
        if res.get("exa") is not None:
            failures[domain]["exa"] = res.get("exa")
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
        # Preserve the Exa-annotated reason when present (e.g.
        # `moved-to:royalholloway.ac.uk+exa-verified`); else the plain pointer.
        reason = str(res.get("reason", "") or "")
        if not reason.startswith("moved-"):
            reason = f"moved-to:{target}"
        row.update(_row_extra(res, d))
        row["reason"] = reason  # pointer reason, not the raw fetch reason
        failures[d] = {"confidence": res.get("confidence", 0),
                       "reason": reason,
                       "code": res.get("code", 0)}
        if res.get("exa") is not None:
            failures[d]["exa"] = res.get("exa")
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
            redirect_from = _redirect_from_source(row.get("sources", ""))
            status, res = check(d, row["school_name"], iso, multisrc, vcfg,
                                redirect_from=redirect_from,
                                exa_verify_fn=_exa_hook,
                                exa_fallback_fn=_exa_fallback_hook)
            mv = res.get("moved_to")
            if mv and mv != d:
                _mark_moved(d, row, mv, res, prev_fc)
            else:
                row["last_visited"] = today_iso()
                row["status"] = status
                row.update(_row_extra(res, d))
                if not row.get("years_registered"):
                    row["years_registered"] = _age(d)
                failures[d] = {"confidence": res.get("confidence", 0),
                               "reason": res.get("reason", ""),
                               "code": res.get("code", 0)}
                if res.get("exa") is not None:
                    failures[d]["exa"] = res.get("exa")
                failcounts[d] = 0 if status == "Active" else prev_fc + 1
                moved_map.pop(d, None)
                touched.add(iso)
            validated += 1
            reverified += 1

    return {"validated": validated, "added_active": added,
            "reverified": reverified, "touched": touched,
            "pending_left": len(pending), "exa_calls": exa_calls}


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

    cfg, _, paths, state, by_domain, buckets, pending = init_runtime(
        Path(args.config))
    if not args.dry_run and not args.no_network:
        assert_configured_contact(cfg)
    run = cfg.get("run", {})
    countries_dir = paths["countries_dir"]
    index_path = paths["index_path"]
    state_path = paths["state_path"]
    pending_path = paths["pending_path"]

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
    deadline = deadline_for(cfg)
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
