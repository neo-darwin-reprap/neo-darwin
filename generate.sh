#!/bin/bash

# Neo-Darwin Part Generator - Command Line STL Export
# Usage: ./generate.sh [part_name] [--view]
# Examples:
#   ./generate.sh corner_1              # Generate corner_1 STL
#   ./generate.sh corner_1 --view       # Generate and open in build123d
#   ./generate.sh all                    # Generate all parts

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Config
CAD_DIR="cad/parts"
STL_DIR="cad/stl"
CONFIG_FILE="cad/config.py"

# Help function
show_help() {
    echo "Neo-Darwin Part Generator"
    echo ""
    echo "Usage: $0 [part_name] [--view]"
    echo ""
    echo "Options:"
    echo "  part_name    Name of part (without .py extension)"
    echo "                Available parts:"
    echo "                  corner_1"
    echo "                  corner_2"
    echo "                  corner_3"
    echo "                  corner_4"
    echo "                  z_puck"
    echo "                  spider_hub"
    echo "                  spider_arm"
    echo "                  top_corner_tl"
    echo "                  top_corner_tr"
    echo "                  top_corner_bl"
    echo "                  top_corner_br"
    echo "                  all"
    echo ""
    echo "  --view        Open STL in build123d viewer after generation"
    echo ""
    echo "Examples:"
    echo "  $0 corner_1"
    echo "  $0 corner_1 --view"
    echo "  $0 all"
}

# Check if directory exists
check_file() {
    if [ ! -f "$1" ]; then
        echo -e "${RED}Error: File not found: $1${NC}"
        exit 1
    fi
}

# Generate single part
generate_part() {
    local part_name=$1
    local part_file="$CAD_DIR/$part_name.py"
    local stl_name="${part_name}.stl"

    echo -e "${BLUE}Generating: $stl_name${NC}"

    check_file "$part_file"

    # Change to cad directory
    cd "$(dirname "$part_file")" || exit 1

    # Run Python script
    python "$part_name.py"

    # Check if STL was created
    if [ -f "../../$STL_DIR/$stl_name" ]; then
        echo -e "${GREEN}✓ Success: $stl_name created${NC}"
        local stl_size=$(du -h "../../$STL_DIR/$stl_name" | cut -f1)
        echo -e "  Size: $stl_size${NC}"
    else
        echo -e "${RED}✗ Failed: $stl_name not created${NC}"
        return 1
    fi

    # Open in build123d if requested
    if [ "$2" = "--view" ]; then
        echo -e "${YELLOW}Opening in build123d...${NC}"
        code "../../$STL_DIR/$stl_name"
    fi

    cd - > /dev/null
}

# Generate all parts
generate_all() {
    echo -e "${BLUE}Generating all parts...${NC}"

    local parts=(
        "corner_1_front_left_z1"
        "corner_2_front_right_z2"
        "corner_3_back_left"
        "corner_4_back_right"
        "z_puck_back_center"
        "spider_hub"
        "spider_arm"
        "top_corner_tl"
        "top_corner_tr"
        "top_corner_bl"
        "top_corner_br"
    )

    for part in "${parts[@]}"; do
        if [ -f "$CAD_DIR/$part.py" ]; then
            generate_part "$part" ""
        else
            echo -e "${YELLOW}⚠ Skipping: $part.py (not found)${NC}"
        fi
    done

    echo -e "${GREEN}All parts generated!${NC}"
    echo ""
    echo -e "${BLUE}STL files location: $STL_DIR/${NC}"
    echo ""
    echo "View in VSCode: Use build123d extension to open .stl files"
}

# Create STL directory if not exists
mkdir -p "$STL_DIR"

# Parse arguments
if [ $# -eq 0 ]; then
    show_help "$0"
    exit 0
fi

PART_NAME=$1
VIEW_STL=""

# Check for --view flag
if [ "$1" = "--view" ]; then
    VIEW_STL="--view"
    shift
fi

if [ "$1" = "all" ]; then
    generate_all
else
    generate_part "$1" "$VIEW_STL"
fi
