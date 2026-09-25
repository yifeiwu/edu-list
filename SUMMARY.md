# Edu-Domains — Run Summary

_Generated 2026-09-25 01:15 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **6590** across **138** countries
- Active: **3714** (56%) · Inaccessible: **2876** (44%)
- Pending queue: **6902** unvalidated candidates
- Known registration age: **3399** domains (median 26 yrs)

## Last runs

- Verify (2026-09-25 01:02 UTC): validated 118, +53 Active, re-verified 15, pending left 6849
- Curate (2026-09-25 01:15 UTC): 10698 raw candidates, 53 queued, 4782 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1301 | 425 |
| FR | 619 | 308 | 311 |
| IN | 457 | 207 | 250 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| CO | 105 | 59 | 46 |
| ID | 100 | 59 | 41 |
| BD | 80 | 52 | 28 |
| AT | 73 | 47 | 26 |
| CL | 65 | 32 | 33 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 3714 |
| `fetch-error:ConnectionError` | 1220 |
| `http-403` | 329 |
| `fetch-error:ConnectTimeout` | 324 |
| `fetch-error:SSLError` | 269 |
| `low-confidence:http-2xx-html` | 197 |
| `empty-body` | 53 |
| `fetch-error:ReadTimeout` | 33 |
| `http-404` | 23 |
| `http-500` | 16 |
| `parking-linkfarm` | 11 |
| `http-503` | 10 |

## Freshness

- Verified in last 30 days: **6590** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **337**

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
