# Edu-Domains — Run Summary

_Generated 2026-09-18 00:49 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2511** across **88** countries
- Active: **1662** (66%) · Inaccessible: **849** (34%)
- Pending queue: **7900** unvalidated candidates
- Known registration age: **1400** domains (median 24 yrs)

## Last runs

- Verify (2026-09-18 00:49 UTC): validated 118, +73 Active, re-verified 15, pending left 7900
- Curate (2026-09-18 00:04 UTC): 10692 raw candidates, 0 queued, 849 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 910 | 696 | 214 |
| AU | 301 | 215 | 86 |
| FR | 297 | 180 | 117 |
| BR | 139 | 67 | 72 |
| BE | 81 | 57 | 24 |
| GB | 56 | 34 | 22 |
| IN | 56 | 36 | 20 |
| CN | 54 | 16 | 38 |
| AT | 41 | 35 | 6 |
| DE | 38 | 27 | 11 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| CH | 33 | 23 | 10 |
| AL | 28 | 15 | 13 |
| BA | 27 | 14 | 13 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1641 |
| `fetch-error:ConnectionError` | 238 |
| `http-403` | 156 |
| `low-confidence:http-2xx-html` | 124 |
| `fetch-error:ConnectTimeout` | 81 |
| `fetch-error:SSLError` | 61 |
| `empty-body` | 22 |
| `http-500` | 9 |
| `http-404` | 8 |
| `fetch-error:ReadTimeout` | 8 |
| `http-503` | 8 |
| `social-only/placeholder` | 5 |

## Freshness

- Verified in last 30 days: **2511** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **107**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 16/54 (30%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 1/17 (6%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/18 (28%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
