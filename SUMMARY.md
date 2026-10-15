# Edu-Domains — Run Summary

_Generated 2026-10-15 21:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16838** across **204** countries
- Active: **9106** (54%) · Inaccessible: **7732** (46%)
- Pending queue: **2084** unvalidated candidates
- Known registration age: **7245** domains (median 24 yrs)

## Last runs

- Verify (2026-10-15 21:31 UTC): validated 119, +62 Active, re-verified 15, pending left 2084
- Curate (2026-10-15 18:57 UTC): 10685 raw candidates, 57 queued, 37 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3463 | 2605 | 858 |
| FR | 1787 | 903 | 884 |
| AU | 697 | 505 | 192 |
| CN | 648 | 86 | 562 |
| IN | 645 | 324 | 321 |
| JP | 633 | 150 | 483 |
| DE | 592 | 329 | 263 |
| BR | 487 | 235 | 252 |
| RU | 416 | 142 | 274 |
| KR | 314 | 86 | 228 |
| GB | 282 | 144 | 138 |
| ID | 272 | 160 | 112 |
| IR | 252 | 80 | 172 |
| CA | 219 | 133 | 86 |
| MX | 217 | 114 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9108 |
| `unreachable-dns` | 2570 |
| `fetch-error:ConnectTimeout` | 964 |
| `http-403` | 787 |
| `fetch-error:SSLError` | 760 |
| `fetch-error:ConnectionError` | 724 |
| `low-confidence:http-2xx-html` | 619 |
| `empty-body` | 171 |
| `fetch-error:ReadTimeout` | 90 |
| `http-500` | 65 |
| `http-404` | 52 |
| `http-503` | 33 |

## Freshness

- Verified in last 30 days: **16838** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2570**
- Moved pointers (old domain → new): **752**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 86/648 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 150/633 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/314 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 17/116 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
