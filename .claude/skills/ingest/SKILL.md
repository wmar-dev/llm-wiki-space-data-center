---
name: ingest
description: Processes a source document (local file or URL) into wiki pages, updates the index and log, and appends a self-evaluation entry. Use when the researcher wants to add a new source to the wiki, ingest a document, or refresh an existing source.
---

# Ingest Skill

Process a source document (local file or URL) into wiki pages, update the index
and log, and append a micro self-evaluation entry.

**Trigger**: `/ingest <path-or-url>`

## When to use

Use this skill whenever the researcher wants to add a new source to the wiki or
refresh an existing one. Works with Markdown, plain-text, and PDF files, and with
any URL accessible via Playwright MCP.

## Prerequisites

- `index.md` exists (created automatically on first ingest if missing)
- `log.md` exists (created automatically on first ingest if missing)
- For URL input: Playwright MCP configured in `.claude/mcp.json`

---

## Steps

### Step 0 — Bootstrap (first-ever ingest only)

If `index.md` does not exist, create it with the header and format comment from
the project scaffold. If `log.md` does not exist, create it with the header and
format comment. Then proceed to Step 1.

---

### Step 1 — Source acquisition

**If the input is a file path in `raw/`:**

1. Verify the file exists.
2. If the file is a PDF (`.pdf` extension), run:
   ```bash
   bash tools/pdf-extract.sh raw/<filename>.pdf
   ```
   Use the extracted text (`raw/<basename>.txt`) for all subsequent steps.
   If extraction fails or produces <100 words or >50% non-alphanumeric characters,
   log a `fetch-failed` entry, notify the researcher, and stop.
3. Proceed to Step 2.

**If the input is a URL:**

1. Fetch the page using Playwright MCP (`playwright:browser_navigate` + `playwright:browser_snapshot`).
2. If Playwright fails: retry once. If still failing: fall back to `curl -L <url>`.
3. If all fetch attempts fail, OR if the fetched content is <100 words of useful text
   or contains paywall/login markers (e.g., "Sign in to read", "Subscribe to continue"):
   - Log: `## [YYYY-MM-DD] fetch-failed | <url> — <reason>`
   - Notify the researcher.
   - Stop.
4. Save fetched content to `raw/<slug>.md` where `<slug>` is a kebab-case summary of
   the page title or URL path.
5. Log: `## [YYYY-MM-DD] fetch | <url>`
6. Proceed to Step 2.

---

### Step 2 — Duplicate detection

Read `index.md`. Check whether the source filename or origin URL is already present.

**If this is a re-ingest:**

- Log: `## [YYYY-MM-DD] re-ingest | <source title>`
- Set `status: stale` on every wiki page whose `sources[]` frontmatter lists this
  source filename.
- Update `last_updated` on those pages to today's date.
- Continue processing to refresh content.

**If this is a new source:** proceed to Step 3.

---

### Step 3 — Chunking

Estimate the source length in words.

- If the source is likely to exceed the context window (>6000 words):
  - Split into sequential chunks of ≤3000 words.
  - If the final remainder chunk is <200 words, merge it with the preceding chunk.
  - Process each chunk through Steps 4–7 sequentially.
  - Consolidate all chunk summaries into one unified source summary page (note the
    chunked processing in the page body).
  - Set `processing_status: chunked` in the source metadata recorded in `index.md`.
- Otherwise: proceed as a single pass.

---

### Step 4 — Source credibility assessment

Determine the `source_type` using these signals:

| source_type | Signals |
| ----------- | ------- |
| `peer_reviewed` | DOI present, ISSN, journal name in byline, "Abstract" section, "References" section with numbered citations |
| `industry_report` | Company or consultancy byline, market sizing data, "Executive Summary", logo/branding |
| `news_article` | News outlet domain or byline, dateline, inverted-pyramid structure |
| `blog_post` | Personal domain, informal/first-person tone, no institutional affiliation |
| `other` | None of the above signals present |

Record `source_type` in the source metadata to be stored in the `index.md` entry.

---

### Step 5 — Write wiki pages

**Read `index.md` first.** Identify existing pages related to this source's content.
Read at most 5 of those pages (SC-006 token budget). If more than 5 pages are relevant,
run `bash tools/search.sh "<key terms>"` first to pre-filter, then read the top 5.

**Write or update the following pages:**

1. **Source summary** — `wiki/sources/<slug>.md` (`type: source_summary`)
   Always created fresh (or updated if re-ingesting).

2. **Entity pages** — `wiki/entities/<slug>.md` (`type: entity`)
   One page per named actor: company, satellite constellation, orbital regime,
   regulatory body, launch provider. Create if missing (`status: draft`); update
   `sources[]` and body if existing.

3. **Concept pages** — `wiki/concepts/<slug>.md` (`type: concept`)
   One page per significant domain idea: thermal management, radiation hardening,
   latency by orbit, power density, etc. Create if missing (`status: draft`);
   update if existing.

4. **Adjacent page** (if `domain_relevance: adjacent`) — `wiki/adjacent/<slug>.md`
   (`type: adjacent`)
   File out-of-domain sources here. Include a "Relevance Note" section explaining
   the comparative or contextual value. Do NOT create primary entity or concept pages
   for adjacent sources.

All wiki pages MUST include the full YAML frontmatter:

```yaml
---
title: "..."
type: "..."          # source_summary | entity | concept | comparison | synthesis | adjacent
sources:
  - "<raw-filename>"
status: "draft"      # new pages start as draft; set to current once verified
created: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
---
```

Set `status: current` immediately if the source is `peer_reviewed` or
`industry_report`. Set `status: draft` for `news_article`, `blog_post`, or `other`.

For claims sourced from non-peer-reviewed material, append a credibility label:
> "Claim text." — [[wiki/sources/slug.md]] *(blog post)*

Label inferences explicitly: `Inference: <claim>`
Label unanswerable gaps: `Open question: <question>`

---

### Step 6 — Contradiction check

Compare new claims from this source against existing `current` and `contested` pages
just read in Step 6.

**On any disagreement between this source and an existing page (FR-004):**
- Add a note in both the new source summary and the affected existing page.
- Log: `## [YYYY-MM-DD] contradiction | <affected page> vs <new source>`

**When ≥3 sources now disagree on a claim (FR-017):**
- Set `status: contested` on the affected wiki page.
- Add a "Dispute" section to that page:

```markdown
## Dispute

3+ sources disagree on [claim]. See:
- [[wiki/sources/source-a.md]] — claims X *(peer_reviewed)*
- [[wiki/sources/source-b.md]] — claims Y *(industry_report)*
- [[wiki/sources/source-c.md]] — claims Z *(blog_post)*

Credibility-weighted assessment: [which claim is better supported and why]
```

---

### Step 7 — Verify origin_url resolves

After writing wiki pages, if the source summary page has an `origin_url` set:

1. Fetch the URL using `webfetch` or a HEAD request.
2. If the URL returns a non-2xx status (e.g., 404, 410, 403):
   - Notify the researcher: `origin_url returned <status> — may need a corrected URL.`
   - Attempt to search for the correct URL by searching the page title on the source domain.
   - If a working URL is found, update `origin_url` before proceeding.
3. If the URL resolves successfully, continue.

---

### Step 8 — Update index.md

For every wiki page written or modified in Step 6, add or update its index entry:

```
- [Title](wiki/type/slug.md) — one-line summary [status: current] [sources: N]
```

- `status` tag reflects the page's current status field.
- `sources: N` count must match the page's `sources[]` array length.
- `stale` and `contested` pages MUST include their status tag.

---

### Step 9 — Update log.md

Append:

```
## [YYYY-MM-DD] ingest | <source title>

<1–2 sentence summary of what was processed and any notable findings>
```

---

### Step 10 — Micro self-evaluation

Append ≤3 brief observations to `wiki/meta/evaluations.md`:

```
- [YYYY-MM-DD ingest] <brief observation>
```

Observations should note one or more of:
- Token usage (e.g., "read 4/5 allowed pages; no search needed")
- Any contradiction or credibility issue encountered
- A tool gap identified (e.g., "needed more than 5 pages; search.sh would help")

Do NOT write the full 6-dimension evaluation table here — that is for macro
evaluations triggered by the lint skill.

---

### Step 11 — Finalize

Set the source metadata in `index.md`:
- `processing_status: processed` (or `chunked` if Step 3 applied)
- `ingest_count: N` (1 for new source; incremented for re-ingest)

---

## Error handling

| Condition | Action |
| --------- | ------ |
| Playwright fetch fails after retry + curl fallback | Log `fetch-failed`; notify researcher; stop |
| Fetched content <100 words or paywalled | Treat as fetch failure (above) |
| PDF extraction fails or produces garbled output | Log failure; prompt researcher to provide text version |
| Mid-ingest failure | Set `processing_status: failed`; log failure with reason |

---

## Token budget

- 1 read: `index.md`
- ≤5 reads: related wiki pages (use `tools/search.sh` to pre-filter if >5 candidates)
- 1 read: source file (or extracted text for PDFs)
- Total target: ≤8 file reads per ingest

If this budget is exceeded, append a tool-gap observation to `wiki/meta/evaluations.md`
and log a `tool-proposal` entry in `log.md`.
