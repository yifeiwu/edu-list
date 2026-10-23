# Edu-Domains — Run Summary

_Generated 2026-10-23 01:20 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21028** across **205** countries
- Active: **11268** (54%) · Inaccessible: **9760** (46%)
- Pending queue: **47** unvalidated candidates
- Known registration age: **9290** domains (median 22 yrs)

## Last runs

- Verify (2026-10-22 22:52 UTC): validated 63, +23 Active, re-verified 15, pending left 0
- Curate (2026-10-23 01:20 UTC): 10696 raw candidates, 47 queued, 10589 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4401 | 3311 | 1090 |
| FR | 2604 | 1266 | 1338 |
| CN | 1234 | 138 | 1096 |
| IN | 744 | 388 | 356 |
| AU | 734 | 534 | 200 |
| JP | 717 | 192 | 525 |
| DE | 598 | 334 | 264 |
| BR | 550 | 272 | 278 |
| ID | 497 | 296 | 201 |
| RU | 483 | 178 | 305 |
| PL | 416 | 172 | 244 |
| ES | 360 | 231 | 129 |
| KR | 331 | 90 | 241 |
| GB | 289 | 147 | 142 |
| MX | 280 | 154 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11273 |
| `unreachable-dns` | 3046 |
| `fetch-error:ConnectTimeout` | 1219 |
| `fetch-error:ConnectionError` | 1027 |
| `http-403` | 969 |
| `fetch-error:SSLError` | 936 |
| `low-confidence:http-2xx-html` | 932 |
| `empty-body` | 209 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 110 |
| `http-404` | 81 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **18016** (86%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3046**
- Moved pointers (old domain → new): **892**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 138/1234 (11%) — check for blocks/stale sources
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
