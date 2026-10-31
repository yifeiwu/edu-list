# Edu-Domains — Run Summary

_Generated 2026-10-31 13:46 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22789** across **205** countries
- Active: **12180** (53%) · Inaccessible: **10609** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10071** domains (median 21 yrs)

## Last runs

- Verify (2026-10-31 13:46 UTC): validated 61, +21 Active, re-verified 15, pending left 0
- Curate (2026-10-31 13:27 UTC): 10695 raw candidates, 43 queued, 52 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4609 | 3483 | 1126 |
| FR | 2991 | 1449 | 1542 |
| CN | 1291 | 147 | 1144 |
| IN | 808 | 435 | 373 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 583 | 226 | 357 |
| BR | 574 | 282 | 292 |
| ID | 549 | 328 | 221 |
| PL | 454 | 178 | 276 |
| UA | 438 | 184 | 254 |
| ES | 407 | 262 | 145 |
| KR | 341 | 96 | 245 |
| GB | 302 | 154 | 148 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12185 |
| `unreachable-dns` | 3235 |
| `fetch-error:ConnectTimeout` | 1374 |
| `fetch-error:ConnectionError` | 1122 |
| `low-confidence:http-2xx-html` | 1065 |
| `fetch-error:SSLError` | 1028 |
| `http-403` | 1016 |
| `empty-body` | 218 |
| `http-500` | 127 |
| `fetch-error:ReadTimeout` | 126 |
| `http-404` | 89 |
| `http-503` | 50 |

## Freshness

- Verified in last 30 days: **15592** (68%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3235**
- Moved pointers (old domain → new): **956**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1291 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/341 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/152 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
