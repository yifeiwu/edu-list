# Edu-Domains — Run Summary

_Generated 2026-10-07 06:07 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12793** across **203** countries
- Active: **6813** (53%) · Inaccessible: **5980** (47%)
- Pending queue: **4001** unvalidated candidates
- Known registration age: **5594** domains (median 24 yrs)

## Last runs

- Verify (2026-10-07 06:07 UTC): validated 125, +46 Active, re-verified 15, pending left 4001
- Curate (2026-10-07 00:28 UTC): 10700 raw candidates, 40 queued, 10600 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2779 | 2100 | 679 |
| FR | 755 | 382 | 373 |
| JP | 594 | 129 | 465 |
| IN | 544 | 278 | 266 |
| CN | 430 | 55 | 375 |
| AU | 417 | 287 | 130 |
| DE | 393 | 190 | 203 |
| BR | 388 | 179 | 209 |
| RU | 336 | 108 | 228 |
| KR | 280 | 75 | 205 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 212 | 69 | 143 |
| TR | 200 | 137 | 63 |
| CA | 191 | 108 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6815 |
| `fetch-error:ConnectionError` | 2718 |
| `fetch-error:ConnectTimeout` | 723 |
| `http-403` | 630 |
| `fetch-error:SSLError` | 596 |
| `low-confidence:http-2xx-html` | 363 |
| `empty-body` | 125 |
| `fetch-error:ReadTimeout` | 62 |
| `http-404` | 36 |
| `http-500` | 24 |
| `parking-linkfarm` | 22 |
| `http-503` | 15 |

## Freshness

- Verified in last 30 days: **12793** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **579**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 55/430 (13%) — check for blocks/stale sources
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
