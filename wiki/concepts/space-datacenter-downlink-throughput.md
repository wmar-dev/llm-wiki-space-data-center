---
title: "Data Downlink Throughput as a Space Data Center Constraint"
type: "concept"
sources:
  - "china-120gbps-laser-downlink-2026.md"
  - "orbital-datacenter-technical-analysis-2026.md"
  - "satsearch-isl-terminals-2025.md"
  - "satellite-internet-latency-wikipedia.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Data Downlink Throughput as a Space Data Center Constraint

## Why Downlink Is a Binding Constraint

A space data center that processes data must still transmit results to terrestrial customers. Unlike terrestrial cloud infrastructure — where compute and customers are connected by petabit fiber — an orbital facility is limited to intermittent contact windows with ground stations. This creates a fundamental asymmetry: compute capacity may be large, but output bandwidth is structurally constrained by orbital mechanics and antenna technology.

## Contact Window Physics

At 550 km LEO, a satellite passes over a given ground station at roughly 7 km/s. With a 10° minimum elevation mask, the contact window geometry gives:

| Altitude | Typical pass duration | Passes per day (single GS) |
|---|---|---|
| 400 km | ~6–8 min | 3–5 |
| 550 km | ~8–12 min | 2–4 |
| 1,200 km | ~12–18 min | 1–3 |
| GEO | Continuous | Continuous |

**Note:** "Passes per day" is for a single ground station. A global network of ground stations (like Amazon Ground Station or AWS Ground Station) can dramatically increase coverage — a polar ground station pair can receive every orbit for a polar-inclination satellite.

## Achievable Throughput by Link Technology

### Radio Frequency (RF) Downlinks
- Ka-band (26.5–40 GHz): 1–5 Gbps per link under good conditions
- V-band (40–75 GHz): up to 10 Gbps; higher rain attenuation
- X-band (legacy): 300–800 Mbps

### Optical / Laser Downlinks (State of Art 2025–2026)
- DLR OSIRIS v3: 10–100 Gbps, ~5 kg, ~50 W *(Space Investments, 2026)*
- AIRSAT-02 (China, Jan 2026): **120 Gbps peak; 12.656 Tbits per 108-second pass** *(CGTN, Jan 2026)*
- Axiom Space ODC: 2.5 Gbps optical (2025); 10+ Gbps planned
- Voyager µLCT: 400+ Gbps (commercial claim, not flight-validated for ground link) *(Satsearch, May 2025)*
- Laser ISL does not require FCC/ITU frequency coordination *(Satsearch, May 2025)*

**Key achievement:** China's AIRSAT-02 demonstrated 1.58 TB per 108-second pass at 120 Gbps in January 2026 — the current public benchmark for optical downlink throughput.

## Daily Throughput Calculations

### Scenario A: Single ground station, optical downlink at 100 Gbps
- 3 passes/day × 10 min/pass × 100 Gbps = 18 TB/day per satellite

### Scenario B: Global ground station network, optical at 100 Gbps
- 12 passes/day (polar stations) × 10 min/pass × 100 Gbps = 72 TB/day per satellite

### Scenario C: RF Ka-band, single ground station
- 3 passes/day × 10 min/pass × 3 Gbps = 5.4 TB/day per satellite

### For reference: What a 1 MW data center generates
- A 1 MW cluster ≈ 300–400 H100s at ~3 kW each
- Each H100: 80 GB HBM3 memory; 3,958 TOPS INT8
- Training output (model weights): depends on model — a 70B param LLaMA-class model = ~140 GB; full training checkpoint = ~500 GB
- Inference output: varies; for EO image classification, ~1 KB per 10 MB image = 10,000:1 compression
- Earth observation raw data: ~5–50 GB/day per optical sensor (before processing)

**The compression asymmetry:** If the orbital data center is running inference (e.g., classifying satellite imagery), the output-to-input ratio can be 1,000:1 or better — downlink bandwidth is not the bottleneck. If it is training foundation models and must exfiltrate full checkpoints, 18–72 TB/day optical capacity becomes a real constraint for continuous operations.

## ISL vs. Direct Downlink Architecture

An alternative to direct satellite-to-ground downlinks is routing data through an ISL mesh to a satellite with a high-bandwidth ground connection (e.g., a Starlink relay satellite):

- Starlink: 100 Gbps per ISL link; 42 PB/day across 9,000+ satellite constellation *(Space Investments, 2026)*
- SpaceX "Plug and Plaser" terminal: routes customer satellite data through Starlink network

**ISL relay advantage:** The orbital data center satellite doesn't need its own large ground terminal — it hands data to a relay constellation. **Disadvantage:** Adds latency, adds dependency on SpaceX infrastructure, and relay capacity is shared.

## Comparison to Terrestrial Cloud

| System | Downlink capacity | Notes |
|---|---|---|
| AWS data center to internet | Tbps+ | Direct fiber, continuous |
| Starlink LEO constellation | 42 PB/day total | 9,000+ sats, distributed |
| Single LEO sat, optical downlink | 18–72 TB/day | Depends on ground station network |
| Single LEO sat, RF Ka-band | 5–15 TB/day | Weather-dependent |
| Single LEO sat, AIRSAT-02 class | ~6–20 TB/day | 3–4 passes at 120 Gbps, 10 min each |

For a **single satellite** serving a single customer, 18–72 TB/day optical capacity is comparable to a 2–8 Gbps sustained connection — fast enough for most workloads that produce compressed outputs, inadequate for continuous large-checkpoint exfiltration from a large training cluster.

## Key Takeaways for Space Data Centers

1. Downlink is not fatal — 18–72 TB/day per satellite with optical terminals is workload-dependent
2. Workloads that dramatically compress outputs (inference, EO classification, batch analytics) are downlink-feasible; continuous large-model training checkpoint exfiltration is not
3. Optical downlinks (100 Gbps, no spectrum coordination required) are the right technology — laser ISL avoids FCC/ITU bottleneck
4. A global ground station network matters: moving from 2–4 passes/day to 12/day multiplies throughput 3–4×
5. ISL relay (via Starlink) is a viable architecture that offloads ground station capital cost but creates a dependency on SpaceX infrastructure

## Open Questions

- What is the total network throughput of a 5 GW space data center constellation back to Earth? (Starcloud 5 GW = ~5,000 satellites × 18 TB/day = 90 PB/day — comparable to Starlink's 42 PB/day consumer traffic)
- Can immersion-cooled satellites accommodate the large aperture telescopes needed for 100 Gbps optical downlink pointing?

## Related Pages

- [[wiki/sources/china-120gbps-laser-downlink-2026.md]]
- [[wiki/sources/orbital-datacenter-technical-analysis-2026.md]]
- [[wiki/sources/satsearch-isl-terminals-2025.md]]
- [[wiki/synthesis/space-datacenter-latency.md]]
- [[wiki/synthesis/space-datacenter-workload-types.md]]
- [[wiki/concepts/space-regulatory-landscape.md]]
