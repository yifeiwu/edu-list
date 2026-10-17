# Edu-Domains — Run Summary

_Generated 2026-10-17 23:34 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18290** across **205** countries
- Active: **9918** (54%) · Inaccessible: **8372** (46%)
- Pending queue: **1247** unvalidated candidates
- Known registration age: **8099** domains (median 23 yrs)

## Last runs

- Verify (2026-10-17 23:34 UTC): validated 117, +64 Active, re-verified 15, pending left 1247
- Curate (2026-10-17 22:02 UTC): 10699 raw candidates, 47 queued, 40 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3821 | 2876 | 945 |
| FR | 2058 | 1025 | 1033 |
| CN | 743 | 100 | 643 |
| AU | 729 | 529 | 200 |
| IN | 666 | 341 | 325 |
| JP | 644 | 156 | 488 |
| DE | 592 | 329 | 263 |
| BR | 497 | 243 | 254 |
| ID | 439 | 271 | 168 |
| RU | 423 | 146 | 277 |
| PL | 409 | 169 | 240 |
| KR | 316 | 86 | 230 |
| GB | 284 | 144 | 140 |
| IR | 254 | 80 | 174 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9922 |
| `unreachable-dns` | 2684 |
| `fetch-error:ConnectTimeout` | 1035 |
| `http-403` | 854 |
| `fetch-error:SSLError` | 832 |
| `fetch-error:ConnectionError` | 816 |
| `low-confidence:http-2xx-html` | 742 |
| `empty-body` | 180 |
| `fetch-error:ReadTimeout` | 96 |
| `http-500` | 75 |
| `http-404` | 58 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18269** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2684**
- Moved pointers (old domain → new): **815**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 100/743 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 156/644 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/119 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 13 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
