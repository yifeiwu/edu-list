# Edu-Domains — Run Summary

_Generated 2026-10-16 17:14 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17248** across **204** countries
- Active: **9332** (54%) · Inaccessible: **7916** (46%)
- Pending queue: **1895** unvalidated candidates
- Known registration age: **7476** domains (median 24 yrs)

## Last runs

- Verify (2026-10-16 14:22 UTC): validated 116, +61 Active, re-verified 15, pending left 1851
- Curate (2026-10-16 17:14 UTC): 10684 raw candidates, 44 queued, 37 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3593 | 2699 | 894 |
| FR | 1855 | 934 | 921 |
| AU | 711 | 516 | 195 |
| CN | 696 | 92 | 604 |
| IN | 651 | 329 | 322 |
| JP | 636 | 152 | 484 |
| DE | 592 | 329 | 263 |
| BR | 490 | 236 | 254 |
| RU | 418 | 143 | 275 |
| KR | 314 | 86 | 228 |
| ID | 289 | 174 | 115 |
| GB | 283 | 144 | 139 |
| IR | 254 | 80 | 174 |
| CA | 224 | 137 | 87 |
| IT | 218 | 112 | 106 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9334 |
| `unreachable-dns` | 2614 |
| `fetch-error:ConnectTimeout` | 986 |
| `http-403` | 798 |
| `fetch-error:SSLError` | 778 |
| `fetch-error:ConnectionError` | 749 |
| `low-confidence:http-2xx-html` | 659 |
| `empty-body` | 172 |
| `fetch-error:ReadTimeout` | 91 |
| `http-500` | 67 |
| `http-404` | 54 |
| `http-503` | 35 |

## Freshness

- Verified in last 30 days: **17248** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2614**
- Moved pointers (old domain → new): **766**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 92/696 (13%) — check for blocks/stale sources
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
