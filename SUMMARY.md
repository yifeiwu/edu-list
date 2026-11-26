# Edu-Domains — Run Summary

_Generated 2026-11-26 12:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25978** across **207** countries
- Active: **13908** (54%) · Inaccessible: **12070** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11426** domains (median 20 yrs)

## Last runs

- Verify (2026-11-26 12:31 UTC): validated 41, +16 Active, re-verified 15, pending left 0
- Curate (2026-11-26 04:01 UTC): 10706 raw candidates, 24 queued, 10614 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4809 | 3621 | 1188 |
| FR | 3848 | 1856 | 1992 |
| CN | 1400 | 155 | 1245 |
| JP | 983 | 286 | 697 |
| IN | 967 | 549 | 418 |
| AU | 764 | 562 | 202 |
| ID | 762 | 467 | 295 |
| DE | 649 | 366 | 283 |
| RU | 634 | 256 | 378 |
| BR | 618 | 320 | 298 |
| UA | 587 | 254 | 333 |
| PL | 493 | 186 | 307 |
| ES | 422 | 270 | 152 |
| GB | 381 | 215 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13913 |
| `unreachable-dns` | 3540 |
| `fetch-error:ConnectTimeout` | 1617 |
| `low-confidence:http-2xx-html` | 1322 |
| `fetch-error:ConnectionError` | 1319 |
| `fetch-error:SSLError` | 1142 |
| `http-403` | 1119 |
| `empty-body` | 248 |
| `http-500` | 153 |
| `fetch-error:ReadTimeout` | 144 |
| `http-404` | 101 |
| `http-503` | 58 |

## Freshness

- Verified in last 30 days: **6157** (24%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3540**
- Moved pointers (old domain → new): **1074**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1400 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/983 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 298 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
