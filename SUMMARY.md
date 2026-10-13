# Edu-Domains — Run Summary

_Generated 2026-10-13 17:22 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15602** across **204** countries
- Active: **8466** (54%) · Inaccessible: **7136** (46%)
- Pending queue: **2751** unvalidated candidates
- Known registration age: **6750** domains (median 24 yrs)

## Last runs

- Verify (2026-10-13 17:22 UTC): validated 117, +68 Active, re-verified 15, pending left 2751
- Curate (2026-10-13 15:41 UTC): 10689 raw candidates, 43 queued, 38 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3278 | 2468 | 810 |
| FR | 1492 | 753 | 739 |
| AU | 683 | 495 | 188 |
| JP | 623 | 145 | 478 |
| IN | 616 | 308 | 308 |
| DE | 588 | 327 | 261 |
| CN | 508 | 65 | 443 |
| BR | 479 | 230 | 249 |
| RU | 407 | 136 | 271 |
| KR | 309 | 85 | 224 |
| GB | 271 | 135 | 136 |
| ID | 270 | 160 | 110 |
| IR | 238 | 73 | 165 |
| CA | 215 | 130 | 85 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8468 |
| `unreachable-dns` | 2457 |
| `fetch-error:ConnectTimeout` | 878 |
| `http-403` | 740 |
| `fetch-error:SSLError` | 696 |
| `fetch-error:ConnectionError` | 637 |
| `low-confidence:http-2xx-html` | 524 |
| `empty-body` | 160 |
| `fetch-error:ReadTimeout` | 82 |
| `http-500` | 51 |
| `http-404` | 44 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **15602** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2457**
- Moved pointers (old domain → new): **704**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 65/508 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 145/623 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/309 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 13/102 (13%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 7 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
