# 📋 Darwin-Neo Bill of Materials (BOM)

This list is categorized by assembly stage. Check the **[ ]** boxes as you acquire or salvage each part.

## 🏗️ 1. The Skeleton (M12 Frame)

*Standard for all Tiers.*

* [ ] **M12 Threaded Rod:** 4–5 meters total (Cut to size per `config.py`).
* [ ] **M12 Hex Nuts:** ~60 pieces (Zinc or Galvanized).
* [ ] **M12 Washers:** ~60 pieces.
* [ ] **Printed Corners:** 8x M12 Corner Pucks.

---

## ⚙️ 2. The Motion Fork (Choose ONE Path)

### **Path A: The Scavenger (Salvaged Rods)**

* [ ] **Smooth Rods:** 6x (Salvaged 8mm or 10mm).
* [ ] **Bearings:** 12x (Salvaged LM8UU or LM10UU).
* [ ] **Printed Parts:** Set `SMOOTH_ROD_DIA = 8.0` in script.

### **Path B: The Neo Standard (Upgrade to 10mm)**

* [ ] **10mm Hardened Steel Rods:** (2x 370mm, 2x 350mm, 2x 320mm).
* [ ] **LM10UU Linear Bearings:** 12x.
* [ ] **Printed Parts:** Set `SMOOTH_ROD_DIA = 10.0` in script.

### **Path C: The Tinker (Linear Rails)**

* [ ] **MGN12H Linear Rails:** 6x (Lengths as above).
* [ ] **MGN12H Carriage Blocks:** 6x–12x.
* [ ] **Printed Parts:** Use "Rail-Puck" variants.

---

## ⚡ 3. The Organs (Electronics & Drive)

* [ ] **Lead Screws:** 3x T8 Lead Screws (Salvage 1, Buy 2 for Triple-Z).
* [ ] **NEMA 17 Stepper Motors:** - [ ] 4x Salvaged (X, Y, Z, E).
* [ ] 2x New High-Torque (Recommended for X/Y if doing Triple-Z).


* [ ] **Brain:** - [ ] **Option A:** MKS SKIPR (Integrated Klipper).
* [ ] **Option B:** Donor Board + Raspberry Pi / Old Laptop.


* [ ] **ADXL345 Accelerometer:** 1x (Crucial for Input Shaping).
* [ ] **Power Supply:** 1x 12V or 24V (Salvaged from donor).
* [ ] **Heated Bed:** 1x (Salvaged 220mm–235mm bed).

---

## 🦷 4. The Heart (Greg's Wade Extruder)

* [ ] **Motor:** 1x NEMA 17 (Salvaged).
* [ ] **Drive Bolt:** 1x M8 Hobbed Bolt (or DIY notched bolt).
* [ ] **Bearings:** 3x 608 "Skate" Bearings.
* [ ] **Hardware:** Assorted M3/M4/M8 bolts (Hardware store).
* [ ] **Printed Parts:** Large Gear, Small Gear, Body, Idler.

---

## 🛠️ 5. Small Hardware & Consumables

* [ ] **GT2 Belt:** ~3–5 meters.
* [ ] **GT2 Pulleys:** 2x (for X/Y motors).
* [ ] **Flexible Couplers:** 3x (5mm to 8mm for Lead Screws).
* [ ] **Jumper Wires / Looming:** To extend donor wiring for the larger frame.

---
