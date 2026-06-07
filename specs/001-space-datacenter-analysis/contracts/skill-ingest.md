# Contract: Ingest Skill

**Skill file**: `.claude/skills/ingest.md`
**Trigger**: `/ingest` or `EXECUTE_COMMAND: ingest`
**Version**: 1.0.0

---

## Input

The researcher provides one of:

- A file path in `raw/` (e.g., `raw/orbital-cooling-2025.md`)
- A URL (LLM fetches via Playwright MCP per FR-011 and saves to `raw/`)

```text
/ingest raw/orbital-cooling-2025.md
/ingest https://example.com/space-datacenter-report.pdf
```

## Preconditions

- `index.md` exists (created on first ingest if missing)
- `log.md` exists (created on first ingest if missing)
- For URL input: Playwright MCP is configured and reachable

## Processing Steps

1. **Source acquisition**
   - If file path: verify file exists in `raw/`; check if previously ingested (FR-012)
   - If URL: fetch via Playwright MCP; save to `raw/<slug>.md`; log fetch event
     - If fetched content is <100 words of useful text, or contains login/paywall markers
       (e.g., "Sign in to read", "Subscribe to continue"), treat as fetch-failed (FR-016)
   - If PDF: run `tools/pdf-extract.sh` to produce `raw/<slug>.txt`

2. **Duplicate detection** (FR-012)
   - Check `index.md` for existing entry with same filename or origin URL
   - If found: treat as re-ingest; log `re-ingest` event; set `status: stale` on all
     wiki pages in `sources[]` that include this source

3. **Chunking** (FR-014)
   - Estimate source length; if likely to exceed context: split into ≤3000-word chunks
   - If the final remainder chunk is <200 words, merge it with the preceding chunk
   - Process each chunk sequentially; merge summaries
   - Set `processing_status: chunked` in source metadata

4. **Source credibility assessment** (FR-017 prerequisite)
   - Determine `source_type` from title, publication, URL, or content using these signals:
     - `peer_reviewed`: has DOI, ISSN, journal name, "Abstract", "References" section
     - `industry_report`: company or consultancy byline, market data, "executive summary"
     - `news_article`: news outlet domain, dateline, inverted-pyramid structure
     - `blog_post`: personal domain, informal tone, first-person, no institutional affiliation
     - `other`: none of the above signals present
   - Record in source metadata

5. **Discuss key takeaways** with researcher (one-at-a-time ingest; researcher stays
   in the loop)

6. **Write wiki pages** (index-first: read `index.md` to find related pages, then
   read ≤5 of them per SC-006):
   - `wiki/sources/<slug>.md` — source summary page (`type: source_summary`)
   - Update affected `wiki/entities/*.md` pages
   - Update affected `wiki/concepts/*.md` pages
   - If no relevant entity/concept page exists, create it (`status: draft`)
   - If source is out of domain: write to `wiki/adjacent/<slug>.md` (FR-013)

7. **Contradiction check** (FR-004)
   - Compare new claims against existing `current` and `contested` pages
   - If contradiction found: note in both affected pages and log; set `status: contested`
     on affected page if 3+ sources now disagree (FR-017 with credibility weighting)

8. **Update index.md** — add/update entry for every written/modified page

9. **Update log.md** — append entry: `## [YYYY-MM-DD] ingest | <source title>`

10. **Micro self-evaluation** — append ≤3 brief observations to `wiki/meta/evaluations.md`
    using the format `- [YYYY-MM-DD ingest] <observation>` (one line per observation).
    Micro evaluations are NOT the full 6-dimension table (that is reserved for macro
    evaluations triggered by the lint skill). Observations should note: notable token
    usage, any contradiction or credibility issue encountered, or a tool gap identified.

11. **Set processing_status: processed** (or `chunked` if chunked)

## Outputs

- New or updated wiki pages in `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`,
  and/or `wiki/adjacent/`
- Updated `index.md`
- New log entry in `log.md`
- Micro evaluation entry in `wiki/meta/evaluations.md`

## Error Outputs

- Playwright fetch failure: log `fetch-failed` event; notify researcher; do not create
  source file (FR-016)
- PDF extraction failure: log failure; prompt researcher to provide text version
- PDF extraction produces garbled output: if extracted text is <100 words or contains
  >50% non-alphanumeric characters, treat as extraction failure and prompt researcher
- Processing failure mid-ingest: set `processing_status: failed`; log failure with reason

## Token Budget

- Read `index.md` first (1 read)
- Read ≤5 related wiki pages to check for contradictions and update affected pages
- If >5 pages are relevant, invoke `tools/search.sh` to pre-filter before reading
- Total target: ≤8 file reads per ingest (index + 5 wiki + source + 1 related entity)
