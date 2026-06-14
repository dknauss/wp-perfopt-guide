#!/usr/bin/env python3
"""Smoke-check generated PDF, EPUB, and DOCX artifacts for every configured document."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET
from zipfile import ZipFile


class ValidationError(Exception):
    """Artifact validation failed."""


def normalize_text(text: str) -> str:
    text = (
        text.replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u00a0", " ")
    )
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_{}\\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.:;!?])", r"\1", text)
    text = re.sub(r"([\[(])\s+", r"\1", text)
    text = re.sub(r"\s+([\])])", r"\1", text)
    text = re.sub(r'(["\'])\s+', r"\1", text)
    text = re.sub(r'\s+(["\'])', r"\1", text)
    return text




def extract_markdown_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^(#{2,4})\s+(.+?)\s*$", line)
        if match:
            headings.append(re.sub(r"\s+#+$", "", match.group(2)).strip())
    return headings


def assert_all_headings_present(markdown_text: str, rendered_texts: dict[str, str], base: str) -> None:
    headings = extract_markdown_headings(markdown_text)
    if not headings:
        return
    for label, text in rendered_texts.items():
        if label == "Markdown":
            continue
        haystack = normalize_text(text).casefold()
        missing = [heading for heading in headings if normalize_text(heading).casefold() not in haystack]
        if missing:
            preview = "; ".join(missing[:8])
            if len(missing) > 8:
                preview += f"; ... ({len(missing)} total)"
            raise ValidationError(f"{label} missing source Markdown headings for {base}: {preview}")
    print(f"OK   [Coverage] {len(headings)} source Markdown headings found in generated artifacts")

def assert_contains(text: str, tokens: Iterable[str], label: str) -> None:
    haystack = normalize_text(text).casefold()
    missing = [token for token in tokens if normalize_text(token).casefold() not in haystack]
    if missing:
        raise ValidationError(f"{label} missing expected text: {', '.join(missing)}")


def ensure_exists(path: Path, label: str) -> None:
    if not path.is_file():
        raise ValidationError(f"{label} not found: {path}")
    if path.stat().st_size <= 0:
        raise ValidationError(f"{label} is empty: {path}")
    print(f"OK   [{label}] exists ({path.stat().st_size} bytes)")


def extract_pdf_text(path: Path) -> str:
    try:
        result = subprocess.run(["pdftotext", str(path), "-"], check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise ValidationError("pdftotext is required but was not found on PATH") from exc
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() or "unknown error"
        raise ValidationError(f"pdftotext failed for {path}: {stderr}") from exc
    if not result.stdout.strip():
        raise ValidationError(f"pdftotext produced no text for {path}")
    return result.stdout


def extract_xml_text(xml_bytes: bytes) -> str:
    root = ET.fromstring(xml_bytes)
    return " ".join(text for text in root.itertext() if text and text.strip())


def validate_docx(path: Path, title: str, markers: list[str], version: str, status: str, general_editor: str) -> str:
    ensure_exists(path, "DOCX")
    with ZipFile(path) as archive:
        for member in ("[Content_Types].xml", "_rels/.rels", "docProps/core.xml", "word/document.xml"):
            if member not in archive.namelist():
                raise ValidationError(f"DOCX missing required member: {member}")
        document_xml = archive.read("word/document.xml")
        document_text = extract_xml_text(document_xml)
        if b"checkbox" in document_xml or "☐" in document_text:
            document_text += " ☐"
        assert_contains(document_text, [title, "Version", version, status, "General Editor", general_editor, *markers[:2]], "DOCX")
        if "WordPress Security Hardening Guide" in document_text:
            raise ValidationError(f"DOCX contains stale running head from old template: {path}")
    print("OK   [DOCX] structure and canonical text markers found")
    return document_text


def validate_epub(path: Path, title: str, markers: list[str], version: str, status: str, general_editor: str) -> str:
    ensure_exists(path, "EPUB")
    with ZipFile(path) as archive:
        mimetype = archive.read("mimetype").decode("utf-8", errors="ignore").strip()
        if mimetype != "application/epub+zip":
            raise ValidationError(f"EPUB mimetype mismatch: {mimetype!r}")
        for member in ("META-INF/container.xml", "EPUB/content.opf", "EPUB/nav.xhtml"):
            if member not in archive.namelist():
                raise ValidationError(f"EPUB missing required member: {member}")
        xhtml_members = [name for name in archive.namelist() if name.endswith(".xhtml")]
        if not xhtml_members:
            raise ValidationError("EPUB contains no XHTML content files")
        joined_text = " ".join(extract_xml_text(archive.read(member)) for member in xhtml_members)
        assert_contains(joined_text, [title, "Version", version, status, "General Editor", general_editor, *markers[:2]], "EPUB")
        if "WordPress Security Hardening Guide" in joined_text:
            raise ValidationError(f"EPUB contains stale running head from old template: {path}")
    print("OK   [EPUB] structure and canonical text markers found")
    return joined_text


def validate_markdown(path: Path, title: str, markers: list[str], version: str, status: str, general_editor: str) -> str:
    ensure_exists(path, "Markdown")
    text = path.read_text(encoding="utf-8")
    assert_contains(text, [title, "Status", status, "Version", version, "General Editor", general_editor, *markers[:2]], "Markdown")
    if "WordPress Security Hardening Guide" in text:
        raise ValidationError(f"Markdown contains stale running head from old template: {path}")
    print("OK   [Markdown] canonical text markers found")
    return text


def validate_pdf(path: Path, title: str, markers: list[str], intro_marker: str, version: str, status: str, general_editor: str) -> str:
    ensure_exists(path, "PDF")
    text = extract_pdf_text(path)
    assert_contains(text, [title, f"Version {version}", status, f"{general_editor}, General Editor", intro_marker, "Table of Contents", *markers[:2]], "PDF")
    intro_index = text.find(intro_marker)
    toc_index = text.find("Table of Contents")
    if toc_index < intro_index:
        raise ValidationError(f"PDF table of contents appears before intro text: {path}")
    if "WordPress Security Hardening Guide" in text:
        raise ValidationError(f"PDF contains stale running head from old template: {path}")
    print("OK   [PDF] canonical text markers and document metadata found")
    return text


def validate_doc(doc: dict, root: Path) -> None:
    source = root / doc["source"]
    base = doc["base"]
    title = doc["title"]
    markers = doc.get("markers", [])
    version = doc.get("version", "1.0")
    status = doc.get("status", "DRAFT")
    general_editor = doc.get("general_editor", "Dan Knauss")
    print(f"\n==> Validating {base}")
    texts = {
        "Markdown": validate_markdown(source, title, markers, version, status, general_editor),
        "PDF": validate_pdf(root / f"{base}.pdf", title, markers, doc.get("intro_marker", title), version, status, general_editor),
        "EPUB": validate_epub(root / f"{base}.epub", title, markers, version, status, general_editor),
        "DOCX": validate_docx(root / f"{base}.docx", title, markers, version, status, general_editor),
    }
    for label, text in texts.items():
        assert_contains(text, markers, label)
    assert_all_headings_present(texts["Markdown"], texts, base)
    if re.search(r"(?m)^\s*- \[ \]", texts["Markdown"]):
        for label in ("PDF", "EPUB", "DOCX"):
            if "[ ]" in texts[label]:
                raise ValidationError(f"{label} contains literal task-list brackets instead of rendered checkboxes: {base}")
        print("OK   [Task lists] generated artifacts do not expose literal [ ] markers")
    print(f"OK   [Parity] canonical phrases match across {len(texts)} formats")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=".github/documents.json", help="Document manifest path")
    parser.add_argument("--root", default=".", help="Repository/artifact root")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    try:
        docs = json.loads((root / args.manifest).read_text(encoding="utf-8"))
        for doc in docs:
            validate_doc(doc, root)
    except (ValidationError, KeyError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print(f"\nAll artifact and parity checks passed ({len(docs)} documents, 4 formats each).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
