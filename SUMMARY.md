# Edu-Domains — Run Summary

_Generated 2026-09-13 02:18 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **8** across **6** countries
- Active: **4** (50%) · Inaccessible: **4** (50%)
- Pending queue: **1692** unvalidated candidates
- Known registration age: **4** domains (median 17.5 yrs)

## Last runs

- Verify (2026-09-12 00:47 UTC): validated 8, +4 Active, re-verified 0, pending left 1551

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| BR | 2 | 1 | 1 |
| UA | 2 | 1 | 1 |
| AE | 1 | 0 | 1 |
| FR | 1 | 1 | 0 |
| IN | 1 | 0 | 1 |
| UG | 1 | 1 | 0 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4 |
| `fetch-error:ConnectionError` | 3 |
| `http-403` | 1 |

## Freshness

- Verified in last 30 days: **8** (100%)
- Older than 90 days: **0** (oldest check 2026-09-12)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **0**

## Alerts

- No alerts.

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
