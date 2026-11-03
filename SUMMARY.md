# Edu-Domains — Run Summary

_Generated 2026-11-03 15:58 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23277** across **205** countries
- Active: **12476** (54%) · Inaccessible: **10801** (46%)
- Pending queue: **48** unvalidated candidates
- Known registration age: **10317** domains (median 21 yrs)

## Last runs

- Verify (2026-11-03 10:10 UTC): validated 52, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-03 15:58 UTC): 10699 raw candidates, 48 queued, 48 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4688 | 3545 | 1143 |
| FR | 3097 | 1500 | 1597 |
| CN | 1302 | 148 | 1154 |
| IN | 832 | 451 | 381 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 607 | 340 | 267 |
| RU | 594 | 233 | 361 |
| BR | 580 | 287 | 293 |
| ID | 569 | 343 | 226 |
| UA | 469 | 194 | 275 |
| PL | 458 | 179 | 279 |
| ES | 412 | 265 | 147 |
| GB | 355 | 193 | 162 |
| KR | 347 | 96 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12481 |
| `unreachable-dns` | 3262 |
| `fetch-error:ConnectTimeout` | 1398 |
| `fetch-error:ConnectionError` | 1154 |
| `low-confidence:http-2xx-html` | 1098 |
| `fetch-error:SSLError` | 1055 |
| `http-403` | 1033 |
| `empty-body` | 224 |
| `fetch-error:ReadTimeout` | 130 |
| `http-500` | 129 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **14522** (62%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3262**
- Moved pointers (old domain → new): **970**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 148/1302 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/347 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/155 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 55 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
