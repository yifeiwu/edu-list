# Edu-Domains — Run Summary

_Generated 2026-10-27 18:51 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21934** across **205** countries
- Active: **11752** (54%) · Inaccessible: **10182** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9657** domains (median 22 yrs)

## Last runs

- Verify (2026-10-27 18:51 UTC): validated 70, +25 Active, re-verified 15, pending left 0
- Curate (2026-10-27 14:11 UTC): 10699 raw candidates, 54 queued, 47 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4506 | 3395 | 1111 |
| FR | 2816 | 1369 | 1447 |
| CN | 1264 | 143 | 1121 |
| JP | 784 | 213 | 571 |
| IN | 783 | 415 | 368 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 566 | 280 | 286 |
| ID | 521 | 309 | 212 |
| RU | 521 | 195 | 326 |
| PL | 417 | 173 | 244 |
| ES | 405 | 261 | 144 |
| KR | 335 | 94 | 241 |
| GB | 297 | 151 | 146 |
| MX | 286 | 157 | 129 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11757 |
| `unreachable-dns` | 3143 |
| `fetch-error:ConnectTimeout` | 1301 |
| `fetch-error:ConnectionError` | 1072 |
| `low-confidence:http-2xx-html` | 1008 |
| `http-403` | 987 |
| `fetch-error:SSLError` | 972 |
| `empty-body` | 210 |
| `fetch-error:ReadTimeout` | 119 |
| `http-500` | 118 |
| `http-404` | 86 |
| `http-503` | 46 |

## Freshness

- Verified in last 30 days: **16744** (76%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3143**
- Moved pointers (old domain → new): **924**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 143/1264 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 213/784 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/335 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/147 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 32 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
