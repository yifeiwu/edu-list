# Edu-Domains — Run Summary

_Generated 2026-10-17 16:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17979** across **204** countries
- Active: **9752** (54%) · Inaccessible: **8227** (46%)
- Pending queue: **1461** unvalidated candidates
- Known registration age: **7970** domains (median 23 yrs)

## Last runs

- Verify (2026-10-17 16:31 UTC): validated 117, +52 Active, re-verified 15, pending left 1461
- Curate (2026-10-17 16:12 UTC): 10700 raw candidates, 55 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3750 | 2820 | 930 |
| FR | 1997 | 1003 | 994 |
| AU | 729 | 529 | 200 |
| CN | 714 | 97 | 617 |
| IN | 659 | 337 | 322 |
| JP | 639 | 153 | 486 |
| DE | 592 | 329 | 263 |
| BR | 494 | 240 | 254 |
| ID | 426 | 262 | 164 |
| RU | 421 | 145 | 276 |
| PL | 376 | 164 | 212 |
| KR | 315 | 86 | 229 |
| GB | 284 | 144 | 140 |
| IR | 254 | 80 | 174 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9754 |
| `unreachable-dns` | 2647 |
| `fetch-error:ConnectTimeout` | 1017 |
| `http-403` | 847 |
| `fetch-error:SSLError` | 817 |
| `fetch-error:ConnectionError` | 792 |
| `low-confidence:http-2xx-html` | 719 |
| `empty-body` | 179 |
| `fetch-error:ReadTimeout` | 96 |
| `http-500` | 72 |
| `http-404` | 57 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **17958** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2647**
- Moved pointers (old domain → new): **800**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 97/714 (14%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 153/639 (24%) — check for blocks/stale sources
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
