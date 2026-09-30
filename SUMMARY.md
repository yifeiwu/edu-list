# Edu-Domains — Run Summary

_Generated 2026-09-30 22:51 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **9687** across **178** countries
- Active: **4922** (51%) · Inaccessible: **4765** (49%)
- Pending queue: **5569** unvalidated candidates
- Known registration age: **4155** domains (median 26 yrs)

## Last runs

- Verify (2026-09-30 22:26 UTC): validated 117, +29 Active, re-verified 15, pending left 5498
- Curate (2026-09-30 22:51 UTC): 10695 raw candidates, 71 queued, 22 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1729 | 1300 | 429 |
| FR | 619 | 311 | 308 |
| JP | 577 | 125 | 452 |
| IN | 458 | 207 | 251 |
| CN | 415 | 52 | 363 |
| AU | 375 | 257 | 118 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| KR | 278 | 73 | 205 |
| RU | 233 | 69 | 164 |
| ID | 224 | 129 | 95 |
| IR | 212 | 69 | 143 |
| CA | 174 | 95 | 79 |
| MX | 174 | 77 | 97 |
| PL | 154 | 66 | 88 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4924 |
| `fetch-error:ConnectionError` | 2182 |
| `fetch-error:ConnectTimeout` | 598 |
| `http-403` | 484 |
| `fetch-error:SSLError` | 468 |
| `low-confidence:http-2xx-html` | 294 |
| `empty-body` | 91 |
| `fetch-error:ReadTimeout` | 51 |
| `http-404` | 32 |
| `http-500` | 20 |
| `parking-linkfarm` | 15 |
| `http-503` | 13 |

## Freshness

- Verified in last 30 days: **9687** (100%)
- Older than 90 days: **0** (oldest check 2026-09-15)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **443**

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
- ⚠ `RU`: low Active rate 69/233 (30%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
