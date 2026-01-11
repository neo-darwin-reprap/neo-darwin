# ADR-006: Z-Probe Selection (BLTouch vs PINDA)

## Status
Accepted

## Context
The Z-probe is critical for accurate first-layer height detection. It measures the bed surface precisely and enables automated bed leveling and Z-offset calibration.

In 2026, there are multiple Z-probe options:
- BLTouch v3.1 (mechanical servo probe)
- PINDA v2 (inductive probe - Prusa style)
- ADXL345 accelerometer (resonance testing + limited Z-probe)
- Probeless (manual Z-offset)

The Neo-Darwin's Triple-Z system provides physical leveling, but a Z-probe is still needed for:
- Initial Z-offset calibration
- Mesh bed leveling (for warped beds)
- Z-Tilt calibration assistance
- Power-loss recovery Z-position

## Decision
We choose **BLTouch v3.1** as the reference Z-probe for Neo-Darwin, with PINDA v2 as a budget alternative.

### Why BLTouch?
1. **Universal compatibility**: Works with all bed materials (aluminum, PEI, glass, ceramic)
2. **Precise repeatability**: ±0.02mm accuracy
3. **Self-test**: Built-in pin deployment test
4. **Software mature**: Extensive Klipper support and community knowledge
5. **Adjustable**: Pin height can be calibrated
6. **Versatile**: Can probe at multiple points for mesh leveling
7. **Mounting flexibility**: Standard 30mm hole pattern

### PINDA Alternative
- **Cost**: ~$10 cheaper than BLTouch
- **Simpler**: No moving parts, more reliable
- **Limitation**: Only works with metal beds (aluminum, magnetic PEI)
- **Less common**: More community support for BLTouch

## Consequences

### Benefits
- **Automated calibration**: No manual Z-offset adjustment
- **Mesh leveling**: Can compensate for bed warping (±0.5mm)
- **Z-Tilt assist**: Helps Klipper calibrate Triple-Z tilt
- **Power-loss recovery**: Knows exact Z-position after power failure
- **First-layer consistency**: Repeatable probe hits

### Trade-offs
- **Wiring complexity**: Requires 3-4 wires + 5V/GND
- **Mounting space**: Needs clearance on toolhead carriage
- **Cost**: ~$25 AUD
- **Moving parts**: Mechanical pin can fail (but has test function)

### Why NOT Probeless?
1. **Manual tuning**: Requires paper method for Z-offset
2. **No mesh compensation**: Can't handle warped beds
3. **Power loss**: Cannot resume prints correctly
4. **Not "set-and-forget"**: Requires periodic manual adjustment

## BOM Implications (Generic)

### Scenario A: Buying New BLTouch v3.1 (Recommended for Tier 3+)
- **Parts needed**:
  - BLTouch v3.1 (Antclabs clone acceptable)
  - 3D-printed probe mount (included with Wade carriage)
  - 3-pin or 5-pin cable (usually included)
  - 5V power from board
- **Cost implication**: Low (~$25 AUD)
- **Donor compatibility**: All donors (new purchase)
- **Bed compatibility**: All bed types (PEI, glass, aluminum, ceramic)
- **Experience**: Automated calibration

### Scenario B: Salvaging BLTouch from Donor (Ender 3, CR-10)
- **Parts needed**:
  - Salvage: BLTouch from donor
  - 3D-printed probe mount (may need redesign for donor mounting)
  - **Pinout check**: Ender 3 and CR-10 use different BLTouch wiring
- **Cost implication**: Very Low ($0-5 AUD for mount)
- **Donor compatibility**: Ender 3, CR-10, Prusa MK3 (has BLTouch)
- **Warning**: May need to repin connector (Ender 3 uses 5-pin, others use 3-pin)

### Scenario C: Buying PINDA v2 (Budget Alternative)
- **Parts needed**:
  - PINDA v2 probe
  - 3D-printed probe mount
  - 2-pin cable (usually included)
  - **Metal bed required**: Aluminum or magnetic PEI
- **Cost implication**: Very Low (~$15 AUD)
- **Donor compatibility**: All donors (new purchase)
- **Bed compatibility**: Metal beds ONLY (no PEI, no glass)
- **Experience**: Automated calibration

### Scenario D: Salvaging PINDA from Donor (Prusa MK2/3)
- **Parts needed**:
  - Salvage: PINDA from donor
  - 3D-printed probe mount (may need redesign)
- **Cost implication**: Very Low ($0-5 AUD for mount)
- **Donor compatibility**: Prusa MK2/3
- **Bed compatibility**: Must use metal bed with donor
- **Note**: Prusa MK3 has SuperPINDA (better performance)

### Scenario E: ADXL345 Only (Not Recommended)
- **Parts needed**:
  - ADXL345 accelerometer (already needed for Input Shaping)
  - Probeless setup (manual Z-offset)
- **Cost implication**: Low (already have ADXL)
- **Donor compatibility**: All donors
- **Experience**: Manual Z-offset tuning
- **Note**: ADXL cannot measure Z-height accurately for bed leveling
- **Warning**: No power-loss recovery Z-position, manual mesh leveling

### Scenario F: Probeless Manual (Tier 1 Only)
- **Parts needed**: None
- **Cost implication**: $0
- **Donor compatibility**: All donors
- **Experience**: Manual Z-offset tuning with paper method
- **Warning**: Not "set-and-forget", high maintenance required

## Implementation Notes

### BLTouch Mounting
- **Location**: On Wade X-carriage, offset to right of nozzle
- **Clearance**: 10mm clearance from hotend to prevent interference
- **Height**: Pin extends 5mm below mount when deployed
- **Mount pattern**: Standard 30mm × 20mm BLTouch hole pattern

### Probe Modes
```
1. Z-Tilt Calibration (Triple-Z):   Probe 3 corners, calculate tilt
2. Mesh Bed Leveling:               Probe 5×5 or 7×7 grid for warping
3. Z-Offset Calibration:            Probe at center, set offset
4. Power-Loss Recovery:             Record Z-position at interrupt
```

### Wiring
```
BLTouch v3.1 (5-pin):
- Pin 1: GND
- Pin 2: VCC (5V)
- Pin 3: Servo PWM
- Pin 4: Servo GND
- Pin 5: Z-Probe Input

BLTouch v3.1 (3-pin older):
- Pin 1: GND
- Pin 2: VCC (5V)
- Pin 3: Z-Probe Input

Klipper config: [bltouch] section
```

### Bed Compatibility
```
BLTouch:         All bed types ✓
                 - Aluminum heated bed ✓
                 - Aluminum + glass ✓
                 - Aluminum + PEI sheet ✓
                 - Aluminum + ceramic ✓
                 - Non-heated surfaces ✓

PINDA v2:        Metal beds only ✓
                 - Aluminum heated bed ✓
                 - Aluminum + magnetic PEI ✓ (metal particles in sheet)
                 - Aluminum + glass ✗ (cannot see through glass)
                 - Aluminum + non-magnetic PEI ✗ (cannot detect through PEI)
                 - Non-metal beds ✗ (no metal to detect)

SuperPINDA:      Metal beds only (better range) ✓
                 - Same as PINDA but with longer range and better stability

Probeless:       All bed types (manual) ✓
                 - Manual paper method
                 - Works with any bed surface
```

**Key PINDA Limitation:**
PINDA is an inductive sensor that detects metal surfaces. It works:
- Through magnetic PEI (has metal particles) ✓
- Directly on aluminum ✓
- BUT cannot work through glass or non-magnetic PEI sheets

Common 3D printer bed stacks:
- Aluminum + Glass: PINDA cannot work (must use BLTouch)
- Aluminum + Magnetic PEI: Both work
- Aluminum + Non-magnetic PEI: Must use BLTouch
- Unheated (wood, etc.): Must use BLTouch

### Calibration
1. **Z-Tilt Initial**: Use BLTouch for automated calibration
2. **Z-Offset**: Probe at center, adjust until first layer perfect
3. **Mesh Leveling**: Probe grid if bed warped (>0.1mm variation)
4. **Repeatability Test**: Probe same point 10×, check variation

### Mounting on Wade Carriage
- **Mount bracket**: 3D-printed part of Wade carriage design
- **Offset**: 35mm from nozzle (standard BLTouch offset)
- **Protection**: Mount probe above hotend to heat damage
- **Cable routing**: Route cable away from hotend

### PINDA vs BLTouch Decision Tree
```
Have metal bed (aluminum, magnetic PEI)?
  YES → PINDA v2 ($15) or BLTouch ($25)
   NO → MUST use BLTouch ($25)

Budget < $20?
  YES → PINDA (if metal bed) or Manual
   NO → BLTouch (recommended)

Have donor with BLTouch?
  YES → Salvage + redesign mount
   NO → Buy new BLTouch

Want mesh bed leveling?
  YES → BLTouch (PINDA cannot mesh)
   NO → Either works
```

### Software Configuration
```
# Klipper config for BLTouch
[bltouch]
sensor_pin: ^P1.24  # Change to your board pin
control_pin: P1.26
x_offset: 35.0      # mm from nozzle
y_offset: 0.0
z_offset: 1.5       # Adjust after calibration

[safe_z_home]
home_xy_position: 150,150  # Center of bed
speed: 50
z_hop: 10                  # Raise before moving
z_hop_speed: 5
```

### Maintenance
- **Clean pin**: Remove plastic buildup every 50 hours
- **Test deployment**: Run `BLTOUCH_DEBUG COMMAND=pin_down` then `pin_up`
- **Check wiring**: Verify no loose connections
- **Calibration**: Re-calibrate Z-offset after any bed changes

### Common Issues
- **Probe fails to deploy**: Check 5V power, servo pin wiring
- **False triggers**: Ensure no metal debris near probe, check noise filtering
- **Drift**: Z-offset may change slightly over first 10 hours of use
- **Temperature drift**: PINDA affected by ambient temperature (use SuperPINDA if critical)

## References
- [BLTouch v3.1 Documentation](https://www.antclabs.com/bltouch-v3)
- [PINDA v2 Documentation](https://help.prusa3d.com/guide/3d-printers-original-prusa/pinda-v2_34290)
- [Klipper Bed Probe Guide](https://www.klipper3d.org/Probe_Calibrate.html)
- docs/AI-Conversations/ [Relevant conversations about Z-probe selection]
