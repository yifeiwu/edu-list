# Edu-Domains — Run Summary

_Generated 2026-09-13 11:04 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **114** across **11** countries
- Active: **81** (71%) · Inaccessible: **33** (29%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **100** domains (median 26.5 yrs)

## Last runs

- Verify (2026-09-13 11:04 UTC): validated 60, +0 Active, re-verified 60, pending left 0

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 86 | 68 | 18 |
| IN | 8 | 4 | 4 |
| FR | 6 | 2 | 4 |
| GB | 4 | 2 | 2 |
| BR | 2 | 0 | 2 |
| CN | 2 | 1 | 1 |
| UA | 2 | 1 | 1 |
| AE | 1 | 0 | 1 |
| CA | 1 | 1 | 0 |
| CL | 1 | 1 | 0 |
| UG | 1 | 1 | 0 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 45 |
| `fetch-error:ConnectionError` | 4 |
| `http-403` | 3 |
| `fetch-error:ConnectTimeout` | 2 |
| `fetch-error:SSLError` | 2 |
| `moved-to:upmc.com` | 1 |
| `low-confidence:http-2xx-html` | 1 |
| `moved-to:royalholloway.ac.uk` | 1 |
| `moved-to:kean.edu` | 1 |

## Freshness

- Verified in last 30 days: **114** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **3**

## Alerts

- No alerts.

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
