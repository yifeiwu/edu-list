# Edu-Domains — Run Summary

_Generated 2026-10-16 00:05 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16939** across **204** countries
- Active: **9158** (54%) · Inaccessible: **7781** (46%)
- Pending queue: **2038** unvalidated candidates
- Known registration age: **7300** domains (median 24 yrs)

## Last runs

- Verify (2026-10-16 00:05 UTC): validated 116, +53 Active, re-verified 15, pending left 2038
- Curate (2026-10-15 22:06 UTC): 10697 raw candidates, 54 queued, 41 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3496 | 2628 | 868 |
| FR | 1806 | 911 | 895 |
| AU | 698 | 506 | 192 |
| CN | 663 | 88 | 575 |
| IN | 647 | 326 | 321 |
| JP | 636 | 152 | 484 |
| DE | 592 | 329 | 263 |
| BR | 489 | 235 | 254 |
| RU | 416 | 142 | 274 |
| KR | 314 | 86 | 228 |
| GB | 283 | 144 | 139 |
| ID | 272 | 160 | 112 |
| IR | 252 | 80 | 172 |
| CA | 219 | 133 | 86 |
| IT | 217 | 111 | 106 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9160 |
| `unreachable-dns` | 2584 |
| `fetch-error:ConnectTimeout` | 978 |
| `http-403` | 790 |
| `fetch-error:SSLError` | 762 |
| `fetch-error:ConnectionError` | 727 |
| `low-confidence:http-2xx-html` | 626 |
| `empty-body` | 172 |
| `fetch-error:ReadTimeout` | 90 |
| `http-500` | 65 |
| `http-404` | 53 |
| `http-503` | 34 |

## Freshness

- Verified in last 30 days: **16939** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2584**
- Moved pointers (old domain → new): **755**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 88/663 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 152/636 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/314 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 18/118 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 10 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
