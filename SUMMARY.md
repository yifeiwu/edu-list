# Edu-Domains — Run Summary

_Generated 2026-10-08 13:41 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13315** across **203** countries
- Active: **7111** (53%) · Inaccessible: **6204** (47%)
- Pending queue: **3788** unvalidated candidates
- Known registration age: **5896** domains (median 24 yrs)

## Last runs

- Verify (2026-10-08 13:41 UTC): validated 119, +54 Active, re-verified 15, pending left 3788
- Curate (2026-10-08 07:06 UTC): 10695 raw candidates, 60 queued, 31 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2882 | 2177 | 705 |
| FR | 983 | 516 | 467 |
| JP | 594 | 129 | 465 |
| IN | 546 | 278 | 268 |
| BR | 463 | 218 | 245 |
| CN | 438 | 58 | 380 |
| AU | 428 | 295 | 133 |
| DE | 395 | 192 | 203 |
| RU | 374 | 120 | 254 |
| KR | 283 | 77 | 206 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 214 | 69 | 145 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7113 |
| `unreachable-dns` | 2285 |
| `fetch-error:ConnectTimeout` | 748 |
| `http-403` | 650 |
| `fetch-error:SSLError` | 621 |
| `fetch-error:ConnectionError` | 516 |
| `low-confidence:http-2xx-html` | 392 |
| `empty-body` | 125 |
| `fetch-error:ReadTimeout` | 67 |
| `http-404` | 38 |
| `http-500` | 31 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **13315** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2285**
- Moved pointers (old domain → new): **603**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 58/438 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
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
