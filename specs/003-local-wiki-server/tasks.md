---
description: "Task list for Local Wiki Server implementation"
---

# Tasks: Local Wiki Server

**Input**: Design documents from `specs/003-local-wiki-server/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/http-api.md, quickstart.md

**Tests**: Automated unit tests in `tools/test_wiki_server.py` (`uv run tools/test_wiki_server.py`) plus manual validation per `quickstart.md` scenarios.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files or non-overlapping code sections)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

## Path Conventions

Single-file utility at `tools/wiki_server.py`. Support files at project root (`Makefile`). Test file at `tools/test_wiki_server.py`. Dependencies declared inline in both scripts via `uv` script block.

---

## Phase 1: Setup

**Purpose**: Project initialization — files and dependencies that must exist before any code is written.

- [x] T001 [P] Create `Makefile` at project root with `serve` target (`uv run tools/wiki_server.py`) and `PORT` override (`make serve PORT=9000`)
- [x] T002 [P] Create `requirements.txt` at project root listing `markdown>=3.5`

**Checkpoint**: `make serve` target exists; `uv run tools/wiki_server.py --help` auto-installs the dependency and displays usage.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure inside `tools/wiki_server.py` that every user story depends on.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T003 Create `tools/wiki_server.py` scaffold: imports (`http.server`, `pathlib`, `markdown`, `argparse`), `ServerConfig` dataclass (port, wiki_root, live_reload, poll_interval_ms), and `--port` CLI arg parsing
- [x] T004 Implement whitelist-based request router in `tools/wiki_server.py`: routes `/`, `/wiki/**`, `/log.md`, `/llm-wiki.md`, `/__mtime` to their handlers; returns 403 for all other paths; returns 400 and rejects any path containing `../` (path traversal guard)
- [x] T005 [P] Implement `render_markdown(fs_path) -> str` function in `tools/wiki_server.py`: reads file, calls `markdown.markdown()`, returns HTML fragment; raises 404 if file missing, 413 if file > 5 MB
- [x] T006 [P] Implement `page_shell(title, body, nav_entries) -> str` function in `tools/wiki_server.py`: returns a full HTML document (DOCTYPE, UTF-8 charset, minimal inline CSS resembling GitHub markdown style, sidebar nav, body content)
- [x] T007 Implement `.md` link rewriting in `tools/wiki_server.py`: post-process rendered HTML to strip `.md` extension from all internal `href` attributes (regex substitution on `href="...*.md"`)

**Checkpoint**: Scaffold, router, renderer, page shell, and link rewriter all exist. Server is not yet startable.

---

## Phase 3: User Story 1 — Start Server and Browse Wiki (Priority: P1) 🎯 MVP

**Goal**: Researcher runs `make serve`, opens browser, reads wiki pages, and navigates via links.

**Independent Test**: Start server → open `http://localhost:8000` → index renders as HTML → click a wiki link → page loads.

### Implementation

- [x] T008 [US1] Implement `GET /` handler in `tools/wiki_server.py`: serves `index.md` from project root through `render_markdown` + `page_shell`
- [x] T009 [US1] Implement `GET /wiki/**` handler in `tools/wiki_server.py`: resolves `wiki/{url_path}.md` (accepts path with or without `.md` suffix), renders and serves via `render_markdown` + `page_shell`; falls through to directory listing if path is a directory
- [x] T010 [US1] [P] Implement `GET /log.md` handler in `tools/wiki_server.py`: renders and serves `log.md` from project root
- [x] T011 [US1] [P] Implement `GET /llm-wiki.md` handler in `tools/wiki_server.py`: renders and serves `llm-wiki.md` from project root
- [x] T012 [US1] Implement wiki directory listing in `tools/wiki_server.py`: when a `/wiki/**` path resolves to a directory, return an HTML page listing `.md` files within it as links
- [x] T013 [US1] Implement `build_nav(current_url_path) -> list[NavigationEntry]` in `tools/wiki_server.py`: scans top-level `wiki/` subdirectories and returns nav entries with `is_active` flag for the current path
- [x] T014 [US1] Implement server startup in `tools/wiki_server.py`: bind `HTTPServer` to configured port, print `Wiki server running at http://localhost:{PORT}` and `Press Ctrl+C to stop.` to stdout, enter serve loop
- [x] T015 [US1] Manual validation: run Scenarios 1 and 2 from `specs/003-local-wiki-server/quickstart.md`

**Checkpoint**: `make serve` works; index and wiki pages render; internal links navigate correctly.

---

## Phase 4: User Story 2 — Stop Server Cleanly (Priority: P2)

**Goal**: Ctrl+C stops the server; a duplicate start attempt prints a clear error.

**Independent Test**: Start server → Ctrl+C → server exits cleanly → no process on port 8000.

### Implementation

- [x] T016 [US2] Implement `KeyboardInterrupt` / `SIGINT` handler in `tools/wiki_server.py`: catch interrupt in serve loop, print `Shutting down.` to stdout, exit with code 0
- [x] T017 [US2] Implement port-conflict detection in `tools/wiki_server.py`: wrap `HTTPServer` bind in try/except for `OSError` with `errno.EADDRINUSE`; print `Error: port {PORT} is already in use. Choose another with --port.` to stderr and exit with code 1
- [x] T018 [US2] Manual validation: run Scenarios 4 and 5 from `specs/003-local-wiki-server/quickstart.md`

**Checkpoint**: Ctrl+C exits cleanly; duplicate start prints a readable error.

---

## Phase 5: User Story 3 — Live Reload on File Change (Priority: P3)

**Goal**: Saving a wiki page causes the browser to auto-refresh within 3 seconds.

**Independent Test**: Start server → open page → edit `.md` file → browser reloads automatically.

### Implementation

- [x] T019 [US3] Implement `GET /__mtime` handler in `tools/wiki_server.py`: walks the served wiki file tree, finds the maximum `os.path.getmtime()` across all `.md` files, returns `{"mtime": <float>}` as `application/json`
- [x] T020 [US3] Inject JS live-reload snippet into `page_shell()` in `tools/wiki_server.py`: `setInterval` polling `/__mtime` every `poll_interval_ms` ms; stores initial mtime on load; triggers `location.reload()` when mtime increases; controlled by `ServerConfig.live_reload` flag
- [ ] T021 [US3] Manual validation: run Scenario 6 from `specs/003-local-wiki-server/quickstart.md`

**Checkpoint**: Browser refreshes automatically when a wiki file is saved.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final hardening and full validation across all stories.

- [ ] T022 [P] Manual validation: run Scenario 3 (access control — spec/config files return 403) from `specs/003-local-wiki-server/quickstart.md`
- [ ] T023 [P] Manual validation: run Scenario 7 (Linux compatibility) from `specs/003-local-wiki-server/quickstart.md`

**Checkpoint**: All 7 quickstart scenarios pass.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately; T001 and T002 run in parallel
- **Foundational (Phase 2)**: Depends on Phase 1 — blocks all user stories
  - T003 first (scaffold), then T004–T007 in sequence (T005 and T006 can run in parallel)
- **User Stories (Phases 3–5)**: All depend on Foundational completion
  - US1 (P1) first — core browsing is a prerequisite for meaningful testing of US2 and US3
  - US2 (P2) and US3 (P3) can start after US1 is complete; they are independent of each other
- **Polish (Phase 6)**: After all desired user stories complete

### User Story Dependencies

- **US1 (P1)**: After Foundational — no story dependencies
- **US2 (P2)**: After US1 (server must be running to validate shutdown)
- **US3 (P3)**: After US1 (needs a working page to observe live reload)

### Within Each User Story

- Handlers (T008–T012) can start in parallel once T003–T007 are done
- `build_nav` (T013) depends on T006 (page shell must exist to wire nav in)
- Server startup (T014) depends on all handlers existing
- Validation tasks (T015, T018, T021, T022, T023) always last in their phase

---

## Parallel Execution Examples

### Phase 1

```bash
# Both can run simultaneously:
Task T001: Create Makefile
Task T002: Create requirements.txt
```

### Phase 2

```bash
# After T003 scaffold is done:
Task T005: render_markdown() function
Task T006: page_shell() function
```

### Phase 3 (US1)

```bash
# After T007 link rewriting is done:
Task T010: GET /log.md handler
Task T011: GET /llm-wiki.md handler
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Run Scenarios 1–2 from quickstart.md
5. Run `make serve` — wiki is browseable locally

### Incremental Delivery

1. Setup + Foundational → scaffold ready
2. User Story 1 → wiki browseable (MVP — this alone solves the stated problem)
3. User Story 2 → clean shutdown + port error reporting
4. User Story 3 → live reload on edit
5. Polish → full quickstart validation

---

## Notes

- All implementation is in one file: `tools/wiki_server.py`
- [P] marks tasks that touch different functions/sections with no shared state — safe to parallelize
- No automated tests — validation is manual per quickstart.md
- Commit after each phase checkpoint
- Stop at the Phase 3 checkpoint for an immediately usable MVP
