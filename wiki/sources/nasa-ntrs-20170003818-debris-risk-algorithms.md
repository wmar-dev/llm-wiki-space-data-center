---
title: "Debris Risk Computation Algorithms (NASA NTRS 20170003818)"
type: "source_summary"
sources:
  - "nasa-ntrs-20170003818.pdf"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Debris Risk Computation Algorithms (NASA NTRS 20170003818)

**Author**: Mark J. Matney, NASA Orbital Debris Program Office, Johnson Space Center
**Source type**: peer_reviewed (NASA technical report with numbered references, abstract, mathematical derivations)
**Origin URL**: https://ntrs.nasa.gov/api/citations/20170003818/downloads/20170003818.pdf
**Processing status**: processed
**Ingest count**: 1

## Summary

This paper presents the statistical algorithms underlying NASA's Orbital Debris Engineering Model (ORDEM 3.0) and related tools for computing collision probabilities and ground re-entry casualty risk. The algorithms rederive the Kessler spatial density equations from first principles, then extend them to handle circular orbits, 2D disc distributions, and specific orbit pairs.

## Key Claims

- Debris collision risk is computed using spatial density × relative velocity → flux → number of collisions per unit area per unit time. — *peer_reviewed*
- The Kessler spatial density equation gives the probability distribution of finding a debris object at a given orbital radius r, latitude λ, and longitude φ, assuming uniformly distributed ascending nodes and argument of periapsis. — *peer_reviewed*
- Singular (infinite) density values arise at periapsis, apoapsis, and extreme latitudes in single-orbit PDFs; the correct solution is to integrate over a distribution of orbital elements rather than a single orbit. — *peer_reviewed*
- NASA ORDEM 3.0 uses a distribution in periapsis radius, eccentricity, and inclination to model the debris population; this eliminates the infinite-density problem in numerical calculations. — *peer_reviewed*
- For two populations of circular orbits at inclinations i₁ and i₂, the collision flux depends on the incomplete elliptic integral of the first kind K; a high-flux ridge exists where i₁ + i₂ = 180° (counter-rotating, potentially coplanar orbits). — *peer_reviewed*
- The 2D "disc" model reduces to the full 3D Kessler density when the disc is averaged over all ascending nodes; a "caterpillar" model (linear density with Gaussian fuzz) handles cases where specific orbit pairs have fixed nodes. — *peer_reviewed*
- Latitude distribution equations (Eq. 8) are used to estimate the fraction of re-entry time a satellite spends over populated areas, enabling ground casualty risk estimates. — *peer_reviewed*
- The Second Euler-Maclaurin summation formula is recommended for numerical integration near density singularities. — *peer_reviewed*

## Quantitative Relationships

| Parameter | Formula / Value |
|-----------|----------------|
| Spatial density (general) | ρ(r,λ,φ) = [1 / (2π³ r a)] × [1 / √(sin²(i)−sin²(λ))] × [1 / √((rA−r)(r−rP))] |
| Circular orbit spatial density | ρ(r,λ,φ) = D(r) / [2π² r² √(sin²(i)−sin²(λ))] |
| Flux between two circular-orbit populations | Involves elliptic integral K; peaks when inclinations are supplementary |
| Re-entry latitude distribution | p(λ) dλ = cos(λ) dλ / [π √(sin²(i)−sin²(λ))] — exact analytic form |

## Relevance to Space Data Centers

The ORDEM 3.0 model is the operational tool NASA uses to assess debris flux for specific satellite designs and orbits. For space data center risk assessment:

- **LEO is higher debris flux**: At 550 km SSO (Starlink/Starcloud orbit), the inclination (~98°) means counter-rotating encounters with equatorial and mid-inclination debris populations — near the high-flux ridge.
- **Size matters quadratically**: Flux scales with cross-sectional area; a large data center satellite (much larger than a typical comsat) has collision probability proportional to its area.
- Inference: The ORDEM framework implies debris collision probability for a 1 MW orbital data center (large structure, ~100s m²) could be orders of magnitude higher than for a typical 5–10 m² cubesat.
- **SSO dawn-dusk orbits** used by Starcloud create near-supplementary inclination geometry with lower-inclination debris — the highest-flux regime per the analytic formula in Eq. 24.

## Gaps / Open Questions

- Open question: What is the ORDEM 3.0-predicted annual collision probability for a representative space data center satellite (e.g., 200 m² cross-section at 550 km SSO)?
- The paper does not quantify the actual debris flux density at specific altitudes — ORDEM 3.0 outputs are not published in this paper; only the algorithms are described.

## Related Pages

- [[wiki/sources/kessler-syndrome-wikipedia.md]]
- [[wiki/sources/space-debris-wikipedia.md]]
- [[wiki/concepts/orbital-capacity-limits.md]]
- [[wiki/synthesis/orbital-capacity-fundamental-limit.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
