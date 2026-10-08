# Edu-Domains — Run Summary

_Generated 2026-10-08 19:35 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13419** across **203** countries
- Active: **7165** (53%) · Inaccessible: **6254** (47%)
- Pending queue: **3746** unvalidated candidates
- Known registration age: **5951** domains (median 24 yrs)

## Last runs

- Verify (2026-10-08 19:35 UTC): validated 119, +54 Active, re-verified 15, pending left 3746
- Curate (2026-10-08 15:22 UTC): 10681 raw candidates, 58 queued, 33 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2914 | 2200 | 714 |
| FR | 1009 | 530 | 479 |
| JP | 594 | 129 | 465 |
| IN | 547 | 278 | 269 |
| BR | 468 | 221 | 247 |
| CN | 441 | 59 | 382 |
| AU | 428 | 295 | 133 |
| DE | 396 | 193 | 203 |
| RU | 376 | 121 | 255 |
| KR | 284 | 78 | 206 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 214 | 69 | 145 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7167 |
| `unreachable-dns` | 2305 |
| `fetch-error:ConnectTimeout` | 752 |
| `http-403` | 654 |
| `fetch-error:SSLError` | 624 |
| `fetch-error:ConnectionError` | 521 |
| `low-confidence:http-2xx-html` | 398 |
| `empty-body` | 126 |
| `fetch-error:ReadTimeout` | 67 |
| `http-404` | 38 |
| `http-500` | 32 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13419** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2305**
- Moved pointers (old domain → new): **607**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 59/441 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 78/284 (27%) — check for blocks/stale sources
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
