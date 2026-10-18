# Edu-Domains — Run Summary

_Generated 2026-10-18 14:22 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18592** across **205** countries
- Active: **10055** (54%) · Inaccessible: **8537** (46%)
- Pending queue: **1162** unvalidated candidates
- Known registration age: **8209** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 11:54 UTC): validated 116, +43 Active, re-verified 15, pending left 1101
- Curate (2026-10-18 14:22 UTC): 10701 raw candidates, 61 queued, 33 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3883 | 2922 | 961 |
| FR | 2118 | 1049 | 1069 |
| CN | 806 | 104 | 702 |
| AU | 731 | 531 | 200 |
| IN | 667 | 342 | 325 |
| JP | 656 | 161 | 495 |
| DE | 594 | 331 | 263 |
| BR | 501 | 248 | 253 |
| ID | 448 | 272 | 176 |
| RU | 435 | 155 | 280 |
| PL | 410 | 170 | 240 |
| KR | 316 | 86 | 230 |
| GB | 284 | 144 | 140 |
| IR | 255 | 80 | 175 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10059 |
| `unreachable-dns` | 2744 |
| `fetch-error:ConnectTimeout` | 1058 |
| `http-403` | 869 |
| `fetch-error:SSLError` | 843 |
| `fetch-error:ConnectionError` | 838 |
| `low-confidence:http-2xx-html` | 753 |
| `empty-body` | 187 |
| `fetch-error:ReadTimeout` | 98 |
| `http-500` | 79 |
| `http-404` | 64 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18510** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2744**
- Moved pointers (old domain → new): **817**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 104/806 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 161/656 (25%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/130 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
