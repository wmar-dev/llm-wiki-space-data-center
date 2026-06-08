---
title: "Thermal Management in Space Data Centers"
type: "concept"
sources:
  - "space-arch-radiative-cooling-2025.md"
  - "orbital-ai-factory-heat-management.md"
  - "nasa-iss-atcs-overview.txt"
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

## Sources

- [[wiki/sources/space-arch-radiative-cooling-2025.md]] *(industry_report)*
