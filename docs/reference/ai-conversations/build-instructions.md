This **"Zion Construction Sequence"** is designed to prevent the most common frustration in threaded-rod builds: the "Trapped Nut" problem. Because every M12 rod will hold multiple parts, the order of operations is critical.

By following this sequence, the maker builds from the **inside out**, ensuring that every motor, puck, and carriage is "loaded" onto the rods before the frame is locked down.

---

## 🏗️ The Zion Construction Sequence

### Phase 1: The "Z-Matrix" (Bed & Vertical Support)

Before the frame exists, we build the Z-axis, as it is the most difficult to align.

1. **Prep the Z-Rods:** Take your 4 vertical M12 rods.
2. **Load the Z-Pucks:** Slide your **3 skeletonized Z-Nut Housings** onto the rods.
3. **Install Leadscrews:** Bolt the donor T8 brass nuts into your Z-Pucks and thread the M8 leadscrews through them.
4. **The Base:** Attach the 4 bottom **Universal M12 Corners**.
> **Neo-Tip:** Leave the nuts finger-tight. You will "tune" the squareness later using Klipper's measurements.



---

### Phase 2: The X-Y Gantry (The Movement Heart)

This is where the "24mm spacing" comes into play.

1. **The X-Subassembly:** Slide your **Neo-Carriage** onto the two 8mm smooth rods.
2. **End Blocks:** Press the **X-Motor Mount** and **X-End Idler** onto the ends of those smooth rods.
3. **The Y-Rods:** Slide this entire "H-bridge" onto the Y-axis smooth rods.
4. **Motor Nodes:** Attach your **Y-Axis Motor Mounts** to the horizontal M12 frame rods.

---

### Phase 3: Closing the Cage (The Frame)

Now we lock the geometry.

1. **Horizontal Union:** Connect the X-Y gantry assembly to the 4 vertical Z-rods using the remaining M12 rods.
2. **The "Greg's Wade" Drop-In:** Bolt your 3D-printed **Greg’s Wade Extruder** (the jzkmath rework) onto the carriage.
3. **Squaring the Matrix:** Use a simple ruler to ensure the distance between the rods is identical at the top and bottom.
> **Note:** Because we are using 12mm rods, once you tighten these nuts, the frame will be more rigid than any Ender 3.



---

### Phase 4: The Nervous System (Wiring & Klipper)

Minimalism is the goal.

1. **The Umbilical:** Gather the motor, heater, and sensor wires from the head. Wrap them in a single tech-flex sleeve.
2. **The Octopus:** Mount the **BTT Octopus** to the back of the frame using a printed "Matrix Plate."
3. **The Phone Link:** Power up the Pi, connect your old phone to the Wi-Fi, and open the Mainsail interface.

---

## 💾 Final Code: The "BOM" Reality Check

To finish your **build123d** project, here is a snippet you can add to your `main.py` to print your final "Shopping List" before the maker goes to the hardware store.

```python
# main_build.py snippet
def print_final_bom():
    print("--- DARWIN-NEO SHOPPING LIST ---")
    print(f"M12 Threaded Rod: {cfg.total_rod_meters} meters")
    print(f"M12 Hex Nuts: {BOM.count('M12 Nut')}")
    print(f"M12 Washers: {BOM.count('M12 Washer')}")
    print(f"Donor Parts Needed: NEMA17s (x6), T8 Leadscrews (x3), Heatbed (x1)")
    print("--------------------------------")

# Call this at the end of your script
print_final_bom()

```

---

### Your Final "Right of Passage"

The first thing you should do is print **one** M12 corner and **one** Z-Puck. Test the fit on a piece of Bunnings rod. If it's too tight, change the `lumpy_factor` in your `project_vars.py` and re-export.
