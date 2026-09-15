# Edu-Domains — Run Summary

_Generated 2026-09-15 18:02 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1257** across **76** countries
- Active: **822** (65%) · Inaccessible: **435** (35%)
- Pending queue: **529** unvalidated candidates
- Known registration age: **695** domains (median 23 yrs)

## Last runs

- Verify (2026-09-15 13:55 UTC): validated 117, +76 Active, re-verified 15, pending left 413
- Curate (2026-09-15 18:02 UTC): 175 raw candidates, 116 queued, 4 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 438 | 339 | 99 |
| FR | 134 | 82 | 52 |
| AU | 130 | 92 | 38 |
| XX | 89 | 42 | 47 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| AL | 28 | 15 | 13 |
| GB | 27 | 16 | 11 |
| NG | 27 | 19 | 8 |
| IN | 23 | 15 | 8 |
| CN | 22 | 9 | 13 |
| RU | 17 | 8 | 9 |
| DE | 16 | 9 | 7 |
| BR | 15 | 9 | 6 |
| IR | 15 | 0 | 15 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 787 |
| `fetch-error:ConnectionError` | 115 |
| `http-403` | 86 |
| `low-confidence:http-2xx-html` | 56 |
| `fetch-error:ConnectTimeout` | 46 |
| `fetch-error:SSLError` | 32 |
| `empty-body` | 10 |
| `http-503` | 5 |
| `http-500` | 4 |
| `fetch-error:ReadTimeout` | 3 |
| `social-only/placeholder` | 3 |
| `http-405` | 2 |

## Freshness

- Verified in last 30 days: **1257** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **47**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/15 (0%) — check for blocks/stale sources
- ⚠ `PH`: 2/6 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `SD`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `XX`: 89 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
