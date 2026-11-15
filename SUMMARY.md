# Edu-Domains — Run Summary

_Generated 2026-11-15 16:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24934** across **206** countries
- Active: **13361** (54%) · Inaccessible: **11573** (46%)
- Pending queue: **43** unvalidated candidates
- Known registration age: **10973** domains (median 21 yrs)

## Last runs

- Verify (2026-11-15 10:06 UTC): validated 75, +28 Active, re-verified 15, pending left 0
- Curate (2026-11-15 16:11 UTC): 10696 raw candidates, 43 queued, 53 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4770 | 3601 | 1169 |
| FR | 3544 | 1708 | 1836 |
| CN | 1370 | 157 | 1213 |
| IN | 921 | 519 | 402 |
| JP | 893 | 253 | 640 |
| AU | 759 | 557 | 202 |
| DE | 622 | 348 | 274 |
| RU | 619 | 250 | 369 |
| ID | 611 | 371 | 240 |
| BR | 601 | 310 | 291 |
| UA | 581 | 249 | 332 |
| PL | 476 | 184 | 292 |
| ES | 421 | 270 | 151 |
| GB | 375 | 210 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13366 |
| `unreachable-dns` | 3428 |
| `fetch-error:ConnectTimeout` | 1528 |
| `fetch-error:ConnectionError` | 1267 |
| `low-confidence:http-2xx-html` | 1236 |
| `fetch-error:SSLError` | 1105 |
| `http-403` | 1079 |
| `empty-body` | 237 |
| `http-500` | 146 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10495** (42%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3428**
- Moved pointers (old domain → new): **1038**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1370 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 253/893 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 253 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
