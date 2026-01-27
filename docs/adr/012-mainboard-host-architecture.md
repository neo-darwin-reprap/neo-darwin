# ADR-012: Mainboard & Host Architecture

## Status
Accepted

## Context
The Neo-Darwin requires **7 stepper drivers** (X, Y1, Y2, E, Z1, Z2, Z3) for the dual-Y gantry and Triple-Z kinematic leveling. The heavy XY gantry (dual 8mm rods, see ADR-021) benefits from dual Y motors driving from both sides. In 2026, the 3D printing electronics ecosystem offers three distinct approaches:

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

### Tier 2: Multi-MCU Scavenger (Dual Board Triple-Z) ★ Recommended Scavenger Path
**Hardware**: Two salvaged 4-driver boards + external host

This is the **recommended path for dual-donor builds**. Two donor printers provide 8 stepper drivers total—more than enough for Neo-Darwin's 7 motors.

- **Configuration**:
  - Board A: X, Y1, Z1, E (4 drivers)
  - Board B: Y2, Z2, Z3, spare (4 drivers)
- **Connection**: Both boards via USB to single Klipper host
- **Host**: Old laptop (free), Pi Zero 2W ($25), or Pi 3B ($50)
- **Z-Leveling**: Automated Klipper Z-tilt
- **Cost**: ~$100-150 AUD (2× donors @ $50 + host)
- **Trade-off**: Higher wiring complexity, dual firmware flashing
- **Best For**: Maximum scavengeability, lowest total cost

**Why dual Y motors (Y1, Y2)?**
The XY gantry with dual 8mm rods (ADR-021) is heavier than single-rod designs. Driving from both sides eliminates racking forces and improves motion quality. Most donor printers have 4-5 motors, so two donors provide 8-10 motors—plenty for the 7 required.

**Single Y motor option**: If using a lighter gantry or limited motors, a single Y motor works but may exhibit slight racking at high accelerations. This reduces driver requirement to 6, allowing a single 6-driver board (MKS SKIPR) or leaving a spare on Tier 2 dual-board setup.

### Tier 3: Reference Spec (MKS SKIPR)
**Hardware**: MKS SKIPR all-in-one board
- **Integrated SOC**: Rockchip RK3328 (equivalent to Pi 3) built-in
- **Driver Capacity**: 7 driver slots (7 required, or 6 + 1 spare if single Y motor)
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
Host (Pi/Laptop) --USB--> Board A (X, Y1, Z1, E)
                    |
                    +---USB--> Board B (Y2, Z2, Z3)
```

**Driver Assignment**:
| Board | Driver 1 | Driver 2 | Driver 3 | Driver 4 |
|-------|----------|----------|----------|----------|
| A | X | Y1 | Z1 | E |
| B | Y2 | Z2 | Z3 | (spare) |

**printer.cfg Example**:
```ini
[mcu]  # Board A is default MCU
serial: /dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0

[mcu board_b]
serial: /dev/serial/by-id/usb-Klipper_stm32f103xe-if00

# X-axis on Board A
[stepper_x]
step_pin: PA2
dir_pin: PA3
enable_pin: !PA1

# Dual Y motors - one on each board
[stepper_y]
step_pin: PB6
dir_pin: PB7
enable_pin: !PB5

[stepper_y1]
step_pin: board_b:PA2
dir_pin: board_b:PA3
enable_pin: !board_b:PA1

# Triple-Z across both boards
[stepper_z]
step_pin: PC0
dir_pin: PC1
enable_pin: !PC2

[stepper_z1]
step_pin: board_b:PB6
dir_pin: board_b:PB7
enable_pin: !board_b:PB5

[stepper_z2]
step_pin: board_b:PC0
dir_pin: board_b:PC1
enable_pin: !board_b:PC2
```

**Constraints**:
- Y1/Y2 should be configured as a single axis with `[stepper_y1]` mirroring `[stepper_y]`
- Z-tilt works across MCUs (Klipper handles timing)
- Use non-blocking (MTT) USB hubs for 4+ MCUs
- Each board requires separate firmware flash
- Identify unique serial IDs in `/dev/serial/by-id/`

## Second-Hand Market Economics (2026)

### Donor Printer Pricing

The second-hand market for entry-level 3D printers is expected to bottom out around **$50 AUD** per unit by end of 2026. Key factors:

- **Market saturation**: Millions of Ender 3, Anet A8, and i3 clones sold 2017-2024
- **New competition**: Sub-$200 printers (Ender 3 V3, Bambu A1 Mini) make older stock undesirable
- **Perception shift**: Sellers increasingly recognize true market value
- **Patience pays**: Avoid $150+ listings; wait for motivated sellers or post "wanted" ads

**Recommended donor sources:**
- Facebook Marketplace "broken 3D printer" listings
- Gumtree/Craigslist lot sales
- Makerspace clearouts
- University/school surplus

### Real-World Parts Pricing (AliExpress, 2026)

For V-slot donor builds (Ender 3) requiring purchased rods:

| Item | Quantity | Cost (AUD) | Source |
|------|----------|------------|--------|
| Stainless steel 8mm rods | 8× 400mm | $43 | AliExpress |
| IGUS RJ4JP-01-08 bushings | 22× | $30 | AliExpress |
| **Total motion system** | | **$73** | |

This validates the ADR-022 estimate of $70-90 for rod + bushing replacement when donors lack smooth rods.

### Cost Comparison by Path

| Build Path | Donor Cost | Motion Gap | Electronics | Total |
|------------|------------|------------|-------------|-------|
| 2× Anet A8 (rod-bearing) | $100 | $0 | $0 (Tier 2) | **$100** |
| 2× Ender 3 (V-slot) | $100 | $73 | $0 (Tier 2) | **$173** |
| 2× Ender 3 + MKS SKIPR | $100 | $73 | $85 | **$258** |

Add ~$100 for frame materials (M10 rod, MDF, hardware) to get total build cost.

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

### Tier 2: Multi-MCU Scavenger (Dual Board) ★ Recommended
- **Parts needed**:
  - 2× Salvaged 4-driver boards (8 drivers total, need 7)
  - 1× Host (laptop free, Pi Zero 2W $25, or Pi 3B $50)
  - 2× USB cables (host to boards)
  - 7× Motors (X, Y1, Y2, Z1, Z2, Z3, E)
- **Cost implication**: Lowest (~$100-175 AUD for donors + host)
- **Donor compatibility**: Any 4-driver boards (Creality, Anet, etc.)
- **Z-Leveling**: Automated (Klipper Z-tilt)
- **Complexity**: Medium (dual firmware, but well-documented)

### Tier 3: Reference Spec (MKS SKIPR)
- **Parts needed**:
  - 1× MKS SKIPR board (7 driver slots)
  - 7× TMC2209 drivers (sometimes included in bundle)
  - 7× Motors (X, Y1, Y2, Z1, Z2, Z3, E)
  - 1× SD card (for OS, eMMC optional)
  - 1× USB cable (only for firmware flash)
  - 0× External host (integrated)
- **Cost implication**: Low (~$85-100 AUD for board)
- **Donor compatibility**: Motors from donors, board purchased new
- **Z-Leveling**: Automated (Klipper Z-tilt)
- **Complexity**: Low (single board, single firmware)

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
- **ADR-021**: Dual-Rod Motion System (defines dual-Y gantry requirement)
- **ADR-022**: Linear Bearing Selection (rod material for V-slot donor builds)
- **ADR-005**: Triple-Z Kinematic Leveling
- **ADR-013**: TMC driver and endstop architecture
- **docs/reference/ai-conversations/mainboard.md**: Complete mainboard discussion
- **docs/reference/ai-conversations/mcu-drivers-endstops.md**: Driver and endstop strategy
- MKS SKIPR Documentation: [Makerbase Official](https://github.com/makerbase-mks/MKS-SKIPR)
- Klipper Multi-MCU: [Klipper Documentation](https://www.klipper3d.org/Multi_MCU_sample.html)

## Evolution Notes
This ADR establishes the three-tier architecture. As new boards emerge (e.g., MKS SKIPR successors), they will be evaluated against the Reference Spec criteria: 6+ drivers, integrated host, CAN bus support, and <$100 AUD target cost.
