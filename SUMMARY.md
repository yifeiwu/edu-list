# Edu-Domains — Run Summary

_Generated 2026-11-03 07:45 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23240** across **205** countries
- Active: **12455** (54%) · Inaccessible: **10785** (46%)
- Pending queue: **36** unvalidated candidates
- Known registration age: **10303** domains (median 21 yrs)

## Last runs

- Verify (2026-11-03 02:42 UTC): validated 42, +15 Active, re-verified 15, pending left 0
- Curate (2026-11-03 07:45 UTC): 10701 raw candidates, 36 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4685 | 3542 | 1143 |
| FR | 3082 | 1492 | 1590 |
| CN | 1301 | 148 | 1153 |
| IN | 830 | 451 | 379 |
| JP | 807 | 225 | 582 |
| AU | 736 | 537 | 199 |
| DE | 607 | 340 | 267 |
| RU | 592 | 232 | 360 |
| BR | 579 | 286 | 293 |
| ID | 569 | 343 | 226 |
| UA | 469 | 194 | 275 |
| PL | 458 | 179 | 279 |
| ES | 412 | 265 | 147 |
| GB | 350 | 190 | 160 |
| KR | 347 | 96 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12460 |
| `unreachable-dns` | 3260 |
| `fetch-error:ConnectTimeout` | 1396 |
| `fetch-error:ConnectionError` | 1150 |
| `low-confidence:http-2xx-html` | 1097 |
| `fetch-error:SSLError` | 1052 |
| `http-403` | 1032 |
| `empty-body` | 224 |
| `fetch-error:ReadTimeout` | 130 |
| `http-500` | 129 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **14470** (62%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3260**
- Moved pointers (old domain → new): **968**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 148/1301 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/807 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/347 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/155 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 53 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
