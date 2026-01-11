"""
Neo-Darwin Corner 1: Front-Left with Integrated Z1 Motor Mount

This is the first of 4 bottom frame corners, with Z-motor Z1 integrated
into the corner bracket design.

Location: Front-Left corner
Z-Motor: Z1 (integrated)
Rod Clamps: Vertical Front-Left, Vertical Front-Center-Left, Horizontal Front-Left
"""

from build123d import *
from config import *


def make_corner_front_left_z1():
    """
    Generate Front-Left corner with integrated Z1 motor mount

    Frame connections:
    - Vertical rod: Front-Left (VFL)
    - Vertical rod: Front-Center-Left (FCL) - optional center rod
    - Horizontal rod: Front-Left

    Features:
    - Integrated NEMA17 Z1 motor mount
    - M12 rod clamps (2 vertical + 1 horizontal)
    - Leadscrew vertical path clearance
    - Jam nut access points (2 per rod)
    - Cable routing channels for Z-motor
    - Reinforcement structure

    Returns:
        build123d Part object for the corner
    """

    # --- PARAMETERS FROM CONFIG ---
    m12_fit_dia = M12_FIT_DIA  # 12.5mm (12.0 + 0.5 lumpy factor)
    wall_thickness = 5.0  # 5mm walls for strength
    motor_bolt_spacing = 31.0  # NEMA17 standard bolt spacing
    motor_mount_depth = 25.0  # Depth of motor mount from rod center
    leadscrew_clearance = 15.0  # Vertical clearance for leadscrew
    cable_channel_depth = 6.0  # Depth of cable channel
    cable_channel_width = 12.0  # Width of cable channel

    # --- CALCULATED DIMENSIONS ---
    # Corner base size (cube to subtract M12 channels from)
    corner_size = m12_fit_dia + (wall_thickness * 2)  # Side length of cube

    # Motor mount plate dimensions
    motor_plate_width = 42.0  # NEMA17 face width
    motor_plate_height = 42.0  # NEMA17 face height
    motor_plate_depth = motor_mount_depth  # Depth from rod center

    # Jam nut access holes (2 per rod clamp)
    jam_nut_dia = 20.0  # Wrench access diameter
    jam_nut_offset = wall_thickness / 2  # Center access through wall

    # Cable routing channel
    cable_channel_width = cable_channel_width
    cable_channel_height = cable_channel_depth

    # --- BUILD THE PART ---
    with BuildPart() as corner:
        # 1. Create corner base block
        corner_base = Box(corner_size, corner_size, corner_size)

        # 2. Create M12 vertical rod channel (Front-Left)
        with BuildSketch(corner_base.faces(">Z")):
            Circle(m12_fit_dia / 2).extrude(amount=corner_size)

        # 3. Create M12 vertical rod channel (Front-Center-Left) - Optional
        # Only if FRONT_CENTER_V is True in config
        # Add separate channel in same plane
        # if config.get("FRONT_CENTER_V"):
        #     with BuildSketch(corner_base.faces(">Z")):
        #         Location((corner_size * 0.3, corner_size * 0.3), 0).circle(m12_fit_dia / 2)
        #         Circle(m12_fit_dia / 2).extrude(amount=corner_size * 0.4)

        # 4. Create M12 horizontal rod channel (Front-Left)
        with BuildSketch(corner_base.faces(">Y")):
            Location((0, m12_fit_dia / 2, 0)).circle(m12_fit_dia / 2).extrude(
                amount=corner_size
            )

        # 5. Create leadscrew vertical path clearance (through frame interior)
        # This is the vertical path that Z1 leadscrew takes going UP
        leadscrew_path_dia = 10.0  # Clearance for TR8 leadscrew
        with BuildSketch(corner_base.faces(">X")):
            Location(
                (motor_plate_depth + leadscrew_clearance, corner_size / 2, 0)
            ).circle(leadscrew_path_dia / 2).extrude(amount=wall_thickness * 2)

        # 6. Create motor mount plate (Z1)
        with BuildSketch(corner_base.faces(">X")):
            # Motor mount face plate
            motor_face = Rectangle(motor_plate_width, motor_plate_height)
            motor_face = extrude(motor_face, amount=motor_plate_depth)

            # NEMA17 motor bolt holes (4 corners of face)
            bolt_pattern = [
                (-motor_bolt_spacing / 2, motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, -motor_bolt_spacing / 2),
                (motor_bolt_spacing / 2, -motor_bolt_spacing / 2),
            ]

            for bolt_x, bolt_y in bolt_pattern:
                with BuildSketch(motor_face.faces(">X")):
                    Location((bolt_x, bolt_y, 0)).circle(3.0).extrude(
                        amount=wall_thickness
                    )

        # 7. Create cable routing channels (for Z-motor wires)
        with BuildSketch(corner_base.faces(">Z")):
            # Channel on one side of motor mount
            channel_rect = Rectangle(cable_channel_width, cable_channel_height)
            channel_rect = extrude(channel_rect, amount=motor_plate_depth)

        # 8. Create jam nut access holes (2 per rod clamp)
        # Front-Left vertical rod jam nuts
        with BuildSketch(corner_base.faces(">X")):
            # Top jam nut
            Location(
                (
                    corner_size / 2,
                    m12_fit_dia + wall_thickness / 2 + jam_nut_offset,
                    wall_thickness / 2,
                )
            ).circle(jam_nut_dia / 2).extrude(amount=wall_thickness)

            # Side jam nut (for tightening corner to rod)
            with BuildSketch(corner_base.faces(">Y")):
                Location(
                    (
                        wall_thickness / 2 + jam_nut_offset,
                        corner_size / 2,
                        corner_size / 2,
                    )
                ).circle(jam_nut_dia / 2).extrude(amount=wall_thickness)

        # 9. Add fillets (rounded edges for strength)
        edges_to_fillet = [
            corner_base.edges("|X and >Y"),  # Motor mount edges
            corner_base.edges("|Y and >Z"),  # Front face
            corner_base.edges("|Z and >X"),  # Top edges
        ]
        fillet(edges_to_fillet, radius=3.0)

        # 10. Label the part
        corner.label = "Corner-1-FrontLeft-Z1"
        corner.label_location = (-corner_size / 2, -corner_size / 2, corner_size)

    return corner


def main():
    """
    Main function to generate and export Corner 1 (Front-Left + Z1)
    """
    print("Generating Corner 1: Front-Left with integrated Z1 motor mount...")

    # Generate the part
    corner_1 = make_corner_front_left_z1()

    # Export to STL
    export_stl(corner_1, "corner_1_front_left_z1.stl")

    # Print dimensions
    print(f"  M12 rod diameter: {M12_FIT_DIA}mm")
    print(f"  Motor: NEMA17 (Z1)")
    print(f"  Bolt spacing: {42.0}mm (standard)")
    print(f"  Export: corner_1_front_left_z1.stl")
    print("Corner 1 complete!")

    return corner_1


if __name__ == "__main__":
    main()
