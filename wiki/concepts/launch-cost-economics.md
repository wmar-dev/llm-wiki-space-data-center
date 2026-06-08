---
title: "Launch Cost Economics"
type: "concept"
sources:
  - "spacex-launch-cost-analysis.md"
  - "orbital-systems-power-budget-2025.txt"
  - "space-based-solar-power.md"
status: "draft"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Launch Cost Economics

Launch cost — measured in $/kg to orbit — is the single largest variable determining space data center financial viability. The consensus threshold for economic viability is $100–200/kg [[wiki/sources/space-based-solar-power.md]] *(other)* [[wiki/sources/orbital-systems-power-budget-2025.md]] *(industry_report)*.

## Historical Trend

| Era | Vehicle | $/kg to LEO |
|---|---|---|
| Space Shuttle (1981-2011) | STS | ~$54,500 |
| Pre-reuse (2010s) | Falcon 9 expendable | ~$2,700 |
| Partial reuse (2020s) | Falcon 9 reusable | ~$1,500 |
| Partial reuse (2020s) | Falcon Heavy reusable | ~$1,500 |
| Full reuse (target) | Starship | $10–100 |

Based on [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)* and orbital-intel.com data.

## The Cost Equation

Launch cost per kg is determined by three variables:

`$/kg = (Build Cost / Reuses + Operations + Propellant) / Payload Mass`

### 1. Build Cost & Reuse Count

Build cost is amortized over the number of flights. This is the primary lever:

| Scenario | Build Cost | Reuses | Amortized/Fl | $/kg (200 t payload) |
|---|---|---|---|---|
| Expendable | $90M | 1 | $90M | $450 |
| Low reuse | $90M | 5 | $18M | $90 |
| Medium reuse | $50M | 10 | $5M | $25 |
| High reuse | $20M | 100 | $0.2M | $1 |

Build costs themselves decline with production scale (Wright's Law) from $90M to a projected $2-5M at high volume [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*.

### 2. Propellant (the floor)

Starship's 4,800 t of CH₄/LOX at ~$100/t → ~$500K per flight. Even if the vehicle were free, this sets an absolute floor of ~$3.3/kg (at 150 t payload). Propellant accounts for roughly one-third of the $10/kg target [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*.

### 3. Operations & Refurbishment

Ground crew, range fees, inspection, and maintenance. At high cadence: ~$1-3M per flight, contributing ~$5-15/kg.

## Why Full Reuse Matters

Falcon 9's partial reuse (booster only, upper stage expended) cannot push below ~30-40% of build cost per flight because a new upper stage is built each time. Starship's full reuse (both stages return) unlocks the next order-of-magnitude reduction [[wiki/sources/spacex-launch-cost-math.md]] *(blog post)*.

## Thresholds for Space Data Centers

| $/kg Regime | Implication |
|---|---|
| >$500/kg | Prohibitive — only specialized gov/mil payloads |
| $200–500/kg | Marginal — some niche orbital compute possible |
| $100–200/kg | Viability threshold — space data centers approach competitive |
| $10–100/kg | Transformative — 1 MW facility launch costs drop to $1-10M |
| <$10/kg | Disruptive — launch costs become minor line item |

Threshold from [[wiki/sources/space-based-solar-power.md]] [[wiki/sources/orbital-systems-power-budget-2025.md]]; projections from [[wiki/sources/spacex-launch-cost-math.md]].

## Related pages

- [[wiki/entities/spacex.md]]
- [[wiki/sources/spacex-launch-cost-math.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
