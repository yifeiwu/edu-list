# Edu-Domains — Run Summary

_Generated 2026-11-19 01:34 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25375** across **206** countries
- Active: **13574** (53%) · Inaccessible: **11801** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11132** domains (median 21 yrs)

## Last runs

- Verify (2026-11-19 01:34 UTC): validated 45, +20 Active, re-verified 15, pending left 0
- Curate (2026-11-18 21:11 UTC): 10707 raw candidates, 30 queued, 69 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4781 | 3607 | 1174 |
| FR | 3641 | 1761 | 1880 |
| CN | 1381 | 153 | 1228 |
| JP | 977 | 285 | 692 |
| IN | 934 | 526 | 408 |
| AU | 762 | 559 | 203 |
| ID | 659 | 398 | 261 |
| DE | 626 | 352 | 274 |
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
| `http-2xx-html` | 13579 |
| `unreachable-dns` | 3490 |
| `fetch-error:ConnectTimeout` | 1563 |
| `fetch-error:ConnectionError` | 1287 |
| `low-confidence:http-2xx-html` | 1272 |
| `fetch-error:SSLError` | 1129 |
| `http-403` | 1101 |
| `empty-body` | 243 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 97 |
| `http-503` | 54 |

## Freshness

- Verified in last 30 days: **8158** (32%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3490**
- Moved pointers (old domain → new): **1052**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1381 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/977 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 26/162 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 303 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
