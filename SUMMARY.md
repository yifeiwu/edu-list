# Edu-Domains — Run Summary

_Generated 2026-10-20 20:50 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20023** across **205** countries
- Active: **10759** (54%) · Inaccessible: **9264** (46%)
- Pending queue: **367** unvalidated candidates
- Known registration age: **8872** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 20:50 UTC): validated 119, +48 Active, re-verified 15, pending left 367
- Curate (2026-10-20 19:03 UTC): 10693 raw candidates, 59 queued, 25 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4180 | 3154 | 1026 |
| FR | 2423 | 1187 | 1236 |
| CN | 1047 | 123 | 924 |
| AU | 734 | 534 | 200 |
| IN | 724 | 370 | 354 |
| JP | 705 | 188 | 517 |
| DE | 597 | 333 | 264 |
| BR | 515 | 254 | 261 |
| ID | 493 | 295 | 198 |
| RU | 462 | 172 | 290 |
| PL | 413 | 172 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 267 | 84 | 183 |
| MX | 245 | 130 | 115 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10763 |
| `unreachable-dns` | 2922 |
| `fetch-error:ConnectTimeout` | 1153 |
| `fetch-error:ConnectionError` | 940 |
| `http-403` | 938 |
| `fetch-error:SSLError` | 897 |
| `low-confidence:http-2xx-html` | 865 |
| `empty-body` | 200 |
| `fetch-error:ReadTimeout` | 109 |
| `http-500` | 95 |
| `http-404` | 75 |
| `http-503` | 40 |

## Freshness

- Verified in last 30 days: **18731** (94%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2922**
- Moved pointers (old domain → new): **856**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 123/1047 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 188/705 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/137 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 18 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
