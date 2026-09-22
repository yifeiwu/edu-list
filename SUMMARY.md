# Edu-Domains — Run Summary

_Generated 2026-09-22 07:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **4893** across **107** countries
- Active: **2926** (60%) · Inaccessible: **1967** (40%)
- Pending queue: **7651** unvalidated candidates
- Known registration age: **2559** domains (median 28 yrs)

## Last runs

- Verify (2026-09-22 07:53 UTC): validated 116, +21 Active, re-verified 15, pending left 7651
- Curate (2026-09-22 03:57 UTC): 10687 raw candidates, 52 queued, 3046 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1718 | 1294 | 424 |
| CN | 415 | 53 | 362 |
| AU | 374 | 256 | 118 |
| BR | 343 | 160 | 183 |
| FR | 340 | 207 | 133 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| BD | 80 | 52 | 28 |
| AT | 73 | 48 | 25 |
| CL | 65 | 32 | 33 |
| GB | 60 | 36 | 24 |
| BG | 59 | 33 | 26 |
| IN | 56 | 36 | 20 |
| BY | 48 | 15 | 33 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 2926 |
| `fetch-error:ConnectionError` | 816 |
| `http-403` | 272 |
| `fetch-error:ConnectTimeout` | 196 |
| `low-confidence:http-2xx-html` | 166 |
| `fetch-error:SSLError` | 156 |
| `empty-body` | 34 |
| `fetch-error:ReadTimeout` | 22 |
| `http-404` | 18 |
| `http-500` | 11 |
| `http-503` | 9 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **4893** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **225**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/415 (13%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/18 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
