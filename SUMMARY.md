# Edu-Domains — Run Summary

_Generated 2026-11-19 18:46 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25457** across **207** countries
- Active: **13619** (53%) · Inaccessible: **11838** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11167** domains (median 21 yrs)

## Last runs

- Verify (2026-11-19 18:46 UTC): validated 62, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-19 11:27 UTC): 10694 raw candidates, 47 queued, 45 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4781 | 3607 | 1174 |
| FR | 3664 | 1770 | 1894 |
| CN | 1387 | 153 | 1234 |
| JP | 978 | 285 | 693 |
| IN | 938 | 530 | 408 |
| AU | 762 | 559 | 203 |
| ID | 677 | 411 | 266 |
| DE | 627 | 353 | 274 |
| RU | 624 | 252 | 372 |
| BR | 604 | 312 | 292 |
| UA | 584 | 252 | 332 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 378 | 212 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13624 |
| `unreachable-dns` | 3501 |
| `fetch-error:ConnectTimeout` | 1566 |
| `fetch-error:ConnectionError` | 1293 |
| `low-confidence:http-2xx-html` | 1282 |
| `fetch-error:SSLError` | 1133 |
| `http-403` | 1101 |
| `empty-body` | 244 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 97 |
| `http-503` | 55 |

## Freshness

- Verified in last 30 days: **8270** (32%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3501**
- Moved pointers (old domain → new): **1052**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1387 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/978 (29%) — check for blocks/stale sources
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
