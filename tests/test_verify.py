import time

from src import verify


def _cfg(**over):
    base = {"run": {"max_validations": 100, "max_new_per_run": 50,
                    "verify_batch_no_new": 10, "verify_batch_with_new": 2,
                    "archive_after_failures": 6, "archive_skip_days": 90},
            "verify": {}, "validation": {"timeout_seconds": 10,
                                         "max_bytes": 32768,
                                         "user_agent": "t",
                                         "active_threshold": 50,
                                         "politeness_delay_seconds": 0},
            "suffix_country": {"edu": "US"}, "blocklist": [],
            "k12_enabled": True}
    base.update(over)
    return base


def _patch_validate(monkeypatch, reason="http-2xx-html+edu-keywords+structure",
                    conf=80, code=200, moved=None, lang=""):
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        status = "Active" if conf >= active_threshold and 200 <= code < 300 else "Inaccessible"
        return {"status": status, "confidence": conf, "reason": reason,
                "code": code, "final_domain": domain, "moved_to": moved,
                "language": lang}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: 10)


def test_fifo_drain_then_reverify(monkeypatch):
    _patch_validate(monkeypatch)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    by: dict = {}
    buckets: dict = {}
    pending = [{"name": "A", "url": "https://a.edu", "domain": "a.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"},
               {"name": "B", "url": "https://b.edu", "domain": "b.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"}]
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                              pending=pending, deadline=time.time() + 60)
    assert stats["validated"] >= 2
    assert stats["added_active"] == 2
    assert stats["pending_left"] == 0
    assert by["a.edu"][1]["years_registered"] == "10"


def test_blocklist_purged_without_network(monkeypatch):
    called = {"n": 0}
    def boom(*a, **k):
        called["n"] += 1
        raise AssertionError("no network expected")
    monkeypatch.setattr(verify, "validate_site", boom)
    cfg = _cfg()
    cfg["blocklist"] = ["old.edu"]
    buckets = {"US": [{"school_name": "O", "web_domain": "old.edu",
                       "type": "other", "last_visited": "2026-09-12",
                       "status": "Active", "sources": "s",
                       "years_registered": ""}]}
    by = {"old.edu": ("US", buckets["US"][0])}
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    pending = [{"name": "O", "url": "https://old.edu", "domain": "old.edu",
                "iso2": "US", "type_hint": "", "source": "s"}]
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                              pending=pending, new_only=True,
                              deadline=time.time() + 60)
    assert by == {}
    assert pending == []
    assert called["n"] == 0
    assert stats["touched"] == {"US"}


def test_move_chases_target_and_tracks_pointer(monkeypatch):
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        if domain == "old.edu":
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "moved-meta:new.edu", "code": 200,
                    "final_domain": "old.edu", "moved_to": "new.edu"}
        return {"status": "Active", "confidence": 80,
                "reason": "http-2xx-html+edu-keywords", "code": 200,
                "final_domain": domain, "moved_to": None}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: 5)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    by: dict = {}
    buckets: dict = {}
    pending = [{"name": "Old", "url": "https://old.edu", "domain": "old.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"}]
    verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                      pending=pending, deadline=time.time() + 60)
    assert by["old.edu"][1]["status"] == "Inaccessible"
    assert state["moved"]["old.edu"] == "new.edu"
    assert "new.edu" in by  # followed within budget
    assert "redirect:old.edu" in by["new.edu"][1]["sources"]


def test_service_host_target_gets_no_row(monkeypatch):
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        if domain == "old.edu":
            return {"status": "Inaccessible", "confidence": 10, "reason": "x",
                    "code": 200, "final_domain": "old.edu",
                    "moved_to": "mail.old.edu"}
        return {"status": "Active", "confidence": 80, "reason": "x",
                "code": 200, "final_domain": domain, "moved_to": None}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: None)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    by: dict = {}
    buckets: dict = {}
    pending = [{"name": "O", "url": "https://old.edu", "domain": "old.edu",
                "iso2": "US", "type_hint": "", "source": "s"}]
    verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                      pending=pending, deadline=time.time() + 60)
    assert "mail.old.edu" not in by


def test_archive_skip(monkeypatch):
    _patch_validate(monkeypatch)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {"stale.edu": 6},
                   "moved": {}, "domain_age": {}}
    row = {"school_name": "S", "web_domain": "stale.edu",
           "type": "other", "last_visited": "2026-09-12",
           "status": "Inaccessible", "sources": "s", "years_registered": ""}
    by = {"stale.edu": ("US", row)}
    buckets = {"US": [row]}
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                              pending=[], deadline=time.time() + 60)
    # Archived (6 failures, fresh date) -> skipped, nothing validated.
    assert stats["validated"] == 0


def test_move_chain_multi_hop_resolves_in_one_run(monkeypatch):
    # A -> B -> C chain must all resolve without waiting for next run.
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        if domain == "a.edu":
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "moved-meta:b.edu", "code": 200,
                    "final_domain": "a.edu", "moved_to": "b.edu"}
        if domain == "b.edu":
            return {"status": "Inaccessible", "confidence": 10,
                    "reason": "moved-meta:c.edu", "code": 200,
                    "final_domain": "b.edu", "moved_to": "c.edu"}
        return {"status": "Active", "confidence": 80,
                "reason": "http-2xx-html+edu-keywords", "code": 200,
                "final_domain": domain, "moved_to": None}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: 5)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    by: dict = {}
    buckets: dict = {}
    pending = [{"name": "A", "url": "https://a.edu", "domain": "a.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"}]
    verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                      pending=pending, deadline=time.time() + 60)
    assert set(by) == {"a.edu", "b.edu", "c.edu"}
    assert state["moved"]["a.edu"] == "b.edu"
    assert state["moved"]["b.edu"] == "c.edu"
    assert "redirect:b.edu" in by["c.edu"][1]["sources"]
    assert pending == []


def test_move_chain_loop_safe(monkeypatch):
    # A -> B -> A loop must terminate without hanging.
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        nxt = "b.edu" if domain == "a.edu" else "a.edu"
        return {"status": "Inaccessible", "confidence": 10,
                "reason": f"moved-meta:{nxt}", "code": 200,
                "final_domain": domain, "moved_to": nxt}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: None)
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    by: dict = {}
    buckets: dict = {}
    pending = [{"name": "A", "url": "https://a.edu", "domain": "a.edu",
                "iso2": "US", "type_hint": "", "source": "s"}]
    verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                      pending=pending, deadline=time.time() + 60)
    assert set(by) == {"a.edu", "b.edu"}


def test_new_and_reverify_rows_carry_extra_columns(monkeypatch):
    _patch_validate(monkeypatch, lang="fr")
    cfg = _cfg()
    state: dict = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {}}
    row = {"school_name": "Old", "web_domain": "old.edu", "type": "other",
           "last_visited": "2000-01-01", "status": "Active", "sources": "s",
           "years_registered": ""}
    by = {"old.edu": ("US", row)}
    buckets: dict = {"US": [row]}
    pending = [{"name": "A", "url": "https://a.edu", "domain": "a.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"}]
    verify.run_verify(cfg=cfg, state=state, by_domain=by, buckets=buckets,
                      pending=pending, deadline=time.time() + 60)
    new = by["a.edu"][1]
    assert new["confidence"] == "80"
    assert new["reason"] == "http-2xx-html+edu-keywords+structure"
    assert new["final_domain"] == "a.edu"
    assert new["language"] == "fr"
    # Re-verified existing row refreshed too.
    assert by["old.edu"][1]["confidence"] == "80"
    assert by["old.edu"][1]["language"] == "fr"
