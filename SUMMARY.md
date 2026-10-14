# Edu-Domains — Run Summary

_Generated 2026-10-14 20:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16218** across **204** countries
- Active: **8781** (54%) · Inaccessible: **7437** (46%)
- Pending queue: **2446** unvalidated candidates
- Known registration age: **6965** domains (median 24 yrs)

## Last runs

- Verify (2026-10-14 20:55 UTC): validated 118, +49 Active, re-verified 15, pending left 2446
- Curate (2026-10-14 20:30 UTC): 10693 raw candidates, 59 queued, 28 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3361 | 2530 | 831 |
| FR | 1637 | 825 | 812 |
| AU | 691 | 502 | 189 |
| JP | 627 | 146 | 481 |
| IN | 624 | 313 | 311 |
| DE | 591 | 328 | 263 |
| CN | 558 | 71 | 487 |
| BR | 484 | 233 | 251 |
| RU | 414 | 141 | 273 |
| KR | 310 | 85 | 225 |
| GB | 272 | 136 | 136 |
| ID | 271 | 160 | 111 |
| IR | 249 | 79 | 170 |
| CA | 218 | 132 | 86 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8783 |
| `unreachable-dns` | 2508 |
| `fetch-error:ConnectTimeout` | 925 |
| `http-403` | 768 |
| `fetch-error:SSLError` | 734 |
| `fetch-error:ConnectionError` | 670 |
| `low-confidence:http-2xx-html` | 574 |
| `empty-body` | 165 |
| `fetch-error:ReadTimeout` | 89 |
| `http-500` | 62 |
| `http-404` | 50 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **16218** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2508**
- Moved pointers (old domain → new): **722**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 71/558 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 146/627 (23%) — check for blocks/stale sources
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
