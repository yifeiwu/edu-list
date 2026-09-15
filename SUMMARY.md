# Edu-Domains — Run Summary

_Generated 2026-09-15 18:30 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **1358** across **78** countries
- Active: **893** (66%) · Inaccessible: **465** (34%)
- Pending queue: **429** unvalidated candidates
- Known registration age: **745** domains (median 24 yrs)

## Last runs

- Verify (2026-09-15 18:30 UTC): validated 116, +71 Active, re-verified 15, pending left 429
- Curate (2026-09-15 18:02 UTC): 175 raw candidates, 116 queued, 4 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 480 | 373 | 107 |
| AU | 146 | 104 | 42 |
| FR | 134 | 82 | 52 |
| XX | 92 | 42 | 50 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| GB | 31 | 20 | 11 |
| AL | 28 | 15 | 13 |
| NG | 27 | 19 | 8 |
| CN | 26 | 11 | 15 |
| IN | 24 | 16 | 8 |
| DE | 17 | 10 | 7 |
| RU | 17 | 8 | 9 |
| IR | 16 | 0 | 16 |
| BR | 15 | 9 | 6 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 858 |
| `fetch-error:ConnectionError` | 120 |
| `http-403` | 97 |
| `low-confidence:http-2xx-html` | 59 |
| `fetch-error:ConnectTimeout` | 49 |
| `fetch-error:SSLError` | 35 |
| `empty-body` | 14 |
| `http-503` | 5 |
| `http-500` | 4 |
| `fetch-error:ReadTimeout` | 3 |
| `social-only/placeholder` | 3 |
| `http-405` | 2 |

## Freshness

- Verified in last 30 days: **1358** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **48**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `PH`: 4/12 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `XX`: 92 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
