# Edu-Domains — Run Summary

_Generated 2026-10-16 23:21 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17460** across **204** countries
- Active: **9454** (54%) · Inaccessible: **8006** (46%)
- Pending queue: **1769** unvalidated candidates
- Known registration age: **7603** domains (median 24 yrs)

## Last runs

- Verify (2026-10-16 21:54 UTC): validated 121, +58 Active, re-verified 15, pending left 1734
- Curate (2026-10-16 23:21 UTC): 10684 raw candidates, 35 queued, 31 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3637 | 2735 | 902 |
| FR | 1899 | 952 | 947 |
| AU | 722 | 525 | 197 |
| CN | 700 | 93 | 607 |
| IN | 653 | 332 | 321 |
| JP | 638 | 153 | 485 |
| DE | 592 | 329 | 263 |
| BR | 492 | 237 | 255 |
| RU | 418 | 143 | 275 |
| ID | 317 | 189 | 128 |
| KR | 314 | 86 | 228 |
| GB | 283 | 144 | 139 |
| PL | 259 | 118 | 141 |
| IR | 254 | 80 | 174 |
| CA | 226 | 139 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9456 |
| `unreachable-dns` | 2620 |
| `fetch-error:ConnectTimeout` | 995 |
| `http-403` | 811 |
| `fetch-error:SSLError` | 791 |
| `fetch-error:ConnectionError` | 763 |
| `low-confidence:http-2xx-html` | 674 |
| `empty-body` | 173 |
| `fetch-error:ReadTimeout` | 94 |
| `http-500` | 70 |
| `http-404` | 54 |
| `http-503` | 35 |

## Freshness

- Verified in last 30 days: **17460** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2620**
- Moved pointers (old domain → new): **779**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 93/700 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 153/638 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/314 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 18/118 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 12 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
