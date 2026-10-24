# Edu-Domains — Run Summary

_Generated 2026-10-24 21:40 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21497** across **205** countries
- Active: **11532** (54%) · Inaccessible: **9965** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9489** domains (median 22 yrs)

## Last runs

- Verify (2026-10-24 21:40 UTC): validated 40, +12 Active, re-verified 15, pending left 0
- Curate (2026-10-24 20:35 UTC): 10691 raw candidates, 24 queued, 64 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4488 | 3379 | 1109 |
| FR | 2723 | 1324 | 1399 |
| CN | 1249 | 140 | 1109 |
| IN | 757 | 396 | 361 |
| JP | 749 | 203 | 546 |
| AU | 736 | 536 | 200 |
| DE | 599 | 335 | 264 |
| BR | 558 | 277 | 281 |
| RU | 516 | 192 | 324 |
| ID | 503 | 298 | 205 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 333 | 92 | 241 |
| GB | 292 | 148 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11537 |
| `unreachable-dns` | 3089 |
| `fetch-error:ConnectTimeout` | 1264 |
| `fetch-error:ConnectionError` | 1050 |
| `http-403` | 980 |
| `low-confidence:http-2xx-html` | 973 |
| `fetch-error:SSLError` | 949 |
| `empty-body` | 209 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18071** (84%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3089**
- Moved pointers (old domain → new): **908**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 140/1249 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 203/749 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 92/333 (28%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/142 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 24 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
