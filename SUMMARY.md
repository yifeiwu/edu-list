# Edu-Domains — Run Summary

_Generated 2026-09-18 10:47 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2614** across **89** countries
- Active: **1730** (66%) · Inaccessible: **884** (34%)
- Pending queue: **8000** unvalidated candidates
- Known registration age: **1481** domains (median 24 yrs)

## Last runs

- Verify (2026-09-18 06:35 UTC): validated 118, +68 Active, re-verified 15, pending left 7899
- Curate (2026-09-18 10:47 UTC): 10686 raw candidates, 101 queued, 11 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 959 | 736 | 223 |
| FR | 309 | 187 | 122 |
| AU | 303 | 215 | 88 |
| BR | 155 | 75 | 80 |
| BE | 81 | 57 | 24 |
| GB | 57 | 35 | 22 |
| IN | 56 | 36 | 20 |
| CN | 55 | 16 | 39 |
| AT | 41 | 35 | 6 |
| DE | 38 | 27 | 11 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| CH | 33 | 23 | 10 |
| ID | 33 | 16 | 17 |
| AL | 28 | 15 | 13 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1712 |
| `fetch-error:ConnectionError` | 247 |
| `http-403` | 162 |
| `low-confidence:http-2xx-html` | 129 |
| `fetch-error:ConnectTimeout` | 87 |
| `fetch-error:SSLError` | 66 |
| `empty-body` | 22 |
| `http-404` | 9 |
| `http-500` | 9 |
| `fetch-error:ReadTimeout` | 8 |
| `http-503` | 8 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **2614** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **110**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 16/55 (29%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/17 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/18 (28%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
