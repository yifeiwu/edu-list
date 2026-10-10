# Edu-Domains — Run Summary

_Generated 2026-10-10 02:51 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **14048** across **204** countries
- Active: **7527** (54%) · Inaccessible: **6521** (46%)
- Pending queue: **3486** unvalidated candidates
- Known registration age: **6217** domains (median 24 yrs)

## Last runs

- Verify (2026-10-10 02:51 UTC): validated 118, +65 Active, re-verified 15, pending left 3486
- Curate (2026-10-10 00:34 UTC): 10697 raw candidates, 69 queued, 10560 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3044 | 2289 | 755 |
| FR | 1158 | 615 | 543 |
| JP | 595 | 130 | 465 |
| IN | 559 | 284 | 275 |
| DE | 487 | 263 | 224 |
| CN | 475 | 61 | 414 |
| BR | 472 | 224 | 248 |
| AU | 435 | 299 | 136 |
| RU | 395 | 127 | 268 |
| KR | 300 | 80 | 220 |
| GB | 264 | 130 | 134 |
| ID | 241 | 141 | 100 |
| IR | 217 | 69 | 148 |
| TR | 201 | 137 | 64 |
| CA | 195 | 112 | 83 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 7529 |
| `unreachable-dns` | 2354 |
| `fetch-error:ConnectTimeout` | 788 |
| `http-403` | 675 |
| `fetch-error:SSLError` | 645 |
| `fetch-error:ConnectionError` | 550 |
| `low-confidence:http-2xx-html` | 441 |
| `empty-body` | 132 |
| `fetch-error:ReadTimeout` | 75 |
| `http-404` | 41 |
| `http-500` | 36 |
| `parking-linkfarm` | 22 |

## Freshness

- Verified in last 30 days: **14048** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2354**
- Moved pointers (old domain → new): **642**

## Alerts

- ⚠ `AO`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 61/475 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 130/595 (22%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 80/300 (27%) — check for blocks/stale sources
- ⚠ `MA`: low Active rate 11/39 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 11/93 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `XX`: 1 unmapped country — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
