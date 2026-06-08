---
title: "SpaceX Starship Cost Breakdown"
type: "synthesis"
sources:
  - "spacex-launch-cost-analysis.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# SpaceX Starship Cost Breakdown

**Query**: What is the detailed cost breakdown of SpaceX Starship?

## Build Cost Trajectory

Starship's build cost per stack declines with production scale through Wright's Law:

| Year | Build Cost | Driver |
|------|-----------|--------|
| 2024 | $90M | Initial low-volume production |
| 2025 | $50M | Early mass production ramp |
| 2027 | $20M | High-volume production |
| Future | $2–5M | Mature mass production |

[[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

## Component Cost Breakdown

| Component | Current | Target (Mass Production) |
|-----------|---------|-------------------------|
| **Raptor engines** (39/stack) | ~$1M each = $39M | ~$250K each = ~$10M |
| **Stainless steel** (~$5/kg) | ~$1.5M (raw material) | ~$1.5M (material floor) |
| **Rest of vehicle** (tooling, avionics, TPS, assembly) | ~$49.5M | ~$8.5M |
| **Total build cost** | **$90M** | **~$20M** |

Raptor factory targets 4,000 engines/year capacity. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

Stainless steel at ~$5/kg — ~$1.5M for the raw steel of a full Super Heavy + Starship stack. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

## Per-Flight Cost Equation

From [[wiki/concepts/launch-cost-economics.md]]:

`$/kg = (Build Cost / Reuses + Operations + Propellant) / Payload Mass`

### Reuse Scenarios

| Scenario | Build Cost | Reuses | Amortized Build | Ops | Propellant | Total/Flight | $/kg (200 t) |
|----------|-----------|--------|---------------|-----|-----------|-------------|------|
| Expendable (2024) | $90M | 1 | $90M | $2M | $0.5M | ~$92.5M | ~$450 |
| 5 reuses (2024-25) | $90M | 5 | $18M | $2M | $0.5M | ~$20.5M | ~$90 |
| 10 reuses (2025-26) | $50M | 10 | $5M | $2M | $0.5M | ~$7.5M | ~$25 |
| 100 reuses (2027-28) | $20M | 100 | $0.2M | $2M | $0.5M | ~$2.7M | ~$10 |
| Future expendable | $2M | 1 | $2M | $2M | $0.5M | ~$4.5M | ~$15 |

[[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*, [[wiki/concepts/launch-cost-economics.md]]

### Propellant (the floor)

Starship's 4,800 t of CH₄/LOX at ~$100/t → ~$500K per flight. Even if the vehicle were free, this sets an absolute floor of ~$3.3/kg (at 150 t payload). Propellant accounts for roughly one-third of the $10/kg target. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*, [[wiki/concepts/launch-cost-economics.md]]

### Operations & Refurbishment

Ground crew, range fees, inspection, maintenance. At high cadence: ~$1-3M per flight, contributing ~$5-15/kg. [[wiki/concepts/launch-cost-economics.md]]

## Cost Reduction Levers

From [[wiki/entities/spacex.md]]:

1. **Full reusability** — Both Super Heavy booster and Starship upper stage return. Unlike Falcon 9 (expended upper stage, capped at ~30–40% of build cost per flight), full reuse unlocks the next order-of-magnitude reduction.

2. **Engine mass production** — Raptor engines targeted from ~$1M → $250K each at scale. A full stack uses 39 engines, so engine cost falls from $39M to ~$10M.

3. **Low material cost** — Stainless steel at ~$5/kg.

4. **High flight rate** — Spreading fixed costs over hundreds of flights per year.

5. **Vertical integration** — 85–90% of components produced in-house.

## Comparison to Falcon 9

| Vehicle | Reuse Model | Build Cost/Flight | $/kg |
|---------|-----------|-------------------|------|
| Falcon 9 | Booster only (upper stage expended) | ~$15M (booster amortized + new upper stage) | ~$1,500 |
| Starship target | Full reuse (both stages) | ~$2.7M | ~$10 |

Falcon 9 boosters routinely fly 20+ times, with 40-reuse certification and a 100-reuse goal. This demonstrates the reuse curve, but the expended upper stage creates a structural floor that Starship's full reuse eliminates. [[wiki/entities/spacex.md]]

## Open Questions

- No source in the wiki provides verified operational Starship cost data from actual flights (Starship has not yet reached operational reuse cadence). All figures are projections from a blog post citing SpaceX public statements.
- The $2-5M future build cost assumes production volumes not yet demonstrated in aerospace.

## Related pages

- [[wiki/sources/spacex-launch-cost-math.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/entities/spacex.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
