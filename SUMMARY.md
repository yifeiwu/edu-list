# Edu-Domains — Run Summary

_Generated 2026-11-08 09:33 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23885** across **205** countries
- Active: **12857** (54%) · Inaccessible: **11028** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10586** domains (median 21 yrs)

## Last runs

- Verify (2026-11-08 09:33 UTC): validated 46, +21 Active, re-verified 15, pending left 0
- Curate (2026-11-08 07:00 UTC): 10688 raw candidates, 31 queued, 53 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4724 | 3577 | 1147 |
| FR | 3295 | 1603 | 1692 |
| CN | 1328 | 154 | 1174 |
| IN | 871 | 482 | 389 |
| JP | 809 | 226 | 583 |
| AU | 737 | 538 | 199 |
| DE | 611 | 344 | 267 |
| RU | 605 | 241 | 364 |
| BR | 587 | 300 | 287 |
| ID | 584 | 352 | 232 |
| UA | 572 | 243 | 329 |
| PL | 461 | 180 | 281 |
| ES | 414 | 266 | 148 |
| GB | 367 | 203 | 164 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12862 |
| `unreachable-dns` | 3303 |
| `fetch-error:ConnectTimeout` | 1442 |
| `fetch-error:ConnectionError` | 1200 |
| `low-confidence:http-2xx-html` | 1133 |
| `fetch-error:SSLError` | 1065 |
| `http-403` | 1048 |
| `empty-body` | 230 |
| `http-500` | 135 |
| `fetch-error:ReadTimeout` | 134 |
| `http-404` | 90 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **12975** (54%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3303**
- Moved pointers (old domain → new): **984**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 154/1328 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 109 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
