"""
Darwin-Neo Master Configuration
Parametric Logic for High-Mass, Low-Cost 3D Printing.
"""

# --- 1. DONOR & TRANSPARENCY ---
# Options: "PRUSA_CLONE", "ENDER_3", "SCAVENGED"
DONOR_TYPE = "ENDER_3" 

# --- 2. THE SKELETON (M12 RODS) ---
M12_NOMINAL_DIA = 12.0 
# Set 0.2 for Zinc, 0.5+ for Galvanized (The "Lumpy Factor")
LUMPY_FACTOR = 0.5 
M12_FIT_DIA = M12_NOMINAL_DIA + LUMPY_FACTOR

# --- 3. MOTION FORK (SMOOTH RODS) ---
# 8.0 for salvage, 10.0 for "Neo" Standard
SMOOTH_ROD_DIA = 10.0 
BEARING_TYPE = "LM10UU" if SMOOTH_ROD_DIA == 10.0 else "LM8UU"

# --- 4. TIER DEFINITIONS ---
TRIPLE_Z = True          # True = Independent 3-point Z-Tilt
EXTRUDER_TYPE = "WADE"   # The Signature 13:43 Geared Torque Monster
HOTEND_DONOR = "ENDER_MK8" 

# --- 5. BUILD VOLUME ---
BUILD_VOLUME = {"X": 250, "Y": 250, "Z": 250}

# --- 6. DYNAMIC FRAME CALCULATIONS ---
# Greg's Wade requires a significant "Gear Overhang" on the X-axis
X_OVERHANG = 50.0 if EXTRUDER_TYPE == "WADE" else 25.0

# Width: Bed + Overhangs + Rod Clearances
SKELETON_X = BUILD_VOLUME["X"] + (X_OVERHANG * 2) + 40 
# Depth: Bed + room for Triple-Z Spider and cable arches
SKELETON_Y = BUILD_VOLUME["Y"] + 120 
# Height: Bed + Z-Puck stacking
SKELETON_Z = BUILD_VOLUME["Z"] + 80 

# --- 7. UTILITIES ---
def print_config_summary():
    """Manifesto Transparency Check"""
    print(f"--- Darwin-Neo Configuration: {DONOR_TYPE} Path ---")
    if DONOR_TYPE == "ENDER_3":
        print(f"!!! MOTION GAP: Ender rollers incompatible. Buy 6x {SMOOTH_ROD_DIA}mm rods.")
    print(f"Frame Dimensions: {SKELETON_X} x {SKELETON_Y} x {SKELETON_Z}")