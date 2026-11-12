# Edu-Domains — Run Summary

_Generated 2026-11-12 23:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24438** across **205** countries
- Active: **13145** (54%) · Inaccessible: **11293** (46%)
- Pending queue: **49** unvalidated candidates
- Known registration age: **10802** domains (median 21 yrs)

## Last runs

- Verify (2026-11-12 22:49 UTC): validated 62, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-12 23:31 UTC): 10704 raw candidates, 49 queued, 50 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4754 | 3593 | 1161 |
| FR | 3454 | 1665 | 1789 |
| CN | 1352 | 156 | 1196 |
| IN | 895 | 501 | 394 |
| JP | 825 | 229 | 596 |
| AU | 750 | 551 | 199 |
| DE | 617 | 346 | 271 |
| RU | 613 | 247 | 366 |
| ID | 602 | 364 | 238 |
| BR | 591 | 304 | 287 |
| UA | 576 | 246 | 330 |
| PL | 466 | 182 | 284 |
| ES | 419 | 269 | 150 |
| GB | 370 | 205 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13150 |
| `unreachable-dns` | 3350 |
| `fetch-error:ConnectTimeout` | 1489 |
| `fetch-error:ConnectionError` | 1231 |
| `low-confidence:http-2xx-html` | 1182 |
| `fetch-error:SSLError` | 1089 |
| `http-403` | 1059 |
| `empty-body` | 234 |
| `http-500` | 141 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 93 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **11681** (48%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3350**
- Moved pointers (old domain → new): **1016**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1352 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/825 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 163 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
