"""Consolidated geographic reference data — single source of truth.

Previously three parallel maps drifted independently:
- `config.yaml` `suffix_country` (user-overridable suffix -> ISO2)
- `util.MULTI_SUFFIXES` (multi-label suffixes for registrable-base)
- `discover.DEQAR_COUNTRY_ISO` (English country name -> ISO2)

This module owns the defaults. `config.yaml` `suffix_country` entries
*override/extend* `DEFAULT_SUFFIX_COUNTRY` at runtime (see `cli_common`
/ `curate` merge). `util` and `discover` re-export from here for
backwards compatibility.
"""
from __future__ import annotations

# Default suffix -> ISO2. Mirrors the former `config.yaml` block.
# Longest-suffix wins at lookup time. Keep sorted-lookup in caller.
DEFAULT_SUFFIX_COUNTRY: dict[str, str] = {
    "edu": "US",
    "ac.uk": "GB",
    "sch.uk": "GB",
    "co.uk": "GB",
    "edu.au": "AU",
    "ac.in": "IN",
    "edu.in": "IN",
    "ac.za": "ZA",
    "sch.za": "ZA",
    "edu.br": "BR",
    "edu.mx": "MX",
    "ac.jp": "JP",
    "edu.ng": "NG",
    "edu.pk": "PK",
    "edu.ph": "PH",
    "edu.eg": "EG",
    "ac.ke": "KE",
    "edu.gh": "GH",
    "ac.ug": "UG",
    "edu.et": "ET",
    "edu.my": "MY",
    "edu.sg": "SG",
    "ac.th": "TH",
    "edu.tr": "TR",
    "edu.ar": "AR",
    "edu.co": "CO",
    "edu.pl": "PL",
    "ac.nz": "NZ",
    "co.nz": "NZ",
    "school.nz": "NZ",
    "edu.nz": "NZ",
    "edu.id": "ID",
    "ac.id": "ID",
    "edu.cn": "CN",
    "edu.hk": "HK",
    "edu.tw": "TW",
    "ac.kr": "KR",
    "edu.kr": "KR",
    "edu.vn": "VN",
    "edu.sa": "SA",
    "edu.bd": "BD",
    "ac.bd": "BD",
    "edu.np": "NP",
    "edu.lk": "LK",
    "ac.lk": "LK",
    "edu.ke": "KE",
    "edu.ug": "UG",
    "edu.tz": "TZ",
    "ac.tz": "TZ",
    "edu.za": "ZA",
    "gob.mx": "MX",
    "gov.mx": "MX",
    "edu.pe": "PE",
    "edu.cl": "CL",
    "edu.py": "PY",
    "edu.uy": "UY",
    "edu.ec": "EC",
    "edu.ve": "VE",
}


def merge_suffix_map(overrides: dict | None) -> dict[str, str]:
    """Defaults + user overrides (`config.yaml` wins on conflict)."""
    merged = dict(DEFAULT_SUFFIX_COUNTRY)
    for k, v in (overrides or {}).items():
        if k and v:
            merged[str(k).lower().strip(".")] = str(v).upper()
    return merged


# Known multi-label public suffixes (subset needed for move detection and
# country inference). Full PSL would need a dependency; this covers academic
# zones plus common second-level domains. Must be a superset of every
# multi-label key in DEFAULT_SUFFIX_COUNTRY.
MULTI_SUFFIXES = frozenset({
    "ac.uk", "sch.uk", "co.uk", "org.uk", "gov.uk",
    "edu.au", "gov.au", "com.au", "org.au",
    "ac.in", "edu.in", "gov.in", "co.in", "res.in",
    "ac.za", "co.za", "org.za", "sch.za", "edu.za", "gov.za",
    "edu.br", "gov.br", "com.br", "org.br",
    "edu.mx", "gob.mx", "gov.mx", "com.mx",
    "ac.jp", "co.jp", "go.jp", "ed.jp",
    "edu.ng", "gov.ng", "com.ng", "org.ng",
    "edu.pk", "gov.pk", "com.pk",
    "edu.ph", "gov.ph", "com.ph",
    "edu.eg", "gov.eg", "com.eg",
    "ac.ke", "co.ke", "go.ke", "or.ke", "edu.ke",
    "edu.gh", "gov.gh", "com.gh",
    "ac.ug", "co.ug", "go.ug", "or.ug", "edu.ug",
    "edu.et", "gov.et", "com.et",
    "edu.my", "gov.my", "com.my",
    "edu.sg", "gov.sg", "com.sg",
    "ac.th", "co.th", "go.th",
    "edu.tr", "gov.tr", "com.tr",
    "edu.ar", "gov.ar", "com.ar",
    "edu.co", "gov.co", "com.co",
    "edu.pl", "gov.pl", "com.pl",
    "edu.id", "ac.id", "co.id", "go.id",
    "ac.nz", "co.nz", "school.nz", "edu.nz", "govt.nz",
    "edu.cn", "ac.cn", "gov.cn", "com.cn",
    "edu.hk", "edu.tw", "ac.kr", "edu.kr", "go.kr", "co.kr",
    "edu.vn", "edu.sa", "edu.bd", "ac.bd",
    "edu.np", "edu.lk", "ac.lk",
    "edu.tz", "ac.tz", "edu.pe", "edu.cl",
    "edu.py", "edu.uy", "edu.ec", "edu.ve",
})


# English country name -> ISO2 for the DEQAR `country` column. Covers the
# EHEA plus the non-EHEA countries DEQAR reports on; unknown names yield "".
DEQAR_COUNTRY_ISO: dict[str, str] = {
    "Albania": "AL", "Andorra": "AD", "Argentina": "AR", "Armenia": "AM",
    "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ", "Bahrain": "BH",
    "Belarus": "BY", "Belgium": "BE", "Belgium (Flemish Community)": "BE",
    "Belgium (French Community)": "BE",
    "Belgium (German-speaking Community)": "BE",
    "Bosnia and Herzegovina": "BA", "Brazil": "BR", "Bulgaria": "BG",
    "Canada": "CA", "Chile": "CL", "China, People's Republic of": "CN",
    "China": "CN", "Colombia": "CO", "Croatia": "HR", "Cyprus": "CY",
    "Czech Republic": "CZ", "Czechia": "CZ", "Denmark": "DK",
    "Estonia": "EE", "Ethiopia": "ET", "Finland": "FI", "France": "FR",
    "Georgia": "GE", "Germany": "DE", "Ghana": "GH", "Greece": "GR",
    "Holy See": "VA", "Hungary": "HU", "Iceland": "IS", "India": "IN",
    "Indonesia": "ID", "Ireland": "IE", "Israel": "IL", "Italy": "IT",
    "Japan": "JP", "Jordan": "JO", "Kazakhstan": "KZ", "Kenya": "KE",
    "Kosovo": "XK", "Latvia": "LV", "Lebanon": "LB", "Liechtenstein": "LI",
    "Lithuania": "LT", "Luxembourg": "LU", "Malta": "MT", "Mexico": "MX",
    "Moldova": "MD", "Monaco": "MC", "Montenegro": "ME", "Morocco": "MA",
    "Netherlands": "NL", "Nigeria": "NG", "North Macedonia": "MK",
    "Norway": "NO", "Peru": "PE", "Poland": "PL", "Portugal": "PT",
    "Romania": "RO", "Russia": "RU", "Russian Federation": "RU",
    "San Marino": "SM", "Saudi Arabia": "SA", "Serbia": "RS",
    "Slovakia": "SK", "Slovenia": "SI", "South Africa": "ZA",
    "Korea, South": "KR", "South Korea": "KR", "Spain": "ES",
    "Sweden": "SE", "Switzerland": "CH", "Türkiye": "TR", "Turkey": "TR",
    "Ukraine": "UA", "United Kingdom": "GB", "United States": "US",
    "Egypt": "EG", "Hong Kong": "HK", "Malaysia": "MY", "Malawi": "MW",
    "Mali": "ML", "Mauritius": "MU", "Mongolia": "MN", "Namibia": "NA",
    "Oman": "OM", "Panama": "PA", "Paraguay": "PY", "Kuwait": "KW",
    "Kyrgyzstan": "KG", "United Arab Emirates": "AE",
}
