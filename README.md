# Space Data Center Prospects Analysis Wiki

An LLM-maintained wiki analyzing space data center prospects, built using the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#file-llm-wiki-md) pattern by Andrej Karpathy.

---

## Viability Assessment (as of June 2026)

**Short answer: not yet viable, but credibly on a 10–15 year trajectory — contingent on Starship economics and thermal engineering breakthroughs that have not been demonstrated at scale.**

The fundamental value proposition is abundant, free solar power in orbit (~1,361 W/m²
with no weather, no night, no land costs) combined with eliminating terrestrial power
grid dependency. At the right launch cost, this could make orbital compute cheaper per
watt than terrestrial data centers in power-constrained markets.

**The gating variable is launch cost.** At current rates (~$7,000/kg), a 1 MW orbital
facility costs hundreds of millions just to launch — before any hardware. The economic
viability threshold is $100–200/kg; Starship targets $10–100/kg but has achieved only a
55% orbital launch success rate as of late 2025, and full reuse has not been validated
at commercial cadence. The CEO of the most prominent orbital data center startup
(Orbital, a16z-backed) has publicly acknowledged "the economics don't quite work yet."

For context: xAI built its 150 MW Colossus AI supercomputer in 122 days. The US
terrestrial sector adds 2–3 GW of new data center capacity per year. Starcloud's entire
2035 orbital target (5 GW) equals roughly two years of US terrestrial growth. Orbital
compute is most plausibly a **specialized complement** — for Earth observation processing,
jurisdiction-independent compute, and global-coverage workloads — rather than a
general-purpose competitor to terrestrial cloud.

---

## Key Risks and Obstacles

### 1. Launch Cost — The Gating Variable (Critical)

- Viability threshold: **$100–200/kg**; current rate: **~$7,000/kg**
- Starship reusable target: **$10–100/kg**, requiring 70–100 reuse cycles per vehicle
- As of late 2025, Starship has a 55% orbital success rate; booster catch and full
  upper-stage reuse are still under validation
- Even optimistic projections place the threshold crossing at **2029–2035**

### 2. Thermal Management — No MW-Scale Demonstration (Critical)

- Space thermal control has been validated only to **tens of kilowatts** — far below
  data center workloads
- The only heat rejection mechanism in vacuum is radiation: **~450 W/m²** at 300 K
- A 1 MW facility needs **~2,200 m²** of radiators; a 100 MW facility needs ~220,000 m²
- These are massive deployable structures with no flight heritage at this scale
- Thermal waste heat disposal is described as "intractable" when spacecraft absorb
  maximum solar radiation (Wikipedia SBSP)

### 3. Power Intermittency and Battery Degradation (High)

- LEO satellites experience **~5,000 charge-discharge cycles per year** (eclipse every
  90 minutes), vs ~365 for terrestrial UPS systems
- NASA limits depth of discharge to **35%** to preserve battery life
- A 2026 arXiv paper (first of its kind) directly links compute workload scheduling to
  physical battery degradation — the degradation model is not yet incorporated into
  orbital data center designs
- Battery replacement at every 5–7 years adds significant lifecycle cost

### 4. Radiation Effects on Hardware (Medium-High)

- LEO radiation causes both soft errors (Single Event Upsets, recoverable) and
  permanent degradation (Total Ionizing Dose)
- A Starlink-class constellation of 60 processors/satellite would experience
  **30–300 SEU-induced errors per day** even with 1mm aluminum shielding
- Electronics require replacement every **5–6 years** due to radiation and degradation —
  fundamentally different capex model from terrestrial (replaced for performance)
- The South Atlantic Anomaly extends elevated radiation exposure to low-altitude LEO

### 5. Deployable Structure Reliability (High)

- A 1 MW facility needs **~3,600 m²** of solar arrays (roughly 24× the ISS iROSA panels)
- Caltech's SSPP mission (2023) deployed a 1.8m × 1.8m structure and encountered
  **two distinct failure modes** — wire snagging and a secondary jam — neither observed
  in ground testing; both required workarounds
- Space-grade solar cells cost **~100× more** than terrestrial equivalents
- Deployment failure modes do not extrapolate linearly from lab to orbit

### 6. Orbital Congestion (Emerging)

- Two LEO bands are already past critical debris density; the 72,000-satellite
  threshold for Kessler syndrome cascade has been identified in literature
- A 5 GW constellation (Starcloud's target: ~88,000 satellites) would be a major
  contributor to this risk
- US launch sites were already congested in January 2025, before any data center
  launches; regulatory throughput is a binding constraint for GW-scale buildout

---

## Key Companies (mid-2026)

| Company | Status | Scale | Backer |
| --- | --- | --- | --- |
| **Starcloud** | H100 in orbit (Nov 2025) | 60 kg demo; 5 GW target by 2035 | Y Combinator |
| **Orbital** | Pre-launch | 100 kW PoC (2027); 2030 full-scale | a16z |
| **Cowboy Space Corp** (ex-Aetherflux) | Post-pivot | LEO laser constellation | $50M raised |
| **Google Suncatcher** | Feasibility study | Demo 2027; needs <$200/kg by 2035 | Google |
| **SpaceX** | FCC filing (Jan 2026) | Millions of satellites w/ compute | Self-funded |
| **Blue Origin TeraWave** | Announced | ~5,400 satellite constellation | Blue Origin |
| **China Xingshidai** | Operating | Unknown scale | State-backed |
| **Lonestar** | Hardware deployed | Lunar data backup (Mar 2025) | VC-backed |

---

## Best-Fit Workloads

Not all workloads are equal candidates. The clearest case for orbital compute is
data that is *already in orbit*:

- **Earth observation / remote sensing** — process imagery onboard; eliminate downlink
- **AI/GPU batch training** — tolerates 90+ ms round-trip latency; power cost benefit
- **Jurisdiction-free / sovereign compute** — no territorial data law applies in orbit
- **Sun-synchronous persistent workloads** — constant solar exposure eliminates eclipse cycling

**Not viable:** low-latency transactions, interactive APIs, gaming — the two-leg
satellite overhead (~90 ms) is disqualifying. LEO round-trip is ~40–70 ms (Starlink
proxy); GEO is 1,000–1,400 ms.

---

## Wiki Contents

This wiki is organized into four page types:

- **`wiki/sources/`** — summaries of ingested primary sources
- **`wiki/concepts/`** — synthesized concept pages (thermal management, orbital capacity, etc.)
- **`wiki/entities/`** — company and organization profiles
- **`wiki/synthesis/`** — query answers filed as standalone pages

Key synthesis pages:

- [Financial Viability & Key Risks](wiki/synthesis/space-datacenter-financial-viability.md)
- [Key Risks Analysis](wiki/synthesis/space-datacenter-key-risks-analysis.md)
- [Companies Landscape](wiki/synthesis/space-datacenter-companies-landscape.md)
- [Orbital Regime](wiki/synthesis/space-datacenter-orbital-regime.md)
- [Latency vs. Terrestrial Cloud](wiki/synthesis/space-datacenter-latency.md)
- [Workload Types](wiki/synthesis/space-datacenter-workload-types.md)
- [Launch Count Analysis](wiki/synthesis/launches-required-space-datacenter.md)
- [Launch Site Capacity](wiki/synthesis/launch-site-capacity-space-datacenter.md)
- [Solar Cell Efficiency](wiki/synthesis/solar-cell-efficiency-space.md)
- [Theoretical Efficiency Limits](wiki/synthesis/theoretical-solar-cell-efficiency-limit-space.md)
- [Terrestrial Baseline (xAI, global capacity)](wiki/synthesis/terrestrial-datacenter-capacity-baseline.md)
