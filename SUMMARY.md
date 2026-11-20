# Edu-Domains — Run Summary

_Generated 2026-11-20 00:58 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25492** across **207** countries
- Active: **13638** (53%) · Inaccessible: **11854** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11184** domains (median 21 yrs)

## Last runs

- Verify (2026-11-20 00:58 UTC): validated 50, +19 Active, re-verified 15, pending left 0
- Curate (2026-11-19 20:12 UTC): 10693 raw candidates, 34 queued, 50 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4783 | 3609 | 1174 |
| FR | 3676 | 1776 | 1900 |
| CN | 1387 | 153 | 1234 |
| JP | 978 | 285 | 693 |
| IN | 938 | 530 | 408 |
| AU | 762 | 559 | 203 |
| ID | 680 | 413 | 267 |
| DE | 627 | 353 | 274 |
| RU | 625 | 253 | 372 |
| BR | 606 | 313 | 293 |
| UA | 586 | 253 | 333 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 378 | 212 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13643 |
| `unreachable-dns` | 3505 |
| `fetch-error:ConnectTimeout` | 1566 |
| `fetch-error:ConnectionError` | 1296 |
| `low-confidence:http-2xx-html` | 1286 |
| `fetch-error:SSLError` | 1134 |
| `http-403` | 1102 |
| `empty-body` | 245 |
| `http-500` | 149 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 97 |
| `http-503` | 55 |

## Freshness

- Verified in last 30 days: **7615** (30%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3505**
- Moved pointers (old domain → new): **1053**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1387 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/978 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 303 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
