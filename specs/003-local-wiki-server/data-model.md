# Data Model: Local Wiki Server

**Phase 1 output for**: `003-local-wiki-server`
**Date**: 2026-06-07

## Overview

The local wiki server is stateless and read-only. There is no persistent storage beyond the existing markdown files on disk. The "data model" describes the in-memory representations used during a single HTTP request.

---

## Entities

### WikiPage

Represents a single rendered page served to the browser.

| Field | Type | Description |
|-------|------|-------------|
| `fs_path` | `Path` | Absolute filesystem path to the `.md` source file |
| `url_path` | `str` | URL path used by the browser (e.g., `/wiki/concepts/foo`) |
| `raw_markdown` | `str` | Raw markdown content read from disk |
| `html_body` | `str` | Rendered HTML fragment (markdown converted) |
| `title` | `str` | Page title extracted from first H1, or filename if absent |
| `last_modified` | `float` | File modification timestamp (used for live-reload mtime) |

**Validation rules**:
- `fs_path` must exist and be readable; returns 404 if missing.
- `url_path` must match the whitelist; returns 403 otherwise.
- Files larger than 5 MB are rejected with a 413 response.

**State transitions**: None — each request creates a fresh `WikiPage` from disk; no caching layer in v1.

---

### NavigationEntry

A link shown in the sidebar or breadcrumb.

| Field | Type | Description |
|-------|------|-------------|
| `label` | `str` | Display text (directory name or page title) |
| `url_path` | `str` | Relative URL the link points to |
| `is_active` | `bool` | True when this entry matches the current page path |
| `depth` | `int` | Nesting level (0 = top-level section, 1 = page within section) |

---

### ServerConfig

Runtime configuration resolved at startup (not persisted).

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `port` | `int` | `8000` | TCP port to listen on |
| `wiki_root` | `Path` | project root | Filesystem root for content resolution |
| `live_reload` | `bool` | `True` | Whether to inject the JS polling snippet |
| `poll_interval_ms` | `int` | `2000` | Browser polling interval for live reload |

---

## Access Control Rules

The whitelist below is evaluated in order. First match wins.

| Pattern | Action |
|---------|--------|
| `/` | Serve `index.md` |
| `/wiki/**` | Serve matching file under `wiki/` |
| `/log.md` | Serve `log.md` |
| `/llm-wiki.md` | Serve `llm-wiki.md` |
| `/__mtime` | Return JSON `{"mtime": <float>}` (live-reload probe) |
| `/**` | HTTP 403 Forbidden |

---

## Link Rewriting Rules

Applied to `href` attributes in rendered HTML before the response is sent.

| Input href | Rewritten href |
|------------|----------------|
| `../concepts/foo.md` | `../concepts/foo` |
| `./bar.md` | `./bar` |
| `https://...` | unchanged |
| `#anchor` | unchanged |
