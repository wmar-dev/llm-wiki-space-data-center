---
title: "Do We Have Enough Launch Sites to Build a Space Data Center?"
type: "synthesis"
sources:
  - "spaceport-wikipedia.md"
  - "spacex-launch-cost-math.md"
  - "launches-required-space-datacenter.md"
  - "orbital-startup-economics-register-2026.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Do We Have Enough Launch Sites to Build a Space Data Center?

The answer depends on scale. For a single demonstration satellite the answer is
clearly yes. For a gigawatt-class constellation the answer is: not yet, and launch
site throughput is already a measurable bottleneck.

## Current Global Launch Infrastructure

Approximately 12+ countries operate orbital launch sites
[[wiki/sources/spaceport-wikipedia.md]] *(other)*:

| Region | Sites |
|---|---|
| Russia / Kazakhstan | Baikonur, Plesetsk, Vostochny |
| United States | Cape Canaveral / KSC (FL), Vandenberg (CA), Starbase / Boca Chica (TX) |
| China | Jiuquan, Taiyuan, Wenchang, Xichang |
| India | Satish Dhawan |
| Japan | Tanegashima, Uchinoura |
| Europe | Guiana Space Centre (French Guiana) |
| Others | New Zealand (Rocket Lab), South Korea, Israel, Iran, Australia |

Additional sites are proposed in Canada, India, Indonesia, Japan, Sweden, and
the UK [[wiki/sources/spaceport-wikipedia.md]] *(other)*.

## The Congestion Problem Is Already Real

**Key finding**: In January 2025 — before any significant space data center
launches had occurred — the US already experienced **traffic congestion at rocket
launch sites** due to rising launch rates from SpaceX and Blue Origin. Three sites
in Florida and California handle the majority of US launches
[[wiki/sources/spaceport-wikipedia.md]] *(other)*.

This is significant: congestion appeared at current launch cadences, which are
dominated by Starlink replenishment and commercial satellite missions — not space
data centers. Adding data center payloads to this queue compounds the bottleneck.

## Scale Analysis: Sites vs. Required Cadence

From [[wiki/synthesis/launches-required-space-datacenter.md]]:

| Data Center Scale | Estimated Total Mass | Starship Launches Required |
|---|---|---|
| 60 kg demo satellite | 60 kg | 1 (rideshare) |
| 1 MW operational node | 41–88 t | 1–2 |
| 100 MW facility | ~4,000–8,800 t | ~27–59 |
| 5 GW constellation | ~26,000–88,000 t | ~175–590 |

### Near-Term (Single Satellite / 1 MW node): Capacity Exists

A single data center satellite or a 1 MW node requires 1–2 launches, well within
the current global capacity of 200+ orbital launches per year (Inference: based on
2023 global launch cadence; not cited from a wiki source). Any operational launch
site with appropriate vehicle availability can handle this.

### Medium-Term (100 MW facility): Manageable but Constrained

27–59 Starship launches for 100 MW represents roughly half of SpaceX's current
Falcon 9 annual cadence applied to Starship — achievable over 2–3 years at
projected Starship rates, but it would consume a significant fraction of US
launch site throughput. Vandenberg and Boca Chica are the most likely sites;
Cape Canaveral pads are already heavily scheduled.

### Long-Term (GW-scale constellation): Not Supported by Current Infrastructure

175–590 Starship launches for 5 GW is a multi-year, potentially decade-long
campaign. The binding constraint is not the existence of launch sites but:

1. **Launch pad throughput**: Each pad requires hours to days of turnaround time
   between flights. Even at ambitious cadences (Starship targeting 40+ flights
   per year from Boca Chica), 590 launches ≈ 15 years from a single pad.

2. **Range scheduling**: US Eastern and Western ranges operate fixed daily windows;
   regulators must certify each launch. At current bureaucratic throughput, 590
   launches would take far longer than the vehicle and pad could theoretically
   support.

3. **International dependence**: China's four launch sites provide the only
   significant non-US orbital launch capacity. A US-based company cannot easily
   use Chinese facilities; conversely, China's Xingshidai data center program
   [[wiki/sources/space-data-center-wikipedia.md]] *(other)* is not launch-constrained
   by US infrastructure.

## The Real Bottleneck: Cadence, Not Site Count

The launch site question reframes as a launch **cadence** question:

- Sites exist globally and are sufficient for near-term (1–10 launch) deployments.
- **The binding constraint for GW-scale buildout is not the number of pads but
  the rate at which those pads can be turned around, scheduled through regulatory
  bodies, and loaded with payloads.**

Inference: If Starship achieves its target of 40–100 flights per year from
Boca Chica by 2028, and China expands Wenchang similarly, the global launch
cadence would be sufficient for 100 MW class deployments within ~5 years — but
only if most of that cadence is dedicated to space data center launches.

## The Regulatory Bottleneck

Open question: Launch site capacity is also gated by regulatory approval. The
FAA environmental review for Starbase took years; SpaceX has argued that launch
licensing is a binding rate constraint independent of vehicle and pad readiness.
No source in the wiki quantifies regulatory throughput as a specific number of
launches per year.

## Summary

| Question | Answer |
|---|---|
| Enough sites for a demo satellite? | **Yes — trivially** |
| Enough sites for a 1 MW node? | **Yes — 1-2 Starship launches** |
| Enough sites for 100 MW? | **Manageable — 3-5 year program** |
| Enough sites for GW constellation? | **No — cadence, regulation, and international access are all binding constraints** |
| Are US sites already congested? | **Yes — congestion reported January 2025, before data center launches** |

## Open Questions

- What is the actual annual launch capacity (in launches per year) of each major
  US pad, accounting for turnaround, weather, and range scheduling constraints?
- How does FAA launch licensing throughput scale with launch demand — is there a
  regulatory ceiling independent of physical pad capacity?
- Could maritime or aerial launch platforms (e.g., SpaceX drone ships, Rocket Lab
  Neutron maritime) relieve pad congestion for data center payloads?

## Related Pages

- [[wiki/synthesis/launches-required-space-datacenter.md]]
- [[wiki/sources/spaceport-wikipedia.md]]
- [[wiki/concepts/launch-cost-economics.md]]
- [[wiki/synthesis/spacex-starship-cost-breakdown.md]]
- [[wiki/sources/space-data-center-wikipedia.md]]
