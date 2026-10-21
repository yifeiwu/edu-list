# Edu-Domains — Run Summary

_Generated 2026-10-21 07:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20332** across **205** countries
- Active: **10915** (54%) · Inaccessible: **9417** (46%)
- Pending queue: **225** unvalidated candidates
- Known registration age: **8990** domains (median 22 yrs)

## Last runs

- Verify (2026-10-21 07:53 UTC): validated 116, +45 Active, re-verified 15, pending left 225
- Curate (2026-10-21 07:17 UTC): 10698 raw candidates, 56 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4249 | 3202 | 1047 |
| FR | 2481 | 1210 | 1271 |
| CN | 1121 | 131 | 990 |
| AU | 734 | 534 | 200 |
| IN | 728 | 374 | 354 |
| JP | 708 | 189 | 519 |
| DE | 597 | 333 | 264 |
| BR | 516 | 255 | 261 |
| ID | 493 | 295 | 198 |
| RU | 466 | 173 | 293 |
| PL | 413 | 172 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 271 | 85 | 186 |
| ES | 269 | 160 | 109 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10919 |
| `unreachable-dns` | 2965 |
| `fetch-error:ConnectTimeout` | 1174 |
| `fetch-error:ConnectionError` | 967 |
| `http-403` | 944 |
| `fetch-error:SSLError` | 911 |
| `low-confidence:http-2xx-html` | 883 |
| `empty-body` | 202 |
| `fetch-error:ReadTimeout` | 111 |
| `http-500` | 100 |
| `http-404` | 76 |
| `http-503` | 40 |

## Freshness

- Verified in last 30 days: **18365** (90%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2965**
- Moved pointers (old domain → new): **867**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 131/1121 (12%) — check for blocks/stale sources
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
