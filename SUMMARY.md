# Edu-Domains — Run Summary

_Generated 2026-10-08 06:09 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13211** across **203** countries
- Active: **7058** (53%) · Inaccessible: **6153** (47%)
- Pending queue: **3828** unvalidated candidates
- Known registration age: **5843** domains (median 24 yrs)

## Last runs

- Verify (2026-10-08 06:09 UTC): validated 119, +60 Active, re-verified 15, pending left 3828
- Curate (2026-10-08 00:48 UTC): 10701 raw candidates, 60 queued, 10576 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2868 | 2164 | 704 |
| FR | 938 | 496 | 442 |
| JP | 594 | 129 | 465 |
| IN | 546 | 278 | 268 |
| BR | 448 | 211 | 237 |
| CN | 436 | 57 | 379 |
| AU | 428 | 295 | 133 |
| DE | 393 | 190 | 203 |
| RU | 365 | 118 | 247 |
| KR | 283 | 77 | 206 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 213 | 69 | 144 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7060 |
| `unreachable-dns` | 2280 |
| `fetch-error:ConnectTimeout` | 737 |
| `http-403` | 648 |
| `fetch-error:SSLError` | 613 |
| `fetch-error:ConnectionError` | 502 |
| `low-confidence:http-2xx-html` | 390 |
| `empty-body` | 125 |
| `fetch-error:ReadTimeout` | 66 |
| `http-404` | 38 |
| `http-500` | 29 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13211** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2280**
- Moved pointers (old domain → new): **599**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 57/436 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 77/283 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/38 (29%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/91 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
