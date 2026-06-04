#!/usr/bin/env python3
"""Build a Pandoc input file with the generated TOC after the intro."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_{}\\]", "", text).strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def make_toc(body: str) -> str:
    counters: dict[str, int] = {}
    lines = ["# Table of Contents", ""]
    for line in body.splitlines():
        match = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        anchor = slugify(title)
        # Match Pandoc's duplicate-anchor style well enough for repeated headings.
        seen = counters.get(anchor, 0)
        counters[anchor] = seen + 1
        if seen:
            anchor = f"{anchor}-{seen}"
        indent = "  " * (level - 2)
        lines.append(f"{indent}- [{title}](#{anchor})")
    lines.append("")
    return "\n".join(lines)


def split_intro(source: str) -> tuple[str, str]:
    match = re.search(r"^##\s+", source, flags=re.MULTILINE)
    if not match:
        return source.rstrip(), ""
    return source[: match.start()].rstrip(), source[match.start() :].lstrip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("output")
    args = parser.parse_args()

    source_path = Path(args.source)
    output_path = Path(args.output)
    source = source_path.read_text(encoding="utf-8")
    intro, body = split_intro(source)
    toc = make_toc(body)

    # Raw TeX page breaks affect PDF output. They are ignored by DOCX/EPUB writers.
    output = f"{intro}\n\n\\newpage\n\n{toc}\n\\newpage\n\n{body.rstrip()}\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
