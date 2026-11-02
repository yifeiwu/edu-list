# Edu-Domains — Run Summary

_Generated 2026-11-02 02:32 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23097** across **205** countries
- Active: **12369** (54%) · Inaccessible: **10728** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10234** domains (median 21 yrs)

## Last runs

- Verify (2026-11-02 02:32 UTC): validated 64, +35 Active, re-verified 15, pending left 0
- Curate (2026-11-02 00:34 UTC): 10695 raw candidates, 48 queued, 10595 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4666 | 3532 | 1134 |
| FR | 3050 | 1478 | 1572 |
| CN | 1297 | 147 | 1150 |
| IN | 820 | 445 | 375 |
| JP | 803 | 223 | 580 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 590 | 230 | 360 |
| BR | 577 | 284 | 293 |
| ID | 566 | 340 | 226 |
| UA | 467 | 193 | 274 |
| PL | 458 | 179 | 279 |
| ES | 411 | 264 | 147 |
| KR | 344 | 96 | 248 |
| GB | 334 | 179 | 155 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12374 |
| `unreachable-dns` | 3253 |
| `fetch-error:ConnectTimeout` | 1390 |
| `fetch-error:ConnectionError` | 1140 |
| `low-confidence:http-2xx-html` | 1088 |
| `fetch-error:SSLError` | 1045 |
| `http-403` | 1024 |
| `empty-body` | 223 |
| `fetch-error:ReadTimeout` | 129 |
| `http-500` | 127 |
| `http-404` | 89 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **14993** (65%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3253**
- Moved pointers (old domain → new): **962**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1297 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 223/803 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/344 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/154 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 41 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
