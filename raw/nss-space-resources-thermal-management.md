# Thermal Management In Space
Source: https://www.nss.org/settlement/nasa/spaceresvol2/thermalmanagement.html
NSS Space Resources Vol. 2 — NASA/NSS planning document

## Overview

Thermal management challenges for space-based power systems and industrial operations. The key challenge: in vacuum, heat rejection relies exclusively on radiation rather than convection.

## Core Physics Principle

Stefan-Boltzmann Law governs heat rejection: E = σT⁴, where σ = 5.67 W m⁻² K⁻⁴. "The total amount of heat radiated is proportional to the surface area of the radiator. And the lower the radiation temperature, the larger the radiator area (and thus the radiator mass, for a given design) must be."

## Power System Requirements

**Solar Photovoltaic**: Up to several hundred kilowatts; must dissipate ~25% of generated power as waste heat.

**Solar Thermal**: Operates 1000–2000 K; rejects 70–85% of collected energy (15–30% conversion efficiency).

**Nuclear Power**: Rejects heat at relatively high temperatures; example shows ~10% thermal-to-electric conversion.

## Heat Rejection Systems

### Heat Pipes

Passive systems — thin hollow tubes filled with temperature-specific fluid cycling between vapor and liquid phases. Benefits: no moving parts, graceful failure with redundancy. An aluminum heat pipe radiator achieves approximately **5 kg/m²** mass with 0.86 emissivity, operating up to 700 K.

### Pump Loop Systems

Conventional heat exchangers with a carrier fluid pumped through pipes. Space Shuttle used deployed clamshell door radiators as an example.

### Liquid Droplet Radiator (LDR)

Replaces solid radiating surfaces with controlled droplet streams. Droplets of 100 micrometers diameter offer "a power-to-mass advantage over solid surface radiators of between 10 and 100."

Example: A lunar processing facility requiring 1 MW thermal rejection (100 kW nuclear plant at ~10% efficiency):
- Aluminum heat pipe radiator: **256 m²**, **1,300 kg**
- LDR using Dow-Corning 705 vacuum oil: radiating fluid mass only **24 kg**, total system mass "still less than 100 kg"

This represents roughly a 13× mass reduction at total system level.

### Belt Radiator Concepts

Ultrathin solid surfaces coated with low vapor pressure liquids; surface tension maintains continuous heat transfer without droplet capture requirements.

## Laser Power Transmission

**Solar-Pumped Photodissociation Lasers**: C₃F₇I lasant; emits at 1.3 μm; requires no thermal radiator except recirculation pipes; continuous operation without resupplying lasant.

**Solar-Pumped Photoexcitation Lasers**: Neodymium ion lasers absorb visible spectrum, emit near-infrared at 1.06 μm. Dye lasers absorb blue-green, emit red near 0.6 μm.

**Indirect Photoexcitation Lasers**: CO₂ and N₂O molecules lase 9–11 μm; blackbody temperatures 1000–1500 K; "powers approaching 1 watt in initial laboratory versions."

## Critical Insight on Low-Temperature Waste Heat

Low-temperature waste heat from life support and manufacturing is the **dominant thermal challenge** — not the primary heat source. Example: A 100 kW nuclear plant generating 1 MW thermal rejection creates a 256 m² low-temperature radiator (1,300 kg), dwarfing the 50 m² primary reactor radiator (500 kg).
