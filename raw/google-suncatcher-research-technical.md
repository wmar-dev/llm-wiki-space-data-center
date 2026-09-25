# Exploring a space-based, scalable AI infrastructure system design

Source: https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/
Publisher: Google Research
Fetched: 2026-09-24

## Satellite Constellation Architecture

Illustrative design: an 81-satellite constellation operating in a sun-synchronous
low-Earth orbit at approximately 650 km altitude, with a cluster radius of 1 km.
Satellites maintain distances of "hundreds of meters apart," with next-nearest-neighbor
spacing oscillating between 100-200 meters.

**Orbital selection**: Dawn-dusk sun-synchronous orbit, chosen to maximize solar
exposure and minimize battery requirements, enabling near-continuous sunlight.

## TPU Specifications & Radiation Testing

Hardware: Google's Trillium v6e Cloud TPU, tested for space applications.

Radiation results: 67 MeV proton beam testing showed promising durability. High
Bandwidth Memory (HBM) components showed irregularities only after 2 krad(Si) —
nearly triple the anticipated five-year mission dose of 750 rad(Si) with shielding.
No hard failures were attributable to Total Ionizing Dose (TID) up to the maximum
tested dose of 15 krad(Si).

## Inter-Satellite Optical Links

The system requires data-center-scale connectivity supporting "tens of terabits per
second." Early validation achieved 800 Gbps each-way transmission (1.6 Tbps total)
using dense wavelength-division multiplexing and spatial multiplexing. Close formation
flying (kilometers or less) overcomes free-space optical signal attenuation challenges.

## Thermal Management

Identified as a significant remaining engineering challenge; the source does not
provide a detailed thermal architecture.

## Launch Costs / Economics

Analysis projects launch prices potentially reaching less than $200/kg by the
mid-2030s, which the paper frames as the threshold for space-based infrastructure to
become cost-competitive with terrestrial data centers on a per-kilowatt/year basis.

## Next Milestones

Partnership with Planet to launch two prototype satellites by early 2027, to validate
orbital formation-flying models, hardware performance under real space conditions, and
distributed ML optical inter-satellite link functionality.
