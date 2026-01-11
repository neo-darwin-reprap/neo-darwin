from build123d import *

# Config
lead_screw_nut_holes = 16.0  # Spacing for T8 nut screws
rod_dia = 12.2               # M12 Smooth rod clearance
bearing_dia = 15.0           # LM10UU for the guide rods

with BuildPart() as z_bracket:
    # 1. The Main Body (The "Wing")
    # Designed to bridge the Lead Screw and the Smooth Guide Rod
    with BuildSketch() as sk:
        Slot_Overall(60, 25)
    extrude(amount=10)

    # 2. Smooth Rod Bearing Hole (Left side)
    # We use the filter trick to ensure we hit the top face
    top_face = z_bracket.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(top_face) as bearing_sk:
        with Locations((-20, 0)):
            Circle(bearing_dia / 2)
    extrude(amount=-10, mode=Mode.SUBTRACT)

    # 3. Lead Screw Nut Mount (Right side)
    with BuildSketch(top_face) as nut_sk:
        with Locations((20, 0)):
            Circle(10 / 2) # Center hole for screw
            # Mounting holes for the brass nut
            with GridLocations(lead_screw_nut_holes, lead_screw_nut_holes, 2, 2):
                Circle(3.4 / 2)
    extrude(amount=-10, mode=Mode.SUBTRACT)

    # 4. The "Pivot" Cup (The Chic Part)
    # Instead of bolting the bed flat, it sits in this spherical cup
    with BuildSketch(top_face) as pivot_sk:
        with Locations((0, 0)):
            Circle(8 / 2)
    # Use a countersink-style subtraction for the pivot ball
    extrude(amount=-5, mode=Mode.SUBTRACT)