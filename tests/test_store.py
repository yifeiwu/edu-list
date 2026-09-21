import datetime as dt

from src import store


def test_today_iso_is_utc(tmp_path):
    # Format check + UTC date (not local): just assert ISO format parses.
    v = store.today_iso()
    assert dt.date.fromisoformat(v).isoformat() == v


def test_atomic_write_and_roundtrip(tmp_path):
    d = tmp_path / "countries"
    buckets = {"US": [{"school_name": "A", "web_domain": "b.edu",
                       "type": "university/college", "last_visited": "2026-09-12",
                       "status": "Active", "sources": "hipo:x",
                       "years_registered": "10", "confidence": "85",
                       "reason": "http-2xx-html", "final_domain": "b.edu",
                       "language": "en"},
                      {"school_name": "B", "web_domain": "a.edu",
                       "type": "other", "last_visited": "2026-09-12",
                       "status": "Inaccessible", "sources": "ror:x",
                       "years_registered": ""}]}
    store.save_touched(d, buckets, {"US"})
    by, buck = store.load_all(d)
    assert [r["web_domain"] for r in buck["US"]] == ["a.edu", "b.edu"]
    assert by["a.edu"][0] == "US"
    assert by["b.edu"][1]["confidence"] == "85"
    assert by["b.edu"][1]["language"] == "en"
    # Rows predating the new columns load with "" defaults.
    assert by["a.edu"][1]["confidence"] == ""
    assert by["a.edu"][1]["final_domain"] == ""
    # No temp files leaked.
    assert list(d.glob(".tmp-*")) == []


def test_load_all_validates_schema(tmp_path):
    d = tmp_path / "c"
    d.mkdir()
    (d / "US.csv").write_text(
        "school_name,web_domain,type,last_visited,status,sources,years_registered\n"
        "Good,g.edu,university/college,2026-09-12,Active,s,1\n"
        "BadStatus,b.edu,other,2026-09-12,Bogus,s,\n"
        "BadType,t.edu,weird,2026-09-12,Active,s,\n"
        "BadDate,dd.edu,other,not-a-date,Active,s,\n", encoding="utf-8")
    by, _buck = store.load_all(d)
    assert "g.edu" in by
    assert "b.edu" not in by  # invalid status dropped
    assert by["t.edu"][1]["type"] == "other"  # normalized
    assert by["dd.edu"][1]["last_visited"] == "2000-01-01"
    # Pre-column rows get "" for the new fields.
    assert by["g.edu"][1]["confidence"] == ""
    assert by["g.edu"][1]["reason"] == ""
    assert by["g.edu"][1]["final_domain"] == ""
    assert by["g.edu"][1]["language"] == ""


def test_purge_blocklisted(tmp_path):
    buckets = {"US": [{"school_name": "X", "web_domain": "bad.edu",
                       "type": "other", "last_visited": "2026-09-12",
                       "status": "Active", "sources": "s",
                       "years_registered": ""}]}
    by = {"bad.edu": ("US", buckets["US"][0])}
    state: dict = {"failures": {"bad.edu": 3}, "detail": {"bad.edu": {}},
                   "moved": {"bad.edu": "x"}, "domain_age": {"bad.edu": "2020-01-01"}}
    touched = store.purge_blocklisted(by, buckets, state, {"BAD.edu"})
    assert touched == {"US"}
    assert by == {}
    assert buckets["US"] == []
    assert state["failures"] == {}


def test_pending_roundtrip_and_corrupt(tmp_path):
    p = tmp_path / "pending.json"
    store.save_pending(p, [{"domain": "a.edu", "name": "A"}])
    assert store.load_pending(p)[0]["domain"] == "a.edu"
    p.write_text("not json", encoding="utf-8")
    assert store.load_pending(p) == []
    assert list(tmp_path.glob("*.corrupt.json")) != []


def test_state_drops_legacy_keys(tmp_path):
    p = tmp_path / "state.json"
    p.write_text('{"cursors": {"hipo_offset": 5}, "next_idx": 0, '
                 '"per_country_last_discovery": {}}',
                 encoding="utf-8")
    s = store.load_state(p)
    assert "next_idx" not in s
    assert "per_country_last_discovery" not in s
    assert "hipo_offset" not in s["cursors"]
    assert "moved" in s and "domain_age" in s
    store.save_state(p, s)
    assert "next_idx" not in p.read_text(encoding="utf-8")


def test_state_scrubs_tls_unverified(tmp_path):
    import json

    p = tmp_path / "state.json"
    p.write_text(json.dumps({"cursors": {},
                             "detail": {"a.edu": {"reason": "http-2xx-html+tls-unverified",
                                                  "code": 200, "confidence": 50}}}),
                 encoding="utf-8")
    s = store.load_state(p)
    assert "tls-unverified" not in s["detail"]["a.edu"]["reason"]
