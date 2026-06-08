---
title: "Starcloud (Lumen Orbit): Why We Should Train AI in Space (Sep 2024)"
type: "source_summary"
sources:
  - "starcloud-white-paper.txt"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://starcloudinc.github.io/wp.pdf"
---

# Starcloud (Lumen Orbit): Why We Should Train AI in Space (Sep 2024)

**Publisher**: Lumen Orbit (renamed Starcloud in 2025)
**Authors**: Ezra Feilden PhD, Adi Oltean, Philip Johnston
**Source type**: industry_report *(company white paper — self-promotional; claims should be read with that lens)*
**Date**: September 2024

Starcloud's founding technical white paper making the engineering and economic case for GW-scale orbital data centers. Covers cost model, orbit selection, solar power, thermal management, network architecture, physical design, and maintenance.

---

## Cost Model

Starcloud claims a 40 MW space cluster is dramatically cheaper than its terrestrial equivalent over 10 years:

| Cost item | Terrestrial | Space |
|---|---|---|
| Energy (10 years @ $0.04/kWh) | $140M | $2M (solar array materials) |
| Launch | None | $5M (single launch, ~$30/kg assumed) |
| Cooling | $7M (chiller energy) | More efficient (higher ΔT in space) |
| Water | 1.7M tons | Not required |
| Enclosure (building/satellite bus) | Equivalent | Equivalent |
| Backup power supply | $20M | Not required (SSO orbit) |
| All other hardware | Equivalent | Equivalent |
| Radiation shielding | Not required | $1.2M |
| **Total** | **$167M** | **$8.2M** |

**20:1 cost advantage for space** under these assumptions.

Critical assumptions driving this result:
- Launch cost: ~$30/kg (next-gen fully reusable vehicle at $5M / 40 MW launch)
- Solar cell material cost: $0.03/W
- Effective energy cost in space: **~$0.002/kWh** (vs. $0.04–0.17/kWh terrestrial, depending on country)
- No battery backup needed (SSO orbit gives >95% solar illumination)

**Contradiction with Novaspace**: Novaspace's independent analysis (May 2026) finds space is **2.7× more expensive** than terrestrial even under optimistic assumptions using $1,000/kg launch — the inverse conclusion. The divergence is almost entirely the launch cost assumption: Novaspace uses $1,000/kg as "near future"; Starcloud assumes ~$30/kg. See [[wiki/sources/novaspace-orbital-data-centers-2026.md]].

---

## Orbit Selection: Dawn-Dusk Sun-Synchronous Orbit (SSO)

Starcloud's most significant design decision: choose SSO on the terminator line rather than standard LEO.

- The orbital plane precesses at one rotation per year, remaining approximately perpendicular to the sun year-round
- Result: **>95% solar capacity factor** — the spacecraft is in near-continuous illumination
- Eliminates the eclipse cycles of standard LEO (~36 min dark per 90-min orbit)
- Eliminates the battery storage requirement flagged as a risk in other analyses — see [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]]
- Eliminates thermal fatigue from repeated light/dark cycling

Inference: This orbit selection directly resolves the battery degradation problem identified in the arXiv 2026 physics-driven model. Whether Starcloud was aware of that specific work is unclear; the SSO approach appears in this earlier (2024) white paper.

---

## Solar Power

- Space solar capacity factor: **>95%** (vs. 24% median for US terrestrial solar; <10% in temperate Europe)
- Space peak irradiance ~40% higher than terrestrial (no atmospheric attenuation)
- → Same solar array generates **>5× the energy** in space vs. on Earth
- Solar cell material: **thin-film silicon, <25 μm thickness**, >1,000 W/kg power density
  - Can be folded/rolled for launch and deployed to very large areas
  - Anneals (heals) radiation damage at moderate temperatures — no cover-glass needed
  - Cost: ~$0.03/W (commercial scale)
- 5 GW data center requires **4 km × 4 km solar array** (assuming 90% fill factor, 22% BOL efficiency)
- Deployable structure design (Z-fold, roll-out, or picture-frame) is "a core area of development within Starcloud"

---

## Thermal Management

- Radiator area needed is roughly **<50% of solar array area** (1 m² at 20°C nets ~633 W rejection after sun absorption and Earth albedo)
- Radiators positioned in-line with solar arrays, one side exposed to sunlight
- Cooling loop: two-phase systems where practical to reduce mass flow
- Within compute modules: direct-to-chip liquid cooling or two-phase immersion cooling
- Modules may be pressurized with inert atmosphere or submerged in coolant (which also provides radiation shielding)
- No heat pumps required for baseline design; heat pumps could increase per-m² output dramatically (T⁴ benefit in Stefan-Boltzmann law)
- Thermal environment in SSO is extremely stable (beyond ~0.2% solar irradiance variation) — eliminates terrestrial need to provision for worst-case summer days

---

## Radiation

Starcloud argues the radiation risk is overstated for large-scale GW facilities:

- Shielding mass scales with container **surface area**; compute scales with container **volume** → larger containers = lower shielding overhead per unit compute
- Logic devices (GPUs) are inherently radiation-tolerant, especially for AI training workloads — supported by cited IEEE paper
- Storage and power delivery components are the more sensitive elements
- Coolant blocks themselves provide meaningful shielding — reducing additional mass needed
- SSO is relatively low radiation vs. higher orbits

Inference: This geometric argument applies specifically to large centralized modules — it does not help small satellite nodes in a decentralized constellation design.

---

## Physical Architecture and Scale

- 5 GW compute cluster: ~100 launches of compute modules + ~100 launches of solar/radiator modules
- Each launch: ~100 tons to SSO, carrying ~40 MW of compute (300 racks at 50% capacity, 120 kW/rack — equivalent to Nvidia GB200 NVL72)
- Launch vehicle: expects next-gen vehicles launching up to 3×/day → entire 5 GW cluster theoretically deployable in 2–3 months
- More realistic: modular gradual buildout around central hub; solar/radiator modules added incrementally
- Design uses two primary structure types → economies of scale in manufacturing

---

## Network Architecture

- Within cluster: tight daisy-chain network; all containers within a few hundred meters; high bisection bandwidth for AI training
- Uplink: laser-based connectivity to other constellations (Starlink, Kuiper, Kepler)
- Training data transport: **data shuttles** — small docking modules physically launched with petabytes/exabytes of training data (cites Amazon Snowcone to ISS as proof of concept)
- Speed of light in vacuum is 35% faster than in fiber → potential interconnect advantage for within-cluster communication

Open question: What is the round-trip latency for iterative training workflows requiring data uplink from Earth? The data shuttle concept solves bulk data delivery but not real-time feedback loops.

---

## Maintenance and Lifecycle

- Modular containers can be swapped without decommissioning the base infrastructure
- Old containers: re-entered in launcher payload bay, or designed to be fully demisable
- System degrades gracefully as containers fail (redundancy designed in at system level)
- Design lifetime: **~15 years** (matching ISS cooling/power delivery infrastructure lifespan)
- End-of-life: salvage (hardware and raw material recovery) or full demise in upper atmosphere
- Key unknowns on component life: ionizing radiation and thermal stress shorten some devices; cooler stable temps, no corrosive atmosphere may extend others (cites Microsoft Project Natick underwater DC as analogue)

---

## Related Pages

- [[wiki/entities/starcloud.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
- [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]]
- [[wiki/sources/novaspace-orbital-data-centers-2026.md]]
