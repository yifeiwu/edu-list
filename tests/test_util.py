from src import util


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
