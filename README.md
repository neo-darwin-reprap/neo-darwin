# Neo-Darwin

### A 2026 RepRap Reference Specification

**High-Mass, Low-Cost, Total Control.**

---

## The Tractor is Coming

Neo-Darwin is a reimagining of the 2007 RepRap Darwin — a high-mass, fully parametric 3D printer built from M10 threaded rod, salvaged components, and open-source intelligence.

**Expected Release:** Q2/Q3 2026

---

## The Philosophy

We build a **"Tractor with the Brain of a Racecar"** — using heavy, high-torque, battle-tested hardware and giving it extreme precision through Klipper.

| Feature | Target |
|---------|--------|
| **Price** | < $300 AUD |
| **Build Volume** | 220×220×220mm |
| **Accuracy** | ±0.1mm |
| **Speed** | 70–120mm/s |
| **Control** | 100% Local, No Cloud |

---

## Quick Start

### Option 1: Configuration Wizard (Recommended)

```bash
git clone https://github.com/neo-darwin-reprap/neo-darwin.git
cd neo-darwin

# Run the wizard - it asks what parts you have
python scripts/wizard.py
```

The wizard:
1. Asks about your scavenged parts (motors, boards, bed)
2. Auto-detects your build tier (1-3)
3. Generates `config.py`
4. Runs engineering analysis

### Option 2: Quick Analysis

```bash
# See what the reference spec looks like
python scripts/analyze.py --quick

# Explore trade-offs (what if M8 rods? what if 200x200 bed?)
python scripts/whatif.py --compare-rods
python scripts/whatif.py --compare-beds
```

### Option 3: Build STL Parts

```bash
cd cad
./setup.sh        # First time: creates venv, installs deps, configures
./build.sh build_all   # Build all STL files
```

See [BUILDING.md](BUILDING.md) for complete guide.

---

## Build Tiers

| Tier | Name | Description | Cost |
|------|------|-------------|------|
| 1 | Single Donor | One printer, belt-driven Z, no auto-level | ~$80 AUD |
| **2** | **Dual Donor** | Two printers, Triple-Z, dual-MCU Klipper | **~$200 AUD** |
| 3 | Reference Spec | MKS SKIPR, Triple-Z, integrated host | ~$300 AUD |

**Tier 2 is the recommended scavenger path.** Two donor printers provide 8 stepper drivers (need 7), eliminating the need for new electronics. All tiers use the same Pitan extruder, dual-rod motion system, and Klipper tuning.

---

## Documentation

| Document | Description |
|----------|-------------|
| [MANIFESTO.md](MANIFESTO.md) | Quick-start overview |
| [PHILOSOPHY.md](PHILOSOPHY.md) | The "Tractor" philosophy and heritage |
| [REFERENCE-SPEC.md](REFERENCE-SPEC.md) | Hardware specification |
| [BUILDING.md](BUILDING.md) | Complete build guide |
| [scripts/README.md](scripts/README.md) | Build system documentation |
| [docs/adr/](docs/adr/) | Architecture Decision Records |
| [docs/reference/donor-printer-guide.md](docs/reference/donor-printer-guide.md) | Which printers to scavenge |

---

## The Lineage

We stand on the shoulders of giants:

* **[RepRap Darwin (2007)](https://reprap.org/wiki/Darwin):** Box-frame threaded-rod origin. We carry its name forward.
* **[RepRap Mendel (2009)](https://reprap.org/wiki/Mendel):** The "plough" X-carriage sled design.
* **[Prusa i3 Rework (2013)](https://www.thingiverse.com/thing:119616):** Greg's Wade geared extruder—ancestor of our Pitan.
* **[Voron Legacy](https://vorondesign.com/voron_legacy):** Dual 8mm rods with vertical stacking for X-Y gantry.
* **[Voron Trident](https://vorondesign.com/voron_trident):** Three-pillar Z-drop bed with Triple-Z leveling.
* **[The 100](https://github.com/MSzturc/the100) / [The Rook](https://github.com/Kanrog/Rook):** Klipper-first philosophy on DIY frames.

---

## Status

| Component | Status |
|-----------|--------|
| Manifesto & Philosophy | ✅ Complete |
| Build System (wizard, analysis, what-if) | ✅ Complete |
| build123d Parametric Parts | 🔧 In Development |
| Klipper Configurations | 🔧 In Development |
| Assembly Documentation | 🔧 In Development |
| Reference Build | ⏳ Planned |

---

## Stay Updated

⭐ **Star this repo** to follow development.

📬 **Discussions** will open closer to release.

---

## License

**GNU GPL v3** — The same license used by the original RepRap Darwin.

---

> *If you want a printer, buy one. If you want the Red Pill, build this.*
