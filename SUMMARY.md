# Edu-Domains — Run Summary

_Generated 2026-10-09 00:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13526** across **203** countries
- Active: **7226** (53%) · Inaccessible: **6300** (47%)
- Pending queue: **3691** unvalidated candidates
- Known registration age: **5985** domains (median 24 yrs)

## Last runs

- Verify (2026-10-09 00:11 UTC): validated 122, +60 Active, re-verified 15, pending left 3691
- Curate (2026-10-08 21:09 UTC): 10699 raw candidates, 45 queued, 33 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2937 | 2216 | 721 |
| FR | 1029 | 540 | 489 |
| JP | 594 | 129 | 465 |
| IN | 550 | 280 | 270 |
| BR | 469 | 222 | 247 |
| CN | 442 | 59 | 383 |
| AU | 429 | 296 | 133 |
| DE | 396 | 193 | 203 |
| RU | 392 | 125 | 267 |
| KR | 286 | 78 | 208 |
| GB | 258 | 128 | 130 |
| ID | 232 | 134 | 98 |
| IR | 214 | 69 | 145 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7228 |
| `unreachable-dns` | 2313 |
| `fetch-error:ConnectTimeout` | 760 |
| `http-403` | 659 |
| `fetch-error:SSLError` | 626 |
| `fetch-error:ConnectionError` | 522 |
| `low-confidence:http-2xx-html` | 404 |
| `empty-body` | 126 |
| `fetch-error:ReadTimeout` | 70 |
| `http-404` | 38 |
| `http-500` | 32 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13526** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2313**
- Moved pointers (old domain → new): **615**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 59/442 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
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
