# Edu-Domains — Run Summary

_Generated 2026-11-13 14:12 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24537** across **205** countries
- Active: **13194** (54%) · Inaccessible: **11343** (46%)
- Pending queue: **43** unvalidated candidates
- Known registration age: **10836** domains (median 21 yrs)

## Last runs

- Verify (2026-11-13 11:00 UTC): validated 62, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-13 14:12 UTC): 10705 raw candidates, 43 queued, 60 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4758 | 3595 | 1163 |
| FR | 3469 | 1673 | 1796 |
| CN | 1355 | 157 | 1198 |
| IN | 901 | 505 | 396 |
| JP | 837 | 233 | 604 |
| AU | 754 | 553 | 201 |
| DE | 618 | 347 | 271 |
| RU | 615 | 248 | 367 |
| ID | 605 | 367 | 238 |
| BR | 594 | 306 | 288 |
| UA | 577 | 247 | 330 |
| PL | 468 | 182 | 286 |
| ES | 419 | 269 | 150 |
| GB | 372 | 207 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13199 |
| `unreachable-dns` | 3361 |
| `fetch-error:ConnectTimeout` | 1498 |
| `fetch-error:ConnectionError` | 1237 |
| `low-confidence:http-2xx-html` | 1191 |
| `fetch-error:SSLError` | 1093 |
| `http-403` | 1063 |
| `empty-body` | 234 |
| `http-500` | 142 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 93 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **11339** (46%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3361**
- Moved pointers (old domain → new): **1021**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1355 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 233/837 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 187 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
