---
title: "GEO Orbital Slot Capacity — Research Compilation"
type: "source_summary"
sources:
  - "geo-orbital-slots-capacity.md"
status: "current"
created: "2026-06-08"
last_updated: "2026-06-08"
---

# GEO Orbital Slot Capacity — Research Compilation

**Credibility**: compiled from The Conversation, Summit Ridge Group, Space Legal Issues, ITU Hub, UCS Satellite Database *(industry report / other)*

## Slot Count and Spacing

The geostationary ring at 35,786 km altitude is effectively a 1D resource — a single
ring with circumference ~264,924 km. Regulatory capacity is governed by ITU angular
spacing rules rather than physical collision density.

- Minimum spacing: **2°** for C-band and Ku-band satellites (reduced over time from higher values
  due to demand); DBS historically required ≥9°
- Simple geometric capacity: 360° / 2° = **180 unique angular positions**
- Commonly cited figure: **~1,800 total GEO slots**, which accounts for co-location
  (multiple satellites at the same nominal position using different frequency bands
  or polarizations — C, Ku, Ka, V-band)

## Current Occupancy

- **~580 active GEO satellites** (UCS Satellite Database, July 2023) *(other)*
- Many additional ITU registrations exist as "paper satellites" (coordinated but never launched)
- Prime positions over the Americas (70–100°W) and Europe (0–35°E) are fully contested
- Operators retain slots indefinitely by replacing aging satellites with new ones
  (ITU "use it or keep it" precedent)
- Kingdom of Tonga sold GEO slot rights for US$2M/year per slot (1988), illustrating
  the economic scarcity value

## GEO Debris Regime

Unlike LEO, GEO debris does **not** naturally deorbit:

- Atmospheric drag at 35,786 km is negligible; natural decay timescale is thousands to
  millions of years
- Standard practice: boost end-of-life satellites to **graveyard orbit** ~300 km above GEO
  (~36,100 km altitude)
- Kessler cascade risk in GEO is **low** — object count (~580 active) is far below
  any cascade threshold, and widely-spaced satellites have low collision velocities
  relative to LEO
- Long-term risk: failed "zombie satellites" that cannot perform graveyard boosts pose
  a permanent hazard at GEO altitude

## Implications for Space Data Centers

| Factor | GEO Impact |
|--------|-----------|
| Sunlight | Continuous (no eclipse) — no battery sizing penalty |
| Latency | ~500 ms RTT — incompatible with interactive compute |
| Slot availability | ~1,800 total; ~580 occupied; prime positions saturated |
| Slot duration | Indefinite if satellite replaced before end-of-life |
| Debris risk | Low collision risk; debris permanent unless actively disposed |
| Launch cost | ~$2,000/kg (Falcon Heavy) vs ~$1,500/kg to LEO |

## Open Questions

- What fraction of the ~1,800 ITU registrations are active vs. paper satellites?
- How does the ITU plan to reclaim unused registrations to free up slots?
