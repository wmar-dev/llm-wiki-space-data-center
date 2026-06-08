# Quickstart Validation Guide: Local Wiki Server

**Phase 1 output for**: `003-local-wiki-server`
**Date**: 2026-06-07

This guide proves the feature works end-to-end. Run each scenario after implementation.

---

## Prerequisites

- Python 3.8 or later installed (`python3 --version`)
- One-time dependency install: `pip3 install markdown`
- A terminal open at the project root

---

## Scenario 1: Server Starts and Index Loads (P1 core)

```bash
make serve
# or with a custom port:
make serve PORT=9000
# or directly:
python3 tools/wiki_server.py
```

**Expected terminal output**:

```text
Wiki server running at http://localhost:8000
Press Ctrl+C to stop.
```

1. Open `http://localhost:8000` in a browser.
2. **Expected**: The page renders the content of `index.md` as formatted HTML — headings, links, and text are all visible (not raw markdown syntax).

---

## Scenario 2: Internal Links Navigate Correctly (FR-003)

1. From the index page, click any link pointing to a wiki page (e.g., a concept or synthesis page).
2. **Expected**: The linked page loads and renders correctly. The browser URL updates to the page path. No 404 errors appear.
3. From that page, click a cross-reference link to a different wiki page.
4. **Expected**: Navigation continues to work — links chain without breaking.

---

## Scenario 3: Access Control Blocks Non-Wiki Paths (FR-007)

1. With the server running, open `http://localhost:8000/specs/003-local-wiki-server/spec.md`.
2. **Expected**: Browser shows HTTP 403 Forbidden — the spec file is not served.
3. Open `http://localhost:8000/.specify/feature.json`.
4. **Expected**: HTTP 403 Forbidden.

---

## Scenario 4: Port Conflict Reporting (FR-006)

1. Start the server: `python3 tools/wiki_server.py`
2. Without stopping it, open a second terminal and run: `python3 tools/wiki_server.py`
3. **Expected**: The second invocation prints a clear error message (e.g., `Error: port 8000 is already in use`) and exits immediately. It does not silently hang.

---

## Scenario 5: Clean Shutdown (FR-005)

1. With the server running, press `Ctrl+C` in the terminal.
2. **Expected**: The server prints a shutdown message and exits.
3. Run: `lsof -i :8000`
4. **Expected**: No process is listening on port 8000.

---

## Scenario 6: Live Reload on File Edit (P3)

1. Start the server.
2. Open a wiki page in the browser.
3. In an editor, append a line to that markdown file and save.
4. **Expected**: Within 3 seconds, the browser automatically refreshes and shows the new content — without pressing F5.

---

## Scenario 7: Linux Compatibility

Run scenarios 1–5 on a Linux machine (or WSL2 / Docker container).

**Expected**: All scenarios pass identically. No macOS-specific behaviour is required.

---

## References

- Access control rules: see [data-model.md](data-model.md#access-control-rules)
- HTTP interface: see [contracts/http-api.md](contracts/http-api.md)
- Research decisions: see [research.md](research.md)
