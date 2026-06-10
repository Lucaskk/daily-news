#!/bin/zsh
set -euo pipefail

REPO_ROOT="${0:A:h:h}"
LABEL="com.lucaskk.daily-news.stock-analysis"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"

mkdir -p "$HOME/Library/LaunchAgents" "$REPO_ROOT/logs"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>$REPO_ROOT/scripts/run_stock_analysis_queue.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$REPO_ROOT</string>
  <key>StartInterval</key>
  <integer>900</integer>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$REPO_ROOT/logs/stock-analysis-launchd.log</string>
  <key>StandardErrorPath</key>
  <string>$REPO_ROOT/logs/stock-analysis-launchd-error.log</string>
</dict>
</plist>
EOF

chmod +x "$REPO_ROOT/scripts/run_stock_analysis_queue.sh"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl kickstart -k "gui/$(id -u)/$LABEL"
echo "Installed $LABEL (runs every 15 minutes)"
