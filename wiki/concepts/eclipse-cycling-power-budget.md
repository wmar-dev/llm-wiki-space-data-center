---
title: "Eclipse Cycling and Power Budget Management"
type: "concept"
sources:
  - "arxiv-2603-04372-leo-battery-aging.md"
  - "nasa-ntrs-iss-battery-dod.md"
  - "orbital-systems-power-budget-2025.txt"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Eclipse Cycling and Power Budget Management

## The Fundamental Constraint

A satellite in circular LEO at 550 km altitude completes one orbit every ~90 minutes. For a significant fraction of each orbit, the satellite passes through Earth's shadow (eclipse) and receives no solar power. Any onboard compute load must either be suspended, throttled to battery capacity, or bridged by batteries sized for the eclipse duration.

## Eclipse Duration by Orbital Regime

| Orbit | Altitude | Period | Max eclipse | Eclipse fraction |
|---|---|---|---|---|
| Standard LEO | 400–600 km | 90–96 min | ~34–38 min | ~37–40% |
| ISS | 408 km | 92 min | ~36 min | ~38% |
| Starlink | 550 km | 96 min | ~36 min | ~37% |
| SSO dawn-dusk | 550 km | 96 min | ~0–2 min | ~0–2% |
| GEO | 35,786 km | 24 hr | Up to 72 min/day | ~5% (seasonal) |

**Eclipse varies with beta angle** (Sun-orbit plane angle): at high beta angles the orbit stays mostly in sunlight; at low beta angles eclipse is maximum. Standard LEO planning assumes worst-case ~36–38 min eclipse per orbit.

## Battery DoD Constraints

The International Space Station's operational experience provides the authoritative real-world constraint: ISS Ni-H2 batteries are designed for a **maximum 35% depth of discharge (DoD)** during normal LEO operation. The remaining 65% of capacity is held in reserve to extend cycle life across multi-year missions. *(NASA NTRS 20160012048)*

**Why DoD matters:** Cycling batteries beyond ~35% DoD dramatically accelerates electrochemical degradation. This is not a conservative engineering margin — it reflects the physical chemistry of repeated deep cycling in a ~16-orbit-per-day LEO environment.

**Practical sizing consequence:** A battery rated at 100 kWh usable for eclipse bridging must have a nominal capacity of ~154 kWh to stay within the 35% DoD limit. This inflates mass, volume, and cost by ~3×.

## Compute Workloads Drive Battery Aging

A 2026 preprint (arxiv:2603.04372) establishes the **first physics-informed model linking computational task execution directly to battery degradation**. Key findings:

- Standard Depth of Discharge metrics fail to capture the nonlinear, workload-dependent nature of battery aging
- Heavy compute loads during eclipse drawdown increase not just cycle depth but the rate of irreversible degradation
- Optimal scheduling: **prioritize direct solar energy use** under abundant-solar conditions; use reactive real-time battery-state monitoring under energy-scarce conditions

**Implication for orbital data centers:** Running GPU clusters at rated TDP through eclipse periods will exhaust battery lifetime faster than DoD-only calculations would predict. Effective compute scheduling must model battery degradation, not just energy balance.

## Power Budget at 1 MW Scale

From industry analysis (Orbital Systems Research Institute, 2025):

- Solar input at LEO: ~1,400 W/m²; at 20% panel efficiency → 280 W/m² output
- **3,600 m² solar array** required for steady-state 1 MW
- Eclipse bridging: up to **36 min battery window** needed per orbit

**Eclipse bridge sizing example (1 MW, 35% DoD limit):**
- Energy needed for 36 min eclipse at 1 MW: 600 kWh
- With 35% DoD constraint: battery bank must be ~1,714 kWh nominal
- At ~200 Wh/kg (Li-ion): ~8,570 kg of batteries for eclipse bridge alone
- At $7,000/kg launch cost (current): **~$60M in launch cost just for batteries** to sustain 1 MW through eclipse

This is why Starcloud chose SSO dawn-dusk orbit.

## SSO Dawn-Dusk: The Eclipse Mitigation

A sun-synchronous orbit (SSO) at ~97.6° inclination can be timed to track the Earth's day-night terminator — the satellite stays in near-continuous sunlight for months at a time.

**Trade-offs:**

| Factor | Standard LEO (~28–53°) | SSO Dawn-Dusk (~97.6°) |
|---|---|---|
| Eclipse fraction | ~37–40% | ~0–2% |
| Battery required | Large (eclipse bridge) | Minimal |
| Coverage latitude | Mid-latitude, equatorial | Polar, all latitudes |
| Ground station access | Lower latitudes preferred | Polar sites required |
| Debris flux (inclination) | Lower | Higher (SSO = high-flux inclination band per ORDEM 3.0) |
| Orbit altitude choice | Flexible | ~550–600 km typical |

Starcloud's white paper (Sep 2024) explicitly cites SSO dawn-dusk as eliminating the battery risk — the primary justification for their orbital choice alongside 5 GW solar array deployment.

## Key Takeaways for Space Data Centers

1. Standard LEO means ~37–40% of operating time is eclipse — batteries or compute suspension required
2. ISS heritage sets a 35% DoD limit; oversizing batteries by ~3× is the operational norm
3. Compute workloads directly accelerate battery degradation beyond what DoD alone predicts
4. SSO dawn-dusk orbit eliminates eclipse but increases debris collision risk (high-flux inclination) and constrains ground station geography
5. At 1 MW scale, eclipse-bridge batteries alone cost ~$60M in current launch costs — a strong forcing function toward either SSO orbit or aggressive compute throttling

## Related Pages

- [[wiki/sources/arxiv-2603-04372-leo-battery-aging.md]]
- [[wiki/sources/nasa-ntrs-iss-battery-dod.md]]
- [[wiki/sources/orbital-systems-power-budget-2025.md]]
- [[wiki/synthesis/space-datacenter-orbital-regime.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
- [[wiki/concepts/thermal-management.md]]
