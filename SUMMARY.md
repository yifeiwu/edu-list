# Edu-Domains — Run Summary

_Generated 2026-09-16 11:05 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1672** across **82** countries
- Active: **1115** (67%) · Inaccessible: **557** (33%)
- Pending queue: **586** unvalidated candidates
- Known registration age: **895** domains (median 24 yrs)

## Last runs

- Verify (2026-09-16 06:39 UTC): validated 122, +78 Active, re-verified 15, pending left 467
- Curate (2026-09-16 11:05 UTC): 177 raw candidates, 119 queued, 5 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 576 | 449 | 127 |
| AU | 195 | 139 | 56 |
| FR | 180 | 110 | 70 |
| XX | 92 | 41 | 51 |
| BE | 42 | 33 | 9 |
| AT | 41 | 35 | 6 |
| GB | 37 | 25 | 12 |
| AM | 36 | 21 | 15 |
| BR | 33 | 20 | 13 |
| CN | 31 | 12 | 19 |
| AL | 28 | 15 | 13 |
| IN | 28 | 19 | 9 |
| NG | 27 | 19 | 8 |
| BY | 23 | 12 | 11 |
| CH | 21 | 15 | 6 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1080 |
| `fetch-error:ConnectionError` | 148 |
| `http-403` | 109 |
| `low-confidence:http-2xx-html` | 81 |
| `fetch-error:ConnectTimeout` | 53 |
| `fetch-error:SSLError` | 40 |
| `empty-body` | 16 |
| `http-500` | 5 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 4 |
| `social-only/placeholder` | 3 |
| `http-404` | 3 |

## Freshness

- Verified in last 30 days: **1672** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **63**

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
