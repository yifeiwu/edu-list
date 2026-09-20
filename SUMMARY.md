# Edu-Domains — Run Summary

_Generated 2026-09-20 10:08 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **3958** across **97** countries
- Active: **2632** (66%) · Inaccessible: **1326** (34%)
- Pending queue: **7900** unvalidated candidates
- Known registration age: **2236** domains (median 28 yrs)

## Last runs

- Verify (2026-09-20 10:08 UTC): validated 119, +56 Active, re-verified 15, pending left 7900
- Curate (2026-09-20 05:54 UTC): 10670 raw candidates, 100 queued, 9 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1716 | 1294 | 422 |
| AU | 374 | 256 | 118 |
| FR | 340 | 207 | 133 |
| BR | 191 | 94 | 97 |
| AR | 126 | 90 | 36 |
| BE | 81 | 57 | 24 |
| BD | 80 | 52 | 28 |
| AT | 73 | 48 | 25 |
| GB | 60 | 36 | 24 |
| CN | 57 | 16 | 41 |
| IN | 56 | 36 | 20 |
| AM | 44 | 25 | 19 |
| BY | 44 | 15 | 29 |
| AF | 40 | 26 | 14 |
| DE | 40 | 29 | 11 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 2632 |
| `fetch-error:ConnectionError` | 433 |
| `http-403` | 225 |
| `low-confidence:http-2xx-html` | 145 |
| `fetch-error:ConnectTimeout` | 135 |
| `fetch-error:SSLError` | 108 |
| `empty-body` | 28 |
| `fetch-error:ReadTimeout` | 15 |
| `http-404` | 11 |
| `http-500` | 10 |
| `http-503` | 9 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **3958** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **178**

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
