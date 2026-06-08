#!/usr/bin/env -S uv run
# /// script
# dependencies = ["markdown>=3.5"]
# ///
"""Unit tests for wiki_server.py core functions."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_server import parse_frontmatter, render_metadata, _looks_like_url


def test_looks_like_url():
    assert _looks_like_url("https://example.com") is True
    assert _looks_like_url("http://example.com") is True
    assert _looks_like_url("ftp://files.example.org") is True
    assert _looks_like_url("not a url") is False
    assert _looks_like_url("Space Architecture Research Group, 2025") is False
    assert _looks_like_url("/relative/path") is False


def test_parse_frontmatter_empty():
    md, body = parse_frontmatter("no frontmatter here")
    assert md == {}
    assert body == "no frontmatter here"


def test_parse_frontmatter_simple():
    text = """---
title: "Test Page"
type: source_summary
status: current
---
Body content"""
    md, body = parse_frontmatter(text)
    assert md["title"] == "Test Page"
    assert md["type"] == "source_summary"
    assert md["status"] == "current"
    assert body == "Body content"


def test_parse_frontmatter_origin_url_string():
    text = """---
title: "Test"
origin_url: "https://example.com"
---
Body"""
    md, body = parse_frontmatter(text)
    assert md["origin_url"] == "https://example.com"


def test_parse_frontmatter_origin_url_list():
    text = """---
title: "Test"
origin_url:
  - "Source A (2024)"
  - "Source B (2025)"
---
Body"""
    md, body = parse_frontmatter(text)
    assert md["origin_url"] == ["Source A (2024)", "Source B (2025)"]


def test_parse_frontmatter_sources_list():
    text = """---
title: "Test"
sources:
  - "file-a.md"
  - "file-b.md"
---
Body"""
    md, body = parse_frontmatter(text)
    assert md["sources"] == ["file-a.md", "file-b.md"]


def test_render_metadata_empty():
    assert render_metadata({}) == ""


def test_render_metadata_url_string():
    html = render_metadata({"origin_url": "https://example.com/article"})
    assert '<a href="https://example.com/article"' in html
    assert "Source URL →" in html
    assert 'target="_blank"' in html


def test_render_metadata_descriptive_string():
    html = render_metadata({"origin_url": "Space Architecture Research Group, 2025"})
    assert "Space Architecture Research Group, 2025" in html
    assert "<a " not in html


def test_render_metadata_list():
    html = render_metadata({
        "origin_url": [
            "MDPI Applied Sciences (2023)",
            "ScienceDirect (2025)",
        ]
    })
    assert "MDPI Applied Sciences (2023)" in html
    assert "ScienceDirect (2025)" in html
    assert "Sources:" in html


def test_render_metadata_list_with_urls():
    html = render_metadata({
        "origin_url": [
            "https://example.com/paper1",
            "Some Report (2025)",
        ]
    })
    assert '<a href="https://example.com/paper1"' in html
    assert "Some Report (2025)" in html
    assert "Sources:" in html


def test_render_metadata_full_box():
    html = render_metadata({
        "type": "source_summary",
        "status": "current",
        "created": "2026-06-07",
        "sources": ["test.md"],
        "origin_url": "https://example.com",
    })
    assert '<div class="meta-box">' in html
    assert "Source Summary" in html
    assert "current" in html
    assert "Created: 2026-06-07" in html
    assert "test.md" in html
    assert '<a href="https://example.com"' in html


def test_render_metadata_no_origin():
    html = render_metadata({"type": "source_summary", "status": "current"})
    assert "origin_url" not in html
    assert "Source URL" not in html


if __name__ == "__main__":
    tests = [
        ("_looks_like_url", test_looks_like_url),
        ("parse empty", test_parse_frontmatter_empty),
        ("parse simple", test_parse_frontmatter_simple),
        ("parse origin_url string", test_parse_frontmatter_origin_url_string),
        ("parse origin_url list", test_parse_frontmatter_origin_url_list),
        ("parse sources list", test_parse_frontmatter_sources_list),
        ("render empty", test_render_metadata_empty),
        ("render URL string", test_render_metadata_url_string),
        ("render descriptive string", test_render_metadata_descriptive_string),
        ("render list", test_render_metadata_list),
        ("render list with URLs", test_render_metadata_list_with_urls),
        ("render full box", test_render_metadata_full_box),
        ("render no origin", test_render_metadata_no_origin),
    ]
    passed = 0
    failed = 0
    for name, fn in tests:
        try:
            fn()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"  FAIL: {name} — {e}", file=sys.stderr)
        except Exception as e:
            failed += 1
            print(f"  ERROR: {name} — {e}", file=sys.stderr)
    total = passed + failed
    print(f"\n{passed}/{total} tests passed" + ("" if not failed else f", {failed} FAILED"))
    sys.exit(0 if not failed else 1)
