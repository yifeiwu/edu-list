# Edu-Domains — Run Summary

_Generated 2026-10-22 10:16 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20852** across **205** countries
- Active: **11172** (54%) · Inaccessible: **9680** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9212** domains (median 22 yrs)

## Last runs

- Verify (2026-10-22 10:16 UTC): validated 79, +38 Active, re-verified 15, pending left 0
- Curate (2026-10-22 07:18 UTC): 10695 raw candidates, 62 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4363 | 3290 | 1073 |
| FR | 2569 | 1246 | 1323 |
| CN | 1231 | 137 | 1094 |
| IN | 740 | 385 | 355 |
| AU | 734 | 534 | 200 |
| JP | 713 | 190 | 523 |
| DE | 598 | 334 | 264 |
| BR | 540 | 268 | 272 |
| ID | 497 | 297 | 200 |
| RU | 476 | 176 | 300 |
| PL | 416 | 172 | 244 |
| KR | 331 | 90 | 241 |
| ES | 326 | 204 | 122 |
| GB | 289 | 147 | 142 |
| MX | 280 | 154 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11177 |
| `unreachable-dns` | 3034 |
| `fetch-error:ConnectTimeout` | 1201 |
| `fetch-error:ConnectionError` | 1018 |
| `http-403` | 961 |
| `fetch-error:SSLError` | 931 |
| `low-confidence:http-2xx-html` | 918 |
| `empty-body` | 206 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 109 |
| `http-404` | 81 |
| `http-503` | 43 |

## Freshness

- Verified in last 30 days: **18501** (89%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3034**
- Moved pointers (old domain → new): **886**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 137/1231 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 190/713 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 90/331 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/138 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 21 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
