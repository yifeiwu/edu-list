import datetime as dt

from src import whois_check


def test_whole_years_leap_aware():
    assert whois_check.whole_years_since(dt.date(2000, 2, 29), dt.date(2026, 2, 28)) == 25
    assert whois_check.whole_years_since(dt.date(2000, 2, 29), dt.date(2026, 3, 1)) == 26
    assert whois_check.whole_years_since(dt.date(2020, 9, 12), dt.date(2026, 9, 11)) == 5
    assert whois_check.whole_years_since(dt.date(2020, 9, 12), dt.date(2026, 9, 12)) == 6
    assert whois_check.whole_years_since(dt.date(2030, 1, 1), dt.date(2026, 1, 1)) is None


def test_years_registered_uses_cache(monkeypatch):
    cache: dict = {}
    monkeypatch.setattr(whois_check, "registration_date",
                        lambda d, timeout=8: dt.date(2000, 1, 15))
    y = whois_check.years_registered("x.edu", today=dt.date(2026, 1, 14), cache=cache)
    assert y == 25
    assert cache["x.edu"] == "2000-01-15"
    # Second call must not hit network.
    monkeypatch.setattr(whois_check, "registration_date",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError("network")))
    y2 = whois_check.years_registered("x.edu", today=dt.date(2026, 1, 16), cache=cache)
    assert y2 == 26


def test_years_registered_negative_cache(monkeypatch):
    cache: dict = {}
    monkeypatch.setattr(whois_check, "registration_date", lambda *a, **k: None)
    today = dt.date(2026, 9, 12)
    assert whois_check.years_registered("missing.edu", today=today, cache=cache) is None
    entry = cache["missing.edu"]
    assert isinstance(entry, dict) and entry.get("reg") == ""
    assert entry.get("ts") == "2026-09-12"
    # Cached miss stays a miss without network (within TTL).
    monkeypatch.setattr(whois_check, "registration_date",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError()))
    assert whois_check.years_registered("missing.edu", today=today, cache=cache) is None


def test_years_registered_negative_cache_expires(monkeypatch):
    cache: dict = {"old.edu": {"reg": "", "ts": "2026-01-01"}}
    monkeypatch.setattr(whois_check, "registration_date",
                        lambda d, timeout=8: dt.date(2000, 1, 15))
    y = whois_check.years_registered("old.edu", today=dt.date(2026, 9, 12),
                                     cache=cache)
    assert y == 26
    assert cache["old.edu"] == "2000-01-15"


def test_years_registered_legacy_bare_miss_retries(monkeypatch):
    cache: dict = {"legacy.edu": ""}
    monkeypatch.setattr(whois_check, "registration_date",
                        lambda d, timeout=8: dt.date(2010, 6, 1))
    y = whois_check.years_registered("legacy.edu", today=dt.date(2026, 6, 1),
                                     cache=cache)
    assert y == 16


def test_parse_registration_date():
    obj = {"events": [{"eventAction": "registration",
                       "eventDate": "2001-05-06T00:00:00Z"}]}
    assert whois_check.parse_registration_date(obj) == dt.date(2001, 5, 6)
    assert whois_check.parse_registration_date({}) is None


def test_parse_whois_dates():
    assert whois_check.parse_creation_date_whois("Creation Date: 2001-05-06T00:00:00Z") == dt.date(2001, 5, 6)
    assert whois_check.parse_creation_date_whois("no date here") is None
