"""Shared helpers: domain normalization, country inference, classification."""
from __future__ import annotations

import re
import urllib.parse as urlparse

from .geo import MULTI_SUFFIXES  # noqa: F401  (re-export, single source in geo.py)

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
           "campus", "facultad", "estudiantes", "admisiones", "preparatoria",
           "licenciatura", "posgrado", "enseñanza", "ensenanza"],
    "fr": ["université", "universté", "collège", "lycée", "école",
           "institut", "académie", "campus", "faculté", "étudiants", "admissions",
           "formations", "scolarité", "scolarite"],
    "pt": ["universidade", "colégio", "escola", "instituto", "faculdade",
           "campus", "estudantes", "ensino", "graduação", "graduacao",
           "vestibular", "pesquisa", "extensão", "extensao"],
    "id": ["universitas", "sekolah", "institut", "akademi", "kampus",
           "fakultas", "siswa", "penerimaan"],
    "de": ["universität", "hochschule", "schule", "gymnasium", "fakultät",
           "studierende"],
    "ja": ["大学", "学校", "学院", "キャンパス", "学生"],
    "ru": ["университет", "институт", "школа", "колледж", "академия",
           "студенты", "абитуриент", "факультет"],
    "uk": ["університет", "інститут", "школа", "коледж", "академія",
           "студенти", "абітурієнт", "факультет"],
    "ar": ["جامعة", "كلية", "مدرسة", "معهد", "أكاديمية", "طلاب", "القبول"],
    "zh": ["大学", "学校", "学院", "校园", "学生", "招生"],
    "other": ["university", "college", "school", "universidad", "université",
              "universidade", "universitas", "schule", "école", "escuela", "escola"],
}
# Country -> keyword groups (default ['en'] + group below where relevant).
COUNTRY_LANGS = {
    "MX": ["es"], "ES": ["es"], "AR": ["es"], "CO": ["es"], "CL": ["es"],
    "PE": ["es"],
    "FR": ["fr"], "BE": ["fr"], "SN": ["fr"], "CI": ["fr"], "MA": ["fr", "ar"],
    "BR": ["pt"], "PT": ["pt"],
    "ID": ["id"], "DE": ["de"], "JP": ["ja"], "CN": ["zh"],
    "UA": ["uk", "ru"], "RU": ["ru"], "KZ": ["ru"],
    "AE": ["ar", "en"], "SA": ["ar", "en"], "EG": ["ar", "en"],
    "VN": ["en"], "GH": ["en"], "KE": ["en"],
    "IN": ["en"], "NG": ["en"], "PK": ["en"], "PH": ["en"],
    "US": ["en"], "GB": ["en"], "AU": ["en"], "NZ": ["en"],
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
    # Strip wildcard prefix from CT-style names.
    if h.startswith("*."):
        h = h[2:]
    if h.startswith("www."):
        h = h[4:]
    # Reject IPv6 literals and host:port remnants.
    if ":" in h or " " in h or not h or "." not in h or len(h) < 4:
        return ""
    # Reject IPv4 literals.
    parts = h.split(".")
    if all(p.isdigit() for p in parts):
        return ""
    if any(not p or len(p) > 63 for p in parts):
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
    d = domain.lower().strip(".")
    if d in SOCIAL_HOSTS or any(d == s or d.endswith("." + s) for s in SOCIAL_HOSTS):
        return True
    for s in BUILDER_SUFFIXES:
        # Suffixes ending with "." (e.g. "blogspot.") match any TLD
        # ("foo.blogspot.com", "foo.blogspot.fr") via label-boundary check.
        if s.endswith("."):
            base = s.rstrip(".")
            labels = d.split(".")
            if any(lbl == base for lbl in labels[:-1]):
                return True
        elif d == s or d.endswith("." + s):
            return True
    return False


_ACADEMIC_ZONE_RE = re.compile(r"\.(edu|ac|sch)\.[a-z]{2}$", re.I)

# First-label prefixes that mark a host as a service endpoint (webmail,
# LMS, …), never the institution's website itself.
SERVICE_PREFIXES = frozenset({
    "mail", "mail2", "webmail", "email", "mymail", "owa", "outlook",
    "exchange", "zimbra", "roundcube", "moodle", "lms", "canvas",
    "blackboard", "brightspace", "schoology", "elearn", "elearning",
})

# Third-party meeting/classroom platforms: any subdomain is a service
# endpoint, not a school website (e.g. myschool.zoom.us).
SERVICE_PARENT_DOMAINS = frozenset({
    "zoom.us", "webex.com", "gotomeeting.com", "teams.microsoft.com",
    "moodlecloud.com", "instructure.com", "canvaslms.com",
    "blackboard.com", "brightspace.com", "schoology.com",
})


def is_service_host(domain: str) -> bool:
    """True for webmail/LMS/meeting endpoints (mail.X, moodle.X, X.zoom.us).

    These hosts are reachable and university-affiliated, but they are not
    the institution's website, so they are demoted (never Active).
    """
    d = (domain or "").lower().strip(".")
    if not d or "." not in d:
        return False
    first = d.split(".")[0]
    # Exact prefix plus numbered variants (webmail2, mail-01, moodle-02 …).
    if first in SERVICE_PREFIXES:
        return True
    stripped = re.sub(r"[\d_-]+$", "", first)
    if stripped in SERVICE_PREFIXES:
        return True
    labels = d.split(".")
    # Cloud LMS hosts (school.moodlecloud.com, school.instructure.com …).
    for parent in (".".join(labels[-2:]), ".".join(labels[-3:])):
        if parent in SERVICE_PARENT_DOMAINS:
            return True
    # *.zoom.us / *.webex.com etc: any subdomain of a meeting platform.
    for svc in SERVICE_PARENT_DOMAINS:
        if d == svc or d.endswith("." + svc):
            return True
    return False


def is_academic_suffix(domain: str) -> bool:
    """Regulated academic zones: .edu, .ac.uk, .edu.br, .sch.uk, …

    These TLD patterns are restricted to accredited institutions in most
    countries (e.g. edu.br requires MEC accreditation), so they earn a
    small trust bonus during scoring.
    """
    d = (domain or "").lower()
    if d.endswith(".edu") or d == "edu":
        return True
    if ".ac." in d or d.endswith(".sch.uk"):
        return True
    return bool(_ACADEMIC_ZONE_RE.search(d))


def registrable_base(domain: str) -> str:
    """Registrable base (eTLD+1 approx): last 2 labels, or 3 for known
    multi-label suffixes. Used to decide if a redirect stayed on-site."""
    d = (domain or "").lower().strip(".").removeprefix("www.")
    if not d or "." not in d:
        return d
    for suffix in MULTI_SUFFIXES:
        if d == suffix or d.endswith("." + suffix):
            parts = d.split(".")
            # e.g. foo.bar.ac.uk -> bar.ac.uk
            if len(parts) >= 4:
                return ".".join(parts[-3:])
            return d
    parts = d.split(".")
    if len(parts) >= 2:
        return ".".join(parts[-2:])
    return d


def same_site(a: str, b: str) -> bool:
    """True when two hosts share the same registrable base."""
    if not a or not b:
        return False
    return registrable_base(a) == registrable_base(b)


def country_from_suffix(domain: str, suffix_map: dict) -> str:
    # Longest-suffix wins (e.g. ac.uk beats uk). Map is small; pre-sort once.
    for suffix in sorted(suffix_map, key=len, reverse=True):
        if domain == suffix or domain.endswith("." + suffix):
            return suffix_map[suffix]
    # Generic academic fallback: <anything>.edu|ac|sch|univ.<ccTLD> implies
    # the trailing ccTLD (e.g. univ.edu.sn -> SN). Covers long-tail zones
    # without enumerating every country in config.yaml.
    m = re.search(r"\.(edu|ac|sch|univ|college)\.([a-z]{2})$", (domain or "").lower())
    if m:
        cc = m.group(2).upper()
        if cc == "UK":
            return "GB"
        if cc.isalpha():
            return cc
    return ""


_COLLEGE_RE = re.compile(r"\bcollege\b", re.I)


def classify_type(name: str, domain: str, hint: str = "") -> str:
    """Map to the required taxonomy: k-12 | university/college | other."""
    h = re.sub(r"\s+", " ", f"{hint} ".lower()).strip()
    if any(t in h for t in ("k-12", "k12", "primary", "secondary",
                            "high school", "gias", "k_12")):
        return "k-12"
    if any(t in h for t in ("university", "college", "polytechnic", "higher-ed",
                            "higher ed", "tertiary", "ipeds", "scorecard")):
        return "university/college"
    n = re.sub(r"\s+", " ", f"{name} {domain}".lower()).strip()
    uni_markers = ["university", "polytechnic", "universidad",
                   "université", "universidade", "universitas", "universität",
                   "hochschule", "大学", "университет", "університет",
                   "جامعة", "institute of technology"]
    # Bare "college" handled below (ambiguous UK FE vs higher-ed).
    if any(m in n for m in uni_markers):
        return "university/college"
    if _COLLEGE_RE.search(n) and any(
            u in n for u in ("university", "universidad", "université",
                             "polytechnic", "hochschule")):
        return "university/college"
    k12_markers = ["school", "high school", "primary", "elementary", "secondary",
                   "kindergarten", "colegio", "escuela", "escola", "école", "ecole",
                   "collège", "lycée", "lycee", "sekolah",
                   "школа", "gymnasium", "schule", "مدرسة"]
    if any(m in n for m in k12_markers) or domain.endswith(".sch.uk"):
        return "k-12"
    # Bare "college" alone (e.g. "Eton College", UK FE): K-12 side unless
    # higher-ed hint already returned above.
    if _COLLEGE_RE.search(n):
        return "k-12"
    if ("institute" in n or "institute" in domain
            or "academy" in n or "academy" in domain):
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
