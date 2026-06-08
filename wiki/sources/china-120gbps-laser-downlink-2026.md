---
title: "China Achieves 120 Gbps Satellite-to-Ground Laser Downlink (AIRSAT-02, Jan 2026)"
type: "source_summary"
sources:
  - "china-120gbps-laser-downlink-2026.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://news.cgtn.com/news/2026-01-30/China-hits-120-Gbps-in-satellite-to-ground-laser-communications-1KlLhbaqVpu/share_amp.html"
domain_relevance: "primary"
---

# China Achieves 120 Gbps Satellite-to-Ground Laser Downlink

**Source**: CGTN (China Global Television Network), January 30, 2026
**Source type**: news_article
*(news article)*

## Summary

China's AIRSAT-02 satellite achieved a peak 120 Gbps satellite-to-ground laser downlink using a 500 mm-aperture ground terminal on the Pamir Plateau. The record followed a progression: 10 Gbps (2023), 60 Gbps (2025), 120 Gbps (January 2026). Provides the most current public benchmark for laser downlink throughput per pass.

## Key Claims

- **Peak rate**: 120 Gbps; sustained "exceeding 100 Gbps" *(news article)*
- **Per-pass data volume**: 12.656 terabits in 108 seconds = **~1.58 TB per contact window**
- **Contact window**: 108 seconds maximum continuous link
- **Link acquisition**: second-level speed; >93% success rate
- **Ground station**: Pamir Plateau, Xinjiang; 500 mm aperture; operational since September 2024 as first routine commercial laser station in China
- **Satellite**: AIRSAT-02; orbit type and altitude not specified

## Derived Calculations

- At 120 Gbps over 108 s: 12.96 Tbits = 1.62 TB per pass (consistent with reported 12.656 Tbits)
- Typical LEO contact window over a single ground station: 8–12 min at 550 km altitude (longer window than reported 108 s — 108 s may be peak-rate portion of a longer contact)
- At 2–4 passes/day per satellite over one ground station at 100 Gbps for 8 min each: ~18 TB/day per ground station

## Significance

Establishes that optical downlinks can sustain ~100 Gbps and deliver ~1.5–18 TB/day per satellite per ground station depending on contact geometry. This bounds the data exfiltration rate for an orbital data center and shows the downlink bottleneck is real but not as severe as RF-only architectures.

## Related Pages

- [[wiki/concepts/space-datacenter-downlink-throughput.md]]
- [[wiki/synthesis/space-datacenter-latency.md]]
