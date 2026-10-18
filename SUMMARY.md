# Edu-Domains — Run Summary

_Generated 2026-10-18 20:18 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18797** across **205** countries
- Active: **10173** (54%) · Inaccessible: **8624** (46%)
- Pending queue: **1051** unvalidated candidates
- Known registration age: **8313** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 18:17 UTC): validated 117, +57 Active, re-verified 15, pending left 1004
- Curate (2026-10-18 20:18 UTC): 10699 raw candidates, 47 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3930 | 2965 | 965 |
| FR | 2137 | 1059 | 1078 |
| CN | 829 | 108 | 721 |
| AU | 731 | 531 | 200 |
| IN | 695 | 354 | 341 |
| JP | 664 | 166 | 498 |
| DE | 595 | 332 | 263 |
| BR | 503 | 250 | 253 |
| RU | 456 | 167 | 289 |
| ID | 453 | 274 | 179 |
| PL | 410 | 170 | 240 |
| KR | 317 | 87 | 230 |
| GB | 287 | 145 | 142 |
| IR | 257 | 81 | 176 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10177 |
| `unreachable-dns` | 2769 |
| `fetch-error:ConnectTimeout` | 1068 |
| `http-403` | 880 |
| `fetch-error:ConnectionError` | 849 |
| `fetch-error:SSLError` | 848 |
| `low-confidence:http-2xx-html` | 767 |
| `empty-body` | 186 |
| `fetch-error:ReadTimeout` | 101 |
| `http-500` | 80 |
| `http-404` | 65 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18740** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2769**
- Moved pointers (old domain → new): **822**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 108/829 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 166/664 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 87/317 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/134 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
