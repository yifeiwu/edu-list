# Edu-Domains — Run Summary

_Generated 2026-11-01 02:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22895** across **205** countries
- Active: **12235** (53%) · Inaccessible: **10660** (47%)
- Pending queue: **33** unvalidated candidates
- Known registration age: **10122** domains (median 21 yrs)

## Last runs

- Verify (2026-11-01 00:33 UTC): validated 70, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-01 02:00 UTC): 10701 raw candidates, 33 queued, 10612 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4636 | 3506 | 1130 |
| FR | 3011 | 1455 | 1556 |
| CN | 1293 | 147 | 1146 |
| IN | 811 | 436 | 375 |
| JP | 799 | 222 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 585 | 228 | 357 |
| BR | 575 | 283 | 292 |
| ID | 552 | 329 | 223 |
| UA | 465 | 191 | 274 |
| PL | 458 | 179 | 279 |
| ES | 407 | 262 | 145 |
| KR | 341 | 96 | 245 |
| GB | 303 | 155 | 148 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12240 |
| `unreachable-dns` | 3244 |
| `fetch-error:ConnectTimeout` | 1379 |
| `fetch-error:ConnectionError` | 1127 |
| `low-confidence:http-2xx-html` | 1075 |
| `fetch-error:SSLError` | 1036 |
| `http-403` | 1020 |
| `empty-body` | 220 |
| `fetch-error:ReadTimeout` | 128 |
| `http-500` | 127 |
| `http-404` | 89 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15312** (67%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3244**
- Moved pointers (old domain → new): **958**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1293 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 222/799 (28%) — check for blocks/stale sources
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
