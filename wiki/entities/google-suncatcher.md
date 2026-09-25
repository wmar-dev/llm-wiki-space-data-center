---
title: "Google — Project Suncatcher"
type: "entity"
sources:
  - "google-suncatcher-research-technical.md"
  - "google-suncatcher-announcement-blog.md"
  - "scientific-american-space-datacenters.md"
status: "current"
created: "2026-09-24"
last_updated: "2026-09-24"
---

# Google — Project Suncatcher

Google's research moonshot exploring a space-based, TPU-powered AI compute cluster.
Backed by Google's balance sheet and TPU supply chain rather than external venture
funding, distinguishing it from the startup cohort tracked elsewhere in this wiki
[[wiki/synthesis/space-datacenter-companies-landscape.md]].

## Profile

- **Chip**: Google Trillium v6e Cloud TPU — the only tracked entrant using a
  proprietary AI accelerator rather than an NVIDIA GPU
  [[wiki/sources/google-suncatcher-research-technical.md]]
- **Illustrative architecture**: 81-satellite cluster, 1 km radius, ~650 km
  sun-synchronous dawn-dusk orbit [[wiki/sources/google-suncatcher-research-technical.md]]
- **Radiation posture**: 67 MeV proton testing shows TPU/HBM tolerance to ~3× the
  anticipated 5-year mission dose; no hard TID failures observed up to 15 krad(Si)
  [[wiki/sources/google-suncatcher-research-technical.md]]
- **Inter-satellite links**: 800 Gbps each-way demonstrated (1.6 Tbps total),
  targeting tens-of-Tbps aggregate for distributed training/inference
  [[wiki/sources/google-suncatcher-research-technical.md]]
- **Launch cost threshold**: <$200/kg by the mid-2030s
  [[wiki/sources/google-suncatcher-research-technical.md]],
  [[wiki/sources/scientific-american-space-datacenters.md]] *(news_article)*
- **Timeline**: Two prototype satellites with Planet by early 2027
  [[wiki/sources/google-suncatcher-research-technical.md]]
- **Status**: No hardware in orbit yet as of this writing (Sept 2026); feasibility
  study published November 2025 [[wiki/sources/scientific-american-space-datacenters.md]]
  *(news_article)*

## How It Compares to Other Entrants

Unlike Starcloud (hardware in orbit since Nov 2025) and Orbital (a16z-backed, PoC
2027), Suncatcher is still at the pre-flight feasibility/testing stage — Google has
not yet flown compute hardware, only ground-based radiation testing of the TPU
itself. Its differentiators are (1) a proprietary chip with radiation test data
more favorable than published COTS GPU figures for the H100
[[wiki/concepts/cots-vs-rad-hard-computing.md]], and (2) Google's existing TPU
manufacturing and software stack, which none of the GPU-based startups can draw on.

Its stated economic threshold (<$200/kg by mid-2030s) matches the figure used by
Orbital's CEO and the broader industry consensus threshold documented in
[[wiki/synthesis/space-datacenter-key-risks-analysis.md]] — Suncatcher is not
claiming a more favorable economic case than competitors, just working from the
same launch-cost assumption.

## Open Questions

- Open question: Has Google disclosed a thermal management architecture for
  Suncatcher satellites at TPU-cluster power densities?
- Open question: What is Suncatcher's target aggregate power (MW/GW) beyond the
  81-satellite illustrative design, and on what timeline?

## Related Pages

- [[wiki/sources/google-suncatcher-research-technical.md]]
- [[wiki/sources/scientific-american-space-datacenters.md]]
- [[wiki/synthesis/space-datacenter-companies-landscape.md]]
- [[wiki/synthesis/hardware-refresh-penalty-space-compute.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
