---
title: "Space Data Center Power Budget Analysis"
type: "source_summary"
sources:
  - "test-pdf.txt"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# Space Data Center Power Budget Analysis

**Source**: Orbital Systems Research Institute, 2025
**Source type**: industry_report
**Processing status**: processed
**Ingest count**: 1
**Extracted from**: raw/test-pdf.pdf → raw/test-pdf.txt

## Summary

This report provides a power budget analysis for orbital data centers, covering solar generation, energy storage, and thermal rejection constraints. Two key limiting systems are sized against a 1 MW reference facility:

- **Solar generation**: 1.4 kW/m² input at LEO; 20% panel efficiency → 280 W/m² output; ~3,600 m² of panels required for 1 MW
- **Thermal rejection**: 450 W/m² at 300 K radiators; ~2,200 m² of radiators required for 1 MW
- **Eclipse bridging**: LEO eclipse periods up to 36 min / 90 min orbit; battery storage required

The report also identifies $100–200/kg launch cost as the threshold for economic viability, noting SpaceX Starship's $10–100/kg target.

## Key Claims

- Solar panels in LEO receive ~1.4 kW/m²; at 20% efficiency → 280 W/m² output.
- 1 MW data center needs ~3,600 m² solar panels and ~2,200 m² radiators.
- LEO eclipse periods require battery or fuel cell storage for continuous operation.
- Economic viability requires launch costs below $200/kg; Starship targets $10–100/kg.
- Thermal management is identified as the primary engineering constraint at scale.

## Related pages

- [[wiki/concepts/thermal-management.md]]
