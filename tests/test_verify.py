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


# --- DNS-dead retirement -----------------------------------------------------
def _row(domain, status="Inaccessible", reason="fetch-error:ConnectionError",
         visited="2000-01-01"):
    return {"school_name": "S", "web_domain": domain, "type": "other",
            "last_visited": visited, "status": status, "sources": "hipo:x",
            "years_registered": "", "confidence": "0", "reason": reason,
            "final_domain": domain, "language": ""}


def _state(**kw):
    base = {"detail": {}, "failures": {}, "moved": {}, "domain_age": {},
            "dns_dead": {}, "exa_cache": {}}
    base.update(kw)
    return base


def _dead_result(domain):
    return {"status": "Inaccessible", "confidence": 0,
            "reason": "unreachable-dns", "code": 0,
            "final_domain": domain, "moved_to": None, "language": ""}


def test_dns_dead_row_is_recorded_and_skipped_forever(monkeypatch):
    # A dead name is retired on first sight: recorded in state, and the
    # re-verify rotation never picks it up again.
    _patch_validate(monkeypatch, reason="unreachable-dns", conf=0, code=0)
    cfg = _cfg()
    state = _state()
    row = _row("gone.edu")
    by = {"gone.edu": ("US", row)}
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by,
                              buckets={"US": [row]}, pending=[],
                              deadline=time.time() + 60)
    assert stats["validated"] == 1
    assert "gone.edu" in state["dns_dead"]
    assert row["reason"] == "unreachable-dns"

    # Second run: rotation must skip it even though last_visited is ancient
    # and it has only one recorded failure.
    state2 = _state(dns_dead=dict(state["dns_dead"]),
                    failures={"gone.edu": 1}, detail=dict(state["detail"]))
    by2 = {"gone.edu": ("US", row)}
    stats2 = verify.run_verify(cfg=cfg, state=state2, by_domain=by2,
                               buckets={"US": [row]}, pending=[],
                               deadline=time.time() + 60)
    assert stats2["validated"] == 0
    assert stats2["reverified"] == 0


def test_dns_dead_pending_candidates_are_dropped(monkeypatch):
    # A source re-queueing a known-dead name must not burn a validation.
    _patch_validate(monkeypatch)
    cfg = _cfg()
    state = _state(dns_dead={"gone.edu": {"at": time.strftime("%Y-%m-%d")}})
    by: dict = {}
    pending = [{"name": "G", "url": "https://gone.edu", "domain": "gone.edu",
                "iso2": "US", "type_hint": "", "source": "hipo:x"}]
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by,
                              buckets={}, pending=pending,
                              deadline=time.time() + 60)
    assert stats["validated"] == 0
    assert "gone.edu" not in by


def test_dns_dead_cooldown_expires_and_row_returns(monkeypatch):
    # After the cooldown the row is re-checked, so a name that later gets
    # registered is not orphaned forever.
    _patch_validate(monkeypatch)
    cfg = _cfg()
    state = _state(dns_dead={"revived.edu": {"at": "1999-01-01"}},
                   failures={"revived.edu": 1})
    row = _row("revived.edu")
    by = {"revived.edu": ("US", row)}
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by,
                              buckets={"US": [row]}, pending=[],
                              deadline=time.time() + 60)
    assert stats["reverified"] == 1
    assert row["status"] == "Active"
    assert "revived.edu" not in state["dns_dead"]


def test_dns_dead_cooldown_respected(monkeypatch):
    # Retired recently -> still inside the 365d cooldown, so no re-check.
    _patch_validate(monkeypatch)
    cfg = _cfg()
    state = _state(dns_dead={"gone.edu": {"at": iso_days_ago(30)}})
    row = _row("gone.edu")
    by = {"gone.edu": ("US", row)}
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by,
                              buckets={"US": [row]}, pending=[],
                              deadline=time.time() + 60)
    assert stats["validated"] == 0
    assert "gone.edu" in state["dns_dead"]  # not popped, still retired


def test_dns_dead_cooldown_zero_always_rechecks(monkeypatch):
    _patch_validate(monkeypatch)
    cfg = _cfg()
    cfg["run"]["dns_dead_recheck_days"] = 0
    state = _state(dns_dead={"gone.edu": {"at": old_iso()}})
    row = _row("gone.edu")
    by = {"gone.edu": ("US", row)}
    stats = verify.run_verify(cfg=cfg, state=state, by_domain=by,
                              buckets={"US": [row]}, pending=[],
                              deadline=time.time() + 60)
    assert stats["reverified"] == 1


def test_dns_dead_cleared_when_redirect_found(monkeypatch):
    # A redirect proves the name resolves: the retirement must be dropped.
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        return {"status": "Inaccessible", "confidence": 5,
                "reason": "moved-meta:new.edu", "code": 200,
                "final_domain": domain, "moved_to": "new.edu"}
    monkeypatch.setattr(verify, "validate_site", fake)
    monkeypatch.setattr(verify, "_domain_age", lambda d, timeout=8, cache=None: 5)
    cfg = _cfg()
    state = _state(dns_dead={"old.edu": {"at": old_iso()}},
                   failures={"old.edu": 1})
    row = _row("old.edu")
    by = {"old.edu": ("US", row)}
    verify.run_verify(cfg=cfg, state=state, by_domain=by,
                      buckets={"US": [row]}, pending=[],
                      deadline=time.time() + 60)
    assert "old.edu" not in state["dns_dead"]
    assert state["moved"]["old.edu"] == "new.edu"


# --- backfill ----------------------------------------------------------------
def test_backfill_retires_missing_dns_without_fetching(monkeypatch):
    def fake(url, domain, iso, timeout, ua, max_bytes, multisource=False,
             politeness=0, active_threshold=50, sleep_fn=None, **kw):
        raise AssertionError("backfill must not fetch websites")

    monkeypatch.setattr(verify, "validate_site", fake)
    states = {
        "gone.edu": "missing",
        "slow.edu": "unknown",
        "up.edu": "resolves",
        "blocked.edu": "missing",
    }
    monkeypatch.setattr(verify, "dns_state", lambda d: states[d])
    cfg = _cfg()
    state = _state()
    rows = {
        "gone.edu": _row("gone.edu"),
        "slow.edu": _row("slow.edu"),
        "up.edu": _row("up.edu"),
        "blocked.edu": _row("blocked.edu", reason="http-403"),
        "active.edu": _row("active.edu", status="Active"),
    }
    by = {d: ("US", r) for d, r in rows.items()}
    buckets = {"US": list(rows.values())}
    res = verify.backfill_dns_dead(cfg=cfg, state=state, by_domain=by,
                                   buckets=buckets, deadline=time.time() + 60)
    assert res["retired"] == 1          # only gone.edu
    assert res["unknown"] == 1          # slow.edu inconclusive
    assert rows["gone.edu"]["reason"] == "unreachable-dns"
    assert rows["gone.edu"]["confidence"] == "0"
    # Untouched: inconclusive, still-resolving, and non-connection reasons.
    assert rows["slow.edu"]["reason"] == "fetch-error:ConnectionError"
    assert rows["up.edu"]["reason"] == "fetch-error:ConnectionError"
    assert rows["blocked.edu"]["reason"] == "http-403"
    assert "gone.edu" in state["dns_dead"]
    assert "slow.edu" not in state["dns_dead"]


def test_backfill_skips_http_verified_rows(monkeypatch):
    # A row that got real HTTP demonstrably resolved; never re-resolve it.
    def never(d):
        raise AssertionError(f"must not resolve {d}")

    monkeypatch.setattr(verify, "dns_state", never)
    cfg = _cfg()
    rows = {
        "a.edu": _row("a.edu", reason="http-403"),
        "b.edu": _row("b.edu", reason="parking"),
        "c.edu": _row("c.edu", reason="empty-body"),
        "d.edu": _row("d.edu", status="Active"),
    }
    by = {d: ("US", r) for d, r in rows.items()}
    res = verify.backfill_dns_dead(cfg=cfg, state=_state(), by_domain=by,
                                   buckets={"US": list(rows.values())},
                                   deadline=time.time() + 60)
    assert res["candidates"] == 0
    assert res["retired"] == 0


def test_backfill_marks_detail_and_keeps_last_visited(monkeypatch):
    monkeypatch.setattr(verify, "dns_state", lambda d: "missing")
    cfg = _cfg()
    row = _row("gone.edu", visited="2026-05-01")
    state = _state(detail={"gone.edu": {"confidence": 0,
                                         "reason": "fetch-error:ConnectionError",
                                         "code": 0}})
    by = {"gone.edu": ("US", row)}
    verify.backfill_dns_dead(cfg=cfg, state=state, by_domain=by,
                             buckets={"US": [row]},
                             deadline=time.time() + 60)
    assert state["detail"]["gone.edu"]["reason"] == "unreachable-dns"
    # The site was never visited in this pass — don't fake a fresh timestamp.
    assert row["last_visited"] == "2026-05-01"


def old_iso() -> str:
    return iso_days_ago(400)


def iso_days_ago(days: int) -> str:
    import datetime as dt
    return (dt.datetime.now(dt.timezone.utc).date()
            - dt.timedelta(days=days)).isoformat()
