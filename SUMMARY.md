# Edu-Domains — Run Summary

_Generated 2026-11-17 20:56 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25225** across **206** countries
- Active: **13496** (54%) · Inaccessible: **11729** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11082** domains (median 21 yrs)

## Last runs

- Verify (2026-11-17 20:56 UTC): validated 45, +10 Active, re-verified 15, pending left 0
- Curate (2026-11-17 12:52 UTC): 10693 raw candidates, 28 queued, 60 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4779 | 3605 | 1174 |
| FR | 3612 | 1747 | 1865 |
| CN | 1375 | 153 | 1222 |
| JP | 933 | 265 | 668 |
| IN | 930 | 524 | 406 |
| AU | 762 | 559 | 203 |
| ID | 629 | 379 | 250 |
| DE | 624 | 350 | 274 |
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
| `http-2xx-html` | 13501 |
| `unreachable-dns` | 3458 |
| `fetch-error:ConnectTimeout` | 1551 |
| `fetch-error:ConnectionError` | 1284 |
| `low-confidence:http-2xx-html` | 1265 |
| `fetch-error:SSLError` | 1127 |
| `http-403` | 1094 |
| `empty-body` | 239 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 54 |

## Freshness

- Verified in last 30 days: **9350** (37%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3458**
- Moved pointers (old domain → new): **1049**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1375 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 265/933 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/161 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 295 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
