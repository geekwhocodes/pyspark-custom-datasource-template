#!/bin/bash

# Define the virtual environment directory
VENV_DIR=".venv"

# Check if the virtual environment already exists
if [[ ! -d "$VENV_DIR" ]]; then
    echo "Creating virtual environment..."
    python -m venv "$VENV_DIR"
    echo "Virtual environment created at $VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
if [[ -f "$VENV_DIR/bin/activate" ]]; then
    echo "Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
    echo "Virtual environment activated."
    poetry add ipykernel
    poetry install

    source .venv/bin/activate

else
    echo "Error: Unable to activate virtual environment."
    exit 1
fi
