---
title: "Companies Working on Space-Based Data Centers — Landscape"
type: "synthesis"
sources:
  - "space-data-center-wikipedia.md"
  - "scientific-american-space-datacenters.md"
  - "orbital-startup-economics-register-2026.md"
  - "space-based-solar-power.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
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
- Open question: Whether TeraWave is a space data center constellation or a
  communications infrastructure play — the distinction is not yet clear from
  available sources.

## National Programs

### China — Xingshidai

- Operating space data center constellation (status: active)
- No further details confirmed in wiki sources [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

### EU — ASCEND / Edge Aerospace

- Edge Aerospace selected by ESA under the Space Cloud program (May 2026) for an
  "orbital data center" feasibility study [[wiki/sources/space-data-center-wikipedia.md]] *(other)*

## Other Notable Entries

| Entity | Approach | Status |
|---|---|---|
| Lonestar | Lunar surface data backup | Hardware deployed March 2025 |
| University of Pennsylvania | Tether-based architecture | Research; presented AIAA SciTech Jan 2026 |
| OpenAI | Interest in space infrastructure | Referenced, no details confirmed |

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

- What specifically is Xingshidai running, and at what scale?
- Has Starcloud generated revenue from its H100-in-orbit satellite?
- Is Blue Origin's TeraWave genuinely a compute constellation or a communications
  infrastructure play?
- What is OpenAI's actual involvement, if any?
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
