# Edu-Domains — Run Summary

_Generated 2026-09-13 17:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **222** across **31** countries
- Active: **135** (61%) · Inaccessible: **87** (39%)
- Pending queue: **58** unvalidated candidates
- Known registration age: **153** domains (median 23 yrs)

## Last runs

- Verify (2026-09-13 17:11 UTC): validated 123, +53 Active, re-verified 15, pending left 58
- Curate (2026-09-13 13:43 UTC): 184 raw candidates, 158 queued, 16 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 107 | 77 | 30 |
| FR | 17 | 11 | 6 |
| GB | 17 | 9 | 8 |
| RU | 13 | 7 | 6 |
| IN | 11 | 7 | 4 |
| AU | 7 | 1 | 6 |
| XX | 7 | 4 | 3 |
| BR | 6 | 3 | 3 |
| DE | 4 | 1 | 3 |
| CA | 3 | 2 | 1 |
| CN | 3 | 1 | 2 |
| DZ | 3 | 1 | 2 |
| UA | 2 | 1 | 1 |
| GR | 2 | 0 | 2 |
| PL | 2 | 1 | 1 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 100 |
| `http-403` | 18 |
| `fetch-error:ConnectionError` | 18 |
| `fetch-error:ConnectTimeout` | 8 |
| `low-confidence:http-2xx-html` | 7 |
| `fetch-error:SSLError` | 4 |
| `moved-to:kean.edu` | 1 |
| `moved-to:royalholloway.ac.uk` | 1 |
| `moved-to:upmc.com` | 1 |
| `moved-to:noah-495.cloudflareaccess.com` | 1 |
| `moved-to:uno.edu.br` | 1 |
| `moved-to:priem.nevskyinstitute.ru` | 1 |

## Freshness

- Verified in last 30 days: **222** (100%)
- Older than 90 days: **0** (oldest check 2026-09-13)
- Archived chronic failures (re-check paused): **0**
- Moved pointers (old domain → new): **11**

## Alerts

- ⚠ `AU`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `AU`: 5/7 blocked (403/429/block-page) — suspected bot-block, verify manually
- ⚠ `XX`: 7 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify hourly at :30 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
