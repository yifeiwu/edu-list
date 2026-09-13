"""Shared CLI boilerplate — single implementation for curate/verify/crawl.

Previously `log`, `load_cfg`, `assert_configured_contact` and path/state
handling were triplicated across entrypoints and drifted (e.g. `crawl.py`
dropped `unmapped` from `last_curate`). Import from here instead.

Contact identity (consolidated):
- `validation.user_agent` in `config.yaml` is authoritative.
- OpenAlex `mailto` resolves as: `sources.yaml` `mailto` override, else the
  email embedded in the UA (`contact: someone@example.com`), else
  `DEFAULT_MAILTO`.
- `discover.UA` and `whois_check.UA` are both set from the resolved UA via
  `apply_contact()` so all outbound HTTP shares one identity.
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

DEFAULT_USER_AGENT = (
    "edu-domains-bot/1.0 (github-actions; educational-research)"
)
DEFAULT_MAILTO = "edu-domains-bot@example.com"

_EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def log(msg: str) -> None:
    print(f"[{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}] {msg}",
          flush=True)


def load_cfg(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def assert_configured_contact(cfg: dict) -> None:
    ua = str(cfg.get("validation", {}).get("user_agent", ""))
    if "YOUR_USER" in ua or "you@example.com" in ua:
        raise SystemExit(
            "config.yaml still contains placeholder contact "
            "(YOUR_USER/you@example.com). Set validation.user_agent so "
            "operators can reach you before running non-dry-run.")


def resolve_user_agent(cfg: dict) -> str:
    return str(cfg.get("validation", {}).get("user_agent", "") or DEFAULT_USER_AGENT)


def resolve_mailto(cfg: dict, src_cfg: dict, user_agent: str = "") -> str:
    """OpenAlex polite-pool contact: explicit override wins, else UA email."""
    for src in (src_cfg.get("sources", []) or []):
        if isinstance(src, dict) and src.get("id") == "openalex" and src.get("mailto"):
            return str(src["mailto"])
    ua = user_agent or resolve_user_agent(cfg)
    m = _EMAIL_RE.search(ua)
    if m and "example.com" not in m.group(0):
        return m.group(0)
    return DEFAULT_MAILTO


def apply_contact(cfg: dict, src_cfg: dict | None = None) -> tuple[str, str]:
    """Set module-global UAs from config. Returns (user_agent, mailto)."""
    from src import discover as _discover
    from src import whois_check as _whois

    ua = resolve_user_agent(cfg)
    mailto = resolve_mailto(cfg, src_cfg or {}, ua)
    _discover.UA = {"User-Agent": ua}
    _whois.UA = {
        "User-Agent": ua,
        "Accept": "application/rdap+json, application/json",
    }
    return ua, mailto


def resolve_paths(cfg: dict) -> dict[str, Path]:
    out = cfg.get("output", {}) or {}
    countries_dir = ROOT / out.get("countries_dir", "data/countries")
    index_path = ROOT / out.get("index_path", "data/countries/INDEX.md")
    state_path = ROOT / cfg.get("state_path", "state/state.json")
    pending_path = state_path.parent / "pending.json"
    return {
        "countries_dir": countries_dir,
        "index_path": index_path,
        "state_path": state_path,
        "pending_path": pending_path,
    }


def load_runtime(state_path: Path, countries_dir: Path, pending_path: Path):
    """Load (state, by_domain, buckets, pending) with lazy imports (no cycle)."""
    from src.store import load_all, load_pending, load_state

    state = load_state(state_path)
    by_domain, buckets = load_all(countries_dir)
    pending = load_pending(pending_path)
    return state, by_domain, buckets, pending


def save_runtime(*, countries_dir, buckets, touched: set[str],
                 index_path, pending_path, pending,
                 state_path, state, summary_pending: int | None = None,
                 archive_after: int = 6) -> None:
    """Persist touched countries + index + queue + state + SUMMARY.md."""
    from src.store import save_pending, save_state, save_touched, write_index
    from src.summarize import write_summary

    save_touched(countries_dir, buckets, touched)
    write_index(index_path, buckets)
    save_pending(pending_path, pending)
    save_state(state_path, state)
    write_summary(ROOT / "SUMMARY.md", buckets, state,
                  len(pending) if summary_pending is None else summary_pending,
                  archive_after=archive_after)
