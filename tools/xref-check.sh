#!/usr/bin/env bash
# tools/xref-check.sh — cross-reference integrity checker
# Scans wiki/ subdirectory pages for [[target]] refs; verifies each target exists
# Output: "BROKEN: <source> → <target>" per broken ref (stdout)
# Exit 0 when clean, 1 when broken refs found

set -euo pipefail

WIKI_DIR="wiki"
BROKEN=0

# Empty wiki guard
if [ ! -d "$WIKI_DIR" ] || [ -z "$(ls -A "$WIKI_DIR" 2>/dev/null)" ]; then
  exit 0
fi

# Find all markdown files in wiki/ (not index.md or log.md — those use regular links)
while IFS= read -r -d '' SOURCE; do
  # Extract all [[target]] references from this file (BSD grep compatible)
  while IFS= read -r TARGET; do
    # Strip surrounding [[ and ]]
    TARGET="${TARGET#\[\[}"
    TARGET="${TARGET%\]\]}"
    # Resolve relative to repo root
    if [ ! -f "$TARGET" ]; then
      echo "BROKEN: $SOURCE → $TARGET"
      BROKEN=1
    fi
  done < <(grep -oE '\[\[[^]]+\]\]' "$SOURCE" 2>/dev/null || true)
done < <(find "$WIKI_DIR" -name "*.md" -print0 2>/dev/null)

exit $BROKEN
