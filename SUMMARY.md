# Edu-Domains — Run Summary

_Generated 2026-11-07 19:44 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23770** across **205** countries
- Active: **12778** (54%) · Inaccessible: **10992** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10531** domains (median 21 yrs)

## Last runs

- Verify (2026-11-07 19:44 UTC): validated 51, +24 Active, re-verified 15, pending left 0
- Curate (2026-11-07 16:11 UTC): 10696 raw candidates, 36 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4721 | 3575 | 1146 |
| FR | 3268 | 1587 | 1681 |
| CN | 1325 | 153 | 1172 |
| IN | 864 | 475 | 389 |
| JP | 809 | 226 | 583 |
| AU | 737 | 538 | 199 |
| DE | 611 | 344 | 267 |
| RU | 602 | 239 | 363 |
| BR | 584 | 298 | 286 |
| ID | 578 | 347 | 231 |
| UA | 556 | 238 | 318 |
| PL | 461 | 180 | 281 |
| ES | 413 | 265 | 148 |
| GB | 366 | 202 | 164 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12783 |
| `unreachable-dns` | 3298 |
| `fetch-error:ConnectTimeout` | 1434 |
| `fetch-error:ConnectionError` | 1192 |
| `low-confidence:http-2xx-html` | 1127 |
| `fetch-error:SSLError` | 1062 |
| `http-403` | 1046 |
| `empty-body` | 230 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 134 |
| `http-404` | 90 |
| `http-503` | 52 |

## Freshness

- Verified in last 30 days: **13210** (56%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3298**
- Moved pointers (old domain → new): **981**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1325 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 82 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
