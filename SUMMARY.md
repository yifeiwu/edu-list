# Edu-Domains — Run Summary

_Generated 2026-10-06 00:40 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12168** across **203** countries
- Active: **6399** (53%) · Inaccessible: **5769** (47%)
- Pending queue: **4420** unvalidated candidates
- Known registration age: **5219** domains (median 24 yrs)

## Last runs

- Verify (2026-10-05 18:55 UTC): validated 119, +75 Active, re-verified 15, pending left 4374
- Curate (2026-10-06 00:40 UTC): 10700 raw candidates, 46 queued, 10211 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2636 | 1985 | 651 |
| FR | 628 | 318 | 310 |
| JP | 577 | 125 | 452 |
| IN | 465 | 215 | 250 |
| CN | 424 | 52 | 372 |
| AU | 380 | 261 | 119 |
| DE | 380 | 179 | 201 |
| BR | 352 | 164 | 188 |
| RU | 336 | 108 | 228 |
| KR | 278 | 73 | 205 |
| GB | 238 | 116 | 122 |
| ID | 225 | 131 | 94 |
| IR | 212 | 69 | 143 |
| TR | 193 | 134 | 59 |
| CA | 181 | 100 | 81 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6401 |
| `fetch-error:ConnectionError` | 2650 |
| `fetch-error:ConnectTimeout` | 698 |
| `http-403` | 598 |
| `fetch-error:SSLError` | 568 |
| `low-confidence:http-2xx-html` | 346 |
| `empty-body` | 123 |
| `fetch-error:ReadTimeout` | 61 |
| `http-404` | 36 |
| `http-500` | 23 |
| `parking-linkfarm` | 21 |
| `parking` | 14 |

## Freshness

- Verified in last 30 days: **12168** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **548**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 52/424 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 125/577 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 73/278 (26%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 9/85 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
