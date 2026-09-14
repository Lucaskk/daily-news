#!/bin/zsh
cd "$(dirname "$0")/.." || exit 1
/usr/bin/python3 scripts/news_workflow.py mode legacy
