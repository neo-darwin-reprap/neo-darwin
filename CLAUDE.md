# Neo-Darwin AI Context

This file provides context for AI assistants working on the Neo-Darwin project.

## What This Project Is

Neo-Darwin is a **2026 RepRap reference specification** for a scavenger-friendly 3D printer:
- **Target cost:** < $300 AUD (often $200-250 with good donors)
- **Build volume:** 220×220×220mm (Anet A8 bed size)
- **Philosophy:** "Tractor with a Racecar Brain" — heavy hardware + Klipper intelligence
- **Target release:** End of 2026

## Read First (Priority Order)

1. **PHILOSOPHY.md** — The "Tractor" concept, heritage acknowledgments
2. **docs/adr/README.md** — Index of all architectural decisions
3. **docs/adr/021-dual-rod-motion-system.md** — Current motion system (Dual 8mm)
4. **docs/adr/012-mainboard-host-architecture.md** — Tier system, dual-MCU config
5. **docs/reference/donor-printer-guide.md** — Which printers to scavenge

## Key Architectural Decisions

| Topic | Decision | ADR |
|-------|----------|-----|
| Frame | M10 threaded rod skeleton | ADR-001 |
| Motion | Dual 8mm rods, vertical stacking | ADR-021 |
| Bearings | LM8LUU (X), LM8UU (Y/Z), or IGUS | ADR-022 |
| Z-System | Z-drop (bed moves), Triple-Z leveling | ADR-005, ADR-023 |
| Bed Size | 220×220mm (Anet A8 scavenger size) | ADR-024 |
| Extruder | Pitan (3:1 geared, single-drive) | ADR-019 |
| Hotend | E3D V6 + CHT nozzle | ADR-004 |
| Electronics | Dual-MCU Klipper (Tier 2) or MKS SKIPR (Tier 3) | ADR-012 |
| Drivers | TMC2209, sensorless homing optional | ADR-013 |

## Build Tiers

| Tier | Description | Electronics | Cost |
|------|-------------|-------------|------|
| 1 | Single donor, belt-driven Z, no auto-level | 1× 4-driver board | ~$80 |
| **2** | **Dual donor, Triple-Z, dual-MCU Klipper** | **2× 4-driver boards** | **~$200** |
| 3 | Reference spec, integrated host | MKS SKIPR | ~$300 |

**Tier 2 is the recommended scavenger path** — two donor printers provide 8 drivers (need 7).

## Donor Printer Tiers

- **Tier A (best):** Rod-bearing donors — Anet A8, Prusa clones, i3 Mega
- **Tier B:** V-slot donors — Ender 3, CR-10 (no rods, need to buy stainless + IGUS ~$73)
- **Tier C (limited):** Prusa Mini, deltas, resin printers

## Heritage (What We Borrowed)

| Project | Contribution |
|---------|--------------|
| RepRap Darwin | Box-frame threaded-rod skeleton |
| RepRap Mendel | "Plough" X-carriage sled on dual rods |
| Prusa i3 Rework | Wade geared extruder → Pitan |
| Voron Legacy | Dual 8mm rods, vertical stacking |
| Voron Trident | Three-pillar Z-drop, Triple-Z leveling |
| The 100 / The Rook | Klipper-first philosophy |

## Technology Stack

- **CAD:** build123d (Python BREP, not OpenSCAD)
- **Documentation:** Quarto (literate programming, conditional content)
- **Firmware:** Klipper (Input Shaping, Pressure Advance, Z-tilt)
- **Config:** Python (`cad/config.py`) drives parametric generation

## Conventions

- **Currency:** Always AUD (Australian Dollars)
- **ADRs:** All major decisions documented in `docs/adr/`
- **Supersession:** Old ADRs preserved with "Superseded by ADR-XXX" notes
- **Rod sizes:** M10 for frame, 8mm for motion (Dual-8 reference spec)
- **Bed size:** 220×220mm reference (supports 200-250mm parametrically)

## File Structure

```
neo-darwin/
├── MANIFESTO.md          # Quick overview
├── PHILOSOPHY.md         # "Tractor" philosophy, heritage
├── REFERENCE-SPEC.md     # Hardware specification
├── BUILDING.md           # Build instructions
├── cad/
│   ├── config.py.example # Master configuration
│   ├── parts/            # build123d part scripts
│   └── build.sh          # STL generation
├── docs/
│   ├── adr/              # Architecture Decision Records
│   ├── guides/           # Tier-specific build guides
│   ├── reference/        # Background material, donor guide
│   └── deep-dives/       # Design exploration
└── scripts/
    ├── wizard.py         # Configuration wizard
    ├── analyze.py        # Engineering analysis
    └── whatif.py         # Trade-off comparisons
```

## Current Project Status

| Component | Status |
|-----------|--------|
| Philosophy & ADRs | ✅ Complete |
| Build system (wizard, analysis) | ✅ Complete |
| build123d parametric parts | 🔧 In development |
| Klipper configurations | 🔧 In development |
| Assembly documentation | 🔧 Planned |
| Reference build | ⏳ Planned (2026) |

## What NOT To Do

- Don't use OpenSCAD — we chose build123d (ADR-017)
- Don't suggest linear rails — smooth rods are intentional (ADR-021)
- Don't chase high speed — 70-120mm/s is the target, not 300mm/s
- Don't add cloud features — 100% local control is a core value
- Don't forget heritage credits — we stand on shoulders of giants

## Second-Hand Market Context

- Donor printers expected to bottom out at ~$50 AUD by end of 2026
- Real pricing (AliExpress 2026): 8× stainless rods $43, 22× IGUS $30
- Two Anet A8 donors = ~$200 total build (no rod purchase needed)
- Two Ender 3 donors = ~$275 total build (must buy rods + IGUS)

## Useful Commands

```bash
# Generate config from wizard
python scripts/wizard.py

# Quick engineering analysis
python scripts/analyze.py --quick

# Compare rod options
python scripts/whatif.py --compare-rods

# Build all STL parts
cd cad && ./build.sh build_all
```

---

*Last updated: January 2025*
