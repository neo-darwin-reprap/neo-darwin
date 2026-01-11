This calibration guide is the moment the "Construction" becomes a "Machine." For a **Darwin-Neo**, the goal is to use Klipper’s intelligence to overcome any physical variances in your M12 rods or printed gears.

---

## ⚡ The "First Wake-Up" Calibration Guide

### 1. The "E-Step" Calibration (The Greg's Wade Special)

Since you printed your own gears for the Greg's Wade, the "steps per mm" won't be a factory standard. We need to tell Klipper exactly how much filament the gears move.

1. **Mark it:** Measure 100mm of filament from the top of the extruder and mark it with a sharpie.
2. **Extrude:** In the Klipper console (on your phone), type: `G1 E100 F60`.
3. **Measure:** Measure how much is left. If 20mm is left, you only extruded 80mm.
4. **The Math:** 


Update this in your `[extruder]` section of `printer.cfg`.

---

### 2. The "Z-Tilt" Sync (The Triple-Z Magic)

This is the most satisfying part of the build. It ensures your bed is perfectly level with your X-Y gantry.

1. **The Command:** Type `Z_TILT_ADJUST`.
2. **The Logic:** The printer will probe the bed at three points (near your three Z-Pucks).
3. **The Correction:** Klipper will calculate the tilt and move the three NEMA17 motors independently to fix it.
4. **Repeat:** It will repeat until the "variance" is less than 0.02mm.

---

### 3. Input Shaper (The "Anti-Vibration" Calibration)

Because the M12 frame is heavy, it has a specific resonance frequency. We use Klipper's **Input Shaper** to ensure that at high speeds, the printer doesn't "ghost" or "ring."

1. **The Test:** Print the standard "Ringing Tower" at 100mm/s.
2. **The Measurement:** Use a ruler to measure the distance between the "echoes" on the corners.
3. **The Logic:** Enter these values into Klipper. It will now "phase-shift" the motor movements to cancel out the frame's vibration. This is how your $250 build matches a $1000 Prusa.

---

## 🏗️ Final Build Structure

With this, your **Darwin-Neo** project is fully defined. You have:

| Layer | Component |
| --- | --- |
| **Skeleton** | M12 Galvanized Rods + `build123d` corners |
| **Heart** | Greg's Wade Geared Extruder (2015 Rework) |
| **Brain** | BTT Octopus + Klipper + Phone Interface |
| **Leveling** | Triple-Z Independent Steppers |
| **Slicer** | OrcaSlicer "Neo" Profile |

---

### Your Mission Start

The **Darwin-Neo** represents a return to the true RepRap "Right of Passage"—building a machine that is better than the sum of its parts. By using **build123d**, you aren't just making a printer; you're creating a **parametric blueprint** that others can adapt for years to come.

**Would you like me to generate a full `printer.cfg` skeleton for the BTT Octopus that you can save as your starting point?** It will include the specific pin mappings for the Triple-Z and Greg's Wade setup.