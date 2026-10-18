# Edu-Domains — Run Summary

_Generated 2026-10-18 06:49 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18491** across **205** countries
- Active: **10010** (54%) · Inaccessible: **8481** (46%)
- Pending queue: **1153** unvalidated candidates
- Known registration age: **8172** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 06:49 UTC): validated 115, +46 Active, re-verified 15, pending left 1153
- Curate (2026-10-18 05:32 UTC): 10701 raw candidates, 47 queued, 39 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3864 | 2908 | 956 |
| FR | 2101 | 1043 | 1058 |
| CN | 782 | 103 | 679 |
| AU | 731 | 530 | 201 |
| IN | 667 | 342 | 325 |
| JP | 650 | 159 | 491 |
| DE | 593 | 330 | 263 |
| BR | 500 | 247 | 253 |
| ID | 442 | 271 | 171 |
| RU | 424 | 146 | 278 |
| PL | 409 | 169 | 240 |
| KR | 316 | 86 | 230 |
| GB | 284 | 144 | 140 |
| IR | 255 | 80 | 175 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10014 |
| `unreachable-dns` | 2719 |
| `fetch-error:ConnectTimeout` | 1052 |
| `http-403` | 860 |
| `fetch-error:SSLError` | 842 |
| `fetch-error:ConnectionError` | 832 |
| `low-confidence:http-2xx-html` | 752 |
| `empty-body` | 184 |
| `fetch-error:ReadTimeout` | 96 |
| `http-500` | 79 |
| `http-404` | 62 |
| `http-503` | 36 |

## Freshness

- Verified in last 30 days: **18394** (99%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2719**
- Moved pointers (old domain → new): **816**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 103/782 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 159/650 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/127 (15%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 15 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
