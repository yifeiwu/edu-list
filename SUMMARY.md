# Edu-Domains — Run Summary

_Generated 2026-09-24 18:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **6282** across **138** countries
- Active: **3570** (57%) · Inaccessible: **2712** (43%)
- Pending queue: **7087** unvalidated candidates
- Known registration age: **3118** domains (median 27 yrs)

## Last runs

- Verify (2026-09-24 15:17 UTC): validated 118, +54 Active, re-verified 15, pending left 7028
- Curate (2026-09-24 18:52 UTC): 10700 raw candidates, 59 queued, 30 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1302 | 424 |
| FR | 619 | 309 | 310 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| DE | 346 | 155 | 191 |
| BR | 343 | 160 | 183 |
| IN | 216 | 105 | 111 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| CO | 105 | 59 | 46 |
| BD | 80 | 52 | 28 |
| AT | 73 | 47 | 26 |
| CL | 65 | 32 | 33 |
| GB | 60 | 36 | 24 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 3570 |
| `fetch-error:ConnectionError` | 1157 |
| `http-403` | 310 |
| `fetch-error:ConnectTimeout` | 295 |
| `fetch-error:SSLError` | 250 |
| `low-confidence:http-2xx-html` | 189 |
| `empty-body` | 46 |
| `fetch-error:ReadTimeout` | 31 |
| `http-404` | 23 |
| `http-500` | 15 |
| `http-503` | 10 |
| `parking-linkfarm` | 10 |

## Freshness

- Verified in last 30 days: **6282** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **329**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/19 (5%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
