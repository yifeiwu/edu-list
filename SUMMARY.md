# Edu-Domains — Run Summary

_Generated 2026-10-26 21:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **21746** across **205** countries
- Active: **11664** (54%) · Inaccessible: **10082** (46%)
- Pending queue: **39** unvalidated candidates
- Known registration age: **9579** domains (median 22 yrs)

## Last runs

- Verify (2026-10-26 17:45 UTC): validated 50, +13 Active, re-verified 15, pending left 0
- Curate (2026-10-26 21:29 UTC): 10700 raw candidates, 39 queued, 65 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4501 | 3389 | 1112 |
| FR | 2775 | 1347 | 1428 |
| CN | 1258 | 142 | 1116 |
| IN | 775 | 410 | 365 |
| JP | 771 | 211 | 560 |
| AU | 736 | 537 | 199 |
| DE | 603 | 337 | 266 |
| BR | 562 | 279 | 283 |
| RU | 520 | 194 | 326 |
| ID | 511 | 305 | 206 |
| PL | 417 | 173 | 244 |
| ES | 404 | 260 | 144 |
| KR | 335 | 94 | 241 |
| GB | 294 | 149 | 145 |
| MX | 285 | 157 | 128 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11669 |
| `unreachable-dns` | 3115 |
| `fetch-error:ConnectTimeout` | 1287 |
| `fetch-error:ConnectionError` | 1065 |
| `low-confidence:http-2xx-html` | 994 |
| `http-403` | 981 |
| `fetch-error:SSLError` | 964 |
| `empty-body` | 209 |
| `http-500` | 117 |
| `fetch-error:ReadTimeout` | 114 |
| `http-404` | 86 |
| `http-503` | 44 |

## Freshness

- Verified in last 30 days: **17129** (79%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3115**
- Moved pointers (old domain → new): **916**

## Alerts

- ⚠ `AO`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 142/1258 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 211/771 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/335 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/144 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 31 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
