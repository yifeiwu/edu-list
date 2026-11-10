# Edu-Domains — Run Summary

_Generated 2026-11-10 09:52 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24159** across **205** countries
- Active: **12996** (54%) · Inaccessible: **11163** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10691** domains (median 21 yrs)

## Last runs

- Verify (2026-11-10 09:52 UTC): validated 49, +16 Active, re-verified 15, pending left 0
- Curate (2026-11-10 07:06 UTC): 10692 raw candidates, 33 queued, 10595 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4740 | 3586 | 1154 |
| FR | 3375 | 1628 | 1747 |
| CN | 1337 | 155 | 1182 |
| IN | 881 | 491 | 390 |
| JP | 823 | 229 | 594 |
| AU | 743 | 544 | 199 |
| DE | 612 | 345 | 267 |
| RU | 609 | 245 | 364 |
| BR | 591 | 304 | 287 |
| ID | 589 | 354 | 235 |
| UA | 573 | 243 | 330 |
| PL | 461 | 180 | 281 |
| ES | 417 | 269 | 148 |
| GB | 368 | 203 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13001 |
| `unreachable-dns` | 3327 |
| `fetch-error:ConnectTimeout` | 1462 |
| `fetch-error:ConnectionError` | 1223 |
| `low-confidence:http-2xx-html` | 1153 |
| `fetch-error:SSLError` | 1077 |
| `http-403` | 1052 |
| `empty-body` | 235 |
| `http-500` | 138 |
| `fetch-error:ReadTimeout` | 138 |
| `http-404` | 91 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **12169** (50%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3327**
- Moved pointers (old domain → new): **1000**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1337 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 229/823 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 139 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
