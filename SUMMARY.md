# Edu-Domains — Run Summary

_Generated 2026-09-14 23:01 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **841** across **61** countries
- Active: **545** (65%) · Inaccessible: **296** (35%)
- Pending queue: **455** unvalidated candidates
- Known registration age: **467** domains (median 22 yrs)

## Last runs

- Verify (2026-09-14 19:40 UTC): validated 118, +63 Active, re-verified 15, pending left 325
- Curate (2026-09-14 23:01 UTC): 163 raw candidates, 130 queued, 2 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 288 | 228 | 60 |
| FR | 89 | 58 | 31 |
| AU | 82 | 59 | 23 |
| XX | 63 | 33 | 30 |
| AM | 36 | 21 | 15 |
| AL | 27 | 15 | 12 |
| NG | 27 | 19 | 8 |
| GB | 21 | 11 | 10 |
| IN | 16 | 11 | 5 |
| CN | 15 | 6 | 9 |
| IR | 15 | 0 | 15 |
| CZ | 13 | 2 | 11 |
| RU | 13 | 7 | 6 |
| DE | 11 | 6 | 5 |
| AT | 9 | 6 | 3 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 510 |
| `fetch-error:ConnectionError` | 77 |
| `http-403` | 61 |
| `low-confidence:http-2xx-html` | 36 |
| `fetch-error:ConnectTimeout` | 29 |
| `fetch-error:SSLError` | 21 |
| `empty-body` | 9 |
| `http-503` | 3 |
| `http-500` | 2 |
| `soft-404/block-page` | 2 |
| `social-only/placeholder` | 1 |
| `moved-to:azcu.edu` | 1 |

## Freshness

- Verified in last 30 days: **841** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **30**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/15 (0%) — check for blocks/stale sources
- ⚠ `XX`: 63 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
