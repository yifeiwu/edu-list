# Edu-Domains — Run Summary

_Generated 2026-10-17 19:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18084** across **204** countries
- Active: **9809** (54%) · Inaccessible: **8275** (46%)
- Pending queue: **1360** unvalidated candidates
- Known registration age: **8015** domains (median 23 yrs)

## Last runs

- Verify (2026-10-17 19:00 UTC): validated 120, +56 Active, re-verified 15, pending left 1360
- Curate (2026-10-17 16:12 UTC): 10700 raw candidates, 55 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3768 | 2836 | 932 |
| FR | 2014 | 1009 | 1005 |
| AU | 729 | 529 | 200 |
| CN | 722 | 99 | 623 |
| IN | 661 | 339 | 322 |
| JP | 640 | 154 | 486 |
| DE | 592 | 329 | 263 |
| BR | 496 | 242 | 254 |
| ID | 436 | 269 | 167 |
| RU | 421 | 145 | 276 |
| PL | 389 | 166 | 223 |
| KR | 316 | 86 | 230 |
| GB | 284 | 144 | 140 |
| IR | 254 | 80 | 174 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9811 |
| `unreachable-dns` | 2656 |
| `fetch-error:ConnectTimeout` | 1021 |
| `http-403` | 848 |
| `fetch-error:SSLError` | 821 |
| `fetch-error:ConnectionError` | 806 |
| `low-confidence:http-2xx-html` | 729 |
| `empty-body` | 179 |
| `fetch-error:ReadTimeout` | 96 |
| `http-500` | 72 |
| `http-404` | 57 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18063** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2656**
- Moved pointers (old domain → new): **805**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 99/722 (14%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 154/640 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 18/118 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 12 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
