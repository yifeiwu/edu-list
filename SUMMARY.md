# Edu-Domains — Run Summary

_Generated 2026-10-15 17:58 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16734** across **204** countries
- Active: **9043** (54%) · Inaccessible: **7691** (46%)
- Pending queue: **2128** unvalidated candidates
- Known registration age: **7185** domains (median 24 yrs)

## Last runs

- Verify (2026-10-15 17:58 UTC): validated 120, +50 Active, re-verified 15, pending left 2128
- Curate (2026-10-15 14:07 UTC): 10672 raw candidates, 61 queued, 26 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3443 | 2591 | 852 |
| FR | 1758 | 884 | 874 |
| AU | 695 | 504 | 191 |
| IN | 642 | 322 | 320 |
| CN | 637 | 83 | 554 |
| JP | 633 | 150 | 483 |
| DE | 591 | 328 | 263 |
| BR | 487 | 235 | 252 |
| RU | 416 | 142 | 274 |
| KR | 314 | 86 | 228 |
| GB | 281 | 144 | 137 |
| ID | 272 | 160 | 112 |
| IR | 252 | 80 | 172 |
| CA | 219 | 133 | 86 |
| MX | 217 | 114 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9045 |
| `unreachable-dns` | 2566 |
| `fetch-error:ConnectTimeout` | 958 |
| `http-403` | 779 |
| `fetch-error:SSLError` | 759 |
| `fetch-error:ConnectionError` | 718 |
| `low-confidence:http-2xx-html` | 611 |
| `empty-body` | 170 |
| `fetch-error:ReadTimeout` | 91 |
| `http-500` | 65 |
| `http-404` | 51 |
| `http-503` | 33 |

## Freshness

- Verified in last 30 days: **16734** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2566**
- Moved pointers (old domain → new): **746**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 83/637 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 150/633 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/314 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 15/108 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
