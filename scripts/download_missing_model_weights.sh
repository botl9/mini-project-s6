#!/usr/bin/env bash
set -euo pipefail

MISSING=0

check_file() {
  if [ ! -f "$1" ]; then
    echo "  MISSING: $1"
    MISSING=1
  fi
}

echo "Checking model files..."
check_file "model/model_weights.h5"
check_file "model/history.pckl"
check_file "model/X.txt.npy"
check_file "model/Y.txt.npy"

if [ "$MISSING" -eq 0 ]; then
  echo "All model files present."
  exit 0
fi

echo ""
echo "Some model files are missing. To regenerate them:"
echo "  1. Run the training script to re-train the CNN on CIFAR-10"
echo "  2. Or copy them from a backup if you have one saved elsewhere"
echo ""
echo "The model architecture (model.json) is tracked in git."
echo "Large binary files like .h5 and .npy are gitignored by default."
