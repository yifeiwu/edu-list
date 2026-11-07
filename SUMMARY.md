# Edu-Domains — Run Summary

_Generated 2026-11-07 02:26 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23658** across **205** countries
- Active: **12701** (54%) · Inaccessible: **10957** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10475** domains (median 21 yrs)

## Last runs

- Verify (2026-11-07 02:26 UTC): validated 50, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-06 22:52 UTC): 10677 raw candidates, 34 queued, 36 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4714 | 3569 | 1145 |
| FR | 3239 | 1573 | 1666 |
| CN | 1320 | 153 | 1167 |
| IN | 856 | 467 | 389 |
| JP | 809 | 226 | 583 |
| AU | 737 | 538 | 199 |
| DE | 610 | 343 | 267 |
| RU | 598 | 235 | 363 |
| BR | 583 | 297 | 286 |
| ID | 574 | 344 | 230 |
| UA | 540 | 226 | 314 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12706 |
| `unreachable-dns` | 3292 |
| `fetch-error:ConnectTimeout` | 1430 |
| `fetch-error:ConnectionError` | 1188 |
| `low-confidence:http-2xx-html` | 1121 |
| `fetch-error:SSLError` | 1059 |
| `http-403` | 1042 |
| `empty-body` | 228 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 132 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13053** (55%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3292**
- Moved pointers (old domain → new): **978**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1320 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 68 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
