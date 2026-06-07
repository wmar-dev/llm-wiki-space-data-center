# Contract: Wiki Page Format

**Version**: 1.0.0

All wiki pages are Markdown files with YAML frontmatter. This contract defines the
canonical format for each page type. The lint skill enforces these rules (FR-007,
FR-020).

---

## Universal Frontmatter (required on every wiki page)

```yaml
---
title: "Human-readable title"
type: "concept"              # See Page Types below
sources:                     # raw/ filenames this page was derived from
  - "orbital-cooling-2025.md"
status: "current"            # draft | current | stale | contested
created: "2026-06-07"
last_updated: "2026-06-07"
---
```

All 6 fields are required. The lint skill flags pages with missing or invalid fields
as `Error` severity.

---

## Page Types

### `source_summary`

**Location**: `wiki/sources/<slug>.md`
**Created by**: ingest skill
**Represents**: Synthesized summary of a single ingested source

```markdown
---
title: "Orbital Cooling Systems: A Review"
type: "source_summary"
sources:
  - "orbital-cooling-2025.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

## Summary

2-4 paragraph synthesis of the source's key claims relevant to space data center
analysis.

## Key Claims

- Claim 1 (with credibility note if source_type is blog_post or unverified)
- Claim 2

## Source Metadata

| Field | Value |
| ----- | ----- |
| Source type | peer_reviewed |
| Domain relevance | primary |
| Date acquired | 2026-06-07 |
| Origin URL | https://... |

## Cross-references

- [[wiki/concepts/thermal-management.md]]
- [[wiki/entities/orbital-systems-inc.md]]
```

---

### `concept`

**Location**: `wiki/concepts/<slug>.md`
**Created by**: ingest skill (on first mention); updated on subsequent ingests
**Represents**: A domain idea or technical concept

```markdown
---
title: "Thermal Management in Orbital Environments"
type: "concept"
sources:
  - "orbital-cooling-2025.md"
  - "iss-thermal-2024.pdf"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

## Definition

Concise definition of the concept.

## Key Properties

- Property 1
- Property 2

## Evidence

Sourced claims about this concept, each with inline citation:
> "Radiative cooling efficiency drops 40% in direct sunlight exposure." — [[wiki/sources/orbital-cooling-2025.md]]

## Open Questions

- Open question 1 (labeled "Open question:" if unanswerable from current sources)

## Cross-references

- [[wiki/concepts/power-generation.md]]
```

---

### `entity`

**Location**: `wiki/entities/<slug>.md`
**Created by**: ingest skill
**Represents**: A named actor — company, organization, satellite system, orbital regime

```markdown
---
title: "Lumen Orbit Systems"
type: "entity"
sources:
  - "lumen-press-2026.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

## Description

Brief description of the entity and its relevance to space data center analysis.

## Key Facts

- Fact 1
- Fact 2

## Cross-references

- [[wiki/concepts/low-earth-orbit.md]]
```

---

### `comparison`

**Location**: `wiki/comparisons/<slug>.md`
**Created by**: query skill (on file-back) or ingest skill (when multi-source comparison
is warranted)
**Represents**: Side-by-side analysis of two or more subjects

```markdown
---
title: "LEO vs GEO for Edge Computing"
type: "comparison"
sources:
  - "leo-latency-study-2025.md"
  - "geo-bandwidth-report-2024.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

## Comparison

| Dimension | LEO | GEO |
| --------- | --- | --- |
| Latency | 20–40 ms | 500–600 ms |
| Coverage | Constellation required | Single satellite |
| ... | ... | ... |

## Analysis

Prose interpretation of the comparison table with inline citations.

## Cross-references

- [[wiki/concepts/latency.md]]
```

---

### `synthesis`

**Location**: `wiki/synthesis/<slug>.md`
**Created by**: query skill (on file-back)
**Represents**: Cross-cutting analysis that draws on multiple sources and concepts

```markdown
---
title: "Power Economics of Orbital Data Centers"
type: "synthesis"
sources:
  - "solar-power-iss-2024.pdf"
  - "power-density-comparison-2025.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

## Question

What was the research question this synthesis answers?

## Answer

Multi-paragraph synthesis with inline citations.
Factual claims: cited. Inferences: labeled "Inference:". Open questions: labeled
"Open question:".

## Cross-references

- [[wiki/concepts/power-generation.md]]
- [[wiki/comparisons/leo-vs-geo-power.md]]
```

---

### `adjacent`

**Location**: `wiki/adjacent/<slug>.md`
**Created by**: ingest skill (when `domain_relevance: adjacent`)
**Represents**: Out-of-domain source with potential signal for space data center analysis

Same format as `source_summary` but with an additional **Relevance Note** section
explaining why an out-of-domain source was retained.

---

## Cross-reference Syntax

Internal links use double-bracket notation:

```markdown
[[wiki/concepts/thermal-management.md]]
[[wiki/sources/orbital-cooling-2025.md]]
```

The xref-check tool (`tools/xref-check.sh`) validates that all `[[...]]` targets exist
as files. Broken refs are `Error` severity in lint output.

---

## Credibility Labels

When `source_type` is not `peer_reviewed`, claims sourced from that page MUST include
a credibility label in parentheses:

```markdown
> "Claim text." — [[wiki/sources/blog-post.md]] *(industry blog)*
```

| source_type | Label |
| ----------- | ----- |
| `peer_reviewed` | *(no label required)* |
| `industry_report` | *(industry report)* |
| `news_article` | *(news article)* |
| `blog_post` | *(blog post)* |
| `other` | *(unverified)* |

---

## CLI Tool Conventions

All four tools in `tools/` follow these conventions:

**Exit codes**:

- `0` — clean / success (no issues found, or search returned results)
- `1` — issues found (lint/xref errors present) or no results found (search)

**Output streams**:

- `stdout` — structured results intended for parsing (issue lines, file paths)
- `stderr` — error messages when the tool itself fails (e.g., `wiki/` missing)

**Empty wiki guard**: All tools exit `0` with no output when `wiki/` does not exist
or is empty. This prevents false positives during initial scaffold setup (T001).

**Output formats by tool**:

| Tool | Output format | Example |
| ---- | ------------- | ------- |
| `tools/lint-scan.sh` | `ISSUE:<severity>:<type>:<path>` | `ISSUE:Error:orphan-filesystem:wiki/concepts/foo.md` |
| `tools/xref-check.sh` | `BROKEN: <source> → <target>` | `BROKEN: wiki/concepts/foo.md → wiki/concepts/bar.md` |
| `tools/search.sh` | One project-relative file path per line | `wiki/concepts/thermal-management.md` |
| `tools/pdf-extract.sh` | Extracted text to stdout; saved as `raw/<name>.txt` | (file written, path echoed) |

`tools/search.sh` returns project-relative paths only (no match context lines), one
per line. Consumers call it as:

```bash
bash tools/search.sh "radiative cooling"
# → wiki/concepts/thermal-management.md
# → wiki/sources/orbital-cooling-2025.md
```

---

## Contested Page Conventions

When `status: contested`, add a **Dispute** section immediately after the frontmatter:

```markdown
## Dispute

3+ sources disagree on [claim]. See:
- [[wiki/sources/source-a.md]] — claims X
- [[wiki/sources/source-b.md]] — claims Y
- [[wiki/sources/source-c.md]] — claims Z

Credibility-weighted assessment: [which claim is better supported and why]
```
