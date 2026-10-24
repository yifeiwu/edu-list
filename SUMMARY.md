# Edu-Domains — Run Summary

_Generated 2026-10-24 02:08 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21299** across **205** countries
- Active: **11424** (54%) · Inaccessible: **9875** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9396** domains (median 22 yrs)

## Last runs

- Verify (2026-10-24 02:08 UTC): validated 85, +33 Active, re-verified 15, pending left 0
- Curate (2026-10-24 00:23 UTC): 10690 raw candidates, 68 queued, 10565 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4462 | 3358 | 1104 |
| FR | 2667 | 1299 | 1368 |
| CN | 1243 | 139 | 1104 |
| IN | 748 | 390 | 358 |
| AU | 734 | 535 | 199 |
| JP | 733 | 199 | 534 |
| DE | 599 | 335 | 264 |
| BR | 556 | 276 | 280 |
| RU | 512 | 190 | 322 |
| ID | 499 | 296 | 203 |
| PL | 416 | 172 | 244 |
| ES | 385 | 248 | 137 |
| KR | 332 | 91 | 241 |
| GB | 290 | 147 | 143 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11429 |
| `unreachable-dns` | 3076 |
| `fetch-error:ConnectTimeout` | 1244 |
| `fetch-error:ConnectionError` | 1036 |
| `http-403` | 973 |
| `low-confidence:http-2xx-html` | 952 |
| `fetch-error:SSLError` | 945 |
| `empty-body` | 209 |
| `http-500` | 114 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17798** (84%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3076**
- Moved pointers (old domain → new): **901**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 139/1243 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 199/733 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 91/332 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/141 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 23 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
