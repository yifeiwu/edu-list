# Edu-Domains — Run Summary

_Generated 2026-11-20 19:47 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25544** across **207** countries
- Active: **13671** (54%) · Inaccessible: **11873** (46%)
- Pending queue: **30** unvalidated candidates
- Known registration age: **11209** domains (median 21 yrs)

## Last runs

- Verify (2026-11-20 17:22 UTC): validated 43, +15 Active, re-verified 15, pending left 0
- Curate (2026-11-20 19:47 UTC): 10698 raw candidates, 30 queued, 62 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4784 | 3609 | 1175 |
| FR | 3696 | 1785 | 1911 |
| CN | 1387 | 153 | 1234 |
| JP | 979 | 285 | 694 |
| IN | 943 | 534 | 409 |
| AU | 762 | 559 | 203 |
| ID | 690 | 420 | 270 |
| DE | 634 | 359 | 275 |
| RU | 625 | 253 | 372 |
| BR | 606 | 313 | 293 |
| UA | 586 | 253 | 333 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 379 | 213 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13676 |
| `unreachable-dns` | 3509 |
| `fetch-error:ConnectTimeout` | 1570 |
| `fetch-error:ConnectionError` | 1300 |
| `low-confidence:http-2xx-html` | 1289 |
| `fetch-error:SSLError` | 1133 |
| `http-403` | 1103 |
| `empty-body` | 246 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 140 |
| `http-404` | 97 |
| `http-503` | 55 |

## Freshness

- Verified in last 30 days: **7697** (30%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3509**
- Moved pointers (old domain → new): **1054**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1387 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/16 (19%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/979 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 301 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
