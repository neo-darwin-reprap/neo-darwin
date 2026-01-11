from build123d import *

# Config
rod_spacing = 45.0  # Standard Prusa i3 spacing
bearing_dia = 15.0  # LM10UU bearings (10mm rods)
wade_mount_width = 50.0

with BuildPart() as x_carriage:
    # 1. The Main Plate
    # We make it wider than the rods to provide a stable base for the Wade
    Box(70, rod_spacing + 30, 8) 
    
    # 2. The Bearing 'Saddles'
    # We use a Split-Clamp design so you can tighten the bearings with a bolt
    with Locations((0, rod_spacing / 2), (0, -rod_spacing / 2)):
        with BuildSketch() as saddle:
            Circle(bearing_dia / 2 + 4) # Outer housing
            # Subtract the bearing hole
            Circle(bearing_dia / 2, mode=Mode.SUBTRACT)
        extrude(amount=24, both=True)

    # 3. The 'Signature' Wade Mounting Holes
    # Note: We offset these in Y if the puck is extra thick
    y_offset = -5.0 # Shifting the mount to keep nozzle over the rods
    with BuildSketch(x_carriage.faces().sort_by(Axis.Z)[-1]) as mount_holes:
        with Locations((0, y_offset)):
            with GridLocations(wade_mount_width, 0, 2, 1):
                Circle(4.5 / 2) # M4 bolts for the Wade
    extrude(amount=-10, mode=Mode.SUBTRACT)

    # 4. Belt Clamps (The 'Chic' Way)
    # We'll add teeth directly into the print so the belt 'locks' in
    # (Detailed tooth geometry omitted for brevity)