# Edu-Domains — Run Summary

_Generated 2026-09-24 22:33 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **6487** across **138** countries
- Active: **3661** (56%) · Inaccessible: **2826** (44%)
- Pending queue: **6949** unvalidated candidates
- Known registration age: **3303** domains (median 26 yrs)

## Last runs

- Verify (2026-09-24 22:33 UTC): validated 118, +50 Active, re-verified 15, pending left 6949
- Curate (2026-09-24 22:06 UTC): 10699 raw candidates, 62 queued, 24 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1302 | 424 |
| FR | 619 | 308 | 311 |
| IN | 421 | 197 | 224 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| DE | 346 | 155 | 191 |
| BR | 343 | 160 | 183 |
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
| `http-2xx-html` | 3661 |
| `fetch-error:ConnectionError` | 1205 |
| `fetch-error:ConnectTimeout` | 320 |
| `http-403` | 318 |
| `fetch-error:SSLError` | 262 |
| `low-confidence:http-2xx-html` | 195 |
| `empty-body` | 50 |
| `fetch-error:ReadTimeout` | 32 |
| `http-404` | 23 |
| `http-500` | 16 |
| `parking-linkfarm` | 11 |
| `http-503` | 10 |

## Freshness

- Verified in last 30 days: **6487** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **334**

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
