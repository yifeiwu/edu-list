# Edu-Domains — Run Summary

_Generated 2026-10-06 14:52 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12480** across **203** countries
- Active: **6623** (53%) · Inaccessible: **5857** (47%)
- Pending queue: **4222** unvalidated candidates
- Known registration age: **5435** domains (median 24 yrs)

## Last runs

- Verify (2026-10-06 14:33 UTC): validated 117, +80 Active, re-verified 15, pending left 4167
- Curate (2026-10-06 14:52 UTC): 10701 raw candidates, 55 queued, 45 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2734 | 2066 | 668 |
| FR | 653 | 331 | 322 |
| JP | 582 | 126 | 456 |
| IN | 526 | 266 | 260 |
| CN | 426 | 54 | 372 |
| DE | 389 | 186 | 203 |
| AU | 382 | 263 | 119 |
| BR | 360 | 168 | 192 |
| RU | 336 | 108 | 228 |
| KR | 279 | 74 | 205 |
| GB | 251 | 122 | 129 |
| ID | 227 | 132 | 95 |
| IR | 212 | 69 | 143 |
| TR | 200 | 137 | 63 |
| CA | 190 | 107 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6625 |
| `fetch-error:ConnectionError` | 2683 |
| `fetch-error:ConnectTimeout` | 706 |
| `http-403` | 615 |
| `fetch-error:SSLError` | 579 |
| `low-confidence:http-2xx-html` | 347 |
| `empty-body` | 122 |
| `fetch-error:ReadTimeout` | 62 |
| `http-404` | 36 |
| `http-500` | 23 |
| `parking-linkfarm` | 22 |
| `parking` | 14 |

## Freshness

- Verified in last 30 days: **12480** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **564**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 54/426 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 126/582 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 74/279 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/37 (30%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 9/87 (10%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
