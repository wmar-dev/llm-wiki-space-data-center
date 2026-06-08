---
title: "Orbital Debris and the Market for Satellites (Bongers & Torres, Ecological Economics 2023)"
type: "source_summary"
sources:
  - "1-s2.0-S0921800923000940-main.txt"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://doi.org/10.1016/j.ecolecon.2023.107831"
---

# Orbital Debris and the Market for Satellites (Bongers & Torres 2023)

**Authors**: Anelí Bongers, José L. Torres — Department of Economics, University of Málaga, Spain
**Journal**: Ecological Economics, Vol. 209 (2023), article 107831
**DOI**: 10.1016/j.ecolecon.2023.107831
**Access**: Open access (CC BY-NC-ND 4.0)
**Source type**: peer_reviewed

## Abstract

Studies the economic consequences of orbital debris for commercial outer-space activities.
Treats outer space as a global common resource where firms do not internalize the social
cost of orbital pollution. Develops a dynamic investment model for satellites, calibrates
it to current conditions, and derives a closed-form expression for the maximum number of
satellites that prevents the Kessler syndrome.

## Key Quantitative Results

| Metric | Value |
|--------|-------|
| Maximum satellites before Kessler syndrome (baseline) | **72,090** |
| Sensitivity range (debris decay rate 0.002–0.1) | 21,520 – 107,600 |
| Physical Kessler debris threshold (>1 cm pieces) | 1.57 × 10¹⁰ |
| Economic Kessler syndrome onset (debris level) | ~7.69 × 10⁹ (≈ ½ physical threshold) |
| Social cost of orbital debris externality | ~$11.5 billion/year |
| Satellites at calibration date (paper baseline) | ~5,600 operational |

## The Threshold Formula

The paper derives a closed-form expression (equation 28/29) for the maximum satellite count:

```
S_Kessler = δ_d / [θ(γ + ω/η)]
```

where:
- **δ_d**: debris decay rate (atmospheric drag; altitude-dependent)
- **θ**: probability of collision per unit of debris
- **γ**: debris fragments generated per satellite destroyed in collision
- **ω**: debris fragments generated per launch
- **η**: satellites per launch

The threshold is thus a function of five physical parameters. It is NOT a fixed constant —
it shifts with altitude (via δ_d), satellite size (via θ), and active debris removal policy
(which effectively increases δ_d).

## Economic Model Structure

- Competitive market of infinity-lived firms maximizing discounted profits
- Debris is a common-resource negative externality: firms do not internalize its social cost
- Collision probability proportional to debris quantity (𝜃D_t)
- Two debris sources: launches (ω per launch) and collisions (γ × fragments per collision)
- Debris self-propagation: debris collides with debris, producing more debris (𝜐θD_t²)
- Physical depreciation of satellites (δ_s) plus collision destruction (θD_t × S_t)

## Critical Limitations Explicitly Stated by Authors

1. **No active collision avoidance**: Model does not include Space Situational Awareness
   or evasive maneuvering — both "would have a significant impact in the determination of
   the maximum number of satellites."
2. **Orbit-averaged model**: The 72,090 figure is "an average for the different orbits
   and depends on the baseline calibration" — not altitude-specific.
3. **Representative satellite**: Model assumes homogeneous satellite mass/size; actual
   fleet has huge variance (cubesats to 8+ ton data centers).
4. **No ASAT / exogenous debris**: Military test debris (e.g., Fengyun-1C: +3,037 tracked
   fragments; Kosmos 1408: +1,500 fragments) is not in the baseline.

## Economic Kessler vs. Physical Kessler

A key finding: **economic Kessler syndrome occurs before physical Kessler syndrome**.
At debris level ~7.69 × 10⁹ pieces (roughly half the physical threshold of 1.57 × 10¹⁰),
the model's optimal satellite count falls to below 1 — space becomes economically
unprofitable for firms before it becomes physically unusable. This confirms Adilov et al.
(2018).

## Social Cost Estimate

The paper estimates the foregone satellite services from the debris externality at
approximately **$11.5 billion per year** under baseline conditions. As launch costs fall
and more satellites are launched, this cost rises because debris increases and more
satellites are destroyed.

## Implications for Space Data Centers

- The 72,090 number is calibrated to a "representative satellite" — likely close to
  Starlink-class (~260 kg). Large data center satellites (8,000–80,000 kg) with greater
  mass and cross-section consume more of the collision-risk budget per object.
- The formula shows the threshold scales inversely with θ (collision probability per unit
  debris), which scales with cross-sectional area. A 10-ton data center might have
  100× the cross-section of a cubesat, reducing the effective threshold proportionally.
- Active debris removal (increasing δ_d) can raise the threshold substantially.
  The sensitivity analysis shows the range 21,520–107,600 depending on the decay rate.

## Related Pages

- [[wiki/synthesis/starlink-above-kessler-limit.md]]
- [[wiki/synthesis/kessler-limit-calculation.md]]
- [[wiki/synthesis/orbital-capacity-fundamental-limit.md]]
- [[wiki/concepts/orbital-capacity-limits.md]]
