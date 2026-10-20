# Edu-Domains — Run Summary

_Generated 2026-10-20 19:03 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19919** across **205** countries
- Active: **10711** (54%) · Inaccessible: **9208** (46%)
- Pending queue: **467** unvalidated candidates
- Known registration age: **8828** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 17:22 UTC): validated 117, +50 Active, re-verified 15, pending left 408
- Curate (2026-10-20 19:03 UTC): 10693 raw candidates, 59 queued, 25 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4159 | 3137 | 1022 |
| FR | 2405 | 1180 | 1225 |
| CN | 1017 | 120 | 897 |
| AU | 734 | 534 | 200 |
| IN | 724 | 370 | 354 |
| JP | 701 | 186 | 515 |
| DE | 597 | 333 | 264 |
| BR | 514 | 254 | 260 |
| ID | 492 | 295 | 197 |
| RU | 462 | 172 | 290 |
| PL | 412 | 171 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 264 | 83 | 181 |
| MX | 245 | 130 | 115 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10715 |
| `unreachable-dns` | 2908 |
| `fetch-error:ConnectTimeout` | 1141 |
| `http-403` | 935 |
| `fetch-error:ConnectionError` | 930 |
| `fetch-error:SSLError` | 893 |
| `low-confidence:http-2xx-html` | 860 |
| `empty-body` | 198 |
| `fetch-error:ReadTimeout` | 108 |
| `http-500` | 95 |
| `http-404` | 75 |
| `http-503` | 40 |

## Freshness

- Verified in last 30 days: **18612** (93%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2908**
- Moved pointers (old domain → new): **852**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 120/1017 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 186/701 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `MM`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 20/137 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 17 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
