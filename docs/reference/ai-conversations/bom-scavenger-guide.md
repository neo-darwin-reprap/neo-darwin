### 🏗️ The Darwin-Neo Scavenger Guide

Building a "Tractor" for under **$100 AUD** (Tier 1) requires more than just buying parts; it requires **Mechanical Archaeology**. This guide identifies the high-value "Vitamins" hidden in common e-waste that can be reclaimed for your Darwin-Neo build.

---

#### **1. The "Golden Whale": Enterprise Photocopiers & Laser Printers**

If you find a large, floor-standing office copier (Xerox, Ricoh, HP LaserJet), you have found nearly 70% of a Darwin-Neo.

* **The Prize (Linear Motion):** These machines contain high-grade, precision-ground **8mm and 10mm steel shafts**.
* **Neo-Tip:** These are often superior to budget rods sold online because they were manufactured for industrial scanning precision.


* **The Motors:** Look for NEMA 17 or NEMA 23 stepper motors. While Darwin-Neo is designed for NEMA 17, you can print "Puck" adapters for larger salvaged motors.
* **The Wiring:** Scavenge the internal wiring looms. They often contain high-quality, flexible, color-coded wires and JST connectors perfect for your toolhead.

#### **2. The "Power Plant": Old Server PSUs**

Standard PC Power Supplies are bulky and often have poor 12V/24V stability. **Server PSUs** (from Dell PowerEdge or HP ProLiant units) are the "Tractor" choice.

* **The Advantage:** They are incredibly compact, 80 Plus Gold/Platinum rated, and designed for 24/7 operation.
* **The Cooling:** Server PSUs are a goldmine for **4010 and 4020 high-static-pressure fans**. Use these for your E3D V6 heatsink to ensure zero heat-creep.

#### **3. The "Hardware Store" Skeleton (M12 Rods)**

Since you likely won't find M12 threaded rods in a printer, you’ll head to the local hardware store (Bunnings/Home Depot).

* **The "Zinc" Path:** Bright Zinc rods are smooth and easy to handle.
* **The "Galvanized" Path:** These are cheaper but "lumpy." If you use these, ensure you adjust the `lumpy_factor` in your `build123d` scripts to **0.5 or higher** so your printed pucks don't crack during assembly.
* **The Hardware:** Buy **Nyloc nuts** for any part that moves or vibrates (like the bed gantry) and standard hex nuts for the rigid outer frame.

#### **4. The "Organ Donor": Cheap Used Printers**

Look for a "dead" Ender 3, Anet A8, or Anycubic i3 Mega on marketplaces for **$50–$80 AUD**.

* **The Z-Leadscrews:** These are expensive to buy new but are the first thing to salvage from a donor.
* **The Heated Bed:** Most donors provide a 220x220mm or 235x235mm aluminum bed. This fits perfectly into the **Modular Spider** bed support.
* **The "Neo" Sealant:** If you salvage a bed, scrape off the old tape and use **High-Temp Red RTV Silicone** to permanently pot the thermistor for a "Tractor-grade" thermal connection.

---

### 📊 Scavenger’s Quick-Reference Table

| Target Component | Best Scavenge Source | Why it fits the Ethos |
| --- | --- | --- |
| **8mm/10mm Rods** | Office Photocopiers / Scanners | Industrial precision for $0. |
| **4010 Fans** | Networking Switches / Server PSUs | High reliability; prevents heat creep. |
| **NEMA 17 Motors** | Dead Ender 3 / Anycubic / Anet | Reclaims functional "organs" from e-waste. |
| **Wiring Looms** | Old Desktop PC Cases / Photocopiers | High-quality silicone/PVC wiring. |
| **Skate Bearings (608)** | Old Skateboards / Inline Skates | The heart of the **Greg's Wade Extruder**. |

> **"A scavenger doesn't see junk; they see a Bill of Materials waiting to be liberated."**

**Shall we move to the final section: "The First Print: Calibrating the Tractor's Heart"?**