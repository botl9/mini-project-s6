#!/usr/bin/env bash
set -euo pipefail

if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Run scripts/setup.sh first."
  exit 1
fi

source venv/bin/activate
python GUI.py
