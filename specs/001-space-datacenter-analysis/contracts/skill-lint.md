# Contract: Lint Skill

**Skill file**: `.claude/skills/lint.md`
**Trigger**: `/lint`
**Version**: 1.0.0

---

## Input

No arguments required. Operates on the entire wiki directory.

```text
/lint
```

Optional scoped invocation (not yet in spec, reserved for future skill versions):

```text
/lint wiki/concepts/
/lint --stale
```

## Preconditions

- `index.md` exists
- `wiki/` directory exists with at least one page

## Processing Steps

1. **Run lint scanner** (FR-007, FR-022)
   ```bash
   bash tools/lint-scan.sh
   ```
   Returns `ISSUE:<severity>:<type>:<path>` lines. Detects four issue classes:
   - **orphan-filesystem**: wiki page file exists but has NO matching entry in `index.md`
   - **orphan-index**: `index.md` entry whose target file does NOT exist on disk
   - **missing-frontmatter**: wiki page missing any of the 6 required fields from
     data-model.md §WikiPage (`title`, `type`, `sources`, `status`, `created`, `last_updated`)
   - **broken-sources**: wiki page whose `sources[]` frontmatter lists a filename not
     present in `raw/`
   Exit 0 when no issues found; exit 1 when issues found.

2. **Run cross-reference checker** (FR-007)
   ```bash
   bash tools/xref-check.sh
   ```
   Returns `BROKEN: <source-file> → <target>` lines for every unresolvable `[[...]]`
   reference found in `wiki/` subdirectory pages. Scope: `wiki/` only (not `index.md`
   or `log.md`, which do not use `[[...]]` syntax).
   Exit 0 when clean; exit 1 when broken refs found.

3. **Classify issues** by severity:

   | Severity | Examples |
   | -------- | -------- |
   | Error | `orphan-filesystem`; `orphan-index`; broken cross-ref; `missing-frontmatter`; `broken-sources` |
   | Warning | `status: stale` page not updated in >30 days; `status: contested` with no resolution note |
   | Info | Wiki page with `sources: []` (no cited sources) |

4. **Generate lint report** — structured summary with issue counts and a per-issue table:

   ```markdown
   ## Lint Report — [YYYY-MM-DD]

   | Severity | Count |
   | -------- | ----- |
   | Error    | N     |
   | Warning  | N     |
   | Info     | N     |

   ### Errors
   - `wiki/concepts/thermal-management.md`: missing `status` frontmatter field
   - `wiki/entities/orbital-systems.md`: broken ref → `[[wiki/concepts/nonexistent.md]]`

   ### Warnings
   - `wiki/sources/iss-report-2023.md`: status stale, last updated 2026-01-01

   ### Info
   - `wiki/synthesis/launch-cost-trends.md`: no sources cited
   ```

5. **Propose fixes** for Error-severity issues:
   - `orphan-filesystem`: offer to add index entry or delete page
   - `orphan-index`: offer to remove the dangling index entry
   - Broken cross-ref: offer to remove broken ref or create stub target page
   - `missing-frontmatter`: offer to add default values for missing fields
   - `broken-sources`: offer to remove the invalid filename from `sources[]` or locate
     the correct file in `raw/`

6. **Apply fixes** if researcher confirms (FR-007):
   - Update affected wiki pages
   - Update `index.md` for new/removed entries
   - Log `lint` event

7. **Macro self-evaluation trigger** (FR-021):
   - Count ingest-only entries (excluding re-ingest): `grep -c "^## \[.*\] ingest |" log.md`
   - Read `wiki/meta/evaluations.md` to find the ingest count at last macro evaluation
     (stored as `ingest-count-at-trigger: N` in the macro evaluation header)
   - If current count is a multiple of 10 AND count > last-trigger-count: run macro
     self-evaluation and append to `wiki/meta/evaluations.md`; record
     `ingest-count-at-trigger: <current-count>` in the new entry header
   - This prevents double-firing when lint is run multiple times without new ingests

8. **Log entry**
   - Append: `## [YYYY-MM-DD] lint | <N errors, N warnings, N info>`

## Outputs

- Lint report displayed to researcher
- Optionally: fixed wiki pages and updated `index.md`
- Log entry in `log.md`
- Optionally: macro evaluation entry in `wiki/meta/evaluations.md`

## Token Budget

- 0 reads: lint scanner and xref checker are CLI tools (no LLM file reads)
- 0–N reads: only affected pages read when applying fixes (bounded by error count)
- 1 read: `log.md` (for macro trigger count)
- Total target: ≤3 file reads for a clean wiki; proportional to error count otherwise
