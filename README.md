# Edu-Domains (Global, Free-Tier)

Incremental GitHub Actions crawler building **per-country** lists of real,
working educational-institution websites — without relying on `.edu`.

Live project health: **[SUMMARY.md](SUMMARY.md)** (regenerated every run:
totals, last runs, top countries, signals, freshness).

## Output

`data/countries/<ISO2>.csv` (only created once a country has ≥1 entry),
plus `data/countries/INDEX.md`:

```
school_name,web_domain,type,last_visited,status,sources,years_registered
```

* `web_domain`: canonical registrable domain (lowercased, no `www`, punycode).
  Facebook/social-only or site-builder placeholders never count — those rows
  are `Inaccessible`, never `Active`.
* `type`: `k-12` | `university/college` | `other`.
* `last_visited`: `YYYY-MM-DD` of last crawler check.
* `status`: `Active` (final HTTP **2xx** + HTML + confidence ≥ 50) else
  `Inaccessible` — **any non-2xx is `Inaccessible`**, including 401/403/5xx,
  timeouts, DNS/TLS failures.
* `sources`: `;`-separated citations, first-seen order, e.g.
  `hipo:2026-09-11;ror:api-p3;wikidata:P856`.
* `years_registered`: whole years since domain registration (RDAP, port-43
  fallback for `.edu`/`.uk`), `""` when unknown. Informational — never gates
  `status`.

## How it works (two pipelines)

**Curate** (`src/curate.py`, hourly at :00 UTC) — the rate-limit-sensitive half.
Hits every enabled upstream source once per session, each capped by its
strict hourly `sources.yaml` per_run: Hipo, ROR, OpenAlex, Wikidata,
Scorecard (US), FR Annuaire, OSM, WHED-limited, dotgov (US districts),
CRICOS (AU), NUC (NG), NZ Schools (removed sources documented in
SOURCES.md). Per-adapter cursors advance coverage
session-to-session. New domains go to the
pending queue (`state/pending.json`); already-known domains just get their
`sources` column unioned. No website fetching.

**Verify** (`src/verify.py`, hourly at :30 UTC) — the safe half.
Hits each school website **once** (homepage-only `GET`, 10s timeout,
descriptive UA, 0.4s delay). Hosts are spread worldwide, so no single party
sees meaningful load. Per run: drain pending FIFO first, then re-verify —
~15 oldest piggyback when new domains were validated, else ~60 oldest
`last_visited` rows (skipping chronic failures archived after 6× misses).

Both rewrite only touched country files (sorted), update `INDEX.md` + state,
and commit only on diff. Budget guards stop each run at ~25 min / cap.

`src/crawl.py` remains as a legacy all-in-one wrapper (curate + verify) for
local runs.

## Validation highlights

* Redirect-chain audit: cross-domain moves are chased, not misattributed —
  the old domain is marked `moved-to:<new>` and the target is validated as
  its own row (`redirect:<old>` provenance). Social/placeholder landings stay
  `Inaccessible`.
* TLS strictness: valid TLS is required — expired/self-signed/broken chains
  are `Inaccessible` (one `www`-variant retry covers apex-vs-www cert
  mismatches). No unverified fallback.
* Parking / soft-404 / link-farm / empty-body filters; the link-farm check
  exempts pages whose title/H1 already names an institution (real portals
  open with link-heavy navs).
* Service-host demotion: webmail/LMS/meeting endpoints (`mail.*`,
  `moodle.*`, `*.zoom.us`…) are reachable but never the school website —
  capped below Active, tagged `service-host`; redirect targets of that kind
  don't get their own rows.
* Positive signals: `schema.org` edu types, multilingual keywords per country
  (`universidad/colegio`, `université/lycée/école`, `universitas/sekolah`…),
  structural cues (admissions/academics/contact, canonical, favicon),
  trusted suffixes, **multi-source agreement** (`hipo` + `ror` ⇒ +30).
* Internal `confidence 0–100 + reason + code` kept in `state/state.json`
  (CSV stays exactly the documented columns).

## Quickstart

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # tests/lint/types
pytest -q
# Split pipelines (as Actions runs them):
python src/curate.py --config config.yaml --sources sources.yaml --dry-run
python src/verify.py --config config.yaml --limit 50 --dry-run
# Offline (no network, for tests):
python src/curate.py --no-network
python src/verify.py --no-network
# Or legacy all-in-one locally:
python src/crawl.py --config config.yaml --sources sources.yaml --limit 50 --dry-run
```

Force a source: `--source hipo|ror|openalex|wikidata|scorecard|france-annuaire|whed|osm|dotgov|cricos|nuc-ng|nz-schools|deqar|ipeds|eter`.

## Config

* `config.yaml`: `run.*` budgets + archive policy + suffix→country map +
  blocklist; `verify.*` caps for the verify pipeline (hourly scale — websites
  are hit once each, distributed).
* `sources.yaml`: registry (id, kind, url, license, per_run). Rotation order =
  file order. Set `enabled: false` to skip; K-12 ids honor `k12_enabled`.
* Replace `YOUR_USER`/`you@example.com` in `config.yaml` UA so operators can
  reach you. Add removals to `blocklist`.

## Free-tier budget (public repo)

Public repos get unlimited minutes on standard runners: curate runs **hourly**
at :00 (~5–15 min, strict per-source caps) and verify **hourly** at :30
(~10–25 min, ~125 validations/run). Caps exist to respect upstream
politeness (Wikidata, Overpass for curate; per-site delay for verify), not
minutes. Artifacts kept 14 days. On a private Free plan the same setup would
far exceed the 2,000-min/month quota (24 + 24 short runs/day), so staying
public matters.

## Licenses & attribution

See `SOURCES.md`. OSM-derived rows require `© OpenStreetMap contributors`.
WHED is a polite ≤10-pages/run gap-filler (no bulk copy). UNESCO-UIS and
Wayback are intentionally unused.

## Disclaimer

Research/transparency use only; verify via official channels before relying
on any entry. No student data, emails, or precise K-12 coordinates published.
