# Edu-Domains — Run Summary

_Generated 2026-10-17 09:00 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17774** across **204** countries
- Active: **9639** (54%) · Inaccessible: **8135** (46%)
- Pending queue: **1559** unvalidated candidates
- Known registration age: **7822** domains (median 24 yrs)

## Last runs

- Verify (2026-10-17 09:00 UTC): validated 120, +61 Active, re-verified 15, pending left 1559
- Curate (2026-10-17 08:22 UTC): 10700 raw candidates, 45 queued, 39 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3698 | 2784 | 914 |
| FR | 1952 | 982 | 970 |
| AU | 728 | 529 | 199 |
| CN | 708 | 96 | 612 |
| IN | 655 | 333 | 322 |
| JP | 638 | 153 | 485 |
| DE | 592 | 329 | 263 |
| BR | 494 | 240 | 254 |
| RU | 420 | 145 | 275 |
| ID | 385 | 236 | 149 |
| PL | 328 | 145 | 183 |
| KR | 315 | 86 | 229 |
| GB | 284 | 144 | 140 |
| IR | 254 | 80 | 174 |
| CA | 226 | 139 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9641 |
| `unreachable-dns` | 2634 |
| `fetch-error:ConnectTimeout` | 1008 |
| `http-403` | 833 |
| `fetch-error:SSLError` | 804 |
| `fetch-error:ConnectionError` | 774 |
| `low-confidence:http-2xx-html` | 706 |
| `empty-body` | 176 |
| `fetch-error:ReadTimeout` | 95 |
| `http-500` | 71 |
| `http-404` | 56 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **17753** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2634**
- Moved pointers (old domain → new): **795**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 96/708 (14%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 153/638 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/315 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 18/118 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 12 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
