# Research: Local Wiki Server

**Phase 0 output for**: `003-local-wiki-server`
**Date**: 2026-06-07

## Decision 1: Server Technology

**Decision**: Python 3 stdlib (`http.server`) + `markdown` PyPI package.

**Rationale**:
- Python 3 is pre-installed on both macOS (3.9 confirmed) and most Linux distros.
- `http.server` provides the HTTP layer with zero installation.
- `markdown` (pip install) converts CommonMark/GH-flavored markdown to HTML with a single call.
- Single-file implementation (~100 lines) with one external dependency keeps the tool auditable and easy to remove.

**Alternatives considered**:
- **`grip`** (pip install grip): renders GitHub-flavored markdown exactly but calls the GitHub API, requires a token for frequent use, and is offline-hostile. Rejected.
- **`npx serve` + browser markdown extension**: requires Node.js/npm and a browser extension per user. Two moving parts, not self-contained. Rejected.
- **`mdbook`** (Rust): excellent rendered output but requires Rust toolchain install and a `book.toml` config rework. Too heavy for a dev utility. Rejected.
- **`ruby -run -e httpd`** + Markdown gem: Ruby is present on macOS but not guaranteed on Linux. Rejected for cross-platform consistency.

---

## Decision 2: Content Root and Access Control

**Decision**: Serve the entire project root directory but whitelist paths for wiki content. Only the following paths return rendered HTML:
- `/` → renders `index.md`
- `/wiki/**` → renders files under `wiki/`
- `/log.md`, `/llm-wiki.md` → renders root-level wiki companion files

All other paths (e.g., `/specs/`, `/.specify/`, `/raw/`, `/tools/`) return HTTP 403.

**Rationale**: The spec requires FR-007 (no exposure of project source/config). A whitelist is simpler and safer than a blacklist — new directories added to the repo are blocked by default.

**Alternatives considered**:
- Serving only `wiki/` subtree: breaks `index.md` and `log.md` which live at root. Rejected.
- Serving entire project root without access control: violates FR-007 and would expose `.specify/` (contains API config). Rejected.

---

## Decision 3: Link Rewriting

**Decision**: Rewrite `.md` href attributes to strip the `.md` extension before serving the HTML. The server resolves paths both with and without the `.md` suffix.

**Rationale**: Wiki pages cross-link using relative markdown paths (`[page](../concepts/foo.md)`). The browser will GET `/wiki/concepts/foo.md`; the server must recognize this and serve the rendered HTML.

---

## Decision 4: Live Reload (P3)

**Decision**: JavaScript polling against a `/__mtime` endpoint that returns the most recent modification timestamp across the served wiki files. Browser reloads if timestamp changes.

**Rationale**:
- No extra Python dependencies (no `watchdog`, no `inotify`).
- Works on both macOS (kqueue) and Linux (inotify) without platform-specific code.
- Polling interval of 2 seconds is imperceptible for a writing workflow.

**Alternatives considered**:
- `watchdog` (pip install) + WebSocket: more responsive but adds a second dependency and more code. Rejected for simplicity.
- `server-sent events`: cleaner than polling but requires keeping connections open, complicating the single-threaded server model. Rejected.

---

## Decision 5: HTML Rendering Style

**Decision**: Wrap rendered HTML in a minimal page shell (DOCTYPE, UTF-8 charset, GitHub-inspired CSS embedded inline or via CDN-free stylesheet). Include a sidebar listing top-level wiki sections derived from the directory listing.

**Rationale**: Bare HTML without any styling is hard to read. A small inline CSS block (~50 lines) makes the output comparable to GitHub's markdown view without external network calls. Keeps the tool offline-capable.
