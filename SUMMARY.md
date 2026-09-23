# Edu-Domains — Run Summary

_Generated 2026-09-23 16:24 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **5632** across **126** countries
- Active: **3275** (58%) · Inaccessible: **2357** (42%)
- Pending queue: **7354** unvalidated candidates
- Known registration age: **2917** domains (median 28 yrs)

## Last runs

- Verify (2026-09-23 13:12 UTC): validated 123, +41 Active, re-verified 15, pending left 7303
- Curate (2026-09-23 16:24 UTC): 10701 raw candidates, 51 queued, 37 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1724 | 1300 | 424 |
| FR | 619 | 308 | 311 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| BR | 343 | 160 | 183 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| CO | 105 | 59 | 46 |
| BD | 80 | 52 | 28 |
| AT | 73 | 48 | 25 |
| CL | 65 | 32 | 33 |
| GB | 60 | 36 | 24 |
| BG | 59 | 33 | 26 |
| IN | 56 | 36 | 20 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 3275 |
| `fetch-error:ConnectionError` | 1016 |
| `http-403` | 293 |
| `fetch-error:ConnectTimeout` | 250 |
| `fetch-error:SSLError` | 198 |
| `low-confidence:http-2xx-html` | 180 |
| `empty-body` | 38 |
| `fetch-error:ReadTimeout` | 29 |
| `http-404` | 19 |
| `http-500` | 14 |
| `http-503` | 9 |
| `parking-linkfarm` | 6 |

## Freshness

- Verified in last 30 days: **5632** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **266**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/19 (5%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
