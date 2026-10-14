# Edu-Domains — Run Summary

_Generated 2026-10-14 12:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16014** across **204** countries
- Active: **8672** (54%) · Inaccessible: **7342** (46%)
- Pending queue: **2543** unvalidated candidates
- Known registration age: **6892** domains (median 24 yrs)

## Last runs

- Verify (2026-10-14 12:00 UTC): validated 119, +36 Active, re-verified 15, pending left 2543
- Curate (2026-10-14 11:41 UTC): 10695 raw candidates, 49 queued, 33 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3334 | 2509 | 825 |
| FR | 1584 | 796 | 788 |
| AU | 689 | 500 | 189 |
| JP | 625 | 146 | 479 |
| IN | 623 | 313 | 310 |
| DE | 590 | 328 | 262 |
| CN | 542 | 70 | 472 |
| BR | 483 | 233 | 250 |
| RU | 412 | 140 | 272 |
| KR | 310 | 85 | 225 |
| GB | 272 | 136 | 136 |
| ID | 271 | 160 | 111 |
| IR | 245 | 77 | 168 |
| CA | 218 | 132 | 86 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8674 |
| `unreachable-dns` | 2493 |
| `fetch-error:ConnectTimeout` | 912 |
| `http-403` | 763 |
| `fetch-error:SSLError` | 717 |
| `fetch-error:ConnectionError` | 653 |
| `low-confidence:http-2xx-html` | 562 |
| `empty-body` | 163 |
| `fetch-error:ReadTimeout` | 87 |
| `http-500` | 57 |
| `http-404` | 49 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **16014** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2493**
- Moved pointers (old domain → new): **717**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 70/542 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 146/625 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/310 (27%) — check for blocks/stale sources
- ⚠ `KZ`: low Active rate 21/75 (28%) — check for blocks/stale sources
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
