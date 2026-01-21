#!/usr/bin/env python3
"""
Export config.py values to Quarto variables format.

Usage:
    python scripts/export_config.py > docs/_variables.yml

This generates a YAML file that Quarto can use for conditional content
and variable substitution in documentation.
"""

import sys
from pathlib import Path

# Add cad directory to path to import config
cad_path = Path(__file__).parent.parent / "cad"
sys.path.insert(0, str(cad_path))

try:
    import config
except ImportError:
    print("Error: Could not import config.py from cad/", file=sys.stderr)
    print("Make sure cad/config.py exists.", file=sys.stderr)
    sys.exit(1)


def export_quarto_variables():
    """Export config values as Quarto variables."""

    # Mapping of config values to documentation-friendly names
    variables = {
        # Frame skeleton
        "ROD_TYPE": f"M{int(config.M10_NOMINAL_DIA)}",
        "ROD_NOMINAL_DIA": config.M10_NOMINAL_DIA,
        "LUMPY_FACTOR": config.LUMPY_FACTOR,

        # Smooth rods
        "SMOOTH_ROD_DIA": config.SMOOTH_ROD_DIA,
        "BEARING_TYPE": config.BEARING_TYPE,

        # Extruder
        "EXTRUDER_TYPE": config.EXTRUDER_TYPE,
        "EXTRUDER_NAME": {
            "PITAN": "Pitan (3:1 geared)",
            "WADE": "Greg's Wade (5.22:1 geared)",
            "MK8": "MK8 Direct Drive"
        }.get(config.EXTRUDER_TYPE, config.EXTRUDER_TYPE),

        # Z system
        "TRIPLE_Z": config.TRIPLE_Z,
        "Z_SYSTEM": "Triple-Z Independent" if config.TRIPLE_Z else "Belted Single-Z",

        # Build volume
        "BUILD_X": config.BUILD_VOLUME["X"],
        "BUILD_Y": config.BUILD_VOLUME["Y"],
        "BUILD_Z": config.BUILD_VOLUME["Z"],

        # Frame dimensions
        "SKELETON_X": config.SKELETON_X,
        "SKELETON_Y": config.SKELETON_Y,
        "SKELETON_Z": config.SKELETON_Z,

        # Donor type
        "DONOR_TYPE": config.DONOR_TYPE,

        # Derived values for documentation
        "ROD_FINISH_ZINC": "Bright Zinc (lumpy_factor = 0.2)",
        "ROD_FINISH_GALV": "Hot-Dip Galvanized (lumpy_factor = 0.5+)",
    }

    # Output as YAML
    print("# Auto-generated from cad/config.py")
    print("# Run: python scripts/export_config.py > docs/_variables.yml")
    print("")

    for key, value in variables.items():
        if isinstance(value, bool):
            print(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, str):
            print(f'{key}: "{value}"')
        elif isinstance(value, (int, float)):
            print(f"{key}: {value}")
        else:
            print(f'{key}: "{value}"')


def export_tier_config(tier: int):
    """Export tier-specific configuration."""

    tier_configs = {
        0: {
            "TIER_NAME": "Tier 0: Klipper Only",
            "TIER_DESC": "Flash Klipper on existing printer",
            "KLIPPER_HOST": "Laptop/RPi/Zero2W",
            "MCU": "Donor board",
            "Z_SYSTEM": "Keep donor Z system",
            "COST_ESTIMATE": "$0",
        },
        1: {
            "TIER_NAME": "Tier 1: Single Donor",
            "TIER_DESC": "One donor printer, belt-driven Z",
            "KLIPPER_HOST": "Laptop/RPi/Zero2W",
            "MCU": "Donor board",
            "Z_SYSTEM": "Belted Single-Z",
            "COST_ESTIMATE": "~$80 AUD",
        },
        2: {
            "TIER_NAME": "Tier 2: Dual Donor",
            "TIER_DESC": "Two donors, Triple-Z, multi-MCU",
            "KLIPPER_HOST": "Laptop/RPi/Zero2W",
            "MCU": "Multi-MCU (2 donor boards)",
            "Z_SYSTEM": "Triple-Z Independent",
            "COST_ESTIMATE": "~$200 AUD",
        },
        3: {
            "TIER_NAME": "Tier 3: Reference Spec",
            "TIER_DESC": "MKS SKIPR, Triple-Z, CAN bus ready",
            "KLIPPER_HOST": "Integrated (SKIPR)",
            "MCU": "MKS SKIPR",
            "Z_SYSTEM": "Triple-Z Independent",
            "COST_ESTIMATE": "~$270 AUD",
        },
    }

    if tier not in tier_configs:
        print(f"Error: Unknown tier {tier}", file=sys.stderr)
        return

    print(f"# Tier {tier} Configuration")
    for key, value in tier_configs[tier].items():
        print(f'{key}: "{value}"')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Export config.py to Quarto variables")
    parser.add_argument("--tier", type=int, choices=[0, 1, 2, 3],
                        help="Export tier-specific config")
    args = parser.parse_args()

    if args.tier is not None:
        export_tier_config(args.tier)
    else:
        export_quarto_variables()
