# Edu-Domains — Run Summary

_Generated 2026-10-12 00:19 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14986** across **204** countries
- Active: **8072** (54%) · Inaccessible: **6914** (46%)
- Pending queue: **3087** unvalidated candidates
- Known registration age: **6555** domains (median 24 yrs)

## Last runs

- Verify (2026-10-11 23:22 UTC): validated 118, +64 Active, re-verified 15, pending left 3040
- Curate (2026-10-12 00:19 UTC): 10686 raw candidates, 47 queued, 10574 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3182 | 2390 | 792 |
| FR | 1367 | 705 | 662 |
| IN | 609 | 306 | 303 |
| JP | 609 | 137 | 472 |
| AU | 589 | 416 | 173 |
| DE | 584 | 324 | 260 |
| CN | 500 | 63 | 437 |
| BR | 477 | 229 | 248 |
| RU | 405 | 136 | 269 |
| KR | 305 | 83 | 222 |
| GB | 271 | 135 | 136 |
| ID | 260 | 152 | 108 |
| IR | 235 | 73 | 162 |
| CA | 207 | 122 | 85 |
| TR | 203 | 137 | 66 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8074 |
| `unreachable-dns` | 2420 |
| `fetch-error:ConnectTimeout` | 841 |
| `http-403` | 723 |
| `fetch-error:SSLError` | 679 |
| `fetch-error:ConnectionError` | 604 |
| `low-confidence:http-2xx-html` | 487 |
| `empty-body` | 152 |
| `fetch-error:ReadTimeout` | 80 |
| `http-500` | 46 |
| `http-404` | 42 |
| `http-503` | 27 |

## Freshness

- Verified in last 30 days: **14986** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2420**
- Moved pointers (old domain → new): **683**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 63/500 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 137/609 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 12/100 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 4 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
