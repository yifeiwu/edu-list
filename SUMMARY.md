# Edu-Domains — Run Summary

_Generated 2026-09-15 01:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1050** across **67** countries
- Active: **690** (66%) · Inaccessible: **360** (34%)
- Pending queue: **374** unvalidated candidates
- Known registration age: **573** domains (median 23 yrs)

## Last runs

- Verify (2026-09-15 01:55 UTC): validated 118, +74 Active, re-verified 15, pending left 374
- Curate (2026-09-15 01:26 UTC): 161 raw candidates, 119 queued, 15 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 354 | 276 | 78 |
| AU | 114 | 82 | 32 |
| FR | 104 | 67 | 37 |
| XX | 78 | 38 | 40 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| AL | 28 | 15 | 13 |
| NG | 27 | 19 | 8 |
| GB | 22 | 12 | 10 |
| IN | 19 | 13 | 6 |
| CN | 17 | 8 | 9 |
| IR | 15 | 0 | 15 |
| DE | 14 | 7 | 7 |
| JP | 14 | 5 | 9 |
| RU | 14 | 8 | 6 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 655 |
| `fetch-error:ConnectionError` | 97 |
| `http-403` | 72 |
| `low-confidence:http-2xx-html` | 42 |
| `fetch-error:ConnectTimeout` | 38 |
| `fetch-error:SSLError` | 25 |
| `empty-body` | 10 |
| `fetch-error:ReadTimeout` | 3 |
| `http-503` | 3 |
| `social-only/placeholder` | 2 |
| `http-500` | 2 |
| `soft-404/block-page` | 2 |

## Freshness

- Verified in last 30 days: **1050** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **39**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/15 (0%) — check for blocks/stale sources
- ⚠ `XX`: 78 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
