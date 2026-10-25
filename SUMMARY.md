# Edu-Domains — Run Summary

_Generated 2026-10-25 07:23 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21561** across **205** countries
- Active: **11559** (54%) · Inaccessible: **10002** (46%)
- Pending queue: **24** unvalidated candidates
- Known registration age: **9517** domains (median 22 yrs)

## Last runs

- Verify (2026-10-25 06:56 UTC): validated 60, +0 Active, re-verified 60, pending left 0
- Curate (2026-10-25 07:23 UTC): 10688 raw candidates, 24 queued, 66 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4492 | 3382 | 1110 |
| FR | 2743 | 1328 | 1415 |
| CN | 1250 | 140 | 1110 |
| IN | 763 | 400 | 363 |
| JP | 753 | 204 | 549 |
| AU | 736 | 537 | 199 |
| DE | 600 | 335 | 265 |
| BR | 559 | 277 | 282 |
| RU | 519 | 194 | 325 |
| ID | 505 | 300 | 205 |
| PL | 416 | 172 | 244 |
| ES | 403 | 259 | 144 |
| KR | 333 | 92 | 241 |
| GB | 292 | 148 | 144 |
| MX | 283 | 156 | 127 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11564 |
| `unreachable-dns` | 3097 |
| `fetch-error:ConnectTimeout` | 1276 |
| `fetch-error:ConnectionError` | 1055 |
| `low-confidence:http-2xx-html` | 979 |
| `http-403` | 978 |
| `fetch-error:SSLError` | 950 |
| `empty-body` | 210 |
| `http-500` | 115 |
| `fetch-error:ReadTimeout` | 112 |
| `http-404` | 85 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17533** (81%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **3**
- Retired, no DNS record (`unreachable-dns`): **3097**
- Moved pointers (old domain → new): **911**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 140/1250 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 204/753 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 92/333 (28%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/142 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 29 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
