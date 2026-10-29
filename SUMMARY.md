# Edu-Domains — Run Summary

_Generated 2026-10-29 21:42 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22363** across **205** countries
- Active: **11978** (54%) · Inaccessible: **10385** (46%)
- Pending queue: **45** unvalidated candidates
- Known registration age: **9875** domains (median 22 yrs)

## Last runs

- Verify (2026-10-29 18:30 UTC): validated 58, +26 Active, re-verified 15, pending left 0
- Curate (2026-10-29 21:42 UTC): 10686 raw candidates, 45 queued, 41 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4562 | 3443 | 1119 |
| FR | 2901 | 1412 | 1489 |
| CN | 1278 | 144 | 1134 |
| IN | 799 | 429 | 370 |
| JP | 797 | 221 | 576 |
| AU | 736 | 537 | 199 |
| DE | 605 | 338 | 267 |
| BR | 569 | 281 | 288 |
| ID | 540 | 319 | 221 |
| RU | 532 | 202 | 330 |
| PL | 423 | 174 | 249 |
| ES | 405 | 261 | 144 |
| KR | 336 | 94 | 242 |
| UA | 331 | 140 | 191 |
| GB | 300 | 153 | 147 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 11983 |
| `unreachable-dns` | 3189 |
| `fetch-error:ConnectTimeout` | 1327 |
| `fetch-error:ConnectionError` | 1096 |
| `low-confidence:http-2xx-html` | 1037 |
| `http-403` | 1000 |
| `fetch-error:SSLError` | 998 |
| `empty-body` | 213 |
| `fetch-error:ReadTimeout` | 125 |
| `http-500` | 122 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **16123** (72%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3189**
- Moved pointers (old domain → new): **940**

## Alerts

- ⚠ `AO`: low Active rate 4/15 (27%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 144/1278 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/797 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 94/336 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 21/150 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
