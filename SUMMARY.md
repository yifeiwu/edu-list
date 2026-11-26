# Edu-Domains — Run Summary

_Generated 2026-11-26 22:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **26007** across **207** countries
- Active: **13921** (54%) · Inaccessible: **12086** (46%)
- Pending queue: **32** unvalidated candidates
- Known registration age: **11439** domains (median 20 yrs)

## Last runs

- Verify (2026-11-26 22:00 UTC): validated 44, +14 Active, re-verified 15, pending left 0
- Curate (2026-11-26 22:53 UTC): 10705 raw candidates, 32 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4813 | 3625 | 1188 |
| FR | 3854 | 1856 | 1998 |
| CN | 1404 | 156 | 1248 |
| JP | 983 | 286 | 697 |
| IN | 967 | 549 | 418 |
| AU | 764 | 562 | 202 |
| ID | 763 | 468 | 295 |
| DE | 649 | 366 | 283 |
| RU | 634 | 256 | 378 |
| BR | 618 | 320 | 298 |
| UA | 587 | 254 | 333 |
| PL | 494 | 186 | 308 |
| ES | 422 | 270 | 152 |
| GB | 382 | 216 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13926 |
| `unreachable-dns` | 3545 |
| `fetch-error:ConnectTimeout` | 1621 |
| `low-confidence:http-2xx-html` | 1324 |
| `fetch-error:ConnectionError` | 1320 |
| `fetch-error:SSLError` | 1144 |
| `http-403` | 1120 |
| `empty-body` | 248 |
| `http-500` | 153 |
| `fetch-error:ReadTimeout` | 144 |
| `http-404` | 101 |
| `http-503` | 58 |

## Freshness

- Verified in last 30 days: **6201** (24%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3545**
- Moved pointers (old domain → new): **1075**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1404 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/983 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 298 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
