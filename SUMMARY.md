# Edu-Domains — Run Summary

_Generated 2026-10-09 15:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13734** across **204** countries
- Active: **7337** (53%) · Inaccessible: **6397** (47%)
- Pending queue: **3648** unvalidated candidates
- Known registration age: **6066** domains (median 24 yrs)

## Last runs

- Verify (2026-10-09 13:26 UTC): validated 121, +55 Active, re-verified 15, pending left 3597
- Curate (2026-10-09 15:55 UTC): 10701 raw candidates, 51 queued, 25 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2970 | 2238 | 732 |
| FR | 1086 | 574 | 512 |
| JP | 594 | 129 | 465 |
| IN | 552 | 281 | 271 |
| BR | 471 | 223 | 248 |
| CN | 471 | 61 | 410 |
| AU | 432 | 297 | 135 |
| DE | 431 | 221 | 210 |
| RU | 394 | 127 | 267 |
| KR | 286 | 78 | 208 |
| GB | 258 | 128 | 130 |
| ID | 240 | 140 | 100 |
| IR | 216 | 69 | 147 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7339 |
| `unreachable-dns` | 2338 |
| `fetch-error:ConnectTimeout` | 771 |
| `http-403` | 665 |
| `fetch-error:SSLError` | 637 |
| `fetch-error:ConnectionError` | 533 |
| `low-confidence:http-2xx-html` | 417 |
| `empty-body` | 128 |
| `fetch-error:ReadTimeout` | 74 |
| `http-404` | 38 |
| `http-500` | 33 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13734** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2338**
- Moved pointers (old domain → new): **625**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 61/471 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 78/286 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/39 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/92 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 1 unmapped country — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
