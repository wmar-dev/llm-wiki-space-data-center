---
title: "Thermal Management in Space (NSS Space Resources Vol. 2)"
type: "source_summary"
sources:
  - "nss-space-resources-thermal-management.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Thermal Management in Space (NSS Space Resources Vol. 2)

**Origin**: NASA/NSS Space Resources Volume 2 — a NASA-funded space settlement planning study. Authoritative technical reference; classified here as industry report (no DOI, but NASA-commissioned). *(industry report)*

## Core Physics

Stefan-Boltzmann law (E = σT⁴, σ = 5.67 W m⁻² K⁻⁴) fully governs heat rejection in vacuum. Lower radiation temperature requires larger radiator area for the same power load. No convection pathway exists.

## Power System Waste Heat Fractions

| Power type | Waste heat fraction | Operating temperature |
|---|---|---|
| Solar PV | ~25% | Ambient |
| Solar thermal | 70–85% | 1,000–2,000 K |
| Nuclear (example) | ~90% | High temp |

## Heat Rejection Technologies

### Heat Pipes (passive)
- Aluminum heat pipe radiator: **~5 kg/m²**, emissivity 0.86, max ~700 K
- No moving parts; graceful failure mode; TRL 9

### Pump Loop Systems
- Conventional heat exchangers with pumped carrier fluid
- Space Shuttle clamshell radiators are the primary heritage example

### Liquid Droplet Radiator (LDR)
The most significant advanced concept in this source. Replaces solid radiating surfaces with a controlled stream of 100-μm droplets.

**Key claim**: LDR offers "a power-to-mass advantage over solid surface radiators of between 10 and 100."

**Worked example** (1 MW thermal rejection from 100 kW nuclear plant):
- Aluminum heat pipe radiator: 256 m², 1,300 kg
- LDR (Dow-Corning 705 vacuum oil): fluid mass 24 kg, total system mass <100 kg
- Implied system-level mass reduction: **~13×** (at the low end of the claimed 10–100× range)

Inference: LDR represents a potential path to break through the ~19 kg/m² areal density constraint that blocks GW-scale orbital data centers [[wiki/synthesis/thermal-management-scale-vs-breakthrough.md]].

Open question: What is the current TRL for Liquid Droplet Radiators, and what engineering barriers remain to flight qualification?

### Belt Radiator
Ultrathin solid surfaces coated with low vapor pressure liquids; surface tension maintains heat transfer without droplet capture hardware. Less mass advantage than LDR but simpler mechanically.

## Laser Power Transmission (Contextual)

The source also covers three laser transmission approaches that eliminate the need for large radiators on the power transmitter side:

- **Photodissociation lasers** (C₃F₇I, 1.3 μm): no radiator except recirculation pipes
- **Photoexcitation lasers** (Nd ion, 1.06 μm; dye lasers, ~0.6 μm)
- **Indirect photoexcitation** (CO₂/N₂O, 9–11 μm): blackbody-pumped; laboratory-scale watts

These are relevant to Aetherflux-style SBSP laser transmission concepts [[wiki/entities/aetherflux.md]].

## Critical Framing: Low-Temperature Waste Heat Dominates

The source emphasizes that secondary waste heat — from life support, manufacturing auxiliaries, electronics — is the **dominant mass driver**, not primary conversion heat:

- 100 kW nuclear plant primary radiator: 50 m², 500 kg
- Same plant's low-temperature waste heat radiator: 256 m², 1,300 kg (2.6×)

This pattern applies directly to orbital data centers: server waste heat at near-ambient temperatures requires larger radiators than if the same power were rejected at higher temperatures.

## Relationship to Existing Wiki

- Reinforces Stefan-Boltzmann fundamentals in [[wiki/concepts/thermal-management.md]]
- The 5 kg/m² heat pipe panel figure is consistent with the wiki's system-level 14.2 kg/m² for ISS EATCS (panel vs. full system including pumps/joints)
- LDR data is new to the wiki — directly addresses the mass efficiency gap identified in [[wiki/synthesis/thermal-management-scale-vs-breakthrough.md]]
- No contradictions with existing pages found
