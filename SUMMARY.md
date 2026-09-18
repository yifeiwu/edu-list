# Edu-Domains — Run Summary

_Generated 2026-09-18 14:49 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2720** across **91** countries
- Active: **1806** (66%) · Inaccessible: **914** (34%)
- Pending queue: **8000** unvalidated candidates
- Known registration age: **1558** domains (median 25 yrs)

## Last runs

- Verify (2026-09-18 11:48 UTC): validated 121, +76 Active, re-verified 15, pending left 7900
- Curate (2026-09-18 14:49 UTC): 10684 raw candidates, 100 queued, 1 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1014 | 778 | 236 |
| AU | 318 | 226 | 92 |
| FR | 310 | 188 | 122 |
| BR | 176 | 89 | 87 |
| BE | 81 | 57 | 24 |
| GB | 58 | 35 | 23 |
| IN | 56 | 36 | 20 |
| CN | 55 | 16 | 39 |
| AT | 41 | 35 | 6 |
| DE | 39 | 28 | 11 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| CH | 33 | 23 | 10 |
| ID | 33 | 16 | 17 |
| AL | 28 | 15 | 13 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1788 |
| `fetch-error:ConnectionError` | 254 |
| `http-403` | 171 |
| `low-confidence:http-2xx-html` | 129 |
| `fetch-error:ConnectTimeout` | 89 |
| `fetch-error:SSLError` | 69 |
| `empty-body` | 22 |
| `http-404` | 9 |
| `fetch-error:ReadTimeout` | 9 |
| `http-500` | 9 |
| `http-503` | 8 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **2720** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **117**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 16/55 (29%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/18 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/19 (26%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
