# Edu-Domains — Run Summary

_Generated 2026-10-20 09:52 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19714** across **205** countries
- Active: **10623** (54%) · Inaccessible: **9091** (46%)
- Pending queue: **550** unvalidated candidates
- Known registration age: **8753** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 06:50 UTC): validated 116, +46 Active, re-verified 15, pending left 484
- Curate (2026-10-20 09:52 UTC): 10701 raw candidates, 66 queued, 36 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4119 | 3110 | 1009 |
| FR | 2357 | 1159 | 1198 |
| CN | 967 | 118 | 849 |
| AU | 733 | 533 | 200 |
| IN | 720 | 368 | 352 |
| JP | 700 | 185 | 515 |
| DE | 597 | 333 | 264 |
| BR | 514 | 254 | 260 |
| ID | 488 | 291 | 197 |
| RU | 462 | 172 | 290 |
| PL | 412 | 171 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 264 | 83 | 181 |
| CA | 232 | 143 | 89 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10627 |
| `unreachable-dns` | 2878 |
| `fetch-error:ConnectTimeout` | 1123 |
| `http-403` | 928 |
| `fetch-error:ConnectionError` | 913 |
| `fetch-error:SSLError` | 883 |
| `low-confidence:http-2xx-html` | 845 |
| `empty-body` | 195 |
| `fetch-error:ReadTimeout` | 107 |
| `http-500` | 94 |
| `http-404` | 73 |
| `http-503` | 39 |

## Freshness

- Verified in last 30 days: **18377** (93%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2878**
- Moved pointers (old domain → new): **844**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 118/967 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 185/700 (26%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/136 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 17 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
