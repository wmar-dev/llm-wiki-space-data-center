---
title: "Thermal Management in Space Data Centers"
type: "concept"
sources:
  - "space-arch-radiative-cooling-2025.md"
status: "stale"
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

Open question: What is the maximum radiator area practically deployable on an orbital platform given launch mass and deployment complexity constraints?

## Sources

- [[wiki/sources/space-arch-radiative-cooling-2025.md]] *(industry_report)*
