# Edu-Domains — Run Summary

_Generated 2026-11-21 13:06 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25643** across **207** countries
- Active: **13718** (53%) · Inaccessible: **11925** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11259** domains (median 21 yrs)

## Last runs

- Verify (2026-11-21 13:06 UTC): validated 50, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-21 09:23 UTC): 10696 raw candidates, 32 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4788 | 3610 | 1178 |
| FR | 3730 | 1798 | 1932 |
| CN | 1388 | 153 | 1235 |
| JP | 979 | 285 | 694 |
| IN | 947 | 536 | 411 |
| AU | 763 | 560 | 203 |
| ID | 705 | 430 | 275 |
| DE | 638 | 360 | 278 |
| RU | 627 | 254 | 373 |
| BR | 612 | 317 | 295 |
| UA | 586 | 253 | 333 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 380 | 214 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13723 |
| `unreachable-dns` | 3522 |
| `fetch-error:ConnectTimeout` | 1583 |
| `fetch-error:ConnectionError` | 1302 |
| `low-confidence:http-2xx-html` | 1293 |
| `fetch-error:SSLError` | 1137 |
| `http-403` | 1107 |
| `empty-body` | 246 |
| `http-500` | 152 |
| `fetch-error:ReadTimeout` | 141 |
| `http-404` | 97 |
| `http-503` | 56 |

## Freshness

- Verified in last 30 days: **7250** (28%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3522**
- Moved pointers (old domain → new): **1060**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1388 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/979 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 300 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
