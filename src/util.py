"""Shared helpers: domain normalization, country inference, classification."""
from __future__ import annotations

import re
import urllib.parse as urlparse

# Social / placeholder hosts: a "website" that is only one of these doesn't count.
SOCIAL_HOSTS = {
    "facebook.com", "fb.com", "instagram.com", "twitter.com", "x.com",
    "linkedin.com", "youtube.com", "youtu.be", "tiktok.com", "whatsapp.com",
    "wa.me", "linktr.ee", "bit.ly", "tinyurl.com", "t.co",
}
BUILDER_SUFFIXES = (
    "wixsite.com", "weebly.com", "blogspot.", "wordpress.com",
    "sites.google.com", "jimdo.com", "godaddysites.com",
)

PARKING_RES = [
    r"buy this domain", r"domain for sale", r"this domain may be for sale",
    r"parked free", r"sedo\.com", r"godaddy.*auction", r"related links",
    r"this site is parked", r"domain parking",
]
SOFT404_RES = [
    r"^404\b", r"\bnot found\b", r"account suspended", r"403 forbidden",
    r"just a moment", r"attention required.*cloudflare", r"service unavailable",
]

SCHEMA_RE = re.compile(
    r'"@type"\s*:\s*"(CollegeOrUniversity|School|ElementarySchool|HighSchool|MiddleSchool|EducationalOrganization)"',
    re.I,
)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
TAG_RE = re.compile(r"<[^>]+>")
CANONICAL_RE = re.compile(r'<link[^>]+rel=["\']canonical["\']', re.I)
ICON_RE = re.compile(r'<link[^>]+rel=["\'](?:shortcut )?icon["\']', re.I)

# Multilingual education signals, grouped so per-country subsets stay small.
KEYWORDS_I18N = {
    "en": ["university", "college", "school", "institute", "academy",
           "polytechnic", "campus", "faculty", "students", "admissions",
           "kindergarten", "high school"],
    "es": ["universidad", "colegio", "escuela", "instituto", "academia",
           "campus", "facultad", "estudiantes", "admisiones", "preparatoria"],
    "fr": ["université", "universté", "collège", "lycée", "école",
           "institut", "académie", "campus", "faculté", "étudiants", "admissions"],
    "pt": ["universidade", "colégio", "escola", "instituto", "faculdade",
           "campus", "estudantes"],
    "id": ["universitas", "sekolah", "institut", "akademi", "kampus",
           "fakultas", "siswa", "penerimaan"],
    "de": ["universität", "hochschule", "schule", "gymnasium", "fakultät",
           "studierende"],
    "ja": ["大学", "学校", "学院", "キャンパス", "学生"],
    "other": ["university", "college", "school", "universidad", "université",
              "universidade", "universitas", "schule", "école", "escuela", "escola"],
}
# Country -> keyword groups (default ['en'] + group below where relevant).
COUNTRY_LANGS = {
    "MX": ["es"], "ES": ["es"], "AR": ["es"], "CO": ["es"], "CL": ["es"],
    "FR": ["fr"], "BE": ["fr"], "SN": ["fr"], "CI": ["fr"],
    "BR": ["pt"], "PT": ["pt"],
    "ID": ["id"], "DE": ["de"], "JP": ["ja"],
    "IN": ["en"], "NG": ["en"], "GH": ["en"], "KE": ["en"], "US": ["en"],
    "GB": ["en"], "AU": ["en"], "PK": ["en"], "PH": ["en"], "EG": ["en"],
}


def keywords_for_country(iso2: str) -> list[str]:
    langs = COUNTRY_LANGS.get((iso2 or "").upper(), ["en"])
    out: list[str] = []
    for lg in ["en", *langs]:
        out.extend(KEYWORDS_I18N.get(lg, []))
    if "other" not in langs:
        out.extend(KEYWORDS_I18N["other"])
    seen, ded = set(), []
    for k in out:
        if k not in seen:
            seen.add(k)
            ded.append(k)
    return ded


def registrable_host(host: str) -> str:
    """Lowercase, strip www., punycode-normalize. Returns '' if unusable."""
    h = (host or "").strip().lower().strip(".")
    if h.startswith("www."):
        h = h[4:]
    if not h or " " in h or "." not in h or len(h) < 4:
        return ""
    # Reject IPv4 literals.
    parts = h.split(".")
    if all(p.isdigit() for p in parts):
        return ""
    try:
        h = h.encode("idna").decode("ascii")
    except Exception:
        return ""
    return h


def normalize_domain(url_or_host: str) -> str | None:
    s = (url_or_host or "").strip().lower()
    if not s:
        return None
    if "://" not in s:
        s = "https://" + s
    try:
        host = urlparse.urlparse(s).hostname or ""
    except Exception:
        return None
    h = registrable_host(host)
    return h or None


def is_social_or_builder(domain: str) -> bool:
    d = domain.lower()
    if d in SOCIAL_HOSTS or any(d == s or d.endswith("." + s) for s in SOCIAL_HOSTS):
        return True
    return any(d == s or d.endswith("." + s) or s in d for s in BUILDER_SUFFIXES)


def country_from_suffix(domain: str, suffix_map: dict) -> str:
    for suffix, cc in sorted(suffix_map.items(), key=lambda kv: -len(kv[0])):
        if domain == suffix or domain.endswith("." + suffix):
            return cc
    return ""


def clean_text(html: str) -> str:
    return TAG_RE.sub(" ", html or "")


def classify_type(name: str, domain: str, hint: str = "") -> str:
    """Map to the required taxonomy: k-12 | university/college | other."""
    h = f"{hint} ".lower()
    if any(t in h for t in ("k-12", "k12", "primary", "secondary", "high school", "gias")):
        return "k-12"
    if any(t in h for t in ("university", "college", "polytechnic", "higher-ed",
                            "higher ed", "tertiary", "ipeds", "scorecard", "eter")):
        return "university/college"
    n = f"{name} {domain}".lower()
    uni_markers = ["university", "college", "polytechnic", "universidad",
                   "université", "universidade", "universitas", "universität",
                   "hochschule", "大学", "institut of technology"]
    if any(m in n for m in uni_markers):
        return "university/college"
    k12_markers = ["school", "high school", "primary", "elementary", "secondary",
                   "kindergarten", "colegio", "escuela", "escola", "école", "ecole",
                   "collège", "college ", "lycée", "lycee", "sekolah",
                   "gymnasium", "schule"]
    # NB: bare "college" is ambiguous (UK colleges are often secondary/FE);
    # domain signal breaks the tie: .sch.uk / .edu.* K-12 patterns win.
    if any(m in n for m in k12_markers) or domain.endswith(".sch.uk"):
        # "college" + higher-ed hint already returned above, so this is K-12-side.
        if "college" in n and any(u in n for u in ("university", "universidad", "polytechnic")):
            return "university/college"
        return "k-12"
    if "institute" in n or "academy" in n or "academy" in domain:
        # Institutes/academies: default higher-ed unless clearly K-12 named.
        return "university/college" if "school" not in n else "k-12"
    return "other"


def union_sources(old: str, new: str) -> str:
    """Semicolon-joined, order-preserving, deduped sources column."""
    items: list[str] = []
    for chunk in ((old or "") + ";" + (new or "")).split(";"):
        c = chunk.strip().strip(",")
        if c and c not in items:
            items.append(c)
    return ";".join(items)
