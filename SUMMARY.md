# Edu-Domains — Run Summary

_Generated 2026-10-31 07:05 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **22743** across **205** countries
- Active: **12160** (53%) · Inaccessible: **10583** (47%)
- Pending queue: **0** unvalidated candidates
- Known registration age: **10050** domains (median 21 yrs)

## Last runs

- Verify (2026-10-31 07:05 UTC): validated 70, +23 Active, re-verified 15, pending left 0
- Curate (2026-10-31 06:46 UTC): 10701 raw candidates, 52 queued, 47 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4601 | 3477 | 1124 |
| FR | 2982 | 1446 | 1536 |
| CN | 1288 | 146 | 1142 |
| IN | 807 | 435 | 372 |
| JP | 798 | 221 | 577 |
| AU | 736 | 537 | 199 |
| DE | 606 | 339 | 267 |
| RU | 583 | 226 | 357 |
| BR | 573 | 282 | 291 |
| ID | 548 | 327 | 221 |
| PL | 451 | 178 | 273 |
| UA | 426 | 180 | 246 |
| ES | 407 | 262 | 145 |
| KR | 341 | 96 | 245 |
| GB | 302 | 154 | 148 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 12165 |
| `unreachable-dns` | 3232 |
| `fetch-error:ConnectTimeout` | 1365 |
| `fetch-error:ConnectionError` | 1120 |
| `low-confidence:http-2xx-html` | 1061 |
| `fetch-error:SSLError` | 1027 |
| `http-403` | 1015 |
| `empty-body` | 218 |
| `http-500` | 127 |
| `fetch-error:ReadTimeout` | 126 |
| `http-404` | 89 |
| `http-503` | 49 |

## Freshness

- Verified in last 30 days: **15531** (68%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **4**
- Retired, no DNS record (`unreachable-dns`): **3232**
- Moved pointers (old domain → new): **951**

## Alerts

- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 146/1288 (11%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 221/798 (28%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 96/341 (28%) — check for blocks/stale sources
- ⚠ `SL`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 22/152 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 33 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
