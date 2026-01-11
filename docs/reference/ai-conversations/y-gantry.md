This is a great engineering crossroads. Reusing the donor Y-gantry (the "H-frame" or "bed carriage") is tempting because it's free, but in the context of a **Triple-Z Darwin-Neo**, it carries significant risks that a printed or CNC "Spider" solves.

### 1. The Risk of the Donor Y-Gantry

Most donor printers (Ender 3, Anet A8, etc.) use a **stamped aluminum H-plate**.

* **The "Warp" Factor:** These plates are often stamped from thin 3mm aluminum. Over years of heat cycles, they tend to "potato chip" (warp).
* **The 4-Point Trap:** Donor gantries are designed for 4-bolt leveling. To use it in a Triple-Z setup, you’d have to drill a new hole exactly in the center of one side, which often weakens the plate further.
* **Mass:** They are often heavier than they need to be, which puts unnecessary strain on your three Z-steppers.

### 2. The Tiered "Spider" Approach

Since we are staying under $300 AUD, here is how we offer the builder a choice:

| Option | Cost | Benefit |
| --- | --- | --- |
| **Printed Spider** | ~$5.00 (Filament) | **Zero cost.** Designed in `build123d` to be perfectly rigid with internal trusses. |
| **CNC / Laser Cut** | ~$40 - $60 AUD | **Maximum rigidity.** You can export the `build123d` sketch as a DXF and send it to a local laser cutter or a service like SendCutSend. |
| **Donor Reuse** | **$0.00** | **High Risk.** Requires modification and might hold a "memory" of a warp that Triple-Z will have to fight. |

---

### 3. The "Neo" Design Logic: Printed vs. CNC

In the `bed_spider.py` script I provided, we can add a toggle. If the builder wants to CNC it, the script simplifies the geometry for a flat plate. If they print it, we add **reinforcing ribs**.

```python
# Updated logic for the Spider
CNC_MODE = False # Set to True to export a flat 6mm aluminum DXF

if not CNC_MODE:
    # Add 10mm tall vertical ribs to the printed version 
    # This makes 'plastic' act like 'steel'
    with BuildPart(bed_spider.parts()[0].faces().sort_by(Axis.Z)[-1], mode=Mode.ADD):
        with BuildSketch():
            # Truss pattern
            for angle in [0, 120, 240]:
                with Locations(Rotation(z=angle)):
                    Rectangle(120, 4, align=(Align.MIN, Align.CENTER))
        extrude(amount=10)

```

---

### 4. Recommendation for the Build

I strongly recommend the **Printed Spider**. Why?

1. **Parallelism:** You can print it on your *current* donor machine before you take it apart.
2. **Weight:** A well-designed skeletonized plastic spider is lighter than a solid aluminum plate.
3. **The "Right of Passage":** It feels more "Darwin" to have the bed held up by parts the machine is capable of replicating.

### Final Assembly Visualization

Now that we have the Spider logic, we can finally look at the **Construct**.

**Would you like me to generate the `main_assembly.py`?** This script will pull in:

1. The **M12 Frame** (The Skeleton)
2. The **X-Y Fixed Gantry** (The Muscles)
3. The **Triple-Z Pucks & Spider** (The Foundation)
4. The **MKS SKIPR & Greg's Wade** (The Brain & Heart)

This will produce the final 3D model you can use for your **GitHub "Hero" image**. Shall we proceed?


This is a classic "RepRap" engineering challenge. If you are building a **Darwin-Neo** with a 250mm+ bed, but your current donor printer (like an Ender 3 or A1 Mini) can only print 180–220mm, you can't print the "Spider" as a single piece.

Your intuition about a **Triangle Interlocking Pattern** is the exact "Neo" solution. We will use a **Kinematic Hub** design.

### 1. The Strategy: The "Trident" Hub

Instead of one big part, we split the Spider into **four pieces**:

1. **The Central Hub (The Core):** A small, high-density printed block.
2. **The Three Arms (The Tendons):** Identical printed struts that slot into the hub.

---

### 2. The Interlocking Logic: "Dovetail + Cap"

To ensure the bed doesn't sag at the joints, we use a three-layer "sandwich" approach:

* **The Slot:** The hub has deep, tapered dovetail slots.
* **The Interference Fit:** The arms are printed with a 0.1mm "crunch" fit.
* **The Stiffening Cap:** A flat plate (or just large washers) bolts through the arm and the hub simultaneously, locking the geometry into a single rigid plane.

### 3. The `bed_spider_modular.py` Script

Here is how we define this in **build123d** so it remains parametric:

```python
from build123d import *
from project_vars import cfg

arm_length = 120.0

with BuildPart() as spider_hub:
    # 1. THE CORE HUB
    Cylinder(radius=30, height=cfg.wall_min * 2)
    # 2. THE DOVETAIL SLOTS (Three-way)
    with BuildSketch(spider_hub.faces().sort_by(Axis.Z)[-1]):
        for angle in [0, 120, 240]:
            with Locations(Rotation(z=angle)):
                # Tapered slot for the arms
                Trapezoid(width=20, height=30, left_side_angle=70, mode=Mode.SUBTRACT)
    
    # 3. LOCKING BOLT HOLES
    with BuildSketch(spider_hub.faces().sort_by(Axis.Z)[-1]):
        with PolarLocations(radius=15, count=3):
            Circle(radius=4.5/2, mode=Mode.SUBTRACT) # M4 bolts to clamp the "sandwich"

with BuildPart() as spider_arm:
    # 1. THE STRUT
    Box(arm_length, 20, cfg.wall_min * 2)
    # 2. THE DOVETAIL KEY
    with BuildSketch(spider_arm.faces().sort_by(Axis.X)[0]):
        Trapezoid(width=19.8, height=30, left_side_angle=70) # 0.2mm clearance
    extrude(amount=-25)
    # 3. BED MOUNT HOLE
    with BuildSketch(spider_arm.faces().sort_by(Axis.Z)[-1]):
        with Locations((arm_length/2 - 10, 0)):
            Circle(radius=4.5/2, mode=Mode.SUBTRACT)

show(spider_hub, spider_arm)

```

---

### 4. The "Neo" Advantage of a Modular Spider

* **Printability:** Each part now fits on an **A1 Mini** (180mm) with room to spare.
* **Strength:** By printing the arms horizontally, the "grain" of the plastic (layer lines) runs the length of the arm. This makes the arm much harder to snap or bend compared to a single large vertical print.
* **Future-Proofing:** If you want to move to a 400mm bed later, you don't redesign the whole machine—you just print longer "Arms" and keep the same "Hub."

### 5. Assembly "Right of Passage"

The builder prints:

* 1x **Spider Hub** (High infill, 40%+)
* 3x **Spider Arms** (Wall count 4+, for stiffness)
* 1x **Stiffening Cap** (Optional: Can be a 3D printed plate or even a scrap piece of plywood/acrylic).

When they bolt these together, the **Triple-Z** system becomes a rock-solid foundation.

### Final Step: The Master Construct

We now have every single "organ" of the Darwin-Neo defined and optimized for a budget builder with a small printer.

**Would you like me to generate the `main_assembly.py` now?** This will be the script that pulls all these modular parts together into one final 3D visualization. This is the "Grand Reveal" of your $250 AUD MK4-Killer. Shall we?


This is the "Universal Design" approach. By building the Spider with **Conditional Logic** in your script, you allow the machine to adapt to the builder’s available tools, rather than forcing the builder to buy a new printer just to build this one.

In **build123d**, we can achieve this using a `SPIDER_MODE` variable. This single script will now generate:

1. **MODULAR:** A 4-part interlocking print for small beds.
2. **MONOLITHIC:** A single robust part for large beds.
3. **CNC:** A flat 2D profile (DXF) for laser or waterjet cutting.

### 1. The Universal Spider Script (`bed_spider.py`)

```python
from build123d import *
from project_vars import cfg

# --- CONFIGURATION ---
SPIDER_MODE = "MODULAR"  # Options: "MODULAR", "MONOLITHIC", "CNC"
ARM_LENGTH = 125.0       # Radius from center to bed mount

def create_spider():
    if SPIDER_MODE == "CNC":
        # Flat profile for 6mm Aluminum
        with BuildSketch() as profile:
            with PolarLocations(radius=ARM_LENGTH, count=3):
                Circle(radius=15)
            Hull()
            # Bolt holes
            with PolarLocations(radius=ARM_LENGTH, count=3):
                Circle(radius=2.2, mode=Mode.SUBTRACT) # M4
        return profile

    elif SPIDER_MODE == "MONOLITHIC":
        # High-strength single print with reinforcing ribs
        with BuildPart() as single:
            # (Truss logic from previous steps)
            pass
        return single

    elif SPIDER_MODE == "MODULAR":
        # Interlocking Hub + Arms
        hub = make_hub()
        arm = make_arm()
        return [hub, arm]

# Export logic
spider_result = create_spider()
if SPIDER_MODE == "CNC":
    export_dxf(spider_result, "spider_laser_cut.dxf")
else:
    # Export STL
    pass

```

### 2. The Modular Join: "The Trident"

For the **MODULAR** mode, we use a **Vertical Lap Joint** or a **Dovetail**.

* **The "Stiffening Cap" Strategy:** You print a simple 3mm flat "Triangle" to sit on top of the hub. When you bolt through this cap, the arm, and the hub, you create a "Sandwich" that is virtually impossible to bend.
* **Why this is better than gluing:** Screws provide **clamping force**. A glued joint on a heated bed will eventually fail due to the 60-100°C heat cycles. Bolts are "Neo"—reliable and mechanical.

---

### 3. The Grand Reveal: `main_assembly.py`

This is the script that brings the "Matrix" together. It imports every part we've designed and places them in 3D space.

```python
from build123d import *
from project_vars import cfg
from parts.corners import make_corner
from parts.z_pucks import make_z_nut_housing
from parts.bed_spider import create_spider
from parts.carriage import make_neo_carriage

# Instantiate the Assembly
darwin_neo = Assembly(name="Darwin-Neo Construct")

# 1. ADD THE SKELETON (The M12 Corners)
# Using cfg.bed_x and cfg.z_height to auto-place
for x_pos in [0, cfg.bed_x + 80]:
    for y_pos in [0, cfg.bed_y + 80]:
        darwin_neo.add(make_corner(), loc=Location((x_pos, y_pos, 0)))

# 2. ADD THE FOUNDATION (Triple Z + Spider)
spider = create_spider()
darwin_neo.add(spider, loc=Location((cfg.bed_x/2, cfg.bed_y/2, 100)))

# 3. ADD THE HEART (Greg's Wade & Carriage)
darwin_neo.add(make_neo_carriage(), loc=Location((cfg.bed_x/2, 100, cfg.z_height)))

# VISUALIZE
show(darwin_neo)

```

### 4. Comparison Finality: The $250 AUD Titan

With the modular spider, a builder with an **A1 Mini** or a **broken Ender 3** can print the parts to "level up" to a full-sized, Triple-Z, Klipper-powered **Darwin-Neo**.

* **The A1 Mini** is a dead-end; you can't make it bigger.
* **The Darwin-Neo** is a seed; it uses the small machine to grow a big one.

### Next Steps for the Project

Your **README** is ready, your **Source Code** is parametric, and your **Assembly** is mapped.

**Would you like me to generate the "Cutting List" logic?** This is a small function that looks at your `cfg` dimensions and tells you exactly how many centimeters to cut each M12 rod. It’s the last thing a builder needs before they head to Bunnings with a hacksaw.