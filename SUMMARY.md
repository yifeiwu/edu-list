# Edu-Domains — Run Summary

_Generated 2026-09-16 21:44 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1986** across **84** countries
- Active: **1325** (67%) · Inaccessible: **661** (33%)
- Pending queue: **515** unvalidated candidates
- Known registration age: **1089** domains (median 24 yrs)

## Last runs

- Verify (2026-09-16 21:44 UTC): validated 122, +70 Active, re-verified 15, pending left 515
- Curate (2026-09-16 19:53 UTC): 177 raw candidates, 115 queued, 5 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 718 | 546 | 172 |
| AU | 224 | 165 | 59 |
| FR | 212 | 132 | 80 |
| XX | 92 | 41 | 51 |
| BE | 69 | 51 | 18 |
| BR | 60 | 30 | 30 |
| AT | 41 | 35 | 6 |
| GB | 38 | 26 | 12 |
| AM | 36 | 21 | 15 |
| CN | 36 | 13 | 23 |
| CH | 32 | 22 | 10 |
| AL | 28 | 15 | 13 |
| DE | 28 | 19 | 9 |
| IN | 28 | 20 | 8 |
| NG | 27 | 19 | 8 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1290 |
| `fetch-error:ConnectionError` | 174 |
| `http-403` | 129 |
| `low-confidence:http-2xx-html` | 97 |
| `fetch-error:ConnectTimeout` | 68 |
| `fetch-error:SSLError` | 48 |
| `empty-body` | 16 |
| `http-500` | 6 |
| `http-404` | 5 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 4 |
| `social-only/placeholder` | 3 |

## Freshness

- Verified in last 30 days: **1986** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **79**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `PH`: 4/13 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `XX`: 92 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
