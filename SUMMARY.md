# Edu-Domains — Run Summary

_Generated 2026-09-15 01:26 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **947** across **63** countries
- Active: **616** (65%) · Inaccessible: **331** (35%)
- Pending queue: **474** unvalidated candidates
- Known registration age: **527** domains (median 23 yrs)

## Last runs

- Verify (2026-09-14 23:26 UTC): validated 121, +71 Active, re-verified 15, pending left 355
- Curate (2026-09-15 01:26 UTC): 161 raw candidates, 119 queued, 15 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 334 | 258 | 76 |
| AU | 99 | 71 | 28 |
| FR | 89 | 58 | 31 |
| XX | 72 | 36 | 36 |
| AM | 36 | 21 | 15 |
| AL | 27 | 15 | 12 |
| NG | 27 | 19 | 8 |
| AT | 25 | 21 | 4 |
| GB | 22 | 12 | 10 |
| IN | 17 | 11 | 6 |
| CN | 16 | 7 | 9 |
| IR | 15 | 0 | 15 |
| BR | 13 | 7 | 6 |
| CZ | 13 | 2 | 11 |
| RU | 13 | 7 | 6 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 581 |
| `fetch-error:ConnectionError` | 87 |
| `http-403` | 68 |
| `low-confidence:http-2xx-html` | 39 |
| `fetch-error:ConnectTimeout` | 33 |
| `fetch-error:SSLError` | 25 |
| `empty-body` | 9 |
| `http-503` | 3 |
| `fetch-error:ReadTimeout` | 2 |
| `http-500` | 2 |
| `soft-404/block-page` | 2 |
| `social-only/placeholder` | 1 |

## Freshness

- Verified in last 30 days: **947** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **36**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/15 (0%) — check for blocks/stale sources
- ⚠ `XX`: 72 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
