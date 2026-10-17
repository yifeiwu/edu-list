# Edu-Domains — Run Summary

_Generated 2026-10-17 00:02 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **17565** across **204** countries
- Active: **9521** (54%) · Inaccessible: **8044** (46%)
- Pending queue: **1669** unvalidated candidates
- Known registration age: **7674** domains (median 24 yrs)

## Last runs

- Verify (2026-10-17 00:02 UTC): validated 120, +66 Active, re-verified 15, pending left 1669
- Curate (2026-10-16 23:21 UTC): 10684 raw candidates, 35 queued, 31 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3646 | 2744 | 902 |
| FR | 1926 | 971 | 955 |
| AU | 728 | 529 | 199 |
| CN | 700 | 93 | 607 |
| IN | 653 | 332 | 321 |
| JP | 638 | 153 | 485 |
| DE | 592 | 329 | 263 |
| BR | 493 | 239 | 254 |
| RU | 419 | 144 | 275 |
| ID | 338 | 203 | 135 |
| KR | 314 | 86 | 228 |
| GB | 284 | 144 | 140 |
| PL | 283 | 128 | 155 |
| IR | 254 | 80 | 174 |
| CA | 226 | 139 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9523 |
| `unreachable-dns` | 2627 |
| `fetch-error:ConnectTimeout` | 995 |
| `http-403` | 819 |
| `fetch-error:SSLError` | 794 |
| `fetch-error:ConnectionError` | 768 |
| `low-confidence:http-2xx-html` | 681 |
| `empty-body` | 174 |
| `fetch-error:ReadTimeout` | 94 |
| `http-500` | 71 |
| `http-404` | 54 |
| `http-503` | 35 |

## Freshness

- Verified in last 30 days: **17544** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2627**
- Moved pointers (old domain → new): **785**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
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
