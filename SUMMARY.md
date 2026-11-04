# Edu-Domains — Run Summary

_Generated 2026-11-04 08:59 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23380** across **205** countries
- Active: **12529** (54%) · Inaccessible: **10851** (46%)
- Pending queue: **26** unvalidated candidates
- Known registration age: **10352** domains (median 21 yrs)

## Last runs

- Verify (2026-11-04 03:20 UTC): validated 32, +8 Active, re-verified 15, pending left 0
- Curate (2026-11-04 08:59 UTC): 10680 raw candidates, 26 queued, 53 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4692 | 3549 | 1143 |
| FR | 3132 | 1511 | 1621 |
| CN | 1305 | 148 | 1157 |
| IN | 842 | 458 | 384 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 608 | 341 | 267 |
| RU | 596 | 235 | 361 |
| BR | 580 | 287 | 293 |
| ID | 569 | 343 | 226 |
| UA | 478 | 198 | 280 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 348 | 97 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12534 |
| `unreachable-dns` | 3269 |
| `fetch-error:ConnectTimeout` | 1405 |
| `fetch-error:ConnectionError` | 1170 |
| `low-confidence:http-2xx-html` | 1105 |
| `fetch-error:SSLError` | 1058 |
| `http-403` | 1037 |
| `empty-body` | 226 |
| `http-500` | 133 |
| `fetch-error:ReadTimeout` | 129 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13969** (60%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3269**
- Moved pointers (old domain → new): **970**

## Alerts

- ⚠ `CN`: low Active rate 148/1305 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 97/348 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/156 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 59 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
