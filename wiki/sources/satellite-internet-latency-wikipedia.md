---
title: "Satellite Internet Access — Latency Data (Wikipedia)"
type: "source_summary"
sources:
  - "satellite-internet-latency-wikipedia.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
origin_url: "https://en.wikipedia.org/wiki/Satellite_Internet_access"
domain_relevance: "primary"
---

# Satellite Internet Access — Latency Data (Wikipedia)

**Source**: Wikipedia
**Source type**: other
**Processing status**: processed
**Domain relevance**: primary (real-world measured latency for LEO/MEO/GEO satellite links)

## Key Claims

- **Starlink (550 km LEO)**: average RTT **45 ms** measured (2021 study); 1.8–22.8 ms higher than equivalent terrestrial networks (2022 study). — *(other)*
- **Iridium / Globalstar (LEO)**: round-trip delays **<40 ms**. — *(other)*
- **O3b (8,062 km MEO)**: RTT **~125 ms**. — *(other)*
- **GEO theoretical minimum**: one-way propagation ~250 ms; typical total RTT 1,000–1,400 ms (user → ISP → user). — *(other)*
- **Terrestrial cable / VDSL**: 15–40 ms RTT (the baseline LEO outperforms). — *(other)*
- GEO latency is higher than dial-up (150–200 ms total RTT). — *(other)*

## Significance

Starlink's real-world 45 ms RTT for broadband communication at 550 km is the best
available proxy for what a space data center at the same altitude would face for
network-layer latency. This is 1.8–22.8 ms above terrestrial baselines, meaning
LEO compute imposes a measurable but not disqualifying latency premium for most
workloads. GEO latency (1,000–1,400 ms RTT) would exclude all latency-sensitive
workloads.

## Related Pages

- [[wiki/synthesis/space-datacenter-orbital-regime.md]]
- [[wiki/synthesis/space-datacenter-latency.md]]
