---
title: "Thermal Management in Space Data Centers"
type: "concept"
sources:
  - "space-arch-radiative-cooling-2025.md"
  - "orbital-ai-factory-heat-management.md"
  - "nasa-iss-atcs-overview.txt"
  - "nasa-smallsat-thermal-control-soa.md"
  - "nss-space-resources-thermal-management.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Thermal Management in Space Data Centers

## Overview

Earth-based data centers rely on convective cooling — air or liquid carries waste heat away from servers. In space, there is no atmosphere, so convection is impossible. All waste heat must be rejected via **thermal radiation**.

## Radiative Cooling Fundamentals

A body at temperature T radiates power according to the Stefan-Boltzmann law. At operational temperatures (~300 K), a radiator surface can reject approximately **450 W/m²**.

This creates a direct area-to-power relationship:

| Power load | Required radiator area |
| ---------- | ---------------------- |
| 1 MW       | ~2,200 m²              |
| 10 MW      | ~22,000 m²             |

Inference: Radiator area scales linearly with power load at constant temperature, making large-scale space data centers extremely radiator-surface-constrained.

## Implications for Design

- Radiator mass and deployment area are fundamental limits on data center scale in space
- Higher operating temperatures allow more heat rejection per unit area (T⁴ dependence), but raise reliability concerns for electronics
- Two-sided radiators or deployable panels can increase effective area without proportional structural mass

Current large-scale deployable radiator designs achieve ~140-160 m² per assembly (22-23 m × 6-7 m) using ISS-derived scissors-beam mechanisms, with total effective areas of ~1,700-2,000 m² for a 1 MW thermal load [[wiki/sources/orbital-ai-factory-heat-management.md]] *(industry_report)*. Larger areas are structurally feasible but face tradeoffs with launch mass, deployment complexity, and micrometeoroid vulnerability.

**Areal density (primary source)**: The ISS EATCS radiator ORUs (each 23.3 m × 3.4 m, 1,122.6 kg) achieve ~14.2 kg/m² at the panel level [[wiki/sources/nasa-iss-atcs-overview.md]] *(industry_report)*; PVTCS panels reach ~17.5 kg/m². System-level density (including pumps, tanks, rotary joints, and plumbing) is substantially higher. NASA targets <6 kg/m² for future deployable radiator systems to enable MW-scale orbital facilities.

## Technology TRL Landscape (SmallSat to Large-Sat)

From NASA's 2026 SmallSat State-of-the-Art survey [[wiki/sources/nasa-smallsat-thermal-control-soa.md]] *(industry_report)*:

| Technology | TRL | Notes for data center applications |
|------------|-----|-------------------------------------|
| Optical coatings (Z-93, FEP) | 9 | Degrade over mission life; BOL/EOL modeling required for 5–10yr lifetimes |
| MLI insulation | 9 (large) / 4-6 (CubeSat) | Compresses in deployers; edge effects short performance at small scale |
| Thermal straps (pyrolytic graphite) | 7-8 | High conductivity; first flew on ASTERIA 2017 |
| Heat pipes | 9 | No power required; capillary driven |
| Phase change materials | 6-8 | Paraffin at 20–60°C, 140–280 kJ/kg; smooths transients from variable GPU workloads |
| Kapton heaters | 7-9 | −200°C to 300°C; most common active SmallSat technology |
| Cryocoolers | 7-9 (mature) | LM MICRO1-1: 1U, 0.35 kg, 15W at TRL 7-9; not practical at MW thermal loads |
| Thermoelectric coolers | 7-9 | Add net heat (I²R); not viable for primary rejection |
| Pumped fluid loops | 7-9 | ISS EATCS heritage; primary approach for MW scale |
| AMDROHP deployable radiators | ~3-5 | JPL development; oscillating heat pipes in 3U CubeSat; precursor to large deployable panels |

**Key gap**: MLI is unreliable at CubeSat scale due to deployer compression. AMDROHP (TRL ~3-5) is the active development path for next-generation deployable radiators. No single SmallSat thermal technology scales to MW without redesign.

## Advanced Radiator Concepts

### Liquid Droplet Radiator (LDR)

Replaces the solid radiating surface with a controlled stream of 100-μm fluid droplets expelled into space and then recaptured. NASA/NSS Space Resources Vol. 2 claims a **10–100× power-to-mass advantage** over solid surface radiators [[wiki/sources/nss-space-resources-thermal-management.md]] *(industry report)*.

Worked example (1 MW thermal rejection, 100 kW nuclear plant at ~10% efficiency):

| Technology | Area | Mass |
|---|---|---|
| Aluminum heat pipe radiator | 256 m² | 1,300 kg |
| LDR (DC-705 vacuum oil) | — | ~24 kg fluid / <100 kg total |

At ~13× system-level mass reduction, LDR would substantially close the gap between current ~19 kg/m² areal density and NASA's <6 kg/m² target. However, the source predates modern flight qualification work and does not cite current TRL.

Open question: What is the current TRL for Liquid Droplet Radiators, and what engineering barriers remain to flight qualification for MW-scale loads?

### Belt Radiator

Ultrathin solid surfaces coated with low vapor pressure liquids; surface tension maintains continuous heat transfer without the droplet capture hardware that LDR requires. Less mass advantage than LDR but mechanically simpler.

## Sources

- [[wiki/sources/space-arch-radiative-cooling-2025.md]] *(industry_report)*
