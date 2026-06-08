---
title: "NASA SmallSat State-of-the-Art: Thermal Control (Chapter 7, May 2026)"
type: "source_summary"
sources:
  - "nasa-smallsat-thermal-control-soa.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/"
---

# NASA SmallSat State-of-the-Art: Thermal Control (Chapter 7, May 2026)

**Source type**: industry_report (NASA Small Spacecraft Institute, official technical reference)
**Published**: May 7, 2026
**Subject**: State-of-the-art thermal management technologies for small satellites and CubeSats

## Why This Source Matters for Space Data Centers

SmallSats define the TRL floor for deployable thermal hardware. A space data center satellite — 60 kg to multi-ton depending on design — faces the same physics as a SmallSat but at 100–1,000× the power density. Understanding where SmallSat thermal tech stands (and where it fails) sets the lower bound for what is flight-proven and the upper bound of what can be inherited.

## SmallSat-Specific Thermal Challenges

Five constraints that are magnified in data center applications:

1. **Low thermal mass** — reactive temperature responses to environment changes; GPU workload variance makes this worse
2. **Limited external surface area** — competing with solar panels and instruments for radiator space
3. **Constrained volume** — limits component spacing and heat spreading
4. **Power limitations** — active cooling draws from the same budget as compute
5. **Power density** — stacked electronics (GPUs, HBM) create concentrated heat that is hard to spread

## Passive Technologies — TRL and Status

| Technology | TRL (LEO) | Notes |
|------------|-----------|-------|
| Optical coatings (Z-93, FEP tape) | 9 | Fully flight-proven; degrade over mission life (atomic oxygen, UV) — BOL vs EOL modeling required |
| MLI blankets | 9 (large sats); 4-6 (CubeSats) | Compresses in deployers; edge effects short thermal performance — unreliable at CubeSat scale |
| Thermal straps (copper/Al) | 9 | Commodity product; flexible links from source to sink |
| Thermal straps (pyrolytic graphite) | 7-8 | Higher conductivity than metals; ASTERIA flew PGS straps in 2017 |
| Heat pipes (cylindrical/flat) | 9 | Passive, no power; capillary action drives fluid |
| Phase change materials (paraffin) | 6-8 | Paraffin: 20–60°C melt, 140–280 kJ/kg fusion heat; smooths transients |
| Deployable radiators (AMDROHP) | ~3-5 | JPL + CA universities; oscillating heat pipes in 3U form factor; development stage |

## Active Technologies — TRL and Status

| Technology | TRL (LEO) | Specs | Notes |
|------------|-----------|-------|-------|
| Kapton electrical heaters | 7-9 | 0.4–7.75 W/cm²; −200°C to 300°C | Most common active tech on SmallSats |
| Cryocoolers (mature) | 7-9 | LM MICRO1-1: 1U, 0.35 kg, 15W, TRL 7-9 | Lunar IceCube used 600 mW cooler at 80K |
| Cryocoolers (advanced) | 4-6 | AIM SF070: 0.85 kg, 24W, 0.6W @ 80K | Scales poorly with data center heat loads |
| Thermoelectric coolers (TECs) | 7-9 | 1.8–322W cooling capacity | Peltier effect; efficiency degrades below 130K; adds net heat (see Seebeck wiki page) |
| Fluid loops (legacy) | 7-9 | Pumped ammonia/water from HX to radiator | ISS-heritage approach |
| Fluid loops (miniaturized, ATA) | 4-7 | Utah State U: sub-1U, >200% perf, >30% mass savings | Combines pumped loop + cryocooler |

## Key Technology Gaps for Data Center Scale

**MLI failure mode**: MLI — the standard insulation on large satellites — degrades to near-uselessness at CubeSat scale due to deployer compression and edge effects. This suggests that purely passive insulation strategies cannot be directly scaled from SmallSat heritage to larger platforms without redesign.

**AMDROHP**: The most relevant new development is NASA JPL's Additively Manufactured Deployable Radiators with Oscillating Heat Pipes (AMDROHP), fitting within a 3U CubeSat. This is a direct technology precursor to the larger ISS-derived deployable radiators proposed for MW-scale data centers — but at TRL ~3-5, it is not yet flight-qualified.

**Coating degradation**: All passive radiator surfaces degrade due to atomic oxygen and UV in LEO. Beginning-of-life (BOL) vs. end-of-life (EOL) thermal models must account for this — relevant to 5–10 year orbital data center lifetimes.

## Flight-Proven Examples

- **BioSentinel** (6U, Artemis I, 2022): metallized tape + silver FEP for thermal surface management
- **Lunar IceCube** (6U, Artemis I, 2022): 600 mW cryocooler for IR spectrometer at 80K
- **TechEdSat-10** (6U, ISS deploy 2020): FlexCool conformable heat pipes for concentrated radio electronics heat
- **ASTERIA** (CubeSat, 2017): Pyrovo pyrolytic graphite film thermal straps (high-conductivity heat spreading)

## Contradiction Check

No contradictions with existing wiki pages. This source adds:
- TRL ratings (missing from all existing thermal pages)
- MLI failure mode at CubeSat scale (new)
- AMDROHP development path (new — future predecessor to large deployable radiators)
- Coating degradation BOL/EOL modeling requirement (complements radiator lifetime data in component-lifetimes pages)

## Related Pages

- [[wiki/concepts/thermal-management.md]]
- [[wiki/sources/nasa-iss-atcs-overview.md]]
- [[wiki/sources/sciopen-space-datacenter-thermal.md]]
- [[wiki/synthesis/iss-scissors-beam-thermal-mechanisms.md]]
- [[wiki/synthesis/seebeck-effect-heat-dissipation.md]]
