# Edu-Domains — Run Summary

_Generated 2026-10-13 02:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15397** across **204** countries
- Active: **8327** (54%) · Inaccessible: **7070** (46%)
- Pending queue: **2857** unvalidated candidates
- Known registration age: **6692** domains (median 24 yrs)

## Last runs

- Verify (2026-10-13 02:11 UTC): validated 120, +60 Active, re-verified 15, pending left 2857
- Curate (2026-10-13 00:18 UTC): 10695 raw candidates, 59 queued, 10570 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3236 | 2431 | 805 |
| FR | 1454 | 738 | 716 |
| AU | 658 | 472 | 186 |
| JP | 621 | 144 | 477 |
| IN | 615 | 308 | 307 |
| DE | 587 | 326 | 261 |
| CN | 504 | 64 | 440 |
| BR | 479 | 230 | 249 |
| RU | 407 | 136 | 271 |
| KR | 307 | 85 | 222 |
| GB | 271 | 135 | 136 |
| ID | 269 | 159 | 110 |
| IR | 238 | 73 | 165 |
| CA | 215 | 130 | 85 |
| TR | 204 | 137 | 67 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8329 |
| `unreachable-dns` | 2446 |
| `fetch-error:ConnectTimeout` | 865 |
| `http-403` | 736 |
| `fetch-error:SSLError` | 692 |
| `fetch-error:ConnectionError` | 630 |
| `low-confidence:http-2xx-html` | 512 |
| `empty-body` | 157 |
| `fetch-error:ReadTimeout` | 82 |
| `http-500` | 49 |
| `http-404` | 42 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **15397** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2446**
- Moved pointers (old domain → new): **696**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 64/504 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 144/621 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/307 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 12/101 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 7 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
