# Edu-Domains — Run Summary

_Generated 2026-11-23 22:18 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25821** across **207** countries
- Active: **13828** (54%) · Inaccessible: **11993** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11356** domains (median 21 yrs)

## Last runs

- Verify (2026-11-23 22:18 UTC): validated 21, +5 Active, re-verified 15, pending left 0
- Curate (2026-11-23 20:58 UTC): 10690 raw candidates, 6 queued, 86 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4793 | 3612 | 1181 |
| FR | 3799 | 1839 | 1960 |
| CN | 1393 | 153 | 1240 |
| JP | 980 | 286 | 694 |
| IN | 957 | 541 | 416 |
| AU | 763 | 561 | 202 |
| ID | 749 | 459 | 290 |
| DE | 640 | 361 | 279 |
| RU | 632 | 255 | 377 |
| BR | 613 | 317 | 296 |
| UA | 586 | 253 | 333 |
| PL | 484 | 184 | 300 |
| ES | 422 | 270 | 152 |
| GB | 380 | 214 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13833 |
| `unreachable-dns` | 3528 |
| `fetch-error:ConnectTimeout` | 1593 |
| `fetch-error:ConnectionError` | 1313 |
| `low-confidence:http-2xx-html` | 1310 |
| `fetch-error:SSLError` | 1139 |
| `http-403` | 1114 |
| `empty-body` | 247 |
| `http-500` | 152 |
| `fetch-error:ReadTimeout` | 143 |
| `http-404` | 99 |
| `http-503` | 57 |

## Freshness

- Verified in last 30 days: **6722** (26%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3528**
- Moved pointers (old domain → new): **1066**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 153/1393 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/980 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
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
