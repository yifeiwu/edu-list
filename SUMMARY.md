# Edu-Domains — Run Summary

_Generated 2026-11-16 09:10 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **25071** across **206** countries
- Active: **13426** (54%) · Inaccessible: **11645** (46%)
- Pending queue: **41** unvalidated candidates
- Known registration age: **11021** domains (median 21 yrs)

## Last runs

- Verify (2026-11-16 02:11 UTC): validated 65, +21 Active, re-verified 15, pending left 0
- Curate (2026-11-16 09:10 UTC): 10692 raw candidates, 41 queued, 48 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4777 | 3604 | 1173 |
| FR | 3577 | 1729 | 1848 |
| CN | 1372 | 155 | 1217 |
| IN | 923 | 521 | 402 |
| JP | 906 | 256 | 650 |
| AU | 761 | 558 | 203 |
| DE | 622 | 348 | 274 |
| RU | 622 | 251 | 371 |
| ID | 614 | 373 | 241 |
| BR | 602 | 311 | 291 |
| UA | 584 | 252 | 332 |
| PL | 480 | 184 | 296 |
| ES | 421 | 270 | 151 |
| GB | 375 | 210 | 165 |
| KR | 352 | 100 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 13431 |
| `unreachable-dns` | 3444 |
| `fetch-error:ConnectTimeout` | 1537 |
| `fetch-error:ConnectionError` | 1275 |
| `low-confidence:http-2xx-html` | 1252 |
| `fetch-error:SSLError` | 1119 |
| `http-403` | 1080 |
| `empty-body` | 238 |
| `http-500` | 147 |
| `fetch-error:ReadTimeout` | 139 |
| `http-404` | 95 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **9942** (40%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3444**
- Moved pointers (old domain → new): **1044**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/58 (29%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1372 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/15 (20%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 256/906 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 100/352 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 25/159 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 280 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
