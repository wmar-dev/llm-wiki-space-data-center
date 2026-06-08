---
title: "Novaspace: Orbital Data Centers White Paper (May 2026)"
type: "source_summary"
sources:
  - "novaspace-orbital-data-centers-white-paper.txt"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://nova.space/wp-content/uploads/2026/05/Novaspace_Orbital-Data-Centers_White-Paper.pdf"
---

# Novaspace: Orbital Data Centers White Paper (May 2026)

**Publisher**: Novaspace (global space consulting and market intelligence firm, 40-year legacy, 1,200+ clients across 60 countries)
**Authors**: Carla Filotico, Maxime Puteaux, Jean-Loup Rondeau, Felix Rottmann, Lucas Pleney, Ivan Iushchenko, Claire Fortin
**Source type**: industry_report (neutral third-party consultancy — not a company promoting its own concept)
**Date**: May 2026

Novaspace's first dedicated white paper on orbital data centers. Covers rationale, use case maturity, architectural options, cost modeling, building blocks, competitive landscape, and outlook.

---

## Cost Analysis

Space data centers for AI training and inference are **not cost-competitive** with terrestrial alternatives today, even under optimistic assumptions.

| Scenario | Launch cost | Satellite cost | 1 GW DC / 5 yr |
|---|---|---|---|
| Terrestrial reference | — | — | $17 Bn |
| Space (today) | ~$1,000/kg | $25/W ($2.5M) | $46 Bn |
| Space (near future) | ~$150/kg | $10/W ($1M) | ~$14 Bn (approaching parity) |

The $46 Bn space figure assumes a constellation of **10,000 satellites at 1.5 t each**. The bulk of cost is satellite manufacturing; launch is the second-largest driver. After 5 years, the constellation requires full replenishment.

Note: This model puts space at nearly **3× more expensive** than terrestrial even under optimistic "near future" assumptions — directly contradicting Starcloud's own cost model. See [[wiki/sources/starcloud-white-paper-2024.md]] for the conflicting claim; the divergence is almost entirely explained by launch cost assumptions ($150/kg vs. Starcloud's assumed ~$30/kg).

---

## Use Case Maturity

| Use case | Maturity | Orbital value | Notes |
|---|---|---|---|
| Earth Observation (imagery processing) | Very high | Very high | Latency reduction, limited downlink, sensor proximity |
| Defense (ISR, sovereign compute) | High | High | Mission-critical willingness to pay; clearest near-term entry |
| Connectivity (backbone compression) | Medium | Medium | Depends on constellation scale and launch economics |
| AI compute (GPU-as-a-service, inference) | Low | Very high | Many unsolved technical and commercial problems |
| Niche (robotic exploration, crypto mining) | Very low | Medium | Speculative |

Key finding: AI compute has the highest potential orbital value but the lowest maturity — explicitly described as having "many technical problems and open commercial questions." Defense is the most credible near-term revenue source.

---

## Architecture Tradeoffs

### Decentralized (LEO constellation of nodes)
- Technically feasible today using mass manufacturing
- High fault tolerance, proximity to users (lower latency)
- Requires complex distributed computing orchestration
- Must refresh entire constellation each hardware generation (no in-orbit upgrades)
- Lower marginal cost; phased investment profile
- Novaspace verdict: **feasibility in line with existing technology**

### Centralized (single large station or cluster, modular)
- Higher compute density, simpler orchestration
- Modular add/remove in orbit; >10-year base infrastructure lifespan theoretically
- In-orbit assembly and maintenance remain **unproven** — requires in-orbit servicers
- Single point of failure; higher manufacturing and launch requirements
- Novaspace verdict: **"severity of disadvantages outweigh benefits" in current state**

---

## Required Building Blocks

Novaspace classifies enabling technologies by importance and readiness:

| Building block | Readiness | Cost impact |
|---|---|---|
| Satellite subsystems (overall) | — | Largest cost bucket |
| Radiation-hardened components | Development needed | Critical challenge |
| Dedicated processing units (GPUs in space) | Near-ready | Important |
| Large-scale manufacturing | Available | Key differentiator |
| Cooling systems | **Least mature** | Critical enabler |
| Large solar arrays + power management | Available | Manageable |
| Reusable/super-heavy launch vehicles | Development needed | 2nd-largest cost |
| Ground stations | Fully mature | Minor |
| In-orbit servicing | Development needed | Optional long-term |
| Optical ground stations + QKD | Near-ready | Optional |

Cooling is explicitly flagged as the **least mature** critical enabler — consistent with [[wiki/synthesis/space-datacenter-key-risks-analysis.md]].

---

## Competitive Landscape (13+ Players as of May 2026)

| Player | Use case | Planned scale | Status |
|---|---|---|---|
| SpaceX | AI compute | 1,000,000 sats | FCC filing Feb 2026 |
| Blue Origin | AI compute | 51,600 sats | FCC filing Mar 2026 |
| Starcloud | AI compute | 88,000 sats | 1 sat launched 2025 |
| Orbital (a16z) | AI compute | "network of sats" | 2 demo sats planned 2027 |
| Amazon | AI compute | TBD | Exploratory |
| Kepler | Satcom data relay | TBD | 10 sats launched Jan 2026 |
| Space Compass | EO data relay + compute | TBD | Announced Mar 2026 |
| Star.Vision | EO data + AI compute | 2,800 sats | 12 launched May 2025 |
| Xingshidai (CASC) | EO data compute | 258 OSE sats by 2032 | 2 sats May 2026 |
| Sophia Space / Axiom | AI compute | TBD | Feasibility study Apr 2026 |

**Key structural observations:**
- SpaceX is the **only near-fully-vertically-integrated player** outside CASC (China)
- Most players are structurally dependent on SpaceX for launch — even though SpaceX is a direct competitor
- NVIDIA is the de facto chip supplier for most players — a second structural dependency
- OpenAI reportedly explored investing in Stoke Space (launch startup)
- Only a few projects have internal workloads; most must attract external customers to be viable

---

## Rationale vs. Counterarguments

Novaspace's analysis is notably balanced — it presents the case but also the rebuttals:

| Space advantage claim | Novaspace counterargument |
|---|---|
| No land use / real estate | LEO is becoming congested; impacts astronomy |
| Zero CO₂ during operations | Launch and manufacturing emissions offset operational benefit |
| No freshwater cooling | Terrestrial efficiency gains (hardware refresh) can reduce water use |
| Avoids permitting bottlenecks | True, but space has its own regulatory complexity |

---

## Outlook Factors

**Accelerators** (make space DCs more viable): Space-based solar power; autonomous space robotics; fully reusable launch vehicles; AI demand explosion; environmental/regulatory pressure; human presence on Moon/Mars.

**Inhibitors** (undercut the thesis): Breakthroughs in AI efficiency; energy limits alleviated (renewables, fusion); success of competing DC concepts (edge, floating, underwater); AGI risks leading to AI slowdown; Kessler syndrome.

---

## Contradiction Note

Novaspace's cost model (space 2.7× more expensive even optimistically) contradicts Starcloud's white paper claim (space 20× cheaper). See [[wiki/sources/starcloud-white-paper-2024.md]]. The gap is driven almost entirely by launch cost assumptions — Novaspace models $1,000/kg as "near future" while Starcloud assumes ~$30/kg (fully reusable, next-gen). Both conclusions are internally consistent with their assumptions; the question is which launch cost trajectory materializes.

## Related Pages

- [[wiki/entities/spacex.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
- [[wiki/sources/starcloud-white-paper-2024.md]]
