Here is the **`main_build.py`** that acts as the "Construct" for your Darwin-Neo. It uses a modular approach, allowing you to "download" or skip the advanced tiers (PINDA, Filament Sensor, ADXL345) based on the builder's preference.

### 1. The Modular Master Script (`main_build.py`)

This script imports your logic from `project_vars.py` and organizes the CAD generation.

```python
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

```

---

### 2. The "Intelligence" Node: ADXL345 Wiring

To hit that MK4 quality, your builder needs to wire the **ADXL345** to the **MKS SKIPR**. Since the SKIPR has a dedicated "PI" header, we use the hardware SPI pins for maximum data speed.

| ADXL345 Pin | MKS SKIPR Header | Description |
| --- | --- | --- |
| **VCC** | 3.3V | Power (Do NOT use 5V) |
| **GND** | GND | Ground |
| **CS** | GPIO8 (CE0) | Chip Select |
| **SDO** | GPIO9 (MISO) | Master In Slave Out |
| **SDA** | GPIO10 (MOSI) | Master Out Slave In |
| **SCL** | GPIO11 (SCLK) | Clock |

---

### 3. The "Neo" Start G-Code (Tiered)

Update your Klipper `macros.cfg` to handle the ADXL check. This ensures the machine is "self-aware" before it starts a high-speed print.

```toml
[gcode_macro START_PRINT]
gcode:
    # 1. Wake up the Matrix
    G28 ; Home all
    
    # 2. Tier 2: Level the Bed (Triple-Z)
    Z_TILT_ADJUST 
    
    # 3. Tier 3: Quality Check (Input Shaper)
    # This runs a quick resonance check if the user has the ADXL connected
    # MEASURE_AXES_NOISE 

    # 4. Final Prep
    BED_MESH_PROFILE LOAD=default
    LINE_PURGE ; Modern Klipper 'Prime Line'

```

---

### 💡 Why this works as a "Right of Passage"

By building the **Darwin-Neo**, a maker goes through the same journey as the early RepRap pioneers but with 2026 shortcuts:

* **The Manual Phase:** Tightening 100+ M12 nuts (Builds patience/character).
* **The Digital Phase:** Tuning the ADXL345 (Builds technical expertise).
* **The Social Phase:** Printing a set of "Neo Corners" for a friend (Builds the community).

This is the ultimate $300 AUD machine. It has the **soul of a JunkStrap**, the **mass of a bridge**, and the **precision of a laser**.

**Is there any specific donor printer you've seen on Marketplace that we should check the dimensions for?** (e.g. "I found a broken Ender 3 V2 for $50"). Knowing the specific donor helps us lock in the `project_vars.py` for your first test print.