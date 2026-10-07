# Edu-Domains — Run Summary

_Generated 2026-10-07 20:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **13001** across **203** countries
- Active: **6948** (53%) · Inaccessible: **6053** (47%)
- Pending queue: **3971** unvalidated candidates
- Known registration age: **5710** domains (median 24 yrs)

## Last runs

- Verify (2026-10-07 19:39 UTC): validated 120, +65 Active, re-verified 15, pending left 3912
- Curate (2026-10-07 20:29 UTC): 10698 raw candidates, 59 queued, 28 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2830 | 2142 | 688 |
| FR | 837 | 440 | 397 |
| JP | 594 | 129 | 465 |
| IN | 545 | 278 | 267 |
| CN | 433 | 56 | 377 |
| AU | 428 | 295 | 133 |
| BR | 404 | 186 | 218 |
| DE | 393 | 190 | 203 |
| RU | 365 | 118 | 247 |
| KR | 282 | 76 | 206 |
| GB | 257 | 127 | 130 |
| ID | 232 | 134 | 98 |
| IR | 213 | 69 | 144 |
| TR | 200 | 137 | 63 |
| CA | 192 | 109 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6950 |
| `fetch-error:ConnectionError` | 2746 |
| `fetch-error:ConnectTimeout` | 729 |
| `http-403` | 638 |
| `fetch-error:SSLError` | 602 |
| `low-confidence:http-2xx-html` | 376 |
| `empty-body` | 124 |
| `fetch-error:ReadTimeout` | 64 |
| `http-404` | 37 |
| `http-500` | 24 |
| `parking-linkfarm` | 22 |
| `http-503` | 15 |

## Freshness

- Verified in last 30 days: **13001** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **589**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 56/433 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/594 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 76/282 (27%) — check for blocks/stale sources
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
