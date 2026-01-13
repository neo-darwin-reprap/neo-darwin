# ADR-013: Driver & Endstop Strategy

## Status
Accepted

## Context
The Neo-Darwin requires a motion control strategy that balances reliability, cost, and accuracy. Key considerations:

**Driver Technology**:
- **"Smart" Drivers** (TMC2130, TMC2209, TMC2240): UART communication, sensorless homing, silent operation
- **"Dumb" Drivers** (A4988, DRV8825): Fixed step/dir, no communication, no sensorless homing

**Endstop Strategy**:
- **Sensorless Homing**: Detects motor stall (requires TMC drivers)
- **Mechanical Endstops**: Physical switches with electrical contact

**Z-Axis Safety**:
- **Moving Bed**: Neo-Darwin uses moving bed (bed drops for increased Z)
- **Bed-Drop Risk**: Power loss can cause heavy bed to back-drive lead screws and crash
- **Homing Logic**: BLTouch probes bed from below (Z-min at nozzle)

Salvaged donor boards often have "dumb" drivers (A4988/DRV8825) fixed to PCB, limiting sensorless options. However, mechanical switches offer superior repeatability and temperature stability.

## Decision
We adopt a **TMC2209-first strategy with mechanical endstops for reliability**.

### Driver Hierarchy

**Tier 1: Pure Scavenger (Dumb Drivers)**
- **Hardware**: Salvaged board with A4988/DRV8825 drivers
- **Acceptable For**: Triple-Z motors on Multi-MCU setup (Z-motors don't need sensorless homing)
- **Limitation**: X/Y must use mechanical endstops (no sensorless)
- **Trade-off**: No silent operation, no advanced features

**Tier 2: TMC2209 (Recommended)**
- **Hardware**: TMC2209 drivers (SKR Pico, BTT boards, or modular)
- **UART Mode**: Full Klipper communication for stealthchop, spreadcycle, current control
- **Silent Operation**: StealthChop at low speeds, SpreadCycle at high speeds
- **Cost**: ~$5-10 AUD per driver
- **Best For**: All axes, all tiers where budget allows

**Tier 3: High-End TMC (Optional)**
- **Hardware**: TMC2240 or TMC5160 drivers
- **Features**: Higher current, better heat dissipation, more diagnostic data
- **Cost**: ~$15-25 AUD per driver
- **Trade-off**: Overkill for "Tractor" speed envelope
- **Best For**: Voron-style "Racecar" builds

### Endstop Strategy

**X & Y Axes: Mechanical Endstops**
- **Hardware**: Standard mechanical microswitches (NO contacts preferred)
- **Position**: Physical end-of-travel on X and Y
- **Why Mechanical Over Sensorless**:
  - **Repeatability**: Mechanical switches have absolute position (±0.01mm)
  - **Temperature Stability**: No thermal drift (TMC stall detection temperature-sensitive)
  - **Reliability**: Works regardless of driver technology or wear
  - **Cost**: ~$2-5 AUD per switch
- **For TMC Builds**: Can use sensorless, but mechanical recommended for "Tractor" reliability
- **For "Dumb" Driver Builds**: Required (no alternative)

**Z-Axis: BLTouch Virtual Endstop**
- **Hardware**: BLTouch V3.1 or compatible probe
- **Position**: Nozzle tip acts as Z-min
- **How It Works**:
  - Bed moves up toward nozzle
  - BLTouch pin deploys, contacts bed
  - Klipper triggers Z-min interrupt
  - Z-tilt calibration uses BLTouch data
- **Why BLTouch**:
  - **Probing**: Essential for Z-tilt (three-point bed calibration)
  - **Mesh Bed Leveling**: Optional advanced leveling
  - **Reliability**: Well-tested, community-supported
- **Configuration**:
  ```ini
  [bltouch]
  sensor_pin: PB1
  control_pin: PB0

  [safe_z_home]
  home_xy_position: 150,150
  speed: 50
  z_hop: 10
  ```

**Z-Axis Safety: Z-Max Physical Endstop**
- **Hardware**: Mechanical microswitch at bottom of M12 frame
- **Position**: Absolute physical limit (bed cannot go lower)
- **Purpose**: Prevent "bed-drop" crash during power loss
- **How It Works**:
  - Gravity can back-drive lead screws when motors lose power
  - Heavy bed (~3-5kg) can crash into plinth/electronics
  - Z-max switch provides hardware interrupt to stop motion
- **Wiring**: Connect to Z-max pin on mainboard
- **Configuration**:
  ```ini
  [stepper_z]
  endstop_pin: probe:z_virtual_endstop
  position_min: -2
  position_max: 250

  [gcode_button z_max_safety]
  pin: PA2
  press_on_gcode: TURN_OFF_HEATERS ; Safety logic
  ```
- **Klipper Implementation**:
  - Z-max switch can trigger emergency stop (M112)
  - Or pause print and turn off heaters

### Driver Board Configurations

**Option A: SKR Pico (4x TMC2209)**
- **Cost**: ~$35 AUD
- **Drivers**: 4 integrated TMC2209 (no soldering required)
- **Use Case**: Supplement salvaged board in Tier 2 Multi-MCU setup
- **Pinout**: Well-documented for Klipper

**Option B: Modular TMC Sticks**
- **Hardware**: TMC2209 plug-in modules for boards like RAMPS
- **Cost**: ~$5-10 AUD per driver
- **Trade-off**: Requires wiring UART pins with jumper wires
- **Use Case**: Upgrading salvaged boards with soldered A4988 drivers

**Option C: Built-in TMC (Modern Boards)**
- **Hardware**: FYSETC Spider, BTT SKR 3, MKS SKIPR
- **Cost**: Included in board price
- **Use Case**: Tier 3 Reference Spec
- **Advantage**: Factory-wired UART, no jumper wires

### Endstop Wiring

**Mechanical Switches (X/Y/Z-max)**:
- **NO Contacts**: Normally Open (preferred, fail-safe)
- **NC Contacts**: Normally Closed (fails to safe state if wire breaks)
- **Wiring**:
  - One side to ground
  - Other side to endstop pin on mainboard
  - Pull-up resistor enabled in firmware (default)

**BLTouch**:
- **Pinout**:
  - Servo control (deploy/retract)
  - Z-min pin (probe trigger)
  - VCC (5V)
  - Ground
- **Mounting**: 3D-printed bracket to X-carriage or gantry
- **Alignment**: Nozzle tip level with BLTouch pin (offset in config)

## Consequences

### Benefits
- **Tier-1 Compatible**: Works with "dumb" drivers on salvaged boards
- **Tier-2 Optimized**: TMC2209 provides silent operation when budget allows
- **Absolute Reliability**: Mechanical switches have proven repeatability
- **Bed-Drop Protection**: Z-max switch prevents catastrophic crashes
- **Z-Tilt Enabled**: BLTouch provides three-point kinematic leveling

### Trade-offs
- **Sensorless Homing**: Not used (mechanical preferred for reliability)
- **Driver Cost**: TMC2209 adds $30-60 AUD vs "dumb" drivers (if not included with board)
- **Endstop Wires**: Physical switches require more wiring than sensorless
- **BLTouch Complexity**: Additional sensor to calibrate and maintain

### What This Enables
- **Tier 1**: Triple-Z on "dumb" drivers (mechanical switches required)
- **Tier 2**: Hybrid setups (TMC for X/Y/E, "dumb" for Z)
- **Tier 3**: All TMC2209 with full stealthchop/spreadcycle
- **All Tiers**: Z-tilt calibration via BLTouch
- **All Tiers**: Bed-drop safety via Z-max switch

### What This Replaces
- Sensorless homing on X/Y axes (unreliable for "Tractor" mass)
- Z-min physical endstop (BLTouch provides better precision)
- No Z-max protection (prevents bed-drop crashes)

## BOM Implications (Generic)

### Tier 1: Pure Scavenger (Dumb Drivers)
- **Parts needed**:
  - Salvaged board with A4988/DRV8825 drivers
  - 2x Mechanical endstops (X, Y)
  - 1x Z-max mechanical endstop
  - 1x BLTouch
- **Cost implication**: Very Low (~$15-25 AUD for endstops + BLTouch)
- **Driver features**: No silent mode, no sensorless homing, no stealthchop
- **Z-Leveling**: Manual (if belted-Z) or Z-tilt via BLTouch (if triple-Z)

### Tier 2: TMC2209 Upgrade
- **Parts needed**:
  - 4x TMC2209 drivers (or SKR Pico with 4 integrated)
  - 2x Mechanical endstops (X, Y)
  - 1x Z-max mechanical endstop
  - 1x BLTouch
- **Cost implication**: Low (~$50-70 AUD)
- **Driver features**: Silent mode, stealthchop/spreadcycle, current control
- **Compatibility**: Works with all tiers

### Tier 3: Reference Spec (Full TMC2209)
- **Parts needed**:
  - 6x TMC2209 drivers (included with MKS SKIPR)
  - 2x Mechanical endstops (X, Y)
  - 1x Z-max mechanical endstop
  - 1x BLTouch
- **Cost implication**: Low (~$20-30 AUD, drivers included with board)
- **Driver features**: All 6 axes with silent operation
- **Z-Leveling**: Automated Z-tilt via BLTouch

### Universal Requirements (All Tiers)
- **BLTouch**: Required for Z-tilt calibration
- **Mechanical Switches**: X and Y required (regardless of driver)
- **Z-Max Switch**: Strongly recommended for bed-drop protection
- **Wiring**: All endstops require proper grounding and pull-up configuration

## Implementation Notes

### Klipper TMC2209 Configuration
```ini
[tmc2209 stepper_x]
uart_pin: PC4
run_current: 0.600
stealthchop_threshold: 999999
diag_pin: ^PC5

[tmc2209 stepper_y]
uart_pin: PA10
run_current: 0.600
stealthchop_threshold: 999999
diag_pin: ^PA15
```

### Mechanical Endstop Configuration
```ini
[stepper_x]
endstop_pin: !PC2  # ! for NO contacts (active low)
position_endstop: 0
position_max: 250

[stepper_y]
endstop_pin: !PC0
position_endstop: 0
position_max: 250
```

### BLTouch Configuration
```ini
[bltouch]
sensor_pin: PB1
control_pin: PB0
x_offset: -10
y_offset: 20
z_offset: 1.6

[safe_z_home]
home_xy_position: 150,150
speed: 50
z_hop: 10
```

### Z-Tilt Configuration (Triple-Z)
```ini
[z_tilt]
z_positions:
  100,100
  100,300
  300,100
points: 3
horizontal_move_z: 5
retries: 3
```

### Z-Max Safety Configuration
```ini
[gcode_button z_max_safety]
pin: PA2
press_on_gcode:
  M112                    # Emergency stop
  TURN_OFF_HEATERS         # Turn off heaters
```

### Endstop Testing
1. **Mechanical Switches**:
   - Use `QUERY_ENDSTOPS` in Klipper console
   - Manually trigger switch
   - Verify open/closed state changes
   - Test wiring continuity with multimeter

2. **BLTouch**:
   - Use `BLTOUCH_DEBUG COMMAND=pin_down` to deploy pin
   - Use `BLTOUCH_DEBUG COMMAND=pin_up` to retract pin
   - Verify servo movement
   - Test probe trigger with multimeter

### Driver Current Calibration
```bash
# Connect multimeter to driver current test point (if available)
# Or use Klipper command:
SET_TMC_CURRENT STEPPER=run_current=0.600
# Repeat for each axis
```

### Driver Diagnostics
```bash
# Check driver status
DUMP_TMC STEPPER=stepper_x

# Check for errors
DRIVER_ERROR: stepper_x
```

### Safety Considerations
- **Endstop Wiring**: Use shielded cables to prevent EMI
- **BLTouch Mounting**: Ensure secure, no movement during prints
- **Z-Max Position**: Place at physical bottom limit, not operational limit
- **Current Settings**: Don't exceed motor/driver specifications
- **Heat Management**: TMC2209 drivers can overheat at high currents

## References
- **docs/reference/ai-conversations/mcu-drivers-endstops.md**: Complete driver and endstop discussion
- **docs/adr/012-mainboard-host-architecture.md**: Mainboard and host strategy
- **docs/adr/005-triple-z.md**: Triple-Z kinematic leveling
- **docs/adr/010-floating-z-puck.md**: Z-motor mounting
- Klipper TMC Driver Guide: [TMC Drivers](https://www.klipper3d.org/TMC_Drivers.html)
- Klipper BLTouch Guide: [Probe Bed Calibrate](https://www.klipper3d.org/Probe_Calibrate.html)
- Klipper Bed Leveling: [Bed Leveling](https://www.klipper3d.org/Bed_Leveling.html)

## Evolution Notes
This ADR establishes TMC2209 as the standard driver with mechanical endstops for reliability. Future driver technologies (e.g., TMC2240) will be evaluated against the "Tractor" criteria: proven reliability, cost-effectiveness, and compatibility with existing endstop strategy.
