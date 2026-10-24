# Edu-Domains — Run Summary

_Generated 2026-10-24 23:52 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21526** across **205** countries
- Active: **11545** (54%) · Inaccessible: **9981** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9501** domains (median 22 yrs)

## Last runs

- Verify (2026-10-24 23:51 UTC): validated 44, +14 Active, re-verified 15, pending left 0
- Curate (2026-10-24 22:59 UTC): 10692 raw candidates, 27 queued, 62 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4488 | 3379 | 1109 |
| FR | 2734 | 1327 | 1407 |
| CN | 1250 | 140 | 1110 |
| IN | 758 | 397 | 361 |
| JP | 752 | 204 | 548 |
| AU | 736 | 536 | 200 |
| DE | 599 | 335 | 264 |
| BR | 558 | 277 | 281 |
| RU | 518 | 193 | 325 |
| ID | 504 | 299 | 205 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 333 | 92 | 241 |
| GB | 292 | 148 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11550 |
| `unreachable-dns` | 3090 |
| `fetch-error:ConnectTimeout` | 1271 |
| `fetch-error:ConnectionError` | 1051 |
| `http-403` | 980 |
| `low-confidence:http-2xx-html` | 974 |
| `fetch-error:SSLError` | 950 |
| `empty-body` | 210 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 84 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18115** (84%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3090**
- Moved pointers (old domain → new): **911**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 140/1250 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 204/752 (27%) — check for blocks/stale sources
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
