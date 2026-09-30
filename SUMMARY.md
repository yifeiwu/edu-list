# Edu-Domains — Run Summary

_Generated 2026-09-30 13:25 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **9481** across **178** countries
- Active: **4864** (51%) · Inaccessible: **4617** (49%)
- Pending queue: **5641** unvalidated candidates
- Known registration age: **4145** domains (median 26 yrs)

## Last runs

- Verify (2026-09-30 12:50 UTC): validated 121, +58 Active, re-verified 15, pending left 5581
- Curate (2026-09-30 13:25 UTC): 10698 raw candidates, 60 queued, 28 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1729 | 1300 | 429 |
| FR | 619 | 310 | 309 |
| JP | 577 | 125 | 452 |
| IN | 458 | 208 | 250 |
| CN | 415 | 52 | 363 |
| AU | 375 | 257 | 118 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| KR | 278 | 73 | 205 |
| ID | 224 | 129 | 95 |
| IR | 212 | 69 | 143 |
| CA | 174 | 95 | 79 |
| MX | 174 | 77 | 97 |
| PL | 154 | 66 | 88 |
| MY | 145 | 54 | 91 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4866 |
| `fetch-error:ConnectionError` | 2114 |
| `fetch-error:ConnectTimeout` | 565 |
| `http-403` | 477 |
| `fetch-error:SSLError` | 445 |
| `low-confidence:http-2xx-html` | 282 |
| `empty-body` | 91 |
| `fetch-error:ReadTimeout` | 51 |
| `http-404` | 32 |
| `http-500` | 20 |
| `parking-linkfarm` | 15 |
| `http-503` | 14 |

## Freshness

- Verified in last 30 days: **9481** (100%)
- Older than 90 days: **0** (oldest check 2026-09-15)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **437**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 52/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 125/577 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 73/278 (26%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
