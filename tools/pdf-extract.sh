#!/usr/bin/env bash
# tools/pdf-extract.sh — PDF-to-text extraction wrapper
# Usage: bash tools/pdf-extract.sh <input.pdf>
# Output: extracted text to stdout; also saves as raw/<basename>.txt
# Exit 0 on success, 1 on failure (error message to stderr)

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <input.pdf>" >&2
  exit 1
fi

INPUT="$1"
BASENAME="$(basename "$INPUT" .pdf)"
OUTFILE="raw/${BASENAME}.txt"

if [ ! -f "$INPUT" ]; then
  echo "Error: file not found: $INPUT" >&2
  exit 1
fi

# Try pdftotext (poppler) first
if command -v pdftotext &>/dev/null; then
  pdftotext "$INPUT" "$OUTFILE"
  TEXT=$(cat "$OUTFILE")
  WORD_COUNT=$(echo "$TEXT" | wc -w | tr -d ' ')
  NON_ALPHA=$(echo "$TEXT" | tr -cd '[:alpha:][:digit:] \n' | wc -c | tr -d ' ')
  TOTAL=$(echo "$TEXT" | wc -c | tr -d ' ')

  # Guard: garbled output detection
  if [ "$WORD_COUNT" -lt 100 ] 2>/dev/null; then
    echo "Error: extracted text too short ($WORD_COUNT words); PDF may be image-only or extraction failed" >&2
    rm -f "$OUTFILE"
    exit 1
  fi

  cat "$OUTFILE"
  echo "Extracted to: $OUTFILE" >&2
  exit 0
fi

# Fallback: pdfplumber (Python)
if command -v python3 &>/dev/null && python3 -c "import pdfplumber" &>/dev/null; then
  python3 - "$INPUT" "$OUTFILE" <<'PYEOF'
import sys
import pdfplumber

input_path, output_path = sys.argv[1], sys.argv[2]
with pdfplumber.open(input_path) as pdf:
    text = "\n\n".join(page.extract_text() or "" for page in pdf.pages)

if len(text.split()) < 100:
    print(f"Error: extracted text too short; PDF may be image-only", file=sys.stderr)
    sys.exit(1)

with open(output_path, "w") as f:
    f.write(text)

print(text)
PYEOF
  echo "Extracted to: $OUTFILE (via pdfplumber)" >&2
  exit 0
fi

echo "Error: neither pdftotext nor pdfplumber is available. Install with:" >&2
echo "  brew install poppler     # provides pdftotext" >&2
echo "  pip install pdfplumber   # Python fallback" >&2
exit 1
