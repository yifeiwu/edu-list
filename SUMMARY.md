# Edu-Domains — Run Summary

_Generated 2026-11-26 02:54 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25952** across **207** countries
- Active: **13891** (54%) · Inaccessible: **12061** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **11413** domains (median 20 yrs)

## Last runs

- Verify (2026-11-26 02:54 UTC): validated 36, +11 Active, re-verified 15, pending left 0
- Curate (2026-11-25 21:20 UTC): 10691 raw candidates, 21 queued, 68 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4808 | 3620 | 1188 |
| FR | 3844 | 1855 | 1989 |
| CN | 1397 | 154 | 1243 |
| JP | 983 | 286 | 697 |
| IN | 962 | 544 | 418 |
| AU | 763 | 561 | 202 |
| ID | 762 | 467 | 295 |
| DE | 649 | 366 | 283 |
| RU | 633 | 255 | 378 |
| BR | 615 | 318 | 297 |
| UA | 587 | 254 | 333 |
| PL | 493 | 186 | 307 |
| ES | 422 | 270 | 152 |
| GB | 380 | 214 | 166 |
| KR | 353 | 100 | 253 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13896 |
| `unreachable-dns` | 3537 |
| `fetch-error:ConnectTimeout` | 1616 |
| `low-confidence:http-2xx-html` | 1319 |
| `fetch-error:ConnectionError` | 1319 |
| `fetch-error:SSLError` | 1142 |
| `http-403` | 1119 |
| `empty-body` | 248 |
| `http-500` | 153 |
| `fetch-error:ReadTimeout` | 144 |
| `http-404` | 100 |
| `http-503` | 58 |

## Freshness

- Verified in last 30 days: **6116** (24%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3537**
- Moved pointers (old domain → new): **1072**

## Alerts

- ⚠ `AO`: low Active rate 5/17 (29%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 154/1397 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 4/17 (24%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 286/983 (29%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/353 (28%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `SS`: low Active rate 0/5 (0%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 27/164 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 298 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
