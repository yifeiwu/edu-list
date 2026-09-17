# Edu-Domains — Run Summary

_Generated 2026-09-17 21:57 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2408** across **88** countries
- Active: **1589** (66%) · Inaccessible: **819** (34%)
- Pending queue: **8000** unvalidated candidates
- Known registration age: **1338** domains (median 24 yrs)

## Last runs

- Verify (2026-09-17 21:44 UTC): validated 122, +68 Active, re-verified 15, pending left 7900
- Curate (2026-09-17 21:57 UTC): 10691 raw candidates, 100 queued, 2 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 870 | 664 | 206 |
| AU | 286 | 204 | 82 |
| FR | 282 | 170 | 112 |
| BR | 121 | 57 | 64 |
| BE | 81 | 57 | 24 |
| IN | 56 | 36 | 20 |
| GB | 55 | 33 | 22 |
| CN | 50 | 15 | 35 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| DE | 34 | 24 | 10 |
| CH | 33 | 23 | 10 |
| AL | 28 | 15 | 13 |
| BA | 27 | 14 | 13 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1567 |
| `fetch-error:ConnectionError` | 226 |
| `http-403` | 153 |
| `low-confidence:http-2xx-html` | 121 |
| `fetch-error:ConnectTimeout` | 78 |
| `fetch-error:SSLError` | 59 |
| `empty-body` | 19 |
| `http-500` | 9 |
| `http-404` | 8 |
| `fetch-error:ReadTimeout` | 8 |
| `http-503` | 7 |
| `social-only/placeholder` | 4 |

## Freshness

- Verified in last 30 days: **2408** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **104**

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
