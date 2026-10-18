# Edu-Domains — Run Summary

_Generated 2026-10-18 22:51 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19000** across **205** countries
- Active: **10254** (54%) · Inaccessible: **8746** (46%)
- Pending queue: **851** unvalidated candidates
- Known registration age: **8417** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 22:51 UTC): validated 118, +33 Active, re-verified 15, pending left 851
- Curate (2026-10-18 20:18 UTC): 10699 raw candidates, 47 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3973 | 2997 | 976 |
| FR | 2174 | 1073 | 1101 |
| CN | 865 | 109 | 756 |
| AU | 731 | 531 | 200 |
| IN | 697 | 356 | 341 |
| JP | 665 | 166 | 499 |
| DE | 595 | 332 | 263 |
| BR | 505 | 251 | 254 |
| ID | 459 | 276 | 183 |
| RU | 457 | 168 | 289 |
| PL | 411 | 171 | 240 |
| KR | 326 | 88 | 238 |
| GB | 287 | 145 | 142 |
| IR | 258 | 82 | 176 |
| CA | 228 | 141 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10258 |
| `unreachable-dns` | 2787 |
| `fetch-error:ConnectTimeout` | 1080 |
| `http-403` | 898 |
| `fetch-error:ConnectionError` | 862 |
| `fetch-error:SSLError` | 858 |
| `low-confidence:http-2xx-html` | 797 |
| `empty-body` | 189 |
| `fetch-error:ReadTimeout` | 103 |
| `http-500` | 85 |
| `http-404` | 66 |
| `http-503` | 37 |

## Freshness

- Verified in last 30 days: **18943** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2787**
- Moved pointers (old domain → new): **827**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 109/865 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 166/665 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 88/326 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/136 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
