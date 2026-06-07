# Data Model: Space Data Center Prospects Analysis Wiki

**Phase 1 output for** `specs/001-space-datacenter-analysis/plan.md`

All entities are Markdown files with YAML frontmatter. No database schema — the
filesystem is the data store.

---

## Entity: Source

**Location**: `raw/<filename>` (original) + `raw/<filename>.txt` (extracted text if PDF)

**Frontmatter** (stored in `index.md` as metadata, not in the raw file itself):

```yaml
filename: "orbital-cooling-2025.md"
date_acquired: "2026-06-07"
origin_url: "https://example.com/article"   # null if researcher-provided
domain_relevance: "primary"                  # primary | adjacent | unrelated
source_type: "news_article"                  # peer_reviewed | industry_report |
                                             # news_article | blog_post | other
processing_status: "processed"               # unprocessed | processing |
                                             # processed | failed | chunked
ingest_count: 1                              # incremented on each re-ingest
```

**Processing status lifecycle**:

```text
unprocessed ──► processing ──► processed
                    │
                    ├──► failed        (Playwright/HTTP/PDF extraction error)
                    └──► chunked       (source too large; processed in chunks)
```

**Validation rules**:
- `filename` MUST be unique within `raw/`
- `origin_url` is required when source was fetched via Playwright MCP (FR-011)
- `processing_status` MUST transition forward only (no reversion to `unprocessed`)
- `ingest_count` increments on every re-ingest (FR-012); never resets to 0

---

## Entity: Wiki Page

**Location**: `wiki/<type>/<slug>.md`

**Frontmatter** (required on every wiki page per FR-020):

```yaml
title: "Thermal Management in Orbital Data Centers"
type: "concept"              # source_summary | entity | concept | comparison |
                             # synthesis | query_result | adjacent
sources:                     # list of raw/ filenames this page was derived from
  - "orbital-cooling-2025.md"
  - "iss-thermal-2024.pdf"
status: "current"            # draft | current | stale | contested
created: "2026-06-07"
last_updated: "2026-06-07"
```

**Status lifecycle**:

```text
draft ──► current ──► stale      (cited source re-ingested; content may be outdated)
                  └──► contested  (3+ sources disagree on a claim; FR-017)
```

**Validation rules**:
- Every wiki page MUST have all 6 frontmatter fields
- `status: stale` MUST be set when any source in `sources[]` is re-ingested (FR-012)
- `status: contested` is set by the ingest skill when FR-017 conditions are met
- `sources[]` MUST reference existing files in `raw/`; the lint skill flags broken refs
- `type: adjacent` pages live in `wiki/adjacent/` regardless of the `type` field

---

## Entity: Index Entry

**Location**: `index.md` (one entry per wiki page)

**Format** (single line per page):

```markdown
- [Title](wiki/type/slug.md) — one-line summary [status: current] [sources: 2]
```

**Rules**:
- Every wiki page MUST have exactly one index entry (FR-002)
- Index entries MUST be updated on every ingest and re-ingest (FR-002, FR-012)
- Entries for `stale` or `contested` pages MUST include the status tag
- `[sources: N]` count MUST match the page's `sources[]` frontmatter array length

---

## Entity: Log Entry

**Location**: `log.md` (append-only)

**Format**:

```markdown
## [YYYY-MM-DD] <operation> | <title>

<1-3 line summary of what happened>
```

**Operations**: `ingest` | `re-ingest` | `query` | `lint` | `fetch` |
`fetch-failed` | `evaluation` | `tool-proposal`

**Rules**:
- Every ingest, query, lint, fetch, and evaluation MUST produce a log entry (FR-003)
- Log entries MUST NOT be deleted or modified after writing
- The `## [YYYY-MM-DD]` prefix enables `grep "^## \[" log.md` parsing

---

## Entity: Meta Artifact

**Location**: `wiki/meta/<name>.md`

**Required artifacts**:

| File | Purpose | Append-only |
| ---- | ------- | ----------- |
| `evaluations.md` | Self-evaluation record (micro + macro) | Yes |

**Optional future artifacts** (added via FR-009 adaptive tooling):
- `tool-registry.md` — installed CLI/MCP tools and their trigger conditions
- `skills-manifest.md` — current skill versions and observed failure modes

**Evaluation entry format** (in `wiki/meta/evaluations.md`):

```markdown
## [YYYY-MM-DD] Evaluation — <trigger>

| Dimension | Score | Target | Notes |
| --------- | ----- | ------ | ----- |
| Token Economy | On Target | ≤5 pages/query | avg 3 pages this session |
| Wiki Health | On Target | 0 contradictions | — |
| Ingest Quality | On Target | ≥80% update ≥2 pages | 4/5 sources |
| Query Yield | Below Target | ≥50% filed back | 1/4 queries filed |
| Skill Coverage | On Target | ≥80% sessions use skill | used lint skill |
| Tool Adoption | N/A | ≥1 tool/25 sources | 8 sources ingested total |

**Highest-impact improvement**: <proposed action and rationale>
```

---

## Entity: Claude Skill

**Location**: `.claude/skills/<name>.md`

**Required skills** (FR-018):

| File | Triggered by | Core operation |
| ---- | ------------ | -------------- |
| `ingest.md` | `/ingest` | Process source → wiki pages + index + log |
| `query.md` | `/query` | Search index → read pages → synthesize answer |
| `lint.md` | `/lint` | Scan wiki → report findings → log |

**Frontmatter**:

```markdown
---
version: 1.0.0
last_updated: 2026-06-07
failure_modes: []
---
```

**Versioning**: Incremented per constitution Principle VI when failure modes are
observed and fixed. Failure modes are logged in the `failure_modes` frontmatter list
before being resolved.

---

## Entity: CLI Tool

**Location**: `tools/<name>.sh` (or `tools/<name>.py` for Python helpers)

**Required tools at delivery**:

| File | Purpose | Replaces |
| ---- | ------- | -------- |
| `tools/search.sh` | Full-text search across wiki pages | Manual index scan |
| `tools/xref-check.sh` | Verify all wiki cross-refs resolve | Lint manual check |
| `tools/pdf-extract.sh` | PDF-to-text extraction wrapper | Manual conversion |
| `tools/lint-scan.sh` | Orphan/stale/contested page scanner | Manual lint pass |

**Trigger threshold** (per constitution Principle VII): When a routine operation reads
>5 wiki pages, a tool MUST be proposed. `tools/search.sh` is the first tool to reach
for before considering any other approach.
