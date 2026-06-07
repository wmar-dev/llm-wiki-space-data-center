# Tasks: Space Data Center Prospects Analysis Wiki

**Input**: Design documents from `specs/001-space-datacenter-analysis/`

**Prerequisites**: [plan.md](plan.md) · [spec.md](spec.md) · [data-model.md](data-model.md) · [contracts/](contracts/) · [research.md](research.md) · [quickstart.md](quickstart.md)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies on pending tasks)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths are included in each description

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish the required directory layout and seed files so all subsequent phases have a valid target to write to.

- [x] T001 Create directory structure at repository root per FR-022: `mkdir -p raw wiki/sources wiki/entities wiki/concepts wiki/comparisons wiki/synthesis wiki/adjacent wiki/meta .claude/skills tools`
- [x] T002 [P] Initialize `index.md` with header line (`# Index`) and a blank entries section with format reference: `- [Title](wiki/type/slug.md) — summary [status: current] [sources: N]`
- [x] T003 [P] Initialize `log.md` with header line (`# Log`) and format reference: `## [YYYY-MM-DD] <operation> | <title>`
- [x] T004 [P] Write `.claude/mcp.json` with Playwright MCP server configuration per research.md §1: command `npx`, args `["@playwright/mcp@latest"]`, mcpServers key `playwright`
- [x] T005 Write `CLAUDE.md` minimal scaffold with exactly these section headings per FR-008: `## Directory Structure`, `## Page Type Conventions`, `## Ingest Workflow`, `## Query Workflow`, `## Lint Workflow`, `## Schema Evolution Notes` — no prefilled content under any heading
- [x] T006 [P] Initialize `wiki/meta/evaluations.md` with header (`# Evaluations`), append-only warning comment, and format reference block per data-model.md §Meta Artifact

**Checkpoint**: All directories and seed files exist. Proceed to Foundational.

---

## Phase 2: Foundational (CLI Tools)

**Purpose**: Write the four CLI tools that the skills depend on. All four operate on different files and have no dependencies on each other — run in parallel.

**⚠️ CRITICAL**: Ingest, query, and lint skills all call these tools. Complete this phase before Phase 3.

- [x] T007 [P] Write `tools/pdf-extract.sh` — detect `pdftotext` (poppler) or fall back to `pdfplumber`; extract PDF text to stdout; save alongside original as `raw/<name>.txt`; exit 0 on success, 1 on failure with error to stderr. Per research.md §2 (FR-019)
- [x] T008 [P] Write `tools/search.sh` — ripgrep (`rg`) full-text search across `wiki/` returning matching file paths; usage: `bash tools/search.sh "<terms>"`; exit 0 when results found, 1 when none. Per research.md §5 (FR-009, SC-006)
- [x] T009 [P] Write `tools/xref-check.sh` — scan all `.md` files in `wiki/` for `[[...]]` cross-reference syntax; verify each referenced path exists as a file; print `BROKEN: <source> → <target>` per broken ref; exit 0 when clean, 1 when broken refs found. Per contracts/wiki-page-format.md (FR-007)
- [x] T010 [P] Write `tools/lint-scan.sh` — scan for three issue types: (a) pages in `wiki/` with no matching entry in `index.md` (orphaned), (b) wiki pages missing any of the 6 required frontmatter fields, (c) pages with `status: stale` or `status: contested`; output structured `ISSUE:<severity>:<type>:<path>` lines; exit 0 when clean, 1 when issues found. Per data-model.md §WikiPage (FR-007, FR-020)
- [x] T011 Make all four tools executable: `chmod +x tools/pdf-extract.sh tools/search.sh tools/xref-check.sh tools/lint-scan.sh`; run each against empty `wiki/` and verify exit 0 with no false positives

**Checkpoint**: All four tools exit cleanly on an empty wiki. User story implementation can now begin.

---

## Phase 3: User Story 1 — Source Ingest (Priority: P1) 🎯 MVP

**Goal**: A researcher can drop a source into `raw/` (or provide a URL), invoke `/ingest`, and receive a source summary page, updated `index.md`, a log entry, and updated concept/entity pages — all within a single session.

**Independent Test**: Run Scenario 1 from [quickstart.md](quickstart.md) — create `raw/test-source-001.md`, invoke `/ingest`, verify 6 output checks pass (source summary, index entry, log entry, concept page, micro evaluation, valid frontmatter).

### Implementation for User Story 1

- [x] T012 [US1] Write `.claude/skills/ingest.md` — complete ingest skill following all 11 processing steps in [contracts/skill-ingest.md](contracts/skill-ingest.md):
  - Step 1: Source acquisition — file path check OR Playwright MCP fetch + save to `raw/` + fetch log entry (FR-001, FR-011)
  - Step 2: Duplicate detection — check `index.md` for same filename or URL; on match log `re-ingest`, set dependent pages `status: stale` (FR-012)
  - Step 3: Chunking — estimate length; if oversized split into ≤3000-word chunks, process sequentially, merge summaries; set `processing_status: chunked` (FR-014)
  - Step 4: Credibility assessment — determine `source_type` from title/URL/content; record in source metadata (FR-017 prereq)
  - Step 5: Discuss key takeaways with researcher
  - Step 6: Write wiki pages — read `index.md` first; read ≤5 related pages (SC-006); write `wiki/sources/<slug>.md`; update/create affected `wiki/entities/*.md` and `wiki/concepts/*.md`; file out-of-domain sources to `wiki/adjacent/<slug>.md` with relevance note (FR-010, FR-013)
  - Step 7: Contradiction check — compare new claims against `current`/`contested` pages; note contradictions in both pages + log; set `status: contested` when FR-017 threshold met (FR-004, FR-017)
  - Step 8: Update `index.md` — add/update entry for every written/modified page (FR-002)
  - Step 9: Update `log.md` — append `## [YYYY-MM-DD] ingest | <source title>` (FR-003)
  - Step 10: Micro self-evaluation — append ≤3 observations to `wiki/meta/evaluations.md` (FR-021)
  - Step 11: Set `processing_status: processed` (or `chunked`); PDF sources invoke `tools/pdf-extract.sh` before Step 1 text processing (FR-019)
  - Include error outputs: Playwright failure → log `fetch-failed`, notify researcher; PDF failure → log failure, prompt for text version; mid-ingest failure → set `processing_status: failed`
  - Token budget annotation: ≤8 file reads per ingest (FR-009)

- [x] T013 [US1] Validate Scenario 1 from quickstart.md — create `raw/test-source-001.md`, invoke `/ingest raw/test-source-001.md`, verify all 6 checks pass; then validate Scenario 5 (re-ingest) — re-run `/ingest raw/test-source-001.md` and verify `status: stale` and `ingest_count: 2`

**Checkpoint**: User Story 1 fully functional. `/ingest` produces wiki pages, index entries, log entries, and self-evaluation records.

---

## Phase 4: User Story 2 — Wiki Query (Priority: P2)

**Goal**: A researcher can ask a natural language question, receive a cited answer synthesized from relevant wiki pages, and optionally file the answer back as a new wiki page.

**Independent Test**: After running T013, invoke `/query What are the thermal constraints for space data centers?`, verify the answer cites `[[wiki/sources/test-source-001.md]]`, reads ≤5 pages, and offers to file back. Accept file-back and verify new page in `wiki/synthesis/` + `index.md` entry.

### Implementation for User Story 2

- [x] T014 [US2] Write `.claude/skills/query.md` — complete query skill following all 7 processing steps in [contracts/skill-query.md](contracts/skill-query.md):
  - Step 1: Read `index.md`; identify ≤5 most relevant entries (FR-009, SC-006); if >5 candidates, run `tools/search.sh "<terms>"` first to pre-filter
  - Step 2: Read ≤5 selected pages; if more needed, invoke `tools/search.sh` and read top 5 results (SC-006)
  - Step 3: Gap detection — if no relevant pages found, use Playwright MCP to fetch a relevant source; run ingest skill; re-run query (FR-015, FR-016)
  - Step 4: Synthesis — answer with inline citations (`[[wiki/...]]`); label inferences `Inference:`; label unanswerable gaps `Open question:` (FR-005)
  - Step 5: Output format selection — prose (default), comparison table (when "compare"/"vs" in question), Marp slide deck (when researcher requests presentation), matplotlib Python script (when data visualization requested) (FR-006)
  - Step 6: File-back prompt — offer to write answer as `wiki/synthesis/<slug>.md` or `wiki/comparisons/<slug>.md`; update `index.md` if confirmed (FR-006)
  - Step 7: Append `## [YYYY-MM-DD] query | <question summary>` to `log.md` (FR-003)
  - Token budget annotation: ≤7 file reads per query

- [x] T015 [US2] Validate Scenario 2 from quickstart.md — run query against ingested source, verify cited answer with `[[...]]` inline refs, verify ≤5 pages read, accept file-back, verify new wiki page has valid frontmatter and `index.md` entry; run Scenario 3 (URL ingest) — provide Wikipedia URL to `/ingest`, verify `origin_url` recorded and source summary created

**Checkpoint**: User Story 2 fully functional. `/query` synthesizes cited answers, files back to wiki, and logs operations.

---

## Phase 5: User Story 3 — Wiki Lint (Priority: P3)

**Goal**: A researcher can run `/lint` to health-check the wiki and receive a structured report of errors, warnings, and info items — with proposed fixes for error-severity issues.

**Independent Test**: After running T013 and T015, invoke `/lint`, verify structured report produced (0 errors on clean wiki), log entry appended, macro self-evaluation triggered if ≥10 ingest log entries.

### Implementation for User Story 3

- [x] T016 [US3] Write `.claude/skills/lint.md` — complete lint skill following all 8 processing steps in [contracts/skill-lint.md](contracts/skill-lint.md):
  - Step 1: Run `tools/lint-scan.sh`; parse `ISSUE:<severity>:<type>:<path>` output lines (FR-007)
  - Step 2: Run `tools/xref-check.sh`; parse `BROKEN: <source> → <target>` output lines (FR-007)
  - Step 3: Classify issues by severity (Error / Warning / Info) with examples from contracts/skill-lint.md
  - Step 4: Generate lint report — issue count table + per-issue list with file paths (FR-007, FR-020)
  - Step 5: Propose fixes for Error-severity issues (orphan → add index entry or delete; broken ref → remove or create stub; missing frontmatter → add defaults)
  - Step 6: Apply fixes if researcher confirms; update affected wiki pages and `index.md`
  - Step 7: Macro self-evaluation trigger — `grep -c "ingest" log.md`; if count is multiple of 10, append macro evaluation to `wiki/meta/evaluations.md` (FR-021)
  - Step 8: Append `## [YYYY-MM-DD] lint | <N errors, N warnings, N info>` to `log.md` (FR-003)
  - Token budget annotation: ≤3 file reads for a clean wiki; proportional to error count when applying fixes

- [x] T017 [US3] Validate Scenario 4 from quickstart.md — run `/lint` on wiki with test pages, verify zero-error report, verify log entry; then validate Scenario 6 (PDF ingest) — place test PDF in `raw/`, run `/ingest`, verify `raw/<name>.txt` created and wiki page produced

**Checkpoint**: All three user stories fully functional and independently validated.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: End-to-end validation of the full system across all quickstart scenarios. Confirm all FR coverage.

- [x] T018 [P] Validate Scenario 7 from quickstart.md — run `bash tools/search.sh "radiative cooling"` and `bash tools/xref-check.sh` on a populated wiki; verify sub-2s search return and grep-parseable output
- [x] T019 [P] Verify `CLAUDE.md` scaffold headings are intact after first ingest session; verify all 6 required headings present (§Directory Structure through §Schema Evolution Notes)
- [x] T020 [P] Verify `index.md` entries match data-model.md §Index Entry format: `- [Title](wiki/type/slug.md) — summary [status: current] [sources: N]`; verify `log.md` entries match §Log Entry format: `## [YYYY-MM-DD] <operation> | <title>`
- [x] T021 [P] Verify wiki page frontmatter on all created pages: all 6 required fields present (`title`, `type`, `sources`, `status`, `created`, `last_updated`); `type` is one of the 7 valid values per contracts/wiki-page-format.md
- [x] T022 Run final lint pass (`/lint`) after all validation scenarios complete; confirm zero Error-severity findings; confirm `wiki/meta/evaluations.md` contains at least one micro evaluation entry

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 completion — BLOCKS all user stories
- **Phase 3 (US1 Ingest)**: Depends on Phase 2 — first MVP deliverable; must complete before US2/US3
- **Phase 4 (US2 Query)**: Depends on Phase 2; requires at least one ingested source (T013) for validation
- **Phase 5 (US3 Lint)**: Depends on Phase 2; requires ingested sources and at least one query result for meaningful test
- **Phase 6 (Polish)**: Depends on Phases 3–5 completion

### User Story Dependencies

- **US1 (P1)**: Can start after Phase 2 — no dependency on US2 or US3
- **US2 (P2)**: Can start after Phase 2; T015 validation runs after T013 (requires ingested source)
- **US3 (P3)**: Can start after Phase 2; T017 validation runs after T013 and T015 (requires sources and query results)

### Within Each User Story

- Skill file (T012, T014, T016) MUST be written before its validation task (T013, T015, T017)
- Foundational tools MUST be complete before skill files reference them

### Parallel Opportunities

- T002, T003, T004, T006 in Phase 1 can all run in parallel after T001
- T007, T008, T009, T010 in Phase 2 can all run in parallel (different files)
- T018, T019, T020, T021 in Phase 6 can all run in parallel

---

## Parallel Example: Phase 2 (All Four Tools)

```text
Launch all Phase 2 tool tasks in parallel after T011:
  Task T007: "Write tools/pdf-extract.sh per research.md §2"
  Task T008: "Write tools/search.sh per research.md §5"
  Task T009: "Write tools/xref-check.sh per contracts/wiki-page-format.md"
  Task T010: "Write tools/lint-scan.sh per data-model.md §WikiPage"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T006)
2. Complete Phase 2: Foundational tools (T007–T011)
3. Complete Phase 3: Ingest skill (T012–T013)
4. **STOP and VALIDATE**: Run Scenario 1 from quickstart.md
5. A working `/ingest` command is the MVP — the wiki can grow immediately

### Incremental Delivery

1. Setup + Foundational → scaffold ready
2. Add US1 (ingest) → validate independently → wiki can grow
3. Add US2 (query) → validate independently → analytical insights available
4. Add US3 (lint) → validate independently → wiki quality maintained
5. Polish → full system validated end-to-end

### Single-Researcher Context

This is a solo tool — no parallelism needed across user stories. Sequential P1 → P2 → P3
is the correct delivery order. The parallel markers [P] within phases indicate work
that can be farmed to concurrent agent calls or done in any order within that phase.

---

## Notes

- [P] tasks operate on different files with no pending dependencies
- [US1/2/3] labels map tasks to user stories for traceability
- All skill files are Markdown behavioral specifications, not code — write them as
  detailed instruction documents following the corresponding contract file
- Commit after T006 (scaffold ready), T011 (tools ready), T013 (US1 validated),
  T015 (US2 validated), T017 (US3 validated)
- quickstart.md is the acceptance test suite — every Phase 6 task references it
- SC-006 (≤5 pages per query) is enforced by the skill files, not by code
