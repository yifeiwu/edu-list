# Edu-Domains — Run Summary

_Generated 2026-10-19 23:26 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19512** across **205** countries
- Active: **10528** (54%) · Inaccessible: **8984** (46%)
- Pending queue: **633** unvalidated candidates
- Known registration age: **8665** domains (median 23 yrs)

## Last runs

- Verify (2026-10-19 22:29 UTC): validated 116, +60 Active, re-verified 15, pending left 579
- Curate (2026-10-19 23:26 UTC): 10699 raw candidates, 54 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4089 | 3087 | 1002 |
| FR | 2314 | 1141 | 1173 |
| CN | 928 | 116 | 812 |
| AU | 733 | 532 | 201 |
| IN | 710 | 365 | 345 |
| JP | 687 | 179 | 508 |
| DE | 597 | 333 | 264 |
| BR | 511 | 253 | 258 |
| ID | 476 | 285 | 191 |
| RU | 460 | 171 | 289 |
| PL | 412 | 171 | 241 |
| KR | 329 | 89 | 240 |
| GB | 288 | 146 | 142 |
| IR | 261 | 83 | 178 |
| CA | 230 | 142 | 88 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10532 |
| `unreachable-dns` | 2845 |
| `fetch-error:ConnectTimeout` | 1107 |
| `http-403` | 916 |
| `fetch-error:ConnectionError` | 900 |
| `fetch-error:SSLError` | 878 |
| `low-confidence:http-2xx-html` | 828 |
| `empty-body` | 196 |
| `fetch-error:ReadTimeout` | 105 |
| `http-500` | 93 |
| `http-404` | 72 |
| `http-503` | 38 |

## Freshness

- Verified in last 30 days: **18853** (97%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2845**
- Moved pointers (old domain → new): **841**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 116/928 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 179/687 (26%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/329 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/136 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 16 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
