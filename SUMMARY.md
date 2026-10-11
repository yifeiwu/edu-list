# Edu-Domains — Run Summary

_Generated 2026-10-11 09:03 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14675** across **204** countries
- Active: **7867** (54%) · Inaccessible: **6808** (46%)
- Pending queue: **3207** unvalidated candidates
- Known registration age: **6429** domains (median 24 yrs)

## Last runs

- Verify (2026-10-11 09:03 UTC): validated 121, +51 Active, re-verified 15, pending left 3207
- Curate (2026-10-11 08:29 UTC): 10682 raw candidates, 43 queued, 26 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3119 | 2342 | 777 |
| FR | 1299 | 669 | 630 |
| JP | 606 | 134 | 472 |
| IN | 603 | 300 | 303 |
| DE | 581 | 321 | 260 |
| AU | 527 | 368 | 159 |
| CN | 491 | 62 | 429 |
| BR | 476 | 228 | 248 |
| RU | 402 | 133 | 269 |
| KR | 305 | 83 | 222 |
| GB | 267 | 133 | 134 |
| ID | 253 | 148 | 105 |
| IR | 233 | 72 | 161 |
| TR | 203 | 137 | 66 |
| CA | 200 | 115 | 85 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7869 |
| `unreachable-dns` | 2409 |
| `fetch-error:ConnectTimeout` | 832 |
| `http-403` | 702 |
| `fetch-error:SSLError` | 672 |
| `fetch-error:ConnectionError` | 588 |
| `low-confidence:http-2xx-html` | 471 |
| `empty-body` | 146 |
| `fetch-error:ReadTimeout` | 78 |
| `http-500` | 44 |
| `http-404` | 42 |
| `http-503` | 24 |

## Freshness

- Verified in last 30 days: **14675** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2409**
- Moved pointers (old domain → new): **671**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 62/491 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 134/606 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/99 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 2 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
