# Edu-Domains — Run Summary

_Generated 2026-10-10 13:23 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14151** across **204** countries
- Active: **7586** (54%) · Inaccessible: **6565** (46%)
- Pending queue: **3491** unvalidated candidates
- Known registration age: **6261** domains (median 24 yrs)

## Last runs

- Verify (2026-10-10 09:58 UTC): validated 118, +58 Active, re-verified 15, pending left 3440
- Curate (2026-10-10 13:23 UTC): 10700 raw candidates, 51 queued, 30 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3061 | 2304 | 757 |
| FR | 1179 | 626 | 553 |
| JP | 596 | 131 | 465 |
| IN | 566 | 289 | 277 |
| DE | 504 | 276 | 228 |
| CN | 478 | 61 | 417 |
| BR | 473 | 225 | 248 |
| AU | 435 | 299 | 136 |
| RU | 396 | 128 | 268 |
| KR | 301 | 80 | 221 |
| GB | 264 | 130 | 134 |
| ID | 245 | 143 | 102 |
| IR | 218 | 69 | 149 |
| TR | 201 | 137 | 64 |
| CA | 195 | 112 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7588 |
| `unreachable-dns` | 2366 |
| `fetch-error:ConnectTimeout` | 795 |
| `http-403` | 678 |
| `fetch-error:SSLError` | 649 |
| `fetch-error:ConnectionError` | 556 |
| `low-confidence:http-2xx-html` | 445 |
| `empty-body` | 134 |
| `fetch-error:ReadTimeout` | 76 |
| `http-404` | 41 |
| `http-500` | 36 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **14151** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2366**
- Moved pointers (old domain → new): **645**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 61/478 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 131/596 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 80/301 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/39 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/95 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 1 unmapped country — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
