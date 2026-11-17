# Edu-Domains — Run Summary

_Generated 2026-11-17 03:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25154** across **206** countries
- Active: **13468** (54%) · Inaccessible: **11686** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11049** domains (median 21 yrs)

## Last runs

- Verify (2026-11-17 03:00 UTC): validated 54, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-16 20:05 UTC): 10690 raw candidates, 39 queued, 46 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4779 | 3605 | 1174 |
| FR | 3598 | 1741 | 1857 |
| CN | 1374 | 153 | 1221 |
| IN | 927 | 522 | 405 |
| JP | 921 | 262 | 659 |
| AU | 762 | 559 | 203 |
| DE | 623 | 349 | 274 |
| RU | 622 | 251 | 371 |
| ID | 615 | 374 | 241 |
| BR | 602 | 311 | 291 |
| UA | 584 | 252 | 332 |
| PL | 482 | 184 | 298 |
| ES | 421 | 270 | 151 |
| GB | 377 | 212 | 165 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13473 |
| `unreachable-dns` | 3452 |
| `fetch-error:ConnectTimeout` | 1543 |
| `fetch-error:ConnectionError` | 1281 |
| `low-confidence:http-2xx-html` | 1260 |
| `fetch-error:SSLError` | 1124 |
| `http-403` | 1084 |
| `empty-body` | 238 |
| `http-500` | 148 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **9249** (37%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3452**
- Moved pointers (old domain → new): **1047**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1374 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 262/921 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/161 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 288 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
