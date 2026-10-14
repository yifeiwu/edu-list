# Edu-Domains — Run Summary

_Generated 2026-10-14 01:21 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15806** across **204** countries
- Active: **8588** (54%) · Inaccessible: **7218** (46%)
- Pending queue: **2641** unvalidated candidates
- Known registration age: **6824** domains (median 24 yrs)

## Last runs

- Verify (2026-10-14 01:21 UTC): validated 118, +61 Active, re-verified 15, pending left 2641
- Curate (2026-10-14 00:57 UTC): 10689 raw candidates, 40 queued, 10588 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3302 | 2487 | 815 |
| FR | 1544 | 784 | 760 |
| AU | 689 | 500 | 189 |
| JP | 623 | 145 | 478 |
| IN | 621 | 313 | 308 |
| DE | 590 | 328 | 262 |
| CN | 513 | 66 | 447 |
| BR | 483 | 233 | 250 |
| RU | 408 | 136 | 272 |
| KR | 310 | 85 | 225 |
| GB | 271 | 135 | 136 |
| ID | 270 | 160 | 110 |
| IR | 244 | 76 | 168 |
| CA | 216 | 131 | 85 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8590 |
| `unreachable-dns` | 2470 |
| `fetch-error:ConnectTimeout` | 890 |
| `http-403` | 749 |
| `fetch-error:SSLError` | 702 |
| `fetch-error:ConnectionError` | 640 |
| `low-confidence:http-2xx-html` | 550 |
| `empty-body` | 161 |
| `fetch-error:ReadTimeout` | 82 |
| `http-500` | 55 |
| `http-404` | 46 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **15806** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2470**
- Moved pointers (old domain → new): **709**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 66/513 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 145/623 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/310 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 13/102 (13%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
