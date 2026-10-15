# Edu-Domains — Run Summary

_Generated 2026-10-15 07:37 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **16527** across **204** countries
- Active: **8940** (54%) · Inaccessible: **7587** (46%)
- Pending queue: **2237** unvalidated candidates
- Known registration age: **7097** domains (median 24 yrs)

## Last runs

- Verify (2026-10-15 07:37 UTC): validated 119, +46 Active, re-verified 15, pending left 2237
- Curate (2026-10-15 03:47 UTC): 10687 raw candidates, 52 queued, 10573 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 3404 | 2563 | 841 |
| FR | 1707 | 864 | 843 |
| AU | 692 | 503 | 189 |
| IN | 641 | 322 | 319 |
| JP | 630 | 148 | 482 |
| CN | 601 | 80 | 521 |
| DE | 591 | 328 | 263 |
| BR | 485 | 233 | 252 |
| RU | 416 | 142 | 274 |
| KR | 313 | 85 | 228 |
| GB | 280 | 142 | 138 |
| ID | 272 | 160 | 112 |
| IR | 251 | 79 | 172 |
| CA | 219 | 133 | 86 |
| MX | 217 | 114 | 103 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 8942 |
| `unreachable-dns` | 2538 |
| `fetch-error:ConnectTimeout` | 943 |
| `http-403` | 775 |
| `fetch-error:SSLError` | 750 |
| `fetch-error:ConnectionError` | 700 |
| `low-confidence:http-2xx-html` | 597 |
| `empty-body` | 167 |
| `fetch-error:ReadTimeout` | 90 |
| `http-500` | 65 |
| `http-404` | 51 |
| `http-503` | 31 |

## Freshness

- Verified in last 30 days: **16527** (100%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2538**
- Moved pointers (old domain → new): **738**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BI`: low Active rate 1/7 (14%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CI`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 80/601 (13%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/8 (12%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 148/630 (23%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 85/313 (27%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 15/107 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 8 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
