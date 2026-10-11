# Edu-Domains — Run Summary

_Generated 2026-10-11 02:22 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14569** across **204** countries
- Active: **7816** (54%) · Inaccessible: **6753** (46%)
- Pending queue: **3266** unvalidated candidates
- Known registration age: **6391** domains (median 24 yrs)

## Last runs

- Verify (2026-10-11 02:22 UTC): validated 119, +64 Active, re-verified 15, pending left 3266
- Curate (2026-10-11 01:39 UTC): 10696 raw candidates, 54 queued, 10572 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3109 | 2334 | 775 |
| FR | 1271 | 661 | 610 |
| JP | 603 | 133 | 470 |
| IN | 600 | 298 | 302 |
| DE | 569 | 315 | 254 |
| AU | 516 | 359 | 157 |
| CN | 487 | 62 | 425 |
| BR | 476 | 228 | 248 |
| RU | 402 | 133 | 269 |
| KR | 305 | 83 | 222 |
| GB | 265 | 131 | 134 |
| ID | 252 | 147 | 105 |
| IR | 228 | 72 | 156 |
| TR | 203 | 137 | 66 |
| CA | 199 | 114 | 85 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7818 |
| `unreachable-dns` | 2402 |
| `fetch-error:ConnectTimeout` | 824 |
| `http-403` | 692 |
| `fetch-error:SSLError` | 668 |
| `fetch-error:ConnectionError` | 579 |
| `low-confidence:http-2xx-html` | 465 |
| `empty-body` | 146 |
| `fetch-error:ReadTimeout` | 78 |
| `http-404` | 42 |
| `http-500` | 41 |
| `http-503` | 23 |

## Freshness

- Verified in last 30 days: **14569** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2402**
- Moved pointers (old domain → new): **664**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 62/487 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 133/603 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/97 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 2 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
