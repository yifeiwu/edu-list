# Edu-Domains — Run Summary

_Generated 2026-09-24 00:10 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **5972** across **126** countries
- Active: **3421** (57%) · Inaccessible: **2551** (43%)
- Pending queue: **7161** unvalidated candidates
- Known registration age: **2930** domains (median 28 yrs)

## Last runs

- Verify (2026-09-24 00:10 UTC): validated 122, +63 Active, re-verified 15, pending left 7161
- Curate (2026-09-23 23:28 UTC): 10701 raw candidates, 53 queued, 40 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1302 | 424 |
| FR | 619 | 309 | 310 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| DE | 346 | 155 | 191 |
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

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 3421 |
| `fetch-error:ConnectionError` | 1087 |
| `http-403` | 302 |
| `fetch-error:ConnectTimeout` | 274 |
| `fetch-error:SSLError` | 230 |
| `low-confidence:http-2xx-html` | 180 |
| `empty-body` | 39 |
| `fetch-error:ReadTimeout` | 29 |
| `http-404` | 21 |
| `http-500` | 14 |
| `http-503` | 9 |
| `parking-linkfarm` | 9 |

## Freshness

- Verified in last 30 days: **5972** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **316**

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
