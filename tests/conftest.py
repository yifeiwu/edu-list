"""Shared fixtures: sample homepages + fake HTTP responses."""
import sys
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

ACTIVE_HTML = """<html><head><title>Springfield University - Admissions</title>
<link rel="canonical" href="https://example.edu/">
<link rel="icon" href="/favicon.ico">
<script type="application/ld+json">{"@type": "CollegeOrUniversity"}</script>
</head><body><h1>Welcome to Springfield University</h1>
<p>Our university offers admissions, academics, faculties, campus life for students.</p>
<a href="/admissions">Admissions</a><a href="/academics">Academics</a>
<a href="/contact">Contact</a><p>© 2025 Springfield University. All rights reserved.</p>
<p>{extra}</p></body></html>"""


def make_response(url="https://example.edu/", status=200,
                  text=ACTIVE_HTML, ctype="text/html",
                  encoding="utf-8"):
    r = MagicMock()
    r.status_code = status
    r.url = url
    r.headers = {"Content-Type": ctype}
    r.encoding = encoding
    r.text = text
    raw = text.encode(encoding)
    def _iter(chunk_size=32768):
        for i in range(0, len(raw), 32768):
            yield raw[i:i + 32768]
        if not raw:
            yield b""
    r.iter_content = MagicMock(side_effect=_iter)
    r.close = MagicMock()
    return r
