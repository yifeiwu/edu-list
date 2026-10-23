# Edu-Domains — Run Summary

_Generated 2026-10-23 23:36 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21229** across **205** countries
- Active: **11391** (54%) · Inaccessible: **9838** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9376** domains (median 22 yrs)

## Last runs

- Verify (2026-10-23 23:36 UTC): validated 55, +25 Active, re-verified 15, pending left 0
- Curate (2026-10-23 21:56 UTC): 10687 raw candidates, 38 queued, 31 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4450 | 3347 | 1103 |
| FR | 2652 | 1295 | 1357 |
| CN | 1241 | 139 | 1102 |
| IN | 747 | 389 | 358 |
| AU | 734 | 535 | 199 |
| JP | 729 | 198 | 531 |
| DE | 599 | 335 | 264 |
| BR | 555 | 275 | 280 |
| RU | 502 | 187 | 315 |
| ID | 498 | 296 | 202 |
| PL | 416 | 172 | 244 |
| ES | 372 | 240 | 132 |
| KR | 332 | 91 | 241 |
| GB | 290 | 147 | 143 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11396 |
| `unreachable-dns` | 3065 |
| `fetch-error:ConnectTimeout` | 1238 |
| `fetch-error:ConnectionError` | 1032 |
| `http-403` | 971 |
| `low-confidence:http-2xx-html` | 946 |
| `fetch-error:SSLError` | 941 |
| `empty-body` | 209 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18352** (86%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3065**
- Moved pointers (old domain → new): **899**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 139/1241 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 198/729 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 91/332 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/138 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 23 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
