# ADR-015: Single Toolhead Architecture

## Status
Accepted

## Context
The Neo-Darwin requires a decision on multi-material/color capability. Three approaches exist in 2026:

**1. Single Toolhead** (Base Spec)
- One hotend/extruder
- Manual material changes (swap filament manually)
- No waste, no complexity
- Cost: $0 additional

**2. Filament Swapper** (e.g., ERCF v2)
- Single hotend, multiple filament inputs
- Switches filament behind nozzle
- High waste (purge tower), same-material limitation
- Cost: ~$150 AUD
- Best for: Multi-color PLA prints

**3. Tool-Changer** (e.g., Tapchanger, Prusa XL)
- Multiple hotends/extruders on automated docking system
- Near-zero waste, true multi-material (PLA+TPU+PVA)
- Extreme mechanical complexity
- Cost: $300-600+ AUD
- Best for: Professional multi-material production

**Key Engineering Trade-offs**:
- **Cost**: Single → ERCF → Tool-changer (exponential increase)
- **Complexity**: Low → High → Extreme (calibration nightmare)
- **Waste**: None → High → Near-zero
- **Multi-Material**: No → Same-material only → True multi-material

The Neo-Darwin's $300 AUD target and "Tractor" philosophy prioritizes reliability and low cost.

## Decision
We adopt a **Single Toolhead Base Spec** with **ERCF v2 as Official Expansion**.

### Base Spec: Single Toolhead
**Architecture**: One E3D V6/CHT hotend with Greg Wade extruder

**Why This Fits the "Tractor"**:
- **Cost**: $0 additional (already in BOM)
- **Reliability**: One hotend = one point of failure
- **Simplicity**: No calibration, no macro tuning
- **Maintenance**: Standard single-nozzle maintenance only
- **Speed**: No swap time, continuous printing
- **Best For**: Single-color/monochrome prints, prototype iteration

**Limitations**:
- Manual filament changes required
- No multi-material printing (without manual swap)
- No nozzle diversity (one nozzle size per print)

### Official Expansion: ERCF v2 (Filament Swapper)
**Architecture**: ERCF v2 with Bowden extension to single hotend

**Why ERCF Over Tool-Changer**:
- **Cost**: ~$150 AUD vs $300-600+ for tool-changer
- **Simplicity**: High complexity, but manageable macro tuning
- **Compatibility**: Uses single hotend (no multiple hotend costs)
- **Materials**: Handles 12+ colors in same material (e.g., PLA)
- **Proven**: Well-documented community support

**Trade-offs**:
- **Waste**: Requires purge tower (~10-20g waste per swap)
- **Speed**: 30-60s per filament swap
- **Materials**: Limited to same-material family (PLA+PLA, not PLA+TPU)
- **Tuning**: Requires macro calibration for reliable operation

**Best For**: Multi-color prints, hobbyist experimentation, color prototypes

### Rejected: Automated Tool-Changer
**Architecture**: Multiple hotends/extruders with automated docking

**Why Rejected for Neo-Darwin**:
- **Cost**: Violates $300 AUD target immediately
- **Complexity**: Sub-millimeter mechanical offsets required
- **Calibration**: Tool A must be within 0.1mm of Tool B (expert-level tuning)
- **Failure Points**: Docking system, multiple hotends, multiple extruders
- **Not "Tractor"**: Requires constant tweaking, contradicts "set-and-forget" philosophy

**Tool-Changer Advantages** (for reference):
- Near-zero waste (tiny prime tower)
- True multi-material (PLA+TPU+PVA in same print)
- Nozzle diversity (0.4mm + 0.8mm on same job)
- Fast swaps (<10s)

**When to Consider Tool-Changer**:
- Professional multi-material production needs
- Budget $600+ AUD beyond base spec
- Expert-level calibration skills and patience
- Multi-material (not just multi-color) requirements

### Manual Tool Swaps via Puck System (ADR-009)
While automated tool-changing is rejected, the **Modular Puck System** enables manual tool swaps:

**Supported Pucks**:
- **3D Printing Puck**: Standard hotend + extruder
- **Laser Engraving Puck**: 5W-10W diode laser
- **Pen Plotting Puck**: Sharpie or technical pen holder
- **Drag Knife Puck**: Vinyl/cutting blade

**Workflow**:
1. Print completes
2. Power off machine
3. Unscrew 3D printing puck
4. Install laser/pen puck
5. Power on
6. Run `TOOL_OFFSET` calibration macro
7. Execute laser/pen job

**Benefits**:
- **CNC-Style Versatility**: One machine, multiple purposes
- **No Docking Complexity**: Manual swap eliminates automated failure points
- **Cost-Effective**: Each puck ~$20-50 AUD
- **Reliability**: No automated mechanism to fail

**Limitations**:
- Not automated (30-second manual swap required)
- Power cycle between swaps (safety requirement)
- No in-print tool changing (separate jobs)

## Consequences

### Benefits
- **Tiered Flexibility**: Base (single) → Expansion (ERCF) → Advanced (manual pucks)
- **Cost Alignment**: Base spec maintains $300 AUD target
- **Reliability Priority**: Single toolhead = minimal failure points
- **Future-Proof**: ERCF adds color without changing core architecture
- **CNS-Style Expansion**: Manual puck swaps for laser/pen capabilities

### Trade-offs
- **Base Spec**: No multi-color capability (requires manual filament swap)
- **ERCF**: Waste generation (purge tower), same-material limitation
- **No Automated Tool-Changing**: True multi-material (PLA+TPU) requires separate machine or expensive upgrade

### What This Enables
- **Base Spec**: Reliable single-nozzle printing for <$300 AUD
- **Tier 2 Expansion**: ERCF v2 adds 12+ color capability for ~$150 AUD
- **Tier 3 Expansion**: Manual puck swaps for laser/pen/drag knife
- **All Tiers**: Focus on reliability and "set-and-forget" philosophy

### What This Replaces
- Multi-toolhead systems (tool-changers)
- Dual-extruder setups (bowden systems)
- Automated docking systems
- Cross-platform multi-material machines

## BOM Implications (Generic)

### Base Spec: Single Toolhead
- **Parts needed**:
  - 1x E3D V6/CHT hotend (already in BOM)
  - 1x Greg Wade extruder (already in BOM)
  - 1x Toolhead puck (already in ADR-009)
- **Cost implication**: $0 (included in base spec)
- **Capability**: Single-color/monochrome printing
- **Maintenance**: Standard hotend/extruder maintenance only

### Tier 2 Expansion: ERCF v2
- **Parts needed**:
  - 1x ERCF v2 kit (gears, selectors, servos)
  - 1x Servo motor (SG90 or MG90S)
  - 12x Filament tube holders
  - 3D-printed ERCF parts (body, gears, mounting)
  - 1x Bowden extension cable (hotend to ERCF)
  - 1x CAN bus cable (if using remote CAN board)
- **Cost implication**: ~$150 AUD
- **Capability**: 12+ colors, same-material family
- **Complexity**: High (macro calibration required)
- **Prerequisites**: Base spec built, Klipper configured, CAN bus if needed

### Tier 3 Expansion: Manual Pucks
- **Parts needed per puck**:
  - 1x Puck base (3D-printed, standard interface from ADR-009)
  - 1x Device mounting hardware (laser heatsink, pen holder, etc.)
  - 1x Wiring harness (device-specific)
- **Cost implication**: Low (~$20-50 AUD per puck)
- **Capability**: Laser engraving, pen plotting, drag knife cutting
- **Complexity**: Low (manual swap, calibration macro)
- **Prerequisites**: Base spec built, Klipper profiles configured

### Tier 4 (Rejected): Automated Tool-Changer
- **Parts needed**:
  - 3-4x Complete toolheads (hotend + extruder + nozzle)
  - 1x Automated docking system (gantry, sensors, actuators)
  - 1x Kinematic coupling system (ball locks, precision alignment)
  - Extra drivers (1-2 per additional toolhead)
  - Extended wiring harnesses
- **Cost implication**: Very High ($300-600+ AUD)
- **Capability**: True multi-material (PLA+TPU+PVA), zero waste
- **Complexity**: Extreme (sub-millimeter calibration, expert-level tuning)
- **Status**: Rejected for Neo-Darwin (violates cost/reliability targets)

## Implementation Notes

### Base Spec Configuration
```ini
[extruder]
step_pin: PB7
dir_pin: PB6
enable_pin: !PA8
microsteps: 16
rotation_distance: 7.5  # Greg Wade gear ratio

[heater_generic hotend]
pin: PA1
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PC2
min_temp: 0
max_temp: 300
control: pid

[fan]
pin: PA3
```

### ERCF v2 Configuration
```ini
[extruder]
step_pin: PB7
dir_pin: PB6
enable_pin: !PA8
microsteps: 16
rotation_distance: 7.5

# ERCF-specific settings
[gcode_macro ERCF_SELECT_COLOR]
variable_color_index: 0
gcode:
  # ERCF macro sequence
  # 1. Retract filament from hotend
  # 2. Select color via servo
  # 3. Load new filament
  # 4. Purge to wipe tower
```

### Manual Tool-Swap Macros

**Laser Puck Profile**:
```ini
[gcode_macro LASER_MODE]
description: Switch to laser engraving mode
gcode:
  G28                     # Home
  SET_HEATER_TEMPERATURE HEATER=heater_generic_hotend TARGET=0
  # User: Power off, swap puck
  # Power on, run LASER_OFFSET
  SET_VELOCITY_LIMIT VELOCITY=3000 ACCEL=500  # Laser-safe limits
  SET_EXTRUDER_STEP_DISTANCE DISTANCE=0        # Disable extruder
```

**Tool Offset Calibration**:
```ini
[gcode_macro TOOL_OFFSET]
description: Calibrate tool offset after puck swap
gcode:
  G28 X Y
  G0 Z10 F300
  # Manual calibration steps
  # 1. Move nozzle to known position (e.g., bed center)
  # 2. Measure offset from new tool
  # 3. Set TOOL_OFFSET_X/Y
  # 4. Save to config
```

### Puck System Integration
- All pucks use standard interface from ADR-009
- Toolhead puck is "base" reference (0,0,0)
- Laser/pen pucks have calibrated offsets
- Offsets stored in Klipper `[tool_offset]` sections

### Safety Considerations
- **Laser Puck**: Always power off before swap, verify wavelength/功率 safety
- **Manual Swaps**: Power off machine before puck changes (safety requirement)
- **ERCF**: Jam detection, filament runout sensors recommended
- **Hotend**: Always cool before puck removal

## References
- **docs/reference/ai-conversations/multi-toolhead.md**: Complete multi-tool discussion
- **docs/adr/009-puck-system.md**: Modular puck mounting system
- **docs/adr/002-greg-wade.md**: Extruder architecture
- **docs/adr/004-v6-cht.md**: Hotend architecture
- ERCF v2 Documentation: [ERCF Official](https://github.com/Letmein1030/ERCF_v2)
- Tool-Changer References: [Tapchanger](https://tapchanger.com/), [Prusa XL](https://www.prusa3d.com/en/product/original-prusa-xl)

## Evolution Notes
This ADR establishes single toolhead as Base Spec with ERCF as official expansion. The decision framework remains:
- Cost: <$300 AUD (base), +$150 AUD (ERCF)
- Complexity: Low (base) → High (ERCF) → Extreme (tool-changer)
- Reliability: Maximum (base) → Manageable (ERCF) → Difficult (tool-changer)

Future automated tool-changer systems will be evaluated against:
- Sub-$100 AUD additional cost (unlikely)
- Plug-and-play calibration (no manual offset tuning)
- True multi-material capability (beyond ERCF same-material)

Until those criteria are met, manual puck swaps + ERCF remain the recommended path.
