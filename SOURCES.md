# Data sources, licenses & attribution

Output CSVs (`data/countries/*.csv`) redistribute facts (names + domains)
with per-row `sources` citations. Honor each upstream's terms:

| Source | What we take | License | Notes |
|---|---|---|---|
| Hipo university-domains-list | name, domains, web_pages, country | MIT | Whole static file ingested each run (single GET, no paging). Cite `hipo:YYYY-MM-DD`; link repo. |
| ROR (API) | name, website, country | CC0 | Cite `ror:api-pN`. Monthly releases. |
| OpenAlex Institutions | display_name, homepage_url, country_code, ror | CC0 | Cite `openalex:pageN`. |
| Wikidata (P856) | label, website, country ISO | CC0 | Cite `wikidata:P856`. Respect QS rate limits. |
| US College Scorecard bulk | school name + INSTURL | US public domain | Dated release zip auto-resolved from the data page; cite `scorecard:YYYY-MM`. |
| FR Annuaire | nom + site web (website rows only) | Etalab-2.0 | Cite `fr-annuaire:YYYY-MM-DD`. |
| OpenStreetMap (Overpass) | name + website tags | ODbL | Attribute `© OpenStreetMap contributors`; cite `osm:<bbox>`. Share-alike applies to OSM-derived rows. One bbox/session + retries on 429. |
| WHED / IAU | gap-filler only, ≤10 detail pages/session | Proprietary — limited | Cite `whed:IAU-XXXXXX`, link back, no bulk copy without consent (`centre@iau.global`). |
| US .gov zone (CISA dotgov-data) | school-district .gov domains + org names | CC0 | Daily CSV; cite `dotgov:YYYY-MM-DD`. |
| Australia CRICOS register | institution name + Website (1.5k providers) | CC-BY 2.5 AU | CKAN-resolved `CRICOS Institutions.csv`; cite `cricos:YYYY-MM-DD`. |
| Nigeria NUC lists | university name + website (federal/state/private) | NG open data | 3 pages/session; cite `nuc-ng:federal\|state\|private`. |
| NZ Schools Directory | school name + URL (CKAN datastore, paged) | CC-BY 4.0 | Cite `nz-schools:YYYY-MM-DD`. |
| DEQAR institutions | name, website_link, country (daily CSV, ~3MB) | PDDL (public domain) | Cite `deqar:YYYY-MM-DD`. QA-filtered EU higher-ed. |
| US IPEDS HD directory | INSTNM + WEBADDR (year-stamped zip, ~1MB) | US public domain | Year roll-back on 404; cite `ipeds:YYYY-MM`. Broader than Scorecard. |

## Spiked, not added (2026-09-12 — verified, no adapter)

| Source | Verdict |
|---|---|
| Canada ODEF (StatCan ZIP, OGL-Canada) | No website column (name/type/address/coords only) — can't drive discovery. |
| UK APAR (apprenticeships CSV, OGL v3.0) | No website column (UKPRN/name/type only). |
| UK GIAS | Live site 403s bots; no Common Crawl captures of Downloads. Needs form-POST reverse-engineering. |
| UK Live Course Providers CSV | May-2026 file gone (410); no Common Crawl captures. Re-spike when a current monthly file is needed. |
| Brazil MEC dadosabertos | 403 (WAF, even browser UA); no Common Crawl dataset captures. e-MEC is query-UI only. |
| India AISHE / data.gov.in | Dashboard + OGD datasets are stats-only (counts, no names/websites); data.gov.in Akamai-blocks bots and its API needs a personal key; UGC 403s (see Removed); AICTE unreachable; NIRF is ranked-only with no websites. India covered via hipo/ROR/OpenAlex/Wikidata + IN-Delhi OSM box. |
| Philippines CHED | New site 403s bots (no CC captures); legacy list is a Google Apps Script widget (no bulk); data.gov.ph sets are stats-only. Covered via WHED rotation + PH-Manila OSM box. |
| Indonesia PDDikti | Official site behind browser-verification challenge; third-party API gateways are unofficial scrapes (murky license); data.go.id has no usable API. Covered via WHED rotation + ID-Jakarta/ID-Surabaya OSM boxes. |

## Removed (tested, code deleted 2026-09 — re-adding needs a new adapter + tests)

| Source | Verdict from live testing (2026-09-11) |
|---|---|
| UGC India | HTTP 403 (WAF blocks bots, including datacenter IPs). Needs browser/API route. |
| crt.sh | 502s on `%`-wildcard CT queries (full-table scans). Exact-domain lookups work but can't drive discovery. |
| Common Crawl CDX | Prefix scans (`*.edu` + URL-regex filter) time out (504/502). CDX suits known-URL lookups, not discovery sweeps. |
| ETER full dump | Heavy ~93MB/session Zenodo dump; removed 2026-09-14. |
| GIAS (UK) / FR sup-recherche / Giga | No stable bulk URL configured (see spike notes above for UK). |
| edudirectory.school | Hint-only; no bulk endpoint. |

UNESCO-UIS statistics are **not** ingested (no domains). Wayback is **not** used
(per project decision).

## Removal / opt-out

Schools: open an issue or PR editing `config.yaml` `blocklist` with your domain,
or contact the repo owner listed in `config.yaml` (`validation.user_agent`).
Blocklisted domains are never (re-)added and existing rows are removed on next run.
