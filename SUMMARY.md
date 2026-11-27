# Edu-Domains — Run Summary

_Generated 2026-11-27 23:17 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **26106** across **207** countries
- Active: **13973** (54%) · Inaccessible: **12133** (46%)
- Pending queue: **37** unvalidated candidates
- Known registration age: **11483** domains (median 20 yrs)

## Last runs

- Verify (2026-11-27 22:45 UTC): validated 48, +17 Active, re-verified 15, pending left 0
- Curate (2026-11-27 23:17 UTC): 10691 raw candidates, 37 queued, 59 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4814 | 3626 | 1188 |
| FR | 3880 | 1867 | 2013 |
| CN | 1413 | 157 | 1256 |
| JP | 985 | 286 | 699 |
| IN | 973 | 553 | 420 |
| ID | 776 | 476 | 300 |
| AU | 765 | 563 | 202 |
| DE | 650 | 369 | 281 |
| RU | 638 | 258 | 380 |
| BR | 622 | 322 | 300 |
| UA | 588 | 255 | 333 |
| PL | 494 | 186 | 308 |
| ES | 422 | 270 | 152 |
| GB | 382 | 216 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13978 |
| `unreachable-dns` | 3557 |
| `fetch-error:ConnectTimeout` | 1630 |
| `low-confidence:http-2xx-html` | 1331 |
| `fetch-error:ConnectionError` | 1326 |
| `fetch-error:SSLError` | 1145 |
| `http-403` | 1125 |
| `empty-body` | 248 |
| `http-500` | 154 |
| `fetch-error:ReadTimeout` | 144 |
| `http-404` | 101 |
| `http-503` | 59 |

## Freshness

- Verified in last 30 days: **6023** (23%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3557**
- Moved pointers (old domain → new): **1078**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1413 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/985 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 304 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
