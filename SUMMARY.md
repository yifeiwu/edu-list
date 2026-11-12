# Edu-Domains — Run Summary

_Generated 2026-11-12 01:09 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24322** across **205** countries
- Active: **13093** (54%) · Inaccessible: **11229** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10763** domains (median 21 yrs)

## Last runs

- Verify (2026-11-12 01:09 UTC): validated 60, +0 Active, re-verified 60, pending left 0
- Curate (2026-11-11 18:28 UTC): 10695 raw candidates, 35 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4749 | 3592 | 1157 |
| FR | 3425 | 1651 | 1774 |
| CN | 1342 | 155 | 1187 |
| IN | 893 | 499 | 394 |
| JP | 823 | 229 | 594 |
| AU | 748 | 549 | 199 |
| DE | 616 | 345 | 271 |
| RU | 611 | 246 | 365 |
| ID | 594 | 358 | 236 |
| BR | 591 | 304 | 287 |
| UA | 574 | 244 | 330 |
| PL | 465 | 182 | 283 |
| ES | 418 | 269 | 149 |
| GB | 369 | 204 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13098 |
| `unreachable-dns` | 3332 |
| `fetch-error:ConnectTimeout` | 1485 |
| `fetch-error:ConnectionError` | 1224 |
| `low-confidence:http-2xx-html` | 1167 |
| `fetch-error:SSLError` | 1079 |
| `http-403` | 1055 |
| `empty-body` | 234 |
| `http-500` | 140 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 91 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **11520** (47%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3332**
- Moved pointers (old domain → new): **1013**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1342 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/823 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 150 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
