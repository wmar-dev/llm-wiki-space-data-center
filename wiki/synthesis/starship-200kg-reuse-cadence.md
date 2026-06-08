---
title: "At What Reuse Cadence Does Starship Reach $200/kg?"
type: "synthesis"
sources:
  - "spacex-launch-cost-math.md"
  - "orbital-startup-economics-register-2026.md"
status: "current"
created: "2026-06-07"
last_updated: "2026-06-07"
---

# At What Reuse Cadence Does Starship Reach $200/kg?

**Open question from**: [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]

**Short answer**: $200/kg requires only **2–3 reuses** at 2024-era build costs — a
low bar that Starship could cross early in its commercial reuse program. The harder
and more relevant threshold for space data centers is $10–100/kg, which requires
10–100 reuses and has no public commitment from SpaceX.

---

## The Math at Each Cost Era

Using the per-flight cost equation from [[wiki/synthesis/spacex-starship-cost-breakdown.md]]:

`$/kg = (Build Cost / Reuses + Ops + Propellant) / 200 t payload`

Solving for reuses needed to reach exactly $200/kg (40M total flight cost):

| Build Cost Era | Year | Reuses for $200/kg | Reuses for $100/kg | Reuses for $10/kg |
|---|---|---|---|---|
| $90M (current) | 2024 | **~2–3** | ~5 | ~100 |
| $50M (ramp) | 2025 | **~1–2** | ~3 | ~55 |
| $20M (high-volume) | 2027 | **already below** | ~1 | ~20 |

At $20M build cost (projected 2027 high-volume production), Starship clears $200/kg
with a single flight — making reuse count irrelevant for that threshold.

Inference: $200/kg is essentially **already within reach** under optimistic 2025–2027
build cost projections. The space data center viability threshold ($100–200/kg from
[[wiki/synthesis/space-datacenter-financial-viability.md]]) is the *easier* of the
two goals. SpaceX need not demonstrate 100-reuse vehicles to unlock basic space data
center economics.

---

## Why $200/kg Is the Wrong Threshold to Watch

The financial viability analysis uses $100–200/kg as the headline number, but the
underlying math for a 1 MW orbital facility is more demanding:

- A 1 MW node requires ~41–88 t of hardware at launch
  [[wiki/synthesis/launches-required-space-datacenter.md]]
- At $200/kg: launch cost alone = **$8–18M per MW**
- Terrestrial data center construction runs ~$5–10M per MW total (all-in)

At $200/kg, launch cost equals or exceeds the entire terrestrial build cost — leaving
no margin for the satellite hardware itself, solar arrays, radiators, or operations.

Inference: For space data centers to be *competitive* (not merely *possible*) with
terrestrial alternatives, launch costs need to reach **$50–100/kg or below**. That
requires 5–20 reuses at $50M build cost, or 3–10 reuses at $20M build cost.

---

## What SpaceX Has and Has Not Committed To

The reuse cadence data in the wiki is projection-only, sourced from a blog post
citing SpaceX public statements [[wiki/synthesis/spacex-starship-cost-breakdown.md]]
*(blog post)*. No source provides:

- A committed flight rate (launches per year per vehicle)
- A demonstrated turnaround time between Starship flights
- Verified cost data from actual commercial Starship missions

Falcon 9 precedent: boosters routinely fly 20+ times; 40-reuse certification is
demonstrated; 100-reuse is the stated goal. If Starship follows the same trajectory,
10–20 reuses within 2–3 years of commercial operations is plausible — but not
guaranteed.

---

## Summary

| Threshold | Reuses Needed (2025 build costs) | Significance |
|---|---|---|
| $200/kg | **1–2** | Space data centers *possible* |
| $100/kg | ~3 | Space data centers *financially competitive* |
| $10–50/kg | 20–55 | Space data centers *economically compelling* |

The $200/kg question resolves quickly once Starship achieves basic commercial reuse.
The harder question — whether Starship reaches $10–50/kg on a timeline relevant to
space data center investment decisions (2027–2032) — has no public answer.

## Open Questions

- What is SpaceX's actual demonstrated turnaround time between Starship flights,
  and does it support the 100-reuse-per-year cadence needed for $10/kg?
- At what launch cost does the orbital data center business case produce positive
  unit economics, accounting for hardware, operations, and depreciation — not just
  launch cost in isolation?

## Related Pages

- [[wiki/synthesis/spacex-starship-cost-breakdown.md]]
- [[wiki/synthesis/space-datacenter-financial-viability.md]]
- [[wiki/synthesis/launches-required-space-datacenter.md]]
- [[wiki/synthesis/space-datacenter-key-risks-analysis.md]]
