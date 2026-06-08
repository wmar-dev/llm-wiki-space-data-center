# GEO Orbital Slot Capacity — Compiled Research

**Sources consulted (June 2026)**:
- The Conversation: "There's a parking crisis in space – and you should be worried about it" (theconversation.com)
- Summit Ridge Group: "Orbital Slots" glossary (summitridgegroup.com)
- Space Legal Issues: "Orbital slots and space congestion" (spacelegalissues.com)
- ITU Hub (2023): "WRS-22: Regulation of satellites in Earth's orbit"
- UCS Satellite Database (July 2023): active GEO satellite count

---

## Key Facts

### Orbital slot count
- ~1,800 total GEO orbital slots are commonly cited
- Based on 2° minimum angular spacing: 360° / 2° = 180 unique angular positions
- The ~1,800 figure appears to account for multiple frequency band / polarization reuse
  at the same nominal angular position (co-location), not a simple geometric division
- The FCC and ITU have progressively reduced required spacing down to 2° for C-band
  and Ku-band satellites due to high demand

### Current occupancy
- UCS Satellite Database (July 2023): 580 active geostationary satellites out of ~6,718 total
- Prime positions over Americas (70–100°W) and Europe (0–35°E) are fully contested
- Operators can retain slots indefinitely by replacing aging satellites with new ones
  (ITU "use it or keep it" precedent)
- Many more ITU registrations exist as "paper satellites" that never launched

### Spacing and co-location
- Minimum 2° separation for C-band and Ku-band (FCC/ITU reduced over time due to demand)
- Direct broadcast satellites (DBS) historically required ≥9° spacing
- Co-location: multiple satellites can share the same nominal slot using different
  frequency bands (C, Ku, Ka, V) and/or orbital polarizations
- Example: Tonga auctioned five GEO slots for US$2M/year each (1988)

### GEO debris regime (vs. LEO)
- Atmospheric drag is negligible at 35,786 km → debris does NOT naturally deorbit
- Natural orbital decay timescale at GEO: many thousands to millions of years
- Standard practice: boost end-of-life satellites to "graveyard orbit" ~300 km above GEO
  (~36,100 km)
- GEO Kessler cascade risk is LOW relative to LEO due to:
  - Satellites are widely separated (0.05°–2° minimum → hundreds to thousands of km)
  - Collision velocities are much lower relative to LEO
  - Object count is ~580 active, orders of magnitude below any cascade threshold
- Long-term concern: graveyard orbit may eventually become congested;
  "zombie satellites" (failed before disposal) pose future collision risk

### Implications for data centers
- GEO offers continuous sunlight (no eclipse) → no battery sizing penalty
- GEO latency: ~500 ms RTT → incompatible with interactive/real-time compute
- Slot scarcity: ~1,800 total vs ~580 occupied → ~1,200 formally available,
  but prime positions are saturated
- Slot allocation: ITU first-come, first-served; operators hold indefinitely by replacing satellites
- A large data center structure in GEO would occupy one registered slot per satellite
  (or co-locate if using different frequency bands than existing occupants)
