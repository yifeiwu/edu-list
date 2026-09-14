from unittest.mock import MagicMock, patch

from src import discover


def _resp(json_data=None, text="", status=200):
    r = MagicMock()
    r.status_code = status
    r.text = text
    r.headers = {}
    r.json = MagicMock(return_value=json_data)
    r.iter_content = MagicMock(return_value=iter([b"PKfake"]))
    return r


def test_no_dormant_adapters():
    for gone in ("discover_ugc", "discover_crtsh", "discover_commoncrawl",
                 "discover_stub", "discover_csv_generic", "discover_eter"):
        assert not hasattr(discover, gone), gone


def test_hipo_pagination_cursor():
    data = [{"name": f"U{i}", "alpha_two_code": "US", "domains": [f"u{i}.edu"]}
            for i in range(5)]
    with patch("src.discover._get", return_value=_resp(json_data=data)):
        st: dict = {"cursors": {}}
        out = discover.discover_hipo("http://x", st, 2)
        assert len(out) == 2
        assert st["cursors"]["hipo_offset"] == 2
        out2 = discover.discover_hipo("http://x", st, 2)
        assert out2[0]["url"] == "https://u2.edu"


def test_ror_honors_per_run_pages():
    def fake(url, timeout=30, params=None, headers=None, stream=False, tries=3, sleep_fn=None):
        page = params["page"]
        items = [{"links": [{"type": "website", "value": f"https://r{page}a.edu"}],
                  "names": [{"types": ["ror_display"], "value": f"R{page}A"}],
                  "locations": [{"geonames_details": {"country_code": "us"}}]}]
        return _resp(json_data={"items": items})
    with patch("src.discover._get", side_effect=fake):
        st: dict = {"cursors": {"ror_page": 1}}
        out = discover.discover_ror("http://ror", st, 60)
        assert len(out) == 3  # 60/20=3 pages
        assert st["cursors"]["ror_page"] == 4


def test_openalex_walks_pages():
    calls = []
    def fake(url, timeout=30, params=None, headers=None, stream=False, tries=3, sleep_fn=None):
        calls.append(params["page"])
        n = min(params["per_page"], 2)
        return _resp(json_data={"results": [
            {"display_name": f"O{params['page']}-{i}",
             "homepage_url": f"https://o{params['page']}-{i}.edu",
             "country_code": "US"} for i in range(n)]})
    with patch("src.discover._get", side_effect=fake):
        st: dict = {"cursors": {"openalex_page": 1}}
        out = discover.discover_openalex("http://oa", st, 3, mailto="a@b.c")
        assert len(out) == 3
        assert calls[0] == 1


def test_wikidata_has_order_by():
    seen = {}
    def fake(url, timeout=40, params=None, headers=None, stream=False, tries=3, sleep_fn=None):
        seen["q"] = params["query"]
        return _resp(json_data={"results": {"bindings": []}})
    with patch("src.discover._get", side_effect=fake):
        discover.discover_wikidata("http://wd", {"cursors": {}}, 10)
    assert "ORDER BY" in seen["q"]


def test_france_annuaire_pages_until_per_run():
    def fake(url, timeout=30, params=None, headers=None, stream=False, tries=3, sleep_fn=None):
        off = params["offset"]
        if off >= 2:
            return _resp(json_data={"results": []})
        return _resp(json_data={"results": [
            {"web": f"https://f{off}.fr", "nom_etablissement": f"F{off}"}]})
    with patch("src.discover._get", side_effect=fake):
        st: dict = {"cursors": {}}
        out = discover.discover_france_annuaire("http://fr", st, 2)
        assert len(out) == 2


def test_osm_single_bbox_and_cursor():
    posted = {}
    def fake_post(url, data=None, headers=None, timeout=60):
        posted["q"] = data["data"]
        r = MagicMock()
        r.status_code = 200
        r.json = MagicMock(return_value={"elements": [
            {"tags": {"amenity": "school", "website": "https://s1.edu",
                       "name": "S1"}}]})
        return r
    with patch("src.discover.requests.post", side_effect=fake_post):
        st: dict = {"cursors": {"osm_idx": 0}}
        out = discover.discover_osm("http://overpass", st, 10)
        assert out[0]["source"].startswith("osm:")
        assert st["cursors"]["osm_idx"] == 1
        assert "amenity" in posted["q"]


def test_get_retries_transient(monkeypatch):
    calls = {"n": 0}
    def fake_get(*a, **k):
        calls["n"] += 1
        r = MagicMock()
        r.status_code = 429 if calls["n"] == 1 else 200
        r.headers = {}
        r.json = MagicMock(return_value=[])
        return r
    monkeypatch.setattr("src.discover.requests.get", fake_get)
    monkeypatch.setattr("src.discover.time.sleep", lambda s: None)
    r = discover._get("http://x", 5)
    assert r.status_code == 200
    assert calls["n"] == 2


def test_nuc_table_requires_header():
    html = ("<table><tr><th>Name</th><th>X</th><th>Y</th><th>Website Address</th></tr>"
            "<tr><td>1</td><td>Uni A</td><td>X</td><td>https://unia.edu.ng</td></tr></table>"
            "<table><tr><td>junk</td></tr></table>")
    with patch("src.discover._get", return_value=_resp(text=html)), patch(
        "src.discover.time.sleep", lambda s: None
    ):
            out = discover.discover_nuc_ng("", {"cursors": {}}, 10)
    assert any(o["domain"] if "domain" in o else o["url"] for o in out)
    assert out[0]["iso2"] == "NG"


def test_deqar_csv_and_country_map():
    text = ("country,deqar_id,eter_id,name_primary,website_link\n"
            "Germany,DEQARINST1,,Test Uni,https://test-uni.de/\n"
            "Atlantis,DEQARINST2,,No Country,https://nowhere.example/\n"
            "France,DEQARINST3,,No Site,\n"
            "Italy,DEQARINST4,,Uni Roma,https://uniroma.example.it/\n"
            "Spain,DEQARINST5,,Uni Madrid,https://unimadrid.example.es/\n")
    with patch("src.discover._get", return_value=_resp(text=text)):
        st: dict = {"cursors": {}}
        out = discover.discover_deqar("http://x", st, 2)
    assert len(out) == 2
    assert out[0]["name"] == "Test Uni"
    assert out[0]["url"] == "https://test-uni.de/"
    assert out[0]["iso2"] == "DE"
    assert out[0]["source"].startswith("deqar:")
    assert out[1]["iso2"] == ""  # unknown country name
    assert st["cursors"]["deqar_offset"] == 4


def test_deqar_error_returns_empty():
    with patch("src.discover._get", return_value=_resp(status=500)):
        assert discover.discover_deqar("http://x", {"cursors": {}}, 10) == []


def test_ipeds_zip_and_cursor():
    import io as _io
    import zipfile as _zf
    buf = _io.BytesIO()
    with _zf.ZipFile(buf, "w") as zf:
        zf.writestr("HD2024.csv",
                    "UNITID,INSTNM,WEBADDR\n1,Alpha University,https://alpha.edu/\n"
                    "2,Beta College,https://beta.edu/\n"
                    "3,Gamma Institute,https://gamma.edu/\n")
    payload = buf.getvalue()

    def fake(url, timeout=120, params=None, headers=None, stream=False,
             tries=3, sleep_fn=None):
        r = MagicMock()
        r.status_code = 200
        r.iter_content = MagicMock(
            return_value=iter([payload[i:i + 65536]
                               for i in range(0, len(payload), 65536)]))
        return r

    with patch("src.discover._get", side_effect=fake):
        st: dict = {"cursors": {}}
        out = discover.discover_ipeds("https://x/HD2024.zip", st, 1)
    assert len(out) == 1
    assert out[0]["url"] == "https://alpha.edu/"
    assert out[0]["iso2"] == "US"
    assert out[0]["source"].startswith("ipeds:")
    assert st["cursors"]["ipeds_offset"] == 2


def test_ipeds_year_rollback():
    def fake(url, timeout=30, params=None, headers=None, stream=False,
             tries=3, sleep_fn=None):
        r = MagicMock()
        r.status_code = 404 if "HD2024" in url else 200
        r.iter_content = MagicMock(return_value=iter([]))
        return r

    with patch("src.discover._get", side_effect=fake):
        resolved = discover._resolve_ipeds_zip("https://x/HD2024.zip",
                                               {"cursors": {}})
    assert "HD2023.zip" in resolved


def test_sea_coverage_in_rotation():
    labels = [b[0] for b in discover.OSM_BOXES]
    assert "PH-Manila" in labels
    assert "ID-Surabaya" in labels
    assert "ID-Jakarta" in labels
    assert "IN-Delhi" in labels
    for cc in ("India", "Philippines", "Indonesia"):
        assert cc in discover.WHED_COUNTRIES
