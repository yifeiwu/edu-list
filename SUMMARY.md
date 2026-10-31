# Edu-Domains — Run Summary

_Generated 2026-10-31 22:20 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22840** across **205** countries
- Active: **12213** (53%) · Inaccessible: **10627** (47%)
- Pending queue: **53** unvalidated candidates
- Known registration age: **10096** domains (median 21 yrs)

## Last runs

- Verify (2026-10-31 21:36 UTC): validated 66, +29 Active, re-verified 15, pending left 0
- Curate (2026-10-31 22:20 UTC): 10699 raw candidates, 53 queued, 47 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4624 | 3498 | 1126 |
| FR | 3001 | 1453 | 1548 |
| CN | 1293 | 147 | 1146 |
| IN | 809 | 435 | 374 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 584 | 227 | 357 |
| BR | 575 | 283 | 292 |
| ID | 550 | 329 | 221 |
| PL | 458 | 179 | 279 |
| UA | 451 | 188 | 263 |
| ES | 407 | 262 | 145 |
| KR | 341 | 96 | 245 |
| GB | 303 | 155 | 148 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12218 |
| `unreachable-dns` | 3241 |
| `fetch-error:ConnectTimeout` | 1375 |
| `fetch-error:ConnectionError` | 1124 |
| `low-confidence:http-2xx-html` | 1070 |
| `fetch-error:SSLError` | 1032 |
| `http-403` | 1015 |
| `empty-body` | 218 |
| `fetch-error:ReadTimeout` | 127 |
| `http-500` | 127 |
| `http-404` | 88 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15718** (69%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3241**
- Moved pointers (old domain → new): **956**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1293 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/341 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/152 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
