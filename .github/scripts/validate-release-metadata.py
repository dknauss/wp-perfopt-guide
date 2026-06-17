#!/usr/bin/env python3
"""Validate release metadata for the Performance series manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


class ValidationError(Exception):
    """Metadata validation failed."""


def normalize_semver(version: str) -> str:
    version = version.strip()
    if not re.fullmatch(r"\d+\.\d+(?:\.\d+)?", version):
        raise ValidationError(f"Version is not semver-like: {version!r}")
    parts = version.split('.')
    if len(parts) == 2:
        parts.append('0')
    return '.'.join(str(int(part)) for part in parts)


def parse_expected_tag(value: str | None) -> str | None:
    if not value:
        return None
    return normalize_semver(value.removeprefix('refs/tags/').removeprefix('v'))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', default='.github/documents.json', help='Path to documents manifest')
    parser.add_argument('--expected-tag', help='Optional batch release tag, validated for semver shape only')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest_path = Path(args.manifest)
        docs = json.loads(manifest_path.read_text(encoding='utf-8'))
        if not isinstance(docs, list) or not docs:
            raise ValidationError(f"Manifest must contain a non-empty list: {manifest_path}")

        seen_sources: set[str] = set()
        seen_bases: set[str] = set()
        allowed_statuses = {'Released', 'DRAFT'}

        for doc in docs:
            for key in ('source', 'base', 'title', 'version', 'status'):
                if key not in doc or not str(doc[key]).strip():
                    raise ValidationError(f"Manifest entry missing required {key!r}: {doc}")
            source = str(doc['source']).strip()
            base = str(doc['base']).strip()
            version = str(doc['version']).strip()
            status = str(doc['status']).strip()
            if source in seen_sources:
                raise ValidationError(f"Duplicate source in manifest: {source}")
            if base in seen_bases:
                raise ValidationError(f"Duplicate base in manifest: {base}")
            seen_sources.add(source)
            seen_bases.add(base)
            normalize_semver(version)
            if status not in allowed_statuses:
                raise ValidationError(f"Unsupported status {status!r} for {base}; expected one of {sorted(allowed_statuses)}")
            if not (manifest_path.parent.parent / source).is_file():
                raise ValidationError(f"Source file listed in manifest does not exist: {source}")

        expected_tag = parse_expected_tag(args.expected_tag)
        if expected_tag:
            print(f"OK   [Batch release tag] normalized={expected_tag}")
        print(f"OK   [Manifest documents] {len(docs)}")
        for doc in docs:
            normalized = normalize_semver(str(doc['version']))
            print(f"OK   [Document] {doc['base']} version={doc['version']} normalized={normalized} status={doc['status']}")
        print('Release metadata validation passed.')
        return 0
    except (ValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
