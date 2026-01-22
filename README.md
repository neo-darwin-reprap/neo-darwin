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
| **Build Volume** | 235×235×250mm |
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
| 1 | Single Donor | One printer, belt-driven Z | ~$80 AUD |
| 2 | Dual Donor | Two printers, Triple-Z | ~$150 AUD |
| **3** | **Reference Spec** | MKS SKIPR, Triple-Z, integrated | ~$270 AUD |

All tiers use the same extruder (Pitan), same motion system, same Klipper tuning. The wizard helps you determine which tier your parts support.

---

## Documentation

| Document | Description |
|----------|-------------|
| [MANIFESTO.md](MANIFESTO.md) | Quick-start overview |
| [PHILOSOPHY.md](PHILOSOPHY.md) | The "Tractor" philosophy |
| [REFERENCE-SPEC.md](REFERENCE-SPEC.md) | Hardware specification |
| [BUILDING.md](BUILDING.md) | Complete build guide |
| [scripts/README.md](scripts/README.md) | Build system documentation |
| [docs/adr/](docs/adr/) | Architecture Decision Records |

---

## The Lineage

* **[RepRap Darwin (2007)](https://reprap.org/wiki/Darwin):** The origin. We carry its name forward.
* **[Prusa i3 Rework (2013)](https://www.thingiverse.com/thing:119616):** The source of our geared extruder heritage.
* **[RepRap Mendel Revisited (2024)](https://www.thingiverse.com/thing:6783269):** A modern nod to the threaded rod skeleton.
* **[The 100](https://github.com/MSzturc/the100) / [The Rook](https://github.com/Kanrog/Rook) (2023):** Proof that Klipper makes DIY frames competitive.

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
