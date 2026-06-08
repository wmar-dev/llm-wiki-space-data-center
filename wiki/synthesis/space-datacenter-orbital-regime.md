---
title: "What Orbit Would Space Data Centers Be Put In?"
type: "synthesis"
sources:
  - "orbital-systems-power-budget-2025.md"
  - "space-based-solar-power.md"
  - "aetherflux.md"
  - "launch-cost-economics.md"
  - "kessler-syndrome-wikipedia.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# What Orbit Would Space Data Centers Be Put In?

**Query**: What orbit would space data centers be put in?

## Primary Candidate: LEO (~550 km)

The existing wiki analysis consistently assumes **Low Earth Orbit** for space data centers:

- **Power budget**: The 1 MW reference facility is sized for LEO conditions: 1.4 kW/m² solar input, ~36-minute eclipses per 90-minute orbit [[wiki/sources/orbital-systems-power-budget-2025.md]] *(industry_report)*
- **Aetherflux precedent**: The only well-funded company to pivot toward orbital data centers (Dec 2025) was building a LEO laser constellation [[wiki/entities/aetherflux.md]] — their data center architecture inherits this LEO design
- **Launch economics**: Falcon Heavy delivers to LEO at ~$1,500/kg vs ~$2,000/kg to GEO [[wiki/concepts/launch-cost-economics.md]]. The gap will grow as Starship targets $10–100/kg primarily to LEO.
- **Latency**: LEO round-trip latency (~5–25 ms) is compatible with real-time cloud and edge computing. GEO (~500 ms) would exclude most commercial workloads.
- **Debris mitigation**: Lower LEO orbits (especially <600 km) benefit from atmospheric drag that deorbits failed satellites and debris within ~5 years [[wiki/sources/kessler-syndrome-wikipedia.md]] *(other)* — this is the same strategy Starlink uses at 550 km.

### LEO Challenges

- **Power intermittency**: 36-minute eclipses require battery/fuel cell storage, adding mass and cycling degradation [[wiki/sources/orbital-systems-power-budget-2025.md]] *(industry_report)*
- **Debris density**: LEO has 85% of tracked space debris [[wiki/sources/kessler-syndrome-wikipedia.md]]; the 900–1,000 km band is already past critical density
- **Orbital maintenance**: Station-keeping and collision-avoidance maneuvers consume propellant

## Secondary Consideration: GEO

GEO is discussed primarily in the context of economic **thresholds** ($100–200/kg to GEO cited as viability target [[wiki/sources/space-based-solar-power.md]]) and for **SBSP heritage** (China CAST's 200-tonne megawatt station planned for GEO by 2035 [[wiki/sources/space-based-solar-power.md]]).

Note: GEO offers continuous sunlight (no eclipses) and stable positioning over a single region. However, the high latency (~500 ms) makes it unsuitable for latency-sensitive compute workloads. The economic viability threshold is also higher ($100–200/kg to GEO vs the $10–100/kg target to LEO).

## Summary

| Factor | LEO (~550 km) | GEO (35,786 km) |
|--------|---------------|-----------------|
| Round-trip latency | ~5–25 ms | ~500 ms |
| Launch cost (Falcon Heavy) | ~$1,500/kg | ~$2,000/kg |
| Eclipse | ~36 min/90 min | None |
| Natural debris cleaning | Years (drag) | Millennia |
| Coverage | Global, moving | Fixed region |
| Wiki consensus | Primary candidate | Secondary / threshold reference |

Inference: The first generation of orbital data centers will likely be deployed in **LEO around 550 km**, mirroring the Starlink constellation model. GEO may host specialized, high-latency-tolerant facilities at a later stage if launch costs to GEO fall sufficiently.

## Related pages

- [[wiki/sources/orbital-systems-power-budget-2025.md]]
- [[wiki/entities/aetherflux.md]]
- [[wiki/sources/space-based-solar-power.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/sources/kessler-syndrome-wikipedia.md]]
