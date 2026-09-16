# Edu-Domains — Run Summary

_Generated 2026-09-16 00:48 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1565** across **81** countries
- Active: **1037** (66%) · Inaccessible: **528** (34%)
- Pending queue: **452** unvalidated candidates
- Known registration age: **850** domains (median 24 yrs)

## Last runs

- Verify (2026-09-16 00:48 UTC): validated 117, +69 Active, re-verified 15, pending left 452
- Curate (2026-09-16 00:08 UTC): 177 raw candidates, 108 queued, 16 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 555 | 430 | 125 |
| AU | 178 | 125 | 53 |
| FR | 165 | 102 | 63 |
| XX | 92 | 41 | 51 |
| AT | 41 | 35 | 6 |
| GB | 37 | 25 | 12 |
| AM | 36 | 21 | 15 |
| CN | 30 | 11 | 19 |
| AL | 28 | 15 | 13 |
| IN | 27 | 18 | 9 |
| NG | 27 | 19 | 8 |
| BE | 25 | 22 | 3 |
| BR | 25 | 16 | 9 |
| BY | 23 | 12 | 11 |
| DE | 17 | 10 | 7 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1002 |
| `fetch-error:ConnectionError` | 140 |
| `http-403` | 106 |
| `low-confidence:http-2xx-html` | 75 |
| `fetch-error:ConnectTimeout` | 51 |
| `fetch-error:SSLError` | 40 |
| `empty-body` | 15 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 4 |
| `http-500` | 4 |
| `social-only/placeholder` | 3 |
| `http-405` | 2 |

## Freshness

- Verified in last 30 days: **1565** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **56**

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
