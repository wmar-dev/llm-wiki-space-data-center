---
title: "Radiation Environment and Electronics Effects (SEU/TID)"
type: "concept"
sources:
  - "arxiv-2302-08952-leo-edge-failures.md"
  - "satellite-component-lifetimes.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Radiation Environment and Electronics Effects (SEU/TID)

## The Three Damage Mechanisms

LEO electronics face three distinct radiation failure modes with different characteristics and mitigations:

| Mechanism | Type | Recoverable? | Mitigation |
|---|---|---|---|
| **SEU** (Single-Event Upset) | Bit flip from a single energetic particle | Yes — reset/ECC | Error-correcting code (ECC), scrubbing |
| **TID** (Total Ionizing Dose) | Cumulative charge trapping in gate oxides | No — permanent | Rad-hard fab process, shielding |
| **Displacement Damage** | Lattice defects from neutron/proton fluence | No — permanent | Careful material selection |

At 550 km LEO, TID and SEU drive satellite design life to 5–7 years for commercial COTS electronics.

## LEO Radiation Environment

**Flux sources:**
- Trapped protons and electrons in the Van Allen belts
- Galactic cosmic rays (GCR) — constant low-level background
- Solar particle events (SPE) — sporadic, high-dose spikes during solar max

**South Atlantic Anomaly (SAA):** A dip in the inner Van Allen belt at 200–800 km altitude above the South Atlantic and South America. Every LEO orbit passes through or near the SAA, delivering a disproportionate fraction of total dose — elevated radiation exposure begins at 200 km altitude.

**Altitude effect:** Radiation flux increases with altitude within LEO. A satellite at 550 km (Starlink shell) receives significantly higher TID than one at 400 km (ISS), but 550 km is below the peak of the inner belt (~1,500 km).

## Quantitative COTS Shielding Data

From arxiv:2302.08952 — study of Snapdragon SA8155P SoC in 550 km LEO, 5-year design life:

- **1 mm aluminum shielding** is sufficient to protect the SoC against its 50 krad TID limit
- **Mass penalty:** +10.8% per device
- **Volume penalty:** +5.49% per device
- **SEU rate (residual):** 10⁻³ to 10⁻⁴ per device per day even with shielding

**Fleet implication:** A Starlink-class satellite with 60 SoCs per spacecraft would experience **30–300 SEU-induced errors per 24 hours** across the fleet. For a data center compute cluster, this translates to a continuous background of soft errors requiring real-time error detection and recovery at the application layer.

## Rad-Hard vs. COTS Trade

| Approach | TID Rating | SEU Tolerance | Compute Performance | Cost |
|---|---|---|---|---|
| Rad-hard processors (heritage flight) | >1 Mrad | Lockstep TMR | ~10-year-old process nodes | Very high |
| Rad-hard FPGAs (Xilinx Kintex-U) | 100–300 krad | SEU-immune config | Moderate | High |
| COTS + shielding (commercial SoC/GPU) | 50–100 krad (with Al shield) | ECC scrubbing | Current-gen | Moderate |
| Bare COTS (no mitigation) | Rapid degradation | Unacceptable SEU rate | Current-gen | Low |

**The orbital data center dilemma:** Rad-hard parts deliver proven reliability but are manufactured on process nodes 2–3 generations behind commercial GPUs, resulting in orders-of-magnitude lower AI compute throughput per watt. A data center using rad-hard processors would be non-competitive for GPU-class inference or training workloads. COTS GPUs with ECC offer modern compute but face unvalidated long-term TID reliability under continuous LEO flux.

## Design-Life Implications

Orbital electronics require replacement every **5–6 years** due to radiation-driven TID accumulation and displacement damage, even with shielding. This constraint is survivability-driven, not performance-driven — it would apply regardless of compute generation progress.

This compounds the [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]] problem: the hardware refresh penalty arises from both planned obsolescence (GPU generations) and radiation-imposed lifetime limits, and the two cycles may not align.

## Key Takeaways for Space Data Centers

1. SEU rates are manageable with ECC but add constant compute overhead for scrubbing
2. TID forces a 5–6 year replacement cadence independent of performance considerations
3. The rad-hard/COTS tradeoff is unresolved: no mission has operated commercial GPU clusters in LEO long-term
4. SAA pass frequency (once per ~90-min orbit) means daily radiation exposure cannot be avoided through orbit design alone at typical LEO altitudes

## Related Pages

- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
- [[wiki/concepts/space-datacenter-component-lifetimes.md]]
- [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]]
- [[wiki/sources/arxiv-2302-08952-leo-edge-failures.md]]
