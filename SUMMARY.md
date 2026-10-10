# Edu-Domains — Run Summary

_Generated 2026-10-10 16:03 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14255** across **204** countries
- Active: **7642** (54%) · Inaccessible: **6613** (46%)
- Pending queue: **3390** unvalidated candidates
- Known registration age: **6306** domains (median 24 yrs)

## Last runs

- Verify (2026-10-10 16:03 UTC): validated 119, +55 Active, re-verified 15, pending left 3390
- Curate (2026-10-10 13:23 UTC): 10700 raw candidates, 51 queued, 30 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3081 | 2318 | 763 |
| FR | 1204 | 637 | 567 |
| JP | 597 | 131 | 466 |
| IN | 575 | 291 | 284 |
| DE | 526 | 291 | 235 |
| CN | 480 | 61 | 419 |
| BR | 473 | 225 | 248 |
| AU | 435 | 299 | 136 |
| RU | 399 | 130 | 269 |
| KR | 302 | 81 | 221 |
| GB | 264 | 130 | 134 |
| ID | 251 | 147 | 104 |
| IR | 219 | 69 | 150 |
| TR | 203 | 137 | 66 |
| CA | 195 | 112 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7644 |
| `unreachable-dns` | 2380 |
| `fetch-error:ConnectTimeout` | 803 |
| `http-403` | 680 |
| `fetch-error:SSLError` | 650 |
| `fetch-error:ConnectionError` | 563 |
| `low-confidence:http-2xx-html` | 454 |
| `empty-body` | 134 |
| `fetch-error:ReadTimeout` | 76 |
| `http-404` | 41 |
| `http-500` | 37 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **14255** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2380**
- Moved pointers (old domain → new): **650**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 61/480 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 131/597 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 81/302 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/97 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 1 unmapped country — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
