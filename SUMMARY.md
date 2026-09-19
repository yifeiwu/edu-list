# Edu-Domains — Run Summary

_Generated 2026-09-19 21:47 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **3648** across **94** countries
- Active: **2459** (67%) · Inaccessible: **1189** (33%)
- Pending queue: **7900** unvalidated candidates
- Known registration age: **2214** domains (median 28 yrs)

## Last runs

- Verify (2026-09-19 21:47 UTC): validated 118, +60 Active, re-verified 15, pending left 7900
- Curate (2026-09-19 20:17 UTC): 10666 raw candidates, 100 queued, 8 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1716 | 1294 | 422 |
| AU | 346 | 246 | 100 |
| FR | 340 | 207 | 133 |
| BR | 191 | 94 | 97 |
| BE | 81 | 57 | 24 |
| GB | 60 | 36 | 24 |
| CN | 57 | 16 | 41 |
| IN | 56 | 36 | 20 |
| AT | 41 | 35 | 6 |
| AF | 40 | 26 | 14 |
| DE | 40 | 29 | 11 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| AL | 35 | 17 | 18 |
| BG | 34 | 22 | 12 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 2459 |
| `fetch-error:ConnectionError` | 386 |
| `http-403` | 201 |
| `low-confidence:http-2xx-html` | 140 |
| `fetch-error:ConnectTimeout` | 121 |
| `fetch-error:SSLError` | 91 |
| `empty-body` | 26 |
| `http-404` | 11 |
| `fetch-error:ReadTimeout` | 11 |
| `http-500` | 10 |
| `http-503` | 8 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **3648** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **158**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 16/57 (28%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/18 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
