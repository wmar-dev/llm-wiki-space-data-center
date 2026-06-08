#!/usr/bin/env -S uv run
# /// script
# dependencies = ["markdown>=3.5"]
# ///
"""Local wiki server — renders wiki/*.md as HTML, served at http://localhost:PORT."""

import argparse
import errno
import json
import os
import re
import sys
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import List, Optional
import urllib.parse

try:
    import markdown
except ImportError:
    print("Error: 'markdown' package not installed. Run: pip3 install markdown", file=sys.stderr)
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MAX_FILE_BYTES = 5 * 1024 * 1024  # 5 MB
MD_EXTENSIONS = ["tables", "fenced_code", "attr_list", "def_list"]


@dataclass
class ServerConfig:
    port: int = 8000
    wiki_root: Path = PROJECT_ROOT
    live_reload: bool = True
    poll_interval_ms: int = 2000
    project_title: str = "Wiki"


@dataclass
class NavEntry:
    label: str
    url_path: str
    is_active: bool


_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 16px; line-height: 1.6; color: #24292e;
  display: flex; min-height: 100vh;
}
nav {
  width: 220px; min-width: 220px; background: #f6f8fa;
  border-right: 1px solid #e1e4e8; padding: 24px 16px;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
}
nav h2 {
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: .05em; color: #586069; margin-bottom: 10px;
}
nav ul { list-style: none; padding: 0; }
nav li { margin-bottom: 2px; }
nav li a {
  display: block; padding: 5px 8px; border-radius: 4px;
  color: #24292e; text-decoration: none; font-size: 14px;
}
nav li a:hover { background: #e1e4e8; }
nav li a.active { background: #0075ca; color: white; }
main { flex: 1; padding: 32px 48px; max-width: 920px; overflow-x: auto; }
h1 {
  font-size: 2em; font-weight: 600;
  border-bottom: 1px solid #e1e4e8; padding-bottom: 8px;
  margin-top: 0; margin-bottom: 16px;
}
h2 {
  font-size: 1.5em; font-weight: 600;
  border-bottom: 1px solid #e1e4e8; padding-bottom: 6px;
  margin-top: 24px; margin-bottom: 16px;
}
h3, h4, h5, h6 { font-weight: 600; margin-top: 24px; margin-bottom: 16px; }
h3 { font-size: 1.25em; }
p { margin-bottom: 16px; }
a { color: #0075ca; }
a:hover { text-decoration: underline; }
code {
  background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 3px;
  padding: 2px 5px; font-size: 85%;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
pre {
  background: #f6f8fa; border: 1px solid #e1e4e8; border-radius: 6px;
  padding: 16px; overflow: auto; margin-bottom: 16px;
}
pre code { background: none; border: none; padding: 0; font-size: 93%; }
blockquote { border-left: 4px solid #dfe2e5; padding: 0 16px; color: #6a737d; margin-bottom: 16px; }
ul, ol { padding-left: 2em; margin-bottom: 16px; }
li { margin-bottom: 4px; }
table { border-collapse: collapse; width: 100%; margin-bottom: 16px; display: block; overflow-x: auto; }
th, td { border: 1px solid #dfe2e5; padding: 6px 13px; text-align: left; }
th { background: #f6f8fa; font-weight: 600; }
tr:nth-child(even) { background: #f6f8fa; }
hr { border: none; border-top: 1px solid #e1e4e8; margin: 24px 0; }
img { max-width: 100%; }
.meta-box {
  background: #f1f8ff; border: 1px solid #c8e1ff; border-radius: 6px;
  padding: 12px 16px; margin-bottom: 24px; font-size: 13px; color: #586069;
  display: flex; flex-wrap: wrap; gap: 8px; align-items: center;
}
.meta-type { font-weight: 600; color: #0075ca; }
.meta-status {
  padding: 2px 8px; border-radius: 12px; font-size: 11px;
  font-weight: 600; text-transform: uppercase;
}
.meta-draft { background: #fff3cd; color: #856404; }
.meta-current { background: #d4edda; color: #155724; }
.meta-stale { background: #f8d7da; color: #721c24; }
.meta-contested { background: #f8d7da; color: #721c24; }
.meta-date { color: #6a737d; }
.meta-sources { color: #6a737d; }
.meta-sources code { font-size: 12px; }
"""

_LIVE_RELOAD_JS_TMPL = """
<script>
(function() {
    var lastMtime = null;
    setInterval(function() {
        fetch('/__mtime')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                if (lastMtime === null) { lastMtime = data.mtime; return; }
                if (data.mtime > lastMtime) { location.reload(); }
            })
            .catch(function() {});
    }, {POLL_MS});
})();
</script>
"""


# ---------------------------------------------------------------------------
# Project title
# ---------------------------------------------------------------------------

def read_project_title(wiki_root: Path) -> str:
    claude_md = wiki_root / "CLAUDE.md"
    if claude_md.exists():
        for line in claude_md.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return "Wiki"


# ---------------------------------------------------------------------------
# Core rendering helpers
# ---------------------------------------------------------------------------

def expand_wikilinks(text: str) -> str:
    # Convert [[wiki/path/to/page.md]] to [label](/wiki/path/to/page) markdown links.
    def replace(m: re.Match) -> str:
        raw = m.group(1).strip()
        url = ("/" + raw) if not raw.startswith("/") else raw
        if url.endswith(".md"):
            url = url[:-3]
        label = Path(raw).stem.replace("-", " ").replace("_", " ")
        return f"[{label}]({url})"
    return re.sub(r"\[\[([^\]]+)\]\]", replace, text)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Strip YAML frontmatter delimited by --- and return (metadata, body)."""
    cleaned = text.lstrip("\n")
    if not cleaned.startswith("---"):
        return {}, text
    end = cleaned.find("---", 3)
    if end == -1:
        return {}, text
    yaml_block = cleaned[3:end].strip()
    body = cleaned[end + 3:].lstrip("\n")
    metadata = {}
    current_list_key = None
    for line in yaml_block.split("\n"):
        s = line.strip()
        if not s:
            continue
        if s.startswith("- "):
            if current_list_key:
                val = s[2:].strip().strip("\"").strip("'")
                metadata.setdefault(current_list_key, []).append(val)
            continue
        if ":" in s:
            key, _, value = s.partition(":")
            key = key.strip()
            value = value.strip().strip("\"").strip("'")
            if value:
                metadata[key] = value
                current_list_key = None
            else:
                current_list_key = key
    return metadata, body


def render_metadata(metadata: dict) -> str:
    """Render frontmatter metadata as a styled info box."""
    if not metadata:
        return ""
    parts = []
    t = metadata.get("type", "")
    if t:
        parts.append(f'<span class="meta-type">{t.replace("_", " ").title()}</span>')
    s = metadata.get("status", "")
    if s:
        parts.append(f'<span class="meta-status meta-{s}">{s}</span>')
    c = metadata.get("created", "")
    u = metadata.get("last_updated", "")
    if c:
        parts.append(f'<span class="meta-date">Created: {c}</span>')
    if u:
        parts.append(f'<span class="meta-date">Updated: {u}</span>')
    sources = metadata.get("sources", [])
    if isinstance(sources, str):
        sources = [sources]
    if sources:
        src_list = ", ".join(f"<code>{x}</code>" for x in sources)
        parts.append(f'<span class="meta-sources">Sources: {src_list}</span>')
    origin = metadata.get("origin_url", "")
    if origin:
        parts.append(f'<span class="meta-origin"><a href="{origin}" target="_blank" rel="noopener">Source URL →</a></span>')
    if not parts:
        return ""
    return f'<div class="meta-box">{" · ".join(parts)}</div>\n'


def render_markdown(fs_path: Path) -> tuple[str, dict]:
    if not fs_path.exists():
        raise FileNotFoundError(fs_path)
    if fs_path.stat().st_size > MAX_FILE_BYTES:
        raise OverflowError("File exceeds 5 MB limit")
    text = expand_wikilinks(fs_path.read_text(encoding="utf-8"))
    metadata, body = parse_frontmatter(text)
    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    html = md.convert(body)
    return html, metadata


def rewrite_md_links(html: str) -> str:
    # Strip .md extension from relative hrefs so browser-side links resolve.
    # Preserves https://, //, and anchor-only (#) hrefs unchanged.
    return re.sub(
        r'href="(?!https?://|//|#)([^"]*?)\.md(#[^"]*?)?"',
        lambda m: f'href="{m.group(1)}{m.group(2) or ""}"',
        html,
    )


def extract_title(html: str, fallback: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else fallback


def build_nav(current_url_path: str, wiki_root: Path) -> List[NavEntry]:
    entries: List[NavEntry] = []
    is_home = current_url_path in ("/", "")
    entries.append(NavEntry("Index", "/", is_home))

    wiki_dir = wiki_root / "wiki"
    if wiki_dir.is_dir():
        for section in sorted(wiki_dir.iterdir()):
            if section.is_dir() and not section.name.startswith("."):
                url = f"/wiki/{section.name}"
                entries.append(NavEntry(section.name.capitalize(), url, current_url_path.startswith(url)))

    return entries


def page_shell(title: str, body: str, nav: List[NavEntry], config: ServerConfig) -> str:
    nav_items_parts = []
    for e in nav:
        cls = ' class="active"' if e.is_active else ""
        nav_items_parts.append(f'    <li><a href="{e.url_path}"{cls}>{e.label}</a></li>')
    nav_items = "\n".join(nav_items_parts)
    reload_js = _LIVE_RELOAD_JS_TMPL.replace("{POLL_MS}", str(config.poll_interval_ms)) if config.live_reload else ""
    return (
        f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
        f"<meta charset='utf-8'>\n"
        f"<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
        f"<title>{title}</title>\n"
        f"<style>{_CSS}</style>\n"
        f"</head>\n<body>\n"
        f"<nav>\n  <h2>{config.project_title}</h2>\n  <ul>\n{nav_items}\n  </ul>\n</nav>\n"
        f"<main>\n{body}\n</main>\n"
        f"{reload_js}"
        f"</body>\n</html>"
    )


def dir_listing_html(dir_path: Path, url_prefix: str, title: str) -> str:
    pages = sorted(p for p in dir_path.iterdir() if p.suffix == ".md" and not p.name.startswith("."))
    if not pages:
        return f"<h1>{title}</h1>\n<p>No pages in this section.</p>"
    items = "\n".join(
        f'  <li><a href="{url_prefix}/{p.stem}">'
        f'{p.stem.replace("-", " ").replace("_", " ").title()}</a></li>'
        for p in pages
    )
    return f"<h1>{title}</h1>\n<ul>\n{items}\n</ul>"


# ---------------------------------------------------------------------------
# HTTP request handler
# ---------------------------------------------------------------------------

class WikiHandler(BaseHTTPRequestHandler):
    config: ServerConfig  # injected by run_server()

    def log_message(self, fmt, *args):  # suppress default verbose access log
        pass

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        url_path = urllib.parse.unquote(parsed.path).rstrip("/") or "/"

        # T004: path traversal guard
        if ".." in url_path.split("/"):
            self._text(400, "Bad request.")
            return

        # T004: whitelist router
        if url_path == "/":
            self._serve_root_md("index.md", "/")
        elif url_path == "/__mtime":
            self._serve_mtime()
        elif url_path in ("/log", "/log.md"):
            self._serve_root_md("log.md", url_path)
        elif url_path in ("/llm-wiki", "/llm-wiki.md"):
            self._serve_root_md("llm-wiki.md", url_path)
        elif url_path.startswith("/wiki"):
            self._serve_wiki(url_path)
        else:
            self._text(403, "Access denied.")

    # -- route handlers --

    def _serve_root_md(self, filename: str, url_path: str):
        fs_path = self.config.wiki_root / filename
        self._render(fs_path, url_path)

    def _serve_wiki(self, url_path: str):
        wiki_rel = url_path[5:].lstrip("/")  # strip leading /wiki
        wiki_dir = self.config.wiki_root / "wiki"

        if not wiki_rel:
            body = dir_listing_html(wiki_dir, "/wiki", "Wiki")
            nav = build_nav(url_path, self.config.wiki_root)
            self._html(200, page_shell("Wiki", body, nav, self.config))
            return

        candidate = wiki_dir / wiki_rel
        candidate_md = candidate if candidate.suffix == ".md" else wiki_dir / (wiki_rel + ".md")

        if candidate_md.is_file():
            self._render(candidate_md, url_path)
        elif candidate.is_dir():
            title = candidate.name.capitalize()
            body = dir_listing_html(candidate, url_path, title)
            nav = build_nav(url_path, self.config.wiki_root)
            self._html(200, page_shell(title, body, nav, self.config))
        else:
            self._text(404, f"Page not found: {url_path}")

    def _serve_mtime(self):
        root = self.config.wiki_root
        candidates = [root / "wiki", root / "index.md", root / "log.md", root / "llm-wiki.md"]
        max_mtime = 0.0
        for p in candidates:
            if p.is_file():
                max_mtime = max(max_mtime, os.path.getmtime(p))
            elif p.is_dir():
                for f in p.rglob("*.md"):
                    max_mtime = max(max_mtime, os.path.getmtime(f))
        payload = json.dumps({"mtime": max_mtime}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    # -- rendering --

    def _render(self, fs_path: Path, url_path: str):
        try:
            body, metadata = render_markdown(fs_path)
        except FileNotFoundError:
            self._text(404, f"Page not found: {url_path}")
            return
        except OverflowError:
            self._text(413, "File too large (> 5 MB).")
            return
        body = rewrite_md_links(body)
        title = metadata.get("title") or extract_title(body, fs_path.stem)
        meta_html = render_metadata(metadata)
        if meta_html:
            body = meta_html + body
        nav = build_nav(url_path, self.config.wiki_root)
        self._html(200, page_shell(title, body, nav, self.config))

    # -- response helpers --

    def _html(self, code: int, html: str):
        data = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _text(self, code: int, message: str):
        data = message.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


# ---------------------------------------------------------------------------
# Dev-mode: restart server process when this file changes
# ---------------------------------------------------------------------------

def _watch_source(script_path: str):
    import time
    mtime = os.path.getmtime(script_path)
    while True:
        time.sleep(1)
        try:
            new_mtime = os.path.getmtime(script_path)
        except OSError:
            continue
        if new_mtime != mtime:
            print(f"\nSource changed — restarting...", flush=True)
            os.execv(sys.executable, [sys.executable] + sys.argv)


# ---------------------------------------------------------------------------
# Server startup
# ---------------------------------------------------------------------------

def run_server(config: ServerConfig):
    WikiHandler.config = config
    try:
        server = HTTPServer(("", config.port), WikiHandler)
    except OSError as exc:
        if exc.errno == errno.EADDRINUSE:
            print(
                f"Error: port {config.port} is already in use. Choose another with --port.",
                file=sys.stderr,
            )
            sys.exit(1)
        raise
    print(f"Wiki server running at http://localhost:{config.port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="Local wiki server")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    parser.add_argument("--no-reload", action="store_true", help="Disable wiki live reload")
    parser.add_argument("--dev", action="store_true", help="Restart server when wiki_server.py changes")
    args = parser.parse_args()

    if args.dev:
        import threading
        t = threading.Thread(target=_watch_source, args=(os.path.abspath(__file__),), daemon=True)
        t.start()

    config = ServerConfig(
        port=args.port,
        live_reload=not args.no_reload,
        project_title=read_project_title(PROJECT_ROOT),
    )
    run_server(config)


if __name__ == "__main__":
    main()
