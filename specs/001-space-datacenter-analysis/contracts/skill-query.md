# Contract: Query Skill

**Skill file**: `.claude/skills/query.md`
**Trigger**: `/query` or natural language question during conversation
**Version**: 1.0.0

---

## Input

Natural language question from the researcher:

```text
/query What are the main power constraints for space-based data centers?
/query Compare LEO vs GEO for low-latency edge computing.
/query Which companies are furthest along in orbital data center development?
```

## Preconditions

- `index.md` exists and is non-empty
- At least one source has been ingested

## Processing Steps

1. **Index scan** (FR-009 — index-first, always)
   - Read `index.md`; identify entries relevant to the query (by title/summary match)
   - Select ≤5 most relevant pages

2. **Page reads** (SC-006 — ≤5 pages)
   - Read selected wiki pages
   - If the query requires more than 5 pages: run `tools/search.sh "<query terms>"` to
     get a pre-filtered list; read the top 5 from that list
   - SC-006 applies to this synthesis step only. Gap-detection (Step 3) triggers a
     separate ingest operation with its own token budget; the subsequent re-query
     resets the page-read count.

3. **Gap detection** (FR-015, FR-016)
   - If no relevant pages found: use Playwright MCP to fetch a relevant source
   - On Playwright failure: retry once; then fall back to basic HTTP fetch (no JS
     rendering); if both fail, log `fetch-failed` with URL, error, and timestamp and
     notify researcher — do not proceed with ingest (FR-016)
   - Run ingest skill on the fetched source
   - Re-run query after ingest completes

4. **Synthesis**
   - Synthesize answer with inline citations (`[[wiki/concepts/thermal-management.md]]`)
   - Distinguish factual claims (sourced) from inferences (labeled "Inference:")
   - Distinguish open questions (labeled "Open question:")

5. **Output format selection** (FR-006)
   - Prose: default for explanatory answers
   - Comparison table: when question asks "compare" or "vs"
   - Marp slide deck: generate `.md` with `marp: true` frontmatter when researcher
     requests a presentation
   - matplotlib chart: generate Python script when data visualization requested

6. **File-back prompt**
   - Offer to file the answer as a new wiki page
   - If researcher confirms: write to `wiki/synthesis/<slug>.md` or
     `wiki/comparisons/<slug>.md`; update `index.md`; log `query` event

7. **Log entry**
   - Append: `## [YYYY-MM-DD] query | <question summary> | pages-read: N`
   - The `pages-read: N` count makes SC-006 compliance verifiable from the log

## Outputs

- Synthesized answer with inline citations
- Optionally: new wiki page in `wiki/synthesis/` or `wiki/comparisons/`
- Updated `index.md` (if page filed back)
- Log entry in `log.md`

## Output Format Details

### Prose page

Standard wiki page with YAML frontmatter (`type: query_result` or `synthesis`).

### Comparison table

Markdown table filed as `wiki/comparisons/<slug>.md` (`type: comparison`).

### Marp slide deck

```markdown
---
marp: true
theme: default
size: 16:9
---

# Title
...
```

Filed as `wiki/synthesis/<slug>-slides.md`. Researcher runs `marp <file>.md` to render.

### matplotlib chart

Python script filed as `wiki/comparisons/<slug>-chart.py`. Researcher runs
`python <script>.py` to produce PNG; PNG is then added to `wiki/comparisons/`.

## Token Budget

- 1 read: `index.md`
- ≤5 reads: relevant wiki pages
- 0–1 reads: Playwright fetch (only if gap detected)
- Total target: ≤7 file reads per query
