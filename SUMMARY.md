# Edu-Domains — Run Summary

_Generated 2026-09-29 15:57 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **9052** across **176** countries
- Active: **4666** (52%) · Inaccessible: **4386** (48%)
- Pending queue: **5829** unvalidated candidates
- Known registration age: **4047** domains (median 26 yrs)

## Last runs

- Verify (2026-09-29 15:57 UTC): validated 119, +54 Active, re-verified 15, pending left 5829
- Curate (2026-09-29 15:29 UTC): 10696 raw candidates, 61 queued, 32 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1729 | 1300 | 429 |
| FR | 619 | 309 | 310 |
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
| MY | 145 | 54 | 91 |
| NG | 143 | 76 | 67 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4666 |
| `fetch-error:ConnectionError` | 2031 |
| `fetch-error:ConnectTimeout` | 533 |
| `http-403` | 460 |
| `fetch-error:SSLError` | 410 |
| `low-confidence:http-2xx-html` | 268 |
| `empty-body` | 84 |
| `fetch-error:ReadTimeout` | 48 |
| `http-404` | 31 |
| `http-500` | 19 |
| `parking-linkfarm` | 15 |
| `http-503` | 13 |

## Freshness

- Verified in last 30 days: **9052** (100%)
- Older than 90 days: **0** (oldest check 2026-09-15)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **405**

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
