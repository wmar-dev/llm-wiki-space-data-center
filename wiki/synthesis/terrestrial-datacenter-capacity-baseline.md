---
title: "Global Data Center Capacity — Current and Projected Terrestrial Baseline"
type: "synthesis"
sources:
  - "global-datacenter-capacity-wikipedia.md"
  - "xai-colossus-wikipedia.md"
  - "space-data-center-wikipedia.md"
  - "scientific-american-space-datacenters.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Global Data Center Capacity — Current and Projected Terrestrial Baseline

Understanding the terrestrial baseline is essential context for evaluating space
data center ambitions. The numbers reveal a stark scale asymmetry.

## Current Global Capacity (2024)

| Metric | Figure |
|---|---|
| Hyperscale data centers globally | **1,136** (end of 2024; doubled over 5 years) |
| US data centers (all types) | **5,381** (March 2024) |
| Colocation centers worldwide | **4,799** in 127 countries |
| US electrical demand | **~17 GW** (2022) |
| Global power consumption | **415–620 TWh/year** (~1.5% of global electricity) |
| Market concentration | Top 3 (AWS, Azure, Google Cloud) = **~59% of hyperscale capacity** |

[[wiki/sources/global-datacenter-capacity-wikipedia.md]] *(other)*

## Projected Growth to 2030

| Metric | 2022/2024 Baseline | 2030 Projection | Growth |
|---|---|---|---|
| US electrical demand | 17 GW | **35 GW** | 2× |
| Global consumption | 415–620 TWh | **~945 TWh** (IEA base case) | ~2× |
| US share of electricity | ~2–3% | **4.6–9.1%** | 2–3× |

The IEA projects global data center consumption could **double by 2030**, driven
primarily by AI workloads [[wiki/sources/global-datacenter-capacity-wikipedia.md]] *(other)*.

## AI as the Growth Driver

A single 100 MW AI data center consumes as much electricity as **100,000 households**
[[wiki/sources/global-datacenter-capacity-wikipedia.md]] *(other)*. At current growth
rates (US demand from 17 GW → 35 GW in 8 years), the industry is adding roughly
2–3 GW of new US capacity per year.

xAI's Colossus (150 MW current, ~300 MW planned, built in 122 days) is the leading
data point for how fast AI-specific compute clusters can scale
[[wiki/sources/xai-colossus-wikipedia.md]] *(other)*. If xAI reaches its "nearly
2 GW" compute expansion target, that single facility would represent ~6% of the
entire 2022 US data center power demand.

## Putting Space Data Center Ambitions in Context

| Entity | Capacity Target | Timeline |
|---|---|---|
| US terrestrial (current) | **17 GW** | 2022 (baseline) |
| US terrestrial (projected) | **35 GW** | 2030 |
| xAI Colossus target | **~2 GW** compute | Under construction (2025–2026) |
| Starcloud (orbital) | **5 GW** | 2035 target |
| Orbital (orbital, per satellite) | **100 kW** | PoC 2027 |
| Google Suncatcher (orbital) | TBD | Feasibility by 2035 |

[[wiki/sources/space-data-center-wikipedia.md]], [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*

**Key finding**: The US alone adds ~2–3 GW of new terrestrial data center capacity
*per year*. Starcloud's entire 5 GW orbital target by 2035 is equivalent to about
two years of US terrestrial growth — yet Starcloud's timeline is 9 years and its
economics are not yet viable.

## The Scale Gap Is Not Closing Near-Term

Inference: Even in the optimistic scenario where orbital data centers achieve 5–10 GW
by 2035, terrestrial capacity will be growing faster in absolute terms. By 2035, US
terrestrial data center demand is likely to exceed 50–70 GW (extrapolating the
doubling from 2022 to 2030). Orbital compute at 5–10 GW would represent
**7–20% of projected US demand** at that point — significant but not dominant.

The more realistic near-term framing for orbital data centers is as a
**specialized complement** to terrestrial infrastructure rather than a competitor:
serving workloads that require orbital data locality, jurisdiction independence,
or global coverage that no terrestrial topology can match
[[wiki/synthesis/space-datacenter-workload-types.md]].

## Environmental Pressure as a Wild Card

Terrestrial data centers face growing constraints:
- Power grid saturation (US demand at 4.6–9.1% of electricity by 2030)
- Water consumption (~2M litres/day per 100 MW)
- Community opposition to fossil-fueled buildout (xAI Colossus methane generator controversy)

Inference: If terrestrial grid access and water rights become binding constraints
for hyperscalers in the 2030s, space solar — with no water cooling and unlimited
solar power — gains relative attractiveness beyond the current economics argument.
Whether this happens on a timescale relevant to space data center investment is
an open question.

## Open Questions

- What is the global (not just US) data center electrical capacity in GW? The wiki
  has US figures (17 GW) and global energy consumption (415–620 TWh) but not a
  global GW figure from a primary source.
- How fast is hyperscale capacity growing in China, given Xingshidai is already
  operating an orbital data center constellation?
- At what terrestrial power density (GW/km²) does physical land scarcity become a
  constraint — and does that create an addressable niche for orbital compute?

## Related Pages

- [[wiki/sources/global-datacenter-capacity-wikipedia.md]]
- [[wiki/synthesis/xai-colossus-vs-space-datacenters.md]]
- [[wiki/synthesis/space-datacenter-workload-types.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
- [[wiki/sources/scientific-american-space-datacenters.md]]
