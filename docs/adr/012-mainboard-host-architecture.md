# ADR-012: Mainboard & Host Architecture

## Status
Accepted

## Context
The Neo-Darwin requires **6 stepper drivers** (X, Y, Extruder, and 3xZ for triple-Z kinematic leveling). In 2026, the 3D printing electronics ecosystem offers three distinct approaches:

1. **Salvaged Legacy Boards**: 4-driver boards from donor printers (Ender 3, Anet A8, i3 Mega)
2. **Modular Modern Boards**: 5-8 driver boards requiring separate host (FYSETC Spider, BTT SKR 3)
3. **Integrated All-in-One Boards**: Boards with built-in Linux host (MKS SKIPR, BTT Manta M8P)

Each path has trade-offs in cost, complexity, and reliability. The decision impacts:
- BOM cost ($0 - $100+ AUD)
- Wiring complexity (USB cabling, power supplies)
- Future expandability (ERCF, multi-color, toolhead modules)
- Maintenance (single vs multiple boards to debug)

## Decision
We adopt a **three-tier architecture** with the **MKS SKIPR** as the Tier 3 Reference Spec mainboard.

### Tier 1: Pure Scavenger (Belted-Z)
**Hardware**: Single salvaged 4-driver board + external host
- **The Hack**: Single Z-motor drives all three lead screws via closed-loop belt
- **Z-Leveling**: Manual leveling once with spacers (no Z-tilt)
- **Host**: Pi Zero 2W or old laptop
- **Cost**: ~$80 AUD total
- **Trade-off**: No automated Z-tilt, belt-driven Z synchronization
- **Best For**: Emergency builds, absolute minimum cost

### Tier 2: Multi-MCU Scavenger (Dual Board Triple-Z)
**Hardware**: Two salvaged 4-driver boards + external host
- **Configuration**:
  - Board A: X, Y, Extruder
  - Board B: 3xZ motors (even with a dead driver slot)
- **Connection**: Both boards via USB to single Klipper host
- **Host**: Pi Zero 2W, Pi 3B, or laptop
- **Z-Leveling**: Automated Klipper Z-tilt (all Z-motors on Board B)
- **Cost**: ~$205 AUD (includes Pi)
- **Trade-off**: Higher wiring complexity, dual firmware flashing
- **Best For**: Repurposing "broken" hardware for premium features

### Tier 3: Reference Spec (MKS SKIPR) ★
**Hardware**: MKS SKIPR all-in-one board
- **Integrated SOC**: Rockchip RK3328 (equivalent to Pi 3) built-in
- **Driver Capacity**: 7 driver slots (6 required + 1 spare for ERCF)
- **Storage**: 8GB/16GB eMMC onboard
- **CAN Bus**: Native port for toolhead modules (MKS THR36/42)
- **Z-Leveling**: Automated Klipper Z-tilt on single MCU
- **Cost**: ~$85 AUD
- **Trade-off**: Cannot upgrade SOC (fixed to RK3328)
- **Best For**: Reference Spec build, maximum reliability

### Why MKS SKIPR (Reference Spec)?

**1. Cost-Performance Ratio**
- $85 AUD vs ~$130+ AUD for BTT Manta M8P + CB1 module
- Includes integrated host (no separate Pi to buy)
- 7 drivers covers all requirements with spare slot

**2. Simplicity**
- One board, one power supply, zero external USB data cables
- Single firmware flash
- Reduces wiring complexity (common failure point in DIY builds)

**3. CAN Bus Synergy**
- Native CAN port compatible with toolhead modules
- Future-proof for ERCF v2, toolhead sensors
- Eliminates need for separate CAN adapters

**4. Driver Density**
- Perfect "6+1" count: Triple-Z + X/Y/E + ERCF spare
- All Z-tilt motors on single MCU timing domain (no sync issues)

### Alternative: BTT Manta M8P V2.0
Considered but rejected for Reference Spec due to:
- Higher total cost (~$130+ AUD with CB1 module)
- Modular complexity (board + separate compute module)
- Overkill for "Tractor" speed envelope (STM32H723 @ 550MHz)

Useful for:
- Builders with existing CB1/CM4 modules
- Voron-style "Racecar" builds requiring 48V support
- Future high-voltage upgrades (beyond Neo-Darwin scope)

### Host Performance Comparison

| Host Option | RAM | Best For | Trade-offs |
|-------------|-----|----------|------------|
| **Pi Zero 2W** | 512MB | Tier 1/2 Builds | UI lag; struggles with high-res webcams |
| **MKS SKIPR SOC** | 1GB | **Reference Spec** | Cleanest integration; built-in eMMC |
| **Pi 3B / 4B** | 1GB+ | Pro/Tinker Build | Snappy UI; handles KlipperScreen, 1080p cameras |

### Multi-MCU Configuration (Tier 2)
Klipper excels at controlling multiple MCUs as a single machine:

**Setup**:
```
Host (Pi) --USB--> Board A (X, Y, E)
    |
    +---USB--> Board B (3xZ)
```

**printer.cfg Example**:
```ini
[mcu board_a]
serial: /dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0

[mcu board_b]
serial: /dev/serial/by-id/usb-Klipper_stm32f103xe-if00

[stepper_x]
step_pin: board_a:PA2
...

[stepper_z]
step_pin: board_b:PC3
...
```

**Constraints**:
- Keep all axes moving together on same MCU (Z-tilt on Board B)
- Use non-blocking (MTT) USB hubs for 4+ MCUs
- Each board requires separate firmware flash
- Identify unique serial IDs in `/dev/serial/by-id/`

## Consequences

### Benefits
- **Tiered Flexibility**: Path exists for $0 salvage builds to $85 Reference Spec
- **Klipper-Native**: All paths use Klipper (no vendor lock-in)
- **Scalable**: Tier 1 can upgrade to Tier 3 without redesigning mechanics
- **Future-Proof**: Reference Spec has CAN bus and spare driver for expansions
- **Reliability**: Single-board Reference Spec eliminates USB failure points

### Trade-offs
- **Tier 1**: No automated Z-tilt, belt complexity
- **Tier 2**: Higher wiring complexity, dual firmware management
- **Tier 3**: Fixed SOC (RK3328), cannot upgrade host separately

### What This Enables
- **Tier 1**: Emergency builds from any 4-driver donor
- **Tier 2**: Premium features (Z-tilt) from broken hardware
- **Tier 3**: Industrial-grade single-board solution
- **All Paths**: Klipper Z-tilt, Input Shaping, Pressure Advance

### What This Replaces
- Discrete Raspberry Pi + separate mainboard (except Tier 2 multi-MCU)
- RAMPS + Arduino combos (obsolete, more expensive than SKR Pico)
- "Dumb" 8-bit MCUs without Klipper support

## BOM Implications (Generic)

### Tier 1: Pure Scavenger (Belted-Z)
- **Parts needed**:
  - 1x Salvaged 4-driver mainboard
  - 1x Host (Pi Zero 2W or laptop)
  - 1x Z-motor (reuses existing)
  - 2x Pulleys + belt (for belted Z)
  - 3x Belt tensioners
- **Cost implication**: Very Low (~$0-30 AUD)
- **Donor compatibility**: Any 4-driver donor board
- **Z-Leveling**: Manual (no Z-tilt)
- **Warning**: No future upgrade path to triple-Z without replacing belt system

### Tier 2: Multi-MCU Scavenger (Dual Board)
- **Parts needed**:
  - 2x Salvaged 4-driver boards
  - 1x Host (Pi Zero 2W or Pi 3B)
  - 2x USB cables (host to boards)
  - 3x Z-motors (triple-Z)
- **Cost implication**: Low (~$50-205 AUD depending on Pi)
- **Donor compatibility**: Any 4-driver boards
- **Z-Leveling**: Automated (Klipper Z-tilt)
- **Complexity**: High (dual firmware, wiring)

### Tier 3: Reference Spec (MKS SKIPR)
- **Parts needed**:
  - 1x MKS SKIPR board
  - 6x TMC2209 drivers (sometimes included in bundle)
  - 3x Z-motors (triple-Z)
  - 1x SD card (for OS, eMMC optional)
  - 1x USB cable (only for firmware flash)
  - 0x External host (integrated)
- **Cost implication**: Low (~$85-100 AUD)
- **Donor compatibility**: None (new board required)
- **Z-Leveling**: Automated (Klipper Z-tilt)
- **Complexity**: Low (single board)

### Tier 3 Alternative: BTT Manta M8P
- **Parts needed**:
  - 1x BTT Manta M8P V2.0
  - 1x CB1 or CM4 module
  - 6x TMC2209 drivers
  - 1x eMMC or SD card for module
- **Cost implication**: Medium (~$130+ AUD)
- **Donor compatibility**: None (new board required)
- **Z-Leveling**: Automated (Klipper Z-tilt)
- **Advantages**: Upgradable host, higher-voltage support

### Universal Requirements (All Tiers)
- **PSU**: 12V or 24V power supply (sufficient current for 6 motors + heater + bed)
- **Firmware**: Klipper compiled for target MCU(s)
- **Cabling**: Motor wiring, thermistor wiring, endstop wiring

## Implementation Notes

### MKS SKIPR Setup (Tier 3)

**Flashing Klipper**:
```bash
# SSH into SKIPR via network or USB
git clone https://github.com/Klipper3d/klipper.git
cd klipper
make menuconfig  # Select STM32F407, 16KB bootloader, USB CDC
make
sudo cp out/klipper.bin /boot/firmware
sudo reboot
```

**pinout Configuration**:
- Follow MKS SKIPR Klipper documentation
- 6 stepper drivers for: X, Y, E, Z1, Z2, Z3
- Spare driver slot for ERCF or additional axis

**Z-Tilt Config**:
```ini
[z_tilt]
z_positions: 100,100 100,300 300,100
points: 3
horizontal_move_z: 5
retries: 3

[stepper_z1]
step_pin: PB13
dir_pin: PB12
enable_pin: !PA8
...
```

### Multi-MCU Setup (Tier 2)

**Identifying Board Serial IDs**:
```bash
ls -l /dev/serial/by-id/
# Output shows unique IDs for each board
```

**Configuring Dual MCUs**:
- Use `[mcu]` section for each board
- Tag pins with `board_name:pin_name` syntax
- Keep all Z-motors on same board for Z-tilt sync

### Performance Optimization

**Pi Zero 2W**:
- Increase swapfile to 1024MB (prevents crashes)
- Consider ZRAM for compressed swap
- Disable webcam during high-load operations (resonance testing)

**MKS SKIPR**:
- Use eMMC for faster OS (if available)
- Klipper host runs on RK3328 (1GB RAM)
- Webcam support good for 720p, may struggle with 1080p

### Safety Considerations
- **USB Cables**: Use shielded cables for MCU communication
- **Power**: Ensure PSU has sufficient current for all motors + hotend + bed
- **Firmware**: Always test on test bench before full assembly
- **Backup**: Keep config backups, especially for multi-MCU setups

## References
- **docs/reference/ai-conversations/mainboard.md**: Complete mainboard discussion
- **docs/reference/ai-conversations/mcu-drivers-endstops.md**: Driver and endstop strategy
- **docs/adr/013-drivers-endstops.md**: TMC driver and endstop architecture
- **docs/adr/005-triple-z.md**: Triple-Z kinematic leveling
- MKS SKIPR Documentation: [Makerbase Official](https://github.com/makerbase-mks/MKS-SKIPR)
- Klipper Multi-MCU: [Klipper Documentation](https://www.klipper3d.org/Multi_MCU_sample.html)

## Evolution Notes
This ADR establishes the three-tier architecture. As new boards emerge (e.g., MKS SKIPR successors), they will be evaluated against the Reference Spec criteria: 6+ drivers, integrated host, CAN bus support, and <$100 AUD target cost.
