# Edu-Domains — Run Summary

_Generated 2026-10-16 04:38 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17043** across **204** countries
- Active: **9210** (54%) · Inaccessible: **7833** (46%)
- Pending queue: **1988** unvalidated candidates
- Known registration age: **7362** domains (median 24 yrs)

## Last runs

- Verify (2026-10-16 04:38 UTC): validated 119, +51 Active, re-verified 15, pending left 1988
- Curate (2026-10-16 01:04 UTC): 10698 raw candidates, 50 queued, 10589 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3517 | 2639 | 878 |
| FR | 1824 | 921 | 903 |
| AU | 702 | 507 | 195 |
| CN | 669 | 88 | 581 |
| IN | 647 | 326 | 321 |
| JP | 636 | 152 | 484 |
| DE | 592 | 329 | 263 |
| BR | 489 | 235 | 254 |
| RU | 416 | 142 | 274 |
| KR | 314 | 86 | 228 |
| ID | 287 | 172 | 115 |
| GB | 283 | 144 | 139 |
| IR | 252 | 80 | 172 |
| CA | 220 | 133 | 87 |
| IT | 217 | 111 | 106 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9212 |
| `unreachable-dns` | 2596 |
| `fetch-error:ConnectTimeout` | 979 |
| `http-403` | 795 |
| `fetch-error:SSLError` | 770 |
| `fetch-error:ConnectionError` | 738 |
| `low-confidence:http-2xx-html` | 633 |
| `empty-body` | 172 |
| `fetch-error:ReadTimeout` | 90 |
| `http-500` | 67 |
| `http-404` | 53 |
| `http-503` | 34 |

## Freshness

- Verified in last 30 days: **17043** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2596**
- Moved pointers (old domain → new): **760**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 88/669 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 152/636 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/314 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 18/118 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 11 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
