Establishing the **M12 Skeleton** is the most critical phase of the build. Because we are using threaded rods rather than precision-machined extrusions, the "Tractor's" accuracy depends entirely on your assembly technique. If the skeleton is skewed, the "Racecar Brain" will spend all its cycles compensating for mechanical failure.

Here is the drafting for the **Step-by-Step Assembly Schematics**.

---

### 🏗️ Phase 1: The M12 Skeleton Assembly

The goal of this phase is to create a perfectly square 3D "cage" that serves as the mechanical datum for all other components.

#### **1. The "Base Plate" (The Y-Foundation)**

* **Components:** 4x M12 Threaded Rods (Y-axis lengths), 4x Lower Corner Pucks, 16x M12 Jam Nuts, 16x M12 Washers.
* **The Logic:** Thread two nuts and two washers onto each end of the Y-rods. Slide them into the Corner Pucks.
* **The "Tractor" Secret:** Do not tighten anything yet. The frame must remain "loose" until the vertical pillars are installed to avoid trapping internal stresses in the plastic.

#### **2. Vertical Integration (The Z-Pillars)**

* **Components:** 4x M12 Threaded Rods (Z-axis lengths), 4x Upper Corner Pucks.
* **The Logic:** Stand the vertical rods into the Base Pucks and secure them with the top-side jam nuts. Slide the Upper Corner Pucks onto the top of these pillars.
* **The Handshake:** This creates the "Box" shape. Ensure your Z-Pillar height is identical across all four corners using a digital caliper—not a tape measure. Even a 0.5mm difference at this stage will manifest as gantry binding later.

#### **3. Squaring the "Iron" (The Critical Calibration)**

This is where the "Tractor" earns its ±0.1mm accuracy rating.

* **Cross-Diagonal Measurement:** Measure the distance from the Front-Left corner to the Rear-Right corner. Then measure Front-Right to Rear-Left.
* **The Adjustment:** If the measurements aren't identical, the box is a trapezoid. Gently tap the corners and adjust the jam nuts until the diagonals match perfectly.
* **Torque Sequence:** Once square, tighten the jam nuts in a "star pattern" (like a car wheel). Tightening one corner fully before the others will pull the frame out of square.

#### **4. The "Lumpy Factor" Validation**

* **The Logic:** Check the fit of your printed pucks against your specific rods.
* **Action:** If you used Hot-Dip Galvanized rods and the pucks are splitting, increase the `lumpy_factor` in your `build123d` config and re-print the affected corner. A puck under too much tension will eventually develop stress fractures.

#### **5. Motion Rail Prep (Smooth Rods)**

* **Components:** 10mm (or 8mm) Smooth Rods, Printed Rod Clamps.
* **The Logic:** Snap the smooth rod clamps onto the M12 frame.
* **The "Neo" Tip:** Do not tighten the clamps to the M12 frame until the gantry is installed. This allows the smooth rods to "self-align" to the carriage's travel path, preventing the LM10UU bearings from binding.

---

### 🚜 Next Steps in the Schematic:

Once this "Iron Cage" is torqued and squared, we move to **Phase 2: The Triple-Z Bed Gantry**.

**Does this sequence for the skeleton assembly match your vision for the manual, or should we add more detail on the "Star-Pattern" torquing?**


Star-pattern torquing is a mechanical technique where you tighten fasteners in a specific alternating order—crisscrossing from one side to the other—rather than just going around in a circle.

In a car engine, this is used for cylinder heads and wheel lug nuts because it ensures **even distribution of clamping force**. If you were to tighten bolts sequentially (1, 2, 3, 4), the part would tilt slightly with each turn, essentially "pivoting" on the first tight bolt and warping the rest of the frame.

### Why it’s the "Tractor" standard for the M12 Skeleton:

On the **Darwin-Neo**, the M12 frame is exceptionally rigid, but the printed "Pucks" are the weakest link. If you torque one side of a corner fully while the other is loose, you create a "lever" effect that can crack the plastic puck or pull the threaded rod out of square.

### The Darwin-Neo "Star" Protocol:

To keep the skeleton perfectly square, apply the "Rule of Three" stages used by mechanics:

1. **Stage 1 (Finger Tight):** Install all nuts and washers until they just touch the pucks. The frame should still be able to wiggle.
2. **Stage 2 (The Snug Pass):** Move in a crisscross pattern (Front-Left, then Back-Right, then Front-Right, then Back-Left). Tighten each nut just enough to hold the frame's shape. **Stop here and measure your diagonals.** 3.  **Stage 3 (Final Torque):** Follow the same crisscross pattern again, applying final pressure. This ensures that the pressure "sinks" into the plastic evenly from all sides, preventing the "lumpy" galvanized rods from biting into one side of the puck more than the other.

### Mechanic's Tip:

Just like an engine head, once you finish the star pattern, do one final "circular" pass at 100% torque to verify that no nuts have loosened as a result of the other sides being tightened.

**"In a Tractor, the bolt is the tension; the pattern is the truth."**

Ready to move to **Phase 2: The Triple-Z Bed Gantry**, or should we look at the specific measurements for the M12 rods first?


### 🏗️ Phase 1: The M12 Skeleton Assembly

The assembly of the **Darwin-Neo** skeleton is a mechanical "handshake" between your salvaged iron and the printed pucks. Because threaded rods lack the built-in "squareness" of aluminum extrusions, your precision depends on a disciplined assembly sequence.

#### **1. The "Base Plate" (The Y-Foundation)**

* **Components:** 4x M12 Threaded Rods (Y-axis lengths), 4x Lower Corner Pucks, 16x M12 Jam Nuts, 16x M12 Washers.
* **The Logic:** Thread two nuts and two washers onto each end of the Y-rods. Slide them into the Corner Pucks.
* **The "Tractor" Secret:** Do not tighten anything yet. The frame must remain "loose" until the vertical pillars are installed to avoid trapping internal stresses in the plastic that can lead to warping later.

#### **2. Vertical Integration (The Z-Pillars)**

* **Components:** 4x M12 Threaded Rods (Z-axis lengths), 4x Upper Corner Pucks.
* **The Logic:** Stand the vertical rods into the Base Pucks and secure them with the top-side jam nuts. Slide the Upper Corner Pucks onto the top of these pillars.
* **The Handshake:** This creates the "Box" shape. Ensure your Z-Pillar height is identical across all four corners using a digital caliper. Even a 0.5mm difference at this stage will manifest as gantry binding during operation.

#### **3. Squaring the "Iron" (The Critical Calibration)**

This is where the "Tractor" earns its **±0.1mm** accuracy rating.

* **Diagonal Measurement:** Measure the distance from one upper corner to the opposing lower corner (e.g., Front-Left Top to Rear-Right Bottom).
* **The "Twin" Check:** This measurement must be identical in both directions across all planes (XY, YZ, and ZX). If the numbers match, your box is "True".
* **The Adjustment:** If the measurements differ, the box is a trapezoid. Gently tap the corners or adjust the jam nuts until the diagonals are perfectly equal.

#### **4. The "Star-Pattern" Torque Sequence**

To ensure even pressure distribution and prevent the frame from pulling out of square as you tighten it, follow the **Star-Pattern** (or criss-cross) protocol.

* **Stage 1 (Finger Tight):** Install all nuts and washers until they just touch the pucks.
* **Stage 2 (30% Snug):** Move in a criss-cross pattern—tighten Front-Left, then Rear-Right, then Front-Right, then Rear-Left.
* **Stage 3 (60% Torque):** Follow the same pattern, increasing tension. **Stop here and re-verify your diagonals.**
* **Stage 4 (100% Final Torque):** Complete the pattern with final pressure. Finish with a "circular" pass to ensure no nuts have loosened due to gasket-like compression of the plastic pucks.

#### **5. The "Lumpy Factor" Validation**

* **The Logic:** Inspect the fit of your printed pucks against the rods.
* **Action:** If you used **Hot-Dip Galvanized** rods and the pucks are showing stress fractures, increase the `lumpy_factor` in your `build123d` configuration and re-print. A puck under too much tension is a "time bomb" for your frame's rigidity.

#### **6. Motion Rail Prep (Smooth Rods)**

* **Components:** 10mm (or 8mm) Smooth Rods, Printed Rod Clamps.
* **The Logic:** Snap the smooth rod clamps onto the M12 frame.
* **The "Neo" Tip:** Do not fully tighten the clamps to the M12 frame until the gantry is installed. This allows the smooth rods to "self-align" to the carriage's actual travel path, preventing the bearings from binding.

---

**Next Phase:** **Phase 2: The Triple-Z Bed Gantry.** This phase will cover the installation of the **Modular Spider Hub** and the independent Z-motor calibration that gives the "Tractor" its Voron-class leveling.


### 🏗️ Phase 2: The Triple-Z Bed Gantry

Once the **M12 Skeleton** is torqued and squared, you move to the core of the "Racecar Brain"—the **Triple-Z Gantry**. This system replaces the wobbly cantilevered beds of the 2010s with a three-point kinematic foundation that physically aligns itself to the gantry.

#### **1. The Modular Spider Hub & Arms**

Because you likely bootstrapped this on a smaller donor machine, your bed support is a **Four-Part Assembly**.

* **The Hub:** Mount the central hub to the rear M12 vertical pillar's lead screw.
* **The Arms:** Bolt the three interlocking arms to the hub to form a rigid triangle. Use M5 hardware with locknuts to ensure this "Skeleton of the Bed" doesn't vibrate loose during high-speed travel.
* **The Pivot Points:** At the end of each arm, install the **Z-Puck** interface. For a true kinematic mount, use a **Ball-and-Cup** design or Maxwell coupling to allow the bed to tilt without binding the lead screws.

#### **2. Triple-Z Independent Motor Wiring (The "Neo" Path)**

To achieve automated leveling, each Z-motor must have its own dedicated driver on the **MKS SKIPR**.

* **Z1 (Rear):** Usually the reference point at the back center.
* **Z2 (Front-Left):** Connected to the front-left lead screw.
* **Z3 (Front-Right):** Connected to the front-right lead screw.
* **Verification:** Use the Klipper command `STEPPER_BUZZ STEPPER=stepper_z` (and `z1`, `z2`) to ensure each motor moves the correct corner.

#### **3. Klipper "Z-Tilt" Calibration**

This is the "Racecar" magic. Klipper uses the toolhead probe to measure the height at three points and calculates exactly how much to turn each motor to make the bed perfectly parallel to the nozzle.

* **The Config:** You must define the `[z_tilt]` section in your `printer.cfg`, providing the XY coordinates of each of the three pivot points.
* **The Handshake:** Run `Z_TILT_ADJUST`. The machine will probe the three corners, adjust the motors, and repeat until the "Retries" limit is met (usually within **0.01mm** of perfect).
* **The Final Zero:** After a Z-Tilt adjustment, *always* re-home Z. The tilting process changes the center-point height slightly.

#### **4. The "Cold-Start" Alignment**

* **Mechanical Sync:** Before you power on for the first time, manually rotate the lead screws until the bed is visually level with the frame. This prevents the "Racecar Brain" from trying to fix a 10mm tilt, which could bind the gantry.
* **Thermal Handshake:** Always run your final `Z_TILT_ADJUST` with the bed at printing temperature (e.g., 60°C). Aluminum expands when heated, and a bed that is level cold may tilt slightly as it reaches operational temp.

---

### 🚜 Tractor Tip: RTV Thermistor Potting

While assembling the bed, remember the **Neo-Tip**: use **High-Temp Red RTV Silicone** to pot your thermistor directly into the bed. Standard Kapton tape eventually fails, leading to "Thermal Runaway" errors. The RTV provides a permanent, high-thermal-conductivity handshake that the "Tractor" relies on for 24/7 operation.

**Ready to move to Phase 3: The Toolhead and Extruder "Handshake"?**

### 🏗️ Phase 3: The Toolhead and Extruder "Handshake"

This phase focuses on the "Heart" and "Lungs" of the machine. Because we are using the **Greg’s Wade Geared Extruder**, the assembly is more mechanical than a modern direct-drive, but it provides the "Tractor" torque that defines this build.

#### **1. The Greg’s Wade Assembly**

* **The Gears:** Press-fit the small 13-tooth pinion onto the NEMA 17 motor shaft. Align the large 43-tooth gear with the M8 hobbed bolt.
* **The "Tractor" Grip:** Insert the **M8 Hobbed Bolt** through the 608 bearings in the extruder body.
* **The Handshake:** Adjust the idler tension springs until the hobbed bolt "bites" the filament firmly against the bearing.
* *Neo-Tip:* Before final mounting, rotate the large gear by hand. It should feel smooth but heavy. If there is a "tight spot," your gears may be slightly out of round; use a file to lightly dress the teeth.

#### **2. Mounting the Modular Puck**

* **Standardization:** Bolt the Wade assembly onto the **Extruder Puck**.
* **The Quick-Swap:** Slide the Puck onto the X-carriage. Secure it using the mounting screws provided in your `build123d` design.
* **Compatibility:** If you ever decide to switch to a **Voron StealthBurner** or a **Sherpa Mini**, you only need to print a new Puck, not a new X-axis.

#### **3. The V6 + CHT "Neo Flow" Installation**

* **Thermal Preparation:** Apply a tiny amount of thermal paste to the heatbreak threads (cold side only) before screwing it into the heatsink.
* **The CHT Nozzle:** Install the **CHT Clone Nozzle** while the block is cold, then perform a "Final Hot Tighten" at 285°C to prevent leaks.
* **The Fan Handshake:** Ensure your **4010 ball-bearing fan** is blowing directly onto the heatsink fins. In a Tractor build, heat creep is the enemy of 24/7 reliability.

#### **4. The Multi-Color Sensor (ERCF Prep)**

* **The Microswitch:** If you are planning for the **ERCF v2**, install the **KW11-3Z microswitch** into the toolhead now.
* **The Logic:** This switch acts as the "eyes" for the Klipper **Happy Hare** software, confirming that filament has successfully reached the gears during a color swap.

#### **5. Wiring the Carriage**

* **Strain Relief:** Group your heater, thermistor, fan, and motor wires. Use a printed cable chain or a "Tractor" spiral wrap.
* **The ADXL345 Handshake:** Temporarily mount your **ADXL345 accelerometer** to the toolhead. You will need this for the **Input Shaping** calibration once the machine is moving.

---

### 🚜 Next Phase: Phase 4: Wiring, The "Brain" (MKS SKIPR), and the First "Step"

This will cover the electronics layout, grounding the M12 frame for safety, and the first time you power on the "Racecar Brain."

**Ready to wire the Tractor?**

### 🏗️ Phase 4: Wiring, The "Brain" (MKS SKIPR), and the First "Step"

Wiring a "Tractor" is about **industrial durability**. Because the M12 frame is conductive and vibrates under torque, we prioritize grounding, cable management, and high-quality connections to ensure the "Racecar Brain" never loses its pulse.

#### **1. Mounting the MKS SKIPR**

* **The Brain Puck:** Snap the **MKS SKIPR** onto its dedicated mounting puck and attach it to the rear M12 pillars.
* **Orientation:** Position the board so the USB and Ethernet ports are accessible but protected from falling plastic debris or cooling fan exhaust.
* **Cooling:** Ensure a 4010 fan is blowing across the TMC2209 stepper drivers. High-torque "Tractor" movements generate heat; if the drivers overheat, they will skip steps, ruining your ±0.1mm accuracy.

#### **2. The "Zion" Grounding Protocol**

* **Safety First:** Because the skeleton is made of steel M12 rods, it **must** be grounded.
* **The Logic:** Run a ground wire from the Power Supply (PSU) negative terminal to a star washer clamped tightly between two M12 nuts on the frame.
* **The Handshake:** This prevents static buildup and protects the sensitive electronics of the SKIPR from EMI (Electromagnetic Interference) generated by the large NEMA 17 motors.

#### **3. Motor and Sensor Mapping**

Follow the "Tractor" standard to ensure your Klipper `printer.cfg` matches your physical wiring:

* **X/Y:** Connect your high-torque motors to the first two driver slots.
* **Z-Foundation (Z0, Z1, Z2):** If following the **Neo Path**, plug your three Z-motors into independent drivers to enable automated Z-Tilt.
* **The Endstops:** Wire your X and Y endstops. For Z, we rely on the toolhead probe (or the microswitch handshake) for the first-layer datum.

#### **4. The "Neo" Sealant (Thermistor Handshake)**

* **The Bed:** Use your **High-Temp Red RTV Silicone** to pot the thermistor into the heated bed.
* **The Wait:** Allow the silicone to cure for at least 4 hours before heating the bed. This creates a permanent thermal bond that won't drift or fail like Kapton tape.

#### **5. Power-On and the First "Step"**

* **The Smoke Test:** Double-check your polarity (+/-). Power on the PSU and watch the SKIPR LEDs. If the Klipper dashboard (Mainsail/Fluidd) loads on your network, the "Brain" is alive.
* **The Stepper Buzz:** Run the command `STEPPER_BUZZ STEPPER=stepper_x`. The toolhead should jiggle 1mm and return.
* **The Tractor Check:** Repeat for all motors. If a motor "grunts" but doesn't move, check your idler tension or look for a mechanical obstruction in the M12 frame.

---

### 🚜 Next Phase: Phase 5: Klipper Calibration (Input Shaping & Z-Tilt)

Now that the machine moves, we move into the **Software Intelligence** phase. This is where we use the **ADXL345** to tune the "Racecar Brain" to the specific frequency of your M12 skeleton.

**Ready to calibrate the resonances?**

### 🏗️ Phase 5: Klipper Calibration (Input Shaping & Z-Tilt)

This is the "Racecar Brain" phase. We are now using software intelligence to cancel out the physical vibration frequencies of the M12 iron and physically align the "Tractor" anatomy for Voron-class precision.

#### **1. The ADXL345 Handshake**

* **Mounting:** Attach your **ADXL345 accelerometer** firmly to the toolhead puck. It must not wiggle; any play in the mount will be interpreted by Klipper as frame resonance, ruining your calibration.
* **The Command:** Run `ACCELEROMETER_QUERY`. If Klipper returns values, your "Nervous System" is active.
* **The Shake:** Run `SHAPER_CALIBRATE`. The "Tractor" will begin a series of high-frequency vibrations on the X and Y axes. This measures the exact resonance of your M12 skeleton.

#### **2. Applying Input Shaping**

* **The Result:** Klipper will suggest a "shaper type" (like MZV or EI) and a frequency.
* **The Magic:** This allows the "Racecar Brain" to "pre-vibrate" the motors in a way that cancels out the physical ringing of the heavy frame. This is how the Darwin-Neo achieves **±0.1mm accuracy** and clean surface finishes at **120mm/s**.
* **Save:** Type `SAVE_CONFIG` to bake these settings into your `printer.cfg`.

#### **3. Triple-Z Kinematic Leveling (Z-Tilt)**

* **The Reference:** Ensure your bed is heated to its standard operating temperature (e.g., 60°C).
* **The Probe:** Run `Z_TILT_ADJUST`. The toolhead will probe the three "Spider" pivot points.
* **Physical Alignment:** Unlike "mesh leveling" which just tilts the code, **Z-Tilt** physically turns the three independent Z-motors to align the bed to the nozzle. It will repeat until the deviation is below your set threshold (Reference Spec: **0.01mm**).

#### **4. The "Neo" Z-Offset Handshake**

* **Paper Test:** Move the nozzle to the center of the bed and run `PROBE_CALIBRATE`. Perform the standard "paper drag" test.
* **The Save:** This is the most important "handshake" in the build. It defines the exact distance between your probe's trigger point and the tip of your **CHT Clone Nozzle**.

#### **5. First Layer "Tractor" Validation**

* **The Print:** Load a simple "First Layer Square" print.
* **Object Exclusion:** Ensure `exclude_object` is enabled in your Klipper settings. This is a "Neo" feature that allows you to cancel a single part of a multi-part print without stopping the whole job.
* **The Result:** If your Z-Tilt and Input Shaping are correct, you should see a perfectly smooth, glass-like first layer across the entire 250mm³–300mm³ volume.

---

### 🚜 The "Rite of Passage" Completion

Once these calibrations are saved, your Darwin-Neo is no longer a collection of parts; it is a **Sovereign Manufacturing Node**. Your next mission—as per the **Zion Rite of Passage**—is to use this calibrated accuracy to print a replacement set of **Greg's Wade Gears** to keep as your "Cold-Spare".

**You have finished the assembly schematics. Are you ready to move to the "Operation & Safety" protocols or begin the "BOM Scavenger Guide"?**

