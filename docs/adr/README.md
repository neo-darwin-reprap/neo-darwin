# Neo-Darwin Architecture Decision Records (ADRs)

This directory contains all Architecture Decision Records (ADRs) for the Neo-Darwin project. Each ADR documents a significant engineering decision, including context, alternatives, rationale, and consequences.

## How to Read This Directory

ADRs are numbered chronologically in order of creation (000-018). However, for understanding the project's engineering philosophy:

1. **Start with ADR-000**: Engineering Philosophy and "Tractor" principles
2. **Read Core Hardware ADRs (001-016)**: Foundation, motion, electronics
3. **Read Tooling/Software ADRs (017-018)**: CAD, documentation, systems

## ADR Index

### Foundational ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-000](000-engineering-philosophy.md) | Engineering Philosophy (20 Years of RepRap Wisdom) | Accepted | Core principles: Mass, Software, Gearing, Neo-Darwin Square trade-offs |
| [ADR-001](001-m12-skeleton.md) | M12 Threaded Rod Skeleton | Accepted | Heavy steel frame for mass damping and rigidity |
| [ADR-002](002-greg-wade.md) | Greg's Wade Geared Extruder | Accepted | 5.22:1 geared extruder for "Tractor Torque" |
| [ADR-003](003-smooth-rods.md) | Smooth Rods vs Linear Rails | Accepted | 10mm precision ground rods over 8mm salvage, linear rails for speed experiments |
| [ADR-004](004-v6-cht.md) | E3D V6 Hotend with CHT Nozzle | Accepted | Standard V6 with CHT clone nozzle for high flow without ooze |

### Motion & Leveling ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-005](005-triple-z.md) | Triple-Z Kinematic Leveling | Accepted | 3 independent Z-motors for automated bed leveling |
| ~~ADR-006~~ | Z-Probe Selection (Legacy) | **Archived** | Superseded by ADR-014 |
| [ADR-009](009-puck-system.md) | Modular Puck & Spider Bed System | Accepted | Standardized mounting for toolheads, bed supports, Z-motors |
| [ADR-010](010-floating-z-puck.md) | Floating Z-Puck System | Accepted | Parametric Z-motor pucks for any bed size, double-nut anchor |

### Foundation & Electronics ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-007](007-can-bus.md) | CAN Bus Architecture | Accepted | Future-proofing for toolhead boards, ERCF, modular expansion |
| [ADR-008](008-spider-bed.md) | Spider Bed Support System | Accepted | Modular 3-part bed support for printing on small donor machines |
| [ADR-011](011-laminated-plinth.md) | Laminated Plinth Baseboard | Accepted | Constrained Layer Damping (CLD) foundation for Tier 3 Reference Spec |
| [ADR-012](012-mainboard-host-architecture.md) | Mainboard & Host Architecture | Accepted | MKS SKIPR Reference Spec, multi-MCU salvage paths |
| [ADR-013](013-drivers-endstops.md) | Driver & Endstop Strategy | Accepted | TMC2209 with mechanical switches, Z-max safety switch |
| [ADR-016](016-electronics-mounting.md) | Electronics & PSU Mounting Strategy | Accepted | Direct MDF coupling (Reference) vs printed puck frames |

### Tooling & Probing ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-014](014-z-probe-selection.md) | Z-Probe Selection (SuperPINDA vs BLTouch) | Accepted | SuperPINDA for Reference Spec (metal beds), BLTouch for scavenger (universal) |
| [ADR-015](015-single-toolhead.md) | Single Toolhead Architecture | Accepted | Base spec single toolhead, ERCF v2 expansion, manual puck swaps for laser/pen |

### Software & Tooling ADRs

| ADR | Title | Status | Summary |
|-----|-------|--------|---------|
| [ADR-017](017-parametric-cad-system.md) | Parametric CAD System | Accepted | build123d over OpenSCAD/FreeCAD/TinkerCAD for BREP and Python ecosystem |
| [ADR-018](018-documentation-system.md) | Documentation & Assembly Guide System | Accepted | Quarto for literate CAD, professional PDFs, conditional content |

## ADR Categories

### Core Hardware (001-004)
Frame, extruder, hotend, and motion system - the physical foundation of the machine.

### Motion & Leveling (005, 007-010)
Z-axis leveling, CAN bus, modular bed, and Z-motor mounting - kinematic accuracy and foundation.

### Foundation & Electronics (008-009, 011-013, 016)
Baseboard, mainboard, drivers, endstops, and electronics mounting - "Brain" and power.

### Tooling & Probing (014-015)
Z-probe selection and toolhead architecture - single/multi-material capability.

### Software & Tooling (017-018)
CAD system and documentation - parametric design and assembly guides.

## Reading Order for New Contributors

If you're new to Neo-Darwin and want to understand the engineering decisions:

1. **Engineering Philosophy** → ADR-000
2. **Hardware Foundations** → ADR-001, 002, 004
3. **Motion System** → ADR-003, 005
4. **Electronics** → ADR-012, 013
5. **Probing** → ADR-014
6. **Advanced Features** → ADR-007, 009, 011, 015, 016
7. **Tooling** → ADR-017, 018

## ADR Template

When creating a new ADR, use the template at `template.md`:

```markdown
# ADR-XXX: [Title]

## Status
Accepted | Proposed | Deprecated | Superseded

## Context
What is the issue we're facing that motivated this decision?

## Decision
What is the change we're proposing?

## Consequences
What becomes easier or more difficult to do because of this change?

## BOM Implications (Generic)
What parts are affected by this decision?

## References
Links to relevant documentation, AI conversations, or external resources.
```

## ADR Lifecycle

- **Proposed**: Initial draft, under discussion
- **Accepted**: Decision finalized, implemented
- **Deprecated**: Still in use, but recommended against for new builds
- **Archived**: Replaced by newer ADR, kept for historical reference

## Version Control

All ADRs are tracked in git. Changes to accepted ADRs should be:
- Clearly explained in commit messages
- Discussed with project maintainers before merging
- Documented with rationale for the change

## References

- **Project Manifesto**: `MANIFESTO.md` - High-level philosophy and goals
- **Reference Documentation**: `docs/reference/` - Detailed technical discussions
- **AI Conversations**: `docs/reference/ai-conversations/` - Raw design discussions
- **CAD System**: `cad/` - build123d parametric scripts
- **Build Instructions**: `docs/planning/` - Assembly and construction guides

---

**"The code handles the permutations; the iron handles the quality."**
