# Edu-Domains — Run Summary

_Generated 2026-09-16 12:52 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1776** across **83** countries
- Active: **1183** (67%) · Inaccessible: **593** (33%)
- Pending queue: **486** unvalidated candidates
- Known registration age: **953** domains (median 24 yrs)

## Last runs

- Verify (2026-09-16 12:52 UTC): validated 119, +69 Active, re-verified 15, pending left 486
- Curate (2026-09-16 11:05 UTC): 177 raw candidates, 119 queued, 5 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 614 | 474 | 140 |
| AU | 210 | 152 | 58 |
| FR | 196 | 120 | 76 |
| XX | 92 | 41 | 51 |
| BR | 43 | 25 | 18 |
| BE | 42 | 33 | 9 |
| AT | 41 | 35 | 6 |
| GB | 37 | 25 | 12 |
| AM | 36 | 21 | 15 |
| CH | 32 | 22 | 10 |
| CN | 32 | 12 | 20 |
| AL | 28 | 15 | 13 |
| IN | 28 | 19 | 9 |
| NG | 27 | 19 | 8 |
| DE | 24 | 16 | 8 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1148 |
| `fetch-error:ConnectionError` | 156 |
| `http-403` | 119 |
| `low-confidence:http-2xx-html` | 87 |
| `fetch-error:ConnectTimeout` | 57 |
| `fetch-error:SSLError` | 41 |
| `empty-body` | 16 |
| `http-500` | 6 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 4 |
| `http-404` | 4 |
| `social-only/placeholder` | 3 |

## Freshness

- Verified in last 30 days: **1776** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **68**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `PH`: 4/13 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `XX`: 92 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
