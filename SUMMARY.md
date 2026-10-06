# Edu-Domains — Run Summary

_Generated 2026-10-06 00:55 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **12271** across **203** countries
- Active: **6467** (53%) · Inaccessible: **5804** (47%)
- Pending queue: **4318** unvalidated candidates
- Known registration age: **5294** domains (median 24 yrs)

## Last runs

- Verify (2026-10-06 00:55 UTC): validated 118, +67 Active, re-verified 15, pending left 4318
- Curate (2026-10-06 00:40 UTC): 10700 raw candidates, 46 queued, 10211 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 2665 | 2009 | 656 |
| FR | 632 | 320 | 312 |
| JP | 580 | 125 | 455 |
| IN | 501 | 242 | 259 |
| CN | 424 | 52 | 372 |
| DE | 384 | 181 | 203 |
| AU | 380 | 261 | 119 |
| BR | 354 | 165 | 189 |
| RU | 336 | 108 | 228 |
| KR | 278 | 73 | 205 |
| GB | 241 | 116 | 125 |
| ID | 227 | 132 | 95 |
| IR | 212 | 69 | 143 |
| TR | 193 | 134 | 59 |
| CA | 181 | 100 | 81 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 6469 |
| `fetch-error:ConnectionError` | 2666 |
| `fetch-error:ConnectTimeout` | 700 |
| `http-403` | 603 |
| `fetch-error:SSLError` | 574 |
| `low-confidence:http-2xx-html` | 346 |
| `empty-body` | 123 |
| `fetch-error:ReadTimeout` | 61 |
| `http-404` | 36 |
| `http-500` | 23 |
| `parking-linkfarm` | 21 |
| `parking` | 14 |

## Freshness

- Verified in last 30 days: **12271** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **553**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 52/424 (12%) — check for blocks/stale sources
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
