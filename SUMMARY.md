# Edu-Domains — Run Summary

_Generated 2026-09-14 19:06 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **738** across **60** countries
- Active: **483** (65%) · Inaccessible: **255** (35%)
- Pending queue: **425** unvalidated candidates
- Known registration age: **403** domains (median 21 yrs)

## Last runs

- Verify (2026-09-14 14:29 UTC): validated 118, +66 Active, re-verified 15, pending left 295
- Curate (2026-09-14 19:06 UTC): 177 raw candidates, 130 queued, 9 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 235 | 188 | 47 |
| AU | 81 | 58 | 23 |
| FR | 74 | 49 | 25 |
| XX | 57 | 30 | 27 |
| AM | 36 | 21 | 15 |
| AL | 27 | 16 | 11 |
| NG | 27 | 19 | 8 |
| GB | 21 | 11 | 10 |
| IN | 14 | 10 | 4 |
| RU | 13 | 7 | 6 |
| CN | 12 | 5 | 7 |
| CZ | 12 | 2 | 10 |
| AT | 9 | 6 | 3 |
| IR | 9 | 0 | 9 |
| DE | 8 | 3 | 5 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 448 |
| `fetch-error:ConnectionError` | 61 |
| `http-403` | 56 |
| `low-confidence:http-2xx-html` | 33 |
| `fetch-error:ConnectTimeout` | 24 |
| `fetch-error:SSLError` | 17 |
| `empty-body` | 8 |
| `http-503` | 2 |
| `soft-404/block-page` | 2 |
| `social-only/placeholder` | 1 |
| `moved-to:azcu.edu` | 1 |
| `moved-to:brooklynadultlearning.center` | 1 |

## Freshness

- Verified in last 30 days: **738** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **27**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/12 (17%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/9 (0%) — check for blocks/stale sources
- ⚠ `XX`: 57 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
