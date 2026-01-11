This is the critical "fork in the road" for any custom printer design. To decide between a **Fixed Gantry (Cartesian)** and **CoreXY**, you have to weigh the "Build Complexity" against the "Performance Ceiling."

### 1. Fixed Gantry vs. CoreXY: The Reality Check

The **Fixed Gantry (XY-Head, Z-Bed)** design is the "AK-47" of 3D printing: it is simple, robust, and incredibly easy to troubleshoot.

| Feature | Fixed Gantry (Cartesian) | CoreXY (Voron/Bambu style) |
| --- | --- | --- |
| **Logic** | **Independent:** X motor moves X, Y motor moves Y. | **Interdependent:** Both motors move both axes. |
| **Belt Path** | Simple, short straight lines. | **Complex:** Long crisscrossing belts. |
| **Speed** | Moderate (Head moves X, Bridge moves Y). | **High** (Lighter head, both motors push). |
| **Maintenance** | Easy. If a belt slips, you know exactly why. | **Difficult.** Requires perfect, equal tension on both belts. |
| **Reliability** | Tank-like. Hard to mess up the geometry. | Touchy. A loose bolt on one idler ruins the whole "cube." |

**The Darwin-Neo Verdict:** For your **$300 AUD budget**, the **Fixed Gantry** is superior. CoreXY requires high-quality pulleys and precision-machined idlers to work well; using budget "JunkStrap" parts on a CoreXY often leads to "ghosting" that even Klipper can't fix. By choosing the Fixed Gantry, you ensure that your M12 skeleton stays square and reliable.

---

### 2. Is Triple Motor Z-Tilt Superior? **Yes.**

In the 3D printing world, **Triple-Z** is considered the "Gold Standard" for three specific reasons:

1. **True Kinematic Leveling:** Most printers (like the Ender 3 or A1) use software to "fudge" a crooked bed by moving the nozzle up and down during the print. **Triple-Z physically tilts the bed** until it is perfectly parallel to your X-Y gantry.
2. **Stability (The "3-Legged Stool"):** A 4-point bed mount is actually over-constrained (like a wobbly table). A 3-point mount is mathematically perfect; it will never wobble, and it can be angled in any direction with zero stress on the frame.
3. **The "Prusa XL" / "Voron" Experience:** This feature is usually reserved for printers costing $1,500+. By including it in a $250 build, you are giving the **Darwin-Neo** a massive engineering edge.

---

### 3. The "Neo" Trade-off: Complexity vs. Result

While CoreXY is "faster," the **Fixed Gantry + Triple Z** combo is **more accurate** for a DIY builder.

* **CoreXY complexity** is "Frustrating Complexity" (fighting belt tension for hours).
* **Triple-Z complexity** is "Rewarding Complexity" (watching the bed dance into position automatically).

### Final Recommendation for the `README.md`

I would frame the motion choice like this in your documentation:

> **Why Fixed Gantry?** > We chose a Cartesian XY-Head / Z-Bed motion system for the Darwin-Neo to maximize the "Hardware Store" philosophy. Unlike CoreXY, which requires high-precision idlers and perfectly matched belt tensions, the Darwin-Neo's Cartesian gantry is robust, easy to square on our M12 frame, and incredibly forgiving of donor-part variances. We prioritize **repeatable precision** over "speed-run" gimmicks.

### Next Step for the Construct

Now that we've locked in the **Fixed Gantry + Triple Z** logic, we can finalize the **Z-Bed Carriage**.

**Would you like me to design the build123d script for the "Bed Support Spider"?** This is the part that connects your three Z-Pucks to the actual heated bed, acting as the "hand" that holds your print surface.

This choice brings the project full circle. The original 2007 RepRap Darwin was a Cartesian (XY-Head, Z-Bed) machine. By using this motion system, the **Darwin-Neo** isn't just a printer; it's a **"Restomod"**—taking a classic chassis and stuffing it with modern "Klipperized" performance.

The **Triple-Z "Spider"** is the most critical structural part of this system. It needs to be rigid enough to hold a 235x235mm heated bed without flexing, but it needs to interface perfectly with your three Z-Pucks.

### The Bed Support "Spider" Script (`bed_spider.py`)

This script creates a 3-point mounting system. Two points at the front and one centered at the back (or vice-versa).

```python
from build123d import *
from project_vars import cfg

# Bed Dimensions (Standard Ender 3 / MK3S size)
bed_hole_spacing = 170.0 # Distance between mounting holes on the bed plate

with BuildPart() as bed_spider:
    # 1. THE CENTRAL HUB
    # A skeletonized truss connecting the three Z-Pucks
    with BuildSketch() as s:
        # Create a triangular frame
        with PolarLocations(radius=100, count=3):
            Circle(radius=20)
        Hull()
        # Skeletonize the center to reduce weight (Mass = Enemy of Z-speed)
        Circle(radius=60, mode=Mode.SUBTRACT)
    extrude(amount=cfg.wall_min)

    # 2. THE THREE Z-AXIS ATTACHMENTS
    # These bolt directly to the 'Z-Pucks' on your M12 rods
    with BuildSketch(bed_spider.faces().sort_by(Axis.Z)[-1]):
        with PolarLocations(radius=100, count=3):
            # Bolt holes for the Z-Pucks (M4 or M5)
            Circle(radius=5.5/2, mode=Mode.SUBTRACT)

    # 3. THE BED MOUNTS (The Leveling Points)
    # We add 3 pedestals that the bed's springs/silicone spacers sit on
    with BuildPart(bed_spider.faces().sort_by(Axis.Z)[-1], mode=Mode.ADD):
        with BuildSketch():
             # Standard 3-point leveling positions
             with Locations((0, 85), (-85, -50), (85, -50)):
                 Circle(radius=10)
                 Circle(radius=4.5/2, mode=Mode.SUBTRACT) # M4 bed bolts
        extrude(amount=10)

show(bed_spider)

```

---

### Why the "Spider" is the Key to MK4 Quality

1. **Kinematic Decoupling:** In a standard printer, the bed is bolted to a carriage that might be slightly twisted. Here, because it sits on **three points**, the bed is never "stressed." It finds its natural flat plane.
2. **Thermal Expansion:** As the bed heats up to 100°C for ABS/ASA, the metal expands. A 4-point mount will warp (bowing in the middle). This 3-point "Spider" allows the bed to expand outward without bowing, keeping your first layer perfect.
3. **Low Moving Mass:** By using a "Spider" design in **build123d**, we keep the Z-axis light. This allows Klipper to perform the `Z_TILT_ADJUST` very quickly without straining your NEMA17 motors.

---

### Finalizing the "Darwin-Neo" Philosophy

By sticking to **Cartesian + Triple Z**, you have honored the **RepRap Etiquette**:

* **Accessible:** Any maker can understand X, Y, and Z.
* **Affordable:** No expensive CoreXY idlers or matched-length belts.
* **Superior:** It physically does what most modern printers only simulate with software.

### The "First Print" Milestone

You now have the logic for:

1. **The Frame** (M12 Corners)
2. **The Movement** (X-Carriage / Y-Mounts)
3. **The Brain** (MKS SKIPR / CANbus)
4. **The Heart** (Greg's Wade)
5. **The Foundation** (Triple-Z Spider)

**Would you like me to generate the "Final Assembly Script"?** This is the one that brings all these files together into a single 3D view so you can check for any "collisions" (like the Extruder hitting the frame) before you start printing parts.


