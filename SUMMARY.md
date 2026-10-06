# Edu-Domains — Run Summary

_Generated 2026-10-06 23:54 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12683** across **203** countries
- Active: **6767** (53%) · Inaccessible: **5916** (47%)
- Pending queue: **4063** unvalidated candidates
- Known registration age: **5531** domains (median 24 yrs)

## Last runs

- Verify (2026-10-06 23:54 UTC): validated 115, +70 Active, re-verified 15, pending left 4063
- Curate (2026-10-06 20:04 UTC): 10701 raw candidates, 44 queued, 51 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2763 | 2091 | 672 |
| FR | 705 | 365 | 340 |
| JP | 593 | 129 | 464 |
| IN | 542 | 278 | 264 |
| CN | 430 | 55 | 375 |
| AU | 402 | 278 | 124 |
| DE | 392 | 189 | 203 |
| BR | 374 | 175 | 199 |
| RU | 336 | 108 | 228 |
| KR | 280 | 75 | 205 |
| GB | 256 | 126 | 130 |
| ID | 232 | 134 | 98 |
| IR | 212 | 69 | 143 |
| TR | 200 | 137 | 63 |
| CA | 191 | 108 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6769 |
| `fetch-error:ConnectionError` | 2706 |
| `fetch-error:ConnectTimeout` | 713 |
| `http-403` | 623 |
| `fetch-error:SSLError` | 585 |
| `low-confidence:http-2xx-html` | 353 |
| `empty-body` | 122 |
| `fetch-error:ReadTimeout` | 62 |
| `http-404` | 36 |
| `http-500` | 24 |
| `parking-linkfarm` | 22 |
| `http-503` | 14 |

## Freshness

- Verified in last 30 days: **12683** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **570**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 55/430 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 129/593 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 75/280 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/37 (30%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/89 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
