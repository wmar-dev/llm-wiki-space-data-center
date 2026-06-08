---
title: "On-Orbit Servicing (OOS)"
type: "concept"
sources:
  - "on-orbit-satellite-servicing-wikipedia.md"
  - "on-orbit-servicing-refueling-2026.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# On-Orbit Servicing (OOS)

## What It Is

On-orbit servicing (OOS) encompasses refueling, life extension, inspection, repair, and component replacement of satellites while in orbit. For orbital data centers, OOS is the theoretical mechanism by which hardware refresh (upgrading compute modules to newer GPU generations) could occur without deorbiting the satellite.

## Demonstrated Capabilities (TRL 7–9)

| Mission | Year | Capability | Orbit |
|---|---|---|---|
| Shuttle SMM repair | 1984 | Manual repair by astronauts | LEO |
| Hubble servicing (×5) | 1993–2009 | Modular subsystem replacement | LEO |
| DARPA Orbital Express | 2007 | First **autonomous** satellite servicing; fluid transfer + ORU swap | LEO |
| Northrop MEV-1 | 2019–2025 | GEO life extension via docking to apogee engine nozzle | GEO |
| Northrop MEV-2 | 2021 | Second GEO life extension | GEO |
| Astroscale Provisioner | 2024+ | Propellant refueling (Space Force contract) | LEO |
| Orbit Fab depots | 2024+ | RAFTI-standard propellant ports; depots operational | LEO/GEO |

**Key milestone:** MEV-1 first undocking (April 2025) — the satellite returned to normal commercial operations after 5 years of MEV-provided station-keeping, then MEV-1 moved to service another client. GEO life extension via propellant transfer / thruster augmentation is now a commercial service.

## Capabilities Still Undemonstrated

- **Component-level hardware swap in LEO** at commercial scale — Orbital Express demonstrated it on a purpose-built modular testbed; no commercial mission has swapped compute or sensor modules on a production satellite
- **Standardized compute module interfaces** — no equivalent of ESPA or CubeSat standards exists for orbital GPU modules
- **LEO servicing economics** — GEO life extension is economically justified ($300M GEO satellite + $50M servicing vs. $350M replacement). LEO satellites cost $1–10M; servicing costs may exceed replacement costs at current pricing

## Current Industry State (2026)

- **OSAM-1 cancelled** (NASA, 2024) — the flagship robotics-based OOS demonstration was cancelled after $2B in expenditure; slows development of dexterous manipulation capabilities
- **DARPA RSGS** — still in development; targets GEO robotic servicing
- **Lockheed MAP standard** (2022) — mechanical interface for on-orbit docking; not yet widely adopted
- **Orbit Fab RAFTI ports** — propellant transfer standard gaining adoption; ~10 satellites manifested

**Assessment:** Propellant transfer and GEO life extension are commercially viable today. Compute module swap in LEO is not demonstrated and lacks the interface standards, economics, or logistics infrastructure to be viable within a 5–10 year horizon.

## Implication for Space Data Center Hardware Refresh

The [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]] analysis establishes that GPU generations turn over every 2–3 years while space hardware is locked in for 5–6 years. OOS is frequently cited as the solution, but:

1. No mission has replaced a compute module on orbit
2. Standardized compute interfaces for orbital swap do not exist
3. LEO servicing economics disfavor replacement (low satellite cost)
4. OSAM-1 cancellation set back dexterous robotics by years

**Inference:** On-orbit compute hardware refresh via OOS is unlikely to be commercially available before 2035 at the earliest, and will require purpose-designed satellites with standardized modular interfaces from the start. It does not resolve the hardware refresh penalty for any satellite launched in the 2025–2030 window.

## Related Pages

- [[wiki/sources/on-orbit-satellite-servicing.md]]
- [[wiki/sources/on-orbit-servicing-refueling-2026.md]]
- [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
