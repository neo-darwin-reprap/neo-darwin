with BuildPart() as y_motor_mount:
    # 1. The Base Block (Clamps to the M12 rod)
    Box(30, 50, 40)
    
    # 2. The Motor Plate (Offset to the side)
    with Locations((35, 0, 0)):
        Box(42, 50, 40) # Standard NEMA 17 is ~42mm
        
    # 3. The M12 Hole (Using our new filtering trick!)
    with BuildSketch(y_motor_mount.faces().filter_by(Axis.Y)) as rod_hole:
        Circle(rod_dia / 2)
    extrude(amount=-30, mode=Mode.SUBTRACT)

    # 4. Motor Mounting Pattern (NEMA 17 = 31mm spacing)
    # We select the face furthest out on the X axis
    motor_face = y_motor_mount.faces().sort_by(Axis.X)[-1]
    with BuildSketch(motor_face) as motor_holes:
        Circle(22/2) # Central boss hole
        with GridLocations(31, 31, 2, 2):
            Circle(3.4 / 2) # M3 screw holes
    extrude(amount=-10, mode=Mode.SUBTRACT)