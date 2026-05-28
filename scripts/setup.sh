#!/usr/bin/env bash
set -euo pipefail

echo "Creating Python virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r Requirements.txt

echo "Setup complete. Activate with: source venv/bin/activate"
