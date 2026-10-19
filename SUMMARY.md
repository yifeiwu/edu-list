# Edu-Domains — Run Summary

_Generated 2026-10-19 05:36 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19205** across **205** countries
- Active: **10370** (54%) · Inaccessible: **8835** (46%)
- Pending queue: **706** unvalidated candidates
- Known registration age: **8519** domains (median 23 yrs)

## Last runs

- Verify (2026-10-19 05:36 UTC): validated 116, +61 Active, re-verified 15, pending left 706
- Curate (2026-10-19 00:55 UTC): 10701 raw candidates, 55 queued, 10587 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4023 | 3035 | 988 |
| FR | 2227 | 1103 | 1124 |
| CN | 895 | 114 | 781 |
| AU | 732 | 532 | 200 |
| IN | 703 | 360 | 343 |
| JP | 670 | 168 | 502 |
| DE | 597 | 333 | 264 |
| BR | 508 | 253 | 255 |
| ID | 463 | 278 | 185 |
| RU | 457 | 168 | 289 |
| PL | 411 | 171 | 240 |
| KR | 328 | 89 | 239 |
| GB | 288 | 146 | 142 |
| IR | 258 | 83 | 175 |
| CA | 229 | 141 | 88 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10374 |
| `unreachable-dns` | 2813 |
| `fetch-error:ConnectTimeout` | 1087 |
| `http-403` | 903 |
| `fetch-error:ConnectionError` | 875 |
| `fetch-error:SSLError` | 869 |
| `low-confidence:http-2xx-html` | 807 |
| `empty-body` | 189 |
| `fetch-error:ReadTimeout` | 104 |
| `http-500` | 90 |
| `http-404` | 68 |
| `http-503` | 38 |

## Freshness

- Verified in last 30 days: **18501** (96%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2813**
- Moved pointers (old domain → new): **832**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 114/895 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 168/670 (25%) — check for blocks/stale sources
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
