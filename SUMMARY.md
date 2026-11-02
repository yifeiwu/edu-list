# Edu-Domains — Run Summary

_Generated 2026-11-02 10:04 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23153** across **205** countries
- Active: **12401** (54%) · Inaccessible: **10752** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10263** domains (median 21 yrs)

## Last runs

- Verify (2026-11-02 10:04 UTC): validated 71, +32 Active, re-verified 15, pending left 0
- Curate (2026-11-02 07:29 UTC): 10694 raw candidates, 51 queued, 42 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4671 | 3535 | 1136 |
| FR | 3060 | 1482 | 1578 |
| CN | 1301 | 148 | 1153 |
| IN | 825 | 448 | 377 |
| JP | 803 | 223 | 580 |
| AU | 736 | 537 | 199 |
| DE | 607 | 340 | 267 |
| RU | 590 | 230 | 360 |
| BR | 577 | 284 | 293 |
| ID | 566 | 340 | 226 |
| UA | 469 | 194 | 275 |
| PL | 458 | 179 | 279 |
| ES | 411 | 264 | 147 |
| KR | 344 | 96 | 248 |
| GB | 340 | 184 | 156 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12406 |
| `unreachable-dns` | 3256 |
| `fetch-error:ConnectTimeout` | 1394 |
| `fetch-error:ConnectionError` | 1140 |
| `low-confidence:http-2xx-html` | 1092 |
| `fetch-error:SSLError` | 1050 |
| `http-403` | 1025 |
| `empty-body` | 223 |
| `fetch-error:ReadTimeout` | 130 |
| `http-500` | 128 |
| `http-404` | 89 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15064** (65%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3256**
- Moved pointers (old domain → new): **967**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 148/1301 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 223/803 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/344 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/155 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 47 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
