# Edu-Domains — Run Summary

_Generated 2026-10-14 17:23 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16115** across **204** countries
- Active: **8732** (54%) · Inaccessible: **7383** (46%)
- Pending queue: **2487** unvalidated candidates
- Known registration age: **6919** domains (median 24 yrs)

## Last runs

- Verify (2026-10-14 17:23 UTC): validated 116, +60 Active, re-verified 15, pending left 2487
- Curate (2026-10-14 16:47 UTC): 10692 raw candidates, 44 queued, 27 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3345 | 2519 | 826 |
| FR | 1610 | 813 | 797 |
| AU | 690 | 501 | 189 |
| JP | 625 | 146 | 479 |
| IN | 623 | 313 | 310 |
| DE | 591 | 328 | 263 |
| CN | 543 | 70 | 473 |
| BR | 483 | 233 | 250 |
| RU | 412 | 140 | 272 |
| KR | 310 | 85 | 225 |
| GB | 272 | 136 | 136 |
| ID | 271 | 160 | 111 |
| IR | 247 | 78 | 169 |
| CA | 218 | 132 | 86 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8734 |
| `unreachable-dns` | 2498 |
| `fetch-error:ConnectTimeout` | 918 |
| `http-403` | 765 |
| `fetch-error:SSLError` | 726 |
| `fetch-error:ConnectionError` | 662 |
| `low-confidence:http-2xx-html` | 567 |
| `empty-body` | 164 |
| `fetch-error:ReadTimeout` | 87 |
| `http-500` | 60 |
| `http-404` | 49 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **16115** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2498**
- Moved pointers (old domain → new): **718**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 70/543 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 146/625 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/310 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 13/102 (13%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
