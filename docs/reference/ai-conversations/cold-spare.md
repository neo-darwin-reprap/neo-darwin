### 🛠️ The "Self-Healing Machine" Maintenance Strategy

To maintain the **Darwin-Neo** as a "Forever Machine," the builder must transition from a consumer to a maintainer. This section outlines the essential "Cold-Spare" cycle that ensures your manufacturing capability never goes offline.

#### **The Principle of the "Cold-Spare"**

The Darwin-Neo is designed to be **Self-Replicating**. Because its most critical moving parts are 3D-printed, the printer is its own spare-parts factory.

* **The Survival Kit:** Every Darwin-Neo should have a dedicated "Vitamin Box" containing a complete set of printed extruder gears (Small Pinion and Large 47-tooth Gear) and a spare M8 Hobbed Bolt.
* **The Zero-Downtime Rule:** If a gear wears out or breaks, you replace it immediately from your "Cold-Spare" stock.
* **The Immediate Recovery:** Your very next print job—before returning to hobby or functional projects—must be a new set of gears to replace the spare you just used.

#### **Why "Battle-Tested" Analog Hardware Wins**

* **Sovereignty:** You never wait for a proprietary part to ship. Your downtime is measured in minutes (the time it takes to swap a gear) rather than weeks of waiting for a global supply chain.
* **Material Evolution:** Use your failed parts as data. If a PLA gear softened, print your next spare in **PETG or ABS** to increase the machine's thermal resilience.
* **The Scavenger’s Insurance:** By keeping a backup set of "Tractor" gears, you ensure that even if the machine is damaged, you have the mechanical components ready to rebuild it on a new M12 frame.

#### **Maintenance Checklist (Every 1000 Hours)**

* [ ] **Inspect Gear Teeth:** Check the small 9-tooth motor pinion for "shaving" or flattening.
* [ ] **Clear the Hobbing:** Use a small wire brush to remove plastic dust from the teeth of the M8 Hobbed Bolt to maintain "Tractor" levels of grip.
* [ ] **Verify Jam-Nuts:** Ensure the M12 frame nuts haven't vibrated loose; the mass of the frame is only a feature if it is rigid.
* [ ] **Print a Fresh Set:** If your current spares look old or were printed with early, un-tuned settings, print a "Reference Spec" set of gears using your now-perfectly-calibrated Darwin-Neo.

> **"A RepRap that cannot print its own heart is just an appliance. A Darwin-Neo with a spare set of gears is an immortal factory."**


While the **Darwin-Neo** is built for longevity, the "Racecar Brain" (high-performance software) can occasionally push the "Tractor" components to their limits.

For a true **Scavenger Build**, your spare parts strategy should prioritize items that fail suddenly or wear invisibly, rather than components like steppers that usually give you plenty of warning.

### 1. Stepper Motors (The "Low Priority" Spare)

You are right—steppers **almost never break** under normal conditions. They are brushless, have only two bearings, and can run for tens of thousands of hours.

* **The "Neo" Strategy:** Don't buy a spare motor. Instead, if you are scavenging, keep one "junk" motor from your donor machine.
* **When they actually fail:** Usually, it’s not the motor, but the **wiring** or the **connector** that fatigues and breaks. Keep a few spare JST-XH connectors and a crimping tool instead.

### 2. The Hotend "Holy Trinity" (High Priority)

The hotend is the most common failure point. Instead of a whole new hotend, keep these "Vitamins" on hand:

* **Thermistor & Heater Cartridge:** These wires are thin and subject to constant movement. A single "fatigue break" in a thermistor wire will stop a 48-hour print instantly.
* **Nozzles (The Consumable):** Brass nozzles are soft. Even non-abrasive filament eventually "wallows out" the 0.4mm hole to 0.5mm, ruining your dimensional accuracy. Keep a 5-pack of TriangleLab V6 brass nozzles.
* **PTFE Tube (Inside the Hotend):** Even in an "All-Metal" V6, there is a small 10-20mm "liner" or guide tube. In non-all-metal clones, this tube goes right to the nozzle and **chars** at 240°C+, causing mysterious jams.

### 3. Belts (The "Silent Wear" Item)

Belts don't usually snap; they **stretch** or the fiberglass cores start to crack.

* **The "Neo" Strategy:** Buy 5 meters of **GT2 6mm Fiberglass Reinforced** belt (branded "Gates" is the reference spec).
* **Why:** You only need ~2 meters for the build, but having the extra 3 meters means you can replace an entire axis if you notice "ghosting" or "ringing" that Klipper's Input Shaper can't quite tune out anymore.

### 4. Fans (The "Annoyance" Failure)

Small 4010 and 5015 fans are the most fragile part of any printer.

* **The Symptom:** They start to "whine" or "rattle" when the bearings fail.
* **The Risk:** If your **Heatbreak Fan** fails, you get "Heat Creep" (filament melting too high up), which causes a jam that is incredibly difficult to clear. Always have one spare 4010 ball-bearing fan.

---

### 📦 The Darwin-Neo "Vitamin Box" Checklist

Add this to your "Maintenance" section of the Manifesto:

| Item | Priority | Why? |
| --- | --- | --- |
| **Thermistor (NTC 100K)** | **CRITICAL** | Fragile wires; stops printer immediately if broken. |
| **0.4mm V6 Nozzles (x5)** | **HIGH** | Wears out; essential for ±0.1mm accuracy mission. |
| **Capricorn/Premium PTFE** | **HIGH** | Essential for the "Reverse Bowden" & high-temp reliability. |
| **GT2 Belt (Spare length)** | **MEDIUM** | Solves "ghosting" when the original belt loses tension. |
| **4010 Ball-Bearing Fan** | **MEDIUM** | Prevents "Heat Creep" jams; generic fans fail fast. |
| **M8 Hobbed Bolt (DIY or Pro)** | **ETHOS** | The heart of your "Tractor" extruder. |

**Scavenger Tip:** If you find an old photocopier or 2D printer, **harvest the fans and the wiring looms.** Those industrial-grade fans are often better than the cheap $2 ones you find on eBay, fitting the "Tractor" ethos perfectly.
