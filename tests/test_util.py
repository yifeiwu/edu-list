from src import util

WINDOWS = util.socket.__name__ == "socket" and hasattr(util.socket, "WSAHOST_NOT_FOUND")


def _gaierror(msg, errno):
    return util.socket.gaierror(errno, msg)


def test_registrable_host_strips_www_and_wildcard():
    assert util.registrable_host("www.Example.EDU.") == "example.edu"
    assert util.registrable_host("*.example.edu") == "example.edu"
    assert util.registrable_host("MY-SCHOOL.ac.uk") == "my-school.ac.uk"


def test_registrable_host_rejects_ip_and_port_and_ipv6():
    assert util.registrable_host("192.168.1.1") == ""
    assert util.registrable_host("2001:db8::1") == ""
    assert util.registrable_host("example.edu:443") == ""
    assert util.registrable_host("localhost") == ""
    assert util.registrable_host("") == ""


def test_normalize_domain():
    assert util.normalize_domain("https://WWW.Stanford.EDU/path") == "stanford.edu"
    assert util.normalize_domain("not a domain") is None
    assert util.normalize_domain("") is None


def test_is_social_or_builder_exact_suffix_only():
    assert util.is_social_or_builder("facebook.com")
    assert util.is_social_or_builder("sub.facebook.com")
    assert util.is_social_or_builder("myschool.wixsite.com")
    assert util.is_social_or_builder("foo.blogspot.com")
    assert util.is_social_or_builder("foo.blogspot.fr")
    # Must NOT overmatch: substring is not enough.
    assert not util.is_social_or_builder("myblogspot.example.edu")
    assert not util.is_social_or_builder("stanford.edu")
    assert not util.is_social_or_builder("notfacebook.com")


def test_is_service_host_variants():
    assert util.is_service_host("mail.stanford.edu")
    assert util.is_service_host("webmail2.stanford.edu")
    assert util.is_service_host("moodle.stanford.edu")
    assert util.is_service_host("myschool.zoom.us")
    assert util.is_service_host("school.moodlecloud.com")
    assert not util.is_service_host("stanford.edu")
    assert not util.is_service_host("emailforward.example.com")


def test_registrable_base_and_same_site():
    assert util.registrable_base("www.stanford.edu") == "stanford.edu"
    assert util.registrable_base("foo.bar.ac.uk") == "bar.ac.uk"
    assert util.same_site("stanford.edu", "www.stanford.edu")
    assert util.same_site("student.eit.edu.au", "eit.edu.au")
    assert not util.same_site("unochapeco.edu.br", "uno.edu.br")


def test_country_from_suffix_longest_wins():
    m = {"uk": "GB", "ac.uk": "GBX", "edu": "US"}
    assert util.country_from_suffix("foo.ac.uk", m) == "GBX"
    assert util.country_from_suffix("foo.edu", m) == "US"
    assert util.country_from_suffix("foo.com", m) == ""


def test_country_from_suffix_academic_fallback():
    assert util.country_from_suffix("univ.edu.sn", {}) == "SN"
    assert util.country_from_suffix("foo.ac.zz", {}) == "ZZ"
    assert util.country_from_suffix("foo.sch.uk", {}) == "GB"  # UK->GB
    # Non-academic second level must NOT infer.
    assert util.country_from_suffix("foo.com.br", {}) == ""
    assert util.country_from_suffix("foo.gov.br", {}) == ""
    # Explicit map still wins over fallback.
    assert util.country_from_suffix("foo.edu.cn", {"edu.cn": "XX-Custom"}) == "XX-Custom"


def test_classify_type_hints_and_markers():
    assert util.classify_type("Anything", "x.edu", "k-12 school") == "k-12"
    assert util.classify_type("Anything", "x.edu", "university") == "university/college"
    assert util.classify_type("Springfield University", "springfield.edu", "") == "university/college"
    assert util.classify_type("Institute of Technology", "x.edu", "") == "university/college"
    assert util.classify_type("Springfield High School", "x.org", "") == "k-12"
    assert util.classify_type("Eton College", "etoncollege.org", "") == "k-12"
    assert util.classify_type("Random Site", "random.example.com", "") == "other"
    # Regression: Russian "university" must not classify as K-12.
    assert util.classify_type("Московский университет", "msu.ru", "") == "university/college"
    assert util.classify_type("Школа №1", "school1.ru", "") == "k-12"
    # institute/academy in domain also counts as higher-ed.
    assert util.classify_type("X", "foo-institute.example.com", "") == "university/college"
    assert util.classify_type("X", "foo-academy.example.com", "") == "university/college"


def test_keywords_cover_new_langs():
    assert "університет" in util.keywords_for_country("UA")
    assert "университет" in util.keywords_for_country("UA")
    assert "جامعة" in util.keywords_for_country("AE")
    assert "大学" in util.keywords_for_country("JP")


def test_union_sources_dedupes_ordered():
    assert util.union_sources("a;b", "b;c") == "a;b;c"
    assert util.union_sources("", "x") == "x"


def test_retry_wait_is_exponential_and_capped():
    assert util.retry_wait(0) == 1.0
    assert util.retry_wait(1) == 2.0
    assert util.retry_wait(2) == 4.0
    assert util.retry_wait(3) == 8.0
    # Capped from there on, and never blows up on huge attempt counts.
    assert util.retry_wait(10) == util.RETRY_BACKOFF_CAP
    assert util.retry_wait(10_000) == util.RETRY_BACKOFF_CAP
    # Negative attempts clamp to the first backoff step.
    assert util.retry_wait(-5) == 1.0


def test_retry_wait_respects_base():
    assert util.retry_wait(0, base=2.0) == 2.0
    assert util.retry_wait(2, base=2.0) == 8.0
    # A small base still tops out at the absolute cap.
    assert util.retry_wait(9, base=0.5) == util.RETRY_BACKOFF_CAP


def test_retry_wait_honors_numeric_retry_after():
    # Retry-After (delta-seconds) overrides the computed backoff...
    assert util.retry_wait(0, "12") == 12.0
    # ...but is itself capped so a hostile/incorrect header can't stall a run.
    assert util.retry_wait(0, "9999") == util.RETRY_AFTER_CAP
    # HTTP-date and junk values fall back to the exponential schedule.
    assert util.retry_wait(1, "Wed, 21 Oct 2026 07:28:00 GMT") == 2.0
    assert util.retry_wait(1, "") == 2.0
    assert util.retry_wait(1, None) == 2.0
    assert util.retry_wait(1, "-5") == 2.0


def test_retry_wait_never_negative():
    assert util.retry_wait(0, base=-5.0) >= 0.0
    assert util.retry_wait(3, base=0.0) >= 0.0


def test_transient_statuses_exclude_403():
    # 403 is a real Inaccessible verdict (WAF/bot block), not a hiccup.
    assert util.TRANSIENT_STATUSES == frozenset({429, 502, 503, 504})
    assert 403 not in util.TRANSIENT_STATUSES


# --- DNS reachability ---------------------------------------------------------
def test_dns_state_detects_missing(monkeypatch):
    def boom(*a, **k):
        raise _gaierror("Name or service not known", 11001 if WINDOWS else -2)
    monkeypatch.setattr(util.socket, "getaddrinfo", boom)
    assert util.dns_state("nope.example") == util.DNS_MISSING


def test_dns_state_detects_resolves(monkeypatch):
    monkeypatch.setattr(util.socket, "getaddrinfo",
                        lambda *a, **k: [(2, 1, 6, "", ("1.2.3.4", 443))])
    assert util.dns_state("ok.example") == util.DNS_RESOLVES


def test_dns_state_timeout_is_unknown_not_missing(monkeypatch):
    # A resolver timeout must never retire a healthy domain.
    def slow(*a, **k):
        raise _gaierror("timed out", 11002 if WINDOWS else -3)
    monkeypatch.setattr(util.socket, "getaddrinfo", slow)
    assert util.dns_state("slow.example") == util.DNS_UNKNOWN


def test_dns_state_other_gaierror_is_unknown(monkeypatch):
    def refused(*a, **k):
        raise _gaierror("server failure", 11002 if WINDOWS else -1)
    monkeypatch.setattr(util.socket, "getaddrinfo", refused)
    assert util.dns_state("x.example") == util.DNS_UNKNOWN


def test_dns_state_bogus_host_is_unknown(monkeypatch):
    def never(*a, **k):
        raise AssertionError("must not resolve an unusable host")
    monkeypatch.setattr(util.socket, "getaddrinfo", never)
    assert util.dns_state("") == util.DNS_UNKNOWN
    assert util.dns_state("   ") == util.DNS_UNKNOWN
    assert util.dns_state("localhost") == util.DNS_UNKNOWN  # no dot
    assert util.dns_state("127.0.0.1") == util.DNS_UNKNOWN  # IP literal


def test_dns_state_restores_default_timeout(monkeypatch):
    import socket as _socket
    monkeypatch.setattr(util.socket, "getaddrinfo",
                        lambda *a, **k: [(2, 1, 6, "", ("1.2.3.4", 443))])
    before = _socket.getdefaulttimeout()
    util.dns_state("ok.example", timeout=3)
    assert _socket.getdefaulttimeout() == before


def test_dns_dead_reason_constant():
    assert util.DNS_DEAD_REASON == "unreachable-dns"
