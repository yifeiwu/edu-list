# Edu-Domains — Run Summary

_Generated 2026-11-02 20:26 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **23213** across **205** countries
- Active: **12438** (54%) · Inaccessible: **10775** (46%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10293** domains (median 21 yrs)

## Last runs

- Verify (2026-11-02 20:26 UTC): validated 75, +35 Active, re-verified 15, pending left 0
- Curate (2026-11-02 18:00 UTC): 10692 raw candidates, 59 queued, 35 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4683 | 3541 | 1142 |
| FR | 3071 | 1487 | 1584 |
| CN | 1301 | 148 | 1153 |
| IN | 828 | 450 | 378 |
| JP | 805 | 224 | 581 |
| AU | 736 | 537 | 199 |
| DE | 607 | 340 | 267 |
| RU | 590 | 230 | 360 |
| BR | 579 | 286 | 293 |
| ID | 568 | 342 | 226 |
| UA | 469 | 194 | 275 |
| PL | 458 | 179 | 279 |
| ES | 411 | 264 | 147 |
| KR | 347 | 96 | 251 |
| GB | 345 | 187 | 158 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12443 |
| `unreachable-dns` | 3259 |
| `fetch-error:ConnectTimeout` | 1396 |
| `fetch-error:ConnectionError` | 1146 |
| `low-confidence:http-2xx-html` | 1095 |
| `fetch-error:SSLError` | 1052 |
| `http-403` | 1031 |
| `empty-body` | 223 |
| `fetch-error:ReadTimeout` | 130 |
| `http-500` | 128 |
| `http-404` | 90 |
| `http-503` | 51 |

## Freshness

- Verified in last 30 days: **15139** (65%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3259**
- Moved pointers (old domain → new): **968**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 148/1301 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 224/805 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/347 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 23/155 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 52 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
