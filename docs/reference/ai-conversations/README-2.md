# 🏗️ Darwin-Neo: The 2026 RepRap Manifesto

**High-Performance. Parametric. Minimalist. Industrial.**

Darwin-Neo is a reimagining of the original [RepRap Darwin](https://reprap.org/wiki/Darwin) (2007). It takes the "threaded-rod-box" soul of the first RepRap and updates it with 20 years of mechanical engineering, Code-CAD logic, and Klipper-driven intelligence.

> **The Goal:** Match or exceed the print quality of a Bambu Lab A1 or Prusa MK4 for under $200 (using a donor printer) with a significantly larger build volume.

---

## 💎 The "Industrial Chic" Philosophy

We don't hide the hardware. We use it.

* **The Skeleton:** M12 Galvanized Threaded Rods. Heavy, rigid, and dirt cheap at any hardware store.
* **The Brain:** BTT Octopus + Raspberry Pi (or old phone/tablet).
* **The Leveling:** Triple-independent Z-axis. Software (Klipper) corrects hardware imperfections in real-time.
* **The Code:** Fully parametric design using **build123d**. Change one variable to swap from M8 to M12 or to resize the entire machine.

---

## 🛠️ The "Big Three" Parametric Variables

Unlike standard STLs, Darwin-Neo is generated via Python. You only need to touch `config.py`:

1. **`ROD_DIA`**: (8, 10, 12, or 12.7mm) — Adjusts every hole and nut-trap in the system.
2. **`BED_TYPE`**: (Ender3, MK52, or Custom) — Adapts the Y-carriage and frame width to your donor bed.
3. **`BUILD_HEIGHT`**: Define your Z-travel. The script generates the exact rod "Cut List" for you.

---

## 🚀 The Quality Secret: The "Software Fix"

We don't rely on precision-machined aluminum extrusions. We rely on math.

* **Z-Tilt Adjust:** 3 independent motors align the bed to the nozzle automatically.
* **Input Shaping:** Klipper measures the resonance of the heavy M12 frame and cancels out ghosting.
* **OrcaSlicer Integration:** Native Klipper profiles provided. Drag, drop, and print from your phone.

---

## 📦 Getting Started

1. **Source a Donor:** Find a broken Ender 3, Anet A8, or similar. You need the motors, the bed, and the rods.
2. **Go to the Hardware Store:** Buy 12 meters of M12 threaded rod and 100+ nuts/washers.
3. **Run the Script:** Install `build123d`, set your variables, and generate your STLs.
4. **Assemble & Flash:** Use the provided `printer.cfg` to get your BTT Octopus talking to Klipper.
