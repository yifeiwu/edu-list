# Edu-Domains — Run Summary

_Generated 2026-10-14 06:30 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **15910** across **204** countries
- Active: **8636** (54%) · Inaccessible: **7274** (46%)
- Pending queue: **2594** unvalidated candidates
- Known registration age: **6851** domains (median 24 yrs)

## Last runs

- Verify (2026-10-14 06:30 UTC): validated 119, +48 Active, re-verified 15, pending left 2594
- Curate (2026-10-14 06:00 UTC): 10691 raw candidates, 53 queued, 32 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3313 | 2496 | 817 |
| FR | 1571 | 792 | 779 |
| AU | 689 | 500 | 189 |
| JP | 624 | 145 | 479 |
| IN | 622 | 313 | 309 |
| DE | 590 | 328 | 262 |
| CN | 525 | 68 | 457 |
| BR | 483 | 233 | 250 |
| RU | 410 | 138 | 272 |
| KR | 310 | 85 | 225 |
| GB | 272 | 136 | 136 |
| ID | 270 | 160 | 110 |
| IR | 245 | 77 | 168 |
| CA | 218 | 132 | 86 |
| MX | 215 | 112 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8638 |
| `unreachable-dns` | 2480 |
| `fetch-error:ConnectTimeout` | 905 |
| `http-403` | 753 |
| `fetch-error:SSLError` | 706 |
| `fetch-error:ConnectionError` | 648 |
| `low-confidence:http-2xx-html` | 556 |
| `empty-body` | 162 |
| `fetch-error:ReadTimeout` | 84 |
| `http-500` | 56 |
| `http-404` | 47 |
| `http-503` | 30 |

## Freshness

- Verified in last 30 days: **15910** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2480**
- Moved pointers (old domain → new): **713**

## Alerts

- ⚠ `AO`: low Active rate 3/12 (25%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 68/525 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 145/624 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/310 (27%) — check for blocks/stale sources
- ⚠ `MG`: low Active rate 1/6 (17%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 13/102 (13%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
