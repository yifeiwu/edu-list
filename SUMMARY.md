# Edu-Domains — Run Summary

_Generated 2026-10-11 15:46 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14779** across **204** countries
- Active: **7934** (54%) · Inaccessible: **6845** (46%)
- Pending queue: **3171** unvalidated candidates
- Known registration age: **6469** domains (median 24 yrs)

## Last runs

- Verify (2026-10-11 15:46 UTC): validated 119, +67 Active, re-verified 15, pending left 3171
- Curate (2026-10-11 15:27 UTC): 10680 raw candidates, 64 queued, 16 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3147 | 2363 | 784 |
| FR | 1319 | 684 | 635 |
| JP | 606 | 134 | 472 |
| IN | 603 | 300 | 303 |
| DE | 581 | 321 | 260 |
| AU | 549 | 381 | 168 |
| CN | 493 | 62 | 431 |
| BR | 477 | 229 | 248 |
| RU | 403 | 134 | 269 |
| KR | 305 | 83 | 222 |
| GB | 270 | 135 | 135 |
| ID | 256 | 150 | 106 |
| IR | 233 | 72 | 161 |
| TR | 203 | 137 | 66 |
| CA | 200 | 115 | 85 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7936 |
| `unreachable-dns` | 2411 |
| `fetch-error:ConnectTimeout` | 833 |
| `http-403` | 712 |
| `fetch-error:SSLError` | 674 |
| `fetch-error:ConnectionError` | 593 |
| `low-confidence:http-2xx-html` | 478 |
| `empty-body` | 151 |
| `fetch-error:ReadTimeout` | 78 |
| `http-500` | 45 |
| `http-404` | 42 |
| `http-503` | 24 |

## Freshness

- Verified in last 30 days: **14779** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2411**
- Moved pointers (old domain → new): **675**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 62/493 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 134/606 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 83/305 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/99 (11%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 2 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
