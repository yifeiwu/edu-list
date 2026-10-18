# Edu-Domains — Run Summary

_Generated 2026-10-18 20:49 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18897** across **205** countries
- Active: **10222** (54%) · Inaccessible: **8675** (46%)
- Pending queue: **951** unvalidated candidates
- Known registration age: **8352** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 20:49 UTC): validated 115, +50 Active, re-verified 15, pending left 951
- Curate (2026-10-18 20:18 UTC): 10699 raw candidates, 47 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3953 | 2982 | 971 |
| FR | 2160 | 1070 | 1090 |
| CN | 848 | 108 | 740 |
| AU | 731 | 531 | 200 |
| IN | 696 | 355 | 341 |
| JP | 665 | 166 | 499 |
| DE | 595 | 332 | 263 |
| BR | 503 | 250 | 253 |
| RU | 457 | 168 | 289 |
| ID | 455 | 275 | 180 |
| PL | 410 | 170 | 240 |
| KR | 322 | 88 | 234 |
| GB | 287 | 145 | 142 |
| IR | 257 | 81 | 176 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10226 |
| `unreachable-dns` | 2778 |
| `fetch-error:ConnectTimeout` | 1073 |
| `http-403` | 895 |
| `fetch-error:SSLError` | 854 |
| `fetch-error:ConnectionError` | 852 |
| `low-confidence:http-2xx-html` | 773 |
| `empty-body` | 188 |
| `fetch-error:ReadTimeout` | 102 |
| `http-500` | 82 |
| `http-404` | 65 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18840** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2778**
- Moved pointers (old domain → new): **823**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 108/848 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 166/665 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 88/322 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/135 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
