# Edu-Domains — Run Summary

_Generated 2026-10-30 15:42 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22522** across **205** countries
- Active: **12055** (54%) · Inaccessible: **10467** (46%)
- Pending queue: **59** unvalidated candidates
- Known registration age: **9934** domains (median 22 yrs)

## Last runs

- Verify (2026-10-30 09:05 UTC): validated 71, +29 Active, re-verified 15, pending left 0
- Curate (2026-10-30 15:42 UTC): 10700 raw candidates, 59 queued, 44 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4575 | 3454 | 1121 |
| FR | 2935 | 1426 | 1509 |
| CN | 1282 | 145 | 1137 |
| IN | 800 | 430 | 370 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| BR | 572 | 282 | 290 |
| RU | 558 | 212 | 346 |
| ID | 544 | 323 | 221 |
| PL | 425 | 175 | 250 |
| ES | 407 | 262 | 145 |
| UA | 371 | 154 | 217 |
| KR | 336 | 94 | 242 |
| GB | 301 | 154 | 147 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12060 |
| `unreachable-dns` | 3207 |
| `fetch-error:ConnectTimeout` | 1339 |
| `fetch-error:ConnectionError` | 1111 |
| `low-confidence:http-2xx-html` | 1046 |
| `fetch-error:SSLError` | 1012 |
| `http-403` | 1006 |
| `empty-body` | 215 |
| `fetch-error:ReadTimeout` | 126 |
| `http-500` | 124 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **15857** (70%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3207**
- Moved pointers (old domain → new): **942**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 145/1282 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/336 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/151 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
