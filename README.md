# WordPress Performance Optimization Guide
[![AI Authorship](https://img.shields.io/badge/AI%20authorship-disclosed-8a63d2.svg)](docs/ai-authorship.md)


General and enterprise WordPress performance optimization guidance for developers, technical leads, and operators. Together, the four canonical source documents in this repository form the **Performance series**.

## Contents

- [`DEVELOPER_REFERENCE.md`](DEVELOPER_REFERENCE.md) — unified developer reference and diagnostic model.
- [`wordpress-performance-optimization-checklist.md`](wordpress-performance-optimization-checklist.md) — general checklist and triage flow.
- [`enterprise-performance-operational-checklist.md`](enterprise-performance-operational-checklist.md) — enterprise/WP VIP-oriented operational checklist.
- [`REFERENCE-WP-Transients-Persistent-Object-Cache.md`](REFERENCE-WP-Transients-Persistent-Object-Cache.md) — focused reference on transients and persistent object caching.

## Working Principles

- Measure first, optimize second.
- Keep cache layers and responsibilities distinct.
- Preserve correctness, security, editorial workflows, and user-critical flows.
- State assumptions about hosting, cache plugins, CDNs, traffic patterns, and WordPress versions.
- Verify source-sensitive claims before updating guidance.

## Repository Management

This repository uses the same AI-assisted management pattern as related local documentation repositories:

- `AGENTS.md` contains editorial and agent instructions.
- `.github/` contains owner, issue, pull request, and dependency-management scaffolding.
- `reviews/` contains editorial review rounds, synthesis, and correction rationale that explain important source-sensitive changes.
- `CHANGELOG.md` records meaningful documentation and governance changes.

Local planning state may exist during drafting, but publication focuses on the canonical Markdown sources, supporting review history, and generated artifacts.

## License

See [`LICENSE`](LICENSE).

## Generated Documents

PDF, Word, and EPUB artifacts are generated from the four source Markdown files with Pandoc and the Eisvogel LaTeX template.

Configured source documents live in [`.github/documents.json`](.github/documents.json). The GitHub Actions workflow [`.github/workflows/generate-docs.yml`](.github/workflows/generate-docs.yml) generates and validates:

- `WordPress-Performance-Optimization-Developer-Reference.{pdf,docx,epub}`
- `WordPress-Performance-Optimization-Checklist.{pdf,docx,epub}`
- `Enterprise-WordPress-Performance-Operational-Checklist.{pdf,docx,epub}`
- `WordPress-Transients-Persistent-Object-Cache-Reference.{pdf,docx,epub}`

Local generation requires Pandoc, XeLaTeX, the Eisvogel template, and `pdftotext` for validation:

```bash
npm run docs:generate
npm run docs:validate
```
