# Edu-Domains — Run Summary

_Generated 2026-11-01 14:19 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22962** across **205** countries
- Active: **12284** (53%) · Inaccessible: **10678** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10160** domains (median 21 yrs)

## Last runs

- Verify (2026-11-01 14:19 UTC): validated 49, +23 Active, re-verified 15, pending left 0
- Curate (2026-11-01 09:04 UTC): 10698 raw candidates, 33 queued, 56 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4647 | 3516 | 1131 |
| FR | 3018 | 1459 | 1559 |
| CN | 1294 | 147 | 1147 |
| IN | 818 | 443 | 375 |
| JP | 799 | 222 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 586 | 229 | 357 |
| BR | 576 | 284 | 292 |
| ID | 559 | 335 | 224 |
| UA | 467 | 193 | 274 |
| PL | 458 | 179 | 279 |
| ES | 407 | 262 | 145 |
| KR | 343 | 96 | 247 |
| GB | 312 | 160 | 152 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12289 |
| `unreachable-dns` | 3246 |
| `fetch-error:ConnectTimeout` | 1380 |
| `fetch-error:ConnectionError` | 1130 |
| `low-confidence:http-2xx-html` | 1080 |
| `fetch-error:SSLError` | 1039 |
| `http-403` | 1020 |
| `empty-body` | 223 |
| `fetch-error:ReadTimeout` | 128 |
| `http-500` | 127 |
| `http-404` | 89 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15409** (67%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3246**
- Moved pointers (old domain → new): **959**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 147/1294 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 222/799 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/343 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/153 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 34 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
