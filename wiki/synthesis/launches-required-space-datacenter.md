---
title: "How Many Launches Would It Take to Put a Data Center in Space?"
type: "synthesis"
sources:
  - "orbital-systems-power-budget-2025.txt"
  - "spacex-launch-cost-analysis.md"
  - "orbital-startup-economics-register-2026.md"
  - "space-data-center-wikipedia.md"
  - "nasa-irosa-solar-arrays.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# How Many Launches Would It Take to Put a Data Center in Space?

The answer depends entirely on the scale of the facility. There is a wide range
from a single-satellite demo to a gigawatt-class constellation, each requiring
a very different number of launches.

## Key Parameters

### Launch Vehicle Payload Capacity

| Vehicle | Payload to LEO | $/kg (current) | $/kg (target) |
|---|---|---|---|
| Falcon 9 (reusable) | ~23 t | ~$1,500 | — |
| Falcon Heavy (reusable) | ~64 t | ~$1,500 | — |
| Starship (full reuse, target) | ~150–200 t | ~$7,000 now | ~$10–100 |

[[wiki/concepts/launch-cost-economics.md]], [[wiki/synthesis/spacex-starship-cost-breakdown.md]]

### Physical Scale of a Space Data Center

A reference **1 MW orbital facility** requires
[[wiki/sources/orbital-systems-power-budget-2025.md]] *(industry_report)*:
- Solar panels: **~3,600 m²** (at 280 W/m² output, 20% efficiency, 1,400 W/m² LEO input)
- Thermal radiators: **~2,200 m²** (at 450 W/m², 300 K)

Both scale linearly with power [[wiki/concepts/thermal-management.md]].

## Scenario 1: Single-Satellite Demo (~60–100 kW)

Real-world examples from the wiki:
- **Starcloud**: 60 kg satellite with NVIDIA H100 GPU (deployed November 2025) [[wiki/sources/space-data-center-wikipedia.md]] *(other)*
- **Orbital**: 100 kW satellite described as "roughly four refrigerators" in size [[wiki/sources/orbital-startup-economics-register-2026.md]] *(news_article)*; Orbital's solar array is "~two halves of a tennis court" (~130 m²)

For a demo-scale satellite:
- **Launch count: 1** — a Falcon 9 rideshare or dedicated small-lift launch is sufficient
- The Starcloud 60 kg satellite could share a launch with dozens of other payloads

## Scenario 2: Single 1 MW Operational Node

This is the reference scale from the industry report.

**Mass estimation** (Inference — wiki provides areas, not masses; mass figures use
published solar array and radiator mass density ranges):

| Component | Area / Count | Estimated Mass |
|---|---|---|
| Solar arrays (iROSA-class, ~40–50 W/kg) | 3,600 m² | **~20,000–25,000 kg** |
| Thermal radiators (~5–15 kg/m²) | 2,200 m² | **~11,000–33,000 kg** |
| Server racks / compute / storage | — | ~5,000–15,000 kg |
| Bus structure, propulsion, batteries | — | ~5,000–15,000 kg |
| **Total estimated** | | **~41,000–88,000 kg (41–88 t)** |

The iROSA benchmark provides a partial anchor: 6 iROSA panels deliver >250 kW to
the ISS [[wiki/sources/nasa-irosa-solar-arrays.md]], so 1 MW would require ~24 iROSA
panels. If each panel masses ~700–1,500 kg, solar arrays alone total ~17,000–36,000 kg.

**Launch count at 1 MW:**

| Vehicle | Payload (t) | Estimated Launches |
|---|---|---|
| Falcon 9 (~23 t) | 23 | **2–4 launches** |
| Falcon Heavy (~64 t) | 64 | **1–2 launches** |
| Starship (~150–200 t) | 150–200 | **1 launch** |

Inference: A 1 MW facility fits within 1–2 Starship launches or 2–4 Falcon Heavy
launches, assuming a modular design that can be assembled in orbit. Monolithic
deployment of 88 tons requires Starship.

## Scenario 3: 100 MW Commercial Data Center

Scale up linearly from the 1 MW reference:
- Solar panels: ~360,000 m²
- Radiators: ~220,000 m²
- Estimated total mass: **~4,000–8,800 t**

| Vehicle | Estimated Launches |
|---|---|
| Falcon 9 | **175–385 launches** |
| Starship (150 t) | **27–59 launches** |

At current Starship cadence (projected dozens of flights/year), a 100 MW facility
would require years of dedicated launch capacity.

## Scenario 4: Gigawatt-Scale Constellation (Starcloud 5 GW Target)

Starcloud projects **~88,000 satellites** for 5 GW capacity by 2035
[[wiki/sources/space-data-center-wikipedia.md]] *(other)*. At 60 kg per satellite
(the current demo scale):

- Total mass: 88,000 × 60 kg = **~5,300 t**
- Starship launches at 150 t payload: **~36 launches**

However, operational 57 kW satellites (5 GW / 88,000) would be substantially
heavier than the 60 kg H100 demo. At 300–1,000 kg per operational satellite:
- Total mass: 26,000–88,000 t
- Starship launches: **175–590 launches**

Inference: A full 5 GW constellation is a decade-scale deployment program requiring
sustained Starship production and flight rates — not achievable with current launch
infrastructure.

## Launch Cost at Each Scale

At current $7,000/kg (Orbital CEO figure) [[wiki/sources/orbital-startup-economics-register-2026.md]]:

| Scale | Est. Mass | Launch Cost Now | Launch Cost at $10/kg |
|---|---|---|---|
| 60 kg demo | 60 kg | $420K | $600 |
| 1 MW node | ~65 t | **~$455M** | ~$650K |
| 100 MW facility | ~6,400 t | **~$45B** | ~$64M |
| 5 GW constellation | ~50,000 t | **~$350B** | ~$500M |

The 1 MW node at current costs (~$455M just to launch) confirms the CEO's
assessment that "the economics of launch don't quite work yet"
[[wiki/sources/orbital-startup-economics-register-2026.md]] *(news_article)*.

## Open Questions

- What is the actual wet mass of the Orbital 100 kW satellite? The "four
  refrigerators" description gives size but not mass; no source in the wiki
  provides this figure.
- Can a 1 MW data center satellite be designed as a monolithic structure that
  survives launch loads, or does it require orbital assembly?
- At what Starship reuse cadence does the launch supply to support gigawatt-scale
  constellations become the binding constraint vs. satellite manufacturing rate?

## Related Pages

- [[wiki/sources/orbital-systems-power-budget-2025.md]]
- [[wiki/synthesis/spacex-starship-cost-breakdown.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/sources/orbital-startup-economics-register-2026.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
- [[wiki/sources/nasa-irosa-solar-arrays.md]]
