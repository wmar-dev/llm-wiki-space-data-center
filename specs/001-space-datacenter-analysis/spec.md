# Feature Specification: Space Data Center Prospects Analysis Wiki

**Feature Branch**: `001-space-datacenter-analysis`

**Created**: 2026-06-07

**Status**: Draft

**Input**: User description: "Read @llm-wiki.md and implement a system to help analyze the prospects of data centers in space."

## Clarifications

### Session 2026-06-07

- Q: Is the LLM allowed to actively fetch web sources, or does it only process researcher-provided documents? → A: LLM can fetch and use Playwright MCP (web fetch is in scope; fetched pages saved to `raw/` as immutable sources and logged).

### Session 2026-06-07 (continued)

- Q: How should the system handle a source too large to process in one context window pass? → A: Split into chunks, process sequentially, produce one unified summary page noting the split.
- Q: What should happen when a query cannot be answered from existing wiki content? → A: Use Playwright MCP to fetch a relevant source, ingest it into the wiki, then answer with citations.
- Q: What should the system do when Playwright MCP cannot render or fetch a URL? → A: Retry once, then fall back to basic HTTP (no JS rendering); log the result either way.
- Q: How should a concept page represent a claim when three or more sources disagree? → A: Reason about the credibility of each source (e.g., peer-reviewed paper vs. industry report vs. blog), weight positions accordingly, document all views with credibility assessments and citations, and mark the page "Contested."
- Q: Should the implementation ship a starter CLAUDE.md schema or emerge through use? → A: Minimal scaffold — CLAUDE.md with section headings but no prefilled content; conventions fill in organically through the first ingest sessions.

### Session 2026-06-07 (third pass)

- Q: Should the implementation deliver initial Claude skills for the core wiki operations? → A: Yes — deliver skills for all three core operations: ingest, query, and lint.

### Session 2026-06-07 (fourth pass)

- Q: Self-evaluation user story and FR — add to spec or defer? → A: Defer to planning; planner derives evaluation tasks from the constitution directly.
- Q: What are the valid lifecycle states for a Source's processing status? → A: unprocessed → processing → processed | failed | chunked.
- Q: Should `wiki/meta/` be explicitly required as a directory for system artifacts? → A: Yes — add as a required directory; `evaluations.md` is a mandatory artifact within it.
- Q: Should the spec include an explicit top-level directory structure requirement? → A: Yes — enumerate the full required layout so the planner has a single source of truth for all paths.
- Q: Should wiki pages carry a status field? → A: Yes — optional YAML frontmatter status with values: draft | current | stale | contested.
- Q: How should PDF sources be handled — system converts or researcher pre-converts? → A: System converts PDFs automatically during ingest using available tools (MCP or CLI).
- Q: Should there be an explicit success criterion for token-efficient operation? → A: Yes — routine queries MUST read `index.md` plus no more than 5 wiki pages per operation; any operation requiring more triggers a CLI/MCP tool proposal.
- Q: What should the system do when a source that was already ingested is submitted again? → A: Accept as an update — note the re-ingest in `log.md` and refresh all affected wiki pages.
- Q: What should happen when a source has no meaningful relevance to space data centers? → A: Accept it, file under `wiki/adjacent/` with a relevance note explaining its adjacency value.
- Q: Which output formats should query answers support in v1? → A: All formats from llm-wiki.md — prose markdown pages, comparison tables, Marp slide decks, and matplotlib charts.
- Q: Who is the intended user of this wiki? → A: Single researcher only — personal tool, no access control or concurrent ingest coordination required.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest a Source on Space Data Centers (Priority: P1)

The researcher drops a source document (article, paper, report) into the raw sources
collection and asks the system to process it. The LLM reads the source, discusses key
takeaways, then writes or updates wiki pages covering relevant entities (companies,
satellites, orbital regimes, power sources, cooling technologies, launch providers) and
concepts (latency, radiation hardening, thermal management, regulatory environment).
The index and log are updated.

**Why this priority**: Without ingest, the wiki cannot grow. This is the foundational
operation that every other story depends on.

**Independent Test**: Can be fully tested by adding a single source document and
verifying that a summary page, updated index entry, and log entry all appear in the
wiki directory.

**Acceptance Scenarios**:

1. **Given** a new article on orbital data center cooling is dropped into `raw/`,
   **When** the researcher says "ingest this source",
   **Then** a summary page appears in `wiki/sources/`, the index is updated with a
   one-line entry, affected concept pages (cooling, thermal management) are updated,
   and a timestamped log entry is appended.

2. **Given** the new source contradicts a claim in an existing wiki page,
   **When** ingest completes,
   **Then** the contradiction is noted in both the affected page and the log before
   the session closes.

---

### User Story 2 - Query the Wiki for Analytical Insight (Priority: P2)

The researcher asks a question about space data center prospects (e.g., "What are the
most promising orbital regimes for low-latency edge computing?" or "How does radiation
exposure affect hardware longevity in LEO vs GEO?"). The system reads the index,
retrieves relevant pages, and synthesizes a cited answer. If the answer constitutes
reusable analysis, it is filed back into the wiki.

**Why this priority**: Query is the primary read operation. It transforms accumulated
sources into actionable insight, which is the project's core value proposition.

**Independent Test**: Can be tested independently after at least one source is ingested:
pose a question answerable from that source and verify the response cites specific wiki
pages and is filed back if substantive.

**Acceptance Scenarios**:

1. **Given** several sources on power generation in orbit have been ingested,
   **When** the researcher asks "What are the main power constraints for space-based
   data centers?",
   **Then** the answer cites at least one specific wiki page, distinguishes factual
   claims from inferences, and offers to file the synthesis as a new wiki page.

2. **Given** the query produces a comparison table of orbital regimes,
   **When** the researcher confirms it is worth keeping,
   **Then** the table is filed as a new wiki page and the index is updated.

---

### User Story 3 - Lint the Wiki for Health and Gaps (Priority: P3)

The researcher asks the system to health-check the wiki. The system scans for
contradictions between pages, stale claims superseded by newer sources, orphan pages,
missing cross-references, and implied concepts that lack their own page. It surfaces
findings with suggested follow-up sources or questions.

**Why this priority**: Lint keeps the wiki trustworthy as it scales. Without it, the
knowledge base drifts into inconsistency. Lower priority than ingest/query because
value accumulates first; linting is maintenance.

**Independent Test**: Can be tested after at least five sources are ingested by running
a lint pass and verifying the output lists at least one actionable finding (orphan,
gap, or contradiction) with a specific page reference.

**Acceptance Scenarios**:

1. **Given** the wiki has grown to 10+ pages,
   **When** the researcher requests a lint pass,
   **Then** the system surfaces any contradictions, orphan pages, and concept gaps,
   each with a specific page reference and a suggested next action.

2. **Given** a lint pass finds no issues,
   **When** the results are reported,
   **Then** a "wiki is healthy" confirmation is appended to the log with a timestamp.

---

### Edge Cases

- Sources too large for a single context window pass are split into chunks, processed
  sequentially, and summarized into one unified wiki page that notes the chunked processing.
- Sources outside the space data center domain are accepted and filed under
  `wiki/adjacent/` with a short relevance note; no primary entity or concept pages
  are created for them unless the researcher requests it.
- When three or more sources disagree on a claim, the system reasons about the
  credibility of each source (peer-reviewed paper > industry report > blog post),
  documents all positions with credibility assessments and citations, and marks
  the affected concept page as "Contested."
- When a query cannot be answered from existing wiki content, the system MUST use
  Playwright MCP to fetch a relevant source, ingest it, and answer with citations
  from the newly added page.
- When Playwright MCP fails to render a URL, the system retries once, then falls back
  to a basic HTTP fetch (no JS rendering). If both fail, the failure is logged with the
  URL, error reason, and timestamp, and the researcher is notified.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support ingesting source documents from a designated `raw/`
  directory and producing wiki pages in a designated `wiki/` directory.
- **FR-002**: System MUST maintain an `index.md` catalog updated on every ingest,
  listing each wiki page with a link and a one-line summary.
- **FR-003**: System MUST maintain an append-only `log.md` recording every ingest,
  query, and lint event with a timestamp and consistent prefix format.
- **FR-004**: System MUST flag contradictions between newly ingested content and
  existing wiki pages before closing an ingest session.
- **FR-005**: System MUST label inferences and open questions explicitly in wiki pages,
  distinguishing them from source-backed claims.
- **FR-006**: System MUST file substantive query answers back into the wiki as new
  pages when the researcher confirms their value. Supported output formats in v1:
  prose markdown pages, comparison tables, Marp slide decks, and matplotlib charts.
- **FR-007**: System MUST perform lint passes that identify: contradictions, stale
  claims, orphan pages, missing cross-references, and concept gaps.
- **FR-008**: System MUST deliver a minimal `CLAUDE.md` scaffold with section headings
  for: directory structure, page type conventions, ingest workflow, query workflow,
  lint workflow, and schema evolution notes. Content fills in through use; no
  domain-specific conventions are prefilled at delivery.
- **FR-009**: System MUST use `index.md` as the first navigation step for every query
  and lint operation. When a routine operation requires reading more than 5 wiki pages,
  the system MUST propose a CLI or MCP tool to pre-filter results, per constitution
  Principle VII. Adopted tools MUST be documented in the schema.
- **FR-010**: System MUST support domain-specific entity pages covering at minimum:
  companies, orbital regimes, power sources, cooling technologies, launch providers,
  and regulatory bodies relevant to space data centers.
- **FR-011**: System MAY fetch web pages as sources using the Playwright MCP tool.
  Each fetch MUST be logged in `log.md` with the URL, fetch timestamp, and reason.
  Fetched pages MUST be treated as immutable raw sources once saved to `raw/`.
- **FR-012**: System MUST detect when a source (by filename or URL) has been previously
  ingested. On re-ingest, the system MUST log the update event, re-process the source,
  and refresh all wiki pages whose content was derived from that source.
- **FR-013**: When a source is assessed as outside the space data center domain, the
  system MUST file it under `wiki/adjacent/` with a relevance note explaining its
  comparative or contextual value, rather than rejecting or silently ignoring it.
- **FR-014**: When a source is too large to process in a single context window pass,
  the system MUST split it into sequential chunks, process each chunk, and consolidate
  the results into one unified summary page that explicitly notes the chunked processing.
- **FR-015**: When a query cannot be answered from existing wiki content, the system
  MUST use Playwright MCP to fetch a relevant source, ingest it following the standard
  ingest flow, and synthesize an answer with citations from the newly added page.
- **FR-016**: When Playwright MCP fails to fetch a URL, the system MUST retry once,
  then attempt a basic HTTP fetch. If both fail, the system MUST log the failure with
  URL, error reason, and timestamp, and notify the researcher before proceeding.
- **FR-017**: When three or more sources make conflicting claims about a topic, the
  system MUST assess the credibility of each source (e.g., peer-reviewed paper,
  industry report, blog post), document all positions with credibility assessments
  and inline citations, and mark the affected wiki page as "Contested."
- **FR-018**: The implementation MUST deliver Claude skills in `.claude/skills/` for
  the three core wiki operations: ingest (process a source into wiki pages), query
  (search the wiki and synthesize a cited answer), and lint (health-check the wiki
  for contradictions, orphans, and gaps). Skills MUST be versioned and improved as
  failure modes are observed, per constitution Principle VI.
- **FR-019**: When a source file is a PDF, the system MUST automatically extract text
  during ingest using an available MCP or CLI tool before processing. PDFs are treated
  as equivalent to text sources once converted; the original PDF is preserved in `raw/`.
- **FR-020**: Every wiki page MUST include YAML frontmatter with a `status` field.
  Valid values: `draft` (newly created, not yet verified), `current` (up to date),
  `stale` (cited source re-ingested; content may be outdated), `contested` (3+
  sources disagree per FR-017). The lint pass (FR-007) MUST surface all `stale`
  and `draft` pages as actionable findings.
- **FR-021**: The implementation MUST create a `wiki/meta/` directory containing
  `evaluations.md` as an append-only record of all micro and macro self-evaluations,
  per the constitution Self-Evaluation Framework. This file MUST NOT be deleted or
  truncated.
- **FR-022**: The implementation MUST establish the following required directory layout
  at the repository root:

  ```text
  raw/                  # Immutable source documents (researcher-provided or fetched)
  wiki/
    sources/            # One summary page per ingested source
    entities/           # Named actors and artifacts (companies, orbital regimes, etc.)
    concepts/           # Domain ideas requiring their own page
    comparisons/        # Comparison tables and multi-source analyses
    synthesis/          # Cross-cutting synthesis and query-result pages
    adjacent/           # Out-of-domain source pages (filed per FR-013)
    meta/
      evaluations.md    # Append-only self-evaluation record (FR-020)
  index.md              # Content catalog updated on every ingest (FR-002)
  log.md                # Append-only operation log (FR-003)
  CLAUDE.md             # Minimal schema scaffold (FR-008)
  .claude/
    skills/             # Claude skills for ingest, query, and lint (FR-018)
  ```

### Key Entities *(include if feature involves data)*

- **Source**: An immutable raw document (article, paper, report, transcript) in `raw/`.
  May be researcher-provided or fetched from the web via Playwright MCP.
  Attributes: filename, date acquired, origin URL (if fetched), domain relevance,
  processing status (lifecycle: unprocessed → processing → processed | failed | chunked),
  ingest count (incremented on each re-ingest),
  source type (peer-reviewed paper / industry report / news article / blog post / other).
- **Wiki Page**: An LLM-generated markdown file in `wiki/`. Types: source summary,
  entity page, concept page, comparison, synthesis, query result. Out-of-domain
  sources produce an adjacent page filed under `wiki/adjacent/`.
  Attributes: title, type, sources (list of source filenames cited), status
  (YAML frontmatter — lifecycle: `draft` | `current` | `stale` | `contested`).
  Status transitions: new pages start as `draft`; promoted to `current` once all
  cited sources are processed; set to `stale` when a cited source is re-ingested
  and content may be outdated; set to `contested` when FR-017 applies.
- **Meta Artifact**: A system-level file in `wiki/meta/`. Required artifacts:
  `evaluations.md` (append-only self-evaluation record, per constitution
  Self-Evaluation Framework). Additional meta artifacts may be added as the system
  evolves (e.g., skills manifest, tool registry).
- **Index Entry**: A line in `index.md` linking to a wiki page with a one-line summary
  and optional metadata (date, source count).
- **Log Entry**: An append-only record in `log.md` of the form
  `## [YYYY-MM-DD] <operation> | <title>`.
- **Entity**: A named actor or artifact in the space data center domain (company,
  satellite constellation, orbital regime, technology).
- **Concept**: A domain idea requiring its own page (e.g., thermal management in
  vacuum, radiation hardening, latency by orbit, space-to-ground bandwidth).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A researcher can ingest a new source and see a complete summary page,
  updated index, and log entry within a single session.
- **SC-002**: After 10 ingested sources, the researcher can ask a cross-cutting
  analytical question and receive a cited answer that references at least 3 wiki pages.
- **SC-003**: A lint pass after 10+ sources identifies at least one actionable finding
  (contradiction, gap, or orphan) with a specific page reference and next-action
  suggestion.
- **SC-004**: All factual claims in wiki pages can be traced to at least one source
  document by following inline citations.
- **SC-005**: The wiki index remains navigable and complete as the source collection
  grows — every wiki page has an index entry and every index entry links to an
  existing page.
- **SC-006**: Routine query operations read `index.md` plus no more than 5 wiki pages
  per response. Any operation that would require reading more than 5 pages MUST
  trigger a proposal to build a CLI or MCP tool that pre-filters the result set.

## Assumptions

- This is a single-researcher personal tool — no multi-user access control, concurrent
  ingest coordination, or sharing infrastructure is required.
- The researcher uses a markdown-capable editor (e.g., Obsidian) to browse the wiki
  alongside the LLM agent in conversation.
- Source documents may be markdown, plain text, or PDF. The system converts PDFs
  automatically during ingest using available MCP or CLI tools. Image-only sources
  (no extractable text) are out of scope for v1.
- The researcher ingests sources one at a time and remains in the loop — batch
  unsupervised ingest is out of scope for v1.
- The system MAY fetch web pages using Playwright MCP as an additional sourcing
  mechanism; all fetched pages are saved to `raw/` and treated as immutable sources.
- No external database or vector store is required initially; the `index.md` file is
  sufficient for navigation at the expected scale (up to ~200 sources).
- The domain is "space data centers" broadly: orbital platforms, launch economics,
  power and thermal systems, connectivity, regulation, and commercial viability.
- The implementation MUST deliver a minimal `CLAUDE.md` scaffold with section headings
  (directory structure, page conventions, ingest/query/lint workflows) but no
  prefilled content. Conventions fill in organically through the first ingest sessions.
