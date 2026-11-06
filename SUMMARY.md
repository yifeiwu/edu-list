# Edu-Domains — Run Summary

_Generated 2026-11-06 17:33 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23589** across **205** countries
- Active: **12657** (54%) · Inaccessible: **10932** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10442** domains (median 21 yrs)

## Last runs

- Verify (2026-11-06 17:32 UTC): validated 46, +20 Active, re-verified 15, pending left 0
- Curate (2026-11-06 10:34 UTC): 10691 raw candidates, 31 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4713 | 3569 | 1144 |
| FR | 3215 | 1555 | 1660 |
| CN | 1318 | 152 | 1166 |
| IN | 854 | 466 | 388 |
| JP | 809 | 226 | 583 |
| AU | 737 | 538 | 199 |
| DE | 610 | 343 | 267 |
| RU | 597 | 234 | 363 |
| BR | 583 | 297 | 286 |
| ID | 572 | 344 | 228 |
| UA | 523 | 216 | 307 |
| PL | 459 | 180 | 279 |
| ES | 413 | 265 | 148 |
| GB | 365 | 201 | 164 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12662 |
| `unreachable-dns` | 3290 |
| `fetch-error:ConnectTimeout` | 1425 |
| `fetch-error:ConnectionError` | 1182 |
| `low-confidence:http-2xx-html` | 1118 |
| `fetch-error:SSLError` | 1057 |
| `http-403` | 1039 |
| `empty-body` | 227 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 132 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **13411** (57%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3290**
- Moved pointers (old domain → new): **978**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 152/1318 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 62 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
