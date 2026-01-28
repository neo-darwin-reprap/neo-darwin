# 📋 Master Parts List (MPL) - Amalgam M12 Box Frame

**Project Context:**
- **Frame Type:** M12 Box Frame
- **Extruder Setup:** Wade Extruder + BLTouch
- **Motion System:** Z-bed gantry and X-gantry
- **Configuration:** Triple-Z (Reference Spec / Tier 3)

---

## Frame/Structural (Bottom Frame)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Corner 1: Front-Left + Z1** | 1 | Corner bracket with integrated NEMA17 Z1 motor mount, 4× M12 rod clamps, jam nut access holes |
| **Corner 2: Front-Right + Z2** | 1 | Corner bracket with integrated NEMA17 Z2 motor mount, 4× M12 rod clamps, jam nut access holes |
| **Corner 3: Back-Left** | 1 | Standard corner bracket (no Z-motor), 4× M12 rod clamps, jam nut access holes |
| **Corner 4: Back-Right** | 1 | Standard corner bracket (no Z-motor), 4× M12 rod clamps, jam nut access holes |
| **Z-Puck: Z3 Mount** | 1 | Slide-on clamp for back horizontal rod with integrated Z3 NEMA17 motor mount, leadscrew clearance |

---

## Frame/Structural (Top Frame/Gantry)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Top Corner TL** | 1 | Top-Left standard corner bracket, 4× M12 rod clamps |
| **Top Corner TR** | 1 | Top-Right standard corner bracket, 4× M12 rod clamps |
| **Top Corner BL** | 1 | Bottom-Left standard corner bracket, 4× M12 rod clamps |
| **Top Corner BR** | 1 | Bottom-Right standard corner bracket, 4× M12 rod clamps |

---

## X-Axis Components

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **X-Carriage** | 1 | Main carriage plate with 2× LM10UU (or LM8UU) bearing housings at 24mm spacing, universal toolhead puck mount pattern |
| **X-Carriage: Toolhead Puck** | 1 | Universal mounting plate (30×30mm pattern) for Wade extruder/swappable toolheads |
| **X-Motor Mount** | 1 | M12-to-NEMA17 motor mount, holds X-motor with GT2 pulley, clamps to X-axis smooth rods |
| **X-End Idler** | 1 | Opposite end of X-axis, holds GT2 idler pulley with belt tensioning slot |
| **X-Axis Belt Tensioner** | 1 | Screw-drive tensioner integrated into idler (adjusts GT2 belt tension) |

---

## Y-Axis Components

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Y-Motor Mount (Left)** | 1 | M12-to-NEMA17 motor mount at back-left corner, clamps to Y-axis horizontal rod |
| **Y-Motor Mount (Right)** | 1 | M12-to-NEMA17 motor mount at back-right corner, clamps to Y-axis horizontal rod |
| **Y-Axis Rod Clamps** | 2× | Clamps to attach Y-axis smooth rods to front horizontal M12 rods |
| **Y-Idler Pulley Mount** | 1 | Idler for Y-belt return path (if dual-belt system used) |

---

## Z-Bed Gantry (Triple-Z System)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Spider Hub** | 1 | Central bed support hub, high-density printed block with dovetail slots |
| **Spider Arm** | 3 | Identical struts (125mm long) that slot into hub, bolt to bed mount points |
| **Spider Stiffening Cap** | 1 | Optional flat triangular plate that sandwiches hub+arms for rigidity |
| **Lead Screw Nut Housing** | 3 | Integrated into corners/Z-puck, holds T8 brass nuts for lead screws |

---

## Extruder/Hotend (Greg's Wade)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Wade Extruder: Large Gear** | 1 | 43-tooth printed gear, drives M8 hobbed bolt (5.22:1 ratio) |
| **Wade Extruder: Small Gear** | 1 | 13-tooth pinion gear, mounts to NEMA17 motor shaft |
| **Wade Extruder: Body** | 1 | Main body housing gears and 608 bearings, hinged idler arm |
| **Wade Extruder: Idler Arm** | 1 | Hinged idler arm with tension spring, holds 608 idler bearing against hobbed bolt |

---

## Toolhead Sensors & Mounts

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **BLTouch/PINDA Mount** | 1 | Wing extending from carriage, holds probe ~45mm from nozzle, pinch slot for secure fit |
| **Filament Sensor Cage** | 1 | Skeletonized cage housing V-15-1C25 microswitch, clips to Wade extruder top |
| **Filament Guide Tube** | 1 | 2mm path through sensor cage, ensures filament accuracy |
| **ADXL345 Mount** | 1 | Temporary mount on carriage for Input Shaping calibration (can be removed after calibration) |

---

## Electronics/Mounting

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Brain/Electronics Puck** | 1 | Mounting plate for MKS SKIPR or donor board, clamps to back M12 rods |
| **MKS SKIPR Mount** | 1 | Specific bracket for SKIPR board (if SKIPR used) |
| **Donor Board Puck** | 1 | Alternative mount for Creality 4.2.2, Anet V1.0, or Trigorilla boards |
| **Endstop Mount (X)** | 1 | Mount for X-axis mechanical/optical endstop switch |
| **Endstop Mount (Y)** | 1 | Mount for Y-axis mechanical/optical endstop switch |

---

## Cable Management

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Cable Chain Clip (Frame)** | 4× | Clips to secure cable chain to vertical M12 rods |
| **Cable Chain Clip (Gantry)** | 2× | Clips to secure cable chain to horizontal rods |
| **Wire Guide Clips** | 6× | Small clips to organize wiring harness along frame |
| **Umbilical Sleeve Mount** | 1 | Guide for main wiring loom from carriage to frame |

---

## Motion System (Optional Variants)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Smooth Rod Clamp (8mm)** | 8× | Clamps for 8mm smooth rods (if using salvaged rods) |
| **Smooth Rod Clamp (10mm)** | 8× | Clamps for 10mm smooth rods (Neo Standard) |
| **Rail-Puck (MGN12H)** | 8× | Alternative clamp for MGN12H linear rails (Tinker path) |
| **Bearing Housing Cover** | 4× | Snap-on covers for LM10UU/LM8UU bearings (protection) |

---

## Multi-Color Expansion (ERCF Optional)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Reverse Bowden Guide** | 1 | Bracket to guide filament tube from frame to toolhead |
| **ERCF Mount** | 1 | Wall-mount puck for standalone ERCF v2 unit |
| **Filametrix Cutter Mount** | 1 | Mount for mechanical filament cutter on toolhead |

---

## Alternative Toolheads (Optional)

| Part Name | Qty | Description/Function |
|-----------|-----|-------------------|
| **Pen Plotter Puck** | 1 | Simple spring-loaded holder for Sharpie/drawing pen |
| **Laser Engraver Puck** | 1 | Mount for 5W-10W diode laser module |
| **Drag Knife Puck** | 1 | Mount for vinyl/sticker cutting tool |

---

## Configuration Notes

### Total Printed Parts Count
- **Reference Spec (Triple-Z):** ~45-55 parts
- **Belted-Z (Tier 1):** ~40-45 parts (reduce corners to 2× Z-mount + 2× standard, remove Z-puck)
- **Tinker Path (Linear Rails):** Replace rod clamps with rail-pucks (same count)

### Tier-Specific Adjustments
| Tier | Z-System | Corner Configuration | Changes to MPL |
|------|----------|---------------------|----------------|
| Tier 1 (Belted-Z) | Single motor with belt sync | 2× Z-mount corners + 2× standard | Remove Z-puck, reduce Spider to 4-arm symmetric, remove 1× Z-motor mount |
| Tier 3 (Triple-Z) | 3 independent motors | 3× Z-mount corners + 1× standard + Z-puck | As shown above |
| Tinker (Linear Rails) | Either system | Same corners | Replace smooth rod clamps (8×) with rail-pucks (8×) |

### Build Volume Variants
- **220mm³ Build:** Standard dimensions as listed
- **250mm³ Build:** Spider arm length increases to ~135mm
- **300mm³ Build:** Spider arm length increases to ~160mm, may require larger hub

### Motion System Variants
- **Path A (Scavenger):** 8mm smooth rods + LM8UU bearings
- **Path B (Neo Standard):** 10mm smooth rods + LM10UU bearings
- **Path C (Tinker):** MGN12H linear rails + rail-pucks

---

## Parts Not Yet Designed

As of CAD-FILE-ORG.md, the following parts are **planned but not yet implemented:**

### Motion System
- [ ] X-Carriage with bearing housings (24mm spacing)
- [ ] X-Motor Mount (M12-to-NEMA17)
- [ ] X-End Idler with tensioning
- [ ] Y-Motor Mounts (Left & Right)
- [ ] Y-Axis Rod Clamps
- [ ] Y-Idler Pulley Mount

### Bed Support
- [ ] Spider Hub (central bed support)
- [ ] Spider Arms (3× interlocking struts)
- [ ] Spider Stiffening Cap

### Extruder/Toolhead
- [ ] X-Carriage: Universal Toolhead Puck
- [ ] Wade Extruder Gears (Large 43T + Small 13T)
- [ ] Wade Extruder Body (with hinged idler)
- [ ] Wade Extruder Idler Arm
- [ ] BLTouch/PINDA Probe Mount (wing)
- [ ] Filament Sensor Cage (microswitch housing)
- [ ] ADXL345 Calibration Mount

### Electronics/Mounting
- [ ] Brain/Electronics Puck (MKS SKIPR or donor board)
- [ ] MKS SKIPR Mount (specific bracket)
- [ ] Donor Board Puck (Creality/Anet/Trigorilla)
- [ ] Endstop Mounts (X and Y axes)

### Cable Management
- [ ] Cable Chain Clips (Frame & Gantry)
- [ ] Wire Guide Clips
- [ ] Umbilical Sleeve Mount

### Optional/Expansion
- [ ] Reverse Bowden Guide (ERCF)
- [ ] ERCF Mount (wall puck)
- [ ] Filametrix Cutter Mount
- [ ] Pen Plotter Puck
- [ ] Laser Engraver Puck
- [ ] Drag Knife Puck
- [ ] Smooth Rod Clamps (8mm variant)
- [ ] Smooth Rod Clamps (10mm variant)
- [ ] Rail-Pucks (MGN12H variant)
- [ ] Bearing Housing Covers

---

## Design Progress Summary

**Complete:** 2/9 frame parts (22%)
- [x] Corner Standard
- [x] Corner Front-Left (Z1 integrated)

**Pending:** 7/9 frame parts (78%)
- [ ] Corner Front-Right (Z2 integrated)
- [ ] Corner Back-Left (standard)
- [ ] Corner Back-Right (standard)
- [ ] Z-Puck (Z3, back center horizontal rod)
- [ ] Top Corner TL
- [ ] Top Corner TR
- [ ] Top Corner BL
- [ ] Top Corner BR

**Overall Progress:** ~4% of total parts (2/50+ designed)
