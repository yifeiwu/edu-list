# Edu-Domains — Run Summary

_Generated 2026-10-28 18:08 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22111** across **205** countries
- Active: **11845** (54%) · Inaccessible: **10266** (46%)
- Pending queue: **42** unvalidated candidates
- Known registration age: **9728** domains (median 22 yrs)

## Last runs

- Verify (2026-10-28 14:36 UTC): validated 48, +13 Active, re-verified 15, pending left 0
- Curate (2026-10-28 18:08 UTC): 10701 raw candidates, 42 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4523 | 3410 | 1113 |
| FR | 2848 | 1382 | 1466 |
| CN | 1273 | 144 | 1129 |
| JP | 794 | 219 | 575 |
| IN | 789 | 421 | 368 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 568 | 281 | 287 |
| ID | 522 | 310 | 212 |
| RU | 522 | 196 | 326 |
| PL | 419 | 174 | 245 |
| ES | 405 | 261 | 144 |
| KR | 336 | 94 | 242 |
| GB | 298 | 152 | 146 |
| MX | 288 | 158 | 130 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11850 |
| `unreachable-dns` | 3162 |
| `fetch-error:ConnectTimeout` | 1312 |
| `fetch-error:ConnectionError` | 1083 |
| `low-confidence:http-2xx-html` | 1017 |
| `http-403` | 994 |
| `fetch-error:SSLError` | 986 |
| `empty-body` | 211 |
| `http-500` | 120 |
| `fetch-error:ReadTimeout` | 119 |
| `http-404` | 86 |
| `http-503` | 48 |

## Freshness

- Verified in last 30 days: **16277** (74%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3162**
- Moved pointers (old domain → new): **928**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 144/1273 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 219/794 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/336 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 21/149 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
