---
title: "Thermal Constraints for Space Data Centers"
type: "synthesis"
sources:
  - "space-arch-radiative-cooling-2025.md"
  - "orbital-ai-factory-heat-management.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Thermal Constraints for Space Data Centers

**Query**: What are the thermal constraints for space data centers?

## Answer

Space data centers face a fundamental thermal constraint with no Earth analogue: **the absence of convective cooling**. [[wiki/concepts/thermal-management.md]]

On Earth, data centers shed heat through airflow or liquid cooling. In space, there is no atmosphere, so convection is physically impossible. All waste heat must be rejected via **thermal radiation** — the only viable mechanism.

The key quantitative constraint is the radiator area required per unit of power:

- A radiator at ~300 K rejects approximately **450 W/m²** [[wiki/sources/space-arch-radiative-cooling-2025.md]] *(industry_report)*
- A **1 MW** data center therefore requires approximately **2,200 m²** of radiator surface area [[wiki/sources/space-arch-radiative-cooling-2025.md]] *(industry_report)*

Inference: Radiator area scales linearly with power load at constant operating temperature, making the structural mass and deployable surface area of radiators the binding constraint on space data center scale.

Higher operating temperatures improve heat rejection per unit area (following Stefan-Boltzmann's T⁴ dependence), but this trades off against electronics reliability and thermal cycling stress. [[wiki/concepts/thermal-management.md]]

Current large-scale deployable radiator designs achieve ~1,700-2,000 m² for a 1 MW node using 2-4 ISS-derived assemblies, each ~140-160 m² [[wiki/sources/orbital-ai-factory-heat-management.md]] *(industry_report)*. NASA's current state-of-the-art deployable radiator aerial density is ~19 kg/m², with a target of <6 kg/m². The practical maximum scales with launch vehicle payload fairing volume and mass capacity — Starship's 100+ ton payload could theoretically support 3,000-5,000+ m² of deployable radiator surface given appropriate deployment kinematics.
