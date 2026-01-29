# Z-Height Analysis: When Tall Builds Become Problematic

## 1. Purpose

This analysis helps users understand the engineering tradeoffs when using donor printers with Z-heights exceeding the recommended Tier 1 limit (280mm). If you're scavenging a donor with 300mm, 400mm, or larger Z-travel, this document quantifies what you're giving up.

**Bottom line:** Amalgam can work with tall Z, but print quality and reliability degrade. Use this analysis to make an informed decision.

---

## 2. The Three Problems with Tall Z

### 2.1 Leadscrew Buckling

T8 leadscrews (8mm diameter) are essentially slender columns under compressive load. As length increases, they become susceptible to **Euler buckling** — sudden lateral deflection under load.

### 2.2 Leadscrew Whip

At high rotation speeds, long leadscrews develop **whip** — a lateral oscillation caused by the screw's own mass and rotational dynamics. This manifests as vibration and noise, particularly during fast Z-hops.

### 2.3 Frame Resonance

Taller frames have lower natural frequencies. This means:
- Resonance occurs at lower print speeds
- Input shaping must work harder to compensate
- More energy transfers to the print

---

## 3. Leadscrew Buckling Analysis

### 3.1 Euler Buckling Formula

For a column with one end fixed and one end guided (typical leadscrew mounting):

```
P_critical = (π² × E × I) / (K × L)²
```

Where:
- P_critical = critical buckling load (N)
- E = Young's modulus (steel: 200 GPa)
- I = second moment of area (m⁴)
- K = effective length factor (0.7 for fixed-guided)
- L = unsupported length (m)

### 3.2 T8 Leadscrew Properties

| Property | Value |
|----------|-------|
| Diameter (d) | 8mm = 0.008m |
| I = πd⁴/64 | 2.01 × 10⁻¹¹ m⁴ |
| E (steel) | 200 GPa |
| K (fixed-guided) | 0.7 |

### 3.3 Critical Buckling Load vs Length

| Z-Height | Effective Length | P_critical | Safety Factor* |
|----------|-----------------|------------|----------------|
| 200mm | 140mm | 20,400 N | >100× |
| 280mm | 196mm | 10,400 N | >50× |
| 350mm | 245mm | 6,600 N | ~33× |
| 400mm | 280mm | 5,100 N | ~25× |
| 500mm | 350mm | 3,200 N | ~16× |

*Safety factor relative to ~200N bed load (typical 220×220 glass + carriage)

### 3.4 Interpretation

**Buckling is NOT the limiting factor** for any reasonable Z-height. Even at 500mm, the safety factor is 16×. The leadscrew won't buckle under normal operation.

The real problems are whip and frame resonance.

---

## 4. Leadscrew Whip Analysis

### 4.1 Critical Speed Formula

The first critical speed (where whip begins) for a simply-supported shaft:

```
N_critical = (π/2) × √(E × I / (ρ × A)) / L²
```

Where:
- N_critical = critical rotational speed (rad/s)
- ρ = density (steel: 7850 kg/m³)
- A = cross-sectional area (m²)
- L = unsupported length (m)

### 4.2 Critical Speed vs Z-Height

Converting to RPM for practical interpretation:

| Z-Height | Critical Speed (RPM) | Max Safe Z-Speed* |
|----------|---------------------|-------------------|
| 200mm | ~8,500 | Unlimited practical |
| 280mm | ~4,300 | ~25 mm/s |
| 350mm | ~2,750 | ~16 mm/s |
| 400mm | ~2,100 | ~12 mm/s |
| 500mm | ~1,350 | ~8 mm/s |

*Assuming T8×2 leadscrew (2mm pitch), staying at 70% of critical speed

### 4.3 Interpretation

At **280mm Z** (Tier 1 limit):
- Z-speeds up to 25mm/s are safe
- Fast Z-hops (layer changes) work normally
- No audible whip during operation

At **400mm Z** (Tier 2):
- Z-speed should be limited to ~12mm/s
- Fast Z-hops may cause vibration
- Audible whip possible during rapid moves

At **500mm Z** (beyond Tier 2):
- Z-speed limited to ~8mm/s
- Z-hops become slow
- Print time increases for tall objects with many layers

---

## 5. Frame Resonance Analysis

### 5.1 Natural Frequency Scaling

For a cantilevered or box frame, natural frequency scales approximately as:

```
f_n ∝ √(stiffness / mass) ∝ 1 / height
```

Doubling height roughly halves the natural frequency.

### 5.2 Estimated Natural Frequencies

| Z-Height | Frame Type | Est. Natural Freq | Problematic Speed* |
|----------|-----------|-------------------|-------------------|
| 200mm | M10 + MDF | ~45-55 Hz | 90-110 mm/s |
| 280mm | M10 + MDF | ~35-40 Hz | 70-80 mm/s |
| 350mm | M10 + MDF | ~28-32 Hz | 55-65 mm/s |
| 400mm | M10 + MDF | ~24-28 Hz | 48-55 mm/s |
| 500mm | M10 + MDF | ~18-22 Hz | 35-45 mm/s |

*Speed where resonance affects print quality (before Input Shaping)

### 5.3 Input Shaping Compensation

Klipper's Input Shaping can compensate for frame resonance, but:

| Resonance Freq | Shaping Effectiveness | Notes |
|----------------|----------------------|-------|
| >40 Hz | Excellent | Minimal speed penalty |
| 30-40 Hz | Good | ~10-15% speed reduction |
| 20-30 Hz | Moderate | ~20-30% speed reduction |
| <20 Hz | Poor | Significant quality/speed tradeoff |

### 5.4 Interpretation

At **280mm Z**:
- Frame resonance ~35-40 Hz
- Input shaping handles it well
- Target 70-80 mm/s achievable

At **400mm Z**:
- Frame resonance ~24-28 Hz
- Input shaping works but with penalty
- Target speed drops to ~55-65 mm/s

At **500mm Z**:
- Frame resonance <22 Hz
- Input shaping struggles
- Quality depends heavily on tuning

---

## 6. Practical Recommendations

### 6.1 Decision Matrix

| Your Z-Height | Recommendation |
|---------------|----------------|
| ≤280mm | **Go ahead** — no modifications needed |
| 280-350mm | **Proceed with caution** — reduce Z-speed to 15mm/s, expect 10-15% slower prints |
| 350-400mm | **Consider alternatives** — add frame bracing, reduce print speed to 60mm/s |
| >400mm | **Strongly reconsider** — significant compromises required |

### 6.2 Mitigation Strategies for Tall Z

If you must use a tall donor:

1. **Add leadscrew support bearing** at mid-height (reduces effective length for whip)
2. **Add frame cross-bracing** (increases stiffness, raises resonance frequency)
3. **Reduce Z-speed** in Klipper config (`max_z_velocity`)
4. **Reduce print acceleration** (lower inertial loads on frame)
5. **Use MDF damping** (already in spec, helps absorb resonance)

### 6.3 Klipper Configuration for Tall Z

For Z-heights 300-400mm, consider these config changes:

```ini
[printer]
max_z_velocity: 12          # Down from 25
max_z_accel: 100            # Down from 200

[stepper_z]
homing_speed: 8             # Slower homing

# Input shaping may need more aggressive settings
[input_shaper]
shaper_freq_x: 35           # Measure with ADXL345
shaper_freq_y: 35
shaper_type: mzv            # or ei for lower frequencies
```

---

## 7. Why the 280mm Tier 1 Limit?

The 280mm limit in ADR-026 was chosen because:

1. **Leadscrew whip** stays manageable (>20mm/s Z-speed safe)
2. **Frame resonance** stays above 35Hz (Input Shaping effective)
3. **Common donors** (Anet A8, Ender 3) are 220-250mm Z — natural fit
4. **Margin for error** — some headroom below problem thresholds

Going above 280mm doesn't break Amalgam, but it requires understanding and accepting the tradeoffs.

---

## 8. Summary

| Factor | Effect of Increasing Z | Mitigation |
|--------|----------------------|------------|
| Leadscrew buckling | Minimal concern | Not needed |
| Leadscrew whip | Limits Z-speed | Mid-support bearing |
| Frame resonance | Limits print speed | Bracing, Input Shaping tuning |
| Print time | Increases | Accept or reduce Z-height |

**The honest answer:** If your donor has 400mm+ Z, you can use it, but expect to print 15-25% slower than the reference spec to maintain quality. If that's acceptable, proceed. If not, sell the tall donor and buy a shorter one.

---

*"Tall printers aren't wrong — they're just honest about their tradeoffs."*
