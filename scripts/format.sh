#!/usr/bin/env bash
set -euo pipefail

if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Run scripts/setup.sh first."
  exit 1
fi

source venv/bin/activate

echo "Running black (code formatter)..."
black .

echo "Running ruff (linter)..."
ruff check . --fix

echo "Formatting complete."
