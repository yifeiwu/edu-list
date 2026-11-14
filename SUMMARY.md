# Edu-Domains — Run Summary

_Generated 2026-11-14 13:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24738** across **206** countries
- Active: **13281** (54%) · Inaccessible: **11457** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10914** domains (median 21 yrs)

## Last runs

- Verify (2026-11-14 13:55 UTC): validated 61, +17 Active, re-verified 15, pending left 0
- Curate (2026-11-14 09:57 UTC): 10704 raw candidates, 45 queued, 55 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4767 | 3600 | 1167 |
| FR | 3505 | 1688 | 1817 |
| CN | 1359 | 157 | 1202 |
| IN | 910 | 512 | 398 |
| JP | 852 | 238 | 614 |
| AU | 759 | 557 | 202 |
| DE | 621 | 348 | 273 |
| RU | 616 | 248 | 368 |
| ID | 607 | 369 | 238 |
| BR | 598 | 308 | 290 |
| UA | 579 | 249 | 330 |
| PL | 473 | 183 | 290 |
| ES | 421 | 270 | 151 |
| GB | 374 | 209 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13286 |
| `unreachable-dns` | 3387 |
| `fetch-error:ConnectTimeout` | 1510 |
| `fetch-error:ConnectionError` | 1254 |
| `low-confidence:http-2xx-html` | 1217 |
| `fetch-error:SSLError` | 1100 |
| `http-403` | 1069 |
| `empty-body` | 236 |
| `http-500` | 144 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 94 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10893** (44%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3387**
- Moved pointers (old domain → new): **1034**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1359 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 238/852 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 218 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
