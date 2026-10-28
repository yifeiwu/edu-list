# Edu-Domains — Run Summary

_Generated 2026-10-28 23:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22156** across **205** countries
- Active: **11863** (54%) · Inaccessible: **10293** (46%)
- Pending queue: **58** unvalidated candidates
- Known registration age: **9751** domains (median 22 yrs)

## Last runs

- Verify (2026-10-28 19:59 UTC): validated 60, +17 Active, re-verified 15, pending left 0
- Curate (2026-10-28 23:00 UTC): 10701 raw candidates, 58 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4523 | 3411 | 1112 |
| FR | 2857 | 1385 | 1472 |
| CN | 1273 | 144 | 1129 |
| JP | 796 | 220 | 576 |
| IN | 789 | 421 | 368 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 568 | 281 | 287 |
| ID | 527 | 312 | 215 |
| RU | 523 | 197 | 326 |
| PL | 419 | 174 | 245 |
| ES | 405 | 261 | 144 |
| KR | 336 | 94 | 242 |
| GB | 300 | 153 | 147 |
| MX | 289 | 158 | 131 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11868 |
| `unreachable-dns` | 3166 |
| `fetch-error:ConnectTimeout` | 1317 |
| `fetch-error:ConnectionError` | 1087 |
| `low-confidence:http-2xx-html` | 1022 |
| `http-403` | 996 |
| `fetch-error:SSLError` | 986 |
| `empty-body` | 212 |
| `fetch-error:ReadTimeout` | 121 |
| `http-500` | 120 |
| `http-404` | 87 |
| `http-503` | 48 |

## Freshness

- Verified in last 30 days: **16337** (74%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3166**
- Moved pointers (old domain → new): **931**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 144/1273 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 220/796 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/336 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 21/150 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
