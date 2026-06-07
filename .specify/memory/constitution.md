<!--
SYNC IMPACT REPORT
==================
Version change: 1.2.1 → 1.3.0
Modified principles: none
Added sections: Self-Evaluation Framework (metrics, cadence, process, targets, artifact)
Removed sections: none
Templates requiring updates:
  ✅ constitution.md — this file
  ✅ plan-template.md — no changes required
  ✅ spec-template.md — no changes required
  ✅ tasks-template.md — no changes required
Follow-up TODOs: none
-->

# LLM Wiki Constitution

## Core Principles

### I. Source Immutability

Raw sources are the immutable ground truth of the knowledge base. The LLM MUST read from
source files but MUST NOT modify, delete, or overwrite them. If a source is superseded,
the wiki page referencing it MUST note the supersession — the original source stays intact.

**Rationale**: Preserving raw sources ensures analysis can always be re-grounded. Any
wiki claim can be traced back and verified against the document that produced it.

### II. Fact-Grounded Analysis

Every claim written into the wiki MUST be traceable to one or more source documents.
Inferences that go beyond the source material MUST be explicitly labeled (e.g.,
"Inference:", "Open question:"). Speculation without an evidential basis MUST NOT be
presented as fact.

**Rationale**: The user input "Ground analysis in facts and first principles" is the
load-bearing directive of this constitution. A wiki that blurs sources and speculation
degrades into noise over time. Explicit traceability lets the human owner audit, correct,
and build on the wiki with confidence.

### III. Incremental, Compounding Synthesis

Knowledge MUST be compiled once into the wiki and kept current as new sources arrive.
When a new source is ingested, the LLM MUST update every affected wiki page — entity
pages, concept pages, the synthesis, the index — rather than leaving stale content in
place. Re-deriving knowledge from scratch on each query is not acceptable.

**Rationale**: The core value of the wiki pattern is accumulation. A wiki that requires
re-synthesis on every query is just RAG with extra steps.

### IV. Navigability and Internal Consistency

The wiki MUST maintain a complete `index.md` (content catalog with one-line summaries)
and an append-only `log.md` (chronological record of ingests, queries, and lint passes).
Every cross-reference in a wiki page MUST point to a page that exists. Orphan pages
(no inbound links) MUST be flagged during lint. Contradictions between pages MUST be
noted explicitly in the affected pages and in the log.

**Rationale**: A large wiki without navigation infrastructure collapses under its own
size. The index and log are first-class artifacts, not afterthoughts.

### V. Human Direction, LLM Execution

Humans own: source curation, analytical direction, question framing, and quality review.
The LLM owns: summarizing, cross-referencing, filing, bookkeeping, and wiki maintenance.
The LLM MUST NOT make editorial decisions about which sources to retain or discard. It
MAY suggest sources to investigate but MUST NOT autonomously ingest sources not provided
by the human.

**Rationale**: The division of labor is the system's core design. Blurring it — either
by asking humans to maintain the wiki manually, or by letting the LLM decide what
knowledge matters — undermines both the efficiency and the integrity of the knowledge
base.

### VI. Adaptive Tooling and Self-Improvement

The system MUST identify when its current tools, workflows, or schema conventions are
insufficient and propose concrete improvements. The LLM MAY build new tools (search
scripts, CLI utilities, index generators) when the human approves. The schema
(e.g., `CLAUDE.md`) MUST be updated to document any new tool, workflow change, or
operational convention as soon as it is adopted.

Self-improvement operates at three levels:

- **Tooling**: When the index-file approach becomes slow or incomplete, the LLM SHOULD
  propose a specific tool and, upon approval, build and document it. Tooling takes two
  forms — CLI tools (scripts, search engines, linters) and MCP servers (Playwright for
  web fetch, PDF extraction, external APIs). Both are first-class options; choose
  whichever better fits the capability. CLI tools that reduce token consumption
  (see Principle VII) are the highest-priority tooling investment. MCP servers SHOULD
  be added when a capability cannot be reasonably delivered as a CLI tool.
- **Schema co-evolution**: After each significant ingest cycle or lint pass, the LLM
  SHOULD identify one improvement to the schema or workflow and propose it to the
  human. Accepted proposals MUST be written into the schema before the next session.
- **Skill generation**: Repeated multi-step workflows SHOULD be codified as Claude
  skills in `.claude/skills/`. When the LLM performs the same compound operation more
  than twice, it SHOULD propose a skill that encapsulates it. Skills MUST be versioned,
  documented, and actively improved based on observed failure modes or inefficiencies.

The LLM MUST NOT silently change its own operating procedures. All self-improvement
MUST be made explicit, approved by the human, and recorded in the log.

**Rationale**: A system that cannot improve itself will be abandoned as the wiki
scales. The maintenance cost of a static workflow grows with the wiki; an adaptive
system keeps that cost near zero. First-principles check: every tool, schema change,
or skill MUST solve a demonstrated problem, not an anticipated one.

### VII. Token Economy

All LLM operations MUST minimize unnecessary token consumption. Token cost is a real
constraint; a wiki that requires reading large amounts of content on every operation
becomes expensive and slow as it scales.

Concrete rules:

- **Index-first navigation**: The index (`index.md`) MUST be consulted before any
  wiki-wide search. Never read pages speculatively — read only those the index
  identifies as relevant.
- **Pre-computed artifacts**: Source summaries, entity manifests, and concept indexes
  MUST be maintained so sources are never re-read in full when a summary suffices.
  Once a source is summarized, the summary is the operative artifact.
- **CLI/MCP-first for bulk operations**: Search, deduplication, cross-reference
  checking, and page listing SHOULD be handled by CLI tools or MCP servers rather
  than LLM passes over raw files. The LLM receives compact, pre-filtered results —
  not raw file contents. Use CLI for local file operations; use MCP for external
  services, rendering, and API calls.
- **Targeted reads**: When updating a wiki page, read only that page and its direct
  dependencies. Do not re-read the full wiki to make a local change.
- **Build CLI tools to cut tokens**: Whenever an LLM operation reads more than ~5
  files to answer a routine question, the LLM SHOULD propose a CLI tool that
  pre-computes or caches the answer. Token savings are the primary justification for
  new tooling investment.

**Rationale**: First-principles check — every token spent reading content the system
already processed is waste. The wiki's value comes from accumulated synthesis, not
from re-reading raw material on every query. Keeping operations token-lean means the
system remains fast and affordable as the knowledge base grows to hundreds of sources.

## Wiki Health Standards

The wiki MUST remain healthy as it grows. The following standards apply:

- **Completeness**: Every concept mentioned in a source MUST have a corresponding wiki
  page or a clear cross-reference to the page that covers it.
- **Freshness**: Pages MUST be updated when new sources supersede prior claims. Stale
  claims MUST be marked with a supersession note and the superseding source cited.
- **Lint cadence**: A lint pass (contradiction check, orphan detection, cross-reference
  audit, gap identification) MUST be performed periodically — at minimum after every
  ten ingested sources, or when the human requests it.
- **Output formats**: The wiki MAY produce outputs beyond plain markdown pages (tables,
  slide decks, charts, analyses). Valuable outputs MUST be filed back into the wiki
  as new pages rather than left in chat history.
- **Tooling**: CLI tools (e.g., local search engines) MAY be added when the index-file
  approach is no longer sufficient. Tooling choices MUST be documented in the schema.

## Operations Workflow

The three canonical operations and their non-negotiable steps:

**Ingest**:

1. LLM reads the source document.
2. LLM discusses key takeaways with the human (one-at-a-time ingest preferred).
3. LLM writes a summary page; updates the index; updates affected entity, concept, and
   synthesis pages; appends an entry to the log.
4. Any contradictions with prior wiki content MUST be flagged before closing the ingest.

**Query**:

1. LLM reads the index to identify relevant pages.
2. LLM reads the relevant pages and synthesizes an answer with inline citations.
3. If the answer constitutes new, reusable knowledge, it MUST be filed as a wiki page.

**Lint**:

1. LLM scans for: contradictions, stale claims, orphan pages, missing cross-references,
   implied concepts lacking their own page, and data gaps.
2. Findings MUST be surfaced to the human with suggested follow-up sources or questions.
3. Lint results MUST be appended to the log.

## Self-Evaluation Framework

The system MUST periodically evaluate its own performance against measurable targets
and propose the highest-impact improvement. Evaluation is not optional — a system that
cannot measure itself cannot improve itself.

### Dimensions and Targets

| Dimension | Metric | Target |
| --------- | ------ | ------ |
| Token Economy | Pages read per routine query | ≤ 5 (index + pages) |
| Wiki Health | Unresolved contradictions at session end | 0 |
| Ingest Quality | Sources that update ≥ 2 concept/entity pages | ≥ 80% |
| Query Yield | Substantive queries filed back as wiki pages | ≥ 50% |
| Skill Coverage | Sessions invoking at least one defined skill | ≥ 80% |
| Tool Adoption | New CLI/MCP tool proposed per 25 sources ingested | ≥ 1 |

### Evaluation Cadence

- **Micro (every session)**: At session end, the LLM MUST record ≤ 3 observations
  about what worked well, what was inefficient, and one proposed improvement. This
  takes no more than one paragraph and is appended to `wiki/meta/evaluations.md`.
- **Macro (every 10 sources or monthly)**: The LLM MUST perform a full evaluation
  across all six dimensions, score each against its target, identify the single
  highest-impact improvement, propose it to the researcher, and record the full
  evaluation in `wiki/meta/evaluations.md`.

### Evaluation Process

1. Review the last N log entries to reconstruct recent operations.
2. Score each dimension: **On Target** / **Below Target** / **No Data**.
3. For any dimension Below Target, identify the root cause (missing tool, schema
   gap, skill not yet defined, constitutional violation).
4. Select the single highest-impact improvement (by Impact × Feasibility).
5. Propose it to the researcher with a concrete action (build tool X, define skill Y,
   update schema section Z).
6. Record the evaluation and proposal in `wiki/meta/evaluations.md` under a dated
   heading: `## [YYYY-MM-DD] Evaluation — <trigger>`.

### Evaluation Artifact

`wiki/meta/evaluations.md` is an append-only record of all evaluations. It MUST NOT
be deleted or truncated. The LLM reads it at the start of each macro evaluation to
detect trends (a dimension that has been Below Target for two consecutive macro cycles
MUST trigger a tool or skill investment, not just another proposal).

**Rationale**: First-principles check — if the system never measures its own behavior,
it cannot know whether changes made through Principle VI (Adaptive Tooling) actually
improved anything. The evaluation framework closes the feedback loop. Targets are
concrete enough to be testable and forgiving enough to allow early-wiki variability.

## Governance

This constitution supersedes all other practices for this knowledge base. Amendments
require: a description of the change, a rationale grounded in first principles, and
an update to this document with an incremented version number.

**Versioning policy**:

- MAJOR: Removal or fundamental redefinition of a principle.
- MINOR: New principle, section, or materially expanded guidance.
- PATCH: Clarifications, wording fixes, non-semantic refinements.

**Compliance**: All ingest, query, and lint operations MUST be checked against this
constitution before execution. The plan-template.md Constitution Check gate enforces
this at the feature level.

**Runtime guidance**: The schema file (e.g., `CLAUDE.md` for Claude Code) is the
operational companion to this constitution. It documents wiki structure, conventions,
and workflows for the specific domain. The schema MUST not contradict this constitution.

**Version**: 1.3.0 | **Ratified**: 2026-06-07 | **Last Amended**: 2026-06-07
