# Edu-Domains — Run Summary

_Generated 2026-11-06 10:02 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23558** across **205** countries
- Active: **12637** (54%) · Inaccessible: **10921** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10426** domains (median 21 yrs)

## Last runs

- Verify (2026-11-06 10:02 UTC): validated 60, +0 Active, re-verified 60, pending left 0
- Curate (2026-11-06 02:05 UTC): 10691 raw candidates, 24 queued, 10616 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4707 | 3563 | 1144 |
| FR | 3206 | 1550 | 1656 |
| CN | 1317 | 152 | 1165 |
| IN | 852 | 465 | 387 |
| JP | 808 | 225 | 583 |
| AU | 737 | 538 | 199 |
| DE | 610 | 343 | 267 |
| RU | 597 | 234 | 363 |
| BR | 581 | 295 | 286 |
| ID | 571 | 343 | 228 |
| UA | 516 | 214 | 302 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12642 |
| `unreachable-dns` | 3286 |
| `fetch-error:ConnectTimeout` | 1421 |
| `fetch-error:ConnectionError` | 1182 |
| `low-confidence:http-2xx-html` | 1118 |
| `fetch-error:SSLError` | 1056 |
| `http-403` | 1038 |
| `empty-body` | 227 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 132 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13365** (57%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3286**
- Moved pointers (old domain → new): **977**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 152/1317 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 225/808 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/156 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 62 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
