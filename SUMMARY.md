# Edu-Domains — Run Summary

_Generated 2026-09-17 11:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2198** across **86** countries
- Active: **1454** (66%) · Inaccessible: **744** (34%)
- Pending queue: **665** unvalidated candidates
- Known registration age: **1215** domains (median 24 yrs)

## Last runs

- Verify (2026-09-17 06:39 UTC): validated 119, +56 Active, re-verified 15, pending left 555
- Curate (2026-09-17 07:21 UTC): 179 raw candidates, 110 queued, 9 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 811 | 615 | 196 |
| AU | 254 | 184 | 70 |
| FR | 254 | 154 | 100 |
| BR | 89 | 41 | 48 |
| BE | 81 | 57 | 24 |
| IN | 55 | 36 | 19 |
| CN | 48 | 15 | 33 |
| GB | 44 | 29 | 15 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| CH | 33 | 23 | 10 |
| DE | 30 | 20 | 10 |
| AL | 28 | 15 | 13 |
| BY | 23 | 12 | 11 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1428 |
| `fetch-error:ConnectionError` | 204 |
| `http-403` | 140 |
| `low-confidence:http-2xx-html` | 111 |
| `fetch-error:ConnectTimeout` | 72 |
| `fetch-error:SSLError` | 51 |
| `empty-body` | 18 |
| `http-500` | 8 |
| `http-404` | 7 |
| `fetch-error:ReadTimeout` | 6 |
| `http-503` | 6 |
| `social-only/placeholder` | 3 |

## Freshness

- Verified in last 30 days: **2198** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **93**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
