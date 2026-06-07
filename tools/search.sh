#!/usr/bin/env bash
# tools/search.sh — full-text search across wiki/ pages
# Usage: bash tools/search.sh "<search terms>"
# Output: one project-relative file path per line (no match context)
# Exit 0 when results found, 1 when no results or wiki/ absent

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 \"<search terms>\"" >&2
  exit 1
fi

QUERY="$1"
WIKI_DIR="wiki"

# Empty wiki guard
if [ ! -d "$WIKI_DIR" ] || [ -z "$(ls -A "$WIKI_DIR" 2>/dev/null)" ]; then
  exit 1
fi

# Use ripgrep if available (preferred)
if command -v rg &>/dev/null; then
  rg --type md -il "$QUERY" "$WIKI_DIR" 2>/dev/null
  exit $?
fi

# Fallback: grep -r (case-insensitive)
grep -ril "$QUERY" "$WIKI_DIR" --include="*.md" 2>/dev/null
exit $?
