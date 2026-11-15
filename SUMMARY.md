# Edu-Domains — Run Summary

_Generated 2026-11-15 02:46 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24874** across **206** countries
- Active: **13332** (54%) · Inaccessible: **11542** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10956** domains (median 21 yrs)

## Last runs

- Verify (2026-11-15 02:46 UTC): validated 59, +13 Active, re-verified 15, pending left 0
- Curate (2026-11-15 01:34 UTC): 10704 raw candidates, 43 queued, 10608 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4769 | 3600 | 1169 |
| FR | 3530 | 1701 | 1829 |
| CN | 1368 | 156 | 1212 |
| IN | 919 | 517 | 402 |
| JP | 878 | 246 | 632 |
| AU | 759 | 557 | 202 |
| DE | 621 | 348 | 273 |
| RU | 617 | 248 | 369 |
| ID | 609 | 371 | 238 |
| BR | 601 | 310 | 291 |
| UA | 581 | 249 | 332 |
| PL | 474 | 183 | 291 |
| ES | 421 | 270 | 151 |
| GB | 375 | 210 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13337 |
| `unreachable-dns` | 3418 |
| `fetch-error:ConnectTimeout` | 1521 |
| `fetch-error:ConnectionError` | 1264 |
| `low-confidence:http-2xx-html` | 1233 |
| `fetch-error:SSLError` | 1105 |
| `http-403` | 1076 |
| `empty-body` | 237 |
| `http-500` | 146 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10420** (42%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3418**
- Moved pointers (old domain → new): **1034**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 156/1368 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 246/878 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 242 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
