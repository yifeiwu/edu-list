# Edu-Domains — Run Summary

_Generated 2026-09-26 12:47 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **7406** across **140** countries
- Active: **4000** (54%) · Inaccessible: **3406** (46%)
- Pending queue: **6508** unvalidated candidates
- Known registration age: **3539** domains (median 26 yrs)

## Last runs

- Verify (2026-09-26 12:36 UTC): validated 115, +20 Active, re-verified 15, pending left 6453
- Curate (2026-09-26 12:47 UTC): 10701 raw candidates, 55 queued, 39 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 1726 | 1301 | 425 |
| FR | 619 | 308 | 311 |
| IN | 457 | 207 | 250 |
| CN | 415 | 53 | 362 |
| AU | 375 | 256 | 119 |
| DE | 346 | 155 | 191 |
| BR | 343 | 161 | 182 |
| JP | 330 | 66 | 264 |
| ID | 224 | 129 | 95 |
| IR | 212 | 69 | 143 |
| CA | 174 | 95 | 79 |
| AR | 126 | 90 | 36 |
| BE | 122 | 71 | 51 |
| CO | 105 | 59 | 46 |
| IT | 96 | 45 | 51 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 4000 |
| `fetch-error:ConnectionError` | 1522 |
| `fetch-error:ConnectTimeout` | 410 |
| `http-403` | 383 |
| `fetch-error:SSLError` | 314 |
| `low-confidence:http-2xx-html` | 208 |
| `empty-body` | 55 |
| `fetch-error:ReadTimeout` | 41 |
| `http-404` | 24 |
| `http-500` | 16 |
| `parking` | 11 |
| `parking-linkfarm` | 11 |

## Freshness

- Verified in last 30 days: **7406** (100%)
- Older than 90 days: **0** (oldest check 2026-09-14)
- Archived chronic failures (re-check paused): **2**
- Moved pointers (old domain → new): **355**

## Alerts

- ⚠ `AO`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 53/415 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 2/13 (15%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 66/330 (20%) — check for blocks/stale sources
- ⚠ `SD`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
