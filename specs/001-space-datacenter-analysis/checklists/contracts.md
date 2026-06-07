# Contracts Checklist: Space Data Center Prospects Analysis Wiki

**Purpose**: Validate quality of behavioral requirements in skill contracts and CLI tool specifications — completeness, clarity, consistency, and measurability of the requirements themselves (not whether the implementation works).
**Created**: 2026-06-07
**Feature**: [spec.md](../spec.md) · [contracts/](../contracts/) · [data-model.md](../data-model.md)
**Scope**: Skill behavioral requirements (`.claude/skills/*.md`) + CLI tool requirements (`tools/*.sh`)
**Depth**: Focused — 33 items targeting highest-risk requirement gaps

---

## Skill Behavioral Completeness

- [x] CHK001 Are the conditions under which `status: stale` is set (re-ingest of a cited source) vs. `status: contested` (≥3 conflicting sources) fully enumerated without overlap? [Completeness, Spec §FR-012, FR-017]
  - Resolved: distinct conditions, non-overlapping by definition. Stale = source freshness; contested = claim conflict.
- [x] CHK002 Is the "credibility weighting" algorithm for contested sources specified beyond the qualitative ranking (peer-reviewed > industry report > blog post) — e.g., is a numeric or ordinal scoring rule defined? [Completeness, Spec §FR-017]
  - Resolved: intentional qualitative LLM judgment; no numeric algorithm needed. Ordinal ranking (peer_reviewed > industry_report > news_article > blog_post > other) is sufficient.
- [x] CHK003 Are requirements defined for the ingest skill's behavior on first-ever run — when `index.md` and `log.md` do not yet exist? [Completeness, Spec §FR-002, FR-003]
  - Resolved: contracts/skill-ingest.md Preconditions already state "created on first ingest if missing".
- [x] CHK004 Is the content of the micro self-evaluation entry specified — are "≤3 observations" requirements defined (what dimension to evaluate, minimum specificity)? [Completeness, Spec §FR-021, data-model.md §Meta Artifact]
  - Fixed: contracts/skill-ingest.md Step 10 now specifies micro format as `- [YYYY-MM-DD ingest] <observation>` lines (not the full 6-dimension table, which is macro-only).
- [x] CHK005 Are requirements for the "discuss key takeaways with researcher" step (ingest Step 5) specified — what constitutes a complete discussion, or is it intentionally left to LLM discretion? [Completeness, contracts/skill-ingest.md §Step 5]
  - Resolved: intentionally conversational; researcher-driven interaction step with no mechanical completion criterion.
- [x] CHK006 Are requirements defined for what the query skill should do when the Playwright MCP gap-detection fetch produces content already present in the wiki (redundant fetch)? [Completeness, Spec §FR-015, Gap]
  - Resolved: ingest skill's duplicate detection (FR-012 Step 2) handles redundant fetches naturally via re-ingest path.

---

## Skill Behavioral Clarity

- [x] CHK007 Are the output format selection triggers for the query skill unambiguous — is "compare" / "vs" in the question the only criterion for comparison table format, or are other triggers defined? [Clarity, Spec §FR-006, contracts/skill-query.md §Step 5]
  - Resolved: prose is default; comparison table triggered by "compare"/"vs" keywords; Marp/matplotlib only when researcher explicitly requests. Sufficient for implementation.
- [x] CHK008 Is the domain boundary for `domain_relevance: adjacent` vs. `primary` explicitly defined with criteria or examples — or is classification left to LLM judgment per session? [Clarity, Spec §FR-013]
  - Resolved: intentional LLM judgment. Domain scope is defined in spec Assumptions: "orbital platforms, launch economics, power and thermal systems, connectivity, regulation, and commercial viability."
- [x] CHK009 Are `source_type` classification signals documented (which title/URL/content signals identify `peer_reviewed` vs. `industry_report` vs. `blog_post`)? [Clarity, Spec §FR-017]
  - Fixed: contracts/skill-ingest.md Step 4 now lists explicit signals for all 5 source_type values.
- [x] CHK010 Is the contradiction check threshold quantified — does FR-004 require flagging any disagreement between two sources, or only when ≥3 sources disagree (the FR-017 threshold)? [Clarity, Spec §FR-004, FR-017]
  - Resolved: contracts/skill-ingest.md Step 7 already distinguishes: note contradiction on ANY disagreement (FR-004); set `status: contested` only at ≥3 sources (FR-017).
- [x] CHK011 Is the definition of "substantive query answer" (that triggers the file-back offer in FR-006) specified with measurable criteria, or left to LLM judgment? [Clarity, Spec §FR-006, Ambiguity]
  - Resolved: intentional — researcher confirmation is the gate. File-back is always offered; researcher decides substantiveness.
- [x] CHK012 Is the maximum chunk size for FR-014 (large source chunking) specified — the contract says "≤3000-word chunks" but does not define the minimum or what to do with a remainder chunk smaller than a useful summary unit? [Clarity, Spec §FR-014, contracts/skill-ingest.md §Step 3]
  - Fixed: contracts/skill-ingest.md Step 3 now specifies: if final remainder chunk is <200 words, merge it with the preceding chunk.
- [x] CHK013 Is "routine query" (the operation bounded by SC-006's ≤5 page limit) defined — are multi-step queries (gap-detection + re-query) treated as one or two routine operations? [Clarity, Spec §SC-006]
  - Fixed: contracts/skill-query.md Step 2 now clarifies SC-006 applies to the synthesis step only; gap-detection triggers a separate ingest operation with its own budget.

---

## Skill Behavioral Consistency

- [x] CHK014 Do the Playwright failure fallback behaviors in the ingest skill (FR-016: retry once, then curl) and the query gap-detection flow (FR-015) specify identical retry logic and logging behavior? [Consistency, Spec §FR-015, FR-016]
  - Fixed: contracts/skill-query.md Step 3 now includes explicit FR-016 fallback (retry once → curl → log fetch-failed → notify researcher).
- [x] CHK015 Are the log entry formats for all 8 operation types (ingest, re-ingest, fetch, fetch-failed, query, lint, evaluation, tool-proposal) consistent across all three skill contracts and data-model.md §Log Entry? [Consistency, data-model.md §Log Entry]
  - Resolved: all three skill contracts use `## [YYYY-MM-DD] <operation> | <title>` format consistent with data-model.md §Log Entry.
- [x] CHK016 Are the index entry update rules (add new vs. update existing) consistent between the ingest skill (FR-002, FR-012) and the query skill (file-back prompt in FR-006)? [Consistency, contracts/skill-ingest.md §Step 8, contracts/skill-query.md §Step 6]
  - Resolved: both skills update index.md for any new/modified pages using the same add/update rule.
- [x] CHK017 Does the lint skill's macro self-evaluation trigger definition (FR-021: "every 10 ingest operations") align with data-model.md's log entry format — is "ingest operation" defined to exclude re-ingest, fetch-failed, and query events? [Consistency, Spec §FR-021, data-model.md §Log Entry]
  - Fixed: contracts/skill-lint.md Step 7 now uses `grep -c "^## \[.*\] ingest |" log.md` (matches "ingest" but not "re-ingest").

---

## Skill Behavioral Coverage

- [x] CHK018 Are requirements specified for when a Playwright MCP fetch succeeds but returns empty, paywalled, or non-parseable content — is this treated as a fetch failure (FR-016) or a different error class? [Coverage, Spec §FR-011, FR-016]
  - Fixed: contracts/skill-ingest.md Step 1 now treats <100 useful words or paywall markers as fetch-failed (FR-016 path).
- [x] CHK019 Are requirements defined for the lint skill's handling of a wiki page whose `sources[]` frontmatter references a file that no longer exists in `raw/`? [Coverage, Edge Case, contracts/skill-lint.md]
  - Fixed: contracts/skill-lint.md Step 1 now includes `broken-sources` as a fourth lint-scan.sh issue class (Error severity).
- [x] CHK020 Are requirements defined for the ingest skill when PDF extraction (FR-019) produces empty or garbled output — is this treated as `processing_status: failed` or does the spec define a researcher escalation path? [Coverage, Spec §FR-019, contracts/skill-ingest.md §Error Outputs]
  - Fixed: contracts/skill-ingest.md Error Outputs now defines garbled output threshold (<100 words or >50% non-alphanumeric) → treat as extraction failure → prompt researcher.
- [x] CHK021 Are requirements specified for what happens when a re-ingest (FR-012) finds that affected wiki pages have since been manually deleted — should the ingest skill recreate them or log the gap? [Coverage, Edge Case, Spec §FR-012]
  - Resolved: acceptable behavior — ingest checks existing pages; deleted pages are not auto-recreated; lint handles any dangling index entries.
- [x] CHK022 Are requirements defined for the query skill's behavior when `tools/search.sh` returns zero results for a gap-detection query before invoking Playwright — should it attempt a broader query first? [Coverage, Spec §FR-015, SC-006]
  - Resolved: zero results from search → Playwright gap-detection triggers (FR-015). No broader-query retry required.

---

## CLI Tool Completeness

- [x] CHK023 Are exit code conventions (0 = clean, 1 = issues found) defined consistently across all four tools, and is stderr vs. stdout usage specified for error messages? [Completeness, contracts/skill-lint.md, Gap]
  - Fixed: contracts/wiki-page-format.md §CLI Tool Conventions now documents exit codes (0/1) and stdout/stderr usage for all four tools.
- [x] CHK024 Is the output format of `tools/search.sh` fully specified — one file path per line, relative or absolute paths, with or without match context lines? [Completeness, Gap, research.md §5]
  - Fixed: contracts/wiki-page-format.md §CLI Tool Conventions now specifies: project-relative paths, one per line, no match context.
- [x] CHK025 Are error handling requirements defined for all four tools when called on a non-existent or empty `wiki/` directory — should they exit 0 (no issues) or exit with a specific error? [Completeness, Coverage, Gap]
  - Fixed: contracts/wiki-page-format.md §CLI Tool Conventions now specifies: all tools exit 0 with no output when `wiki/` is absent or empty.

---

## CLI Tool Clarity

- [x] CHK026 Is the `tools/lint-scan.sh` definition of "orphaned page" unambiguous — does it mean absent from `index.md` only, absent from any `sources[]` reference, or both conditions simultaneously? [Clarity, contracts/skill-lint.md §Step 1, Ambiguity]
  - Fixed: contracts/skill-lint.md Step 1 now distinguishes two orphan types: `orphan-filesystem` (file exists, no index entry) and `orphan-index` (index entry, no file).
- [x] CHK027 Is the scope of `tools/xref-check.sh` clearly bounded — does it check `[[...]]` refs in `wiki/` subdirectories only, or also in `index.md`, `log.md`, and `wiki/meta/evaluations.md`? [Clarity, contracts/skill-lint.md §Step 2]
  - Resolved: contracts/skill-lint.md Step 2 now explicitly states scope is `wiki/` only; log.md and index.md don't use `[[...]]` syntax.
- [x] CHK028 Is the "missing required frontmatter field" criterion in `tools/lint-scan.sh` explicitly linked to the exact 6 fields defined in data-model.md §WikiPage (`title`, `type`, `sources`, `status`, `created`, `last_updated`)? [Clarity, Traceability, data-model.md §WikiPage]
  - Fixed: contracts/skill-lint.md Step 1 now references "the 6 required fields from data-model.md §WikiPage" by name.

---

## Acceptance Criteria Quality

- [x] CHK029 Can SC-006 ("≤5 wiki pages per routine query") be objectively verified from the skill contract alone — is there a logging mechanism that records how many pages were read per query operation? [Measurability, Spec §SC-006]
  - Fixed: contracts/skill-query.md Step 7 log format now includes `| pages-read: N` suffix, making SC-006 compliance grep-verifiable from log.md.
- [x] CHK030 Is the macro self-evaluation trigger (every 10 ingest operations per FR-021) measurable by the lint skill using only `grep -c "ingest" log.md` — or does `log.md` format need a distinct marker that excludes re-ingest entries? [Measurability, Spec §FR-021, data-model.md §Log Entry]
  - Fixed: contracts/skill-lint.md Step 7 now uses precise grep pattern and adds double-fire prevention via `ingest-count-at-trigger` header in macro evaluation entries.
- [x] CHK031 Are the 6 self-evaluation dimensions (Token Economy, Wiki Health, Ingest Quality, Query Yield, Skill Coverage, Tool Adoption) specified with measurable targets in both the constitution and the data model — and are those targets consistent between the two documents? [Measurability, Consistency, data-model.md §Meta Artifact]
  - Resolved: 6 dimensions and targets are consistent between constitution and data-model.md §Meta Artifact.

---

## Dependencies & Assumptions

- [x] CHK032 Is the assumption that `ripgrep` (`rg`) is installed documented as an explicit prerequisite for `tools/search.sh` — and is a fallback (e.g., `grep -r`) specified if `rg` is absent? [Assumption, research.md §5, Gap]
  - Resolved: ripgrep documented in quickstart.md Prerequisites (`brew install poppler ripgrep`). No fallback needed — ripgrep is an explicit installation step.
- [x] CHK033 Are requirements defined for the case where both `pdftotext` and `pdfplumber` are unavailable during ingest — should the ingest skill fail gracefully, prompt the researcher, or skip PDF processing entirely? [Assumption, Spec §FR-019, research.md §2]
  - Resolved: pdf-extract.sh detects available tool; if neither available, tool fails; contracts/skill-ingest.md Error Outputs covers "PDF extraction failure → log + prompt researcher to provide text version."

---

## Notes

- Items marked `[Gap]` indicate a requirement that appears absent from all spec/contract/plan documents
- Items marked `[Ambiguity]` indicate a requirement that exists but uses unquantified or subjective language
- Items marked `[Consistency]` indicate a potential conflict between two documents that reference the same behavior
- All 33 items resolved 2026-06-07. Contract fixes applied to: contracts/skill-ingest.md, contracts/skill-query.md, contracts/skill-lint.md, contracts/wiki-page-format.md
