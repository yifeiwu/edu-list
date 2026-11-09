# Edu-Domains — Run Summary

_Generated 2026-11-09 15:36 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **24037** across **205** countries
- Active: **12932** (54%) · Inaccessible: **11105** (46%)
- Pending queue: **33** unvalidated candidates
- Known registration age: **10636** domains (median 21 yrs)

## Last runs

- Verify (2026-11-09 08:01 UTC): validated 61, +27 Active, re-verified 15, pending left 0
- Curate (2026-11-09 15:36 UTC): 10698 raw candidates, 33 queued, 58 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4733 | 3582 | 1151 |
| FR | 3338 | 1612 | 1726 |
| CN | 1331 | 154 | 1177 |
| IN | 876 | 486 | 390 |
| JP | 809 | 226 | 583 |
| AU | 740 | 541 | 199 |
| DE | 612 | 345 | 267 |
| RU | 607 | 243 | 364 |
| BR | 591 | 303 | 288 |
| ID | 584 | 352 | 232 |
| UA | 573 | 243 | 330 |
| PL | 461 | 180 | 281 |
| ES | 414 | 266 | 148 |
| GB | 368 | 203 | 165 |
| KR | 350 | 98 | 252 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12937 |
| `unreachable-dns` | 3317 |
| `fetch-error:ConnectTimeout` | 1454 |
| `fetch-error:ConnectionError` | 1215 |
| `low-confidence:http-2xx-html` | 1142 |
| `fetch-error:SSLError` | 1071 |
| `http-403` | 1051 |
| `empty-body` | 233 |
| `http-500` | 138 |
| `fetch-error:ReadTimeout` | 137 |
| `http-404` | 91 |
| `http-503` | 53 |

## Freshness

- Verified in last 30 days: **12597** (52%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3317**
- Moved pointers (old domain → new): **991**

## Alerts

- ⚠ `BI`: low Active rate 2/10 (20%) — check for blocks/stale sources
- ⚠ `BY`: low Active rate 17/57 (30%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 154/1331 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 226/809 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 98/350 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 24/157 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/8 (25%) — check for blocks/stale sources
- ⚠ `XX`: 128 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
