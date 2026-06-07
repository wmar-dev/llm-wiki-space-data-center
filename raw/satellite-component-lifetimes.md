# Satellite Component Lifetimes

Source aggregation from web search, 2026-06-07

Key sources:
- MDPI Applied Sciences: "Degradation Modeling and Telemetry-Based Analysis of Solar Cells in LEO for Nano- and Pico-Satellites" (2025)
- JAXA: "Cycle-life testing of large-capacity lithium-ion cells in simulated satellite operation"
- NASA: VES16 Li-ion cell life test data
- Aerospace Corporation: "Majority of Satellites Exceed Design Life" (2019)
- University of Athens: Power subsystem design slides

## Solar Panel Degradation (LEO)

| Cell Type | Degradation over 6 months (<500 km) | Annual degradation rate |
|-----------|--------------------------------------|------------------------|
| Si (coated) | 25-35% | ~3.75%/year typical |
| GaAs | 10-20% | ~2.75%/year typical |
| Triple-junction (GaInP/GaAs/Ge) | 5-15% | <2%/year |
| CIGS | 20-40% | N/A |

TJ cells with AO-resistant coatings retain >85% of initial efficiency after 1 year in LEO.

PV panels degrade ~8× faster in space than on Earth.

## Battery Cycle Life

Li-ion space batteries:
- >30,000 cycles in simulated LEO (5-year equivalent at 20% DoD)
- >60,000 cycles with <20% loss (VES16, 20-40% DoD)
- LEO: ~5,000 cycles/year, 30 min eclipse per 90 min orbit
- GEO: 1,800+ cycles (15-20 year equivalent)
- GEO batteries must last 15-18 years

## Satellite Design Life

- ~87% of US military/civil satellites meet/exceed design life
- ~75% of commercial satellites meet/exceed design life
- Typical LEO satellite design life: 5-8 years
- Typical GEO satellite design life: 15-18 years
- Large constellations (Iridium, Globalstar): 5-8 year design life
- Class A US military/civil: >11 years
- Experimental: 1-3 years

## Electronics

- Commercial semiconductor devices: 3-7 year useful life
- Space-grade electronics: wearout not typically an issue for 15-year GEO missions
- Radiation effects (TID, displacement damage) primary concern in LEO
- FIT rates allow MTBF prediction for entire systems
