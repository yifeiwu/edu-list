# Edu-Domains — Run Summary

_Generated 2026-10-21 13:35 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20436** across **205** countries
- Active: **10966** (54%) · Inaccessible: **9470** (46%)
- Pending queue: **190** unvalidated candidates
- Known registration age: **9025** domains (median 22 yrs)

## Last runs

- Verify (2026-10-21 13:23 UTC): validated 119, +51 Active, re-verified 15, pending left 125
- Curate (2026-10-21 13:35 UTC): 10686 raw candidates, 65 queued, 22 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4269 | 3219 | 1050 |
| FR | 2494 | 1217 | 1277 |
| CN | 1149 | 135 | 1014 |
| AU | 734 | 534 | 200 |
| IN | 730 | 375 | 355 |
| JP | 708 | 189 | 519 |
| DE | 597 | 333 | 264 |
| BR | 516 | 255 | 261 |
| ID | 493 | 295 | 198 |
| RU | 472 | 174 | 298 |
| PL | 416 | 172 | 244 |
| KR | 330 | 89 | 241 |
| GB | 289 | 147 | 142 |
| ES | 277 | 166 | 111 |
| IR | 272 | 86 | 186 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10971 |
| `unreachable-dns` | 2982 |
| `fetch-error:ConnectTimeout` | 1177 |
| `fetch-error:ConnectionError` | 973 |
| `http-403` | 947 |
| `fetch-error:SSLError` | 915 |
| `low-confidence:http-2xx-html` | 894 |
| `empty-body` | 202 |
| `fetch-error:ReadTimeout` | 111 |
| `http-500` | 102 |
| `http-404` | 77 |
| `http-503` | 40 |

## Freshness

- Verified in last 30 days: **18484** (90%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2982**
- Moved pointers (old domain → new): **872**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 135/1149 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 189/708 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/138 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 19 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
