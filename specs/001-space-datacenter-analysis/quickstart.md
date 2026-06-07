# Quickstart: Space Data Center Prospects Analysis Wiki

**Validates**: [plan.md](plan.md) end-to-end
**Data model**: [data-model.md](data-model.md)
**Contracts**: [contracts/](contracts/)

This guide proves the system works by running each skill against a real source and
verifying the expected outputs. Run these scenarios in order on a fresh repository.

---

## Prerequisites

Install dependencies once:

```bash
brew install poppler ripgrep          # pdftotext + rg for search.sh
npm install -g @marp-team/marp-cli    # Marp slide rendering
pip install pdfplumber                # PDF fallback (optional)
```

Configure Playwright MCP in `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Verify required directories exist (created as part of initial scaffold):

```bash
ls raw/ wiki/sources/ wiki/concepts/ wiki/entities/ \
   wiki/comparisons/ wiki/synthesis/ wiki/adjacent/ wiki/meta/ \
   .claude/skills/ tools/
```

---

## Scenario 1 — First Ingest (Local File)

**Goal**: Ingest a local Markdown source and verify wiki structure is created.

**Setup**: Create a minimal test source:

```bash
cat > raw/test-source-001.md << 'EOF'
# Radiative Cooling for Space Data Centers

Space data centers face a unique thermal challenge: without convective cooling,
heat must be radiated directly to space. Radiators operating at ~300K can reject
~450 W/m². A 1 MW data center requires roughly 2,200 m² of radiator surface.

Published by: Space Architecture Research Group, 2025.
EOF
```

**Run**:

```
/ingest raw/test-source-001.md
```

**Expected outputs** (verify each):

| Check | Command | Expected |
| ----- | ------- | -------- |
| Source summary page created | `ls wiki/sources/test-source-001.md` | File exists |
| Index entry added | `grep "test-source-001" index.md` | 1 line match |
| Log entry appended | `grep "ingest" log.md` | `## [2026-...] ingest \| ...` |
| Concept page created | `ls wiki/concepts/` | ≥1 `.md` file |
| Evaluation entry | `tail -20 wiki/meta/evaluations.md` | Micro eval table |
| Frontmatter valid | `grep "^status:" wiki/sources/test-source-001.md` | `status: current` |

**Success criterion**: All 6 checks pass. SC-006: skill should read ≤8 files total.

---

## Scenario 2 — Query Against Single Source

**Goal**: Query the wiki and receive a cited answer from the ingested source.

**Run**:

```
/query What are the thermal constraints for space data centers?
```

**Expected outputs**:

| Check | Command | Expected |
| ----- | ------- | -------- |
| Answer cites source | Visual inspection | Contains `[[wiki/sources/test-source-001.md]]` |
| Reads ≤5 pages | (model self-reports in eval) | ≤5 pages read |
| Log entry appended | `grep "query" log.md` | `## [2026-...] query \| ...` |

**Follow-up**: Accept the file-back offer and verify:

```bash
ls wiki/synthesis/      # or wiki/comparisons/
grep "thermal" index.md # new index entry
```

**Success criterion**: Cited answer with inline ref; filed page has valid frontmatter.

---

## Scenario 3 — URL Ingest via Playwright MCP

**Goal**: Fetch and ingest a web source using Playwright MCP.

**Run** (use any publicly accessible article about space data centers):

```
/ingest https://en.wikipedia.org/wiki/Space-based_solar_power
```

**Expected outputs**:

| Check | Command | Expected |
| ----- | ------- | -------- |
| Raw file created | `ls raw/` | New `.md` file with fetched content |
| `origin_url` recorded | `grep "origin_url" index.md` | Wikipedia URL present |
| Source summary page | `ls wiki/sources/` | New page for fetched source |
| `adjacent` or `primary` domain | `grep "domain_relevance" index.md` | One of the valid values |

**Success criterion**: Fetch + ingest completes without error; `fetch` log entry precedes
`ingest` log entry in `log.md`.

---

## Scenario 4 — Lint on Clean Wiki

**Goal**: Lint passes with zero errors on a well-formed wiki.

**Run**:

```
/lint
```

**Expected outputs**:

| Check | Expectation |
| ----- | ----------- |
| Lint report shows 0 Errors | Visual inspection |
| xref-check finds no broken refs | Visual inspection |
| Log entry appended | `grep "lint" log.md` |

**Success criterion**: Zero errors. Warnings are acceptable (stale pages if any).

---

## Scenario 5 — Re-ingest and Stale Detection

**Goal**: Re-ingesting a source marks dependent pages as stale.

**Setup**: Note which wiki pages reference `test-source-001.md` in their `sources[]`.

**Run**:

```
/ingest raw/test-source-001.md
```

**Expected outputs**:

| Check | Command | Expected |
| ----- | ------- | -------- |
| `re-ingest` log entry | `grep "re-ingest" log.md` | Entry present |
| Pages marked stale | `grep "status: stale" wiki/sources/test-source-001.md` | `status: stale` |
| `ingest_count` incremented | `grep "ingest_count" index.md` | Count is 2 |

**Success criterion**: Stale status applied; no pages silently left as `current` when
their source was updated.

---

## Scenario 6 — PDF Ingest

**Goal**: PDF extraction pipeline works end-to-end.

**Setup**: Place any PDF in `raw/`:

```bash
cp /path/to/any.pdf raw/test-pdf.pdf
```

**Run**:

```
/ingest raw/test-pdf.pdf
```

**Expected outputs**:

| Check | Command | Expected |
| ----- | ------- | -------- |
| Text extracted | `ls raw/test-pdf.txt` | File exists with non-zero size |
| Source summary created | `ls wiki/sources/test-pdf.md` | File exists |
| `processing_status: processed` | `grep "processing_status" index.md` | `processed` or `chunked` |

**Success criterion**: Wiki page created from PDF content without manual intervention.

---

## Scenario 7 — Search Tool Efficiency

**Goal**: `tools/search.sh` returns results faster than manual index scan for
multi-keyword queries.

**Run**:

```bash
bash tools/search.sh "radiative cooling"
```

**Expected output**: List of wiki page paths containing the term. Should complete in
under 2 seconds.

**Run**:

```bash
bash tools/xref-check.sh
```

**Expected output**: Either "No broken cross-references found" or a list of broken refs
with file path and target.

**Success criterion**: Both tools exit 0 (or exit 1 with a structured report for
xref-check); output is grep-parseable.

---

## Scenario 8 — Macro Self-Evaluation Trigger

**Goal**: After 10 ingest operations, a macro evaluation is appended automatically.

**Setup**: Run `/ingest` until `grep -c "^## \[" log.md` shows 10 or more `ingest`
entries (use test sources).

**Trigger**:

```
/lint
```

**Expected output**: `wiki/meta/evaluations.md` gains a new macro evaluation entry
with the full 6-dimension table.

**Success criterion**: Evaluation entry present with `trigger: macro-10-sources`.

---

## Failure Mode Reference

| Symptom | Likely cause | Remediation |
| ------- | ------------ | ----------- |
| `/ingest` URL fails | Playwright MCP not running | Check `.claude/mcp.json`; restart Claude Code |
| `pdftotext: command not found` | poppler not installed | `brew install poppler` |
| Lint reports orphaned pages | Page written but index not updated | Re-run ingest on affected source |
| `status: stale` not set on re-ingest | Skill version older than 1.0.0 | Update `.claude/skills/ingest.md` |
| `[[wiki/...]]` refs not resolving | Page deleted or renamed | Run `tools/xref-check.sh` to find all broken refs |
