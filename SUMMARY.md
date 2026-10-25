# Edu-Domains — Run Summary

_Generated 2026-10-25 23:07 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21642** across **205** countries
- Active: **11610** (54%) · Inaccessible: **10032** (46%)
- Pending queue: **29** unvalidated candidates
- Known registration age: **9545** domains (median 22 yrs)

## Last runs

- Verify (2026-10-25 22:04 UTC): validated 35, +13 Active, re-verified 15, pending left 0
- Curate (2026-10-25 23:07 UTC): 10686 raw candidates, 29 queued, 54 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4498 | 3386 | 1112 |
| FR | 2751 | 1335 | 1416 |
| CN | 1252 | 141 | 1111 |
| IN | 771 | 407 | 364 |
| JP | 765 | 209 | 556 |
| AU | 736 | 537 | 199 |
| DE | 601 | 336 | 265 |
| BR | 560 | 277 | 283 |
| RU | 519 | 194 | 325 |
| ID | 509 | 303 | 206 |
| PL | 416 | 172 | 244 |
| ES | 404 | 260 | 144 |
| KR | 334 | 93 | 241 |
| GB | 293 | 149 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11615 |
| `unreachable-dns` | 3105 |
| `fetch-error:ConnectTimeout` | 1280 |
| `fetch-error:ConnectionError` | 1058 |
| `low-confidence:http-2xx-html` | 988 |
| `http-403` | 979 |
| `fetch-error:SSLError` | 954 |
| `empty-body` | 209 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 86 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17674** (82%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **3**
- Retired, no DNS record (`unreachable-dns`): **3105**
- Moved pointers (old domain → new): **912**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 141/1252 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 209/765 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 93/334 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/142 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 31 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
