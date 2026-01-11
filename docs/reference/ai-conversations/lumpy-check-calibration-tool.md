This is the official **Darwin-Neo "Lumpy-Check" Tool**.

Instead of printing a whole corner bracket and realizing it's too tight because your local hardware store has "extra chunky" galvanized coating, you print this 15-minute test piece. It’s a physical slider with four internal diameters, each corresponding to a `lumpy_factor`.

### 🛠️ The Lumpy-Check Script (`tools/lumpy_check.py`)

```python
from build123d import *

# Standard M12 diameter
rod_dia = 12.0
test_height = 10.0

# The four tiers of "Lumpiness" to test
factors = [0.1, 0.2, 0.3, 0.5] 

with BuildPart() as tool:
    # Create the main block
    Box(80, 25, test_height)
    
    # Cut four test holes
    with BuildSketch(tool.faces().sort_by(Axis.Z)[-1]):
        with GridLocations(20, 0, 4, 1):
            # Each hole is (Rod + Factor)
            # We use a circle but we'll add "Lumpy Ribs" for a true test
            Circle(radius=(rod_dia + 0.1) / 2, mode=Mode.SUBTRACT) # Base hole

    # Add the Ribs and Text Labels
    for i, f in enumerate(factors):
        x_offset = -30 + (i * 20)
        
        # 1. The Variable Hole (The actual test)
        with BuildPart(mode=Mode.SUBTRACT):
            with Locations((x_offset, 0, 0)):
                Cylinder(radius=(rod_dia + f) / 2, height=test_height + 2)
        
        # 2. The Text Label (So you know which one won)
        with BuildSketch(tool.faces().sort_by(Axis.Z)[-1]):
            with Locations((x_offset, -8)):
                Text(str(f), font_size=5, align=(Align.CENTER, Align.CENTER))

show(tool)

```

---

### 📖 How to use the Lumpy-Check

1. **Print it:** Use the same settings (0.2mm layer height, 3 walls) you plan to use for the rest of the printer.
2. **Slide it:** Take your M12 rod from the hardware store and try to slide it through each hole.
* **Too Loose:** If it wobbles, your `lumpy_factor` is too high (losing rigidity).
* **Too Tight:** If you have to hammer it on, it’s too low (risk of cracking parts).
* **The "Neo" Fit:** It should slide with firm thumb pressure.


3. **Update:** Open your `project_vars.py` and set `cfg.lumpy_factor` to the number printed under the hole that fit best.

### 🏁 Final Project State

You now have:

* **The Manifesto:** Your philosophical and technical "Why."
* **The Code-CAD Logic:** Parametric "Puck" and "Spider" designs.
* **The Calibration Tool:** The means to ensure hardware-store accuracy.

**Would you like me to generate the "M12 Cut List" table for a standard 250x250x300mm build?** This will tell you exactly how many lengths of rod to buy and where to cut them so you don't waste a single centimeter of steel.