#!/usr/bin/env bash
# Sync notes from the raw survey folder into this repo (PDFs and extracted texts are excluded).
set -euo pipefail
SRC="${1:-$HOME/Desktop/research/ot_variants_survey}"
DST="$(cd "$(dirname "$0")/.." && pwd)"
rsync -av --delete \
  --exclude '*.pdf' --exclude 'paper.txt' --exclude '.DS_Store' \
  --exclude '.git/' --exclude 'README.md' --exclude 'LICENSE' --exclude '.gitignore' --exclude 'scripts/' \
  "$SRC/" "$DST/"
python3 "$DST/scripts/build_readme.py"
