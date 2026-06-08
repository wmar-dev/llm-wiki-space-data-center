# Implementation Plan: Local Wiki Server

**Branch**: `003-local-wiki-server` | **Date**: 2026-06-07 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/003-local-wiki-server/spec.md`

## Summary

Build a single-file Python development server (`tools/wiki_server.py`) that renders the project's markdown wiki files as HTML and serves them at `http://localhost:8000`. The server whitelists the `wiki/` directory plus root-level wiki companion files, rewrites internal markdown links, and includes a lightweight JS polling mechanism for live reload on file changes. One-time dependency: `pip3 install markdown`.

## Technical Context

**Language/Version**: Python 3.8+ (pre-installed on macOS and most Linux distros; confirmed 3.9 on this machine)

**Primary Dependencies**: `markdown` (PyPI) — single external dependency for markdown-to-HTML conversion; stdlib `http.server` for the HTTP layer

**Storage**: N/A — read-only access to existing wiki markdown files on disk

**Testing**: Manual validation per `quickstart.md` scenarios; no automated test suite for a single-file dev utility

**Target Platform**: macOS + Linux (developer's local machine, localhost only)

**Project Type**: CLI dev utility / local tool

**Performance Goals**: Sub-100ms page load for any wiki page (files are small, single user)

**Constraints**: Single user; localhost only; must not expose project config, secrets, or spec files (FR-007)

**Scale/Scope**: ~50–100 markdown files, single concurrent user

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Verdict | Notes |
| --------- | ------- | ----- |
| I. Source Immutability | ✅ Pass | Server is read-only; never writes wiki files |
| II. Fact-Grounded Analysis | N/A | Tooling feature, not wiki content |
| III. Incremental Synthesis | N/A | Tooling feature |
| IV. Navigability | ✅ Supports | Server improves wiki navigability and internal link traversal |
| V. Human Direction | ✅ Pass | Human-requested tooling improvement; LLM builds on approval |
| VI. Adaptive Tooling | ✅ Aligned | This is precisely the CLI tool investment called for by Principle VI |
| VII. Token Economy | ✅ Strongly aligned | Browsing locally replaces reading files through the LLM; reduces token spend |

**Post-design re-check**: No violations. Design adds no new principles concerns.

## Project Structure

### Documentation (this feature)

```text
specs/003-local-wiki-server/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── http-api.md      # Phase 1 output
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (/speckit-tasks)
```

### Source Code (repository root)

```text
Makefile              ← new (make serve / make serve PORT=9000)
tools/
├── wiki_server.py    ← new (the entire implementation)
├── lint-scan.sh
├── pdf-extract.sh
├── search.sh
└── xref-check.sh
```

**Structure Decision**: Single-file utility added to the existing `tools/` directory. A new `Makefile` at the project root provides the `make serve` shortcut. No `src/`, `tests/`, or build system needed — this is a self-contained dev script.

## Complexity Tracking

No constitution violations to justify.
