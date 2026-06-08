---
title: "Companies Working on Space-Based Data Centers — Landscape"
type: "synthesis"
sources:
  - "space-data-center-wikipedia.md"
  - "scientific-american-space-datacenters.md"
  - "orbital-startup-economics-register-2026.md"
  - "space-based-solar-power.md"
  - "blue-origin-terawave-2026.md"
  - "adaspace-xingshidai-first-launch.md"
  - "starcloud-revenue-openai-orbital-data-centers.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-08"
---

# Companies Working on Space-Based Data Centers — Landscape

As of mid-2026, at least a dozen entities — from venture-backed startups to
hyperscalers to national programs — are actively pursuing orbital data center
concepts at varying levels of maturity.

## Venture-Backed Startups (Most Active)

### Starcloud

- **Backing**: Y Combinator
- **Status**: Hardware in orbit (November 2025) — 60 kg satellite with NVIDIA H100 GPU
- **Claim**: "First company to train an LLM in space" [[wiki/sources/space-data-center-wikipedia.md]] *(other)*
- **Target**: 5 GW orbital capacity by 2035, via ~88,000-satellite constellation
- **Additional**: Announced Bitcoin mining plans in orbit
- **Contested**: 10× carbon reduction claim contradicted by Saarland University study [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

Starcloud is the furthest along on hardware — the only entity confirmed to have
operational AI compute in orbit.

- **Business**: 18 customers on Kepler Communications network; two business models (on-orbit edge compute for other spacecraft, eventual terrestrial cloud competition) [[wiki/sources/starcloud-revenue-openai-orbital-data-centers.md]] *(news article)*
- **Revenue**: No public revenue figures disclosed; likely pre-revenue [[wiki/sources/starcloud-revenue-openai-orbital-data-centers.md]] *(inference)*
- **Funding**: $170M raised at ~$1.1B valuation [[wiki/sources/starcloud-revenue-openai-orbital-data-centers.md]] *(news article)*

### Orbital

- **Backing**: a16z (speedrun program)
- **CEO**: Euwyn Poon (formerly Spin electric scooters)
- **Planned chip**: Nvidia Space-1 Vera Rubin module
- **Power**: 100 kW per satellite ("the sweet spot" per CEO)
- **Timeline**: PoC flight 2027; full-scale satellite 2030
- **CEO's own assessment**: "The economics of launch don't quite work yet" — needs
  $10/kg launch cost vs. current ~$7,000/kg [[wiki/sources/orbital-startup-economics-register-2026.md]] *(news_article)*

### Cowboy Space Corporation (formerly Aetherflux)

- **Funding**: $50 million (+ US DoD Operational Energy Capability Improvement Fund)
- **Origin**: Pivoted from space-based solar power (laser beaming) to space data centers in December 2025; subsequently renamed [[wiki/sources/space-based-solar-power.md]] *(other)*
- **Architecture**: LEO constellation with infrared laser links and small ground stations (~5–10 m diameter)
- **Status**: Pre-hardware; concept phase post-pivot [[wiki/entities/aetherflux.md]]

## Big Tech

### Google — Project Suncatcher

- Solar-powered satellite constellation with AI chips
- Published feasibility study November 2025
- Requires launch costs below **$200/kg by 2035** for viability
- Demo mission targeting 2027 [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

### SpaceX

- Filed FCC plans in January 2026 for millions of satellites with data center
  functionality — integrating with the Starlink constellation [[wiki/sources/space-data-center-wikipedia.md]] *(other)*
- SpaceX is both a potential operator and the primary launch provider for all
  other space data center projects [[wiki/entities/spacex.md]]

## Aerospace Incumbents

### Blue Origin — TeraWave

- Unveiled a constellation of ~5,400 satellites for "high-throughput networking"
- Positioned as space infrastructure rather than explicitly as compute [[wiki/sources/space-data-center-wikipedia.md]] *(other)*
- **Resolved**: TeraWave is a communications infrastructure play, not a space data center. Blue Origin's FCC filing (Jan 2026) and press release describe it as an "advanced communications infrastructure" providing symmetrical data speeds up to 6 Tbps for enterprise, data center, and government connectivity [[wiki/sources/blue-origin-terawave-2026.md]] *(news article)*. The constellation (5,280 LEO + 128 MEO) serves as high-capacity backhaul between terrestrial data centers, not as orbital compute. Deployment begins Q4 2027.

## National Programs

### China — Xingshidai

- **Company**: AdaSpace (Beijing, founded 2020)
- **Status**: First 12 satellites launched (2025); 2,800-satellite constellation planned
- **AI capability**: Each satellite runs an 8 billion parameter AI model on-orbit [[wiki/sources/adaspace-xingshidai-first-launch.md]] *(news article)*
- **Inter-satellite**: 100 Gbps optical laser communication links [[wiki/sources/adaspace-xingshidai-first-launch.md]] *(news article)*
- **Bus platform**: XingShengLi-100; construction started end of 2023
- **Positioning**: Indigenous Chinese development (parallel to DeepSeek) for a "Global Space AI Computing Network"

Xingshidai is the only confirmed operational AI-in-orbit constellation beyond Starcloud's single-satellite demo.

### EU — ASCEND / Edge Aerospace

- Edge Aerospace selected by ESA under the Space Cloud program (May 2026) for an
  "orbital data center" feasibility study [[wiki/sources/space-data-center-wikipedia.md]] *(other)*

## Other Notable Entries

| Entity | Approach | Status |
|---|---|---|
| Lonestar | Lunar surface data backup | Hardware deployed March 2025 |
| University of Pennsylvania | Tether-based architecture | Research; presented AIAA SciTech Jan 2026 |
| OpenAI | Personal interest (Altman), no formal initiative | Referenced, no longer active early 2026 [[wiki/sources/starcloud-revenue-openai-orbital-data-centers.md]] |

## Maturity Comparison

| Company | Hardware in Orbit? | Revenue-Generating? | Economics Viable? |
|---|---|---|---|
| Starcloud | Yes (Nov 2025) | Unknown | Contested |
| Lonestar | Yes (Mar 2025) | Unknown | Niche |
| Google Suncatcher | No (demo 2027) | No | Requires $200/kg by 2035 |
| Orbital | No (PoC 2027) | No | Explicitly not yet (CEO) |
| Cowboy/Aetherflux | No | No | Pre-pivot; unclear |
| SpaceX | Filing stage | No | Depends on Starship |
| Blue Origin TeraWave | Announced | No | Unknown |
| China Xingshidai | Yes (operating) | Unknown | Unknown |

## Open Questions

- ~~What specifically is Xingshidai running, and at what scale?~~ *(resolved — 8B param AI models on 2,800-satellite Xingshidai constellation; first 12 launched)*
- ~~Has Starcloud generated revenue from its H100-in-orbit satellite?~~ *(resolved — no public revenue figures; 18 customers on Kepler; likely pre-revenue)*
- ~~Is Blue Origin's TeraWave genuinely a compute constellation or a communications infrastructure play?~~ *(resolved — communications infrastructure)*
- ~~What is OpenAI's actual involvement, if any?~~ *(resolved — Altman personal interest only; no formal initiative; no longer active early 2026)*
- Are there additional companies not yet covered (Lumen Orbit, others reported
  in trade press after mid-2026)?

## Related Pages

- [[wiki/entities/aetherflux.md]]
- [[wiki/entities/orbital.md]]
- [[wiki/entities/starcloud.md]]
- [[wiki/entities/spacex.md]]
- [[wiki/sources/scientific-american-space-datacenters.md]]
- [[wiki/sources/orbital-startup-economics-register-2026.md]]
- [[wiki/sources/space-data-center-wikipedia.md]]
