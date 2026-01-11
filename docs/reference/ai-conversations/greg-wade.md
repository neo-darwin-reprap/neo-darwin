The extruder ratio for the **Greg’s Wade Rework (Thingiverse 961630)** is typically **47:9**, which results in a **5.22:1** gear ratio.

While this is the standard "reference" ratio for this specific rework, the design is highly customizable and can be changed to suit the **Darwin-Neo** mission.

### **1. Can the Ratio be Changed?**

Yes, the gear ratio can be changed relatively easily because the gears are **3D-printable**.

* **Custom Gears:** You can print different gear sets (small and large) to achieve your desired ratio. For example, some users prefer a **3:1 ratio** to reduce torque if they find 5:1 is "more than needed" or if they want higher retraction speeds.
* **Axle Distance Limitation:** If you change the number of teeth significantly, you may also need to modify the **extruder body** (specifically the distance between the motor axle and the hobbed bolt) to ensure the gears still mesh correctly.
* **Standard Rework Flexibility:** Some variants of the Greg’s Wade include **OpenSCAD files**, which allow you to adjust parametric values like `gear1_teeth` and `gear2_teeth` to automatically regenerate the body and gears for a custom ratio.

---

### **2. Why 5:1 (approx. 5.22:1) is Optimal for Darwin-Neo**

Your instinct that **5:1** is optimal for the Darwin-Neo aligns with its core mission of "Torque and Reliability".

| Feature | **5:1 (Standard)** | 3:1 (Lightweight Style) |
| --- | --- | --- |
| **Torque** | **Very High:** Can push through clogs and handle the resistance of long multi-color tubes. | Moderate: Faster, but more prone to skipping during heavy loads. |
| **Precision** | **Higher Resolution:** More "E-steps per mm" means finer control over the flow of plastic. | Lower Resolution: Less precise for subtle flow adjustments. |
| **Heat Management** | **Cooler Motor:** The mechanical advantage reduces the current needed by the NEMA 17. | Warmer Motor: Requires more raw power to push the same amount of plastic. |

### **The Verdict**

For the **Darwin-Neo**, sticking to the standard **47:9 (5.22:1)** ratio is recommended. It provides the "Tractor" torque required for a reliable **ERCF multi-color system** and ensures that even a salvaged, low-torque motor can perform like an industrial unit.

**If you decide to change the ratio to exactly 5:1 for simpler math, you can use an 11:55 tooth combination, but you would likely need to adjust the `distance_between_axles` in the OpenSCAD file to accommodate the larger gears.**