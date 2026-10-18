# Edu-Domains — Run Summary

_Generated 2026-10-18 15:03 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18695** across **205** countries
- Active: **10115** (54%) · Inaccessible: **8580** (46%)
- Pending queue: **1062** unvalidated candidates
- Known registration age: **8267** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 15:03 UTC): validated 118, +60 Active, re-verified 15, pending left 1062
- Curate (2026-10-18 14:22 UTC): 10701 raw candidates, 61 queued, 33 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3906 | 2944 | 962 |
| FR | 2124 | 1054 | 1070 |
| CN | 815 | 106 | 709 |
| AU | 731 | 531 | 200 |
| IN | 693 | 354 | 339 |
| JP | 659 | 162 | 497 |
| DE | 595 | 332 | 263 |
| BR | 502 | 249 | 253 |
| RU | 454 | 166 | 288 |
| ID | 450 | 272 | 178 |
| PL | 410 | 170 | 240 |
| KR | 316 | 86 | 230 |
| GB | 286 | 145 | 141 |
| IR | 256 | 81 | 175 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10119 |
| `unreachable-dns` | 2758 |
| `fetch-error:ConnectTimeout` | 1063 |
| `http-403` | 875 |
| `fetch-error:SSLError` | 848 |
| `fetch-error:ConnectionError` | 842 |
| `low-confidence:http-2xx-html` | 756 |
| `empty-body` | 187 |
| `fetch-error:ReadTimeout` | 99 |
| `http-500` | 80 |
| `http-404` | 64 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18628** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2758**
- Moved pointers (old domain → new): **820**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 106/815 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 162/659 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/133 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
