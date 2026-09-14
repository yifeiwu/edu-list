# Edu-Domains — Run Summary

_Generated 2026-09-14 00:57 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **428** across **48** countries
- Active: **265** (62%) · Inaccessible: **163** (38%)
- Pending queue: **314** unvalidated candidates
- Known registration age: **245** domains (median 22 yrs)

## Last runs

- Verify (2026-09-13 22:41 UTC): validated 118, +67 Active, re-verified 15, pending left 71
- Curate (2026-09-13 23:00 UTC): 177 raw candidates, 118 queued, 27 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 152 | 114 | 38 |
| AU | 32 | 21 | 11 |
| FR | 29 | 18 | 11 |
| AL | 27 | 16 | 11 |
| XX | 24 | 13 | 11 |
| NG | 21 | 14 | 7 |
| GB | 19 | 10 | 9 |
| RU | 13 | 7 | 6 |
| CZ | 12 | 2 | 10 |
| IN | 12 | 8 | 4 |
| CN | 10 | 3 | 7 |
| DE | 7 | 2 | 5 |
| BR | 6 | 3 | 3 |
| BJ | 5 | 3 | 2 |
| CA | 5 | 4 | 1 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 230 |
| `http-403` | 36 |
| `fetch-error:ConnectionError` | 34 |
| `low-confidence:http-2xx-html` | 20 |
| `fetch-error:ConnectTimeout` | 17 |
| `fetch-error:SSLError` | 7 |
| `empty-body` | 7 |
| `http-503` | 2 |
| `moved-to:brooklynadultlearning.center` | 1 |
| `parking-linkfarm` | 1 |
| `moved-meta:bundesfinanzministerium.de` | 1 |
| `moved-to:ccsdschools.com` | 1 |

## Freshness

- Verified in last 30 days: **428** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **17**

## Alerts

- ⚠ `CZ`: low Active rate 2/12 (17%) — check for blocks/stale sources
- ⚠ `DE`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 24 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
