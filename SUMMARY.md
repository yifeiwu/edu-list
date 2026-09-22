# Edu-Domains — Run Summary

_Generated 2026-09-22 23:23 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **5308** across **121** countries
- Active: **3155** (59%) · Inaccessible: **2153** (41%)
- Pending queue: **7456** unvalidated candidates
- Known registration age: **2657** domains (median 27 yrs)

## Last runs

- Verify (2026-09-22 23:23 UTC): validated 118, +54 Active, re-verified 15, pending left 7456
- Curate (2026-09-22 21:52 UTC): 10699 raw candidates, 45 queued, 26 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1720 | 1296 | 424 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| BR | 343 | 160 | 183 |
| FR | 340 | 208 | 132 |
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
| `http-2xx-html` | 3155 |
| `fetch-error:ConnectionError` | 899 |
| `http-403` | 290 |
| `fetch-error:ConnectTimeout` | 227 |
| `fetch-error:SSLError` | 178 |
| `low-confidence:http-2xx-html` | 174 |
| `empty-body` | 35 |
| `fetch-error:ReadTimeout` | 25 |
| `http-404` | 18 |
| `http-500` | 12 |
| `http-503` | 9 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **5308** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **242**

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
