# Edu-Domains — Run Summary

_Generated 2026-11-01 19:16 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23000** across **205** countries
- Active: **12306** (54%) · Inaccessible: **10694** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10181** domains (median 21 yrs)

## Last runs

- Verify (2026-11-01 19:16 UTC): validated 53, +22 Active, re-verified 15, pending left 0
- Curate (2026-11-01 16:39 UTC): 10695 raw candidates, 38 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4649 | 3519 | 1130 |
| FR | 3022 | 1462 | 1560 |
| CN | 1297 | 147 | 1150 |
| IN | 819 | 444 | 375 |
| JP | 801 | 223 | 578 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 588 | 230 | 358 |
| BR | 577 | 284 | 293 |
| ID | 562 | 337 | 225 |
| UA | 467 | 193 | 274 |
| PL | 458 | 179 | 279 |
| ES | 410 | 264 | 146 |
| KR | 344 | 96 | 248 |
| GB | 319 | 166 | 153 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12311 |
| `unreachable-dns` | 3248 |
| `fetch-error:ConnectTimeout` | 1383 |
| `fetch-error:ConnectionError` | 1133 |
| `low-confidence:http-2xx-html` | 1082 |
| `fetch-error:SSLError` | 1042 |
| `http-403` | 1021 |
| `empty-body` | 223 |
| `fetch-error:ReadTimeout` | 129 |
| `http-500` | 127 |
| `http-404` | 89 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15462** (67%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3248**
- Moved pointers (old domain → new): **960**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1297 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 223/801 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/344 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/153 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 36 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
