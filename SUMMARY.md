# Edu-Domains — Run Summary

_Generated 2026-09-17 17:50 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **2301** across **87** countries
- Active: **1520** (66%) · Inaccessible: **781** (34%)
- Pending queue: **7900** unvalidated candidates
- Known registration age: **1269** domains (median 24 yrs)

## Last runs

- Verify (2026-09-17 17:50 UTC): validated 118, +67 Active, re-verified 15, pending left 7900
- Curate (2026-09-17 13:11 UTC): 10692 raw candidates, 7335 queued, 763 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 843 | 641 | 202 |
| FR | 269 | 163 | 106 |
| AU | 268 | 193 | 75 |
| BR | 98 | 45 | 53 |
| BE | 81 | 57 | 24 |
| IN | 56 | 36 | 20 |
| CN | 50 | 15 | 35 |
| GB | 45 | 29 | 16 |
| AT | 41 | 35 | 6 |
| AM | 36 | 21 | 15 |
| NG | 36 | 23 | 13 |
| CH | 33 | 23 | 10 |
| DE | 32 | 22 | 10 |
| AL | 28 | 15 | 13 |
| BA | 27 | 14 | 13 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 1497 |
| `fetch-error:ConnectionError` | 218 |
| `http-403` | 147 |
| `low-confidence:http-2xx-html` | 115 |
| `fetch-error:ConnectTimeout` | 74 |
| `fetch-error:SSLError` | 54 |
| `empty-body` | 18 |
| `http-500` | 9 |
| `http-404` | 8 |
| `fetch-error:ReadTimeout` | 7 |
| `http-503` | 7 |
| `social-only/placeholder` | 4 |

## Freshness

- Verified in last 30 days: **2301** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **96**

## Alerts

- ⚠ `CD`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CZ`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `EG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `IR`: low Active rate 0/16 (0%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
