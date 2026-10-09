# Edu-Domains — Run Summary

_Generated 2026-10-09 08:38 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13628** across **203** countries
- Active: **7282** (53%) · Inaccessible: **6346** (47%)
- Pending queue: **3699** unvalidated candidates
- Known registration age: **6013** domains (median 24 yrs)

## Last runs

- Verify (2026-10-09 06:16 UTC): validated 117, +56 Active, re-verified 15, pending left 3640
- Curate (2026-10-09 08:38 UTC): 10701 raw candidates, 59 queued, 27 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2947 | 2222 | 725 |
| FR | 1058 | 561 | 497 |
| JP | 594 | 129 | 465 |
| IN | 550 | 280 | 270 |
| BR | 469 | 222 | 247 |
| CN | 460 | 60 | 400 |
| AU | 429 | 296 | 133 |
| DE | 415 | 208 | 207 |
| RU | 393 | 126 | 267 |
| KR | 286 | 78 | 208 |
| GB | 258 | 128 | 130 |
| ID | 240 | 140 | 100 |
| IR | 216 | 69 | 147 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7284 |
| `unreachable-dns` | 2328 |
| `fetch-error:ConnectTimeout` | 762 |
| `http-403` | 663 |
| `fetch-error:SSLError` | 631 |
| `fetch-error:ConnectionError` | 528 |
| `low-confidence:http-2xx-html` | 407 |
| `empty-body` | 127 |
| `fetch-error:ReadTimeout` | 74 |
| `http-404` | 38 |
| `http-500` | 32 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13628** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2328**
- Moved pointers (old domain → new): **619**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 60/460 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 78/286 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/39 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/91 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
