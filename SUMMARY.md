# Edu-Domains — Run Summary

_Generated 2026-11-10 22:14 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24190** across **205** countries
- Active: **13012** (54%) · Inaccessible: **11178** (46%)
- Pending queue: **32** unvalidated candidates
- Known registration age: **10706** domains (median 21 yrs)

## Last runs

- Verify (2026-11-10 17:52 UTC): validated 46, +16 Active, re-verified 15, pending left 0
- Curate (2026-11-10 22:14 UTC): 10697 raw candidates, 32 queued, 59 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4740 | 3586 | 1154 |
| FR | 3385 | 1633 | 1752 |
| CN | 1338 | 155 | 1183 |
| IN | 883 | 492 | 391 |
| JP | 823 | 229 | 594 |
| AU | 744 | 545 | 199 |
| DE | 613 | 345 | 268 |
| RU | 609 | 245 | 364 |
| BR | 591 | 304 | 287 |
| ID | 591 | 355 | 236 |
| UA | 573 | 243 | 330 |
| PL | 463 | 180 | 283 |
| ES | 417 | 269 | 148 |
| GB | 369 | 204 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13017 |
| `unreachable-dns` | 3329 |
| `fetch-error:ConnectTimeout` | 1464 |
| `fetch-error:ConnectionError` | 1224 |
| `low-confidence:http-2xx-html` | 1157 |
| `fetch-error:SSLError` | 1077 |
| `http-403` | 1052 |
| `empty-body` | 235 |
| `http-500` | 139 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 91 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **12215** (50%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3329**
- Moved pointers (old domain → new): **1004**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1338 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/823 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 140 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
