---
name: lint
description: Health-checks the wiki for structural issues (orphaned pages, broken cross-references, missing frontmatter), surfaces findings with proposed fixes, and triggers macro self-evaluation at ingest milestones. Use after accumulating several sources, when wiki quality is in question, or to run a periodic health check.
---

# Lint Skill

Health-check the wiki for structural issues, surface findings with proposed fixes,
and trigger macro self-evaluation when the ingest count reaches a milestone.

**Trigger**: `/lint`

## When to use

Use this skill to maintain wiki quality after accumulating several sources, or
whenever the researcher suspects broken cross-references, stale pages, or missing
index entries. Also used to trigger the macro self-evaluation cycle.

## Prerequisites

- `index.md` exists
- `wiki/` directory exists with at least one page

---

## Steps

### Step 1 — Run lint scanner

```bash
bash tools/lint-scan.sh
```

Parse each output line with format `ISSUE:<severity>:<type>:<path>`:

| Issue type | Severity | Description |
| ---------- | -------- | ----------- |
| `orphan-filesystem` | Error | Wiki page file exists but has no `index.md` entry |
| `orphan-index` | Error | `index.md` entry points to a file that does not exist |
| `missing-frontmatter` | Error | Wiki page missing one or more of the 6 required fields (`title`, `type`, `sources`, `status`, `created`, `last_updated`) per data-model.md §WikiPage |
| `broken-sources` | Error | Wiki page `sources[]` lists a filename not present in `raw/` |
| `stale` | Warning | Page has `status: stale` |
| `contested` | Warning | Page has `status: contested` with no "Dispute" section |
| `no-sources` | Info | Wiki page has `sources: []` (no cited sources) |

---

### Step 2 — Run cross-reference checker

```bash
bash tools/xref-check.sh
```

Parse each `BROKEN: <source> → <target>` line. Scope: `wiki/` subdirectory pages
only (not `index.md` or `log.md`, which do not use `[[...]]` syntax).

Classify broken cross-references as **Error** severity.

---

### Step 3 — Classify all issues

Combine findings from Steps 1 and 2 into three groups:

- **Error**: `orphan-filesystem`, `orphan-index`, `missing-frontmatter`,
  `broken-sources`, broken cross-refs
- **Warning**: `stale`, `contested` (with no Dispute section)
- **Info**: `no-sources`, any other advisory findings

---

### Step 4 — Generate lint report

Output a structured summary:

```markdown
## Lint Report — [YYYY-MM-DD]

| Severity | Count |
| -------- | ----- |
| Error    | N     |
| Warning  | N     |
| Info     | N     |

### Errors
- `wiki/concepts/thermal-management.md`: missing-frontmatter (missing: status:)
- `wiki/entities/orbital-systems.md`: BROKEN: → wiki/concepts/nonexistent.md

### Warnings
- `wiki/sources/iss-report-2023.md`: stale

### Info
- `wiki/synthesis/launch-cost-trends.md`: no-sources
```

If there are zero issues, output:

```markdown
## Lint Report — [YYYY-MM-DD]

Wiki is healthy. No errors, warnings, or info items found.
```

---

### Step 5 — Propose fixes for Error-severity issues

For each Error, propose one or two options:

| Error type | Proposed fixes |
| ---------- | -------------- |
| `orphan-filesystem` | (A) Add index entry for the page, or (B) Delete the orphaned page |
| `orphan-index` | Remove the dangling index entry |
| Broken cross-ref | (A) Remove the broken `[[...]]` ref, or (B) Create a stub page at the target path |
| `missing-frontmatter` | Add default values for missing fields |
| `broken-sources` | (A) Remove the invalid filename from `sources[]`, or (B) Locate the correct file in `raw/` |

---

### Step 6 — Apply fixes (if researcher confirms)

For each Error where the researcher confirms a fix:

1. Read the affected wiki page.
2. Apply the fix (edit frontmatter, remove broken ref, add index entry, etc.).
3. Update `index.md` if entries were added or removed.
4. Write the updated file.

Do not modify Warning or Info items unless the researcher explicitly requests it.

---

### Step 7 — Macro self-evaluation trigger

Count ingest-only log entries (excluding re-ingest):

```bash
grep -c "^## \[.*\] ingest |" log.md
```

Read `wiki/meta/evaluations.md` to find the `ingest-count-at-trigger:` value from
the most recent macro evaluation entry (or 0 if no macro evaluation has been run yet).

**Trigger condition**: current count is a multiple of 10 AND current count > last
trigger count. This prevents double-firing when lint is run multiple times without
new ingests.

**When triggered**, append a macro evaluation to `wiki/meta/evaluations.md`:

```markdown
## [YYYY-MM-DD] Evaluation — macro-N-sources
ingest-count-at-trigger: N

| Dimension      | Score          | Target               | Notes |
| -------------- | -------------- | -------------------- | ----- |
| Token Economy  | On/Below Target | ≤5 pages/query      | avg N pages across last 10 sessions |
| Wiki Health    | On/Below Target | 0 contradictions    | N unresolved contradictions |
| Ingest Quality | On/Below Target | ≥80% update ≥2 pages | N/10 sources updated ≥2 pages |
| Query Yield    | On/Below Target | ≥50% filed back     | N/M queries filed back |
| Skill Coverage | On/Below Target | ≥80% sessions use skill | skill used in N/M sessions |
| Tool Adoption  | On Target / N/A | ≥1 tool/25 sources  | N tools adopted; N sources total |

**Highest-impact improvement**: <proposed action and rationale>
```

Also log: `## [YYYY-MM-DD] evaluation | macro-N-sources`

---

### Step 8 — Log entry

Append to `log.md`:

```
## [YYYY-MM-DD] lint | <N errors, N warnings, N info>
```

---

## Token budget

- 0 reads: lint scanner and xref checker are CLI tools (no LLM file reads for scanning)
- 0–N reads: only affected pages read when applying fixes (bounded by error count)
- 1 read: `log.md` (for macro trigger count)
- 1 read: `wiki/meta/evaluations.md` (for last trigger count, macro eval only)
- Total target: ≤3 file reads for a clean wiki; proportional to error count otherwise
