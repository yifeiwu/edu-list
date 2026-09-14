# Edu-Domains — Run Summary

_Generated 2026-09-14 06:01 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **532** across **51** countries
- Active: **344** (65%) · Inaccessible: **188** (35%)
- Pending queue: **354** unvalidated candidates
- Known registration age: **304** domains (median 22.5 yrs)

## Last runs

- Verify (2026-09-14 01:34 UTC): validated 119, +79 Active, re-verified 15, pending left 214
- Curate (2026-09-14 00:57 UTC): 176 raw candidates, 125 queued, 29 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 189 | 147 | 42 |
| AU | 49 | 32 | 17 |
| FR | 44 | 28 | 16 |
| XX | 36 | 19 | 17 |
| AL | 27 | 16 | 11 |
| NG | 21 | 14 | 7 |
| GB | 20 | 11 | 9 |
| AM | 16 | 12 | 4 |
| RU | 13 | 7 | 6 |
| CZ | 12 | 2 | 10 |
| IN | 12 | 8 | 4 |
| CN | 10 | 3 | 7 |
| DE | 8 | 3 | 5 |
| BR | 6 | 3 | 3 |
| BJ | 5 | 3 | 2 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 309 |
| `http-403` | 41 |
| `fetch-error:ConnectionError` | 40 |
| `low-confidence:http-2xx-html` | 26 |
| `fetch-error:ConnectTimeout` | 19 |
| `fetch-error:SSLError` | 8 |
| `empty-body` | 7 |
| `http-503` | 2 |
| `moved-to:brooklynadultlearning.center` | 1 |
| `parking-linkfarm` | 1 |
| `moved-meta:bundesfinanzministerium.de` | 1 |
| `moved-to:biolabet3.com` | 1 |

## Freshness

- Verified in last 30 days: **532** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **21**

## Alerts

- ⚠ `CZ`: low Active rate 2/12 (17%) — check for blocks/stale sources
- ⚠ `XX`: 36 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
