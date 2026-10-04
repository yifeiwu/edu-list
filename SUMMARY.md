# Edu-Domains — Run Summary

_Generated 2026-10-04 23:39 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **11856** across **203** countries
- Active: **6188** (52%) · Inaccessible: **5668** (48%)
- Pending queue: **4503** unvalidated candidates
- Known registration age: **5030** domains (median 24 yrs)

## Last runs

- Verify (2026-10-04 23:39 UTC): validated 115, +76 Active, re-verified 15, pending left 4503
- Curate (2026-10-04 23:02 UTC): 10686 raw candidates, 63 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2445 | 1846 | 599 |
| FR | 619 | 313 | 306 |
| JP | 577 | 125 | 452 |
| IN | 459 | 209 | 250 |
| CN | 415 | 52 | 363 |
| AU | 375 | 259 | 116 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| RU | 336 | 108 | 228 |
| KR | 278 | 73 | 205 |
| GB | 234 | 113 | 121 |
| ID | 224 | 130 | 94 |
| IR | 212 | 69 | 143 |
| TR | 189 | 130 | 59 |
| CA | 174 | 95 | 79 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6190 |
| `fetch-error:ConnectionError` | 2605 |
| `fetch-error:ConnectTimeout` | 690 |
| `http-403` | 580 |
| `fetch-error:SSLError` | 560 |
| `low-confidence:http-2xx-html` | 345 |
| `empty-body` | 122 |
| `fetch-error:ReadTimeout` | 61 |
| `http-404` | 35 |
| `http-500` | 23 |
| `parking-linkfarm` | 21 |
| `parking` | 14 |

## Freshness

- Verified in last 30 days: **11856** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **531**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 52/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 125/577 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 73/278 (26%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 9/85 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
