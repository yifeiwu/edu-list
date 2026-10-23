# Edu-Domains — Run Summary

_Generated 2026-10-23 18:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21146** across **205** countries
- Active: **11345** (54%) · Inaccessible: **9801** (46%)
- Pending queue: **42** unvalidated candidates
- Known registration age: **9352** domains (median 22 yrs)

## Last runs

- Verify (2026-10-23 17:09 UTC): validated 52, +23 Active, re-verified 15, pending left 0
- Curate (2026-10-23 18:11 UTC): 10691 raw candidates, 42 queued, 29 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4432 | 3335 | 1097 |
| FR | 2635 | 1288 | 1347 |
| CN | 1239 | 138 | 1101 |
| IN | 747 | 389 | 358 |
| AU | 734 | 535 | 199 |
| JP | 721 | 194 | 527 |
| DE | 599 | 335 | 264 |
| BR | 555 | 275 | 280 |
| ID | 497 | 296 | 201 |
| RU | 488 | 180 | 308 |
| PL | 416 | 172 | 244 |
| ES | 366 | 236 | 130 |
| KR | 331 | 90 | 241 |
| GB | 290 | 147 | 143 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11350 |
| `unreachable-dns` | 3058 |
| `fetch-error:ConnectTimeout` | 1231 |
| `fetch-error:ConnectionError` | 1028 |
| `http-403` | 969 |
| `low-confidence:http-2xx-html` | 937 |
| `fetch-error:SSLError` | 937 |
| `empty-body` | 209 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18239** (86%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3058**
- Moved pointers (old domain → new): **896**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 138/1239 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 194/721 (27%) — check for blocks/stale sources
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
