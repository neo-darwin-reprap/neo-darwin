# ADR-014: Z-Probe Selection (SuperPINDA vs BLTouch)

## Status
Accepted

## Context
The Neo-Darwin requires a Z-probe for homing and bed-leveling. The choice depends heavily on the bed surface material:

**Two Probe Technologies**:
1. **BLTouch**: Physical Hall Effect probe with moving pin that touches bed
2. **SuperPINDA**: Inductive proximity sensor that detects metal without contact

**Bed Surface Constraints**:
- **Inductive Probes**: Only work on conductive metal (magnetic spring steel sheets like MK52)
- **Physical Probes**: Work on any surface (glass, spring steel, wood, carbon fiber, plain aluminum)

**Engineering Philosophy**:
- **"Tractor" Goal**: Set-and-forget reliability with minimal maintenance
- **"Scavenger" Goal**: Universal compatibility with repurposed beds

This creates a decision matrix based on both bed surface and reliability requirements.

## Decision
We adopt a **bed-surface-dependent probe strategy** with **SuperPINDA as Reference Spec** and **BLTouch as Scavenger Fallback**.

### Probe Options

**Option A: SuperPINDA (Reference Spec)**
- **Technology**: Inductive proximity sensor (solid-state)
- **Bed Requirement**: Magnetic spring steel sheet (MK52 or compatible)
- **Mounting**: Fixed position on X-carriage or gantry
- **Wiring**: 3 wires (VCC, Ground, Signal)
- **Reliability**: Maximum - no moving parts, resin-encased, nearly indestructible
- **Cost**: ~$30-40 AUD
- **Best For**: Tier 3 Reference Spec builds with MK52 bed

**Option B: BLTouch V3.1 (Scavenger Fallback)**
- **Technology**: Physical Hall Effect probe with deployable pin
- **Bed Requirement**: Any surface (glass, carbon fiber, aluminum, spring steel)
- **Mounting**: Fixed position on X-carriage or gantry
- **Wiring**: 5 wires (VCC, Ground, Signal, Control Servo)
- **Reliability**: Moderate - moving pin can snap or bend if it hits print/clip
- **Cost**: ~$50-60 AUD (authentic), ~$15-25 AUD (3DTouch clone)
- **Best For**: Tier 1-2 builds with scavenged beds (glass, etc.)

### Technical Comparison

| Feature | SuperPINDA (Inductive) | BLTouch (Physical) |
|---------|------------------------|-------------------|
| **Bed Surface** | Metal only (conductive) | Universal (any material) |
| **Accuracy** | Extremely high, repeatable | Extremely high, but can drift if pin bent |
| **Robustness** | **Maximum** (solid-state, no moving parts) | Moderate (pin can snap/bend) |
| **Complexity** | Simple (3 wires, always-on) | Moderate (5 wires, deploy/retract logic) |
| **Wear Items** | None | Pin, springs, servo |
| **Thermal Drift** | Minimal (modern SuperPINDA) | None (mechanical contact) |
| **Calibration** | Z-offset once | Z-offset once, pin deployment verification |

### Why SuperPINDA for Reference Spec?

**1. Solid-State Reliability**
- Zero moving parts to fail
- Immune to "pin-snag" failures during high-speed travel
- Resin-encased design is nearly indestructible
- No deployment mechanism to jam or misfire

**2. Thermal Stability**
- Older inductive probes drifted with bed temperature
- PINDA V2 added thermistor to compensate (0.02mm adjustments)
- SuperPINDA uses higher-quality components that don't drift
- Trigger height identical at 20°C or 60°C chamber temperature

**3. "Set-and-Forget" Philosophy**
- Once calibrated, requires no ongoing maintenance
- No pin to straighten or replace
- No servo mechanism to lubricate or adjust
- Perfect for 1000+ day maintenance intervals

**4. Simplicity**
- 3-wire connection (vs 5 wires for BLTouch)
- No deployment/retract logic in Klipper
- Always-on proximity sensing
- Lower failure surface area

### Why BLTouch for Scavenger Builds?

**1. Universal Compatibility**
- Works on any bed surface (glass, carbon fiber, plain aluminum)
- Only option for salvaged Ender 3, i3 Mega, Anet A8 beds
- Allows flexibility in bed choice during Tier 1 builds
- Doesn't force MK52 bed purchase

**2. Well-Understood Technology**
- Years of community documentation and troubleshooting
- Wide availability of clones and spare parts
- Proven track record in millions of printers

**3. Bed-Surface Flexibility**
- User can experiment with different bed surfaces
- No commitment to magnetic spring steel upfront
- Universal "key" for uncertain scavenger inventory

### Build Wizard Logic

```
Configuration Wizard → Z-Probe Selection
├─ Question: "What is your bed surface material?"
│  ├─ Glass / Carbon Fiber / Plain Aluminum
│  │  └─ Force: BLTouch (inductive cannot see)
│  ├─ Magnetic Spring Steel (MK52 or compatible)
│  │  └─ Recommend: SuperPINDA ★ Reference Spec
│  │     └─ Option: BLTouch (if preferred)
│  └─ Unknown / Not sure
│     └─ Default: BLTouch (universal fallback)
```

### Bed-Probe Compatibility Matrix

| Bed Surface | SuperPINDA | BLTouch | Recommended |
|-------------|-------------|---------|--------------|
| **Magnetic Spring Steel (MK52)** | ✅ Works | ✅ Works | SuperPINDA ★ |
| **Plain Aluminum** | ✅ Works | ✅ Works | BLTouch (easier) |
| **Glass** | ❌ Won't detect | ✅ Works | BLTouch only |
| **Carbon Fiber** | ❌ Won't detect | ✅ Works | BLTouch only |
| **PEI on Glass** | ❌ Won't detect | ✅ Works | BLTouch only |
| **BuildTak on Aluminum** | ❌ Won't detect | ✅ Works | BLTouch only |

## Consequences

### Benefits
- **Tiered Flexibility**: Reference path (SuperPINDA) and Scavenger path (BLTouch) both supported
- **Bed-Surface Logic**: Clear decision matrix based on bed material
- **Reliability Optimization**: Reference spec maximizes solid-state reliability
- **Universal Fallback**: BLTouch works with any scavenged bed
- **Cost Awareness**: Clones available for low-budget builds

### Trade-offs
- **SuperPINDA**: Locked to metal beds, no flexibility in surface choice
- **BLTouch**: Higher failure rate (moving parts), pin maintenance required
- **Cross-Compatibility**: Cannot easily switch probes without changing bed
- **Clone Quality**: BLTouch clones vary in reliability (3DTouch vs authentic)

### What This Enables
- **Tier 3**: SuperPINDA + MK52 bed = maximum reliability (reference spec)
- **Tier 1-2**: BLTouch + scavenged glass bed = universal compatibility
- **All Tiers**: Z-tilt calibration and mesh bed leveling (both probes support)

### What This Replaces
- Single-probe assumption (no longer viable for mixed bed inventory)
- Glass-bed + inductive probe combinations (won't work)
- Universal probe recommendation (bed-surface dependent)

## BOM Implications (Generic)

### Tier 3: Reference Spec (SuperPINDA + MK52)
- **Parts needed**:
  - 1x SuperPINDA probe (Prusa or high-quality clone)
  - 1x MK52 magnetic spring steel sheet (250x250mm)
  - 1x Magnetic build surface (under spring steel)
  - 1x Probe mounting bracket
  - 3x Female-to-female dupont cables (VCC, GND, Signal)
- **Cost implication**: Low-Medium (~$50-70 AUD for probe + bed)
- **Bed compatibility**: Metal only (spring steel required)
- **Reliability**: Maximum (solid-state, no moving parts)
- **Maintenance**: None (set-and-forget)

### Tier 1-2: Scavenger Fallback (BLTouch + Glass)
- **Parts needed**:
  - 1x BLTouch V3.1 (authentic) or 3DTouch clone
  - 1x Scavenged bed (glass, etc.)
  - 1x Probe mounting bracket
  - 5x Female-to-female dupont cables (VCC, GND, Signal, Control, Servo)
- **Cost implication**: Low (~$15-60 AUD depending on authenticity)
- **Bed compatibility**: Universal (any surface)
- **Reliability**: Moderate (moving parts, potential pin failure)
- **Maintenance**: Periodic pin inspection, occasional replacement

### Hybrid Option: BLTouch on Metal Bed
- **Use Case**: User has metal bed but prefers BLTouch familiarity
- **Cost implication**: Same as BLTouch + metal bed (~$50-70 AUD)
- **Trade-off**: Loses SuperPINDA reliability advantages
- **Recommended**: Only if user has strong BLTouch experience or spare parts

### Universal Requirements (All Options)
- **Z-Max Switch**: Required regardless of probe choice (see ADR-013)
- **Mounting Bracket**: 3D-printed bracket to secure probe to X-carriage
- **Klipper Configuration**: `[probe]` or `[bltouch]` section based on choice
- **Z-Offset Calibration**: Required for both probes (probe to nozzle distance)

## Implementation Notes

### SuperPINDA Klipper Configuration
```ini
[probe]
pin: ^PC2    # Example pin, adjust for board
x_offset: -10
y_offset: 20
z_offset: 1.6   # Calibrated via PROBE_CALIBRATE
samples: 3
sample_retract_dist: 2.0
speed: 5.0

[bed_mesh]
mesh_min: 30,30
mesh_max: 220,220
probe_count: 3,3
```

### BLTouch Klipper Configuration
```ini
[bltouch]
sensor_pin: ^PC2
control_pin: PA2
x_offset: -10
y_offset: 20
z_offset: 1.6
stow_on_each_sample: False
probe_with_touch_mode: True

[safe_z_home]
home_xy_position: 150,150
speed: 50
z_hop: 10
```

### Probe Calibration Procedure
```bash
# Home all axes
G28

# Calibrate Z-offset
PROBE_CALIBRATE

# Test repeatability
PROBE_ACCURACY

# (BLTouch only) Test pin deployment
BLTOUCH_DEBUG COMMAND=pin_down
BLTOUCH_DEBUG COMMAND=pin_up
```

### Mounting Considerations

**SuperPINDA**:
- Mount ~5mm above bed surface when deployed
- Ensure bed is flat (spring steel on magnetic surface)
- No need for retraction mechanism
- Secure firmly (no vibration or movement)

**BLTouch**:
- Mount so pin deploys ~2-3mm above bed
- Test pin deployment before first print
- Verify pin retraction doesn't collide with bed clips
- Check for pin bending after print failures

### Troubleshooting

**SuperPINDA**:
- **Issue**: Probe doesn't trigger
  - Check bed is metal (spring steel)
  - Verify probe is within 4mm of bed surface
  - Test with multimeter (check signal pin toggles)
- **Issue**: Inconsistent readings
  - Clean bed surface (metal debris can affect inductive)
  - Check wiring for loose connections
  - Verify probe mounting is secure

**BLTouch**:
- **Issue**: Pin doesn't deploy
  - Check servo control wiring
  - Verify `[bltouch]` section in config
  - Test pin manually with BLTOUCH_DEBUG commands
- **Issue**: Pin stuck in deployed position
  - Emergency retract: BLTOUCH_DEBUG COMMAND=reset
  - Check for debris or bent pin
  - May need to disassemble and clean

### Safety Considerations
- **BLTouch Pin Breakage**: Can occur if nozzle crashes into bed or print curls up
- **SuperPINDA Distance**: Too far from bed = won't trigger; too close = premature trigger
- **Wiring**: Use shielded cables to prevent EMI interference
- **Hotend Temperature**: BLTouch pin can deform near hot nozzle (ensure proper mounting)

## References
- **docs/reference/ai-conversations/pinda-v-bltouch.md**: Complete probe comparison
- **docs/adr/013-drivers-endstops.md**: Driver and endstop strategy
- **docs/adr/005-triple-z.md**: Triple-Z kinematic leveling
- Klipper Probe Guide: [Probe Bed Calibrate](https://www.klipper3d.org/Probe_Calibrate.html)
- Klipper BLTouch Guide: [BLTouch](https://www.klipper3d.org/BLTouch.html)
- Prusa SuperPINDA Documentation: [Prusa Knowledge Base](https://help.prusa3d.com/en/guide/44704-prusa-superpinda_484760)

## Evolution Notes
This ADR establishes SuperPINDA as the Reference Spec probe for maximum reliability. Future probe technologies will be evaluated against: solid-state reliability, bed-surface compatibility, thermal stability, and cost. BLTouch remains the universal fallback for scavenger builds with non-metal beds.

**Emerging Technologies**:
- LVDT sensors (high-precision, expensive)
- Capacitive sensors (work on some non-metal surfaces, experimental)
- Optical sensors (complex, not widely adopted)

Current consensus favors inductive (SuperPINDA) for metal beds and physical (BLTouch) for universal compatibility.
