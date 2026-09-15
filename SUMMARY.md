# Edu-Domains — Run Summary

_Generated 2026-09-15 08:05 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1155** across **73** countries
- Active: **746** (65%) · Inaccessible: **409** (35%)
- Pending queue: **390** unvalidated candidates
- Known registration age: **631** domains (median 23 yrs)

## Last runs

- Verify (2026-09-15 08:05 UTC): validated 120, +57 Active, re-verified 15, pending left 390
- Curate (2026-09-15 07:25 UTC): 179 raw candidates, 117 queued, 5 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 381 | 297 | 84 |
| AU | 130 | 92 | 38 |
| FR | 119 | 73 | 46 |
| XX | 88 | 41 | 47 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| AL | 28 | 15 | 13 |
| NG | 27 | 19 | 8 |
| GB | 26 | 15 | 11 |
| IN | 23 | 15 | 8 |
| CN | 20 | 8 | 12 |
| DE | 16 | 9 | 7 |
| RU | 16 | 8 | 8 |
| IR | 15 | 0 | 15 |
| JP | 15 | 5 | 10 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 711 |
| `fetch-error:ConnectionError` | 109 |
| `http-403` | 81 |
| `low-confidence:http-2xx-html` | 52 |
| `fetch-error:ConnectTimeout` | 42 |
| `fetch-error:SSLError` | 28 |
| `empty-body` | 10 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 3 |
| `social-only/placeholder` | 3 |
| `http-500` | 3 |
| `http-405` | 2 |

## Freshness

- Verified in last 30 days: **1155** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **45**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/15 (0%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `XX`: 88 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
