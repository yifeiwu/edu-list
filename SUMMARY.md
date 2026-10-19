# Edu-Domains — Run Summary

_Generated 2026-10-19 12:33 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19307** across **205** countries
- Active: **10412** (54%) · Inaccessible: **8895** (46%)
- Pending queue: **717** unvalidated candidates
- Known registration age: **8560** domains (median 23 yrs)

## Last runs

- Verify (2026-10-19 11:32 UTC): validated 117, +42 Active, re-verified 15, pending left 665
- Curate (2026-10-19 12:33 UTC): 10700 raw candidates, 52 queued, 39 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4045 | 3051 | 994 |
| FR | 2260 | 1113 | 1147 |
| CN | 914 | 115 | 799 |
| AU | 732 | 532 | 200 |
| IN | 704 | 360 | 344 |
| JP | 671 | 169 | 502 |
| DE | 597 | 333 | 264 |
| BR | 509 | 253 | 256 |
| ID | 465 | 279 | 186 |
| RU | 458 | 169 | 289 |
| PL | 412 | 171 | 241 |
| KR | 328 | 89 | 239 |
| GB | 288 | 146 | 142 |
| IR | 259 | 83 | 176 |
| CA | 229 | 141 | 88 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10416 |
| `unreachable-dns` | 2824 |
| `fetch-error:ConnectTimeout` | 1098 |
| `http-403` | 906 |
| `fetch-error:ConnectionError` | 888 |
| `fetch-error:SSLError` | 872 |
| `low-confidence:http-2xx-html` | 815 |
| `empty-body` | 192 |
| `fetch-error:ReadTimeout` | 104 |
| `http-500` | 92 |
| `http-404` | 69 |
| `http-503` | 38 |

## Freshness

- Verified in last 30 days: **18618** (96%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2824**
- Moved pointers (old domain → new): **835**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 115/914 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 169/671 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/328 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/136 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 16 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
