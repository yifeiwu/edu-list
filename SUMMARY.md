# Edu-Domains — Run Summary

_Generated 2026-10-18 01:46 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **18391** across **205** countries
- Active: **9963** (54%) · Inaccessible: **8428** (46%)
- Pending queue: **1206** unvalidated candidates
- Known registration age: **8135** domains (median 23 yrs)

## Last runs

- Verify (2026-10-18 01:46 UTC): validated 116, +48 Active, re-verified 15, pending left 1206
- Curate (2026-10-18 00:43 UTC): 10700 raw candidates, 59 queued, 10578 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3843 | 2891 | 952 |
| FR | 2081 | 1033 | 1048 |
| CN | 763 | 101 | 662 |
| AU | 731 | 530 | 201 |
| IN | 666 | 341 | 325 |
| JP | 650 | 159 | 491 |
| DE | 593 | 330 | 263 |
| BR | 499 | 245 | 254 |
| ID | 441 | 271 | 170 |
| RU | 424 | 146 | 278 |
| PL | 409 | 169 | 240 |
| KR | 316 | 86 | 230 |
| GB | 284 | 144 | 140 |
| IR | 254 | 80 | 174 |
| CA | 227 | 140 | 87 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 9967 |
| `unreachable-dns` | 2703 |
| `fetch-error:ConnectTimeout` | 1045 |
| `http-403` | 858 |
| `fetch-error:SSLError` | 837 |
| `fetch-error:ConnectionError` | 825 |
| `low-confidence:http-2xx-html` | 746 |
| `empty-body` | 181 |
| `fetch-error:ReadTimeout` | 96 |
| `http-500` | 77 |
| `http-404` | 60 |
| `http-503` | 35 |

## Freshness

- Verified in last 30 days: **18279** (99%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2703**
- Moved pointers (old domain → new): **816**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 101/763 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 159/650 (24%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 86/316 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/121 (16%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 14 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
