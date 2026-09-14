"""Exa second-opinion for dissimilar redirects (rhul.ac.uk -> royalholloway)."""
from unittest.mock import MagicMock, patch

from src import exa_check as exa
from src import validate, verify
from tests.conftest import ACTIVE_HTML, make_response

UA = "test-bot/1.0"


def _no_sleep(s):
    return None


# --- dissimilarity -----------------------------------------------------------

def test_dissimilar_rhul_case():
    assert exa.is_dissimilar_redirect("rhul.ac.uk", "royalholloway.ac.uk") is True


def test_same_site_never_dissimilar():
    assert exa.is_dissimilar_redirect("example.edu", "www.example.edu") is False
    assert exa.is_dissimilar_redirect("example.edu", "example.edu") is False
    assert exa.is_dissimilar_redirect("student.eit.edu.au", "eit.edu.au") is False
    assert exa.is_dissimilar_redirect("", "x.edu") is False


def test_cross_domain_is_dissimilar():
    assert exa.is_dissimilar_redirect("old.edu", "other.edu") is True


# --- key / config ------------------------------------------------------------

def test_resolve_api_key_env_wins(monkeypatch):
    monkeypatch.setenv("EXA_API_KEY", "env-key-123")
    cfg = {"validation": {"exa_api_key": "cfg-key"}}
    assert exa.resolve_api_key(cfg) == "env-key-123"


def test_resolve_api_key_cfg_fallback(monkeypatch):
    monkeypatch.delenv("EXA_API_KEY", raising=False)
    assert exa.resolve_api_key({"validation": {"exa_api_key": "cfg-key"}}) == "cfg-key"
    assert exa.resolve_api_key({}) is None
    assert exa.resolve_api_key({"validation": {"exa_api_key": ""}}) is None


def test_exa_config_defaults(monkeypatch):
    monkeypatch.delenv("EXA_API_KEY", raising=False)
    c = exa.exa_config_from_cfg({})
    assert c["enabled"] is True
    assert c["api_key"] is None
    assert c["max_calls_per_run"] == 20
    assert c["timeout"] == 15


# --- search + interpret ------------------------------------------------------

def _payload(title="Royal Holloway, University of London",
             url="https://www.royalholloway.ac.uk/",
             text="Royal Holloway University admissions campus students"):
    return {"results": [{"title": title, "url": url, "text": text,
                         "highlights": [text]}]}


def test_search_posts_constrained_body():
    fake = MagicMock()
    fake.status_code = 200
    fake.json.return_value = {"results": []}
    with patch("src.exa_check.requests.post", return_value=fake) as mp:
        out = exa.search_exa("royalholloway.ac.uk", "Royal Holloway official",
                             api_key="k", timeout=5, num_results=5)
    assert out == {"results": []}
    _, kw = mp.call_args
    assert kw["json"]["includeDomains"] == ["royalholloway.ac.uk"]
    assert kw["json"]["query"]
    assert kw["headers"]["x-api-key"] == "k"


def test_search_failure_is_none():
    with patch("src.exa_check.requests.post",
               side_effect=Exception("down")):
        assert exa.search_exa("x.edu", "q", api_key="k") is None


def test_interpret_verified_by_keywords():
    v = exa.interpret_results(_payload(), "royalholloway.ac.uk", "GB",
                              "Royal Holloway")
    assert v["verified"] is True
    assert v["reason"].startswith("exa-verified")


def test_interpret_parking():
    p = _payload(title="Buy this domain",
                 url="https://parked-example.ac.uk/",
                 text="Buy this domain sedo.com parked free")
    v = exa.interpret_results(p, "parked-example.ac.uk", "GB", "Some School")
    assert v["verified"] is False
    assert v["reason"] == "exa-parking"


def test_interpret_no_results_and_error():
    assert exa.interpret_results({"results": []}, "x.edu")["verified"] is None
    assert exa.interpret_results({"results": []}, "x.edu")["reason"] == "exa-no-results"
    assert exa.interpret_results(None, "x.edu")["reason"] == "exa-error"


def test_interpret_commercial_takeover_is_inconclusive():
    # A lapsed domain serving unrelated commercial copy (e.g. a betting
    # operator on an expired college domain): substantial indexed text with
    # no school-name or edu-keyword signal must never verify — word count
    # alone is not educational evidence.
    p = _payload(title="Best Games Online - Prizes Every Hour",
                 url="https://example.edu/",
                 text=("Play the best games online now. Daily prizes, big "
                       "winners, fast payouts, bonus rewards every hour. " * 10))
    v = exa.interpret_results(p, "example.edu", "US", "Springfield University")
    assert v["verified"] is None
    assert v["reason"] == "exa-inconclusive"


def test_verify_redirect_skips_same_site_and_no_key():
    assert exa.verify_redirect_target(
        "example.edu", "www.example.edu", api_key="k")["reason"] == "exa-skipped:same-site"
    assert exa.verify_redirect_target(
        "a.edu", "b.edu", api_key="")["reason"] == "exa-skipped:no-key"


def test_verify_redirect_uses_search(monkeypatch):
    with patch("src.exa_check.search_exa", return_value=_payload()):
        v = exa.verify_redirect_target("rhul.ac.uk", "royalholloway.ac.uk",
                                       "Royal Holloway", "GB", api_key="k")
    assert v["verified"] is True


def test_cached_verify_uses_cache_without_network():
    cache = {"royalholloway.ac.uk": {"verified": True,
                                     "reason": "exa-verified",
                                     "evidence": [],
                                     "ts": "2026-09-13"}}
    with patch("src.exa_check.search_exa",
               side_effect=AssertionError("no network expected")):
        v = exa.cached_verify("rhul.ac.uk", "royalholloway.ac.uk",
                              "Royal Holloway", "GB",
                              cache=cache, api_key="k")
    assert v is not None and v["verified"] is True


def test_cached_verify_same_site_returns_none():
    assert exa.cached_verify("a.edu", "www.a.edu", cache={}, api_key="k") is None


# --- validate.py integration -------------------------------------------------

def _exa_verified(source, target, name="", iso=""):
    return {"verified": True, "reason": "exa-verified",
            "evidence": [f"https://{target}/"]}


def _exa_parking(source, target, name="", iso=""):
    return {"verified": False, "reason": "exa-parking", "evidence": []}


def test_move_pointer_annotated_with_exa():
    r = make_response(url="https://royalholloway.ac.uk/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://rhul.ac.uk", "rhul.ac.uk", "GB",
                                     10, UA, 32768, politeness=0,
                                     sleep_fn=_no_sleep,
                                     school_name="Royal Holloway",
                                     exa_verify_fn=_exa_verified)
    assert res["moved_to"] == "royalholloway.ac.uk"
    assert res["status"] == "Inaccessible"  # pointers never Active
    assert "exa-verified" in res["reason"]
    assert res["exa"]["verified"] is True


def test_move_without_exa_unchanged():
    r = make_response(url="https://other.edu/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://old.edu", "old.edu", "US",
                                     10, UA, 32768, politeness=0,
                                     sleep_fn=_no_sleep)
    assert res["moved_to"] == "other.edu"
    assert "exa-" not in res["reason"]
    assert "exa" not in res


def test_same_site_never_calls_exa():
    called = {"n": 0}

    def boom(source, target, name="", iso=""):
        called["n"] += 1
        return {"verified": True, "reason": "exa-verified", "evidence": []}

    r = make_response(url="https://www.example.edu/", text=ACTIVE_HTML)
    with patch("src.validate.requests.get", return_value=r):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768, politeness=0,
                                     sleep_fn=_no_sleep, exa_verify_fn=boom)
    assert res["moved_to"] is None
    assert called["n"] == 0


def test_redirect_target_rescued_by_exa():
    thin = ("<html><head><title>Home</title>"
            '<link rel="canonical" href="https://new.edu/">'
            "</head><body><h1>Welcome</h1><p>"
            + ("lorem ipsum dolor sit amet " * 60) + "</p></body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(url="https://new.edu/", text=thin)):
        local = validate.validate_site("https://new.edu", "new.edu", "US",
                                       10, UA, 32768, politeness=0,
                                       sleep_fn=_no_sleep,
                                       active_threshold=99)
        assert local["status"] == "Inaccessible"
        rescued = validate.validate_site(
            "https://new.edu", "new.edu", "US", 10, UA, 32768,
            politeness=0, sleep_fn=_no_sleep, active_threshold=99,
            school_name="New University", redirect_from="old.edu",
            exa_verify_fn=_exa_verified)
    assert rescued["status"] == "Active"
    assert "exa-verified" in rescued["reason"]


def test_redirect_target_demoted_on_exa_parking():
    with patch("src.validate.requests.get",
               return_value=make_response(url="https://new.edu/",
                                          text=ACTIVE_HTML)):
        res = validate.validate_site(
            "https://new.edu", "new.edu", "US", 10, UA, 32768,
            multisource=True, politeness=0, sleep_fn=_no_sleep,
            school_name="New University", redirect_from="old.edu",
            exa_verify_fn=_exa_parking)
    assert res["status"] == "Inaccessible"
    assert "exa-parking" in res["reason"]


def test_service_host_never_promoted_by_exa():
    with patch("src.validate.requests.get",
               return_value=make_response(url="https://mail.example.edu/",
                                          text=ACTIVE_HTML)):
        res = validate.validate_site(
            "https://mail.example.edu", "mail.example.edu", "US",
            10, UA, 32768, multisource=True, politeness=0,
            sleep_fn=_no_sleep, active_threshold=10,
            redirect_from="old.edu", exa_verify_fn=_exa_verified)
    assert res["status"] == "Inaccessible"
    assert "service-host" in res["reason"]


def test_meta_refresh_move_annotated():
    html = ('<html><head><meta http-equiv="refresh" content="0;url=https://new.edu/">'
            '<title>x</title></head><body>' + ("pad " * 100) + "</body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(url="https://old.edu/", text=html)):
        res = validate.validate_site("https://old.edu", "old.edu", "US",
                                     10, UA, 32768, politeness=0,
                                     sleep_fn=_no_sleep,
                                     exa_verify_fn=_exa_verified)
    assert res["moved_to"] == "new.edu"
    assert "exa-verified" in res["reason"]


# --- verify.py integration ---------------------------------------------------

def test_redirect_from_source_parsing():
    assert verify._redirect_from_source("redirect:old.edu") == "old.edu"
    assert verify._redirect_from_source("hipo:x;redirect:old.edu") == "old.edu"
    assert verify._redirect_from_source("hipo:x") is None
    assert verify._redirect_from_source("") is None


def test_check_passes_redirect_provenance(monkeypatch):
    seen = {}

    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None,
             school_name="", redirect_from=None, exa_verify_fn=None, **kw):
        seen.update(school_name=school_name, redirect_from=redirect_from,
                    has_exa=exa_verify_fn is not None)
        return {"status": "Active", "confidence": 80, "reason": "x",
                "code": 200, "final_domain": domain, "moved_to": None}

    monkeypatch.setattr(verify, "validate_site", fake)
    vcfg = {"timeout": 10, "max_bytes": 100, "ua": "t", "threshold": 50,
            "polite": 0}
    verify.check("new.edu", "New Uni", "US", False, vcfg,
                 redirect_from="old.edu", exa_verify_fn=lambda *a: None)
    assert seen["redirect_from"] == "old.edu"
    assert seen["school_name"] == "New Uni"
    assert seen["has_exa"] is True


def test_verify_exa_budget_caps_calls(monkeypatch):
    import time
    monkeypatch.setenv("EXA_API_KEY", "test-key")
    calls = {"n": 0}

    def fake_cached(source, target, name="", iso="", cache=None, api_key="",
                    timeout=15, num_results=5, search_type="fast"):
        calls["n"] += 1
        return {"verified": True, "reason": "exa-verified",
                "evidence": [], "ts": "2026-09-13"}

    monkeypatch.setattr(verify, "cached_verify", fake_cached)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: None)

    def fake_validate(url, domain, iso, timeout, ua, max_bytes,
                      multisource=False, politeness=0, active_threshold=50,
                      sleep_fn=None, school_name="", redirect_from=None,
                      exa_verify_fn=None, **kw):
        # Every domain reports a dissimilar move to force an Exa consultation.
        target = f"target-{domain.replace('.', '-')}.edu"
        verdict = None
        if exa_verify_fn is not None:
            try:
                verdict = exa_verify_fn(domain, target, school_name, iso)
            except Exception:
                verdict = None
        reason = f"moved-to:{target}"
        if isinstance(verdict, dict) and verdict.get("verified") is True:
            reason += "+exa-verified"
        out = {"status": "Inaccessible", "confidence": 10, "reason": reason,
               "code": 200, "final_domain": domain, "moved_to": target}
        if verdict is not None:
            out["exa"] = verdict
        return out

    monkeypatch.setattr(verify, "validate_site", fake_validate)
    cfg = {"run": {"max_validations": 100, "max_new_per_run": 50,
                   "verify_batch_no_new": 0, "verify_batch_with_new": 0,
                   "archive_after_failures": 6, "archive_skip_days": 90},
           "verify": {}, "validation": {"timeout_seconds": 10,
                                        "max_bytes": 100,
                                        "user_agent": "t",
                                        "active_threshold": 50,
                                        "politeness_delay_seconds": 0,
                                        "exa_max_calls_per_run": 2},
           "suffix_country": {"edu": "US"}, "blocklist": []}
    state: dict = {"detail": {}, "failures": {}, "moved": {},
                   "domain_age": {}, "exa_cache": {}}
    pending = [{"name": f"S{i}", "url": f"https://s{i}.edu",
                "domain": f"s{i}.edu", "iso2": "US", "type_hint": "",
                "source": "hipo:x"} for i in range(5)]
    stats = verify.run_verify(cfg=cfg, state=state, by_domain={},
                              buckets={}, pending=pending, new_only=True,
                              deadline=time.time() + 60)
    assert stats["exa_calls"] == 2
    assert calls["n"] == 2
    # Pointer reasons carry the Exa annotation for the consulted moves.
    assert "exa-verified" in state["detail"]["s0.edu"]["reason"]


# --- fallback rescue + discovery ---------------------------------------------

def _fb_verified(domain, school="", iso=""):
    return {"verified": True, "reason": "exa-verified",
            "evidence": [f"https://{domain}/"], "candidate": None}


def _fb_moved(domain, school="", iso=""):
    return {"verified": None, "reason": "exa-discovered",
            "evidence": ["https://new.edu/"], "candidate": "new.edu"}


def test_fallback_rescues_403_to_active():
    with patch("src.validate.requests.get",
               return_value=make_response(status=403, text="forbidden")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Example University",
                                     exa_fallback_fn=_fb_verified)
    assert res["status"] == "Active"
    assert res["moved_to"] is None
    assert "exa-verified" in res["reason"]
    assert res["exa"]["verified"] is True
    # Original transport code preserved for transparency.
    assert res["code"] == 403


def test_fallback_no_hook_keeps_403_inaccessible():
    with patch("src.validate.requests.get",
               return_value=make_response(status=403, text="forbidden")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep)
    assert res["status"] == "Inaccessible"
    assert res["reason"] == "http-403"


def test_fallback_rescues_connection_error():
    import requests as _rq
    with patch("src.validate.requests.get",
               side_effect=_rq.exceptions.ConnectionError("down")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     retries=0,
                                     school_name="Example University",
                                     exa_fallback_fn=_fb_verified)
    assert res["status"] == "Active"
    assert "exa-verified" in res["reason"]


def test_fallback_discovers_replacement_domain():
    import requests as _rq
    with patch("src.validate.requests.get",
               side_effect=_rq.exceptions.ConnectionError("down")):
        res = validate.validate_site("https://old.edu", "old.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     retries=0, school_name="Old University",
                                     exa_fallback_fn=_fb_moved)
    assert res["status"] == "Inaccessible"
    assert res["moved_to"] == "new.edu"
    assert "exa-discovered" in res["reason"]


def test_fallback_tls_never_rescues_same_domain():
    import requests as _rq
    with patch("src.validate.requests.get",
               side_effect=_rq.exceptions.SSLError("bad chain")):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     exa_fallback_fn=_fb_verified)
    assert res["status"] == "Inaccessible"
    assert "SSLError" in res["reason"]


def test_fallback_tls_can_discover_replacement():
    import requests as _rq
    with patch("src.validate.requests.get",
               side_effect=_rq.exceptions.SSLError("bad chain")):
        res = validate.validate_site("https://old.edu", "old.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     exa_fallback_fn=_fb_moved)
    assert res["moved_to"] == "new.edu"


def test_fallback_never_rescues_service_or_social():
    with patch("src.validate.requests.get",
               return_value=make_response(url="https://mail.example.edu/",
                                          text=ACTIVE_HTML)):
        res = validate.validate_site("https://mail.example.edu",
                                     "mail.example.edu", "US",
                                     10, UA, 32768, multisource=True,
                                     politeness=0, sleep_fn=_no_sleep,
                                     active_threshold=10,
                                     exa_fallback_fn=_fb_verified)
    assert res["status"] == "Inaccessible"
    assert "service-host" in res["reason"]
    # Social placeholders never consult fallback at all.
    res2 = validate.validate_site("https://facebook.com/x", "facebook.com",
                                  "US", 10, UA, 32768, politeness=0,
                                  exa_fallback_fn=_fb_verified)
    assert res2["reason"] == "social-only/placeholder"


def test_fallback_rescues_low_confidence():
    thin = ("<html><head><title>Home</title></head><body><h1>Hi</h1><p>"
            + ("lorem ipsum " * 60) + "</p></body></html>")
    with patch("src.validate.requests.get",
               return_value=make_response(text=thin)):
        res = validate.validate_site("https://example.edu", "example.edu",
                                     "US", 10, UA, 32768,
                                     politeness=0, sleep_fn=_no_sleep,
                                     school_name="Example University",
                                     exa_fallback_fn=_fb_verified)
    assert res["status"] == "Active"
    assert "exa-verified" in res["reason"]


def test_verify_domain_self_check():
    with patch("src.exa_check.search_exa", return_value=_payload()):
        v = exa.verify_domain("royalholloway.ac.uk", "Royal Holloway", "GB",
                              api_key="k")
    assert v["verified"] is True


def test_extract_candidate_filters_source_and_social():
    payload = {"results": [
        {"url": "https://old.edu/a", "title": "Old", "text": "x"},
        {"url": "https://www.facebook.com/old", "title": "fb", "text": "x"},
        {"url": "https://new.edu/", "title": "New University site",
         "text": "New University admissions campus"},
        {"url": "https://new.edu/about", "title": "About", "text": "y"},
    ]}
    cand, ev = exa.extract_candidate_domain(payload, "old.edu")
    assert cand == "new.edu"
    assert ev


def test_discover_domain_uses_unconstrained_search():
    payload = {"results": [
        {"url": "https://new.edu/", "title": "New University",
         "text": "New University admissions campus students",
         "highlights": ["New University"]},
    ]}
    with patch("src.exa_check.search_general", return_value=payload):
        out = exa.discover_domain("New University", "US", "old.edu",
                                  api_key="k")
    assert out["domain"] == "new.edu"
    assert out["verified"] is True


def test_check_allows_exa_rescued_403():
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None,
             school_name="", redirect_from=None, exa_verify_fn=None,
             exa_fallback_fn=None, **kw):
        return {"status": "Active", "confidence": 50,
                "reason": "http-403+exa-verified", "code": 403,
                "final_domain": domain, "moved_to": None,
                "exa": {"verified": True, "reason": "exa-verified",
                        "evidence": []}}
    import tests.test_exa as _t  # noqa: F401 (ensure module loaded)
    from src import verify as _v
    orig = _v.validate_site
    _v.validate_site = fake  # type: ignore[assignment]
    try:
        vcfg = {"timeout": 10, "max_bytes": 100, "ua": "t", "threshold": 50,
                "polite": 0}
        status, res = _v.check("x.edu", "X", "US", False, vcfg)
        assert status == "Active"
    finally:
        _v.validate_site = orig  # type: ignore[assignment]
