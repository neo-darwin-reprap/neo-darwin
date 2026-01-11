#!/bin/bash

# Neo-Darwin Setup Wizard
# Full setup for new users: environment setup, configuration, and building

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Paths
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
CONFIG_SCRIPT="configure.py"
BUILD_SCRIPT="build.sh"

print_header() {
    echo ""
    echo "${BLUE}========================================${NC}"
    echo "  $1"
    echo "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

check_python() {
    print_header "Checking Python Installation"

    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        echo "Please install Python 3.9 or higher from https://www.python.org/"
        exit 1
    fi

    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

    print_success "Found Python $PYTHON_VERSION"

    if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 9 ]); then
        print_error "Python 3.9 or higher required"
        exit 1
    fi

    print_success "Python version meets requirements"
}

setup_venv() {
    print_header "Setting Up Python Virtual Environment"

    if [ -d "$VENV_DIR" ]; then
        print_warning "Virtual environment already exists"
        if ask_yes_no "Recreate virtual environment?"; then
            rm -rf "$VENV_DIR"
            python3 -m venv "$VENV_DIR"
            print_success "Virtual environment recreated"
        else
            print_success "Using existing virtual environment"
            return 0
        fi
    else
        python3 -m venv "$VENV_DIR"
        print_success "Virtual environment created"
    fi
}

activate_venv() {
    print_header "Activating Virtual Environment"

    if [ ! -f "$VENV_DIR/bin/activate" ]; then
        print_error "Virtual environment not found"
        exit 1
    fi

    source "$VENV_DIR/bin/activate"
    print_success "Virtual environment activated"
}

install_dependencies() {
    print_header "Installing Dependencies"

    if [ ! -f "$REQUIREMENTS_FILE" ]; then
        print_warning "requirements.txt not found, creating minimal version"
        cat > "$REQUIREMENTS_FILE" << 'EOF'
build123d>=0.2.0
numpy>=1.20.0
EOF
    fi

    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
    print_success "Dependencies installed"
}

run_configure() {
    print_header "Configuration Wizard"

    if [ ! -f "$CONFIG_SCRIPT" ]; then
        print_error "Configuration script not found: $CONFIG_SCRIPT"
        exit 1
    fi

    python "$CONFIG_SCRIPT"
}

build_parts() {
    print_header "Building Parts"

    if [ ! -f "$BUILD_SCRIPT" ]; then
        print_error "Build script not found: $BUILD_SCRIPT"
        exit 1
    fi

    chmod +x "$BUILD_SCRIPT"
    ./"$BUILD_SCRIPT" build_all
}

ask_yes_no() {
    local prompt="$1"
    local default="${2:-n}"
    local default_str

    if [ "$default" = "y" ]; then
        default_str="[Y/n]"
    else
        default_str="[y/N]"
    fi

    while true; do
        read -p "$prompt $default_str: " response
        response=${response:-$default}
        case $response in
            [Yy]*)
                return 0
                ;;
            [Nn]*)
                return 1
                ;;
            *)
                echo "Please answer yes or no."
                ;;
        esac
    done
}

main() {
    print_header "Neo-Darwin Setup Wizard"

    echo "This wizard will guide you through:"
    echo "  1. Checking Python installation"
    echo "  2. Setting up Python virtual environment"
    echo "  3. Installing required packages"
    echo "  4. Running configuration wizard"
    echo "  5. Building all parts"
    echo ""

    if ! ask_yes_no "Continue?"; then
        echo "Setup cancelled."
        exit 0
    fi

    # Step 1: Check Python
    check_python

    # Step 2: Setup venv
    setup_venv

    # Step 3: Activate venv
    activate_venv

    # Step 4: Install dependencies
    install_dependencies

    # Step 5: Run configuration
    run_configure

    # Step 6: Build parts
    if ask_yes_no "Build all parts now?"; then
        build_parts
    fi

    print_header "Setup Complete"

    echo ""
    echo "Your Neo-Darwin environment is ready!"
    echo ""
    echo "STL files are in the 'stl' directory"
    echo ""
    echo "To build parts in the future:"
    echo "  1. Activate venv: source $VENV_DIR/bin/activate"
    echo "  2. Build parts: ./$BUILD_SCRIPT build_all"
    echo ""
    print_success "Happy building!"
}

main "$@"
