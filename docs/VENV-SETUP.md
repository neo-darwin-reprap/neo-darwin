# Phase 2: Virtual Environment Setup

## Why Use Virtual Environment?

**Current Problem:**
- VSCode shows import errors for old code (main.py, components/*.py)
- Errors are from imports that don't exist (project_vars, parts.corners, etc.)
- Hard to debug which imports actually work

**Solution: Use Python venv**
1. Clean Python environment isolated from system
2. Test imports and build123d work separately
3. Verify config parameters are read correctly
4. No interference from old code
5. Reproducible setup

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
# In project root directory
cd /Users/michael/Projects/Personal/neo-darwin

# Create venv named 'venv'
python3 -m venv venv
```

### 2. Activate Virtual Environment

```bash
# Activate venv
source venv/bin/activate

# Verify activated (prompt should show (venv))
which python  # Should show: /Users/michael/Projects/Personal/neo-darwin/venv/bin/python
```

### 3. Install build123d

```bash
# Make sure pip is up to date
pip install --upgrade pip

# Install build123d
pip install build123d[all]
```

**Optional: Install visualization**
```bash
# For better CAD visualization (if needed)
pip install ocp_vscode
```

### 4. Test Configuration Import

```bash
# Activate venv first!
source venv/bin/activate

# Test if config.py is readable
python -c "from config import *; print('Config loaded successfully')"
```

Expected output:
```
--- Darwin-Neo Configuration: ENDER_3 Path !!!
Frame Dimensions: 540 x 370 x 300
Z-Travel: 260mm (Frame: 300mm)
Z-Motors: front_left_corner, front_right_corner, back_center_rod
Parts: 4 bottom corners + 4 top corners = 8 total
```

### 5. Test Part Generation

```bash
# Activate venv
source venv/bin/activate

# Generate Corner 1
cd cad/parts
python corner_1_front_left_z1.py
```

Expected output:
```
Generating Corner 1: Front-Left with integrated Z1 motor mount...
M12 rod diameter: 12.5mm
Motor: NEMA17 (Z1)
Bolt spacing: 42.0mm (standard)
Export: corner_1_front_left_z1.stl
Corner 1 complete!
```

---

## VSCode Integration

### Option 1: Use venv Interpreter

**In VSCode:**
1. Open Neo-Darwin project
2. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
3. Type: `Python: Select Interpreter`
4. Choose: `./venv/bin/python`
5. Reload VSCode window

**Benefit:** VSCode will use venv for running scripts, no more import errors

### Option 2: Disable Old Code Errors

**In `.vscode/settings.json`:**
```json
{
  "python.linting.ignorePatterns": [
    "cad/main.py",
    "cad/components/*.py"
    "cad/project_vars.py",
    "cad/parts/corners.py",
    "cad/parts/z_pucks.py",
    "cad/parts/carriage.py",
    "cad/parts/electronics.py"
  ],
  "files.exclude": {
    "**/.venv": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

**Benefit:** VSCode won't try to lint old code, focus on new parts/

---

## Design Workflow with venv

### For Each New Part:

1. **Activate venv**
   ```bash
   source venv/bin/activate
   ```

2. **Write part code** in `cad/parts/`
   - Import from config
   - Use build123d
   - Write clean code

3. **Test import** in venv
   ```bash
   python -c "from config import *; from parts import YOUR_PART; print('Imports work!')"
   ```

4. **Generate part**
   ```bash
   python cad/parts/your_part.py
   ```

5. **Render in VSCode**
   - Open STL in build123d viewer
   - Check dimensions
   - Verify features

6. **Export to STL**
   - Build123d script already exports
   - Verify STL file created in `cad/stl/`

---

## Quick Reference

```bash
# Setup (one time)
cd /Users/michael/Projects/Personal/neo-darwin
python3 -m venv venv
source venv/bin/activate
pip install build123d[all]

# Design workflow (repeat for each part)
source venv/bin/activate  # Activate venv
python cad/parts/your_part.py  # Generate STL
# Check STL in build123d viewer
# Verify dimensions, adjust config if needed

# Deactivate when done
deactivate
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError"

```bash
# Install missing dependency
pip install <module_name>
```

### Issue: "ImportError"

```bash
# Check file is in correct location
ls cad/parts/
# Check venv is activated
which python
```

### Issue: VSCode shows errors for old code

**Solution:** Use Option 1 (venv interpreter) or Option 2 (exclude old files from linting)

---

## Next Steps

After venv setup:

1. [ ] Create venv
2. [ ] Install build123d
3. [ ] Test config import
4. [ ] Generate Corner 1
5. [ ] Verify STL export
6. [ ] Update DESIGN-TRACKING.md
7. [ ] Continue with Corner 2
