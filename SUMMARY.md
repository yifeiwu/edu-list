# Edu-Domains — Run Summary

_Generated 2026-10-23 13:13 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21109** across **205** countries
- Active: **11321** (54%) · Inaccessible: **9788** (46%)
- Pending queue: **36** unvalidated candidates
- Known registration age: **9340** domains (median 22 yrs)

## Last runs

- Verify (2026-10-23 12:11 UTC): validated 48, +19 Active, re-verified 15, pending left 0
- Curate (2026-10-23 13:13 UTC): 10695 raw candidates, 36 queued, 29 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4428 | 3331 | 1097 |
| FR | 2622 | 1277 | 1345 |
| CN | 1238 | 138 | 1100 |
| IN | 747 | 389 | 358 |
| AU | 734 | 535 | 199 |
| JP | 718 | 193 | 525 |
| DE | 599 | 335 | 264 |
| BR | 555 | 275 | 280 |
| ID | 497 | 296 | 201 |
| RU | 483 | 178 | 305 |
| PL | 416 | 172 | 244 |
| ES | 364 | 234 | 130 |
| KR | 331 | 90 | 241 |
| GB | 290 | 147 | 143 |
| MX | 282 | 156 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11326 |
| `unreachable-dns` | 3054 |
| `fetch-error:ConnectTimeout` | 1226 |
| `fetch-error:ConnectionError` | 1027 |
| `http-403` | 969 |
| `fetch-error:SSLError` | 937 |
| `low-confidence:http-2xx-html` | 936 |
| `empty-body` | 209 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18187** (86%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3054**
- Moved pointers (old domain → new): **895**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 138/1238 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 193/718 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 90/331 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/138 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 22 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
