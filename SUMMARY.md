# Edu-Domains — Run Summary

_Generated 2026-10-15 02:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16423** across **204** countries
- Active: **8894** (54%) · Inaccessible: **7529** (46%)
- Pending queue: **2285** unvalidated candidates
- Known registration age: **7056** domains (median 24 yrs)

## Last runs

- Verify (2026-10-15 02:00 UTC): validated 118, +60 Active, re-verified 15, pending left 2285
- Curate (2026-10-14 23:45 UTC): 10689 raw candidates, 39 queued, 37 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3391 | 2553 | 838 |
| FR | 1692 | 858 | 834 |
| AU | 692 | 503 | 189 |
| IN | 629 | 315 | 314 |
| JP | 628 | 147 | 481 |
| DE | 591 | 328 | 263 |
| CN | 579 | 77 | 502 |
| BR | 485 | 233 | 252 |
| RU | 415 | 141 | 274 |
| KR | 311 | 85 | 226 |
| GB | 274 | 137 | 137 |
| ID | 271 | 160 | 111 |
| IR | 249 | 79 | 170 |
| CA | 219 | 133 | 86 |
| MX | 216 | 113 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8896 |
| `unreachable-dns` | 2525 |
| `fetch-error:ConnectTimeout` | 940 |
| `http-403` | 771 |
| `fetch-error:SSLError` | 746 |
| `fetch-error:ConnectionError` | 684 |
| `low-confidence:http-2xx-html` | 590 |
| `empty-body` | 166 |
| `fetch-error:ReadTimeout` | 90 |
| `http-500` | 65 |
| `http-404` | 51 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **16423** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2525**
- Moved pointers (old domain → new): **730**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 77/579 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 147/628 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/311 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 14/106 (13%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
