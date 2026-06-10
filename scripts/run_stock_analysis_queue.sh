#!/bin/zsh
set -euo pipefail

REPO_ROOT="${0:A:h:h}"
cd "$REPO_ROOT"

mkdir -p logs
/usr/bin/python3 scripts/run_stock_analysis_queue.py >> logs/stock-analysis.log 2>&1
