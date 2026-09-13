"""Run summary: SUMMARY.md for humans (linked from README).

Regenerated at the end of every curate/verify run from live state —
never hand-edited. Shows totals, last-run stats, top countries (full
table lives in data/countries/INDEX.md), signal breakdown and freshness.
"""
from __future__ import annotations

import datetime as dt
import statistics
from collections import Counter
from pathlib import Path


def _pct(a: int, b: int) -> str:
    return f"{100 * a / b:.0f}%" if b else "—"


def compute_alerts(buckets: dict[str, list[dict]], state: dict,
                   min_country_n: int = 5, low_active: float = 0.30,
                   blocked_ratio: float = 0.30) -> list[str]:
    """Per-country data-quality alerts: low Active rate, suspected bot-blocks,
    unmapped XX bucket. A sudden 403 spike otherwise looks like normal data."""
    alerts: list[str] = []
    detail = state.get("detail", {}) or {}
    # Domain -> country for reason attribution.
    dom_iso: dict[str, str] = {}
    for iso, rows in buckets.items():
        for r in rows:
            d = r.get("web_domain", "")
            if d:
                dom_iso[d] = iso
    blocked_by_iso: dict[str, int] = {}
    for d, info in detail.items():
        if d not in dom_iso:
            continue
        reason = str((info or {}).get("reason", ""))
        if reason.startswith("http-403") or reason.startswith("http-429") \
                or "block-page" in reason:
            blocked_by_iso[dom_iso[d]] = blocked_by_iso.get(dom_iso[d], 0) + 1
    for iso in sorted(buckets):
        rows = buckets[iso]
        total = len(rows)
        if not total:
            continue
        active = sum(1 for r in rows if r.get("status") == "Active")
        if iso == "XX" and total > 0:
            alerts.append(
                f"`XX`: {total} unmapped countr{'y' if total == 1 else 'ies'} — "
                f"expand `suffix_country` or fix source ISO")
            continue
        if total >= min_country_n and (active / total) < low_active:
            alerts.append(
                f"`{iso}`: low Active rate {active}/{total} ({_pct(active, total)}) — "
                f"check for blocks/stale sources")
        blocked = blocked_by_iso.get(iso, 0)
        if total >= min_country_n and (blocked / total) >= blocked_ratio:
            alerts.append(
                f"`{iso}`: {blocked}/{total} blocked (403/429/block-page) — "
                f"suspected bot-block, verify manually")
    return alerts


def write_summary(summary_path: Path, buckets: dict[str, list[dict]],
                  state: dict, pending_total: int,
                  archive_after: int = 6) -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows = [r for v in buckets.values() for r in v]
    total = len(rows)
    active = sum(1 for r in rows if r.get("status") == "Active")
    known_age = [int(r["years_registered"]) for r in rows
                 if str(r.get("years_registered", "")).isdigit()]
    known_age.sort()
    median_age = (statistics.median(known_age) if known_age else None)
    median_str = (f"{median_age:g}" if isinstance(median_age, float)
                  else (str(median_age) if median_age is not None else ""))

    today = dt.datetime.now(dt.timezone.utc).date()

    def _age_days(r):
        try:
            return (today - dt.date.fromisoformat(
                r.get("last_visited", "2000-01-01"))).days
        except ValueError:
            return 9999

    fresh = sum(1 for r in rows if _age_days(r) <= 30)
    stale90 = sum(1 for r in rows if _age_days(r) > 90)
    oldest = min((r.get("last_visited", "?") for r in rows), default="?")
    archived = sum(1 for d in (state.get("failures", {}) or {})
                   if int(state["failures"].get(d, 0) or 0) >= archive_after)
    moved = len(state.get("moved", {}) or {})

    current = {r["web_domain"] for r in rows}
    reasons = Counter(
        (state.get("detail", {}) or {}).get(d, {}).get(
            "reason", "?").split("+")[0]
        for d in state.get("detail", {}) if d in current)

    by_country = sorted(buckets.items(), key=lambda kv: -len(kv[1]))[:15]

    lv = state.get("last_verify") or {}
    lc = state.get("last_curate") or {}

    L = ["# Edu-Domains — Run Summary", "",
         f"_Generated {now}. Full per-country table: "
         f"[data/countries/INDEX.md](data/countries/INDEX.md)._", "",
         "## Totals", "",
         f"- Domains tracked: **{total}** across **{len(buckets)}** countries",
         f"- Active: **{active}** ({_pct(active, total)}) · "
         f"Inaccessible: **{total - active}** ({_pct(total - active, total)})",
         f"- Pending queue: **{pending_total}** unvalidated candidates",
         f"- Known registration age: **{len(known_age)}** domains"
         + (f" (median {median_str} yrs)" if median_age is not None else ""),
         ""]
    if lv or lc:
        L += ["## Last runs", ""]
        if lv:
            L.append(f"- Verify ({lv.get('at', '?')}): validated "
                     f"{lv.get('validated', '?')}, "
                     f"+{lv.get('added_active', '?')} Active, re-verified "
                     f"{lv.get('reverified', '?')}, "
                     f"pending left {lv.get('pending_left', '?')}")
        if lc:
            L.append(f"- Curate ({lc.get('at', '?')}): {lc.get('raw', '?')} "
                     f"raw candidates, {lc.get('new', '?')} queued, "
                     f"{lc.get('recited', '?')} re-cited")
        L.append("")
    L += ["## Countries (top 15 by size)", "",
          "| country | total | Active | Inaccessible |",
          "|---|---|---|---|"]
    L += [f"| {iso} | {len(v)} | {sum(1 for r in v if r.get('status') == 'Active')} "
          f"| {sum(1 for r in v if r.get('status') != 'Active')} |"
          for iso, v in by_country]
    L += ["", "## Validation signals (reasons in state detail)", "",
          "| reason | count |", "|---|---|"]
    L += [f"| `{rsn[:60]}` | {n} |" for rsn, n in reasons.most_common(12)]
    L += ["", "## Freshness", "",
          f"- Verified in last 30 days: **{fresh}** ({_pct(fresh, total)})",
          f"- Older than 90 days: **{stale90}** (oldest check {oldest})",
          f"- Archived chronic failures (re-check paused): **{archived}**",
          f"- Moved pointers (old domain → new): **{moved}**",
          "", "## Alerts", ""]
    alerts = compute_alerts(buckets, state)
    if alerts:
        L += [f"- ⚠ {a}" for a in alerts]
    else:
        L += ["- No alerts."]
    L += ["", "## Pipelines", "",
          "- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → "
          "`state/pending.json`.",
          "- Verify hourly at :30 UTC (`src/verify.py`): homepage "
          "checks + registration age → `data/countries/*.csv`.",
          "- Schema: `school_name,web_domain,type,last_visited,status,sources,"
          "years_registered`.",
          "- `status` is Active only on final HTTP 2xx + HTML + confidence "
          "with valid TLS; any non-2xx or TLS error is Inaccessible. "
          "`years_registered` is informational "
          "and never gates status.", ""]
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text("\n".join(L), encoding="utf-8")
