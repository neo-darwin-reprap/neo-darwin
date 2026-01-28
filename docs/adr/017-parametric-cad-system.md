# ADR-017: Parametric CAD System

## Status
Accepted

## Context
The Amalgam requires a parametric CAD system that supports:
- **Customizable Dimensions**: Variable build volumes, rod lengths, bed sizes
- **Code-First Approach**: Version control, diff-friendly, scriptable
- **Precision Geometry**: NURBS/BREP for accurate manufacturing
- **Parametric Flexibility**: Easy dimension changes without manual remodeling
- **Integration**: Works with Python ecosystem (scripts, NumPy, APIs)
- **Professional Output**: STEP files for CNC, STL for 3D printing

In 2026, several CAD paradigms exist with different trade-offs:
1. **Visual/Drag-Drop**: TinkerCAD, Fusion 360
2. **GUI Parametric**: FreeCAD, SolidWorks
3. **Scripted CSG**: OpenSCAD
4. **Scripted BREP**: build123d

Each has different capabilities for parametric hardware design.

## Decision
We adopt **build123d** as the core parametric CAD system.

### CAD Paradigm Comparison

| Feature | TinkerCAD | FreeCAD (GUI) | OpenSCAD | **build123d** |
|---------|-----------|---------------|----------|-------------|
| **Core Paradigm** | Simple CSG (Visual) | BREP (Feature Tree) | Scripted CSG | **Scripted BREP** |
| **Language** | None (Drag/Drop) | Python (Optional) | OpenSCAD (Domain) | **Python (Native)** |
| **Geometry** | Meshes | Precise NURBS | Meshes/CSG | **Precise NURBS/STEP** |
| **Selection** | Mouse | Mouse (Unstable) | Manual Math | **Smart Selectors** |
| **Version Control** | Poor | Difficult (Binary) | Excellent (Text) | **Excellent (Python)** |
| **Parametric** | Limited | Good | Excellent | **Excellent** |
| **Learning Curve** | Low | High | Medium | **Medium** |

### Why build123d

**1. Object Awareness (BREP Advantage)**
- Unlike OpenSCAD's CSG, build123d understands topology
- Can find faces, edges, and vertices programmatically
- Example: "Find top-most face and fillet all edges parallel to X-axis"
- If part grows/shrinks, script still finds correct features
- OpenSCAD requires manual coordinate tracking that breaks on size changes

**2. Native Python Power**
- No proprietary CAD language to learn
- Full Python ecosystem: NumPy for math, requests for APIs, logging for debugging
- pip install infrastructure for extensions
- Standard Python tooling: pytest, black, ruff, mypy
- Familiar to developers, steep learning curve only for CAD concepts

**3. "Builder" vs "Algebra" Modes**
- `with BuildPart() as part:` context mimics human building workflow
- "I am working on this face, now sketching here"
- More readable than functional CSG languages
- Supports both algebraic (`Box() - Cylinder()`) and builder (`build123d`)

**4. Professional Output**
- Exports true STEP files (industry standard for CNC, manufacturing)
- STL export with high-quality mesh generation
- BREP kernel (OpenCascade) provides precise geometry
- OpenSCAD largely stuck in STL world (mesh approximations)

**5. Fillet/Chamfer Support**
- OpenSCAD: Mathematically exhausting for complex edges
- FreeCAD: Fillets work but can break on topology changes
- build123d: Smart selectors + BREP make fillets reliable
- Can fillet specific edges based on orientation, length, etc.

### Why Alternatives Were Rejected

**OpenSCAD (The "Old Guard" of Code-CAD)**
- **Math Tax**: Must track coordinates manually (no object awareness)
- **Fillet/Chamfer Nightmare**: Complex geometry is mathematically exhausting
- **Non-Standard Language**: Proprietary functional language with no ecosystem
- **Mesh-Only Output**: Lacks STEP export for professional manufacturing
- **Slow Rendering**: CSG evaluation is slower than BREP

**FreeCAD & GUI Systems**
- **Topological Naming Problem**: Internal face names "shuffle" on dimension changes
- Breaking features: Hole suddenly on wrong side after early dimension change
- **Hard to Automate**: Python API bolted onto GUI-first workflow
- **GUI Dependency**: Requires graphical environment (not server-friendly)
- **Binary Files**: Poor version control, diff-friendly text not available

**TinkerCAD & Visual Systems**
- **No Version Control**: Binary files, impossible to diff
- **No Parametric**: Manual remodeling for dimension changes
- **Poor Precision**: Mesh-based approximation vs NURBS
- **No Automation**: Drag-drop cannot be scripted
- **Limited Ecosystem**: No integration with Python tooling

### Integration with Quarto (ADR-018)

**Literate CAD**:
- build123d is Python, Quarto executes Python cells
- Can embed CAD code directly in documentation
- Automated rendering: Generate part views during doc build
- Diagrams stay synchronized with code

**Single Source of Truth**:
- CAD code and documentation in same ecosystem
- Change dimension → regenerate STLs → regenerate docs → all synchronized
- No manual screenshot taking or image updating

## Consequences

### Benefits
- **Parametric Power**: Infinite permutations, single codebase
- **Python Ecosystem**: NumPy, pytest, black, ruff, mypy, requests, logging
- **Object Awareness**: Smart selectors for reliable geometry operations
- **Version Control**: Text files, diff-friendly, git-friendly
- **Professional Output**: STEP files for CNC, STL for 3D printing
- **Automatable**: CLI-first, no GUI dependency
- **Community**: Growing Python CAD community, not niche OpenSCAD ecosystem

### Trade-offs
- **Learning Curve**: Requires learning build123d API + CAD concepts
- **Python Required**: Users need Python environment to generate parts
- **Preview Limited**: No visual editor (though OCP-VSCode provides some visualization)
- **Performance**: BREP operations can be slower than simple CSG
- **Ecosystem**: Smaller than OpenSCAD community (but growing)

### What This Enables
- **Infinite Customization**: User changes one dimension, entire machine regenerates
- **Automated Workflows**: CI/CD for CAD validation, doc generation
- **Web UI**: Server-side part generation for non-technical users
- **Literate Documentation**: CAD code embedded in Quarto docs (ADR-018)
- **Integration**: NumPy for complex geometry, APIs for pulling data

### What This Replaces
- Static STL repositories (manual management, limited permutations)
- OpenSCAD scripts (object awareness, Python ecosystem)
- FreeCAD files (topological naming, GUI dependency)
- Visual CAD (no version control, no automation)

## Implementation Notes

### build123d Project Structure
```
cad/
├── include/              # Shared components (brackets, pucks)
│   ├── corner_components.py
│   ├── puck_components.py
│   └── ...
├── parts/                # Individual parts
│   ├── corner_standard.py
│   ├── bed_spider.py
│   └── ...
├── config.py.example      # Reference configuration
├── config.py             # User configuration (gitignored)
├── build.sh               # Build script (STL generation)
├── configure.py           # Configuration wizard
└── .venv/                # Python virtual environment
```

### Code Style
```python
# Import pattern (parts/)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from include.corner_components import make_standard_corner

# Always use config values (no fallbacks)
from config import CORNER_SIZE, M12_FIT_DIA

def main():
    from build123d import export_stl as export_stl_func
    corner = make_standard_corner(
        corner_size=CORNER_SIZE,
        m12_fit_dia=M12_FIT_DIA,
    )
    export_stl_func(corner, "stl/filename.stl")
```

### Smart Selectors Example
```python
# Find all faces normal to Z-axis
top_faces = part.faces().filter_by_position(Axis.Z, position=0)

# Find edges parallel to X and longer than 10mm
x_parallel_edges = part.edges().filter_by_direction(Axis.X)
x_parallel_long = x_parallel_edges.filter_by_length(min=10)

# Fillet all matching edges
part = part.fillet(x_parallel_long, radius=2)
```

### Builder Context Example
```python
with BuildPart() as corner:
    # Sketch on XY plane
    Box(50, 50, 20)
    # Select top face
    top = faces().sort_by(Axis.Z).last
    with BuildSketch(top.workplane()):
        Circle(10)
    extrude(amount=5)
```

### Version Control Best Practices
- **Text Files**: build123d scripts are plain text, git-friendly
- **Diff-Friendly**: Changes show line-by-line, not binary diffs
- **Review**: Can review PRs with git diff
- **Blame**: Can trace design decisions with git blame
- **CI/CD**: Lint (ruff), typecheck (mypy), test (pytest) on PRs

## References
- **docs/reference/ai-conversations/why-build123d.md**: Complete CAD discussion
- **docs/adr/018-documentation-system.md**: Quarto documentation system
- build123d Documentation: [build123d.io](https://build123d.com/)
- OpenCascade (BREP Kernel): [opencascade.com](https://www.opencascade.com/)
- OCP-VSCode Preview: [OCVSCode](https://github.com/CadQuery/OCP-vscode)

## Evolution Notes
This ADR establishes build123d as the core CAD system. Future CAD technologies will be evaluated against:
- Python native (not proprietary language)
- BREP with object awareness (not CSG only)
- STEP export capability (professional manufacturing)
- Smart selectors for reliable geometry operations
- Python ecosystem integration (NumPy, APIs, etc.)

Alternative emerging technologies:
- CadQuery (older version of build123d)
- PythonOCC (lower-level OpenCascade bindings)
- CQ-Editor (build123d GUI, but CLI-first preferred)
