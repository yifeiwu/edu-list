# Edu-Domains — Run Summary

_Generated 2026-11-05 00:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23447** across **205** countries
- Active: **12565** (54%) · Inaccessible: **10882** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10379** domains (median 21 yrs)

## Last runs

- Verify (2026-11-05 00:29 UTC): validated 39, +17 Active, re-verified 15, pending left 0
- Curate (2026-11-04 23:24 UTC): 10682 raw candidates, 24 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4697 | 3552 | 1145 |
| FR | 3161 | 1528 | 1633 |
| CN | 1312 | 149 | 1163 |
| IN | 847 | 462 | 385 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 608 | 341 | 267 |
| RU | 596 | 234 | 362 |
| BR | 580 | 288 | 292 |
| ID | 570 | 343 | 227 |
| UA | 487 | 202 | 285 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 349 | 98 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12570 |
| `unreachable-dns` | 3276 |
| `fetch-error:ConnectTimeout` | 1411 |
| `fetch-error:ConnectionError` | 1172 |
| `low-confidence:http-2xx-html` | 1111 |
| `fetch-error:SSLError` | 1060 |
| `http-403` | 1040 |
| `empty-body` | 226 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 130 |
| `http-404` | 91 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13724** (59%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3276**
- Moved pointers (old domain → new): **971**

## Alerts

- ⚠ `CN`: low Active rate 149/1312 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/349 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/156 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 61 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
