# Edu-Domains — Run Summary

_Generated 2026-10-24 16:06 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21440** across **205** countries
- Active: **11504** (54%) · Inaccessible: **9936** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9464** domains (median 22 yrs)

## Last runs

- Verify (2026-10-24 16:06 UTC): validated 51, +22 Active, re-verified 15, pending left 0
- Curate (2026-10-24 14:20 UTC): 10693 raw candidates, 36 queued, 59 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4486 | 3378 | 1108 |
| FR | 2705 | 1319 | 1386 |
| CN | 1246 | 140 | 1106 |
| IN | 755 | 395 | 360 |
| JP | 740 | 201 | 539 |
| AU | 736 | 536 | 200 |
| DE | 599 | 335 | 264 |
| BR | 558 | 277 | 281 |
| RU | 514 | 190 | 324 |
| ID | 502 | 297 | 205 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 333 | 92 | 241 |
| GB | 292 | 148 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11509 |
| `unreachable-dns` | 3081 |
| `fetch-error:ConnectTimeout` | 1255 |
| `fetch-error:ConnectionError` | 1048 |
| `http-403` | 980 |
| `low-confidence:http-2xx-html` | 966 |
| `fetch-error:SSLError` | 949 |
| `empty-body` | 209 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 83 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17984** (84%)
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
