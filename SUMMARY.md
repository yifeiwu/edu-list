# Edu-Domains — Run Summary

_Generated 2026-11-18 03:25 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25271** across **206** countries
- Active: **13515** (53%) · Inaccessible: **11756** (47%)
- Pending queue: **39** unvalidated candidates
- Known registration age: **11089** domains (median 21 yrs)

## Last runs

- Verify (2026-11-18 03:01 UTC): validated 61, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-18 03:25 UTC): 10689 raw candidates, 39 queued, 10592 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4779 | 3605 | 1174 |
| FR | 3627 | 1750 | 1877 |
| CN | 1376 | 153 | 1223 |
| JP | 948 | 271 | 677 |
| IN | 930 | 524 | 406 |
| AU | 762 | 559 | 203 |
| ID | 631 | 381 | 250 |
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
| `http-2xx-html` | 13520 |
| `unreachable-dns` | 3467 |
| `fetch-error:ConnectTimeout` | 1559 |
| `fetch-error:ConnectionError` | 1284 |
| `low-confidence:http-2xx-html` | 1268 |
| `fetch-error:SSLError` | 1128 |
| `http-403` | 1095 |
| `empty-body` | 241 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 96 |
| `http-503` | 54 |

## Freshness

- Verified in last 30 days: **8596** (34%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3467**
- Moved pointers (old domain → new): **1051**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1376 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 271/948 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/161 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 301 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
