# Edu-Domains — Run Summary

_Generated 2026-10-23 01:35 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21076** across **205** countries
- Active: **11299** (54%) · Inaccessible: **9777** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9321** domains (median 22 yrs)

## Last runs

- Verify (2026-10-23 01:35 UTC): validated 63, +32 Active, re-verified 15, pending left 0
- Curate (2026-10-23 01:20 UTC): 10696 raw candidates, 47 queued, 10589 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4418 | 3323 | 1095 |
| FR | 2612 | 1272 | 1340 |
| CN | 1236 | 138 | 1098 |
| IN | 746 | 389 | 357 |
| AU | 734 | 535 | 199 |
| JP | 717 | 192 | 525 |
| DE | 598 | 334 | 264 |
| BR | 555 | 275 | 280 |
| ID | 497 | 296 | 201 |
| RU | 483 | 178 | 305 |
| PL | 416 | 172 | 244 |
| ES | 363 | 233 | 130 |
| KR | 331 | 90 | 241 |
| GB | 289 | 147 | 142 |
| MX | 282 | 156 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11304 |
| `unreachable-dns` | 3051 |
| `fetch-error:ConnectTimeout` | 1223 |
| `fetch-error:ConnectionError` | 1026 |
| `http-403` | 970 |
| `fetch-error:SSLError` | 937 |
| `low-confidence:http-2xx-html` | 936 |
| `empty-body` | 209 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 111 |
| `http-404` | 82 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18079** (86%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3051**
- Moved pointers (old domain → new): **893**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 138/1236 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 192/717 (27%) — check for blocks/stale sources
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
