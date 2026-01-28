# ADR-007: CAN Bus Architecture

## Status
Accepted

## Context
The Amalgam has multiple electrical components that need to communicate:
- Main board (motion control)
- Toolhead (extruder, hotend, fan)
- Z-probe (BLTouch/PINDA)
- Future expansions (ERCF, toolhead boards, bed heater, etc.)

In 2026, there are two main communication architectures:
- **Traditional wiring**: Every component wired directly to main board with individual cables
- **CAN bus**: Network-based communication with shared twisted-pair wiring

Traditional 3D printers use direct wiring, but high-end systems (Voron 2.4, toolhead boards) use CAN bus for reduced wiring and improved reliability.

## Decision
We choose **CAN bus support as an optional upgrade path** for Amalgam, with traditional wiring as the baseline.

### Architecture Options
1. **Tier 1-2: Traditional Wiring** (Baseline)
   - All stepper motors wired to main board
   - Toolhead components wired with multicore cable
   - BLTouch wired directly to board
   - Simple, proven, works with all boards

2. **Tier 3-4: CAN Bus** (Optional Upgrade)
   - CAN-connected toolhead board (e.g., BTT EBB36)
   - CAN bus for expansions (ERCF, bed heaters, etc.)
   - Reduced wiring (4 wires: VCC, GND, CAN-H, CAN-L)
   - Requires CAN-capable main board

### Why Optional CAN Bus?
1. **Wiring reduction**: 20+ wires reduced to 4 for toolhead
2. **Noise immunity**: Differential signaling is electrically robust
3. **Expandability**: Easy to add CAN-connected devices
4. **Modern standard**: Used in Voron, RatRig, high-end systems
5. **Future-proof**: Supports toolhead boards, smart peripherals

## Consequences

### Benefits (CAN Bus)
- **Reduced cable clutter**: 4 wires vs 20+ for toolhead
- **Improved reliability**: Fewer connections = fewer failure points
- **Noise resistance**: CAN bus immune to EMI from steppers
- **Flexible mounting**: CAN nodes can be placed anywhere
- **Daisy-chain**: Multiple devices on single bus
- **Hot-swappable**: Some CAN boards support hot-plug

### Trade-offs (CAN Bus)
- **Cost**: Additional CAN board(s) ~$30-50 AUD
- **Complexity**: Requires CAN-capable main board
- **Configuration**: More complex Klipper setup
- **Debugging**: Hardware issues harder to diagnose
- **Compatibility**: Not all boards support CAN

### Benefits (Traditional Wiring - Baseline)
- **Simple**: Works with all boards, no special hardware
- **Proven**: Decades of community knowledge
- **Cheap**: No extra boards required
- **Easy debugging**: Each wire individually testable
- **Universal**: Works with any board/donor

### Trade-offs (Traditional Wiring)
- **Cable clutter**: Wiring looms can be messy
- **More connections**: More potential failure points
- **EMI sensitive**: Long cable runs susceptible to noise
- **Fixed architecture**: Adding devices requires running new cables

## BOM Implications (Generic)

### Scenario A: Traditional Wiring (Recommended for Tier 1-2)
- **Parts needed**:
  - Main board (MKS SKIPR, BTT SKR 3, etc.)
  - Standard stepper motor cables (4-pin)
  - Multicore toolhead cable (4-6 conductors)
  - BLTouch cable (3-5 pin)
  - Hotend cable (heater, thermistor, fan)
- **Cost implication**: Included in main board price
- **Donor compatibility**: All donors
- **Board requirement**: Any board with 6+ drivers
- **Experience**: Simple, proven setup

### Scenario B: CAN Toolhead Only (Tier 3)
- **Parts needed**:
  - Main board with CAN support (MKS SKIPR, BTT SKR 3, BTT Octopus)
  - CAN toolhead board (BTT EBB36, EBB42)
  - CAN bus cable (twisted pair, 4 wires)
  - 24V power for toolhead board
  - Reduced toolhead cabling (just 4 CAN + 24V)
- **Cost implication**: Medium (+$35-50 AUD for EBB36)
- **Donor compatibility**: All donors (board upgrade)
- **Board requirement**: MUST have CAN port
- **Benefits**: Cleaner toolhead wiring, noise immunity

### Scenario C: Full CAN System (Tier 4)
- **Parts needed**:
  - Main board with CAN support
  - CAN toolhead board (BTT EBB36/EBB42)
  - CAN ERCF controller (Happy Hare CAN)
  - CAN bed heater controller
  - Multiple CAN bus segments (terminators as needed)
  - CAN bus cables throughout
- **Cost implication**: High (+$100-150 AUD for all CAN boards)
- **Donor compatibility**: All donors (board upgrade)
- **Board requirement**: Multiple CAN ports or CAN hub
- **Benefits**: Minimal wiring, highly modular, future-proof

### Scenario D: Hybrid CAN (Recommended Path)
- **Parts needed**:
  - Main board with CAN support (MKS SKIPR)
  - CAN toolhead board (future upgrade)
  - Traditional wiring for now
  - Upgrade toolhead to CAN later
- **Cost implication**: Medium (buy CAN-capable board, add EBB36 later)
- **Donor compatibility**: All donors
- **Board requirement**: CAN-capable board
- **Experience**: Traditional start, upgrade to CAN as needed

### Scenario E: Legacy Board (Tier 1)
- **Parts needed**:
  - Salvaged board (Creality 4.2.2, Anet, etc.)
  - All traditional wiring
- **Cost implication**: Very Low ($0)
- **Donor compatibility**: Use donor board
- **Board requirement**: Legacy board (no CAN)
- **Limitation**: Cannot upgrade to CAN without board replacement

## Implementation Notes

### CAN Bus Topology
```
Main Board (CAN Controller)
  |
  +-- CAN Termination (120Ω)
  |
  +-- Toolhead CAN Board (EBB36)
  |
  +-- CAN Hub (if needed)
        |
        +-- ERCF CAN Controller
        +-- Bed Heater CAN Board
        +-- Other CAN peripherals
  |
  +-- CAN Termination (120Ω)
```

### MKS SKIPR CAN Support
```
Native CAN Port: Yes
CAN Protocol:  CAN FD (backward compatible with CAN 2.0)
Max Nodes:     64 (theoretical)
Recommended:   Start with 1-3 nodes
```

### CAN Cable Requirements
```
Type:           Twisted pair (CAN-H and CAN-L)
Shielding:      Optional but recommended (EMI)
Termination:    120Ω resistor at each end
Length:         Up to 40m (NEO-DARWIN: < 2m typical)
Wire gauge:     22-24 AWG
```

### CAN Toolhead Board (EBB36 Example)
```
Drivers:        2x TMC2209 (for dual gear or direct drive)
Sensors:        Thermistor, ADXL345 (onboard)
Outputs:        Heater, Fan, Part fan
Inputs:         BLTouch, Probe
Power:          24V (5V generated onboard)
Communication:  CAN bus
Size:           36mm × 36mm
```

### Traditional vs CAN Wiring Comparison
```
Traditional Toolhead Wiring:
- Extruder motor:  4 wires
- Hotend heater:   2 wires
- Hotend therm:    2 wires
- Part fan:        2 wires
- Hotend fan:      2 wires
- BLTouch:         3-5 wires
- Total:           15-17 wires + bulky cable management

CAN Toolhead Wiring:
- CAN bus:        4 wires (VCC, GND, CAN-H, CAN-L)
- 24V power:      2 wires (from main PSU)
- Total:          6 wires (clean loom)
```

### Board CAN Compatibility
```
MKS SKIPR:     ✓ Native CAN (recommended)
BTT SKR 3:     ✓ Native CAN
BTT Octopus:   ✓ Native CAN
Creality 4.x:  ✗ No CAN
Anet A8:       ✗ No CAN
Prusa boards:  ✗ No CAN (proprietary)
```

### Klipper CAN Configuration
```
# MCU config for CAN-connected toolhead
[mcu canbus]
canbus_uuid: [UUID from EBB36]

# Extruder on CAN toolhead
[extruder]
step_pin: canbus_gpio:26
dir_pin: canbus_gpio:22
enable_pin: !canbus_gpio:10
...
```

### CAN UUID Discovery
```bash
# On MKS SKIPR or Pi host
~/klippy-env/bin/python -m klippy.canbus_query
# Press BOOT button on CAN board to get UUID
```

### CAN Bus Health Monitoring
```
Klipper command: CAN_BUS_STATUS

Monitors:
- Bus errors
- Node status
- Message rates
- Error counters

Normal: < 10 errors/hour
High:   > 100 errors/hour (check terminators, noise)
```

### Termination
```
Required: 120Ω resistor at BOTH ends of CAN bus
- One on main board
- One on furthest node
- Remove terminators from middle nodes

Diagnostic: Measure resistance between CAN-H and CAN-L
- With power off: 60Ω (two 120Ω in parallel)
- With terminators: Correct
- Without terminators: Open circuit
```

### Recommended Path for Amalgam
```
Tier 1-2:
  - Use traditional wiring
  - Save money
  - Focus on frame mechanics first

Tier 3 (MKS SKIPR):
  - Buy CAN-capable board
  - Start with traditional wiring
  - Plan for CAN toolhead upgrade

Tier 4:
  - Full CAN system from start
  - Toolhead CAN board
  - Clean wiring loom
  - Future ERCF CAN integration
```

### Common CAN Issues
- **No communication**: Check terminators, verify 24V power, check UUID
- **High error rate**: Check for loose connections, add shielding, reduce cable length
- **Node not detected**: Press BOOT button to get UUID, check canbus_uuid in config
- **Intermittent faults**: Add CAN bus shield, separate from stepper cables

## References
- [BTT EBB36 Documentation](https://github.com/bigtreetech/EBB/tree/master/EBB36%20V1.2)
- [Klipper CAN Bus Guide](https://www.klipper3d.org/CANbus.html)
- [Voron 2.4 CAN Bus Setup](https://docs.vorondesign.com/build/electronics/canbus.html)
- docs/AI-Conversations/ [Relevant conversations about CAN bus architecture]
