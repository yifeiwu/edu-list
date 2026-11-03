# Edu-Domains — Run Summary

_Generated 2026-11-03 23:27 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23363** across **205** countries
- Active: **12521** (54%) · Inaccessible: **10842** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10347** domains (median 21 yrs)

## Last runs

- Verify (2026-11-03 23:27 UTC): validated 53, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-03 21:41 UTC): 10698 raw candidates, 37 queued, 61 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4691 | 3548 | 1143 |
| FR | 3123 | 1508 | 1615 |
| CN | 1304 | 148 | 1156 |
| IN | 842 | 458 | 384 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 608 | 341 | 267 |
| RU | 596 | 235 | 361 |
| BR | 580 | 287 | 293 |
| ID | 569 | 343 | 226 |
| UA | 474 | 196 | 278 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 348 | 97 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12526 |
| `unreachable-dns` | 3269 |
| `fetch-error:ConnectTimeout` | 1402 |
| `fetch-error:ConnectionError` | 1166 |
| `low-confidence:http-2xx-html` | 1104 |
| `fetch-error:SSLError` | 1057 |
| `http-403` | 1037 |
| `empty-body` | 226 |
| `http-500` | 132 |
| `fetch-error:ReadTimeout` | 129 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **14638** (63%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3269**
- Moved pointers (old domain → new): **971**

## Alerts

- ⚠ `CN`: low Active rate 148/1304 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 97/348 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/156 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 59 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
