---
title: "Space Regulatory and Spectrum Access Landscape"
type: "concept"
sources:
  - "faa-part-450-licensing-2026.md"
  - "geo-orbital-slots-capacity.md"
  - "bongers-2026-space-economics-survey.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# Space Regulatory and Spectrum Access Landscape

## The Multi-Agency Stack

An orbital data center operator in the US must navigate four distinct regulatory bodies before launch. Each operates on its own timeline and scope.

| Agency | Jurisdiction | What it governs | Timeline |
|---|---|---|---|
| **FAA AST** | US launch vehicles | Launch vehicle licensing (Part 450) | 180-day statutory target |
| **FCC** | US spectrum users | Satellite spectrum allocation, earth station licenses | 6–18 months typical |
| **ITU** (via NTIA/FCC) | International spectrum | Frequency coordination, orbital slot filing | Up to 7 years advance filing required |
| **State Dept (ITAR/EAR)** | US defense/dual-use tech | Export licenses for rad-hard parts, encryption | Months to years |

## FAA Part 450 — Launch Licensing

The FAA's Part 450 rule (effective 2021, full compliance March 2026) consolidated all commercial space launch and reentry licensing under a single framework. *(FAA, March 2026)*

**Current state:**
- 14 licenses issued under Part 450 since 2021
- FAA reached 1,000 cumulative licensed space operations by August 2025
- 180-day statutory processing target; historically overrun in complex cases
- Three Florida/California sites handle the majority of US orbital launches
- US launch cadence already congested as of January 2025

**Implication:** Part 450 is a meaningful gating event, not a rubber stamp. A company planning first launch in 2027 should have filed no later than early 2027 — and the 180-day target may slip for novel vehicle configurations.

## FCC Satellite Spectrum — Data Downlink

For a space data center to transmit results to ground users, it needs FCC-licensed frequencies. Ka-band (26.5–40 GHz) and V-band (40–75 GHz) are the primary bands for high-throughput LEO data downlinks.

**Key constraints:**
- FCC requires coordination with existing license holders in the same frequency bands
- Optical/laser downlinks are largely unregulated for spectrum but require ground station pointing and clear-sky weather
- Mega-constellations have crowded Ka-band filings; new entrants face interference coordination delays

Open question: What sustained downlink throughput is achievable per satellite per day for data-center-class output volumes? *(See also: research gap in [[wiki/synthesis/concepts-research-gaps.md]])*

## ITU Coordination — GEO Slots and LEO Filings

The International Telecommunication Union coordinates spectrum and orbital slots globally. *(wiki/sources/geo-orbital-slots-capacity.md)*

**GEO:** ~1,800 ITU-coordinated slots at 2° spacing; only ~180 unique positions (some co-located multi-band filings). Filing requires up to 7 years advance notice for priority protection. ~580 GEO satellites are currently active.

**LEO:** No exclusive orbital slots; ITU manages frequency coordination. Large constellations must file "mega-constellation" coordination with all affected operators — a process that can take years for novel systems.

**National orbital object registry:** All satellites must be registered with the UN Office for Outer Space Affairs (OOSA) through their national space agency. The US State Dept handles this via the FCC/NTIA channel.

## ITAR and EAR — Export Controls

The US International Traffic in Arms Regulations (ITAR) and Export Administration Regulations (EAR) affect space data center hardware procurement and international commercial agreements:

- **Radiation-hardened processors and ASICs** are frequently ITAR-controlled as space-qualified defense articles
- **Encryption hardware** in onboard compute may require Commerce Department ECC licenses for non-US customers
- **International launch providers** (Arianespace, JAXA commercial) face ITAR license requirements for US-origin payloads

**Practical implication:** A startup planning to serve international customers from orbit with US-origin compute hardware faces two licensing stacks — commercial (FCC/FAA) and export control (ITAR/EAR). The EAR licensing timeline is unpredictable and can block international revenue.

## Orbital Governance and the Open-Access Problem

Beyond licensing, orbital data center operators face the systemic governance problem identified in [[wiki/sources/bongers-2026-space-economics-survey.md]]:

- LEO is an open-access commons; operators do not pay for orbital slots or debris externalities
- Economic modeling (Rao & Rondina) projects the orbit could become unusable between 2040–2184 under current governance
- The gap between open-access NPV (~$600B) and optimal-management NPV (~$3,000B) is ~$2.4T in foregone value from debris externalities

No binding international debris-mitigation treaty exists. The 25-year deorbit guideline (recently tightened to 5 years by FCC for US operators) is the primary regulatory mechanism.

## Key Takeaways for Space Data Centers

1. Launch licensing (Part 450) and spectrum licensing (FCC) run in parallel but are independent — both must complete before operations begin
2. ITU coordination for frequency protection requires 7-year advance filing for GEO; LEO frequency rights are less protected but still require FCC coordination
3. ITAR/EAR export controls may limit the international customer base for US-origin compute hardware in orbit
4. The FCC 5-year deorbit rule imposes a hard operational lifetime ceiling on any LEO satellite, compounding the hardware refresh penalty
5. Regulatory throughput, not physical site capacity, is the binding constraint on the US launch schedule

## Open Questions

- What is the FCC's current processing time for novel satellite broadband applications in Ka/V-band?
- Has any US regulator addressed jurisdiction for data processed exclusively in orbit (tax, data residency, GDPR)?

## Related Pages

- [[wiki/sources/faa-part-450-licensing-2026.md]]
- [[wiki/sources/geo-orbital-slots-capacity.md]]
- [[wiki/sources/bongers-2026-space-economics-survey.md]]
- [[wiki/synthesis/launch-site-capacity-space-datacenter.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
- [[wiki/concepts/orbital-capacity-limits.md]]
