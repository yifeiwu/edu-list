import time

import pytest

from src import curate
from src.curate import ADAPTERS, pick_sources


def test_no_dormant_adapters_registered():
    for gone in ("gias", "france-sup", "ugc-in", "giga",
                 "crtsh", "edudirectory", "commoncrawl", "eter"):
        assert gone not in ADAPTERS
    for keep in ("hipo", "ror", "openalex", "wikidata", "scorecard",
                 "france-annuaire", "osm", "whed", "dotgov",
                 "cricos", "nuc-ng", "nz-schools", "deqar", "ipeds"):
        assert keep in ADAPTERS


def test_pick_sources_unknown_raises():
    with pytest.raises(SystemExit):
        pick_sources([{"id": "hipo"}], True, forced="nope")


def test_pick_sources_k12_filter():
    srcs = [{"id": "hipo", "enabled": True}, {"id": "osm", "enabled": True},
            {"id": "dotgov", "enabled": True}]
    assert {s["id"] for s in pick_sources(srcs, True, "")} == {"hipo", "osm", "dotgov"}
    assert {s["id"] for s in pick_sources(srcs, False, "")} == {"hipo"}


def test_run_curate_dedupe_recite_and_blocklist(monkeypatch):
    monkeypatch.setattr(curate.discover, "UA", {"User-Agent": "t"})
    cfg = {"suffix_country": {"edu": "US"}, "blocklist": ["bad.edu"],
           "k12_enabled": True, "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "http://x", "timeout_seconds": 5}]}
    state: dict = {"cursors": {}}
    by = {"known.edu": ("US", {"sources": "hipo:old", "web_domain": "known.edu"})}
    buckets: dict = {"US": [{"web_domain": "known.edu", "sources": "hipo:old"}]}
    pending: list = []
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "Known", "url": "https://known.edu", "iso2": "US",
         "type_hint": "university", "source": "hipo:new"},
        {"name": "Bad", "url": "https://bad.edu", "iso2": "US",
         "type_hint": "", "source": "hipo:new"},
        {"name": "New Uni", "url": "https://newuni.edu", "iso2": "",
         "type_hint": "", "source": "hipo:new"},
    ])
    stats = curate.run_curate(cfg=cfg, src_cfg=src_cfg, state=state,
                              by_domain=by, buckets=buckets, pending=pending,
                              deadline=time.time() + 60)
    assert stats["recited"] == 1
    assert "hipo:new" in by["known.edu"][1]["sources"]
    assert all(p["domain"] != "bad.edu" for p in pending)
    assert pending[0]["domain"] == "newuni.edu"
    assert pending[0]["iso2"] == "US"  # suffix fallback


def test_run_curate_max_pending_and_xx(monkeypatch):
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 1}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "u", "timeout_seconds": 1}]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "A", "url": "https://a123.example", "iso2": "", "type_hint": "",
         "source": "s"},
        {"name": "B", "url": "https://b123.example", "iso2": "", "type_hint": "",
         "source": "s"},
    ])
    stats = curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={}, by_domain={},
                              buckets={}, pending=[],
                              deadline=time.time() + 60)
    assert stats["new"] == 1


def test_run_curate_academic_fallback_and_unmapped_count(monkeypatch):
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "u", "timeout_seconds": 1}]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "SN Univ", "url": "https://univ-foo.edu.sn", "iso2": "",
         "type_hint": "", "source": "s"},
        {"name": "Nowhere", "url": "https://foo123.example", "iso2": "",
         "type_hint": "", "source": "s"},
    ])
    pending: list = []
    stats = curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={}, by_domain={},
                              buckets={}, pending=pending,
                              deadline=time.time() + 60)
    by_iso = {p["domain"]: p["iso2"] for p in pending}
    assert by_iso["univ-foo.edu.sn"] == "SN"  # generic edu.<cc> fallback
    assert by_iso["foo123.example"] == "XX"
    assert stats["unmapped"] == 1


def test_placeholder_contact_guard():
    with pytest.raises(SystemExit):
        curate.assert_configured_contact(
            {"validation": {"user_agent": "x YOUR_USER y"}})


def test_run_curate_skips_service_hosts(monkeypatch):
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "u", "timeout_seconds": 1}]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "Mail", "url": "https://mail.example.edu", "iso2": "US",
         "type_hint": "", "source": "s"},
        {"name": "LMS", "url": "https://moodle.example.edu", "iso2": "US",
         "type_hint": "", "source": "s"},
        {"name": "Real", "url": "https://real.example.edu", "iso2": "US",
         "type_hint": "", "source": "s"},
    ])
    pending: list = []
    stats = curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={}, by_domain={},
                              buckets={}, pending=pending,
                              deadline=time.time() + 60)
    assert [p["domain"] for p in pending] == ["real.example.edu"]
    assert stats["new"] == 1
    assert stats["skipped_service"] == 2


def test_run_curate_drops_queued_service_hosts(monkeypatch):
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "u", "timeout_seconds": 1}]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [])
    pending = [{"name": "M", "url": "https://mail.example.edu",
                "domain": "mail.example.edu", "iso2": "US",
                "type_hint": "", "source": "s"},
               {"name": "R", "url": "https://real.example.edu",
                "domain": "real.example.edu", "iso2": "US",
                "type_hint": "", "source": "s"}]
    curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={}, by_domain={},
                      buckets={}, pending=pending,
                      deadline=time.time() + 60)
    assert [p["domain"] for p in pending] == ["real.example.edu"]


def test_suffix_defaults_merged(monkeypatch):
    # Empty user map still resolves .edu via geo defaults.
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                            "url": "u", "timeout_seconds": 1}]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "U", "url": "https://someuni.edu", "iso2": "",
         "type_hint": "", "source": "s"},
    ])
    pending: list = []
    curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={}, by_domain={},
                      buckets={}, pending=pending,
                      deadline=time.time() + 60)
    assert pending[0]["iso2"] == "US"


def test_recite_promotes_xx_row_to_candidate_country(monkeypatch):
    row = {"web_domain": "lagos-sch.ng", "sources": "osm:NG-Lagos",
           "school_name": "Lagos School"}
    by = {"lagos-sch.ng": ("XX", row)}
    buckets: dict = {"XX": [row]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "Lagos School", "url": "https://lagos-sch.ng", "iso2": "NG",
         "type_hint": "", "source": "hipo:2026-09-14"},
    ])
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                             "url": "u", "timeout_seconds": 1}]}
    stats = curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={},
                              by_domain=by, buckets=buckets, pending=[],
                              deadline=time.time() + 60)
    assert by["lagos-sch.ng"][0] == "NG"
    assert buckets["XX"] == []
    assert buckets["NG"] == [row]
    assert {"XX", "NG"} <= stats["touched"]


def test_recite_keeps_country_when_candidate_xx(monkeypatch):
    row = {"web_domain": "known.edu", "sources": "hipo:old"}
    by = {"known.edu": ("US", row)}
    buckets: dict = {"US": [row]}
    monkeypatch.setattr(curate.discover, "discover_hipo", lambda *a, **k: [
        {"name": "Known", "url": "https://known.edu", "iso2": "",
         "type_hint": "", "source": "hipo:new"},
    ])
    cfg = {"suffix_country": {}, "blocklist": [], "k12_enabled": True,
           "run": {"max_pending": 10}}
    src_cfg = {"sources": [{"id": "hipo", "enabled": True, "per_run": 10,
                             "url": "u", "timeout_seconds": 1}]}
    curate.run_curate(cfg=cfg, src_cfg=src_cfg, state={},
                      by_domain=by, buckets=buckets, pending=[],
                      deadline=time.time() + 60)
    assert by["known.edu"][0] == "US"
    assert buckets["US"] == [row]
