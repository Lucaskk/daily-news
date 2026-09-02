#!/bin/zsh
set -euo pipefail

REPO_ROOT="${0:A:h:h}"
LABEL="com.lucaskk.daily-news.stock-analysis"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
INSTALL_DIR="$HOME/Library/Application Support/daily-news-stock-analysis"
RUNTIME_ROOT="$INSTALL_DIR/runtime"
LAUNCHER="$INSTALL_DIR/run.sh"

mkdir -p "$HOME/Library/LaunchAgents" "$RUNTIME_ROOT/scripts"
cp "$REPO_ROOT/scripts/generate_stock_analysis.py" "$RUNTIME_ROOT/scripts/"
cp "$REPO_ROOT/scripts/run_stock_analysis_queue.py" "$RUNTIME_ROOT/scripts/"
if [[ -f "$REPO_ROOT/.env" ]]; then
  cp "$REPO_ROOT/.env" "$RUNTIME_ROOT/.env"
  chmod 600 "$RUNTIME_ROOT/.env"
fi
cat > "$LAUNCHER" <<EOF
#!/bin/zsh
set -euo pipefail
cd "$RUNTIME_ROOT"
/usr/bin/python3 scripts/run_stock_analysis_queue.py >> "$INSTALL_DIR/stock-analysis.log" 2>&1
EOF
chmod +x "$LAUNCHER"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>$LAUNCHER</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$INSTALL_DIR</string>
  <key>StartInterval</key>
  <integer>60</integer>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$INSTALL_DIR/launchd.log</string>
  <key>StandardErrorPath</key>
  <string>$INSTALL_DIR/launchd-error.log</string>
</dict>
</plist>
EOF

chmod +x "$REPO_ROOT/scripts/run_stock_analysis_queue.sh"
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl kickstart -k "gui/$(id -u)/$LABEL"
echo "Installed $LABEL (runs every minute)"
