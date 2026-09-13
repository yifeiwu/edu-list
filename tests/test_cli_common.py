from src import cli_common


def test_resolve_user_agent_default():
    assert "edu-domains-bot" in cli_common.resolve_user_agent({})
    assert cli_common.resolve_user_agent(
        {"validation": {"user_agent": "custom/1.0"}}) == "custom/1.0"


def test_resolve_mailto_prefers_explicit_then_ua():
    cfg = {"validation": {"user_agent": "bot/1.0 (contact: ops@example.org)"}}
    src_cfg = {"sources": [{"id": "openalex", "mailto": "override@example.org"}]}
    assert cli_common.resolve_mailto(cfg, src_cfg, "x") == "override@example.org"
    src_cfg2 = {"sources": [{"id": "openalex"}]}
    assert cli_common.resolve_mailto(cfg, src_cfg2, "") == "ops@example.org"
    assert cli_common.resolve_mailto({}, {"sources": []}, "") == cli_common.DEFAULT_MAILTO


def test_apply_contact_sets_both_uas():
    from src import discover, whois_check

    ua, mailto = cli_common.apply_contact(
        {"validation": {"user_agent": "test-bot/9.9 (contact: a@b.co)"}},
        {"sources": []})
    assert ua == "test-bot/9.9 (contact: a@b.co)"
    assert discover.UA == {"User-Agent": ua}
    assert whois_check.UA["User-Agent"] == ua
    assert mailto == "a@b.co"


def test_no_legacy_migrate_import():
    import src.store as store

    assert not hasattr(store, "migrate_legacy")
