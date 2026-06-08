# Space Data Center Prospects Analysis Wiki

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
at `specs/003-local-wiki-server/plan.md`.
<!-- SPECKIT END -->

## Directory Structure

```
wiki/
├── sources/          # Source summaries (type: source_summary)
├── concepts/         # Concept definitions (type: concept)
├── entities/         # Company/organization profiles (type: entity)
├── synthesis/        # Query answers filed back (type: synthesis)
├── comparisons/      # Side-by-side analyses (type: comparison)
├── adjacent/         # Out-of-domain sources (type: adjacent)
└── meta/             # Self-evaluations (evaluations.md)
raw/                  # Raw ingested files (.md, .pdf, .txt)
tools/                # CLI utilities (lint-scan, xref-check, search, pdf-extract, wiki_server)
specs/                # Spec/plan/tasks artifacts per feature
```

Root files: `index.md` (page catalog), `log.md` (append-only operation log),
`SUMMARY.md` (human-readable overview), `Makefile`, `opencode.json`.

Reference: `specs/001-space-datacenter-analysis/plan.md §Project Structure`

## Page Type Conventions

All wiki pages require 6-field YAML frontmatter:
```yaml
---
title: "Human-readable title"
type: "source_summary"    # source_summary | concept | entity | comparison | synthesis | adjacent
sources:
  - "<raw-filename>"
status: "current"         # draft | current | stale | contested
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
---
```

- `status: draft` for news/blog/other sources; `status: current` for peer-reviewed/industry reports
- `status: stale` on re-ingest; `status: contested` when 3+ sources disagree
- Cross-references use `[[wiki/type/slug.md]]` syntax
- Non-peer-reviewed claims include credibility labels: *(blog post)*, *(news article)*, *(industry report)*
- Inferences labeled `Inference:`; unanswerable gaps labeled `Open question:`

Reference: `specs/001-space-datacenter-analysis/contracts/wiki-page-format.md`

## Ingest Workflow

**Trigger**: `/ingest <path-or-url>`

Load skill `.claude/skills/ingest/SKILL.md` for full details. Summary:

1. **Source acquisition** — local file (raw/ or PDF) or URL (Playwright → curl fallback)
2. **Duplicate detection** — check index.md; mark existing pages `stale` on re-ingest
3. **Chunking** — split sources >6000 words into ≤3000-word chunks
4. **Credibility assessment** — classify as `peer_reviewed` / `industry_report` / `news_article` / `blog_post` / `other`
5. **Write pages** — always a source_summary; add entity/concept pages as warranted
6. **Contradiction check** — compare with existing pages; flag disagreements
7. **Update index.md** — add/update catalog entries
8. **Update log.md** — append ingest entry
9. **Micro self-evaluation** — append ≤3 observations to `wiki/meta/evaluations.md`
10. **Finalize** — set `processing_status: processed` in index.md

Budget: ≤8 file reads per ingest.

Reference: `specs/001-space-datacenter-analysis/contracts/skill-ingest.md`

## Query Workflow

**Trigger**: `/query <natural language question>`

Load skill `.claude/skills/query/SKILL.md` for full details. Summary:

1. **Index scan** — read index.md, select ≤5 relevant pages (search.sh to pre-filter if needed)
2. **Page reads** — extract facts, inferences, open questions from ≤5 pages
3. **Gap detection** — total gap (auto-fetch + ingest new sources), partial gap (enrich), or full coverage
4. **Synthesis** — write cited answer
5. **Output format** — prose page (`wiki/synthesis/`), comparison table (`wiki/comparisons/`), Marp slides, or matplotlib chart
6. **File back** — write new wiki page with full frontmatter; add entry to index.md
7. **Open question cleanup** — remove answered questions from source pages
8. **Log entry** — append to log.md with pages-read count

Reference: `specs/001-space-datacenter-analysis/contracts/skill-query.md`

## Lint Workflow

**Trigger**: `/lint`

Load skill `.claude/skills/lint/SKILL.md` for full details. Summary:

1. Run `tools/lint-scan.sh` (checks: orphan filesystem/index, missing frontmatter, broken sources, stale/contested status)
2. Run `tools/xref-check.sh` (validates `[[...]]` cross-reference targets)
3. Classify issues: Error / Warning / Info
4. Generate structured lint report
5. Propose fixes for Error-severity issues
6. Apply fixes if researcher confirms
7. Trigger macro self-evaluation at ingest-count milestones (every 10)
8. Log entry

Reference: `specs/001-space-datacenter-analysis/contracts/skill-lint.md`

## Answer Open Questions Workflow

**Trigger**: `/answer-open-questions`

Load skill `.claude/skills/answer-open-questions/SKILL.md` for full details. Summary:

1. **Scan** — `rg -n "Open question:" wiki/` to find all unresolved gaps
2. **Research** — for each selected question: web search → fetch → ingest → update originating page
3. **Cross-page cleanup** — check other pages for the same open question
4. **Log** — append answer/unresolved entries to log.md
5. **Micro self-evaluation**

Reference: `.claude/skills/answer-open-questions/SKILL.md`

## Schema Evolution Notes

Extended metadata tracked in `index.md` entries beyond standard frontmatter:
- `[ingest_count: N]` — number of times a source has been ingested
- `[origin_url: <url>]` — source origin URL (for fetched sources)
- `[domain_relevance: primary|adjacent]` — domain relevance classification
- `[processing_status: processed|chunked|failed]` — ingest processing status

`log.md` operation types: `ingest | re-ingest | fetch | fetch-failed | query | lint | evaluation | tool-proposal | answer | answer-unresolved`

`wiki/meta/evaluations.md` is append-only, with micro entries on each ingest and macro entries (6-dimension table) at every 10th ingest.
