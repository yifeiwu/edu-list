# Edu-Domains — Run Summary

_Generated 2026-11-16 19:59 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25115** across **206** countries
- Active: **13446** (54%) · Inaccessible: **11669** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11039** domains (median 21 yrs)

## Last runs

- Verify (2026-11-16 19:59 UTC): validated 60, +0 Active, re-verified 60, pending left 0
- Curate (2026-11-16 09:10 UTC): 10692 raw candidates, 41 queued, 48 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4779 | 3605 | 1174 |
| FR | 3586 | 1734 | 1852 |
| CN | 1374 | 153 | 1221 |
| IN | 925 | 522 | 403 |
| JP | 910 | 256 | 654 |
| AU | 762 | 559 | 203 |
| DE | 623 | 349 | 274 |
| RU | 622 | 251 | 371 |
| ID | 615 | 374 | 241 |
| BR | 602 | 311 | 291 |
| UA | 584 | 252 | 332 |
| PL | 482 | 184 | 298 |
| ES | 421 | 270 | 151 |
| GB | 376 | 211 | 165 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13451 |
| `unreachable-dns` | 3448 |
| `fetch-error:ConnectTimeout` | 1540 |
| `fetch-error:ConnectionError` | 1278 |
| `low-confidence:http-2xx-html` | 1257 |
| `fetch-error:SSLError` | 1122 |
| `http-403` | 1083 |
| `empty-body` | 238 |
| `http-500` | 148 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **10061** (40%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3448**
- Moved pointers (old domain → new): **1047**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1374 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 256/910 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/160 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 286 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
