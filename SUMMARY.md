# Edu-Domains — Run Summary

_Generated 2026-09-14 13:45 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **635** across **55** countries
- Active: **417** (66%) · Inaccessible: **218** (34%)
- Pending queue: **395** unvalidated candidates
- Known registration age: **366** domains (median 22 yrs)

## Last runs

- Verify (2026-09-14 07:01 UTC): validated 118, +73 Active, re-verified 15, pending left 254
- Curate (2026-09-14 13:45 UTC): 177 raw candidates, 141 queued, 4 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 217 | 172 | 45 |
| AU | 64 | 44 | 20 |
| FR | 59 | 39 | 20 |
| XX | 48 | 26 | 22 |
| AM | 30 | 18 | 12 |
| AL | 27 | 16 | 11 |
| NG | 22 | 15 | 7 |
| GB | 20 | 11 | 9 |
| IN | 14 | 10 | 4 |
| RU | 13 | 7 | 6 |
| CZ | 12 | 2 | 10 |
| CN | 10 | 3 | 7 |
| DE | 8 | 3 | 5 |
| GH | 8 | 6 | 2 |
| BR | 6 | 3 | 3 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 382 |
| `http-403` | 50 |
| `fetch-error:ConnectionError` | 49 |
| `low-confidence:http-2xx-html` | 29 |
| `fetch-error:ConnectTimeout` | 21 |
| `fetch-error:SSLError` | 11 |
| `empty-body` | 7 |
| `http-503` | 2 |
| `soft-404/block-page` | 2 |
| `moved-to:azcu.edu` | 1 |
| `moved-to:brooklynadultlearning.center` | 1 |
| `parking-linkfarm` | 1 |

## Freshness

- Verified in last 30 days: **635** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **24**

## Alerts

- ⚠ `CZ`: low Active rate 2/12 (17%) — check for blocks/stale sources
- ⚠ `XX`: 48 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
