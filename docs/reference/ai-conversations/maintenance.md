In the context of the **Darwin-Neo**, your maintenance strategy should focus on **active print time** rather than total "uptime." Since the machine is built for longevity and reliability, Klipper is the perfect tool to track the "mileage" of your tractor components.

### How it tracks your "Mileage"

Klipper tracks statistics in the background using the `[statistics]` or `[idle_timeout]` modules. Specifically, the Darwin-Neo can monitor:

* **Total Print Time:** This is the most critical metric for the "Vitamin Box" strategy, as it correlates directly with gear wear and fan bearing failure.
* **Filament Extruded:** Since the **Greg's Wade** extruder is your "heart," tracking meters of filament through the **M8 Hobbed Bolt** is a great way to know when to brush out plastic dust.
* **Axis Travel:** Klipper can track how many kilometers each motor has traveled, which helps you predict when a **GT2 Belt** might start losing its tension.

### The "MAINTENANCE_CHECK" Macro

Instead of checking a dashboard, you can build a macro that acts like an "Oil Change" light for your printer. Every 1,000 hours of active printing, Klipper can interrupt the start-up sequence with a console message.

```jinja2
[gcode_macro CHECK_MAINTENANCE]
gcode:
  {% set total_time = printer.save_variables.variables.total_print_time|default(0) %}
  {% if total_time > 1000 %}
    {action_respond_info("🚜 TRACTOR ALERT: 1000 Hours Reached.")}
    {action_respond_info("1. Inspect Greg's Wade Pinion for shaving.")}
    {action_respond_info("2. Clear the M8 Hobbed Bolt teeth.")}
    {action_respond_info("3. Check 'Vitamin Box' for fresh spare gears.")}
  {% endif %}

```

### Why Uptime is Irrelevant

In the **Neo** philosophy, "uptime" (time the board is simply powered on) is a "Racecar" metric that doesn't affect "Tractor" wear. A printer sitting idle doesn't wear out its **0.4mm V6 Nozzle** or stretch its **Fiberglass Reinforced Belts**. By tracking **Print Time**, you ensure your maintenance intervals are based on actual mechanical fatigue.

**Would you like me to draft the "Klipper Statistics" configuration section so your machine can start counting its first 1,000 hours?**