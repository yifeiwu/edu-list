# Edu-Domains — Run Summary

_Generated 2026-09-17 00:54 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2094** across **84** countries
- Active: **1398** (67%) · Inaccessible: **696** (33%)
- Pending queue: **539** unvalidated candidates
- Known registration age: **1153** domains (median 24 yrs)

## Last runs

- Verify (2026-09-17 00:54 UTC): validated 123, +73 Active, re-verified 15, pending left 539
- Curate (2026-09-16 22:43 UTC): 178 raw candidates, 124 queued, 13 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 757 | 577 | 180 |
| AU | 239 | 176 | 63 |
| FR | 229 | 140 | 89 |
| XX | 92 | 41 | 51 |
| BE | 77 | 56 | 21 |
| BR | 66 | 34 | 32 |
| IN | 43 | 29 | 14 |
| AT | 41 | 35 | 6 |
| CN | 39 | 14 | 25 |
| GB | 39 | 27 | 12 |
| AM | 36 | 21 | 15 |
| CH | 32 | 22 | 10 |
| DE | 30 | 20 | 10 |
| AL | 28 | 15 | 13 |
| NG | 27 | 19 | 8 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1367 |
| `fetch-error:ConnectionError` | 187 |
| `http-403` | 133 |
| `low-confidence:http-2xx-html` | 101 |
| `fetch-error:ConnectTimeout` | 70 |
| `fetch-error:SSLError` | 50 |
| `empty-body` | 16 |
| `http-500` | 7 |
| `http-404` | 6 |
| `http-503` | 5 |
| `fetch-error:ReadTimeout` | 4 |
| `social-only/placeholder` | 3 |

## Freshness

- Verified in last 30 days: **2094** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **87**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `PH`: 4/13 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `XX`: 92 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
