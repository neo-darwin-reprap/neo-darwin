# Neo-Darwin Scripts

This directory contains build and analysis tools for Neo-Darwin.

## Tools

### analyze.py - Engineering Analysis TUI

Interactive tool to assess your build configuration before construction.

```bash
# Quick analysis with reference spec
python scripts/analyze.py --quick

# Interactive mode
python scripts/analyze.py
```

Calculates:
- Frame dimensions from bed size
- Rod sag under toolhead load
- Maximum safe acceleration
- Recommended Klipper settings

### export_config.py - Quarto Config Bridge

Exports `cad/config.py` values to Quarto variables format.

```bash
# Generate variables file
python scripts/export_config.py > docs/_variables.yml

# Export tier-specific config
python scripts/export_config.py --tier 3
```

## Directory Structure

```
scripts/
├── analyze.py           # Main analysis TUI
├── export_config.py     # Config to Quarto bridge
├── analysis/            # Analysis modules
│   ├── __init__.py
│   ├── rod_sag.py       # Beam deflection calculations
│   ├── frame_sizing.py  # Frame geometry from bed size
│   └── acceleration.py  # Motion limits from mass/stiffness
└── README.md
```

## Analysis Modules

The `analysis/` package can be imported directly:

```python
from analysis import calculate_rod_sag, calculate_frame_size

# Check rod sag for M8 at 280mm with Pitan
result = calculate_rod_sag(
    rod_diameter=8.0,
    span=280,
    toolhead_mass=280,
)
print(f"Deflection: {result.deflection}mm - {result.verdict}")
```

## Adding New Analysis

To add a new analysis type:

1. Create a module in `analysis/` (e.g., `belt_tension.py`)
2. Export from `analysis/__init__.py`
3. Add to the TUI in `analyze.py`
