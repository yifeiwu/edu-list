# Edu-Domains — Run Summary

_Generated 2026-10-30 02:43 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22466** across **205** countries
- Active: **12026** (54%) · Inaccessible: **10440** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **9905** domains (median 22 yrs)

## Last runs

- Verify (2026-10-30 02:43 UTC): validated 73, +24 Active, re-verified 15, pending left 0
- Curate (2026-10-30 01:42 UTC): 10701 raw candidates, 58 queued, 10587 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4569 | 3448 | 1121 |
| FR | 2925 | 1421 | 1504 |
| CN | 1279 | 144 | 1135 |
| IN | 800 | 430 | 370 |
| JP | 797 | 221 | 576 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 571 | 282 | 289 |
| RU | 558 | 212 | 346 |
| ID | 541 | 320 | 221 |
| PL | 423 | 174 | 249 |
| ES | 407 | 262 | 145 |
| UA | 356 | 150 | 206 |
| KR | 336 | 94 | 242 |
| GB | 301 | 154 | 147 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12031 |
| `unreachable-dns` | 3200 |
| `fetch-error:ConnectTimeout` | 1336 |
| `fetch-error:ConnectionError` | 1106 |
| `low-confidence:http-2xx-html` | 1042 |
| `fetch-error:SSLError` | 1009 |
| `http-403` | 1005 |
| `empty-body` | 214 |
| `fetch-error:ReadTimeout` | 125 |
| `http-500` | 123 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **15786** (70%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3200**
- Moved pointers (old domain → new): **941**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 144/1279 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/797 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/336 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/151 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
