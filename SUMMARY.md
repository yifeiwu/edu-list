# Edu-Domains — Run Summary

_Generated 2026-11-21 01:11 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25575** across **207** countries
- Active: **13687** (54%) · Inaccessible: **11888** (46%)
- Pending queue: **32** unvalidated candidates
- Known registration age: **11223** domains (median 21 yrs)

## Last runs

- Verify (2026-11-20 23:29 UTC): validated 46, +16 Active, re-verified 15, pending left 0
- Curate (2026-11-21 01:11 UTC): 10696 raw candidates, 32 queued, 10606 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4784 | 3609 | 1175 |
| FR | 3706 | 1789 | 1917 |
| CN | 1388 | 153 | 1235 |
| JP | 979 | 285 | 694 |
| IN | 943 | 534 | 409 |
| AU | 762 | 559 | 203 |
| ID | 694 | 423 | 271 |
| DE | 635 | 359 | 276 |
| RU | 625 | 253 | 372 |
| BR | 611 | 316 | 295 |
| UA | 586 | 253 | 333 |
| PL | 483 | 184 | 299 |
| ES | 421 | 270 | 151 |
| GB | 379 | 213 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13692 |
| `unreachable-dns` | 3513 |
| `fetch-error:ConnectTimeout` | 1575 |
| `fetch-error:ConnectionError` | 1300 |
| `low-confidence:http-2xx-html` | 1290 |
| `fetch-error:SSLError` | 1133 |
| `http-403` | 1105 |
| `empty-body` | 246 |
| `http-500` | 150 |
| `fetch-error:ReadTimeout` | 140 |
| `http-404` | 97 |
| `http-503` | 55 |

## Freshness

- Verified in last 30 days: **7152** (28%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3513**
- Moved pointers (old domain → new): **1055**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1388 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 285/979 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 301 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
