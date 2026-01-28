# Session Notes - Amalgam CAD Project

**Date:** January 12, 2026
**Session Focus:** Architecture cleanup, build system improvements, standard corner implementation

---

## What We Accomplished

### 1. Architecture Review and Cleanup
- **Evaluated CAD project architecture** - Confirmed `include/` folder as primary engine is good design
- **Deleted obsolete files:**
  - `cad/components/` folder (7 legacy files with broken code)
  - `cad/main.py` (replaced by build.sh)
- **Fixed import paths** in `parts/corner_front_left.py` using `os.path.dirname(os.path.dirname(__file__))`
- **Updated Python requirement** from `>=3.14` to `>=3.10,<3.14` (build123d compatibility)

### 2. Build System Improvements
- **Updated `include/list.py`:**
  - Added recursive part discovery using `rglob` instead of `glob`
  - Added `--build-format` option for build.sh integration
  - Made script executable (`chmod +x`)
- **Updated `build.sh`:**
  - Changed `PARTS_LIST_SCRIPT` from `parts/list.py` to `include/list.py`
  - Added `setup_environment()` function
  - Fixed test mode fallback list

### 3. Documentation Updates
- **BUILDING.md:** Updated architecture section emphasizing `include/` as engine
- **README.md:** Added neodarwin.org link under Quick Start
- **Moved `.nojekyll`** from root to `docs/` folder (correct location for GitHub Pages)

### 4. Configuration and Fallback Handling
- **Removed fallback values** from part files - now exit with error if config.py missing
- **Added corner parameters to config.py:**
  - `CORNER_SIZE = 50.0`
  - `WALL_THICKNESS = 5.0`
  - `JAM_NUT_ACCESS_DIA = 20.0`
- **Error message:** Parts now show:
  ```
  ERROR: config.py not found
  Please run: ./configure.py
  ```

### 5. Created corner_standard.py
- **Purpose:** Basic standard corner with 4 M12 rod clamps and jam nut access
- **Implementation:**
  - Uses `Box()` for corner cube
  - Creates 4 M12 rod holes using `Cylinder()` and subtraction
  - Adds jam nut access holes on all faces
  - Rotates cylinders using `.rotate(Axis.Z, 90)` (not `.rotated()`)
- **Exports to:** `stl/corner_standard.stl`
- **Successfully tested:** Generated 75KB STL file

### 6. Created AGENTS.md
- **Purpose:** Coding guidelines for AI agents working on this repo
- **Content (123 lines):**
  - Build/test/lint commands
  - File structure and import patterns
  - Naming conventions (snake_case, UPPER_SNAKE_CASE)
  - Config usage patterns (always use config, no fallbacks)
  - build123d patterns (Box, Cylinder, .moved(), .rotate())
  - Common pitfalls

### 7. Git Operations
- Created 4 commits and pushed all changes
- Updated `.gitignore` to exclude `cad/stl/*.stl`

---

## Current Status

### Working Parts
- ✅ `corner_standard.py` - Successfully generates STL (75KB)
  - Used for: back-left, back-right, top-left, top-right, top-back-left, top-back-right (6 total)

### Files Modified This Session

| File | Changes |
|------|---------|
| `cad/build.sh` | Added `setup_environment()`, fixed PARTS_LIST_SCRIPT path |
| `cad/include/list.py` | Recursive discovery, `--build-format` option, made executable |
| `cad/include/corner_components.py` | Added `make_standard_corner()` function |
| `cad/parts/corner_front_left.py` | Fixed import path, removed config fallbacks |
| `cad/parts/corner_standard.py` | **NEW** - working standard corner implementation |
| `cad/config.py` | Added corner parameters (CORNER_SIZE, WALL_THICKNESS, JAM_NUT_ACCESS_DIA) |
| `cad/config.py.example` | Added corner parameters |
| `cad/pyproject.toml` | Changed Python requirement to `>=3.10,<3.14` |
| `BUILDING.md` | Updated architecture documentation |
| `README.md` | Added neodarwin.org link |
| `docs/.nojekyll` | Moved from root directory |
| `.gitignore` | Added `cad/stl/*.stl` patterns |
| `AGENTS.md` | **NEW** - agent guidelines (123 lines) |

---

## Key Technical Decisions

1. **`include/` as engine:** Shared CAD logic in `include/`, part configurations in `parts/`
2. **No fallbacks for config:** Exit with error to prevent wrong parts from being built
3. **Python 3.10-3.13:** build123d 0.10.0 doesn't support 3.14
4. **STL location:** All exports go to `stl/` directory
5. **Import pattern:** `sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))` from `parts/` to access `include/`
6. **build123d methods:** Use `.rotate()`, not `.rotated()`
7. **Standard corner design:** Single `corner_standard.py` file used for 6 positions (back-left, back-right, and all 4 top corners)

---

## Next Steps

### Immediate Tasks (Based on FINAL-FRAME-PARTS.md)

**Remaining Corner Parts:**

1. **`corner_front_left.py` (motorized)** - needs implementation
   - Extends standard corner with NEMA17 motor mount
   - Motor mounting holes on YZ plane
   - Belt routing features
   - Status: File exists but needs complete implementation

2. **`corner_front_right.py` (motorized)** - needs implementation
   - Mirror version of `corner_front_left.py`
   - Motor mounting on same side but mirrored geometry

3. **`corner_back_left.py`** - use `make_standard_corner()` from `include/corner_components.py`
   - File exists but needs implementation
   - Should simply call `make_standard_corner()` and export

4. **`corner_back_right.py`** - use `make_standard_corner()` from `include/corner_components.py`
   - File exists but needs implementation
   - Should simply call `make_standard_corner()` and export

5. **`z_puck.py` (Z3 motor mount)** - new component
   - Not yet created
   - Motor mount for Z-axis at top of frame
   - May need separate component file

**Top Frame Corners (4 parts):**

6. **`corner_tl.py`** - use `make_standard_corner()` (top-left)
7. **`corner_tr.py`** - use `make_standard_corner()` (top-right)
8. **`corner_bl.py`** - use `make_standard_corner()` (top-back-left)
9. **`corner_br.py`** - use `make_standard_corner()` (top-back-right)

### Recommended Implementation Order

1. **Complete `corner_front_left.py`** (motorized)
   - Extend standard corner with NEMA17 mount
   - Add motor bolt holes (4× M3)
   - Add center bore for shaft
   - Add belt routing features if needed

2. **Complete `corner_front_right.py`** (motorized)
   - Mirror of `corner_front_left.py`
   - Similar NEMA17 mount but mirrored geometry

3. **Create standard top corners** (tl, tr, bl, br)
   - Reuse `make_standard_corner()` from `include/corner_components.py`
   - Simple export wrapper files

4. **Implement back corners** (back_left, back_right)
   - Reuse `make_standard_corner()`
   - Simple export wrapper files

5. **Create `z_puck.py`** (Z3 motor mount)
   - Design new component for Z-axis motor
   - May require new include function

---

## Project Structure (Current)

```
amalgam/
├── cad/
│   ├── include/                    # Shared CAD components (engine)
│   │   ├── corner_components.py    # Standard corner function
│   │   └── list.py                 # Part discovery script
│   ├── parts/                      # Individual part implementations
│   │   ├── corner_standard.py      # ✅ Working (75KB STL)
│   │   ├── corner_front_left.py    # ⚠️ Needs motorized implementation
│   │   ├── corner_front_right.py   # ⚠️ Needs motorized implementation
│   │   ├── corner_back_left.py     # ⚠️ Needs to call make_standard_corner()
│   │   ├── corner_back_right.py    # ⚠️ Needs to call make_standard_corner()
│   │   ├── corner_tl.py            # ⚠️ Not created yet
│   │   ├── corner_tr.py            # ⚠️ Not created yet
│   │   ├── corner_bl.py            # ⚠️ Not created yet
│   │   └── corner_br.py            # ⚠️ Not created yet
│   ├── stl/                        # Generated STL files
│   │   └── corner_standard.stl     # ✅ Generated
│   ├── config.py                   # User configuration (gitignored)
│   ├── config.py.example           # Reference configuration
│   ├── pyproject.toml              # Python 3.10-3.13 requirement
│   └── build.sh                    # Build script
├── docs/
│   └── .nojekyll                   # GitHub Pages file
├── BUILDING.md                     # Build documentation
├── README.md                       # Project overview
├── AGENTS.md                       # AI agent guidelines
├── FINAL-FRAME-PARTS.md            # Part specifications
└── SESSION_NOTES.md                # This file
```

---

## Quick Commands

### Build/Test
```bash
cd cad

# Test single part (fastest iteration)
.venv/bin/python parts/corner_standard.py

# Build all parts
./build.sh build_all

# Build specific part
./build.sh build corner_standard

# List all parts
./build.sh list
```

### Lint/Format
```bash
cd cad
ruff check .      # Lint
ruff format .     # Format
pytest             # Run tests
```

### Git
```bash
git status        # Check current state
git add .         # Stage changes
git commit        # Commit with message
git push          # Push to remote
```

---

## Important User Preferences

- **No fallbacks for config** - Exit with error if config.py missing
- **Use config values** for all dimensions affecting fit
- **STLs go to stl/** directory
- **include/ is the engine** - Shared components live here
- **Individual part files** in `parts/` that import from `include/`
- **Python 3.10-3.13** - Not 3.14+
- **AGENTS.md** exists for future agent reference
- **Standard corner design:** One `corner_standard.py` file for 6 positions (assembly docs will specify quantities)

---

## Pending Issues / Notes

- Motorized corners (`corner_front_left.py`, `corner_front_right.py`) need NEMA17 mount design
- Need to determine if `z_puck.py` should reuse corner components or be standalone
- Assembly instructions not yet created (will specify part quantities)
- Top corner files not yet created (tl, tr, bl, br)
- Back corner files exist but need implementation

---

## How to Resume This Session

Simply say: **"continue from SESSION_NOTES.md"**

I will read this file and:
1. Understand what we've accomplished
2. See the current state of the codebase
3. Continue with the next logical task

---

**End of Session Notes**
