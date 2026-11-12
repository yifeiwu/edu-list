# Edu-Domains — Run Summary

_Generated 2026-11-12 17:09 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24391** across **205** countries
- Active: **13128** (54%) · Inaccessible: **11263** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10789** domains (median 21 yrs)

## Last runs

- Verify (2026-11-12 17:09 UTC): validated 51, +17 Active, re-verified 15, pending left 0
- Curate (2026-11-12 09:37 UTC): 10678 raw candidates, 35 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4750 | 3593 | 1157 |
| FR | 3443 | 1661 | 1782 |
| CN | 1351 | 156 | 1195 |
| IN | 895 | 501 | 394 |
| JP | 824 | 229 | 595 |
| AU | 749 | 550 | 199 |
| DE | 617 | 346 | 271 |
| RU | 611 | 246 | 365 |
| ID | 602 | 364 | 238 |
| BR | 591 | 304 | 287 |
| UA | 576 | 246 | 330 |
| PL | 466 | 182 | 284 |
| ES | 418 | 269 | 149 |
| GB | 369 | 204 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13133 |
| `unreachable-dns` | 3343 |
| `fetch-error:ConnectTimeout` | 1486 |
| `fetch-error:ConnectionError` | 1228 |
| `low-confidence:http-2xx-html` | 1174 |
| `fetch-error:SSLError` | 1085 |
| `http-403` | 1057 |
| `empty-body` | 234 |
| `http-500` | 141 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 92 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **11619** (48%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3343**
- Moved pointers (old domain → new): **1014**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1351 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/824 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 155 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
