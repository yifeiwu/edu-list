# Edu-Domains — Run Summary

_Generated 2026-10-24 14:20 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21404** across **205** countries
- Active: **11482** (54%) · Inaccessible: **9922** (46%)
- Pending queue: **36** unvalidated candidates
- Known registration age: **9445** domains (median 22 yrs)

## Last runs

- Verify (2026-10-24 12:20 UTC): validated 69, +26 Active, re-verified 15, pending left 0
- Curate (2026-10-24 14:20 UTC): 10693 raw candidates, 36 queued, 59 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4483 | 3375 | 1108 |
| FR | 2692 | 1313 | 1379 |
| CN | 1246 | 140 | 1106 |
| IN | 753 | 393 | 360 |
| JP | 740 | 201 | 539 |
| AU | 736 | 536 | 200 |
| DE | 599 | 335 | 264 |
| BR | 556 | 275 | 281 |
| RU | 513 | 190 | 323 |
| ID | 501 | 297 | 204 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 333 | 92 | 241 |
| GB | 291 | 148 | 143 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11487 |
| `unreachable-dns` | 3081 |
| `fetch-error:ConnectTimeout` | 1251 |
| `fetch-error:ConnectionError` | 1043 |
| `http-403` | 979 |
| `low-confidence:http-2xx-html` | 963 |
| `fetch-error:SSLError` | 949 |
| `empty-body` | 209 |
| `http-500` | 114 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17933** (84%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3081**
- Moved pointers (old domain → new): **907**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 140/1246 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 201/740 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 92/333 (28%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/142 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 24 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
