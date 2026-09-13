# Edu-Domains — Run Summary

_Generated 2026-09-13 19:53 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **325** across **40** countries
- Active: **197** (61%) · Inaccessible: **128** (39%)
- Pending queue: **74** unvalidated candidates
- Known registration age: **190** domains (median 24 yrs)

## Last runs

- Verify (2026-09-13 19:53 UTC): validated 118, +63 Active, re-verified 15, pending left 74
- Curate (2026-09-13 17:20 UTC): 178 raw candidates, 116 queued, 26 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 126 | 93 | 33 |
| NG | 21 | 13 | 8 |
| FR | 19 | 13 | 6 |
| GB | 18 | 10 | 8 |
| AU | 17 | 10 | 7 |
| AL | 15 | 11 | 4 |
| RU | 13 | 7 | 6 |
| CZ | 12 | 2 | 10 |
| IN | 11 | 7 | 4 |
| CN | 9 | 3 | 6 |
| XX | 7 | 4 | 3 |
| BR | 6 | 3 | 3 |
| DE | 6 | 1 | 5 |
| CA | 5 | 4 | 1 |
| BI | 4 | 0 | 4 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 162 |
| `fetch-error:ConnectionError` | 28 |
| `http-403` | 26 |
| `low-confidence:http-2xx-html` | 14 |
| `fetch-error:ConnectTimeout` | 12 |
| `fetch-error:SSLError` | 6 |
| `empty-body` | 3 |
| `http-503` | 2 |
| `moved-meta:bundesfinanzministerium.de` | 1 |
| `moved-to:ccsdschools.com` | 1 |
| `moved-to:clackesd.org` | 1 |
| `soft-404/block-page` | 1 |

## Freshness

- Verified in last 30 days: **325** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **14**

## Alerts

- ⚠ `CZ`: low Active rate 2/12 (17%) — check for blocks/stale sources
- ⚠ `DE`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `XX`: 7 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
