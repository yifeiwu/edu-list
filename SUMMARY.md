# Edu-Domains — Run Summary

_Generated 2026-10-06 07:40 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12378** across **203** countries
- Active: **6543** (53%) · Inaccessible: **5835** (47%)
- Pending queue: **4269** unvalidated candidates
- Known registration age: **5359** domains (median 24 yrs)

## Last runs

- Verify (2026-10-06 07:40 UTC): validated 122, +76 Active, re-verified 15, pending left 4269
- Curate (2026-10-06 07:19 UTC): 10700 raw candidates, 55 queued, 44 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2700 | 2037 | 663 |
| FR | 646 | 326 | 320 |
| JP | 580 | 125 | 455 |
| IN | 507 | 248 | 259 |
| CN | 425 | 53 | 372 |
| DE | 385 | 182 | 203 |
| AU | 382 | 263 | 119 |
| BR | 356 | 166 | 190 |
| RU | 336 | 108 | 228 |
| KR | 278 | 73 | 205 |
| GB | 246 | 119 | 127 |
| ID | 227 | 132 | 95 |
| IR | 212 | 69 | 143 |
| TR | 199 | 136 | 63 |
| CA | 184 | 103 | 81 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6545 |
| `fetch-error:ConnectionError` | 2673 |
| `fetch-error:ConnectTimeout` | 704 |
| `http-403` | 610 |
| `fetch-error:SSLError` | 576 |
| `low-confidence:http-2xx-html` | 347 |
| `empty-body` | 123 |
| `fetch-error:ReadTimeout` | 62 |
| `http-404` | 36 |
| `http-500` | 23 |
| `parking-linkfarm` | 22 |
| `parking` | 14 |

## Freshness

- Verified in last 30 days: **12378** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **561**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/425 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 125/580 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 73/278 (26%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 9/86 (10%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
