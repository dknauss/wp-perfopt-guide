#!/usr/bin/env bash
set -euo pipefail

manifest="${1:-.github/documents.json}"
out_dir="${2:-.}"
mkdir -p "$out_dir"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc is required" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi

mkdir -p .github/pandoc
if [ ! -f .github/pandoc/reference.docx ]; then
  pandoc --print-default-data-file reference.docx > .github/pandoc/reference.docx
fi

if command -v xelatex >/dev/null 2>&1; then
  pdf_engine=xelatex
elif command -v tectonic >/dev/null 2>&1; then
  pdf_engine=tectonic
else
  echo "xelatex or tectonic is required for PDF generation" >&2
  exit 1
fi
echo "Using PDF engine: $pdf_engine"

python3 - "$manifest" <<'PY' | while IFS=$'\t' read -r source base title version status general_editor; do
import json, sys
from pathlib import Path
for doc in json.loads(Path(sys.argv[1]).read_text()):
    print("\t".join([
        doc['source'],
        doc['base'],
        doc['title'],
        doc.get('version', '1.0'),
        doc.get('status', 'DRAFT'),
        doc.get('general_editor', 'Dan Knauss'),
    ]))
PY
  if [ ! -f "$source" ]; then
    echo "Missing source: $source" >&2
    exit 1
  fi

  work_file="${TMPDIR:-/tmp}/${base}.pandoc.md"
  docx_file="$out_dir/${base}.docx"
  pdf_file="$out_dir/${base}.pdf"
  epub_file="$out_dir/${base}.epub"

  echo "Generating $base from $source"
  subtitle="Version ${version} — ${status}"
  author="${general_editor}, General Editor"
  python3 .github/scripts/build-doc-input.py "$source" "$work_file"

  pandoc "$work_file" \
    --from markdown-task_lists \
    --metadata "title=${title}" \
    --metadata "subtitle=${subtitle}" \
    --metadata "author=${author}" \
    --metadata "version=${version}" \
    --metadata "status=${status}" \
    --reference-doc=".github/pandoc/reference.docx" \
    -o "$docx_file"

  pandoc "$docx_file" \
    --from docx \
    --metadata "title=${title}" \
    --metadata "subtitle=${subtitle}" \
    --metadata "author=${author}" \
    --metadata "version=${version}" \
    --metadata "status=${status}" \
    --variable "header-left=${title}" \
    --template eisvogel \
    --pdf-engine "$pdf_engine" \
    --defaults ".github/pandoc/pdf-defaults.yaml" \
    -o "$pdf_file"

  pandoc "$docx_file" \
    --from docx \
    --metadata "title=${title}" \
    --metadata "subtitle=${subtitle}" \
    --metadata "author=${author}" \
    --metadata "version=${version}" \
    --metadata "status=${status}" \
    --css ".github/pandoc/epub.css" \
    --epub-title-page=false \
    --metadata "lang=en-US" \
    -o "$epub_file"
done
