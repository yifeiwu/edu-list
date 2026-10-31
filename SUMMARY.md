# Edu-Domains — Run Summary

_Generated 2026-10-31 00:57 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22688** across **205** countries
- Active: **12137** (53%) · Inaccessible: **10551** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10014** domains (median 21 yrs)

## Last runs

- Verify (2026-10-31 00:57 UTC): validated 56, +18 Active, re-verified 15, pending left 0
- Curate (2026-10-31 00:34 UTC): 10701 raw candidates, 41 queued, 10598 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4595 | 3472 | 1123 |
| FR | 2968 | 1441 | 1527 |
| CN | 1285 | 145 | 1140 |
| IN | 806 | 434 | 372 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 583 | 226 | 357 |
| BR | 573 | 282 | 291 |
| ID | 547 | 326 | 221 |
| PL | 442 | 177 | 265 |
| UA | 414 | 174 | 240 |
| ES | 407 | 262 | 145 |
| KR | 339 | 96 | 243 |
| GB | 302 | 154 | 148 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12142 |
| `unreachable-dns` | 3224 |
| `fetch-error:ConnectTimeout` | 1360 |
| `fetch-error:ConnectionError` | 1118 |
| `low-confidence:http-2xx-html` | 1055 |
| `fetch-error:SSLError` | 1025 |
| `http-403` | 1011 |
| `empty-body` | 218 |
| `fetch-error:ReadTimeout` | 126 |
| `http-500` | 126 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **15461** (68%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3224**
- Moved pointers (old domain → new): **947**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 145/1285 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/339 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/152 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
