# Edu-Domains — Run Summary

_Generated 2026-11-18 11:41 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25311** across **206** countries
- Active: **13544** (54%) · Inaccessible: **11767** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11109** domains (median 21 yrs)

## Last runs

- Verify (2026-11-18 11:41 UTC): validated 55, +29 Active, re-verified 15, pending left 0
- Curate (2026-11-18 03:25 UTC): 10689 raw candidates, 39 queued, 10592 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4780 | 3606 | 1174 |
| FR | 3639 | 1759 | 1880 |
| CN | 1376 | 153 | 1223 |
| JP | 963 | 281 | 682 |
| IN | 931 | 524 | 407 |
| AU | 762 | 559 | 203 |
| ID | 639 | 387 | 252 |
| DE | 625 | 351 | 274 |
| RU | 622 | 251 | 371 |
| BR | 604 | 312 | 292 |
| UA | 584 | 252 | 332 |
| PL | 482 | 184 | 298 |
| ES | 421 | 270 | 151 |
| GB | 378 | 212 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13549 |
| `unreachable-dns` | 3472 |
| `fetch-error:ConnectTimeout` | 1559 |
| `fetch-error:ConnectionError` | 1285 |
| `low-confidence:http-2xx-html` | 1269 |
| `fetch-error:SSLError` | 1129 |
| `http-403` | 1096 |
| `empty-body` | 242 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 96 |
| `http-503` | 54 |

## Freshness

- Verified in last 30 days: **8651** (34%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3472**
- Moved pointers (old domain → new): **1052**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1376 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 281/963 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/161 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 302 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
