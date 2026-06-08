"""
Kessler Critical Density Calculator
====================================
Implements the Kessler (1978) collision-cascade model to find the critical
number of objects per orbital shell above which debris production exceeds
atmospheric decay — the "Kessler instability threshold".

Usage
-----
    python wiki/comparisons/kessler-limit-calculator.py

Output
------
    wiki/comparisons/kessler-critical-density.png
    Console table of N_crit vs altitude for Starlink-class objects

Model summary
-------------
For N objects uniformly distributed in a thin spherical shell of volume V:

    Collision rate:    R   = (N² / 2V) × σ × v_rel        [collisions/s]
    Debris generated:  Ṅ+ = R × δ_shell                   [fragments/s in this shell]
    Debris removed:    Ṅ- = N_debris / τ_debris            [fragments/s via drag]

At the critical threshold Ṅ+ = Ṅ-:

    N_crit = 2V / (δ_shell × σ × v_rel × τ_debris)

Key references
--------------
- Kessler & Cour-Palais (1978) "Collision frequency of artificial satellites"
  J. Geophys. Res. 83(A6):2637-2646.
- Johnson et al. (2001) NASA Standard Breakup Model (SBM) for fragment count.
- Chobotov (2002) "Orbital Mechanics" 3rd ed. for drag-lifetime formula.
- Bongers & Torres (2023) for the 72,000-satellite economic threshold.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
R_EARTH     = 6.371e6    # Earth radius (m)
MU          = 3.986e14   # gravitational parameter (m³/s²)
SEC_PER_YR  = 3.156e7    # seconds per year


# ---------------------------------------------------------------------------
# Atmospheric density model
# ---------------------------------------------------------------------------
# NRLMSISE-00 approximate, F10.7 = 150 (moderate solar activity).
# Values represent total mass density in kg/m³ at listed altitudes.
_ALT_KM  = np.array([200,    300,    400,    500,    600,    700,    800,    1000,   1500  ])
_RHO_KGM = np.array([2.0e-10,2.0e-11,2.5e-12,3.5e-13,6.0e-14,1.2e-14,3.0e-15,2.5e-16,1.5e-18])


def atmospheric_density(altitude_km: float) -> float:
    """Atmospheric density (kg/m³) via log-interpolation on NRLMSISE-00 nodes."""
    h = float(np.clip(altitude_km, 200, 1500))
    return float(10 ** np.interp(h, _ALT_KM, np.log10(_RHO_KGM)))


# ---------------------------------------------------------------------------
# Orbital mechanics
# ---------------------------------------------------------------------------

def orbital_radius(altitude_km: float) -> float:
    """Orbital radius from Earth centre (m)."""
    return R_EARTH + altitude_km * 1_000.0


def orbital_velocity(altitude_km: float) -> float:
    """Circular orbital speed (m/s)."""
    return float(np.sqrt(MU / orbital_radius(altitude_km)))


def relative_velocity(altitude_km: float) -> float:
    """
    Average relative speed between two objects in the same shell.
    Kessler (1978) derived v_rel ≈ 1.4 × v_circ for an isotropic
    inclination distribution; √2 applies only for head-on encounters.
    """
    return 1.4 * orbital_velocity(altitude_km)


def shell_volume(altitude_km: float, thickness_km: float = 10.0) -> float:
    """Volume of a thin spherical shell (m³)."""
    r = orbital_radius(altitude_km)
    return 4.0 * np.pi * r ** 2 * (thickness_km * 1_000.0)


def orbital_lifetime_years(altitude_km: float, beta_kg_m2: float) -> float:
    """
    Natural orbital decay lifetime (years) for given ballistic coefficient.

    Derivation (circular orbit, small drag):
        dh/dt = -(CdA/m) × ρ × v_orb × r     [Chobotov 2002, eq. 9.12]
    Integrating with ρ ≈ const over the decay path:
        τ ≈ β × h / (ρ × v_orb × r)
    where β = m / (Cd × A).

    Parameters
    ----------
    altitude_km  : orbit altitude (km)
    beta_kg_m2   : ballistic coefficient m/(Cd·A) in kg/m²
    """
    h   = altitude_km * 1_000.0
    rho = atmospheric_density(altitude_km)
    v   = orbital_velocity(altitude_km)
    r   = orbital_radius(altitude_km)
    tau_sec = beta_kg_m2 * h / (rho * v * r)
    return tau_sec / SEC_PER_YR


# ---------------------------------------------------------------------------
# NASA Standard Breakup Model (simplified)
# ---------------------------------------------------------------------------

def lethal_fragments(total_mass_kg: float) -> float:
    """
    Number of fragments > 10 cm (lethal to satellites) from a catastrophic
    hypervelocity collision.

    NASA SBM (Johnson et al. 2001) cumulative distribution:
        N(L > L_c) = 0.1 × M_LB^0.75 × L_c^{-1.71}
    At L_c = 0.1 m and M_LB = total mass:
        N(L > 0.1 m) ≈ 5.13 × M_total^0.75
    """
    return 5.13 * total_mass_kg ** 0.75


# ---------------------------------------------------------------------------
# Kessler critical count
# ---------------------------------------------------------------------------

def kessler_critical_count(
    altitude_km:         float,
    satellite_mass_kg:   float = 260.0,   # Starlink-class ~260 kg
    satellite_area_m2:   float = 10.0,    # typical cross-section (m²)
    debris_mass_kg:      float = 0.5,     # typical 10-cm fragment mass
    debris_area_m2:      float = 0.015,   # typical 10-cm fragment area
    Cd:                  float = 2.2,     # drag coefficient (tumbling fragment)
    shell_thickness_km:  float = 10.0,
    debris_ejection_dv:  float = 300.0,   # m/s — typical fragment ejection speed
) -> dict:
    """
    Solve for the critical object count that puts a 10-km orbital shell at
    the Kessler instability boundary.

    Balance equation
    ----------------
    Production = Decay
        (N² / 2V) × σ × v_rel × δ_shell  =  N / τ_debris
    Solve for N:
        N_crit = 2V / (δ_shell × σ × v_rel × τ_debris)

    δ_shell : fragments per collision that remain inside *this* shell.
        Total fragments spread over altitude range ≈ ±(Δv/v_orb) × r
        Fraction in a shell of thickness Δh ≈ Δh / (2 × altitude_spread).
    σ : collision cross-section for two identical objects with area A:
        σ = π × (2 r_eff)² = 4A,  r_eff = √(A/π)
    """
    beta_d  = debris_mass_kg / (Cd * debris_area_m2)   # debris ballistic coeff (kg/m²)

    # Shell geometry
    V     = shell_volume(altitude_km, shell_thickness_km)   # m³
    r     = orbital_radius(altitude_km)                     # m
    v_orb = orbital_velocity(altitude_km)                   # m/s
    v_rel = relative_velocity(altitude_km)                  # m/s

    # Debris lifetime in this shell
    tau_yr  = orbital_lifetime_years(altitude_km, beta_d)
    tau_sec = tau_yr * SEC_PER_YR

    # Collision cross-section (m²)
    sigma = 4.0 * satellite_area_m2

    # Fragments per collision retained in this 10-km shell
    total_frags    = lethal_fragments(2.0 * satellite_mass_kg)
    altitude_spread_m  = (debris_ejection_dv / v_orb) * r        # half-spread (m)
    shell_fraction = (shell_thickness_km * 1000.0) / (2.0 * altitude_spread_m)
    shell_fraction = min(shell_fraction, 1.0)
    delta_shell    = total_frags * shell_fraction

    # Critical count
    N_crit = 2.0 * V / (delta_shell * sigma * v_rel * tau_sec)

    return {
        "altitude_km"      : altitude_km,
        "N_crit"           : N_crit,
        "tau_debris_yr"    : tau_yr,
        "v_rel_km_s"       : v_rel / 1000.0,
        "sigma_m2"         : sigma,
        "delta_shell"      : delta_shell,
        "shell_volume_km3" : V / 1e9,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    altitudes = np.linspace(300, 1400, 250)

    # Three scenarios: cubesat, Starlink-class, orbital data center
    scenarios = [
        dict(label="CubeSat (5 kg, 0.03 m²)",          mass=5,     area=0.03,  color="mediumseagreen"),
        dict(label="Starlink-class (260 kg, 10 m²)",    mass=260,   area=10.0,  color="steelblue"),
        dict(label="Orbital data center (8,000 kg, 150 m²)", mass=8000, area=150.0, color="darkorange"),
    ]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # ---- LEFT: N_crit vs altitude ----
    ax = axes[0]
    for s in scenarios:
        Nc = [kessler_critical_count(h, satellite_mass_kg=s["mass"],
                                      satellite_area_m2=s["area"])["N_crit"]
              for h in altitudes]
        ax.semilogy(altitudes, Nc, label=s["label"], color=s["color"], linewidth=2)

    # Shade bands already past critical density (NAS / IADC)
    for lo, hi, txt in [(900, 1000, "900-1000 km\n(past critical, NAS)"),
                         (1450, 1550, "~1500 km\n(past critical, NAS)")]:
        ax.axvspan(lo, hi, alpha=0.15, color="red", zorder=0)
        ax.text((lo + hi) / 2, 8e4, txt, ha="center", fontsize=7,
                color="darkred", va="bottom")

    # Reference lines
    ax.axhline(11_800, color="gray",  linestyle="--", linewidth=1.2, zorder=1)
    ax.text(1380, 13_000, "~11,800 active\nsatellites (2025)",
            fontsize=7, ha="right", va="bottom", color="gray")

    ax.axhline(72_000, color="black", linestyle=":",  linewidth=1.2, zorder=1)
    ax.text(350, 79_000, "Bongers & Torres (2023)\n72,000 economic threshold",
            fontsize=7, ha="left", va="bottom", color="black")

    ax.set_xlabel("Altitude (km)")
    ax.set_ylabel("N_crit — max stable objects per 10-km shell")
    ax.set_title("Kessler Critical Count vs. Altitude")
    ax.legend(loc="lower right", fontsize=8)
    ax.set_xlim(300, 1400)
    ax.set_ylim(10, 5e7)
    ax.grid(True, alpha=0.3)

    # ---- RIGHT: orbital lifetime vs altitude ----
    ax2 = axes[1]
    for beta, label, color in [
        (3.0,   "Small debris 10 cm (β ≈ 3 kg/m²)",        "red"),
        (26.0,  "Starlink-class β ≈ 26 kg/m²",              "steelblue"),
        (200.0, "Orbital data center β ≈ 200 kg/m²",        "darkorange"),
    ]:
        lt = [orbital_lifetime_years(h, beta) for h in altitudes]
        ax2.semilogy(altitudes, lt, label=label, color=color, linewidth=2)

    ax2.axhline(25, color="gray", linestyle="--", linewidth=1.2)
    ax2.text(350, 27, "25-yr IADC deorbit guideline", fontsize=8, color="gray")

    ax2.set_xlabel("Altitude (km)")
    ax2.set_ylabel("Natural orbital lifetime (years)")
    ax2.set_title("Orbital Lifetime vs. Altitude  [F10.7 = 150, moderate solar]")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.set_xlim(300, 1400)
    ax2.set_ylim(0.01, 1e7)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = "wiki/comparisons/kessler-critical-density.png"
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    print(f"Chart saved: {outpath}")

    # ---- Console table ----
    print("\n=== N_crit per 10-km shell (Starlink-class: 260 kg, 10 m²) ===")
    print(f"{'Alt (km)':>9}  {'N_crit':>10}  {'τ_debris (yr)':>14}  "
          f"{'v_rel (km/s)':>13}  {'δ_shell':>8}")
    for h in [300, 400, 500, 550, 600, 700, 800, 1000, 1200]:
        r = kessler_critical_count(h)
        print(f"{h:>7} km   {r['N_crit']:>10,.0f}   {r['tau_debris_yr']:>12.1f}   "
              f"{r['v_rel_km_s']:>11.2f}   {r['delta_shell']:>8.1f}")

    print("\nNote: N_crit rises steeply above 600 km because atmospheric drag vanishes")
    print("and debris lifetime becomes centuries-to-millennia, making any collision")
    print("effectively permanent.  The 900-1000 km band is already past critical density.")
