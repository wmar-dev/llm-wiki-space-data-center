---
title: "Project Suncatcher: Space-Based AI Infrastructure System Design (Google Research)"
type: "source_summary"
sources:
  - "google-suncatcher-research-technical.md"
  - "google-suncatcher-announcement-blog.md"
status: "current"
created: "2026-09-24"
last_updated: "2026-09-24"
origin_url: "https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/"
domain_relevance: "primary"
---

# Project Suncatcher: Space-Based AI Infrastructure System Design

**Source**: Google Research (technical blog + companion announcement on The Keyword)
**Source type**: industry_report *(primary corporate source, not peer-reviewed)*
**Origin URL**: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/

## Summary

Google's own technical account of Project Suncatcher — an illustrative 81-satellite
AI-compute cluster design — plus the companion product announcement confirming a
near-term hardware validation flight with Planet.

## Key Claims

**Constellation architecture** (illustrative design, not a committed deployment plan):
- 81 satellites in a sun-synchronous LEO at ~650 km altitude
- Cluster radius ~1 km; next-nearest-neighbor spacing 100–200 m
- Dawn-dusk sun-synchronous orbit chosen to maximize solar exposure and minimize
  battery/eclipse cycling — same rationale already documented for Starcloud
  [[wiki/concepts/eclipse-cycling-power-budget.md]]

**Hardware and radiation testing**:
- Chip: Google's Trillium v6e Cloud TPU (not a GPU — distinct from every other
  orbital compute entrant tracked in this wiki, which fly NVIDIA GPUs)
- 67 MeV proton beam testing: HBM irregularities only appeared at 2 krad(Si) —
  ~3× the anticipated 5-year mission dose (750 rad(Si) with shielding)
- No hard TID failures up to the maximum tested dose of 15 krad(Si)
- *(Compare [[wiki/concepts/radiation-environment-seu-tid.md]] and
  [[wiki/concepts/cots-vs-rad-hard-computing.md]], which document COTS GPU
  vulnerability data for the H100; Suncatcher's TPU radiation results are
  meaningfully more favorable than published H100 figures, though methodology
  differs and is not directly comparable device-for-device.)*

**Inter-satellite links**:
- Target: tens of Tbps aggregate for data-center-scale distributed ML
- Early validation: 800 Gbps each-way (1.6 Tbps total) via dense WDM + spatial
  multiplexing
- Close formation flying (km-scale or less) needed to manage free-space optical
  signal attenuation

**Thermal management**: Explicitly flagged as a significant open engineering
challenge; no architecture detail disclosed.

**Launch cost threshold**: <$200/kg by the mid-2030s, framed as the point where
space-based infrastructure becomes cost-competitive with terrestrial data centers
on a per-kW-year basis — consistent with the figure previously reported secondhand
via Scientific American [[wiki/sources/scientific-american-space-datacenters.md]]
*(news_article)*.

**Timeline**: Two prototype satellites launching with Planet by early 2027 to
validate formation flying, hardware survivability, and optical ISL performance.
*(A separate Sept 2026 news report indicates a first single-satellite hardware
test — 4 TPUs aboard a SpaceX Transporter rideshare — precedes the two-satellite
Planet mission; not yet independently verified from a primary source.)*

## Open Questions

- Open question: What thermal management architecture will Suncatcher satellites
  use at TPU power densities, given Google has not disclosed a radiator design?
- Open question: How does the 81-satellite/1km-cluster design scale to
  commercially meaningful aggregate power (MW+), and what does that imply for
  total constellation count?

## Related Pages

- [[wiki/entities/google-suncatcher.md]]
- [[wiki/sources/scientific-american-space-datacenters.md]]
- [[wiki/synthesis/space-datacenter-companies-landscape.md]]
- [[wiki/concepts/cots-vs-rad-hard-computing.md]]
