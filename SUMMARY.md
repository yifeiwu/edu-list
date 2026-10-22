# Edu-Domains — Run Summary

_Generated 2026-10-22 01:22 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20735** across **205** countries
- Active: **11109** (54%) · Inaccessible: **9626** (46%)
- Pending queue: **51** unvalidated candidates
- Known registration age: **9155** domains (median 22 yrs)

## Last runs

- Verify (2026-10-22 00:27 UTC): validated 107, +40 Active, re-verified 15, pending left 0
- Curate (2026-10-22 01:22 UTC): 10695 raw candidates, 51 queued, 10576 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4338 | 3271 | 1067 |
| FR | 2543 | 1236 | 1307 |
| CN | 1224 | 137 | 1087 |
| IN | 738 | 383 | 355 |
| AU | 734 | 534 | 200 |
| JP | 709 | 189 | 520 |
| DE | 598 | 334 | 264 |
| BR | 529 | 261 | 268 |
| ID | 496 | 297 | 199 |
| RU | 475 | 176 | 299 |
| PL | 416 | 172 | 244 |
| KR | 331 | 90 | 241 |
| ES | 313 | 194 | 119 |
| GB | 289 | 147 | 142 |
| MX | 280 | 154 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11114 |
| `unreachable-dns` | 3018 |
| `fetch-error:ConnectTimeout` | 1196 |
| `fetch-error:ConnectionError` | 1009 |
| `http-403` | 958 |
| `fetch-error:SSLError` | 927 |
| `low-confidence:http-2xx-html` | 910 |
| `empty-body` | 205 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 108 |
| `http-404` | 79 |
| `http-503` | 42 |

## Freshness

- Verified in last 30 days: **18354** (89%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3018**
- Moved pointers (old domain → new): **882**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 137/1224 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 189/709 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 90/331 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/138 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 20 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
