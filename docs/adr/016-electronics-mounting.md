# ADR-016: Electronics & PSU Mounting Strategy

## Status
Accepted

## Context
The Neo-Darwin requires decisions on where to mount the mainboard, host (Pi/SKIPR), and power supply unit (PSU). The placement affects:

**Vibration Physics**:
- Electronics and stepper drivers are sensitive to vibration
- High-torque Wade extruder and 3xZ motors generate significant vibration
- Direct coupling vs isolation affects reliability and signal integrity

**Serviceability**:
- Mainboard maintenance access
- PSU replacement
- Wire management for repairs

**Thermal Management**:
- TMC2209 drivers generate heat
- MOSFETs for heated bed can run hot
- Convection airflow vs active cooling

**Weight Distribution**:
- PSU weight adds to machine mass
- Location affects center of gravity
- Affects portability

With laminated plinth (ADR-011) and modular puck system (ADR-009), multiple mounting options exist.

## Decision
We adopt a **three-tier electronics mounting strategy** with **direct MDF coupling as Reference Spec**.

### Mounting Options

**Option A: Direct to Laminated Plinth (Reference Spec)**
- **Architecture**: Mainboard and PSU bolted directly to laminated MDF plinth
- **Vibration Strategy**: Direct coupling to vibration sink (MDF CLD kills frame vibration)
- **Weight**: PSU adds to plinth mass (lowers center of gravity)
- **Thermal**: Open bottom square, natural convection + optional quiet fan
- **Cost**: $0 (uses MDF plinth from ADR-011)
- **Best For**: Tier 3 Reference Spec builds

**Option B: Printed "Brain Puck" Frame (Alternative)**
- **Architecture**: 3D-printed puck/frame holds mainboard and PSU
- **Vibration Strategy**: Lightweight plastic, couples to workspace surface
- **Weight**: Self-contained, portable
- **Thermal**: Enclosed or honeycomb design, may require active cooling
- **Cost**: Low (~$5-10 AUD in filament)
- **Best For**: Tier 1-2 builds without plinth, portable maintenance

**Option C: Hybrid - Printed Puck to MDF (Tier 3 Enhancement)**
- **Architecture**: Printed "Brain Puck" screwed into laminated MDF plinth
- **Vibration Strategy**: MDF plinth provides damping, puck provides modularity
- **Weight**: Puck + PSU contribute to plinth mass
- **Thermal**: Open design with MDF backing for heat sink
- **Cost**: Low (~$5-10 AUD in filament)
- **Best For**: Tier 3 with modular electronics upgrades

### Vibration Physics: Coupling vs Isolation

**Direct Coupling to MDF (Reference)**:
- Frame bolted directly to plinth (no rubber between)
- MDF acts as massive vibration sink
- Constrained Layer Damping (ADR-011) converts vibration to heat
- Electronics experience minimal transmitted vibration
- **Recommendation**: Direct coupling preferred for "Tractor" reliability

**Bolting Through Rubber (Isolation)**:
- Rubber pads between frame and MDF, bolts through to plinth
- Creates tuned mass damper
- Can reduce high-frequency transmission
- **Trade-off**: Reduces coupling, may allow slight frame movement
- **Recommendation**: Use rubber pads **under plinth**, not between frame and plinth

**Isolation Under Plinth**:
- 4x rubber feet under MDF plinth corners
- Isolates entire 20kg+ machine from desk
- Prevents desk from becoming sounding board
- **Recommendation**: Mandatory for all tiers with plinth

### Electronics Placement Comparison

| Feature | Direct to MDF (Reference) | Printed Brain Puck (Alternative) |
|---------|--------------------------|----------------------------------|
| **Vibration Damping** | **Superior** (MDF mass) | Poor (light plastic) |
| **Maintenance** | Permanent (harder to remove) | **Excellent** (modular) |
| **Cost** | Minimal (screws) | Low (filament) |
| **Airflow** | Open, natural convection | Restricted if enclosed |
| **Portability** | Low (part of plinth) | **High** (standalone) |
| **Serviceability** | Moderate | **Excellent** |

### PSU Mounting Strategy

**Positioning**:
- **Bottom Rear Corner**: Standard placement, balances weight distribution
- **Bottom Front Corner**: Easier access, but may affect Z-homing
- **On MDF Plinth**: Recommended (adds mass, stable)
- **In Brain Puck**: Only for puck-frame builds

**Wiring Considerations**:
- **High-Current Wires** (heated bed): Use thick gauge (14-16 AWG) to prevent voltage drop
- **Low-Current Wires** (signal): Keep away from high-voltage wiring to prevent EMI
- **Cable Chains**: Required for X/Y axis loom to prevent snagging on moving bed
- **Wire Length**: Keep as short as possible within safety margins

**Thermal Management**:
- **PSU Ventilation**: Ensure airflow, don't enclose
- **TMC Drivers**: Can overheat at high currents, add slow quiet fan if needed
- **MOSFETs**: May need heatsinks or active cooling for high-current beds

### Wiring Loom Design

**Voltage Drop Mitigation**:
- Heated bed draws highest current (10-15A)
- Use 14 AWG or 16 AWG wire for bed power
- Keep bed power wires short and direct
- Monitor for overheating wires (should not feel hot)

**EMI Protection**:
- Keep endstop and probe wires away from motor/bed power wires
- Use twisted pairs for signal wires
- Shield long signal cables
- Separate high-current and low-current wiring in cable chains

**Cable Chain Routing**:
- X/Y axis loom from mainboard to gantry
- Separate: motors (power), endstops (signal), probe (signal)
- Use cable chain or umbilical (bundle held by filament)
- Prevent snagging on moving bed components

## Consequences

### Benefits
- **Tiered Flexibility**: Direct MDF (Reference), Printed Puck (Alternative), Hybrid (Best of both)
- **Vibration Optimization**: Direct coupling to CLD plinth provides industrial-grade damping
- **Modularity**: Printed puck enables easy mainboard upgrades without unbolting frame
- **Serviceability**: Multiple options from permanent (Reference) to modular (Puck)
- **Thermal Management**: Open designs provide natural convection, fan options available

### Trade-offs
- **Direct to MDF**: Permanent, harder to remove for mainboard replacement
- **Printed Puck**: Poor vibration damping (lightweight plastic)
- **Hybrid**: Adds filament cost, but provides modularity + damping

### What This Enables
- **Tier 3 Reference**: Direct MDF mounting for maximum damping
- **Tier 1-2 Alternative**: Printed puck builds without plinth
- **All Tiers**: Proper wire management (voltage drop, EMI protection)
- **Future Upgrades**: Modular puck allows mainboard swaps

### What This Replaces
- Mainboard mounting to M12 frame (transmits vibration)
- PSU mounting to moving gantry (adds mass to moving parts)
- Uncontrolled wire runs (voltage drop, EMI issues)
- Enclosed electronics boxes (poor thermal management)

## BOM Implications (Generic)

### Tier 3 Reference: Direct to MDF Plinth
- **Parts needed**:
  - MDF plinth (already in ADR-011)
  - 4x Rubber feet for plinth (vibration isolation)
  - Mounting screws for mainboard and PSU
  - Optional: Slow quiet 120mm fan for electronics cooling
- **Cost implication**: Very Low (~$10-15 AUD for feet + screws)
- **Vibration Damping**: Superior (MDF mass)
- **Maintenance**: Moderate (permanently mounted)
- **Thermal Management**: Open, natural convection

### Tier 1-2 Alternative: Printed Brain Puck
- **Parts needed**:
  - 3D-printed "Brain Puck" frame/enclosure
  - Mounting hardware (standoffs, screws)
  - Optional: 4x Rubber feet for puck
- **Cost implication**: Very Low (~$5-10 AUD in filament)
- **Vibration Damping**: Poor (lightweight plastic)
- **Maintenance**: Excellent (modular, portable)
- **Thermal Management**: May require active cooling fan

### Tier 3 Enhancement: Hybrid (Puck to MDF)
- **Parts needed**:
  - 3D-printed "Brain Puck" with mounting holes
  - Wood screws to secure puck to MDF
  - MDF plinth (already in ADR-011)
  - 4x Rubber feet for plinth
- **Cost implication**: Very Low (~$5-10 AUD in filament)
- **Vibration Damping**: Superior (MDF mass)
- **Maintenance**: Excellent (puck can be unscrewed for upgrades)
- **Thermal Management**: Open with MDF backing (heat sink)

### Universal Requirements (All Options)
- **PSU**: 12V or 24V (sufficient current: 20A for 12V, 12A for 24V)
- **Wiring**:
  - 14-16 AWG for heated bed
  - 18-20 AWG for hotend/fans
  - 22-24 AWG for signals
  - Shielded cables for long signal runs
- **Cable Management**: Cable chains or umbilicals for X/Y loom
- **EMI Protection**: Separate high-current and low-current wiring

## Implementation Notes

### Direct to MDF Mounting (Reference)

**Mainboard Mounting**:
- Use M3 or M4 standoffs (height ~10mm)
- Secure to MDF with wood screws
- Ensure flat mounting surface (no warping)
- Leave clearance for connectors on all sides

**PSU Mounting**:
- Bottom rear corner of plinth
- Use 4x M4 or M5 bolts through PSU mounting holes
- Secure to MDF with large fender washers
- Ensure ventilation holes are not blocked
- Leave space for wiring access

**Wiring Layout**:
```
Bottom Square Layout:
┌─────────────────────────────────────┐
│          [MDF Plinth]             │
│  ┌─────┐    ┌──────────────┐    │
│  │PSU  │    │  Mainboard    │    │
│  └─────┘    │  (SKIPR/Manta)│    │
│              └──────────────┘    │
│         [Cable Chain to Gantry]    │
└─────────────────────────────────────┘
```

### Printed Brain Puck Design

**Puck Frame Specifications**:
- Fits within bottom M12 square
- Holds mainboard + PSU (if compact)
- Honeycomb or perforated sides for airflow
- Mounting holes for MDF attachment (if hybrid)
- Cable management loops for wire routing

**Mounting to Puck**:
- Mainboard on standoffs (10mm height)
- PSU either on puck or next to puck
- Leave access for connectors and fan mounting
- Wire management channels to prevent tangling

**Hybrid Puck to MDF**:
- Puck screwed into MDF with 4x wood screws
- Puck provides modularity, MDF provides damping
- Remove puck for mainboard upgrades without unbolting frame

### Wire Management

**Voltage Drop Calculation**:
```
V_drop = I × R × L
I = Current (heated bed ~12A)
R = Resistance per meter (14 AWG: 0.0083 Ω/m)
L = Length in meters (keep <2m if possible)

Example: 12A × 0.0083 × 1.5m = 0.15V drop (acceptable)
```

**EMI Protection**:
- Separate power and signal wires by at least 20mm
- Use twisted pairs for signal wires
- Shield long signal cables (connect shield to ground at one end)
- Keep motor wires away from endstop/probe wires

**Cable Chain Routing**:
- Bundle X/Y axis wires (motors + endstops + probe)
- Use cable chain from mainboard to X/Y gantry
- Prevent snagging on moving bed or Z-rods
- Leave slack for full travel range

### Thermal Management

**TMC Driver Cooling**:
- Check driver temperature with Klipper: `DUMP_TMC STEPPER=stepper_x`
- Add slow quiet 120mm fan if drivers > 60°C
- Point airflow across heatsinks, not directly at components

**PSU Ventilation**:
- Ensure ventilation holes are not obstructed
- Keep at least 10mm clearance around PSU
- If enclosed, add exhaust fan for hot air removal

**MOSFET Cooling**:
- Check heated bed MOSFET temperature during heating cycle
- Add small heatsink or directed airflow if > 60°C

### Safety Considerations
- **PSU Mounting**: Secure with proper bolts, don't rely on gravity
- **Wire Gauge**: Use appropriate gauge for current (voltage drop = fire risk)
- **Ventilation**: Don't enclose PSU without exhaust fan (overheating = fire risk)
- **Water Protection**: If using laminated plinth, seal MDF edges to prevent moisture absorption
- **Strain Relief**: Use cable glands or zip ties to prevent wire fatigue

## References
- **docs/reference/ai-conversations/electronics-mounting.md**: Complete mounting discussion
- **docs/adr/011-laminated-plinth.md**: Laminated plinth baseboard foundation
- **docs/adr/009-puck-system.md**: Modular puck mounting system
- **docs/adr/012-mainboard-host-architecture.md**: Mainboard selection
- Klipper Wiring Guide: [Wiring](https://www.klipper3d.org/Installation.html#check-and-connect-all-wiring)
- AWG Wire Gauge Chart: [Wire Size Calculator](https://www.calculator.net/voltage-drop-calculator.html)

## Evolution Notes
This ADR establishes direct MDF coupling as Reference Spec with printed puck as alternative. The decision framework prioritizes:
- Vibration damping (MDF mass over portability)
- Serviceability (modular pucks for easy upgrades)
- Thermal management (open designs, natural convection)
- Wire management (voltage drop, EMI protection)

Future mounting systems will be evaluated against: vibration damping performance, serviceability, thermal efficiency, and modularity for mainboard upgrades.
