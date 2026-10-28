# Edu-Domains — Run Summary

_Generated 2026-10-28 04:43 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22033** across **205** countries
- Active: **11812** (54%) · Inaccessible: **10221** (46%)
- Pending queue: **44** unvalidated candidates
- Known registration age: **9696** domains (median 22 yrs)

## Last runs

- Verify (2026-10-28 01:49 UTC): validated 60, +22 Active, re-verified 15, pending left 0
- Curate (2026-10-28 04:43 UTC): 10684 raw candidates, 44 queued, 10598 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4516 | 3406 | 1110 |
| FR | 2835 | 1377 | 1458 |
| CN | 1264 | 143 | 1121 |
| JP | 789 | 215 | 574 |
| IN | 787 | 419 | 368 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 568 | 281 | 287 |
| ID | 522 | 310 | 212 |
| RU | 522 | 196 | 326 |
| PL | 418 | 174 | 244 |
| ES | 405 | 261 | 144 |
| KR | 335 | 94 | 241 |
| GB | 297 | 151 | 146 |
| MX | 288 | 158 | 130 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11817 |
| `unreachable-dns` | 3149 |
| `fetch-error:ConnectTimeout` | 1306 |
| `fetch-error:ConnectionError` | 1079 |
| `low-confidence:http-2xx-html` | 1012 |
| `http-403` | 990 |
| `fetch-error:SSLError` | 980 |
| `empty-body` | 210 |
| `fetch-error:ReadTimeout` | 119 |
| `http-500` | 119 |
| `http-404` | 86 |
| `http-503` | 46 |

## Freshness

- Verified in last 30 days: **16169** (73%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3149**
- Moved pointers (old domain → new): **926**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 143/1264 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 215/789 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/335 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 21/148 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
