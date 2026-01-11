from build123d import *
from project_vars import cfg, BOM
# Importing our modular parts
from parts.corners import make_corner
from parts.z_pucks import make_z_nut_housing
from parts.carriage import make_neo_carriage
from parts.electronics import make_skipr_mount

# --- TIER SELECTION (The Neo Choice) ---
BUILD_TIER = 3  # 1: Basic, 2: Auto-Level, 3: Full Neo (Sensors + ADXL)

def generate_full_assembly():
    assembly = Compound(label="Darwin_Neo_Construct")
    
    # 1. GENERATE SKELETON (8 Corners)
    for x in [0, cfg.bed_x + 100]:
        for y in [0, cfg.bed_y + 100]:
            for z in [0, cfg.z_height + 100]:
                assembly.add(make_corner().moved(Location((x, y, z))))
    
    # 2. GENERATE MOTION (Z-Pucks & X-Carriage)
    # We add 3 Z-pucks for our Triple-Z setup
    for i in range(3):
        assembly.add(make_z_nut_housing().moved(Location((0, 0, 50 * i))))

    # 3. APPLY TIERS
    carriage = make_neo_carriage(include_sensor_wing=(BUILD_TIER >= 2))
    assembly.add(carriage)

    if BUILD_TIER >= 3:
        # Add the 'Intelligence' hardware
        print(">> Adding ADXL345 Mount & Filament Sensor Puck...")
        BOM.add("ADXL345 Accelerometer", 1)
        BOM.add("Filament Microswitch", 1)
        # (Add CAD generation for these here)

    return assembly

if __name__ == "__main__":
    neo_printer = generate_full_assembly()
    export_stl(neo_printer, "darwin_neo_full_assembly.stl")
    
    # The Matrix Output
    BOM.print_report()
    print(f"Construction Complete. Build Tier: {BUILD_TIER}")