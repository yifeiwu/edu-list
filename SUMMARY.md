# Edu-Domains — Run Summary

_Generated 2026-10-21 21:51 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **20643** across **205** countries
- Active: **11069** (54%) · Inaccessible: **9574** (46%)
- Pending queue: **43** unvalidated candidates
- Known registration age: **9119** domains (median 22 yrs)

## Last runs

- Verify (2026-10-21 21:51 UTC): validated 120, +63 Active, re-verified 15, pending left 43
- Curate (2026-10-21 18:29 UTC): 10671 raw candidates, 53 queued, 17 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4323 | 3260 | 1063 |
| FR | 2523 | 1227 | 1296 |
| CN | 1197 | 136 | 1061 |
| IN | 737 | 382 | 355 |
| AU | 734 | 534 | 200 |
| JP | 708 | 189 | 519 |
| DE | 598 | 334 | 264 |
| BR | 525 | 259 | 266 |
| ID | 495 | 296 | 199 |
| RU | 473 | 174 | 299 |
| PL | 416 | 172 | 244 |
| KR | 331 | 90 | 241 |
| ES | 303 | 188 | 115 |
| GB | 289 | 147 | 142 |
| MX | 280 | 154 | 126 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11074 |
| `unreachable-dns` | 3005 |
| `fetch-error:ConnectTimeout` | 1191 |
| `fetch-error:ConnectionError` | 993 |
| `http-403` | 955 |
| `fetch-error:SSLError` | 922 |
| `low-confidence:http-2xx-html` | 907 |
| `empty-body` | 203 |
| `fetch-error:ReadTimeout` | 112 |
| `http-500` | 106 |
| `http-404` | 78 |
| `http-503` | 42 |

## Freshness

- Verified in last 30 days: **18721** (91%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **3005**
- Moved pointers (old domain → new): **880**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 136/1197 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 189/708 (27%) — check for blocks/stale sources
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
