# Data sources, licenses & attribution

Output CSVs (`data/countries/*.csv`) redistribute facts (names + domains)
with per-row `sources` citations. Honor each upstream's terms:

| Source | What we take | License | Notes |
|---|---|---|---|
| Hipo university-domains-list | name, domains, web_pages, country | MIT | Cite `hipo:YYYY-MM-DD`; link repo. |
| ROR (API) | name, website, country | CC0 | Cite `ror:api-pN`. Monthly releases. |
| OpenAlex Institutions | display_name, homepage_url, country_code, ror | CC0 | Cite `openalex:pageN`. |
| Wikidata (P856) | label, website, country ISO | CC0 | Cite `wikidata:P856`. Respect QS rate limits. |
| ETER / OrgReg | HEI reference list | EU open data | Configure export URL; cite `eter:YYYY-MM-DD`. |
| US College Scorecard bulk | school name + URL | US public domain | Keyless bulk zip; cite `scorecard:YYYY-MM`. |
| UK GIAS | establishment website (K-12, gated) | OGL v3.0 | Cite `gias:YYYY-MM-DD`. |
| FR Annuaire / sup-recherche | nom + site web | Etalab-2.0 | Cite `fr-annuaire:YYYY-MM-DD`. |
| UGC India | university name + View Website | IN open data | Polite ≤50/run; cite `ugc-in:YYYY-MM-DD`. |
| OpenStreetMap (Overpass) | name + website tags (K-12, gated) | ODbL | Attribute `© OpenStreetMap contributors`; cite `osm:<bbox>`. Share-alike applies to OSM-derived rows. |
| Giga Maps (gated) | school names/locations | Open data | Mostly no websites; K-12 names only. |
| crt.sh (CT logs) | newly-issued hosts per academic suffix | Public logs | Cite `crtsh:<suffix>`. |
| WHED / IAU | gap-filler only, ≤10 detail pages/run | Proprietary — limited | Cite `whed:IAU-XXXXXX`, link back, no bulk copy without consent (`centre@iau.global`). |
| edudirectory.school | hints only | Third-party | Single-page, robots-respecting. |
| Common Crawl | optional host existence | Public crawl | Demoted (biased to .edu). |

UNESCO-UIS statistics are **not** ingested (no domains). Wayback is **not** used
(per project decision).

## Removal / opt-out

Schools: open an issue or PR editing `config.yaml` `blocklist` with your domain,
or contact the repo owner listed in `config.yaml` (`validation.user_agent`).
Blocklisted domains are never (re-)added and existing rows are removed on next run.
