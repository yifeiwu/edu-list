# Edu-Domains — Run Summary

_Generated 2026-11-25 10:34 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25907** across **207** countries
- Active: **13871** (54%) · Inaccessible: **12036** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11394** domains (median 21 yrs)

## Last runs

- Verify (2026-11-25 10:34 UTC): validated 40, +13 Active, re-verified 15, pending left 0
- Curate (2026-11-25 02:01 UTC): 10706 raw candidates, 23 queued, 10616 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4804 | 3617 | 1187 |
| FR | 3827 | 1847 | 1980 |
| CN | 1394 | 154 | 1240 |
| JP | 983 | 286 | 697 |
| IN | 960 | 543 | 417 |
| AU | 763 | 561 | 202 |
| ID | 759 | 466 | 293 |
| DE | 645 | 366 | 279 |
| RU | 632 | 255 | 377 |
| BR | 614 | 318 | 296 |
| UA | 587 | 254 | 333 |
| PL | 489 | 185 | 304 |
| ES | 422 | 270 | 152 |
| GB | 380 | 214 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13876 |
| `unreachable-dns` | 3532 |
| `fetch-error:ConnectTimeout` | 1609 |
| `fetch-error:ConnectionError` | 1318 |
| `low-confidence:http-2xx-html` | 1316 |
| `fetch-error:SSLError` | 1139 |
| `http-403` | 1117 |
| `empty-body` | 249 |
| `http-500` | 152 |
| `fetch-error:ReadTimeout` | 143 |
| `http-404` | 99 |
| `http-503` | 58 |

## Freshness

- Verified in last 30 days: **6260** (24%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3532**
- Moved pointers (old domain → new): **1070**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 154/1394 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/983 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 299 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
