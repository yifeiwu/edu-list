# Edu-Domains — Run Summary

_Generated 2026-09-21 10:31 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **4278** across **105** countries
- Active: **2767** (65%) · Inaccessible: **1511** (35%)
- Pending queue: **8000** unvalidated candidates
- Known registration age: **2412** domains (median 28 yrs)

## Last runs

- Verify (2026-09-20 21:08 UTC): validated 123, +48 Active, re-verified 15, pending left 7900
- Curate (2026-09-21 10:31 UTC): 10659 raw candidates, 0 queued, 2533 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1716 | 1293 | 423 |
| AU | 374 | 256 | 118 |
| BR | 343 | 160 | 183 |
| FR | 340 | 207 | 133 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| BD | 80 | 52 | 28 |
| AT | 73 | 48 | 25 |
| GB | 60 | 36 | 24 |
| BG | 59 | 33 | 26 |
| CN | 57 | 16 | 41 |
| IN | 56 | 36 | 20 |
| BY | 48 | 15 | 33 |
| AM | 44 | 25 | 19 |
| AF | 40 | 26 | 14 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 2767 |
| `fetch-error:ConnectionError` | 515 |
| `http-403` | 247 |
| `fetch-error:ConnectTimeout` | 150 |
| `low-confidence:http-2xx-html` | 149 |
| `fetch-error:SSLError` | 134 |
| `empty-body` | 29 |
| `fetch-error:ReadTimeout` | 17 |
| `http-404` | 13 |
| `http-500` | 10 |
| `http-503` | 9 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **4278** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **205**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CM`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 16/57 (28%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/18 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
