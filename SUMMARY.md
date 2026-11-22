# Edu-Domains — Run Summary

_Generated 2026-11-22 15:45 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25749** across **207** countries
- Active: **13779** (54%) · Inaccessible: **11970** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11304** domains (median 21 yrs)

## Last runs

- Verify (2026-11-22 15:45 UTC): validated 42, +16 Active, re-verified 15, pending left 0
- Curate (2026-11-22 10:53 UTC): 10705 raw candidates, 27 queued, 68 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4789 | 3609 | 1180 |
| FR | 3772 | 1820 | 1952 |
| CN | 1391 | 153 | 1238 |
| JP | 980 | 286 | 694 |
| IN | 948 | 536 | 412 |
| AU | 763 | 561 | 202 |
| ID | 727 | 445 | 282 |
| DE | 640 | 361 | 279 |
| RU | 631 | 255 | 376 |
| BR | 612 | 317 | 295 |
| UA | 586 | 253 | 333 |
| PL | 484 | 184 | 300 |
| ES | 422 | 270 | 152 |
| GB | 380 | 214 | 166 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13784 |
| `unreachable-dns` | 3525 |
| `fetch-error:ConnectTimeout` | 1592 |
| `fetch-error:ConnectionError` | 1309 |
| `low-confidence:http-2xx-html` | 1304 |
| `fetch-error:SSLError` | 1139 |
| `http-403` | 1113 |
| `empty-body` | 247 |
| `http-500` | 152 |
| `fetch-error:ReadTimeout` | 142 |
| `http-404` | 98 |
| `http-503` | 57 |

## Freshness

- Verified in last 30 days: **6941** (27%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3525**
- Moved pointers (old domain → new): **1062**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1391 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/980 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 299 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
