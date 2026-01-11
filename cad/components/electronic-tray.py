from build123d import *

# Config
octopus_holes = (150, 90) # Typical BTT Octopus mounting pattern
pi_holes = (58, 49)      # RPi 3B+ pattern
fan_dia = 120.0          # The "Silent" upgrade

with BuildPart() as electronics_tray:
    # 1. The Main Tray Base
    # Sized to fit between the M12 rods (approx 200mm width)
    Box(220, 180, 4)
    
    # 2. The "Honeycomb" Vent (Under the 120mm fan)
    # This ensures your Octopus drivers stay cool
    top_face = electronics_tray.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(top_face) as vent_sk:
        Circle(fan_dia / 2)
        # In a real script, we'd add a Hexagonal grid here
    extrude(amount=-4, mode=Mode.SUBTRACT)

    # 3. Component Standoffs (The 'Lego' Pattern)
    # BTT Octopus Mounts
    with BuildSketch(top_face) as octopus_sk:
        with GridLocations(octopus_holes[0], octopus_holes[1], 2, 2):
            Circle(3.2 / 2) # M3 screw holes
    extrude(amount=5) # Create 5mm tall pillars

    # 4. Raspberry Pi Mounts (Offset to the side)
    with BuildSketch(top_face) as pi_sk:
        with Locations((80, 0)): # Move Pi away from the center
            with GridLocations(pi_holes[0], pi_holes[1], 2, 2):
                Circle(2.5 / 2) # M2.5 for Pi
    extrude(amount=5)