#!/usr/bin/env bash
# tools/lint-scan.sh — wiki health scanner
# Detects: orphan-filesystem, orphan-index, missing-frontmatter, broken-sources
# Output: "ISSUE:<severity>:<type>:<path>" per issue (stdout)
# Exit 0 when clean, 1 when issues found

set -euo pipefail

WIKI_DIR="wiki"
INDEX_FILE="index.md"
RAW_DIR="raw"
ISSUES=0

# Required frontmatter fields (data-model.md §WikiPage)
REQUIRED_FIELDS=("title:" "type:" "sources:" "status:" "created:" "last_updated:")

# Empty wiki guard
if [ ! -d "$WIKI_DIR" ] || [ -z "$(ls -A "$WIKI_DIR" 2>/dev/null)" ]; then
  exit 0
fi

# ── 1. orphan-filesystem: wiki page exists on disk but has no index.md entry ──
if [ -f "$INDEX_FILE" ]; then
  while IFS= read -r -d '' PAGE; do
    # Convert to project-relative path
    REL="${PAGE#./}"
    if ! grep -qF "$REL" "$INDEX_FILE" 2>/dev/null; then
      echo "ISSUE:Error:orphan-filesystem:$REL"
      ISSUES=1
    fi
  done < <(find "$WIKI_DIR" -name "*.md" -not -path "*/meta/*" -print0 2>/dev/null)
fi

# ── 2. orphan-index: index.md entry points to a file that does not exist ──
if [ -f "$INDEX_FILE" ]; then
  # Extract all markdown link targets from index.md: [Title](path)
  while IFS= read -r TARGET; do
    if [ ! -f "$TARGET" ]; then
      echo "ISSUE:Error:orphan-index:$TARGET"
      ISSUES=1
    fi
  done < <(grep -v '^\s*<!--' "$INDEX_FILE" 2>/dev/null | grep -oE '\]\([^)]+\.md\)' | sed 's/^](\(.*\))$/\1/' || true)
fi

# ── 3. missing-frontmatter: wiki page missing any of the 6 required fields ──
while IFS= read -r -d '' PAGE; do
  REL="${PAGE#./}"
  # Read YAML frontmatter block (between first pair of ---)
  FRONTMATTER=$(awk '/^---$/{if(p)exit;p=1;next}p' "$PAGE" 2>/dev/null || true)
  for FIELD in "${REQUIRED_FIELDS[@]}"; do
    if ! echo "$FRONTMATTER" | grep -q "^${FIELD}"; then
      echo "ISSUE:Error:missing-frontmatter:$REL (missing: $FIELD)"
      ISSUES=1
    fi
  done
done < <(find "$WIKI_DIR" -name "*.md" -not -path "*/meta/*" -print0 2>/dev/null)

# ── 4. broken-sources: sources[] lists a filename not present in raw/ ──
while IFS= read -r -d '' PAGE; do
  REL="${PAGE#./}"
  # Extract sources list items (lines like "  - filename.md" inside sources: block)
  IN_SOURCES=0
  while IFS= read -r LINE; do
    if echo "$LINE" | grep -q "^sources:"; then
      IN_SOURCES=1
      continue
    fi
    if [ $IN_SOURCES -eq 1 ]; then
      # List item under sources:
      if echo "$LINE" | grep -q "^  - "; then
        SRC=$(echo "$LINE" | sed 's/^  - //' | tr -d '"' | tr -d "'")
        if [ -n "$SRC" ] && [ ! -f "$RAW_DIR/$SRC" ]; then
          echo "ISSUE:Error:broken-sources:$REL (missing raw/$SRC)"
          ISSUES=1
        fi
      else
        # Left the sources block
        IN_SOURCES=0
      fi
    fi
  done < "$PAGE"
done < <(find "$WIKI_DIR" -name "*.md" -not -path "*/meta/*" -print0 2>/dev/null)

# ── 5. Warning: stale or contested pages ──
while IFS= read -r -d '' PAGE; do
  REL="${PAGE#./}"
  if grep -q "^status: stale" "$PAGE" 2>/dev/null; then
    echo "ISSUE:Warning:stale:$REL"
    ISSUES=1
  elif grep -q "^status: contested" "$PAGE" 2>/dev/null; then
    echo "ISSUE:Warning:contested:$REL"
    ISSUES=1
  fi
done < <(find "$WIKI_DIR" -name "*.md" -not -path "*/meta/*" -print0 2>/dev/null)

# ── 6. Info: wiki pages with empty sources list ──
while IFS= read -r -d '' PAGE; do
  REL="${PAGE#./}"
  if grep -q "^sources: \[\]" "$PAGE" 2>/dev/null; then
    echo "ISSUE:Info:no-sources:$REL"
  fi
done < <(find "$WIKI_DIR" -name "*.md" -not -path "*/meta/*" -print0 2>/dev/null)

exit $ISSUES
