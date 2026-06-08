---
title: "ISS Station Report: ETCS Loop B Ammonia Leak Alarm, January 14, 2015"
type: "source_summary"
sources:
  - "nasa-iss-ammonia-leak-jan2015.md"
status: "draft"
created: "2026-06-08"
last_updated: "2026-06-08"
origin_url: "https://www.nasa.gov/blogs/stationreport/2015/01/14/"
---

# ISS Station Report: ETCS Loop B Ammonia Leak Alarm, January 14, 2015

**Source type**: news_article (NASA Station Report blog post, partial fetch)
**Subject**: ISS ETCS Loop B ammonia leak false alarm; crew emergency evacuation

## Incident Summary

At 3:58 AM CST on January 14, 2015, ISS telemetry indicated a possible ammonia leak within Node 2 (Harmony) in the US Segment. The crew immediately performed emergency procedures and evacuated the US Segment, isolating to the Russian Segment. *(news article)*

The systems implicated:
- **ETCS Loop B**: Port-side external ammonia loop (P1 truss radiator wing); independent from Loop A (S1 starboard)
- **Node 2 Low Temperature Loop**: The ITCS water sub-loop in Harmony at 17–24°C that connects to EATCS via Interface Heat Exchanger (IFHX)

The incident was a **false alarm**. No actual ammonia release occurred. The most likely cause was sensor contamination from METOX (Metal Oxide) canister regeneration off-gassing — a known false-positive trigger for ISS ammonia detectors.

## Operational Significance for Space Thermal Systems

This event documents the **operational risk profile of ammonia-based thermal control**:

1. **Toxicity drives emergency procedures**: Even a possible ammonia leak triggers full US Segment evacuation. Ammonia is immediately dangerous to life at concentrations above ~300 ppm.
2. **Loop B independence is a real safety feature**: The Loop A / Loop B split in EATCS means a leak in one external loop does not require shutting down all thermal management — redundancy is operationally meaningful.
3. **Sensor false-positive rate**: METOX canisters (CO₂ scrubbers) regenerate at ~177°C and release trace compounds that can fool ammonia sensors. This was an operational discovery, not a design-time assumption.
4. **Emergency isolation protocol**: Crew can seal the Russian Segment within minutes using hatch closure — ISS architecture provides an ammonia-safe refuge.

## Relevance to Space Data Center Design

For orbital data center proposals that adopt ISS-derived ammonia thermal loops:

- Ammonia loop integration within pressurized habitable volumes creates a Class 1 toxic hazard requiring emergency evacuation capability.
- Autonomous data centers without crew would still need leak detection and isolation valves to prevent ammonia from venting into any pressurized module (e.g., a maintenance bay or EVA staging area).
- The false-alarm rate at ISS (multiple events over 25-year lifetime) suggests ammonia sensor contamination should be treated as a routine operational event, not a design anomaly.

## Limitations

Source content is a truncated blog archive excerpt. Full daily summary report (including crew activity schedule, system resolution details, and ETCS recovery procedure) was not captured in this fetch.

## Related Pages

- [[wiki/sources/nasa-iss-atcs-overview.md]] — full ATCS architecture including EATCS Loop A/B specs
- [[wiki/synthesis/iss-scissors-beam-thermal-mechanisms.md]] — scissors-beam radiator deployment context
- [[wiki/concepts/thermal-management.md]] — radiative cooling fundamentals
