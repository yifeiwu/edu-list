# Edu-Domains — Run Summary

_Generated 2026-10-20 01:28 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19613** across **205** countries
- Active: **10576** (54%) · Inaccessible: **9037** (46%)
- Pending queue: **533** unvalidated candidates
- Known registration age: **8709** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 01:28 UTC): validated 116, +50 Active, re-verified 15, pending left 533
- Curate (2026-10-19 23:26 UTC): 10699 raw candidates, 54 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4101 | 3096 | 1005 |
| FR | 2340 | 1150 | 1190 |
| CN | 942 | 118 | 824 |
| AU | 733 | 532 | 201 |
| IN | 714 | 367 | 347 |
| JP | 696 | 184 | 512 |
| DE | 597 | 333 | 264 |
| BR | 514 | 254 | 260 |
| ID | 481 | 287 | 194 |
| RU | 461 | 172 | 289 |
| PL | 412 | 171 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 263 | 83 | 180 |
| CA | 231 | 142 | 89 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10580 |
| `unreachable-dns` | 2860 |
| `fetch-error:ConnectTimeout` | 1115 |
| `http-403` | 921 |
| `fetch-error:ConnectionError` | 906 |
| `fetch-error:SSLError` | 881 |
| `low-confidence:http-2xx-html` | 838 |
| `empty-body` | 196 |
| `fetch-error:ReadTimeout` | 106 |
| `http-500` | 94 |
| `http-404` | 72 |
| `http-503` | 38 |

## Freshness

- Verified in last 30 days: **18261** (93%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2860**
- Moved pointers (old domain → new): **843**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 118/942 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 184/696 (26%) — check for blocks/stale sources
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
