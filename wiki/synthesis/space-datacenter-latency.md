---
title: "Space Data Center Latency vs. Terrestrial Cloud"
type: "synthesis"
sources:
  - "satellite-internet-latency-wikipedia.md"
  - "arxiv-2302-08952-leo-edge-failures.md"
  - "leo-isl-handoff-latency-2025.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Space Data Center Latency vs. Terrestrial Cloud

Latency is the key determinant of which compute workloads a space data center can
serve competitively. The analysis has two layers: (1) the physics of signal
propagation to orbit, and (2) real-world measured latency for satellite links at
comparable altitudes.

## Physics Baseline: Propagation Delay

Signal travel time at the speed of light (~300,000 km/s):

| Orbit | Altitude | One-Way Propagation | Round-Trip (propagation only) |
|---|---|---|---|
| LEO (Starlink/data center) | 550 km | ~1.8 ms | ~3.7 ms |
| MEO (O3b) | 8,062 km | ~27 ms | ~54 ms |
| GEO | 35,786 km | ~119 ms | ~238 ms |

Pure propagation at LEO is not a fundamental barrier — 3.7 ms round-trip is
comparable to a cross-datacenter link within a major city.

## Real-World Latency: Starlink as Proxy

The best available proxy for LEO space data center link latency is the Starlink
constellation, operating at the same 550 km altitude:

- **Measured RTT (2021)**: **45 ms average** [[wiki/sources/satellite-internet-latency-wikipedia.md]]
- **Premium over terrestrial (2022)**: **1.8–22.8 ms above equivalent terrestrial networks** [[wiki/sources/satellite-internet-latency-wikipedia.md]]
- Iridium and Globalstar (lower-altitude LEO): **<40 ms RTT** [[wiki/sources/satellite-internet-latency-wikipedia.md]]

The gap between theoretical propagation (~3.7 ms) and measured performance (~45 ms)
reflects ground-station processing, queuing, protocol overhead, and handoff between
moving satellites. A space data center would face the same overheads.

## Comparison: Space vs. Terrestrial Cloud

| Scenario | Typical RTT | Notes |
|---|---|---|
| Same-region terrestrial cloud | 1–10 ms | Intra-datacenter or metro fiber |
| Cross-region terrestrial cloud | 20–100 ms | Depends on distance, routing |
| Transcontinental internet | 70–150 ms | NYC–London ~70 ms |
| LEO space data center (~550 km) | **~40–70 ms** | Starlink proxy; computation adds to this |
| MEO | ~125 ms | O3b measured [[wiki/sources/satellite-internet-latency-wikipedia.md]] |
| GEO space data center | **1,000–1,400 ms** | Excludes all real-time workloads [[wiki/sources/satellite-internet-latency-wikipedia.md]] |

The orbital regime synthesis puts LEO round-trip at **~5–25 ms**
[[wiki/synthesis/space-datacenter-orbital-regime.md]] — this is likely the
propagation-only estimate. Real-world total latency (including link overhead) is
better proxied by the Starlink 45 ms figure.

## Space Data Center vs. Terrestrial Cloud: A Special Consideration

A space data center is not a relay — data travels up, computation occurs in orbit,
and results return. This means users experience **two uplink/downlink legs** plus
compute time:

```
User → Ground Station → Satellite (uplink) → Compute → Satellite (downlink) → Ground Station → User
```

Inference: Total user-perceived latency for a LEO compute request ≈ 2 × satellite
link latency + compute time ≈ 90 ms + compute time. For batch or near-real-time
workloads this is acceptable; for sub-50 ms interactive workloads it is not.

## Visibility and Continuity

A LEO satellite at 550 km travels at ~7.8 km/s and is visible from a fixed ground
point for only **~5–10 minutes per pass**. Continuous compute access requires either:

- A large constellation with inter-satellite links (ISLs), like Starlink's approach
- Ground-station handoff coordination to relay in-flight jobs

Handoff latency between ground stations for LEO satellites is typically <10 ms penalty based on ISL-optimized routing studies [[wiki/sources/leo-isl-handoff-latency-2025.md]] *(research synthesis)*. LEO satellite networks with inter-satellite links (ISLs) can achieve total end-to-end latency of 20-30 ms, with handoff contributing minimal additional delay. ISL-based routing reduces ground-station dependency and the need for frequent handoffs. The job migration cost during ISL-based computation — where a compute job must checkpoint and transfer between satellites — has not been quantified in available sources, but ISL link speeds (optical: >1 Gbps) suggest it would be dominated by serialization delay for typical job state sizes.

## Workload Implications

| Workload Type | LEO Viable? | GEO Viable? | Reason |
|---|---|---|---|
| Batch analytics, ML training | Yes | Marginal | Tolerates 90+ ms latency |
| Remote sensing processing (edge) | Yes | No | Data already in orbit; no uplink needed |
| Low-latency transactions, gaming | No | No | <50 ms required |
| Interactive APIs, web serving | Marginal | No | 90 ms ceiling is borderline |
| Video transcoding / rendering | Yes | No | Throughput-bound, not latency-bound |

[[wiki/sources/arxiv-2302-08952-leo-edge-failures.md]] identifies LEO edge computing
as a distinct use case where the satellite processes data already captured in orbit
(e.g., Earth observation imagery) rather than serving latency-sensitive ground
requests — this is the lowest-latency scenario since no uplink is required.

## Open Questions

- ~~What is the actual handoff latency when a space data center satellite moves out of
  a ground station's field of view?~~ *(resolved — <10 ms penalty with ISL routing)*
- Can ISL-connected constellations deliver consistent sub-50 ms compute latency for
  interactive workloads, or does ISL routing add too much variability?

## Related Pages

- [[wiki/synthesis/space-datacenter-orbital-regime.md]]
- [[wiki/sources/satellite-internet-latency-wikipedia.md]]
- [[wiki/sources/arxiv-2302-08952-leo-edge-failures.md]]
- [[wiki/synthesis/leo-latency-commercial-use-cases.md]]
