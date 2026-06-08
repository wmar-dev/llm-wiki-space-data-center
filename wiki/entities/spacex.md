---
title: "SpaceX"
type: "entity"
sources:
  - "spacex-launch-cost-analysis.md"
status: "draft"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# SpaceX

Space Exploration Technologies Corp. (SpaceX) is the dominant commercial launch provider and the key enabler of space data center economics through Starship, a fully reusable super-heavy launch vehicle.

## Starship Economics

Starship's cost targets are the central variable in space data center financial viability. The vehicle is designed to be fully reusable (both stages), targeting $10–100/kg to LEO [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)* — a 20–200× reduction from Falcon Heavy's ~$2,000/kg [[wiki/sources/space-based-solar-power.md]] *(other)*.

### Cost Reduction Levers

1. **Full reusability**: Both Super Heavy booster and Starship upper stage return to Earth, unlike Falcon 9 which expends its upper stage. This is the single largest factor. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

2. **Engine mass production**: Raptor engines targeted to drop from ~$1M → $250K each at 4,000 engines/year production. A full stack uses 39 engines, so engine cost falls from $39M to ~$10M. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

3. **Low material cost**: Stainless steel construction at ~$5/kg → ~$1.5M for a full stack's raw steel. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

4. **High flight rate**: Spreading fixed production costs over hundreds of flights per year. Mass production of 100–400 ships/year could spread fixed costs 40× over current. [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

5. **Vertical integration**: 85–90% of components produced in-house, reducing external procurement by 20–40%.

### Projected Cost Trajectory

| Year/Build | Build Cost | Reuses | $/kg to LEO |
|---|---|---|---|
| 2024 | $90M | 1 (expendable) | ~$450 |
| 2024-25 | $90M | 5 | ~$90 |
| 2025-26 | $50M | 10 | ~$25 |
| 2027-28 | $20M | 100 | ~$10 |
| Future | $2–5M | 100+ | ~$10 |

Based on [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*

### Falcon 9 as Precedent

Falcon 9 boosters now routinely fly 20+ times, with certification underway for 40 reuses and a goal of 100. This demonstrated reuse curve underpins the Starship projections. However, Falcon 9 is fundamentally limited to ~30–40% of build cost per flight because its upper stage is expended [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)* — Starship's full reuse eliminates this floor.

## Related pages

- [[wiki/sources/spacex-launch-cost-math.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/sources/orbital-systems-power-budget-2025.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
