#!/usr/bin/env bash
set -euo pipefail

echo "Cleaning up temporary files..."

find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.so" -delete
find . -type f -name "*.egg-info" -delete

rm -rf .pytest_cache/
rm -rf venv/
rm -f test.jpg
rm -f temp_input.mp4
rm -f motion_input.mp4

echo "Done."
