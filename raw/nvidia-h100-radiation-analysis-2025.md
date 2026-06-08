# An Analysis of Radiation Protection in the NVIDIA H100 GPU

Source: New Space Economy (newspaceeconomy.ca), November 3, 2025
URL: https://newspaceeconomy.ca/2025/11/03/an-analysis-of-radiation-protection-in-the-nvidia-h100-gpu/
Source type: industry analysis / blog post

---

## Key Content

### Primary Radiation Protection Mechanism
The H100's main defense is Error Correction Code (ECC) memory, implemented across:
- HBM3 main memory
- L1/L2 caches
- Register files

ECC works on redundancy principles: Single-Bit Error Correction, Double-Bit Error Detection.

### Critical Vulnerabilities

**No Radiation Hardening:** The H100 is explicitly "not radiation-hardened or radiation-tolerant."

**Total Ionizing Dose (TID):** The H100's 4-nanometer process makes it "extremely vulnerable" to TID. Smaller transistors accumulate charge damage more readily, eventually causing transistor failure. No quantitative TID limit provided.

**Single Event Latch-up (SEL):** High-energy particles can trigger short circuits causing "a massive, uncontrollable surge of current" leading to chip overheating. The H100 "has no defense against this."

### Design Tradeoffs
- The H100 prioritizes performance and power efficiency, sacrificing physical robustness
- Rad-hard components trade performance, cost, and power for survival capability
- "A rad-hard processor is often 5 to 10 years behind commercial chips"

### Space Deployment Strategy for COTS GPUs
"Rad-tolerant" approach using COTS components with:
- System-level redundancy
- Spot shielding
- Latch-up protection circuits
- Watchdog systems

No quantitative LEO lifetime estimates provided.
