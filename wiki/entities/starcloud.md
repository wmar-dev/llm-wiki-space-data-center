---
title: "Starcloud"
type: "entity"
sources:
  - "scientific-american-space-datacenters.md"
  - "starcloud-white-paper.txt"
status: "draft"
created: "2026-06-07"
last_updated: "2026-06-08"
---

# Starcloud

**Type**: Company
**Sector**: Space data centers / orbital compute

**Funding**: Y Combinator-backed

## Overview

Starcloud is a Y Combinator-backed startup that deployed a 60 kg satellite equipped
with an NVIDIA H100 GPU in November 2025 — claiming to be the "first company to
train an LLM in space." It projects building a 5 GW orbital data center constellation
of ~88,000 satellites by 2035, and has announced plans for Bitcoin mining in orbit.
[[wiki/sources/space-data-center-wikipedia.md]] *(other)*

The company claims orbital solar-powered data centers produce 10× lower carbon
emissions than land-based facilities powered by natural gas generators.
[[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

## Contested Claim

The 10× carbon reduction claim is **contested** by the Saarland University "Dirty Bits in Low-Earth Orbit" paper, which found orbital data centers could generate an order of magnitude *greater* emissions than terrestrial facilities when accounting for rocket launches and atmospheric reentry (including ozone-depleting pollutants). — [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

Status of carbon claim: `contested` pending review of the Saarland University paper.

## Technical Design (from company white paper, Sep 2024)

The following details are sourced from Starcloud's own founding white paper — read with a promotional lens. [[wiki/sources/starcloud-white-paper-2024.md]] *(industry_report)*

### Orbit: Dawn-Dusk Sun-Synchronous Orbit (SSO)

Starcloud's primary design decision is orbit selection. A dawn-dusk SSO tracks the terminator line (Earth's day/night boundary), giving the spacecraft near-continuous solar illumination (>95% capacity factor). This eliminates:

- Eclipse-period battery requirements — directly addressing the battery degradation risk modeled in [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]]
- Thermal fatigue from repeated light/dark cycling
- The need for backup power systems

This is the only LEO orbit with this property.

### Cost Model (40 MW cluster, 10 years)

| Cost item | Terrestrial | Space |
| --- | --- | --- |
| Energy | $140M | $2M (solar array materials) |
| Launch | — | $5M (~$30/kg assumed) |
| Cooling | $7M | More efficient (higher ΔT) |
| Backup power | $20M | Not required (SSO) |
| Radiation shielding | — | $1.2M |
| **Total** | **$167M** | **$8.2M** |

Key assumption: launch at ~$30/kg (next-gen fully reusable). Effective energy cost: ~$0.002/kWh vs. $0.04–0.17/kWh terrestrial.

**This 20:1 space advantage conflicts directly with Novaspace's independent finding** (space is 2.7× more expensive even optimistically, at $1,000/kg launch). See [[wiki/sources/novaspace-orbital-data-centers-2026.md]].

### Physical Scale (5 GW design)

- Solar array: **4 km × 4 km** using thin-film silicon cells (<25 μm, >1,000 W/kg power density)
- Radiator area: roughly <50% of solar array area (~633 W/m² net at 20°C)
- ~100 launches of compute modules + ~100 launches of solar/radiator modules
- Each launch: ~40 MW of compute (300 racks at 50% capacity, 120 kW/rack — Nvidia GB200 NVL72 equivalent)

### Radiation Approach

Geometric scaling argument: shielding mass scales with container surface area; compute scales with volume. Larger containers = proportionally less shielding overhead. Logic devices (GPUs) are inherently more radiation-tolerant than storage. Coolant blocks provide supplemental shielding.

### Data Transport

Proposes **data shuttles** — small docking modules physically launched with petabytes/exabytes of training data. Cites Amazon Snowcone on ISS as proof of concept. Intended to solve the data uplink bottleneck for large training runs.

Open question: What is the latency impact on iterative training workflows requiring real-time data feedback from Earth?

### Lifecycle

Design lifetime ~15 years (matching ISS cooling/power delivery lifespan). Modular container swaps enable hardware refresh. End-of-life: salvage or full atmospheric demise.

## Related Pages

- [[wiki/sources/starcloud-white-paper-2024.md]]
- [[wiki/sources/scientific-american-space-datacenters.md]]
- [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]]
- [[wiki/sources/novaspace-orbital-data-centers-2026.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
