# Edu-Domains (Global, Free-Tier)

Incremental GitHub Actions crawler building **per-country** lists of real,
working educational-institution websites — without relying on `.edu`.

## Output

`data/countries/<ISO2>.csv` (only created once a country has ≥1 entry),
plus `data/countries/INDEX.md`:

```
school_name,web_domain,type,last_visited,status,sources
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

## How it works (two pipelines)

**Curate** (`src/curate.py`, daily 00:00 UTC) — the rate-limit-sensitive half.
Hits every enabled upstream source once per session, each capped by its
`sources.yaml` per_run: Hipo, ROR, OpenAlex, Wikidata, ETER, Scorecard, GIAS,
FR, UGC-IN, OSM, crt.sh, Common Crawl CDX (school-keyword-filtered over
academic suffixes), WHED-limited. Per-adapter cursors advance coverage
session-to-session. New domains go to the
pending queue (`state/pending.json`); already-known domains just get their
`sources` column unioned. No website fetching.

**Verify** (`src/verify.py`, twice daily 06:00 + 18:00 UTC) — the safe half.
Hits each school website **once** (homepage-only `GET`, 10s timeout,
descriptive UA, 0.4s delay). Hosts are spread worldwide, so no single party
sees meaningful load. Per run: drain pending FIFO first, then re-verify —
~100 oldest piggyback when new domains were validated, else ~600 oldest
`last_visited` rows (skipping chronic failures archived after 6× misses).

Both rewrite only touched country files (sorted), update `INDEX.md` + state,
and commit only on diff. Budget guards stop each run at ~45 min / cap.

`src/crawl.py` remains as a legacy all-in-one wrapper (curate + verify) for
local runs.

## Validation highlights

* Redirect-chain audit (landing on social/parked host ⇒ `Inaccessible`).
* Parking / soft-404 / link-farm / empty-body filters.
* Positive signals: `schema.org` edu types, multilingual keywords per country
  (`universidad/colegio`, `université/lycée/école`, `universitas/sekolah`…),
  structural cues (admissions/academics/contact, canonical, favicon),
  trusted suffixes, **multi-source agreement** (`hipo` + `ror` ⇒ +30).
* Internal `confidence 0–100 + reason + code` kept in `state/state.json`
  (CSV stays exactly the 6 locked columns).

## Quickstart

```bash
pip install -r requirements.txt
# Split pipelines (as Actions runs them):
python src/curate.py --config config.yaml --sources sources.yaml --dry-run
python src/verify.py --config config.yaml --limit 50 --dry-run
# Or legacy all-in-one locally:
python src/crawl.py --config config.yaml --sources sources.yaml --limit 50 --dry-run
```

Force a source: `--source hipo|ror|openalex|wikidata|eter|scorecard|france-annuaire|ugc-in|crtsh|whed|osm|commoncrawl`.

## Config

* `config.yaml`: `run.*` budgets + archive policy + suffix→country map +
  blocklist; `verify.*` caps for the verify pipeline (higher — websites are
  hit once each, distributed).
* `sources.yaml`: registry (id, kind, url, license, per_run). Rotation order =
  file order. Set `enabled: false` to skip; K-12 ids honor `k12_enabled`.
* Replace `YOUR_USER`/`you@example.com` in `config.yaml` UA so operators can
  reach you. Add removals to `blocklist`.

## Free-tier budget (public repo)

Public repos get unlimited minutes on standard runners: curate runs **daily**
(~10–30 min) and verify **twice daily** (~20–45 min). Caps exist to respect
upstream politeness (Wikidata, Overpass, crt.sh for curate; per-site delay
for verify), not minutes. Artifacts kept 14 days. On a private Free plan the
same setup would use ~1,500–3,000 min/month — over the 2,000-min quota, so
staying public matters.

## Licenses & attribution

See `SOURCES.md`. OSM-derived rows require `© OpenStreetMap contributors`.
WHED is a polite ≤10-pages/run gap-filler (no bulk copy). UNESCO-UIS and
Wayback are intentionally unused.

## Disclaimer

Research/transparency use only; verify via official channels before relying
on any entry. No student data, emails, or precise K-12 coordinates published.
