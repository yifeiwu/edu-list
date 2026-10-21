# Edu-Domains — Run Summary

_Generated 2026-10-21 01:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20127** across **205** countries
- Active: **10817** (54%) · Inaccessible: **9310** (46%)
- Pending queue: **369** unvalidated candidates
- Known registration age: **8920** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 23:33 UTC): validated 119, +58 Active, re-verified 15, pending left 310
- Curate (2026-10-21 01:29 UTC): 10701 raw candidates, 59 queued, 10584 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4209 | 3173 | 1036 |
| FR | 2441 | 1195 | 1246 |
| CN | 1065 | 124 | 941 |
| AU | 734 | 534 | 200 |
| IN | 725 | 371 | 354 |
| JP | 708 | 189 | 519 |
| DE | 597 | 333 | 264 |
| BR | 516 | 255 | 261 |
| ID | 493 | 295 | 198 |
| RU | 462 | 172 | 290 |
| PL | 413 | 172 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 268 | 85 | 183 |
| MX | 250 | 134 | 116 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10821 |
| `unreachable-dns` | 2934 |
| `fetch-error:ConnectTimeout` | 1157 |
| `fetch-error:ConnectionError` | 947 |
| `http-403` | 940 |
| `fetch-error:SSLError` | 903 |
| `low-confidence:http-2xx-html` | 872 |
| `empty-body` | 200 |
| `fetch-error:ReadTimeout` | 110 |
| `http-500` | 97 |
| `http-404` | 75 |
| `http-503` | 40 |

## Freshness

- Verified in last 30 days: **18130** (90%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2934**
- Moved pointers (old domain → new): **860**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 124/1065 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 189/708 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/137 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 18 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
