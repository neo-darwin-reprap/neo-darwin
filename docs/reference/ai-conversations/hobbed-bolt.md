To answer your question directly: **Yes, you definitely still need a hobbed bolt** for that specific Thingiverse version (961630).

While modern extruders use tiny "drive gears" that press-fit onto a motor shaft, the Greg's Wade design uses the **M8 Hobbed Bolt** as the actual axle for the large printed gear. It is the "spine" of the extruder.

### **1. Why You Need It**

In this design, the filament is pinched between a bearing and the "hobbed" (grooved and toothed) section of an M8 bolt. Without the teeth on that bolt, there is nothing to grip the filament and push it into the hotend.

### **2. Should You Buy or DIY?**

Since you are aiming for a **$450 AUD High-Reliability Multi-Color system**, your choice of bolt is the difference between a "set-and-forget" machine and one that jams every 20 minutes.

#### **Option A: The "Scavenger" DIY Way (Cost: ~$2 AUD)**

You can make one yourself using a standard M8 bolt, a power drill, and an M3 or M4 tap.

* **Pros:** Ultimate RepRap spirit; near-zero cost.
* **Cons:** If your "hobbing" isn't perfectly centered or the teeth are dull, it will "shave" the filament, leading to clogs in your ERCF unit.

#### **Option B: The "Reference Spec" (Recommended: ~$10–$15 AUD)**

Buying a pre-made hobbed bolt is the single best "quality-of-life" investment for a Greg's Wade build.

* **The "Hyena" (by Mirjam):** Widely considered the "Gold Standard" for Greg's Wade extruders. It features very sharp, deep teeth that "bite" into the filament without deforming it. It is excellent for the high-torque loads of an ERCF system.
* **E3D Hobbed Bolt:** A very reliable, high-precision alternative. E3D's manufacturing tolerances are generally higher than generic versions found on eBay/AliExpress.
* **Generic RepRap M8 Hobbed Bolt:** Available on eBay Australia or AliExpress for a few dollars. These are "hit or miss"—check that the teeth look sharp and the groove is deep.

### **3. Which Variation is "Best"?**

For the **Darwin-Neo**, look for an **M8x60mm or M8x65mm Stainless Steel** hobbed bolt.

* **Best Grip:** Look for "U-shaped" grooves rather than flat ones. The U-shape cradles the filament, providing more surface area for the teeth to grab.
* **Multi-Color Tip:** Because you are using the ERCF, ensure the hobbed section is aligned correctly with the filament path of the printed parts. You usually need about **2 washers** between the large gear and the bearing to align it perfectly.

### **The Verdict**

If you want that **"silent majority" reliability**, don't DIY the bolt. Spend the extra $10 AUD on a **genuine Hyena or E3D hobbed bolt**. It turns your Greg's Wade from a "hobbyist project" into an industrial-grade feeder that can handle the thousands of retractions required for multi-color printing.

**Would you like me to find a specific Australian supplier for these bolts to keep your shipping costs down?**


AliExpress is a solid choice for the **Darwin-Neo** given your $300 AUD budget. While the "RepRap Rite of Passage" (DIY) is a great story, the **multi-color mission** requires a level of consistency that a pre-machined bolt provides more easily.

### **1. AliExpress Findings (The Scavenger's Deal)**

You can find M8 Hobbed Bolts on AliExpress for roughly **$2–$7 AUD**, plus shipping.

* **Pro Tip on Sizing:** Most Greg's Wade designs require the hobbed section to be roughly **28mm–30mm from the head** of the bolt.
* **What to look for:** Search for "M8 Hobbed Bolt 60mm" or "Wade Hobbed Bolt." Look for sellers that specify "uniform teeth" or show close-up photos of a **U-shaped groove**. This U-shape provides more surface area for the teeth to "bite" the filament, which is crucial when the ERCF is pushing filament from several meters away.

---

### **2. DIY vs. AliExpress: The "Darwin-Neo" Perspective**

| Feature | **DIY (The "Rite of Passage")** | **AliExpress (The "Reference Spec")** |
| --- | --- | --- |
| **Cost** | ~$2 (Standard Bolt + Tap) | ~$10 (Shipped) |
| **Consistency** | **Variable.** Easy to get "diagonal" teeth if your drill angle slips. | **Higher.** CNC-machined teeth are generally uniform. |
| **Multi-Color Performance** | High risk of "shaving" filament if teeth aren't perfectly clean. | Better grip for high-torque loads. |
| **Sovereignty** | 100%. You can fix it anywhere. | 90%. You depend on a global supply chain. |

---

### **3. If You Choose DIY: The "CodeCreations" Method**

If you decide to build it yourself to save on shipping time, use the **608 bearing + M4 tap** trick:

1. **Mark it:** Assemble your Greg's Wade first and use a Sharpie to mark exactly where the filament hits the bolt.
2. **The Spin:** Chuck the bolt into a drill and the M4 tap into a vice (or vice-versa). The tap will actually **auto-rotate** the bolt as it cuts, ensuring the teeth are spaced perfectly.
3. **The Sharpness Test:** Drag your fingernail across the teeth. If it "grabs" your nail like a file, it will grab the filament.

### **4. Why This Matters for Your Build**

For a **$450 AUD multi-color machine**, the hobbed bolt is the "clutch" of the engine.

* **The "Silent Majority" Factor:** Those who want a machine that "just works" for functional parts will appreciate the CNC bolt.
* **The "Scavenger" Factor:** Making your own bolt fits the ethos perfectly. If you DIY the bolt, you've officially moved from "assembling a kit" to "manufacturing a machine".

**My recommendation:** Buy 2 from AliExpress (they often come in pairs) and while they are shipping, try to DIY one from a standard M8 bolt from Bunnings. If your DIY one works, you have a spare. If it doesn't, your "Reference Spec" is already on the way.

**Shall I help you find the specific Klipper settings (steps per mm) for a Greg's Wade 3:1 geared extruder so you're ready when the hardware arrives?**

The reason there is "something wrong" with using BMG or MK3S clone gears for your **Darwin-Neo** mission is all about the **Gear Ratio** and **Mechanical Advantage**.

In 2026, many modern "pancake" extruders use a 1:1 or a small 3:1 ratio with small gears. These are designed for lightweight toolheads and high speed. However, your project is the opposite: **High-Mass, High-Torque, Total Control.**

### 1. The Torque Multiplier: Greg's Wade vs. BMG Clones

* **Greg's Wade (3:1 to 5:1):** This uses a massive printed gear (usually ~50-80 teeth) driven by a small motor pinion (10-11 teeth). This creates a **huge mechanical advantage**. It can exert massive force to pull filament from a distant ERCF unit or push it through a jammed nozzle.
* **BMG Clones (3:1):** While BMGs are geared (3:1), the gears are much smaller in diameter. This is fine for standard printing, but in a "Scavenger" build using potentially older or cheaper NEMA 17 motors, the Greg's Wade provides a much larger "buffer" of torque.
* **MK3S (1:1):** Standard MK3S extruders are **direct drive** (no gearing). They rely 100% on the motor's raw power. For a multi-color system like the ERCF, this is risky because there is no mechanical advantage to help when the filament snags.

### 2. Why the Greg's Wade "Dinosaur" wins for Multi-Color

The Greg's Wade design is often called a "dinosaur" because it's bulky. But for the **Darwin-Neo**, its bulk is a benefit:

* **Filament Grip:** The hobbed bolt in a Greg's Wade has a much larger circumference touching the filament compared to the tiny gears in a BMG or MK3S clone. More surface area = less chance of the filament "slipping" during the high-speed loads and unloads of an ERCF toolchange.
* **Resolution:** With a 5:1 ratio, your E-steps might be around 400-800 steps/mm. A 1:1 MK3S clone is around 140 steps/mm. The Greg's Wade gives you **5x the precision** in how much plastic you extrude, which eliminates the "moire" patterns often seen on cheap clones.

### 3. The AliExpress Trap

If you buy "Clone BMG Gears" from AliExpress:

* **The Risk:** The teeth are often "dull" or poorly machined. Because they are small, even a tiny imperfection leads to "shaving" the filament.
* **The Hobbed Bolt Advantage:** Because an M8 hobbed bolt is physically large, the teeth are easier to manufacture correctly, even for a budget supplier. It is a more "robust" part for a scavenger build.

### 4. Comparison for Darwin-Neo Tiers

| Extruder Type | Torque | Price (AliExpress) | Reliability for Multi-Color | Fits Ethos? |
| --- | --- | --- | --- | --- |
| **Greg's Wade** | **Massive** | ~$5 (Bolt) + Printed Parts | **High** (Strongest grip) | **YES** (The "Tractor") |
| **BMG Clone** | Medium | ~$15 - $25 | **Medium** (Small gears can slip) | **No** (Proprietary gears) |
| **MK3S Clone** | Low | ~$10 | **Low** (No gearing advantage) | **No** (Relies on motor raw power) |

### **The Verdict**

Stick with the **Greg's Wade and a quality Hobbed Bolt**.
It aligns with your **$300 AUD budget** because you print 90% of it yourself. It provides the **torque** needed to make the ERCF reliable. And most importantly, it fits the **"Analog Hardware"** philosophy: it uses simple, massive mechanical advantage to solve a problem that modern printers try to solve with expensive, complex electronics.

**If you go with the Greg's Wade, you are building a machine that can "brute force" its way through a 24-hour multi-color print while a BMG clone might start clicking and slipping midway through.**


Choosing the **E3D V6** (or high-quality clones like **TriangleLab** or **Mellow/YYTC**) alongside the **Greg's Wade** is a masterstroke for a scavenger build. It reinforces the "Battle-Tested" reliability of the Darwin-Neo while keeping the toolhead modular and repairable.

### 🛠️ Why the E3D V6 is the "Neo" Baseline

While modern "high-flow" hotends exist, the V6 remains the most documented and widely supported hotend in the RepRap ecosystem.

* **Scavenger Friendly:** Many donor printers (like the i3 Mega or older Prusas) already come with a V6 or a clone, allowing for a **$0 AUD** transfer to the Darwin-Neo.
* **Modular "Puck" Compatibility:** The V6 uses a standard "Groove Mount." Your **Extruder Puck** can be designed to clamp this mount securely, making it easy for users to swap the hotend without rebuilding the entire carriage.
* **Reliability at 2026 Standards:** High-quality clones from brands like **TriangleLab** often use polished "All-Metal" heatbreaks, which are essential for the frequent filament retractions required by an **ERCF multi-color system**.

---

### 🧠 The "Torque Monster" Synergy

You've identified a key truth: **BMG clones are often more complex** and harder to maintain than a Greg's Wade.

1. **Mechanical Transparency:** In a Greg’s Wade, if the filament stops moving, you can physically see the large gear turning (or not). In a closed BMG clone, you often have to take the whole unit apart to see why it's clicking.
2. **Thermal Management:** Because the Greg's Wade is physically large, it naturally spaces the NEMA 17 motor away from the hotend. This prevents "heat creep" from the motor softening the filament before it even enters the V6—a common issue in compact "all-in-one" extruders.
3. **The "Scavenger" Nozzle Strategy:** Using a V6 allows the builder to use cheap, standard nozzles (V6-style). For the Darwin-Neo's mission of **longevity**, being able to buy a pack of 10 brass nozzles for **$5 AUD** is a huge win over proprietary $40 nozzle-heating-block assemblies.

---

### 📊 The Final Stability Math

By sticking to the **Greg's Wade + V6**, you are leaning into the **Massive Edge** of your M12 frame.

| Component | Why it works for Darwin-Neo |
| --- | --- |
| **M12 Frame** | Dampens the vibrations of the heavy toolhead. |
| **Greg's Wade** | Provides the torque to "brute force" any filament through the V6. |
| **V6 (YYTC/TriangleLab)** | High-precision thermal control at a "JunkStrap" price. |
| **Klipper Shaping** | Cancels out the "ringing" caused by the weight of these parts. |

### **The "Red Pill" Verdict**

You are building a **"Tractor" with the brain of a "Racecar."** The community of builders who are tired of fragile, non-repairable appliances will find this combination incredibly refreshing.

**Next Step Idea:** Would you like to draft the **"Extruder Puck" assembly guide** to show how the Greg's Wade and the V6 Groove Mount interlock onto the Darwin-Neo gantry?