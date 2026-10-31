# Edu-Domains — Run Summary

_Generated 2026-10-31 00:34 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22647** across **205** countries
- Active: **12119** (54%) · Inaccessible: **10528** (46%)
- Pending queue: **41** unvalidated candidates
- Known registration age: **9991** domains (median 21 yrs)

## Last runs

- Verify (2026-10-30 20:56 UTC): validated 78, +29 Active, re-verified 15, pending left 0
- Curate (2026-10-31 00:34 UTC): 10701 raw candidates, 41 queued, 10598 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4589 | 3467 | 1122 |
| FR | 2959 | 1439 | 1520 |
| CN | 1284 | 145 | 1139 |
| IN | 804 | 433 | 371 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 583 | 226 | 357 |
| BR | 572 | 282 | 290 |
| ID | 546 | 325 | 221 |
| PL | 437 | 177 | 260 |
| ES | 407 | 262 | 145 |
| UA | 403 | 168 | 235 |
| KR | 337 | 94 | 243 |
| GB | 301 | 154 | 147 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12124 |
| `unreachable-dns` | 3219 |
| `fetch-error:ConnectTimeout` | 1350 |
| `fetch-error:ConnectionError` | 1118 |
| `low-confidence:http-2xx-html` | 1053 |
| `fetch-error:SSLError` | 1024 |
| `http-403` | 1009 |
| `empty-body` | 216 |
| `fetch-error:ReadTimeout` | 126 |
| `http-500` | 126 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **15405** (68%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3219**
- Moved pointers (old domain → new): **947**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 145/1284 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/337 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/152 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
