---
title: "ISS Active Thermal Control System (ATCS) Overview (NASA/Boeing)"
type: "source_summary"
sources:
  - "nasa-iss-atcs-overview.txt"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://www.nasa.gov/wp-content/uploads/2021/02/473486main_iss_atcs_overview.pdf"
---

# ISS Active Thermal Control System (ATCS) Overview (NASA/Boeing)

**Source type**: industry_report (NASA/Boeing technical reference, IDS Business Support)
**Subject**: ISS ATCS architecture, hardware specs, operational parameters

## System Architecture

The ISS Active Thermal Control System (ATCS) has four subsystems that together handle all waste heat rejection for the station:

| Subsystem | Working fluid | Heat rejection |
|-----------|--------------|----------------|
| IATCS (Internal) | Water | Internal module cooling only; transfers to EATCS via IFHX |
| EATCS (External, permanent) | Anhydrous ammonia | 70 kW total (35 kW/loop) |
| PVTCS (Photovoltaic) | Anhydrous ammonia | 14 kW per PVR × 4 PVRs = 56 kW |
| EEATCS (Early, temporary) | Anhydrous ammonia | Replaced by EATCS; hardware reused as PVTCS spares |

Total ISS heat rejection capacity at assembly complete: **~126 kW** (EATCS 70 kW + PVTCS up to 56 kW).

## EATCS Radiator Hardware (Primary Heat Rejection)

The EATCS Heat Rejection Subsystem (HRS) is the primary permanent radiator system:

- **Configuration**: Two independent loops (Loop A on S1 Starboard, Loop B on P1 Port truss), each with one radiator wing of 3 ORUs
- **Each Radiator ORU**: 76.4 ft × 11.2 ft (**23.3 m × 3.4 m**) = ~79 m²; weighs **1,122.6 kg** → **~14.2 kg/m²** areal density
- **Each wing (3 ORUs)**: ~237 m²; 3 × 1,122.6 kg = ~3,368 kg
- **Total EATCS radiator area**: ~474 m² (two wings)
- **Panels per ORU**: 8 panels; 22 Inconel flow tubes per panel; Z-93 white coating for optimum thermo-optical properties
- **Coolant**: Anhydrous ammonia; freeze-tolerant flow tube arrangement; ammonia supply at 37°F (2.8°C)
- **Deployment**: Each ORU launches stowed and deploys/retracts on orbit via onboard mechanism

## Thermal Radiator Rotary Joint (TRRJ)

Each radiator wing rotates via a TRRJ — the mechanism behind the "gimbaled panels for sun avoidance" described in data center design proposals:

- Rotates ±115° (software command limit ±105°) at 0–45°/min
- Carries power, data, and liquid ammonia across the rotating interface (via Flex Hose Rotary Coupler)
- RGAC algorithm commands "edge to sun" (isolation phase) or "face to Earth" (eclipse phase) to keep radiator outlet at −40°F
- Each TRRJ weighs 927 lbs (420.5 kg)

## PVTCS Radiator (PVR)

The deployable photovoltaic thermal radiators are smaller and serve the solar array power electronics:

- Each PVR: 10.24 ft × 44.62 ft (**3.12 m × 13.6 m**) = ~42.4 m²; weighs **740.7 kg** → **~17.5 kg/m²** areal density
- 7 panels; rejects up to **14 kW** per PVR
- 4 PVRs at assembly complete (P4, P6, S4, S6)

## Supporting Components

| Component | Mass | Function |
|-----------|------|----------|
| Pump Module (PM) | 353.8 kg each | Circulation, pressure, temperature control; ammonia at 300–390 psia |
| Ammonia Tank Assembly (ATA) | 508 kg each | Fluid supply, primary accumulator; ~640 lbm ammonia per ATA |
| Nitrogen Tank Assembly (NTA) | 208.65 kg each | Nitrogen at 2,500 psia pressurizes ATA bellows |
| TRRJ | 420.5 kg each | Radiator rotation; power/data/ammonia transfer |
| IFHX (Interface Heat Exchanger) | 41.28 kg each | Water-to-ammonia heat exchange; 10 at assembly complete |

## Key Quantitative Data for Space Data Center Analysis

**Validated heat rejection**: ISS EATCS demonstrates 70 kW operational radiative cooling with flight heritage. Combined with PVTCS, total ISS capacity is ~126 kW — establishing the upper bound of heritage-validated thermal systems, far below the 1 MW+ target for orbital data centers.

**Areal density (primary source data)**:
- EATCS radiator panels: ~14.2 kg/m² (panel-only mass)
- PVTCS radiator panels: ~17.5 kg/m² (panel-only mass)
- System-level density (including pumps, tanks, joints, plumbing) is substantially higher

**Deployment**: The ISS radiators launch stowed and deploy on orbit. The specific mechanism type is a deploy/retract system (referenced in vendor literature as a scissors-beam or pantograph mechanism) allowing the ~23 m long ORUs to fit within Shuttle/rocket fairings.

**Coolant choice**: Anhydrous ammonia dominates external loops for its -107°F (-77°C) freeze point and wide operating temperature range.

## Significance

This is the primary NASA technical reference for ISS thermal control hardware — the direct ancestor of the "ISS-derived" radiator designs proposed for orbital data centers. The document confirms:
1. ISS EATCS radiators are ~14 kg/m² at panel level (better than the ~19 kg/m² figure commonly cited)
2. Rotary joint (TRRJ) provides the sun-avoidance articulation assumed in data center proposals
3. Ammonia is the validated external coolant choice
4. 70 kW is the flight-proven ceiling; 1 MW requires ~15× more radiator area than both EATCS wings combined

## Related Pages

- [[wiki/synthesis/iss-scissors-beam-thermal-mechanisms.md]]
- [[wiki/concepts/thermal-management.md]]
- [[wiki/synthesis/thermal-management-scale-vs-breakthrough.md]]
- [[wiki/sources/orbital-ai-factory-heat-management.md]]
