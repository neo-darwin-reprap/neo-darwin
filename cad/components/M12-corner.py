from build123d import *
from ocp_vscode import show, set_port

set_port(3939)



# Config
rod_dia = 12.2   
block_size = 40.0 
bolt_dia = 4.5    

with BuildPart() as m12_corner:
    # 1. The Main Cube
    Box(block_size, block_size, block_size)
    # FILLET COMES LATER - If we do it now, we have to filter faces carefully
    
    # 2. The Three Rod Channels (X, Y, and Z)
    # We use Selectors to find only the flat faces
    # .faces().filter_by(GeomType.PLANE) is the safest way
    with BuildSketch(m12_corner.faces().filter_by(GeomType.PLANE)) as channels:
        Circle(rod_dia / 2)
    extrude(amount=-block_size/2 + 2, mode=Mode.SUBTRACT)

    # 3. The Split-Clamp Slits
    # Let's just pick one face to start the slit
    with BuildSketch(m12_corner.faces().sort_by(Axis.X)[0]) as slit:
        Rectangle(block_size, 1.5)
    extrude(amount=-block_size/2, mode=Mode.SUBTRACT)

    # 4. Now add the Fillets at the very end
    # This way they don't interfere with our sketching logic
    fillet(m12_corner.edges(), radius=2)

show(m12_corner)