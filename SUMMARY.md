# Edu-Domains — Run Summary

_Generated 2026-11-05 21:23 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23502** across **205** countries
- Active: **12596** (54%) · Inaccessible: **10906** (46%)
- Pending queue: **30** unvalidated candidates
- Known registration age: **10404** domains (median 21 yrs)

## Last runs

- Verify (2026-11-05 15:53 UTC): validated 38, +10 Active, re-verified 15, pending left 0
- Curate (2026-11-05 21:23 UTC): 10696 raw candidates, 30 queued, 64 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4700 | 3555 | 1145 |
| FR | 3183 | 1540 | 1643 |
| CN | 1316 | 152 | 1164 |
| IN | 851 | 465 | 386 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 609 | 342 | 267 |
| RU | 597 | 234 | 363 |
| BR | 581 | 287 | 294 |
| ID | 570 | 343 | 227 |
| UA | 496 | 205 | 291 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 349 | 98 | 251 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12601 |
| `unreachable-dns` | 3279 |
| `fetch-error:ConnectTimeout` | 1416 |
| `fetch-error:ConnectionError` | 1177 |
| `low-confidence:http-2xx-html` | 1116 |
| `fetch-error:SSLError` | 1061 |
| `http-403` | 1038 |
| `empty-body` | 227 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 132 |
| `http-404` | 91 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13809** (59%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3279**
- Moved pointers (old domain → new): **975**

## Alerts

- ⚠ `CN`: low Active rate 152/1316 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/349 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/156 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 62 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
