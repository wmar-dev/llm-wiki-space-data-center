# Implementation Plan: Space Data Center Prospects Analysis Wiki

**Branch**: `001-space-datacenter-analysis` | **Date**: 2026-06-07 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-space-datacenter-analysis/spec.md`

## Summary

Build a Claude Code-native LLM Wiki system for analyzing the prospects of space-based
data centers. Deliverables: a required directory layout (`raw/`, `wiki/` subtree,
`wiki/meta/`), append-only `log.md` and content-catalog `index.md`, a minimal
`CLAUDE.md` scaffold, three Claude skills (ingest, query, lint), Bash CLI tools for
token-efficient bulk operations (search, cross-reference check, lint scanner), and
Playwright MCP configuration for web fetching and PDF extraction.

This is a Claude Code-native knowledge management system — no web server, no database,
no build pipeline. All artifacts are Git-tracked Markdown files plus Bash scripts and
Python helpers.

## Technical Context

**Language/Version**: Bash 5.x (CLI tools), Python 3.11+ (matplotlib chart generation),
Markdown (wiki pages, skills, schema)

**Primary Dependencies**:

- Claude Code (Sonnet 4.6) — LLM runtime for all wiki operations
- Playwright MCP — web page fetch and rendering (FR-011, FR-015, FR-016)
- Python 3 + matplotlib — chart generation for query outputs (FR-006)
- Marp CLI (`@marp-team/marp-cli`) — Markdown-to-slide conversion (FR-006)
- pdftotext (poppler-utils) — PDF-to-text extraction during ingest (FR-019)

**Storage**: Git-tracked flat Markdown files. No database or vector store required at
target scale (≤200 sources). `index.md` is the sole navigation artifact until scale
demands a search upgrade (see FR-009).

**Testing**: Manual validation via `quickstart.md` scenarios. Skill correctness verified
by running each skill against sample sources and inspecting wiki output.

**Target Platform**: macOS (darwin), Claude Code CLI, single-researcher local environment

**Project Type**: LLM knowledge management system — wiki directories + Claude skills +
Bash CLI tools

**Performance Goals**: SC-006: routine queries read `index.md` + ≤5 wiki pages.
Micro self-evaluation appended to `wiki/meta/evaluations.md` at every session end.

**Constraints**: Single researcher, local-only, offline-capable except for Playwright
web fetch. `index.md` sufficient at ≤200 source scale. Image-only PDFs out of scope.

**Scale/Scope**: Single user; up to ~200 sources, ~500 wiki pages at target scale.
Search tooling upgrade recommended beyond 200 sources (qmd or ripgrep index).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-checked after Phase 1 design.*

| Principle | Gate | Status |
| --------- | ---- | ------ |
| I. Source Immutability | `raw/` read-only; no FR modifies source files | ✅ Pass |
| II. Fact-Grounded Analysis | FR-005 requires citation labels; FR-017 credibility assessment | ✅ Pass |
| III. Incremental Synthesis | FR-001/002/012 compile once and refresh on re-ingest | ✅ Pass |
| IV. Navigability | FR-002 (index), FR-003 (log), FR-007 (lint orphan/gap detection) | ✅ Pass |
| V. Human Direction | Single researcher owns sourcing; all fetches logged per FR-011 | ✅ Pass |
| VI. Adaptive Tooling + Skills | FR-009 (tool proposals), FR-018 (3 skills), FR-019 (PDF) | ✅ Pass |
| VII. Token Economy | FR-009 index-first navigation; SC-006 ≤5 pages/query | ✅ Pass |
| Self-Evaluation | FR-021 (evaluations.md); micro/macro cadence per constitution | ✅ Pass |

No violations. No complexity tracking required.

*Post-Phase 1 re-check: all gates still pass — design introduces no new abstractions
or dependencies beyond what the spec authorizes.*

## Project Structure

### Documentation (this feature)

```text
specs/001-space-datacenter-analysis/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   ├── skill-ingest.md
│   ├── skill-query.md
│   ├── skill-lint.md
│   └── wiki-page-format.md
└── tasks.md             # Phase 2 output (/speckit-tasks)
```

### Source Code (repository root)

```text
raw/                          # Immutable source documents (researcher-provided or fetched)

wiki/
  sources/                    # One summary page per ingested source
  entities/                   # Named actors/artifacts (companies, orbital regimes, etc.)
  concepts/                   # Domain ideas (thermal management, radiation hardening, etc.)
  comparisons/                # Comparison tables and multi-source analyses
  synthesis/                  # Cross-cutting synthesis and filed query results
  adjacent/                   # Out-of-domain source pages
  meta/
    evaluations.md            # Append-only self-evaluation record

index.md                      # Content catalog (updated on every ingest)
log.md                        # Append-only operation log
CLAUDE.md                     # Minimal schema scaffold

.claude/
  skills/
    ingest.md                 # Claude skill: process a source into wiki pages
    query.md                  # Claude skill: search wiki, synthesize cited answer
    lint.md                   # Claude skill: health-check wiki for issues

tools/
  search.sh                   # Full-text search across wiki pages (token-efficient)
  xref-check.sh               # Cross-reference integrity checker
  pdf-extract.sh              # PDF-to-text extraction wrapper
  lint-scan.sh                # Orphan/stale/contested page scanner
```

**Structure Decision**: Single flat-file project. No src/tests hierarchy — all
"code" is Markdown skills and Bash/Python CLI tools. Wiki directories are the
primary runtime artifacts.

## Complexity Tracking

> No constitution violations to justify.
