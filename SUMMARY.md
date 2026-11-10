# Edu-Domains — Run Summary

_Generated 2026-11-10 00:01 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24073** across **205** countries
- Active: **12958** (54%) · Inaccessible: **11115** (46%)
- Pending queue: **47** unvalidated candidates
- Known registration age: **10653** domains (median 21 yrs)

## Last runs

- Verify (2026-11-09 18:50 UTC): validated 51, +25 Active, re-verified 15, pending left 0
- Curate (2026-11-10 00:01 UTC): 10681 raw candidates, 47 queued, 55 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4733 | 3582 | 1151 |
| FR | 3349 | 1620 | 1729 |
| CN | 1335 | 155 | 1180 |
| IN | 877 | 487 | 390 |
| JP | 809 | 226 | 583 |
| AU | 741 | 542 | 199 |
| DE | 612 | 345 | 267 |
| RU | 608 | 244 | 364 |
| BR | 591 | 303 | 288 |
| ID | 586 | 353 | 233 |
| UA | 573 | 243 | 330 |
| PL | 461 | 180 | 281 |
| ES | 417 | 269 | 148 |
| GB | 368 | 203 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12963 |
| `unreachable-dns` | 3318 |
| `fetch-error:ConnectTimeout` | 1457 |
| `fetch-error:ConnectionError` | 1216 |
| `low-confidence:http-2xx-html` | 1144 |
| `fetch-error:SSLError` | 1072 |
| `http-403` | 1050 |
| `empty-body` | 233 |
| `http-500` | 138 |
| `fetch-error:ReadTimeout` | 137 |
| `http-404` | 91 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **12053** (50%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3318**
- Moved pointers (old domain → new): **993**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 155/1335 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 131 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
