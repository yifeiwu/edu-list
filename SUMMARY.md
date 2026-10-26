# Edu-Domains — Run Summary

_Generated 2026-10-26 22:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21786** across **205** countries
- Active: **11683** (54%) · Inaccessible: **10103** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9599** domains (median 22 yrs)

## Last runs

- Verify (2026-10-26 22:00 UTC): validated 55, +18 Active, re-verified 15, pending left 0
- Curate (2026-10-26 21:29 UTC): 10700 raw candidates, 39 queued, 65 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4502 | 3391 | 1111 |
| FR | 2785 | 1352 | 1433 |
| CN | 1259 | 142 | 1117 |
| IN | 777 | 412 | 365 |
| JP | 773 | 211 | 562 |
| AU | 736 | 537 | 199 |
| DE | 603 | 337 | 266 |
| BR | 565 | 280 | 285 |
| RU | 520 | 194 | 326 |
| ID | 514 | 306 | 208 |
| PL | 417 | 173 | 244 |
| ES | 404 | 260 | 144 |
| KR | 335 | 94 | 241 |
| GB | 294 | 149 | 145 |
| MX | 286 | 157 | 129 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11688 |
| `unreachable-dns` | 3121 |
| `fetch-error:ConnectTimeout` | 1288 |
| `fetch-error:ConnectionError` | 1067 |
| `low-confidence:http-2xx-html` | 998 |
| `http-403` | 983 |
| `fetch-error:SSLError` | 966 |
| `empty-body` | 209 |
| `http-500` | 117 |
| `fetch-error:ReadTimeout` | 114 |
| `http-404` | 86 |
| `http-503` | 45 |

## Freshness

- Verified in last 30 days: **17184** (79%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3121**
- Moved pointers (old domain → new): **917**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 142/1259 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 211/773 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/335 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/144 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 31 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
