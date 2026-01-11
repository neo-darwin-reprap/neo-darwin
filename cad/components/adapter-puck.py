from build123d import *

# --- Config for the Adapter ---
wade_bolt_spacing = 50.0
central_bore = 16.5  # Standard for V6/J-Head
donor_type = "CREALITY_MK8" # Options: "V6_DIRECT", "CREALITY_MK8"

with BuildPart() as adapter_puck:
    # 1. The Main Puck Body (Fits into the bottom of the Wade)
    with BuildSketch() as sk:
        Circle(wade_bolt_spacing / 2 + 8) # Circular base
        # Adding the "ears" for the 50mm Wade bolts
        with GridLocations(wade_bolt_spacing, 0, 2, 1):
            Circle(7)
    extrude(amount=10)

    # 2. Wade Mounting Holes (M4 or M3 depending on your hardware)
    with BuildSketch(adapter_puck.faces().sort_by(Axis.Z)[-1]) as holes:
        with GridLocations(wade_bolt_spacing, 0, 2, 1):
            Circle(4.5 / 2) # Clearance for M4 bolts
    extrude(amount=-10, mode=Mode.SUBTRACT)

    # 3. Donor-Specific Cutouts
    if donor_type == "CREALITY_MK8":
        # Ender 3 hotends have two M3 holes approx 14mm apart
        with BuildSketch(adapter_puck.faces().sort_by(Axis.Z)[0]) as donor_sk:
            Circle(central_bore / 2) # Filament path
            with GridLocations(14, 0, 2, 1):
                Circle(3.2 / 2) # M3 mount holes
        extrude(amount=10, mode=Mode.SUBTRACT)
        
    elif donor_type == "V6_DIRECT":
        # Just a clean 16.5mm hole for the groove mount
        with BuildSketch(adapter_puck.faces().sort_by(Axis.Z)[0]) as donor_sk:
            Circle(central_bore / 2)
        extrude(amount=10, mode=Mode.SUBTRACT)

#