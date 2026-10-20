# Edu-Domains — Run Summary

_Generated 2026-10-20 12:29 UTC. Full per-country table: [data/countries/INDEX.md](data/countries/INDEX.md)._

## Totals

- Domains tracked: **19817** across **205** countries
- Active: **10662** (54%) · Inaccessible: **9155** (46%)
- Pending queue: **450** unvalidated candidates
- Known registration age: **8795** domains (median 23 yrs)

## Last runs

- Verify (2026-10-20 12:29 UTC): validated 118, +40 Active, re-verified 15, pending left 450
- Curate (2026-10-20 09:52 UTC): 10701 raw candidates, 66 queued, 36 re-cited

## Countries (top 15 by size)

| country | total | Active | Inaccessible |
|---|---|---|---|
| US | 4140 | 3122 | 1018 |
| FR | 2385 | 1170 | 1215 |
| CN | 991 | 120 | 871 |
| AU | 733 | 533 | 200 |
| IN | 722 | 369 | 353 |
| JP | 701 | 186 | 515 |
| DE | 597 | 333 | 264 |
| BR | 514 | 254 | 260 |
| ID | 492 | 295 | 197 |
| RU | 462 | 172 | 290 |
| PL | 412 | 171 | 241 |
| KR | 330 | 89 | 241 |
| GB | 288 | 146 | 142 |
| IR | 264 | 83 | 181 |
| CA | 232 | 143 | 89 |

## Validation signals (reasons in state detail)

| reason | count |
|---|---|
| `http-2xx-html` | 10666 |
| `unreachable-dns` | 2894 |
| `fetch-error:ConnectTimeout` | 1133 |
| `http-403` | 932 |
| `fetch-error:ConnectionError` | 920 |
| `fetch-error:SSLError` | 890 |
| `low-confidence:http-2xx-html` | 853 |
| `empty-body` | 199 |
| `fetch-error:ReadTimeout` | 107 |
| `http-500` | 95 |
| `http-404` | 74 |
| `http-503` | 39 |

## Freshness

- Verified in last 30 days: **18495** (93%)
- Older than 90 days: **0** (oldest check 2026-09-16)
- Archived chronic failures (re-check paused): **2**
- Retired, no DNS record (`unreachable-dns`): **2894**
- Moved pointers (old domain → new): **849**

## Alerts

- ⚠ `AO`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `BW`: low Active rate 3/11 (27%) — check for blocks/stale sources
- ⚠ `CN`: low Active rate 120/991 (12%) — check for blocks/stale sources
- ⚠ `CU`: low Active rate 3/14 (21%) — check for blocks/stale sources
- ⚠ `GA`: low Active rate 2/11 (18%) — check for blocks/stale sources
- ⚠ `GN`: low Active rate 1/10 (10%) — check for blocks/stale sources
- ⚠ `JP`: low Active rate 186/701 (27%) — check for blocks/stale sources
- ⚠ `KR`: low Active rate 89/330 (27%) — check for blocks/stale sources
- ⚠ `MM`: low Active rate 4/14 (29%) — check for blocks/stale sources
- ⚠ `NA`: low Active rate 1/5 (20%) — check for blocks/stale sources
- ⚠ `TW`: low Active rate 19/136 (14%) — check for blocks/stale sources
- ⚠ `VA`: low Active rate 2/7 (29%) — check for blocks/stale sources
- ⚠ `XX`: 17 unmapped countries — expand `suffix_country` or fix source ISO

## Pipelines

- Curate hourly at :00 UTC (`src/curate.py`): upstream discovery → `state/pending.json`.
- Verify every 30 min at :15/:45 UTC (`src/verify.py`): homepage checks + registration age → `data/countries/*.csv`.
- Schema: `school_name,web_domain,type,last_visited,status,sources,years_registered,confidence,reason,final_domain,language`.
- `status` is Active only on final HTTP 2xx + HTML + confidence with valid TLS; any non-2xx or TLS error is Inaccessible. `years_registered` is informational and never gates status.
