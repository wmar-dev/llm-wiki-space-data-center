---
title: "Are There More Concepts We Should Research?"
type: "synthesis"
sources:
  - "arxiv-2302-08952-leo-edge-failures.md"
  - "arxiv-2603-04372-leo-battery-aging.md"
  - "nasa-ntrs-iss-battery-dod.md"
  - "on-orbit-satellite-servicing.md"
  - "on-orbit-servicing-refueling-2026.md"
  - "faa-part-450-licensing-2026.md"
  - "caltech-sspp-mission-lessons.md"
  - "space-data-center-wikipedia.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Are There More Concepts We Should Research?

## Current Concept Coverage

The wiki has four concept pages:

| Concept | Coverage | Status |
|---|---|---|
| [[wiki/concepts/thermal-management.md]] | Radiative cooling fundamentals, 450 W/m² limit, area-to-power scaling | Current |
| [[wiki/concepts/launch-cost-economics.md]] | Cost equation, historical trend, $50–200/kg thresholds | Draft |
| [[wiki/concepts/orbital-capacity-limits.md]] | Kessler syndrome regimes, ORDEM 3.0 flux, critical density bands | Current |
| [[wiki/concepts/space-datacenter-component-lifetimes.md]] | TJ solar cells, Li-ion cycles, rad-hard electronics, radiator degradation | Current |

These four cover the thermal, economic, debris, and durability constraints well. Several major concept areas remain without a dedicated page despite having multi-source coverage already in the wiki.

---

## High Priority: Concept Pages Warranted by Existing Sources

### 1. Radiation Environment and Electronics Effects (SEU/TID)

**Why missing:** Radiation is cited as a core risk in [[wiki/synthesis/space-datacenter-key-risks-analysis.md]] and drives the "rad-hard vs. COTS" tradeoff that dominates the hardware refresh penalty discussion. No concept page distills the fundamentals.

**Content already in wiki:**
- [[wiki/sources/arxiv-2302-08952-leo-edge-failures.md]] — radiation taxonomy; quantitative shielding data referenced (PDF not fully extracted)
- [[wiki/concepts/space-datacenter-component-lifetimes.md]] — rad-hard electronics rated 15+ years vs COTS 5–10 years
- [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]] — COTS chips in LEO face 2-3 generation lag plus radiation-induced failure

**What the concept page should cover:**
- Three radiation damage mechanisms: Single Event Upsets (SEU), Total Ionizing Dose (TID), displacement damage
- LEO flux levels at different altitudes (South Atlantic Anomaly hot zone)
- Shielding mass tradeoffs (each 2× shielding reduction = 2–5 g/cm² Al equivalent, non-trivial launch cost)
- Rad-hard processors (heritage flight computers, ~10-year-old node) vs. COTS (modern nodes, higher SEU susceptibility)
- Implication: data centers using commercial GPUs face real-time error correction overhead and finite unshielded lifetime

### 2. Eclipse Cycling and Power Budget Management

**Why missing:** Multiple sources discuss battery degradation and eclipse fractions individually, but no concept page synthesizes the central engineering constraint: a data center in LEO must throttle compute to zero (or near-zero) during ~36% of each 90-minute orbit.

**Content already in wiki:**
- [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]] — physics-informed battery degradation model; workload directly drives cycle depth
- [[wiki/sources/nasa-ntrs-iss-battery-dod.md]] — ISS 35% DoD limit; Li-ion transition details
- [[wiki/sources/orbital-systems-power-budget-2025.md]] — solar + thermal sizing; eclipse battery sizing math
- [[wiki/entities/starcloud.md]] — SSO dawn-dusk orbit eliminates eclipse (near-constant solar illumination), which is why Starcloud chose it

**What the concept page should cover:**
- Eclipse period formula: ~34–38 min dark per 90-min LEO orbit at 550 km (≈ 37–42% eclipse)
- Dawn-dusk SSO: sun-synchronous orbit at 97.6° inclination tracks the terminator, reducing eclipse to near-zero at cost of coverage latitude
- Battery sizing: must store enough energy to sustain minimum compute load through eclipse window
- Compute throttling: GPU clusters cannot run at rated TDP through eclipse without oversized batteries; Inference: a 1 MW steady-state facility needs ~3–4× the battery capacity of the solar array
- DoD constraint: deep discharge (>35%) accelerates degradation; 5–7 year battery life at safe DoD
- SSO trade: eliminates eclipse but constrains orbital inclination, limiting coverage to polar/high-latitude ground stations

### 3. Space Regulatory and Spectrum Access Landscape

**Why partially missing:** The FAA Part 450 source and ITU coordination content appear across several pages, but no concept page maps the full multi-agency regulatory stack a space data center operator faces.

**Content already in wiki:**
- [[wiki/sources/faa-part-450-licensing-2026.md]] — 14 licenses issued since 2021; 180-day processing; US already congested Jan 2025
- [[wiki/sources/geo-orbital-slots-capacity.md]] — ITU 2° spacing rule, coordination process
- [[wiki/synthesis/launch-site-capacity-space-datacenter.md]] — regulatory throughput is binding constraint, not physical site capacity
- [[wiki/sources/bongers-2026-space-economics-survey.md]] — orbit governance, open-access vs. optimal management

**What the concept page should cover:**
- FAA Part 450: launch vehicle licensing (180-day target, historically slow)
- FCC Satellite Broadband: spectrum allocation for downlink (Ka/V-band, optical)
- ITU coordination: mandatory for frequency use; GEO slots require filing 7 years ahead
- ITAR/EAR export controls: US-origin radiation-hardened parts and encryption subject to export licensing; affects international customer base
- National orbital object registries: operators must register satellites with UN OOSA
- Implication: a startup planning first launch in 2027 should be in FCC + ITU filings NOW

---

## Medium Priority: Concepts That Need New Sources

### 4. Space-Qualified vs. COTS Computing Hardware

**Why a gap:** The central compute question for a space data center is whether to use purpose-built radiation-hardened processors (low performance, high cost, proven) or COTS GPUs with error correction (high performance, unproven radiation tolerance). No source in the wiki directly addresses this tradeoff.

**Research needed:**
- Rad-hard processor performance benchmarks (e.g., BAE RAD750, SpaceVPX)
- COTS GPU radiation testing results (NVIDIA Jetson, H100 in simulated flux environments)
- Error correction overhead (ECC scrubbing cycles reduce effective throughput)
- Fault-tolerant computing architectures for orbit (TMR, lockstep)

**Suggested query/ingest:** Search for academic papers on COTS GPU radiation testing in LEO, or SpaceVPX standards documents.

### 5. Data Downlink Throughput as a Constraint

**Why a genuine gap:** No page directly addresses the fundamental bottleneck of getting computation results back to Earth. A space data center that trains an AI model or processes sensor data must still downlink terabytes of results. Current satellite downlink rates (even with optical terminals) may constrain throughput more than compute.

**Research needed:**
- Ka-band and V-band throughput per satellite (typical: 1–10 Gbps per sat)
- Optical inter-satellite link (ISL) + ground station optical throughput (LCRD: 1.2 Gbps; future: 10–100 Gbps)
- Contact time per pass: LEO sat over a ground station for ~8–12 min per orbit
- Implication: a 1 MW data center computing at terrestrial efficiency could generate ~10 TB/day of output but downlink capacity at 1 Gbps over 3 passes/day = ~16 GB/day; 600× gap
- Open question: Does this make space compute viable only for workloads where computation compresses output dramatically (e.g., Earth observation: raw imagery → classification result)?

### 6. On-Orbit Servicing as a Hardware Refresh Enabler

**Why medium priority:** Two sources exist. The concept is strategically important for the hardware refresh penalty problem, but the TRL gap is severe enough that it may not close within the investment horizon.

**Content already in wiki:**
- [[wiki/sources/on-orbit-satellite-servicing.md]] — MEV-1/2 life extension (GEO), Orbital Express; module swap not yet demonstrated
- [[wiki/sources/on-orbit-servicing-refueling-2026.md]] — Provisioner, Orbit Fab; OSAM-1 cancellation; propellant depots operational

**What the concept page should cover:**
- Current TRL: propellant transfer demonstrated (Orbit Fab); component swap demonstrated (Orbital Express, 2007); GPU module swap — not demonstrated
- Key gap: standardized mechanical/electrical interfaces (ESPA ring-equivalent for compute modules not standardized)
- Timeline: Inference: modular GPU swap in LEO is 10+ years from commercial viability
- Strategic implication: servicing does not resolve hardware refresh penalty within any current startup's investment horizon

---

## Lower Priority Research Directions

| Topic | Why Interesting | Why Lower Priority |
|---|---|---|
| Space insurance and liability | Satellite insurance rates, collision liability under Outer Space Treaty | No sources; niche; not a make-or-break factor |
| Power beaming (MAPLE/microwave) | Alternative to downlink; Caltech SSPP demonstrated laser WPT | Only ~kW-scale demonstrated; decades from MW viability |
| China Xingshidai deep dive | State-backed competitor; different economics | AdaSpace source ingested; incremental return |
| Orbital mechanics fundamentals | Eclipse fractions, coverage patterns, inclination tradeoffs | Already embedded in orbital regime synthesis |

---

## Recommended Research Sequence

1. **Write concept: Radiation Environment and SEU/TID** — sources already in wiki; high concept density
2. **Write concept: Eclipse Cycling and Power Budget** — sources already in wiki; central engineering constraint
3. **Research + ingest: Data Downlink Throughput** — genuine gap; needs 1–2 new sources on optical/RF downlink rates
4. **Research + ingest: COTS vs. Rad-Hard Computing** — genuine gap; needs GPU radiation testing sources
5. **Write concept: Regulatory Landscape** — partial sources in wiki; consolidation task
6. **Write concept: On-Orbit Servicing** — sources already in wiki; medium strategic value

Items 1–2 and 5–6 can be addressed with `/query` or directly writing concept pages from existing wiki content. Items 3–4 require `/ingest` of new sources first.
