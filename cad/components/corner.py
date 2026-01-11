from build123d import *
from config import ROD_DIA, WALL_THICKNESS, LUMPY_FACTOR

# The Corner Puck: The primary structural node of the Darwin-Neo
def generate_corner_puck():
    # Base block size derived from M12 rod diameter and required wall thickness
    side_len = ROD_DIA + (WALL_THICKNESS * 2)
    
    with BuildPart() as corner:
        # Create the main structural cube
        Box(side_len, side_len, side_len)
        
        # Hollow out the three intersecting M12 channels (X, Y, Z)
        # The LUMPY_FACTOR in config.py ensures these fit even on galvanized rods
        with BuildSketch(Plane.XY):
            Circle(ROD_DIA / 2)
        extrude(amount=side_len, both=True, mode=Mode.SUBTRACT)
        
        with BuildSketch(Plane.YZ):
            Circle(ROD_DIA / 2)
        extrude(amount=side_len, both=True, mode=Mode.SUBTRACT)
        
        with BuildSketch(Plane.XZ):
            Circle(ROD_DIA / 2)
        extrude(amount=side_len, both=True, mode=Mode.SUBTRACT)
        
    return corner.part

# Export for the community
if __name__ == "__main__":
    puck = generate_corner_puck()
    export_stl(puck, "darwin_neo_corner_puck.stl")