from src.summarize import compute_alerts, write_summary


def _buckets():
    return {"US": [
        {"school_name": "A", "web_domain": "a.edu", "type": "university/college",
         "last_visited": "2026-09-12", "status": "Active",
         "sources": "hipo:x", "years_registered": "10"},
        {"school_name": "B", "web_domain": "b.edu", "type": "other",
         "last_visited": "2020-01-01", "status": "Inaccessible",
         "sources": "ror:x", "years_registered": "20"},
        {"school_name": "C", "web_domain": "c.edu", "type": "other",
         "last_visited": "2026-09-12", "status": "Active",
         "sources": "s", "years_registered": "30"},
    ]}


def test_median_even_count(tmp_path):
    buckets = {"US": [
        {"school_name": str(i), "web_domain": f"d{i}.edu", "type": "other",
         "last_visited": "2026-09-12", "status": "Active", "sources": "s",
         "years_registered": str(v)}
        for i, v in enumerate([10, 20])]}
    p = tmp_path / "SUMMARY.md"
    write_summary(p, buckets, {"failures": {}, "detail": {}}, 0)
    text = p.read_text(encoding="utf-8")
    assert "median 15 yrs" in text  # (10+20)/2, not 20


def test_archive_after_from_config(tmp_path):
    p = tmp_path / "S.md"
    write_summary(p, _buckets(), {"failures": {"b.edu": 2}, "detail": {}}, 5,
                  archive_after=2)
    assert "Archived chronic failures (re-check paused): **1**" in p.read_text(encoding="utf-8")
    write_summary(p, _buckets(), {"failures": {"b.edu": 2}, "detail": {}}, 5,
                  archive_after=6)
    assert "Archived chronic failures (re-check paused): **0**" in p.read_text(encoding="utf-8")


def test_moved_and_tls_copy(tmp_path):
    p = tmp_path / "S.md"
    write_summary(p, _buckets(),
                  {"failures": {}, "detail": {}, "moved": {"x": "y"}}, 0)
    text = p.read_text(encoding="utf-8")
    assert "Moved pointers" in text
    assert "valid TLS" in text


def _big_buckets(iso, total, active):
    rows = []
    for i in range(total):
        rows.append({"school_name": f"S{i}", "web_domain": f"d{i}.{iso.lower()}.edu",
                     "type": "other", "last_visited": "2026-09-12",
                     "status": "Active" if i < active else "Inaccessible",
                     "sources": "s", "years_registered": ""})
    return {iso: rows}


def test_alerts_low_active_and_blocked():
    buckets = _big_buckets("US", 10, 2)  # 20% active
    state = {"detail": {f"d{i}.us.edu": {"reason": "http-403", "code": 403,
                                         "confidence": 5}
                        for i in range(2, 6)}}
    alerts = compute_alerts(buckets, state)
    assert any("low Active rate" in a and "US" in a for a in alerts)
    assert any("blocked" in a and "US" in a for a in alerts)


def test_alerts_xx_bucket(tmp_path):
    buckets = {"XX": [{"school_name": "X", "web_domain": "foo123.example",
                       "type": "other", "last_visited": "2026-09-12",
                       "status": "Inaccessible", "sources": "s",
                       "years_registered": ""}]}
    alerts = compute_alerts(buckets, {})
    assert any("XX" in a for a in alerts)
    p = tmp_path / "S.md"
    write_summary(p, buckets, {"failures": {}, "detail": {}}, 0)
    assert "## Alerts" in p.read_text(encoding="utf-8")


def test_alerts_quiet_when_healthy():
    buckets = _big_buckets("US", 10, 9)
    assert compute_alerts(buckets, {"detail": {}}) == []
