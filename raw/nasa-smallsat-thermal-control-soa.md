# NASA Small Spacecraft Thermal Control - State of the Art

Source: https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/
Chapter 7.0 of "State-of-the-Art of Small Spacecraft Technology"
Published: May 7, 2026

## Key Thermal Control Equation

qsolar + qalbedo + qplanetshine + Qgen = Qstored + Qout,rad

Represents how solar heating, planetary reflections, planetary infrared, and spacecraft-generated heat must balance against stored heat and radiated heat dissipation.

## Primary SmallSat Thermal Challenges

- Low thermal mass creates reactive temperature responses to environmental changes
- Limited external surface area restricts space for solar cells, radiators, and instruments
- Constrained volume limits component spacing and thermal isolation options
- Power limitations restrict active cooling system capabilities
- Power density creates challenges dissipating concentrated heat from stacked electronics

## Passive Thermal Technologies

### Coatings & Surface Properties

Optical surface properties including solar absorptivity and infrared emissivity. Common solutions include matte black paint (high absorption/emission) and silver Fluorinated Ethylene Propylene tapes for radiator surfaces.

Products:
- Socomore Z306/Z307 polyurethane (black, lower cost)
- Huntington Ingalls Z93P silicate (white, requires environmental control during application)
- AZ Technology AZW/LA-II silicate (white, highest application difficulty)

Optical coating properties degrade throughout mission duration due to atomic oxygen and UV exposure, requiring beginning-of-life (BOL) versus end-of-life (EOL) modeling adjustments.

### Thermal Straps

Flexible conductive links connecting heat sources to sinks. Materials include copper, aluminum, and pyrolytic graphite sheets (PGS). Advanced designs using graphite show improved thermal conductivity compared to traditional metals.

Manufacturers: Space Dynamics Laboratory, Boyd Corporation, Thermotive.

### Heat Pipes

Passive devices using liquid vaporization/condensation cycles. Traditional cylindrical heat pipes and flat-plate configurations transfer heat via capillary action without power input.

### Multi-Layer Insulation (MLI)

Typically 10-20 reflective layers with embossed spacing. MLI performs poorly on CubeSats due to compression in deployers and edge effects that "short" thermal performance.

### Deployable Radiators

Dedicated surfaces for heat dissipation deployed when needed. NASA JPL and California universities developing Additively Manufactured Deployable Radiators with Oscillating Heat Pipes (AMDROHP) that fit within 3U CubeSats.

### Phase Change Materials (PCM)

Materials like paraffin wax (melting point 20-60°C, heat of fusion 140-280 kJ/kg) absorb thermal energy during phase transitions, smoothing temperature transients.

## Active Thermal Systems

### Electrical Heaters

Kapton resistance heaters (0.4-7.75 W/cm²). Temperature ranges -200°C to 300°C. TRL 7-9 for LEO applications. Most commonly integrated active technology on SmallSats.

### Cryocoolers

Refrigeration systems achieving ~100K and below:
- Lockheed Martin MICRO1-1: ~1U form factor, 0.350 kg, 15W power, TRL 7-9
- AIM Infrarot-Module SF070: 0.85 kg, 24W power, 0.6W cooling at 80K

### Thermoelectric Coolers (TECs)

Solid-state heat pumps using Peltier effect. Cooling capacities 1.8-322W. Operational limits below 130K due to efficiency degradation.

### Fluid Loops

Pumped systems circulating working fluid from heat exchangers to radiators. Advanced Thermal Architecture (ATA) from Utah State University combines mechanically pumped fluid loops with cryocoolers in sub-1U packages. Achieves >200% baseline thermal performance improvement with >30% mass savings.

Thermal Interface Materials: conductance 0.75-3.5 W/in²-°C. Products include Laird Tflex series (6 W/mK) and Henkel GAP PADs.

## Technology Readiness Levels

| Technology | TRL (LEO) |
|------------|-----------|
| Electrical heaters | 7-9 |
| Cryocoolers (mature) | 7-9 |
| Cryocoolers (advanced) | 4-6 |
| Fluid loops (legacy) | 7-9 |
| Fluid loops (miniaturized) | 4-7 |
| AMDROHP deployable radiators | ~3-5 (development) |

## Mission Examples

- BioSentinel (6U, Artemis I 2022): Sheldahl metallized tape and silver FEP tapes
- Lunar IceCube (6U, Artemis I 2022): 600mW cryocooler for infrared spectrometer
- TechEdSat-10 (6U, ISS deployment 2020): FlexCool conformable heat pipes for radio thermal management
- ASTERIA (CubeSat, 2017): Pyrovo pyrolytic graphite film thermal straps

## Design Methodology Notes

- Material selection based on thermal conductivity requirements
- Spacecraft orientation optimization (when science objectives permit)
- Thermal interface definition through mounting methods
- Circuit board copper layer optimization for heat spreading
- Temperature ranges span -200°C to 300°C depending on technology
- Heat capacities range from <1W to >300W
- Sub-100W total power available on most CubeSats constrains active system deployment
