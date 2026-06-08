---
name: query
description: Searches the wiki, synthesizes a cited answer from accumulated pages, and files the answer back as a new wiki page. Use whenever the researcher asks an analytical question about space data center prospects.
---

# Query Skill

Search the wiki, synthesize a cited answer, and automatically file the answer back
as a new wiki page.

**Trigger**: `/query <natural language question>`

Examples:
```text
/query What are the main power constraints for space-based data centers?
/query Compare LEO vs GEO for low-latency edge computing.
/query Which companies are furthest along in orbital data center development?
```

## When to use

Use this skill whenever the researcher asks an analytical question about space
data center prospects. It reads from the accumulated wiki rather than raw sources,
so at least one ingest session should have run first.

## Prerequisites

- `index.md` exists and has at least one entry
- At least one source has been ingested

---

## Steps

### Step 1 — Index scan (index-first, always)

Read `index.md`. Identify the entries most relevant to the question by matching
title, summary text, and status tags. Select ≤5 candidates.

If the index has many entries and scanning it returns more than 5 plausible
candidates, run the search tool to pre-filter:

```bash
bash tools/search.sh "<key terms from question>"
```

Read the top 5 results from the search output.

**SC-006 applies to this synthesis step.** The ≤5 page limit resets if gap-detection
(Step 3) triggers a separate ingest operation; the re-query after ingest is a fresh
operation with its own budget.

---

### Step 2 — Page reads

Read the ≤5 selected wiki pages. Extract:

- Factual claims relevant to the question (with their source citations)
- Inferences already labeled in those pages
- Open questions already identified

Do not read more than 5 pages in this step. If more are needed, run
`bash tools/search.sh "<refined terms>"` and read the top 5 from that output.

---

### Step 3 — Gap detection and source enrichment

Assess coverage from the pages read in Step 2, then automatically fetch and ingest
any sources needed to improve the answer — regardless of whether some pages were found.

**A. Total gap** (no relevant pages found):
1. Identify 1–3 external URLs highly relevant to the question.
2. For each URL, fetch using `playwright:browser_navigate` + `playwright:browser_snapshot`. On Playwright failure: retry once, then fall back to WebFetch / `curl -L <url>`. If all fetch attempts fail:
   - Log: `## [YYYY-MM-DD] fetch-failed | <url> — <reason>`
   - Skip that URL and try the next candidate.
3. For each successfully fetched source, run the full ingest workflow (save to `raw/<slug>.md`, create wiki pages, update `index.md`, log).
4. If at least one source was ingested, re-run this query from Step 1 as a fresh operation. If all fetches failed, answer with "Open question: <question> — no relevant sources found" and stop.

**B. Partial gap** (some pages found but coverage is incomplete for the question):
1. Identify 1–3 external URLs that would fill specific coverage gaps.
2. Fetch and ingest each one using the same procedure as (A) above — do not prompt the researcher.
3. Proceed to Step 4 using both the originally read pages and any newly created wiki pages.

**C. Full coverage** (existing pages fully address the question):
Proceed directly to Step 4.

**Coverage is partial when any of the following are true:**
- The question has a sub-topic for which no wiki page has a relevant claim
- The most recent source cited in relevant pages is >6 months old for a fast-moving topic
- The synthesis would contain more than 2 "Open question:" labels

---

### Step 4 — Synthesis

Write a cited answer using only information from the pages read in Step 2.

**Citation format:** inline wiki links: `[[wiki/concepts/thermal-management.md]]`

**Labeling rules:**
- Factual claims from pages: cite the source page inline — no additional label needed
- Inferences (not directly stated in sources): prefix with `Inference:`
- Unanswerable gaps (no source covers it): prefix with `Open question:`
- Claims from non-peer-reviewed sources: append credibility label, e.g., *(blog post)*

---

### Step 5 — Output format selection

Choose the output format based on the question:

| Trigger | Format | Location |
| ------- | ------ | -------- |
| Default (any question) | Prose markdown page | `wiki/synthesis/<slug>.md` |
| Question contains "compare" or "vs" | Comparison table | `wiki/comparisons/<slug>.md` |
| Researcher explicitly requests a presentation | Marp slide deck | `wiki/synthesis/<slug>-slides.md` |
| Researcher requests a chart or visualization | matplotlib Python script | `wiki/comparisons/<slug>-chart.py` |

**Marp slide deck format:**
```markdown
---
marp: true
theme: default
size: 16:9
---

# Title

---

## Slide 2
...
```
The researcher runs `marp <file>.md` to render HTML/PDF. Do not run Marp directly.

**matplotlib chart format:**
```python
# Generated by LLM — run with: python wiki/comparisons/<slug>-chart.py
import matplotlib.pyplot as plt
# ... chart data and rendering ...
plt.savefig("wiki/comparisons/<slug>-chart.png")
```
The researcher runs the script to produce the PNG.

---

### Step 6 — File back

Automatically write the answer as a new wiki page with full YAML frontmatter:

```yaml
---
title: "..."
type: "synthesis"       # or "comparison" for tables
sources:
  - "<raw-filename-1>"
  - "<raw-filename-2>"
status: "current"
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
---
```

Then add an entry to `index.md`.

---

### Step 7 — Log entry

Append to `log.md`:

```
## [YYYY-MM-DD] query | <question summary> | pages-read: N
```

The `pages-read: N` count makes SC-006 compliance verifiable from the log.

---

## Token budget

- 1 read: `index.md`
- ≤5 reads: relevant wiki pages
- 0–1 tool invocations: `tools/search.sh` (only if >5 candidates or zero results)
- 0–3 fetches: source enrichment (Step 3B/3A) — each fetch counts as one unit
- Each enrichment ingest: follows ingest skill token budget (≤8 reads)
- Total target for query synthesis: ≤7 file reads (excluding enrichment ingests)

If the synthesis budget is exceeded, append a tool-gap observation to `wiki/meta/evaluations.md`.
