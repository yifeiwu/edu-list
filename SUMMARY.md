# Edu-Domains — Run Summary

_Generated 2026-11-14 21:10 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24784** across **206** countries
- Active: **13297** (54%) · Inaccessible: **11487** (46%)
- Pending queue: **46** unvalidated candidates
- Known registration age: **10924** domains (median 21 yrs)

## Last runs

- Verify (2026-11-14 19:19 UTC): validated 61, +17 Active, re-verified 15, pending left 0
- Curate (2026-11-14 21:10 UTC): 10694 raw candidates, 46 queued, 47 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4767 | 3600 | 1167 |
| FR | 3514 | 1691 | 1823 |
| CN | 1361 | 156 | 1205 |
| IN | 911 | 513 | 398 |
| JP | 864 | 242 | 622 |
| AU | 759 | 557 | 202 |
| DE | 621 | 348 | 273 |
| RU | 616 | 248 | 368 |
| ID | 607 | 369 | 238 |
| BR | 599 | 309 | 290 |
| UA | 580 | 249 | 331 |
| PL | 473 | 183 | 290 |
| ES | 421 | 270 | 151 |
| GB | 374 | 209 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13302 |
| `unreachable-dns` | 3400 |
| `fetch-error:ConnectTimeout` | 1514 |
| `fetch-error:ConnectionError` | 1256 |
| `low-confidence:http-2xx-html` | 1223 |
| `fetch-error:SSLError` | 1101 |
| `http-403` | 1071 |
| `empty-body` | 237 |
| `http-500` | 145 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 94 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10954** (44%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3400**
- Moved pointers (old domain → new): **1034**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1361 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 242/864 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 223 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
