---
title: "Current Solar Cell Efficiency for Space Applications"
type: "synthesis"
sources:
  - "space-based-solar-power.md"
  - "caltech-sspp-mission-lessons.md"
  - "satellite-component-lifetimes.md"
  - "nasa-irosa-solar-arrays.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Current Solar Cell Efficiency for Space Applications

Space solar cells operate under AM0 (Air Mass Zero) conditions — unfiltered solar
spectrum with no atmospheric absorption — and must withstand high-energy radiation,
thermal cycling, and atomic oxygen exposure. Cell technology choice drives both
initial efficiency and the rate at which that efficiency degrades over the mission.

## Cell Technologies in Use

### Triple-Junction (GaInP/GaAs/Ge) — Current Preferred Standard

Triple-junction (TJ) cells are the state of the art for long-duration orbital
missions. They are optimized for AM0 spectral conditions by tuning sub-cell
bandgaps to maximise photon capture across the full unfiltered solar spectrum.

- **Initial efficiency**: Open question — the wiki does not yet contain a
  confirmed AM0 efficiency number for commercial TJ cells from a peer-reviewed
  source. (Terrestrial concentrated records reach ~39.5% per NREL; AM0 space
  figures are lower and are not yet cited in this wiki.)
- **Degradation**: <2%/year in LEO; TJ cells with atomic-oxygen-resistant
  coatings retain **>85% of initial efficiency after 1 year** in LEO
  [[wiki/sources/space-datacenter-component-lifetimes.md]]
- **Deployment example**: iROSA arrays on the ISS use TJ cells; each panel
  produces **>28 kW** at beginning of life [[wiki/sources/nasa-irosa-solar-arrays.md]]
- **Cost**: Commercial space-grade solar cells cost approximately **100× more**
  than terrestrial equivalents [[wiki/sources/caltech-sspp-mission-lessons.md]]

### Gallium Arsenide (GaAs) — Single-Junction

- **Degradation**: ~2.75%/year in LEO [[wiki/sources/space-datacenter-component-lifetimes.md]]
- Caltech SSPP ALBA experiment confirmed low-cost GaAs cells "performed
  consistently well" over 240+ days of on-orbit operation
  [[wiki/sources/caltech-sspp-mission-lessons.md]]
- Suitable for medium-duration missions; lower cost than TJ

### Silicon (Si) — Legacy / Short-Duration

- **Degradation**: 25–35% in the first 6 months in LEO below 500 km
  [[wiki/sources/space-datacenter-component-lifetimes.md]]
- **Efficiency at AM0**: ~14%, compared to ~16% at terrestrial AM1.5 — space
  conditions produce lower efficiency for Si cells due to spectral mismatch
  *(Wikipedia: Solar Cell Efficiency)*
- Practical only for short missions (<1 year) in low-radiation environments

### Perovskite — Experimental

Caltech's ALBA experiment found perovskite cells showed "tremendous variability"
on orbit and are not yet ready for orbital deployment
[[wiki/sources/caltech-sspp-mission-lessons.md]].

## Space vs. Terrestrial Efficiency

Solar cells in space degrade approximately **8× faster** than equivalent
terrestrial installations [[wiki/sources/space-based-solar-power.md]]. This is
driven by:

- High-energy particle radiation (protons, electrons) causing displacement damage
- Thermal cycling between −120°C and +120°C (roughly every 90 minutes in LEO)
- Atomic oxygen erosion at low altitudes
- Ultraviolet exposure without atmospheric filtering

Inference: Despite lower AM0 efficiency for Si cells, TJ cells may generate
comparable or higher power output in space vs. ground installations, because AM0
solar irradiance (~1,361 W/m²) is higher than typical terrestrial irradiance
with atmospheric and weather losses.

## Sizing Implications for Space Data Centers

The iROSA figures establish a practical benchmark: 6 panels totalling **>250 kW**
for the full ISS [[wiki/sources/nasa-irosa-solar-arrays.md]]. A 1 MW orbital data
center would require solar array capacity roughly 4× the entire ISS solar system —
before accounting for thermal radiator power, eclipse battery charging, and
end-of-life power margin.

Inference: With TJ cell degradation at <2%/year and a 10-year design life, a
space data center would need at least 20% initial power oversizing to maintain
rated compute capacity at end of life.

## Open Questions

- What is the confirmed AM0 efficiency for current commercial TJ space cells
  (e.g., Spectrolab XTJ Prime, AZUR 3G30A)? No peer-reviewed source in the wiki
  provides this number directly.
- What efficiency gains have emerged from 4-junction or 5-junction cells now
  reaching commercial qualification for GEO satellites?
- Do low-cost GaAs alternatives (as tested in Caltech SSPP) approach TJ
  efficiency closely enough to reduce cost without sacrificing acceptable
  degradation rates?

## Related Pages

- [[wiki/sources/nasa-irosa-solar-arrays.md]]
- [[wiki/sources/caltech-sspp-mission-lessons.md]]
- [[wiki/sources/space-datacenter-component-lifetimes.md]]
- [[wiki/concepts/space-datacenter-component-lifetimes.md]]
- [[wiki/sources/space-based-solar-power.md]]
