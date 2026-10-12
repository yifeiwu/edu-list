# Edu-Domains — Run Summary

_Generated 2026-10-12 17:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15191** across **204** countries
- Active: **8202** (54%) · Inaccessible: **6989** (46%)
- Pending queue: **2998** unvalidated candidates
- Known registration age: **6635** domains (median 24 yrs)

## Last runs

- Verify (2026-10-12 09:56 UTC): validated 116, +67 Active, re-verified 15, pending left 2949
- Curate (2026-10-12 17:31 UTC): 10696 raw candidates, 49 queued, 27 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3216 | 2414 | 802 |
| FR | 1405 | 726 | 679 |
| AU | 628 | 446 | 182 |
| JP | 619 | 142 | 477 |
| IN | 613 | 308 | 305 |
| DE | 586 | 326 | 260 |
| CN | 504 | 64 | 440 |
| BR | 478 | 229 | 249 |
| RU | 406 | 136 | 270 |
| KR | 306 | 84 | 222 |
| GB | 271 | 135 | 136 |
| ID | 269 | 159 | 110 |
| IR | 237 | 73 | 164 |
| CA | 210 | 124 | 86 |
| TR | 203 | 137 | 66 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8204 |
| `unreachable-dns` | 2438 |
| `fetch-error:ConnectTimeout` | 850 |
| `http-403` | 732 |
| `fetch-error:SSLError` | 684 |
| `fetch-error:ConnectionError` | 610 |
| `low-confidence:http-2xx-html` | 499 |
| `empty-body` | 157 |
| `fetch-error:ReadTimeout` | 82 |
| `http-500` | 46 |
| `http-404` | 42 |
| `http-503` | 29 |

## Freshness

- Verified in last 30 days: **15191** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2438**
- Moved pointers (old domain → new): **689**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 64/504 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 142/619 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 84/306 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 12/101 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 7 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
