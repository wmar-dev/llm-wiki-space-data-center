# Feature Specification: Local Wiki Server

**Feature Branch**: `003-local-wiki-server`

**Created**: 2026-06-07

**Status**: Draft

**Input**: User description: "Make a local server, so i can view the wiki pages without having to push to github."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Start Server and Browse Wiki (Priority: P1)

The researcher runs a single command to start a local server, then opens a browser to read wiki pages rendered as HTML. All internal wiki links work, allowing navigation between pages just as they would on GitHub.

**Why this priority**: This is the core value — eliminating the push-to-view cycle that breaks the research flow.

**Independent Test**: Start the server, open the browser index page, click a link to a wiki page, and confirm the page renders with readable content.

**Acceptance Scenarios**:

1. **Given** the wiki directory contains markdown pages, **When** the researcher runs the start command, **Then** a local server starts and a URL is printed to the terminal.
2. **Given** the server is running, **When** the researcher opens the URL in a browser, **Then** the wiki index page renders as readable HTML.
3. **Given** the index page is open, **When** the researcher clicks a link to another wiki page, **Then** that page loads correctly in the browser.

---

### User Story 2 - Stop Server Cleanly (Priority: P2)

The researcher can stop the server when done without leaving background processes running.

**Why this priority**: A server that's hard to stop or leaves zombie processes is a maintenance burden on a developer's machine.

**Independent Test**: Start the server, then stop it; confirm no process is still listening on the port.

**Acceptance Scenarios**:

1. **Given** the server is running, **When** the researcher presses Ctrl+C, **Then** the server stops cleanly with no lingering processes.

---

### User Story 3 - Live Reload on File Change (Priority: P3)

When the researcher saves a wiki page, the browser automatically refreshes to show the updated content without restarting the server.

**Why this priority**: Useful during active ingest/edit sessions, but the wiki is primarily read-only tooling, so this is an enhancement rather than a blocker.

**Independent Test**: Edit a wiki markdown file while the server is running; confirm the browser refreshes and shows the change within a few seconds.

**Acceptance Scenarios**:

1. **Given** the server is running and a wiki page is open in the browser, **When** the markdown file is saved, **Then** the browser reflects the updated content within 5 seconds without manual refresh.

---

### Edge Cases

- What happens when the server port is already in use by another process?
- How does the system handle wiki pages that reference images or other binary assets?
- What happens if a link points to a wiki page that does not exist?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST serve wiki markdown pages as readable HTML when accessed via a local browser.
- **FR-002**: System MUST start with a single command from the project root.
- **FR-003**: Internal wiki links (relative markdown links) MUST navigate correctly between pages.
- **FR-004**: The server MUST print its local URL to the terminal on startup.
- **FR-005**: The server MUST stop cleanly when the user interrupts it (Ctrl+C).
- **FR-006**: If the requested port is already occupied, the server MUST report a clear error rather than silently failing.
- **FR-007**: The server MUST serve only the `wiki/` directory — it MUST NOT expose project source files, secrets, or configuration.

### Key Entities

- **Wiki Page**: A markdown file under `wiki/`, rendered to HTML for browser display.
- **Index**: The root entry point (`wiki/index.md` or directory listing) shown when the researcher opens the server URL.
- **Server Process**: The local process that handles HTTP requests and renders markdown; runs only during active use.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The researcher can view any wiki page in a browser within 10 seconds of running the start command.
- **SC-002**: All internal wiki cross-reference links resolve correctly (zero broken internal links during a browsing session).
- **SC-003**: The server is started and stopped with a single command each — no multi-step setup.
- **SC-004**: Zero project source files or configuration are accessible via the server URL.

## Assumptions

- This server is for local, single-user use only — no authentication or multi-user access is needed.
- The server must work on both macOS and Linux; Windows support is not required.
- The `wiki/` directory is the sole content root; no content lives outside it.
- Performance expectations are light: the researcher is the only user, and pages are small markdown files.
- A package or tool available without heavy installation is preferred (e.g., something invocable via a short npm/npx/python command or a small script).
- Browser support is limited to a modern desktop browser (Safari, Chrome, Firefox) — no mobile or IE compatibility needed.
