# Evaluations

<!-- APPEND-ONLY. Never delete or truncate entries. -->
<!-- Micro evaluations: appended by the ingest skill after each source is processed. -->
<!-- Macro evaluations: appended by the lint skill when ingest count reaches a multiple of 10. -->

- [2026-06-08 ingest] NASA ATCS overview: primary-source areal density (14.2 kg/m² panel-level) is better than the ~19 kg/m² figure in existing pages; system-level density including pumps/tanks/joints is higher — both figures are valid at different scopes
- [2026-06-08 ingest] Read 0 additional wiki pages (all 4 relevant pages were in context from prior query session); stayed within 8-read budget with no search.sh needed
- [2026-06-08 ingest] TRRJ rotary joint mechanism confirmed as the source of "gimbaled panels for sun avoidance" cited in Orbital AI Factory — closes an implicit open question in the scissors-beam synthesis

<!-- Micro format:
- [YYYY-MM-DD ingest] <brief observation about token usage, contradiction, or tool gap>
-->

- [2026-06-07 ingest] PDF ingest: pdf-extract.sh succeeded on first try; read 2/8 files; solar output figure (280 W/m²) new — thermal figures corroborate prior source; no search needed.
- [2026-06-07 ingest] Read 2/8 allowed files (index.md + source); no search tool needed; created 2 pages (source summary + concept); wiki was empty so no contradiction check possible.
- [2026-06-07 ingest] SpaceX cost math: fetched URL via curl (Playwright not available); read 4 related wiki pages; created 3 pages (source summary + entity + concept) addressing earlier macro finding to improve ingest quality; no contradictions found.
- [2026-06-08 ingest] Bongers & Torres primary source: SSRN blocked (403); user supplied PDF directly; pdf-extract succeeded; upgraded Wikipedia-secondhand citations to peer-reviewed primary source across 3 synthesis pages; 72,090 exact figure and sensitivity range 21,520–107,600 now in wiki.
- [2026-06-08 ingest] 4 sources ingested in one session (2 PDFs + arXiv preprint + ESA news article); CRASH Clock metric (5.5 days) and 300K maneuver count were new quantitative claims not in any prior page; no contradictions with existing pages — figures complementary not conflicting.
- [2026-06-08 ingest] Space Policy 2026 survey: Rao & Rondina 2040–2184 orbit-unusable range is the widest uncertainty bound seen in the wiki — reflects genuine model sensitivity, not sloppiness; flagged in source page.

- [2026-06-07 answer] answer-open-questions: Researched 7 open questions via parallel web search + 4 deep fetches; created 6 new source pages with full frontmatter; updated 9 wiki pages; fixed 1 mislabeled pseudo-question. 2 questions remain partially unresolvable (no known public studies). Budget: 7 web searches, 4 deep fetches, ~25 file operations — within reason but near the upper end for a single workflow.
- [2026-06-08 answer] answer-open-questions: Researched 3 open questions via 4 web searches + 3 deep fetches; created 3 source summary pages; updated 1 synthesis page; 1 question partially resolved (OOS technically mature but GPU swap not demonstrated). Remaining gap: per-kg cost of robotic GPU module replacement.
- [2026-06-08 answer] answer-open-questions: Researched 5 open questions via 4 web searches + 2 deep fetches; created 3 source summary pages; updated 3 synthesis pages; resolved 5 questions (Xingshidai scale, Starcloud revenue, OpenAI involvement, Colossus GPU count, 2 GW ambiguity); 1 unresolved (Orbital wet mass — no public data found). Budget: 4 web searches, 2 deep fetches, ~20 file ops — efficient.
- [2026-06-08 query] GEO slot capacity: partial gap — wiki had Kessler/LEO coverage but no GEO-specific figures; fetched 4 web sources; key finding: GEO constrained by ITU frequency coordination (~1,800 slots) not collision physics; 580 active satellites vs ~1,800 capacity; resolved open question in max-gw-capacity page.

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

- [2026-06-08 ingest] Novaspace: read index + 0 existing pages (search not needed; all relevant pages known from context). Used 1 fetch + 1 PDF extract. Well within budget.
- [2026-06-08 ingest] Starcloud: company white paper directly contradicts Novaspace cost model — key variable is launch cost ($30/kg vs $1,000/kg). SSO orbit selection in 2024 paper pre-empts the battery degradation problem identified in the 2026 arXiv paper; connection flagged in both pages.
- [2026-06-08 ingest] Both ingests updated 4 shared pages (financial-viability, launch-cost-economics, spacex entity, starcloud entity) — managing shared page updates sequentially avoided conflicts.
- [2026-06-08 ingest] NTRS paper: read index + 2 existing pages (orbital-capacity-limits, kessler-syndrome-wikipedia) — within 8-read budget. curl download worked directly; no Playwright needed for NTRS PDF URLs.
- [2026-06-08 ingest] SSO high-flux ridge finding (supplementary inclinations) is a new quantitative claim not in existing pages — surfaced in concept page update. No contradictions with existing claims.
