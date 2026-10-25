# Edu-Domains — Run Summary

_Generated 2026-10-25 13:02 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21585** across **205** countries
- Active: **11574** (54%) · Inaccessible: **10011** (46%)
- Pending queue: **18** unvalidated candidates
- Known registration age: **9526** domains (median 22 yrs)

## Last runs

- Verify (2026-10-25 12:35 UTC): validated 39, +15 Active, re-verified 15, pending left 0
- Curate (2026-10-25 13:02 UTC): 10701 raw candidates, 18 queued, 85 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4495 | 3384 | 1111 |
| FR | 2746 | 1330 | 1416 |
| CN | 1250 | 140 | 1110 |
| IN | 765 | 402 | 363 |
| JP | 754 | 204 | 550 |
| AU | 736 | 537 | 199 |
| DE | 600 | 335 | 265 |
| BR | 559 | 277 | 282 |
| RU | 519 | 194 | 325 |
| ID | 506 | 301 | 205 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 334 | 93 | 241 |
| GB | 293 | 149 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11579 |
| `unreachable-dns` | 3097 |
| `fetch-error:ConnectTimeout` | 1276 |
| `fetch-error:ConnectionError` | 1056 |
| `low-confidence:http-2xx-html` | 984 |
| `http-403` | 978 |
| `fetch-error:SSLError` | 952 |
| `empty-body` | 210 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 86 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17572** (81%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **3**
- Retired, no DNS record (`unreachable-dns`): **3097**
- Moved pointers (old domain → new): **911**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 140/1250 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 204/754 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 93/334 (28%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/142 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 30 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
