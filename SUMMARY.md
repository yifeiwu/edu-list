# Edu-Domains — Run Summary

_Generated 2026-11-14 02:02 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24637** across **206** countries
- Active: **13243** (54%) · Inaccessible: **11394** (46%)
- Pending queue: **54** unvalidated candidates
- Known registration age: **10878** domains (median 21 yrs)

## Last runs

- Verify (2026-11-13 23:57 UTC): validated 72, +29 Active, re-verified 15, pending left 0
- Curate (2026-11-14 02:02 UTC): 10703 raw candidates, 54 queued, 10594 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4764 | 3598 | 1166 |
| FR | 3494 | 1686 | 1808 |
| CN | 1357 | 157 | 1200 |
| IN | 905 | 508 | 397 |
| JP | 837 | 233 | 604 |
| AU | 757 | 555 | 202 |
| DE | 621 | 348 | 273 |
| RU | 616 | 248 | 368 |
| ID | 606 | 368 | 238 |
| BR | 598 | 308 | 290 |
| UA | 578 | 248 | 330 |
| PL | 470 | 182 | 288 |
| ES | 419 | 269 | 150 |
| GB | 372 | 207 | 165 |
| KR | 351 | 99 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13248 |
| `unreachable-dns` | 3369 |
| `fetch-error:ConnectTimeout` | 1502 |
| `fetch-error:ConnectionError` | 1244 |
| `low-confidence:http-2xx-html` | 1205 |
| `fetch-error:SSLError` | 1096 |
| `http-403` | 1068 |
| `empty-body` | 235 |
| `http-500` | 143 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 93 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10762** (44%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3369**
- Moved pointers (old domain → new): **1029**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 157/1357 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 233/837 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 99/351 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/158 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 202 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
