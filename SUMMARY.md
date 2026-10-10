# Edu-Domains — Run Summary

_Generated 2026-10-10 23:41 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14465** across **204** countries
- Active: **7751** (54%) · Inaccessible: **6714** (46%)
- Pending queue: **3313** unvalidated candidates
- Known registration age: **6363** domains (median 24 yrs)

## Last runs

- Verify (2026-10-10 23:41 UTC): validated 121, +44 Active, re-verified 15, pending left 3313
- Curate (2026-10-10 22:19 UTC): 10698 raw candidates, 63 queued, 24 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3105 | 2331 | 774 |
| FR | 1243 | 648 | 595 |
| JP | 602 | 133 | 469 |
| IN | 588 | 296 | 292 |
| DE | 562 | 309 | 253 |
| CN | 486 | 62 | 424 |
| AU | 483 | 331 | 152 |
| BR | 475 | 227 | 248 |
| RU | 401 | 132 | 269 |
| KR | 305 | 83 | 222 |
| GB | 265 | 131 | 134 |
| ID | 251 | 147 | 104 |
| IR | 224 | 71 | 153 |
| TR | 203 | 137 | 66 |
| CA | 199 | 114 | 85 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7753 |
| `unreachable-dns` | 2396 |
| `fetch-error:ConnectTimeout` | 815 |
| `http-403` | 691 |
| `fetch-error:SSLError` | 660 |
| `fetch-error:ConnectionError` | 573 |
| `low-confidence:http-2xx-html` | 463 |
| `empty-body` | 145 |
| `fetch-error:ReadTimeout` | 77 |
| `http-404` | 42 |
| `http-500` | 40 |
| `http-503` | 23 |

## Freshness

- Verified in last 30 days: **14465** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2396**
- Moved pointers (old domain → new): **660**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 62/486 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 133/602 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
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
