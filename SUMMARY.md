# Edu-Domains — Run Summary

_Generated 2026-10-08 00:48 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13107** across **203** countries
- Active: **6998** (53%) · Inaccessible: **6109** (47%)
- Pending queue: **3930** unvalidated candidates
- Known registration age: **5776** domains (median 24 yrs)

## Last runs

- Verify (2026-10-08 00:01 UTC): validated 121, +50 Active, re-verified 15, pending left 3870
- Curate (2026-10-08 00:48 UTC): 10701 raw candidates, 60 queued, 10576 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2856 | 2154 | 702 |
| FR | 887 | 467 | 420 |
| JP | 594 | 129 | 465 |
| IN | 545 | 278 | 267 |
| CN | 434 | 56 | 378 |
| AU | 428 | 295 | 133 |
| BR | 423 | 194 | 229 |
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
| `http-2xx-html` | 7000 |
| `unreachable-dns` | 2271 |
| `fetch-error:ConnectTimeout` | 734 |
| `http-403` | 644 |
| `fetch-error:SSLError` | 606 |
| `fetch-error:ConnectionError` | 496 |
| `low-confidence:http-2xx-html` | 384 |
| `empty-body` | 124 |
| `fetch-error:ReadTimeout` | 64 |
| `http-404` | 38 |
| `http-500` | 27 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13107** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2271**
- Moved pointers (old domain → new): **595**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 56/434 (13%) — check for blocks/stale sources
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
