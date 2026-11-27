# Edu-Domains — Run Summary

_Generated 2026-11-27 14:48 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **26073** across **207** countries
- Active: **13956** (54%) · Inaccessible: **12117** (46%)
- Pending queue: **33** unvalidated candidates
- Known registration age: **11469** domains (median 20 yrs)

## Last runs

- Verify (2026-11-27 14:02 UTC): validated 49, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-27 14:48 UTC): 10706 raw candidates, 33 queued, 65 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4814 | 3626 | 1188 |
| FR | 3872 | 1863 | 2009 |
| CN | 1408 | 157 | 1251 |
| JP | 983 | 286 | 697 |
| IN | 970 | 550 | 420 |
| ID | 772 | 474 | 298 |
| AU | 765 | 563 | 202 |
| DE | 650 | 368 | 282 |
| RU | 638 | 258 | 380 |
| BR | 621 | 321 | 300 |
| UA | 588 | 255 | 333 |
| PL | 494 | 186 | 308 |
| ES | 422 | 270 | 152 |
| GB | 382 | 216 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13961 |
| `unreachable-dns` | 3552 |
| `fetch-error:ConnectTimeout` | 1629 |
| `low-confidence:http-2xx-html` | 1330 |
| `fetch-error:ConnectionError` | 1325 |
| `fetch-error:SSLError` | 1143 |
| `http-403` | 1121 |
| `empty-body` | 248 |
| `http-500` | 153 |
| `fetch-error:ReadTimeout` | 144 |
| `http-404` | 101 |
| `http-503` | 59 |

## Freshness

- Verified in last 30 days: **5975** (23%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3552**
- Moved pointers (old domain → new): **1077**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1408 (11%) — check for blocks/stale sources
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
- ⚠ `XX`: 301 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
