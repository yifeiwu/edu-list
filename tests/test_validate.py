from unittest.mock import patch

import requests

from src import validate
from tests.conftest import ACTIVE_HTML, make_response

UA = "test-bot/1.0"


def _no_sleep(s):
    return None


def _ok(text=ACTIVE_HTML, url="https://example.edu/"):
    return make_response(url=url, status=200, text=text)


def test_active_baseline():
    with patch("src.validate.requests.get", return_value=_ok()):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     multisource=True, politeness=0,
                                     sleep_fn=_no_sleep)
    assert res["status"] == "Active"
    assert res["code"] == 200
    assert "http-2xx-html" in res["reason"]


def test_threshold_is_injected():
    html = ("<html><head><title>Generic Home</title></head><body>"
            "<h1>Welcome</h1><p>" + ("lorem ipsum dolor sit amet " * 60) + "</p></body></html>")
    with patch("src.validate.requests.get") as mg:
        mg.side_effect = lambda *a, **k: make_response(text=html)
        validate.validate_site("https://example.edu", "example.edu",
                               "US", 10, UA, 32768,
                               politeness=0, active_threshold=50,
                               sleep_fn=_no_sleep)
        high = validate.validate_site("https://example.edu", "example.edu",
                                      "US", 10, UA, 32768,
                                      politeness=0, active_threshold=99,
                                      sleep_fn=_no_sleep)
    # Same page: passes default threshold only if scored high; with 99 it must fail.
    assert high["status"] == "Inaccessible"
    assert high["reason"].startswith("low-confidence:")


def test_non_2xx_always_inaccessible():
    with patch("src.validate.requests.get",
               return_value=make_response(status=403, text="forbidden")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert res["reason"] == "http-403"
    assert res["confidence"] == 5


def test_tls_error_is_inaccessible_no_fallback():
    with patch("src.validate.requests.get",
               side_effect=requests.exceptions.SSLError("bad chain")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert "SSLError" in res["reason"]
    # No verify=False fallback: requests.get called at most twice (apex+www).
    # (apex fails, www retry fails -> Inaccessible)


def test_tls_www_retry_succeeds():
    ok = _ok(url="https://www.example.edu/")
    def fake(url, **kw):
        if "://www." in url and "example.edu" in url:
            return ok
        raise requests.exceptions.SSLError("apex bad")
    with patch("src.validate.requests.get", side_effect=fake):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Active"


def test_social_and_builder_inaccessible():
    res = validate.validate_site("https://facebook.com/x", "facebook.com",
                                 "US", 10, UA, 32768, politeness=0)
    assert res["status"] == "Inaccessible"
    assert res["reason"] == "social-only/placeholder"


def test_same_site_redirect_is_not_a_move():
    r = make_response(url="https://www.example.edu/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["moved_to"] is None


def test_cross_domain_move_reported():
    r = make_response(url="https://other.edu/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://old.edu", "old.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["moved_to"] == "other.edu"
    # Moves are pointers, never Active — even with a strong page.
    assert res["status"] == "Inaccessible"
    assert "moved-to:" in res["reason"]


def test_cross_domain_move_never_active_even_multisource():
    r = make_response(url="https://other.edu/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://old.edu", "old.edu",
                                     "US", 10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert res["moved_to"] == "other.edu"


def test_subdomain_to_apex_same_base_is_not_move():
    r = make_response(url="https://eit.edu.au/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://student.eit.edu.au",
                                     "student.eit.edu.au", "AU",
                                     10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["moved_to"] is None


def test_service_host_capped_below_active():
    with patch("src.validate.requests.get", return_value=_ok()):
        res = validate.validate_site("https://mail.example.edu",
                                     "mail.example.edu", "US",
                                     10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert "service-host" in res["reason"]
    assert res["confidence"] <= 40


def test_service_host_forced_inaccessible_even_low_threshold():
    # A lowered threshold must never promote webmail/LMS endpoints.
    with patch("src.validate.requests.get", return_value=_ok()):
        res = validate.validate_site("https://mail.example.edu",
                                     "mail.example.edu", "US",
                                     10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep,
                                     active_threshold=10)
    assert res["status"] == "Inaccessible"
    assert "service-host" in res["reason"]


def test_numbered_service_host_forced_inaccessible():
    # Regression: mail2.sysu.edu.cn previously scored Active.
    with patch("src.validate.requests.get", return_value=_ok()):
        res = validate.validate_site("https://mail2.example.edu.cn",
                                     "mail2.example.edu.cn", "CN",
                                     10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert "service-host" in res["reason"]


def test_parking_and_soft404():
    pad = "<p>" + ("filler content about campus " * 20) + "</p>"
    park = ("<html><head><title>Buy this domain</title></head><body>"
            "domain for sale sedo.com" + pad + "</body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(text=park)):
        assert validate.validate_site("https://x.edu", "x.edu", "US",
                                      10, UA, 32768, politeness=0,
                                      sleep_fn=_no_sleep)["reason"] == "parking"
    soft = ("<html><head><title>404 Not Found</title></head><body>not found"
            + pad + "</body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(text=soft)):
        assert validate.validate_site("https://x.edu", "x.edu", "US",
                                      10, UA, 32768, politeness=0,
                                      sleep_fn=_no_sleep)["reason"] == "soft-404/block-page"


def test_politeness_called_on_failure_paths():
    calls = []
    with patch("src.validate.requests.get",
               return_value=make_response(status=500, text="err")):
        validate.validate_site("https://x.edu", "x.edu", "US", 10, UA, 32768,
                               politeness=0.4, sleep_fn=calls.append)
    assert calls == [0.4]


def test_meta_refresh_move():
    html = ('<html><head><meta http-equiv="refresh" content="0;url=https://new.edu/">'
            '<title>x</title></head><body>' + ("pad " * 100) + '</body></html>')
    with patch("src.validate.requests.get",
               return_value=make_response(text=html)):
        res = validate.validate_site("https://old.edu", "old.edu", "US",
                                     10, UA, 32768, politeness=0,
                                     sleep_fn=_no_sleep)
    assert res["moved_to"] == "new.edu"
    assert res["status"] == "Inaccessible"


def test_transient_retry_then_success():
    ok = _ok()
    calls = {"n": 0}

    def flaky(url, **kw):
        calls["n"] += 1
        if calls["n"] == 1:
            raise requests.exceptions.ConnectionError("reset")
        return ok

    with patch("src.validate.requests.get", side_effect=flaky):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     retries=1, retry_backoff=0)
    assert res["status"] == "Active"
    assert calls["n"] == 2


def test_transient_persistent_failure():
    with patch("src.validate.requests.get",
               side_effect=requests.exceptions.ConnectTimeout("slow")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     retries=1, retry_backoff=0)
    assert res["status"] == "Inaccessible"
    assert "ConnectTimeout" in res["reason"]


def test_transient_no_retry_when_disabled():
    calls = {"n": 0}

    def flaky(url, **kw):
        calls["n"] += 1
        raise requests.exceptions.ConnectionError("reset")

    with patch("src.validate.requests.get", side_effect=flaky):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     retries=0, retry_backoff=0)
    assert res["status"] == "Inaccessible"
    assert calls["n"] == 1


def test_ssl_not_retried_as_transient():
    # SSLError takes the www-variant path only: apex + www = 2 calls max,
    # never the transient backoff loop.
    calls = {"n": 0}

    def always_ssl(url, **kw):
        calls["n"] += 1
        raise requests.exceptions.SSLError("bad")
    with patch("src.validate.requests.get", side_effect=always_ssl):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert "SSLError" in res["reason"]
    assert calls["n"] == 2


def _takeover_html():
    # Lapsed-domain takeover shape: HTTP 200, structural chrome
    # (canonical/icon/contact links, copyright) and substantial copy — but
    # nothing educational: no schema edu type, no school name, no edu
    # keywords. Bonuses alone must never promote it.
    body = ("<p>Play the best games online now. Daily prizes, big winners, "
            "fast payouts, bonus rewards every hour. " * 20) + "</p>"
    return ("<html><head><title>Best Games Online - Prizes Every Hour</title>"
            '<link rel="canonical" href="https://example.edu/">'
            '<link rel="icon" href="/favicon.ico">'
            "</head><body><h1>Welcome - Play and Win</h1>"
            '<a href="/contact">Contact</a><a href="/promotions">Promotions</a>'
            "<p>© 2025 Example Games. All rights reserved.</p>"
            + body + "</body></html>")


def test_takeover_without_edu_signals_never_active():
    # Even multisource + trusted .edu suffix + structure + substantial copy
    # must not promote a page with no educational signal.
    with patch("src.validate.requests.get",
               return_value=make_response(text=_takeover_html())):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Springfield University")
    assert res["status"] == "Inaccessible"
    assert "non-educational-content" in res["reason"]
    assert res["moved_to"] is None


def test_takeover_with_school_name_scores_active():
    body = ("<p>Play the best games online now. Daily prizes, big winners, "
            "fast payouts, bonus rewards every hour. " * 20) + "</p>"
    html = ("<html><head><title>Best Games Online</title>"
            '<link rel="canonical" href="https://example.edu/">'
            '<link rel="icon" href="/favicon.ico">'
            "</head><body><h1>Springfield University Games Night</h1>"
            '<a href="/contact">Contact</a>'
            "<p>© 2025 Springfield University. All rights reserved.</p>"
            + body + "</body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(text=html)):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Springfield University")
    assert res["status"] == "Active"


def test_non_educational_page_tries_exa_discovery():
    def _fb_moved(domain, school="", iso=""):
        return {"verified": None, "reason": "exa-discovered",
                "evidence": ["https://realcollege.edu/"],
                "candidate": "realcollege.edu"}

    with patch("src.validate.requests.get",
               return_value=make_response(text=_takeover_html())):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Springfield University",
                                     exa_fallback_fn=_fb_moved)
    assert res["status"] == "Inaccessible"
    assert res["moved_to"] == "realcollege.edu"


def test_page_lang_extraction():
    assert validate._page_lang('<html lang="fr"><head>') == "fr"
    assert validate._page_lang('<HTML LANG="en-US"><head>') == "en-us"
    assert validate._page_lang("<html><head>") == ""
    assert validate._page_lang("") == ""
    assert validate._page_lang('<html lang="toolongtag">') == ""


def test_result_carries_language_and_final_domain():
    html = ('<html lang="pt-BR"><head><title>Universidade Exemplo - '
            "Admissions</title>"
            '<link rel="canonical" href="https://example.edu/">'
            '<link rel="icon" href="/favicon.ico"></head><body>'
            "<h1>Bem-vindo a Universidade Exemplo</h1>"
            "<p>Admissions, academics, faculties, campus life for students.</p>"
            '<a href="/admissions">Admissions</a>'
            '<a href="/contact">Contact</a></body></html>')
    with patch("src.validate.requests.get",
               return_value=make_response(text=html)):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Universidade Exemplo")
    assert res["language"] == "pt-br"
    assert res["final_domain"] == "example.edu"


def test_result_shape_invariants():
    # Every path returns the full column set (language "" pre-HTML).
    with patch("src.validate.requests.get",
               return_value=make_response(status=403, text="forbidden")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["language"] == ""
    assert res["final_domain"] == "example.edu"
    with patch("src.validate.requests.get",
               return_value=_ok()):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    for key in ("status", "confidence", "reason", "code",
                "final_domain", "moved_to", "language"):
        assert key in res, key
