# Edu-Domains — Run Summary

_Generated 2026-10-11 20:01 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14883** across **204** countries
- Active: **8007** (54%) · Inaccessible: **6876** (46%)
- Pending queue: **3141** unvalidated candidates
- Known registration age: **6498** domains (median 24 yrs)

## Last runs

- Verify (2026-10-11 19:52 UTC): validated 119, +74 Active, re-verified 15, pending left 3071
- Curate (2026-10-11 20:01 UTC): 10679 raw candidates, 70 queued, 15 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3160 | 2374 | 786 |
| FR | 1342 | 695 | 647 |
| IN | 607 | 304 | 303 |
| JP | 607 | 135 | 472 |
| DE | 582 | 322 | 260 |
| AU | 580 | 408 | 172 |
| CN | 494 | 62 | 432 |
| BR | 477 | 229 | 248 |
| RU | 404 | 135 | 269 |
| KR | 305 | 83 | 222 |
| GB | 271 | 135 | 136 |
| ID | 256 | 150 | 106 |
| IR | 235 | 73 | 162 |
| TR | 203 | 137 | 66 |
| CA | 200 | 115 | 85 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8009 |
| `unreachable-dns` | 2413 |
| `fetch-error:ConnectTimeout` | 834 |
| `http-403` | 716 |
| `fetch-error:SSLError` | 678 |
| `fetch-error:ConnectionError` | 599 |
| `low-confidence:http-2xx-html` | 484 |
| `empty-body` | 151 |
| `fetch-error:ReadTimeout` | 78 |
| `http-500` | 46 |
| `http-404` | 42 |
| `http-503` | 27 |

## Freshness

- Verified in last 30 days: **14883** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2413**
- Moved pointers (old domain → new): **679**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 62/494 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 135/607 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 12/100 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 3 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
