# Edu-Domains — Run Summary

_Generated 2026-10-12 02:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15090** across **204** countries
- Active: **8135** (54%) · Inaccessible: **6955** (46%)
- Pending queue: **2987** unvalidated candidates
- Known registration age: **6601** domains (median 24 yrs)

## Last runs

- Verify (2026-10-12 02:29 UTC): validated 119, +62 Active, re-verified 15, pending left 2987
- Curate (2026-10-12 00:19 UTC): 10686 raw candidates, 47 queued, 10574 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3205 | 2405 | 800 |
| FR | 1384 | 713 | 671 |
| JP | 614 | 140 | 474 |
| AU | 613 | 433 | 180 |
| IN | 612 | 308 | 304 |
| DE | 585 | 325 | 260 |
| CN | 501 | 63 | 438 |
| BR | 477 | 229 | 248 |
| RU | 406 | 136 | 270 |
| KR | 306 | 84 | 222 |
| GB | 271 | 135 | 136 |
| ID | 269 | 159 | 110 |
| IR | 237 | 73 | 164 |
| CA | 209 | 123 | 86 |
| TR | 203 | 137 | 66 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8137 |
| `unreachable-dns` | 2428 |
| `fetch-error:ConnectTimeout` | 844 |
| `http-403` | 729 |
| `fetch-error:SSLError` | 681 |
| `fetch-error:ConnectionError` | 608 |
| `low-confidence:http-2xx-html` | 492 |
| `empty-body` | 157 |
| `fetch-error:ReadTimeout` | 80 |
| `http-500` | 46 |
| `http-404` | 42 |
| `http-503` | 29 |

## Freshness

- Verified in last 30 days: **15090** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2428**
- Moved pointers (old domain → new): **688**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 63/501 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 140/614 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 84/306 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 12/101 (12%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 4 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
