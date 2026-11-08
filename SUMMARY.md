# Edu-Domains — Run Summary

_Generated 2026-11-08 20:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23961** across **205** countries
- Active: **12890** (54%) · Inaccessible: **11071** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10611** domains (median 21 yrs)

## Last runs

- Verify (2026-11-08 20:55 UTC): validated 59, +21 Active, re-verified 15, pending left 0
- Curate (2026-11-08 19:25 UTC): 10696 raw candidates, 40 queued, 54 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4728 | 3578 | 1150 |
| FR | 3318 | 1609 | 1709 |
| CN | 1329 | 154 | 1175 |
| IN | 873 | 484 | 389 |
| JP | 809 | 226 | 583 |
| AU | 738 | 539 | 199 |
| DE | 612 | 345 | 267 |
| RU | 606 | 242 | 364 |
| BR | 589 | 301 | 288 |
| ID | 584 | 352 | 232 |
| UA | 573 | 243 | 330 |
| PL | 461 | 180 | 281 |
| ES | 414 | 266 | 148 |
| GB | 368 | 203 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12895 |
| `unreachable-dns` | 3311 |
| `fetch-error:ConnectTimeout` | 1450 |
| `fetch-error:ConnectionError` | 1208 |
| `low-confidence:http-2xx-html` | 1139 |
| `fetch-error:SSLError` | 1066 |
| `http-403` | 1049 |
| `empty-body` | 230 |
| `fetch-error:ReadTimeout` | 137 |
| `http-500` | 136 |
| `http-404` | 90 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **13081** (55%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3311**
- Moved pointers (old domain → new): **990**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 154/1329 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 116 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
