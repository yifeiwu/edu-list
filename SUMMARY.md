# Edu-Domains — Run Summary

_Generated 2026-11-13 05:42 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24490** across **205** countries
- Active: **13176** (54%) · Inaccessible: **11314** (46%)
- Pending queue: **45** unvalidated candidates
- Known registration age: **10824** domains (median 21 yrs)

## Last runs

- Verify (2026-11-13 03:05 UTC): validated 67, +31 Active, re-verified 15, pending left 0
- Curate (2026-11-13 05:42 UTC): 10684 raw candidates, 45 queued, 10600 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4757 | 3595 | 1162 |
| FR | 3463 | 1671 | 1792 |
| CN | 1353 | 156 | 1197 |
| IN | 899 | 503 | 396 |
| JP | 825 | 229 | 596 |
| AU | 752 | 551 | 201 |
| DE | 617 | 346 | 271 |
| RU | 614 | 248 | 366 |
| ID | 604 | 366 | 238 |
| BR | 593 | 306 | 287 |
| UA | 576 | 246 | 330 |
| PL | 467 | 182 | 285 |
| ES | 419 | 269 | 150 |
| GB | 370 | 205 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13181 |
| `unreachable-dns` | 3354 |
| `fetch-error:ConnectTimeout` | 1496 |
| `fetch-error:ConnectionError` | 1233 |
| `low-confidence:http-2xx-html` | 1185 |
| `fetch-error:SSLError` | 1091 |
| `http-403` | 1059 |
| `empty-body` | 234 |
| `http-500` | 141 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 93 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **11277** (46%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3354**
- Moved pointers (old domain → new): **1019**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1353 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/825 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 175 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
