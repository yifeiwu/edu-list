# Edu-Domains — Run Summary

_Generated 2026-11-19 11:27 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25410** across **206** countries
- Active: **13599** (54%) · Inaccessible: **11811** (46%)
- Pending queue: **47** unvalidated candidates
- Known registration age: **11146** domains (median 21 yrs)

## Last runs

- Verify (2026-11-19 09:33 UTC): validated 50, +25 Active, re-verified 15, pending left 0
- Curate (2026-11-19 11:27 UTC): 10694 raw candidates, 47 queued, 45 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4781 | 3607 | 1174 |
| FR | 3648 | 1766 | 1882 |
| CN | 1383 | 153 | 1230 |
| JP | 977 | 285 | 692 |
| IN | 937 | 529 | 408 |
| AU | 762 | 559 | 203 |
| ID | 668 | 404 | 264 |
| DE | 627 | 353 | 274 |
| RU | 623 | 252 | 371 |
| BR | 604 | 312 | 292 |
| UA | 584 | 252 | 332 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 378 | 212 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13604 |
| `unreachable-dns` | 3495 |
| `fetch-error:ConnectTimeout` | 1563 |
| `fetch-error:ConnectionError` | 1287 |
| `low-confidence:http-2xx-html` | 1275 |
| `fetch-error:SSLError` | 1129 |
| `http-403` | 1102 |
| `empty-body` | 243 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 97 |
| `http-503` | 54 |

## Freshness

- Verified in last 30 days: **8208** (32%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3495**
- Moved pointers (old domain → new): **1052**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1383 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/977 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 26/162 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 303 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
