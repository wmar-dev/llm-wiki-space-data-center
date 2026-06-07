# Evaluations

<!-- APPEND-ONLY. Never delete or truncate entries. -->
<!-- Micro evaluations: appended by the ingest skill after each source is processed. -->
<!-- Macro evaluations: appended by the lint skill when ingest count reaches a multiple of 10. -->

<!-- Micro format:
- [YYYY-MM-DD ingest] <brief observation about token usage, contradiction, or tool gap>
-->

- [2026-06-07 ingest] PDF ingest: pdf-extract.sh succeeded on first try; read 2/8 files; solar output figure (280 W/m²) new — thermal figures corroborate prior source; no search needed.
- [2026-06-07 ingest] Read 2/8 allowed files (index.md + source); no search tool needed; created 2 pages (source summary + concept); wiki was empty so no contradiction check possible.
- [2026-06-07 ingest] SpaceX cost math: fetched URL via curl (Playwright not available); read 4 related wiki pages; created 3 pages (source summary + entity + concept) addressing earlier macro finding to improve ingest quality; no contradictions found.

## [2026-06-07] Evaluation — macro-10-sources

ingest-count-at-trigger: 10

| Dimension      | Score        | Target                  | Notes                                         |
| -------------- | ------------ | ----------------------- | --------------------------------------------- |
| Token Economy  | On Target    | ≤5 pages/query          | 1 query; 3 reads total (2 pages + index)      |
| Wiki Health    | On Target    | 0 contradictions        | 0 contradictions; 3 stale pages to review     |
| Ingest Quality | Below Target | ≥80% update ≥2 pages    | 2/10 created ≥2 pages; 7 placeholder ingests  |
| Query Yield    | On Target    | ≥50% filed back         | 1/1 queries filed back to wiki/synthesis/     |
| Skill Coverage | On Target    | ≥80% sessions use skill | All 10 ingests + 1 query used skills          |
| Tool Adoption  | On Target    | ≥1 tool/25 sources      | 3 tools used; 10 sources total                |

**Highest-impact improvement**: Ingest quality is the lagging dimension — 7 of 10 ingests produced source-only pages. For substantive ingests, always create at least one concept or entity page alongside the source summary.

<!-- Macro format:
## [YYYY-MM-DD] Evaluation — macro-N-sources
ingest-count-at-trigger: N

| Dimension      | Score        | Target              | Notes |
| -------------- | ------------ | ------------------- | ----- |
| Token Economy  | On Target    | ≤5 pages/query      |       |
| Wiki Health    | On Target    | 0 contradictions    |       |
| Ingest Quality | On Target    | ≥80% update ≥2 pages|       |
| Query Yield    | On Target    | ≥50% filed back     |       |
| Skill Coverage | On Target    | ≥80% sessions use skill |   |
| Tool Adoption  | N/A          | ≥1 tool/25 sources  |       |

**Highest-impact improvement**: <proposed action and rationale>
-->
