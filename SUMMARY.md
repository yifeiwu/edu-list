# Edu-Domains — Run Summary

_Generated 2026-09-27 13:13 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **8013** across **143** countries
- Active: **4176** (52%) · Inaccessible: **3837** (48%)
- Pending queue: **6220** unvalidated candidates
- Known registration age: **3792** domains (median 26 yrs)

## Last runs

- Verify (2026-09-27 13:13 UTC): validated 116, +20 Active, re-verified 15, pending left 6220
- Curate (2026-09-27 07:47 UTC): 10701 raw candidates, 60 queued, 21 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1301 | 425 |
| FR | 619 | 308 | 311 |
| JP | 577 | 125 | 452 |
| IN | 458 | 208 | 250 |
| CN | 415 | 53 | 362 |
| AU | 375 | 256 | 119 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| KR | 260 | 65 | 195 |
| ID | 224 | 129 | 95 |
| IR | 212 | 69 | 143 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| CO | 105 | 59 | 46 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4176 |
| `fetch-error:ConnectionError` | 1762 |
| `fetch-error:ConnectTimeout` | 474 |
| `http-403` | 393 |
| `fetch-error:SSLError` | 362 |
| `low-confidence:http-2xx-html` | 242 |
| `empty-body` | 69 |
| `fetch-error:ReadTimeout` | 45 |
| `http-404` | 26 |
| `http-500` | 16 |
| `parking-linkfarm` | 15 |
| `http-503` | 11 |

## Freshness

- Verified in last 30 days: **8013** (100%)
- Older than 90 days: **0** (oldest check 2026-09-15)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **364**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 125/577 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 65/260 (25%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
