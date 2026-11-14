# Edu-Domains — Run Summary

_Generated 2026-11-14 06:27 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24692** across **206** countries
- Active: **13264** (54%) · Inaccessible: **11428** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10898** domains (median 21 yrs)

## Last runs

- Verify (2026-11-14 06:27 UTC): validated 70, +21 Active, re-verified 15, pending left 0
- Curate (2026-11-14 02:02 UTC): 10703 raw candidates, 54 queued, 10594 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4767 | 3600 | 1167 |
| FR | 3500 | 1686 | 1814 |
| CN | 1359 | 157 | 1202 |
| IN | 908 | 511 | 397 |
| JP | 837 | 233 | 604 |
| AU | 759 | 557 | 202 |
| DE | 621 | 348 | 273 |
| RU | 616 | 248 | 368 |
| ID | 606 | 368 | 238 |
| BR | 598 | 308 | 290 |
| UA | 578 | 248 | 330 |
| PL | 471 | 183 | 288 |
| ES | 420 | 269 | 151 |
| GB | 373 | 208 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13269 |
| `unreachable-dns` | 3376 |
| `fetch-error:ConnectTimeout` | 1507 |
| `fetch-error:ConnectionError` | 1250 |
| `low-confidence:http-2xx-html` | 1213 |
| `fetch-error:SSLError` | 1099 |
| `http-403` | 1069 |
| `empty-body` | 235 |
| `http-500` | 144 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 94 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10832** (44%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3376**
- Moved pointers (old domain → new): **1030**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1359 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 233/837 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 212 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
