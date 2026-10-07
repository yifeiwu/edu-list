# Edu-Domains — Run Summary

_Generated 2026-10-07 14:25 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12896** across **203** countries
- Active: **6881** (53%) · Inaccessible: **6015** (47%)
- Pending queue: **4014** unvalidated candidates
- Known registration age: **5647** domains (median 24 yrs)

## Last runs

- Verify (2026-10-07 13:25 UTC): validated 118, +68 Active, re-verified 15, pending left 3955
- Curate (2026-10-07 14:25 UTC): 10701 raw candidates, 59 queued, 40 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2806 | 2119 | 687 |
| FR | 793 | 412 | 381 |
| JP | 594 | 129 | 465 |
| IN | 545 | 278 | 267 |
| CN | 432 | 56 | 376 |
| AU | 427 | 294 | 133 |
| BR | 393 | 180 | 213 |
| DE | 393 | 190 | 203 |
| RU | 348 | 113 | 235 |
| KR | 280 | 75 | 205 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 213 | 69 | 144 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6883 |
| `fetch-error:ConnectionError` | 2732 |
| `fetch-error:ConnectTimeout` | 724 |
| `http-403` | 634 |
| `fetch-error:SSLError` | 598 |
| `low-confidence:http-2xx-html` | 370 |
| `empty-body` | 125 |
| `fetch-error:ReadTimeout` | 64 |
| `http-404` | 36 |
| `http-500` | 24 |
| `parking-linkfarm` | 22 |
| `http-503` | 15 |

## Freshness

- Verified in last 30 days: **12896** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **584**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 56/432 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 75/280 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/38 (29%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/90 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
