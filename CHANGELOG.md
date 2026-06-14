# Changelog

All notable changes to this repository are documented here.

## Unreleased

### Changed
- Post-review cleanup: added a new 2026-06-14 review round archive, updated the review methodology to the five-document Performance series, made planning-metrics wording mechanically truthful, removed a dated review-round pointer from the transients reference, and normalized the 2026-05-18 archive to remove local absolute paths and stale filename fossils.
- Added the incident runbook to `.github/documents.json` so PDF, DOCX, and EPUB publication artifacts are generated and validated with the rest of the Performance series.
- Added `wordpress-performance-incident-runbook.md`, a unified operational runbook for active WordPress performance incidents with read-first procedures, rollback steps, verification, and escalation criteria.
- Integrated WordPress 6.4–7.0 performance guidance throughout the general and enterprise checklists, replacing separate “modern additions” appendix framing with section-level guidance for autoloaded options, speculative loading, Performance Lab, PHP/runtime baselines, WP-Cron, frontend loading, and AI/connectors operational review.
- Refreshed the Performance series against WordPress 7.0 on 2026-06-14, including new 7.0 compatibility/performance deltas, PHP runtime guidance, AI/connectors operational cautions, admin/editor regression-test guidance, and real-time-collaboration non-shipping caveats.
- Updated canonical document metadata and `.github/documents.json` versions: `DEVELOPER_REFERENCE.md` to 1.2, the three companion guides to 1.1, and the incident runbook to 0.1.
- Updated Performance Lab feature-plugin verification language against the current WordPress.org plugin page and noted that the featured plugin catalog changes over time.
- Clarified that the committed PDF, DOCX, and EPUB files are intentionally tracked publication artifacts generated from the canonical Markdown sources.
- Normalized the Performance series source map by renaming the enterprise operational checklist to `enterprise-performance-operational-checklist.md` and aligning repo metadata, generation config, and internal links with the new canonical filename.
- Updated artifact validation to read per-document version and status metadata from `.github/documents.json` instead of assuming every source document is `Version 1.0` / `DRAFT`.
- Regenerated and revalidated the full PDF, DOCX, and EPUB publication set after source and metadata updates so release inputs and committed artifacts are back in sync.
- Prepared the repository for publication: keep local planning state and Claude handoff guidance untracked, and align the README/AGENTS workflow notes with that boundary.
- Updated generated document metadata and PDF running heads so each artifact shows its own title, DRAFT status, manifest version, and Dan Knauss as General Editor.
- Applied the 2026-05-18 editorial review fixes across the performance guide documents: Speculative Loading, WP-Cron sequencing, object-cache locks, New Relic instrumentation, autoload vocabulary, cache-layer boundaries, Performance Lab feature-plugin naming, and fragment-cache safety.
- Added Pandoc-based PDF, Word, and EPUB generation workflows for all five guide documents.
- Added repository management scaffolding for AI-assisted editorial work, issue/PR governance, and GSD-style planning state.
- Completed editorial review round 2026-05-18 (phase-1 per-document reviews, phase-2 cross-document audit, synthesis, closeout, and accepted correction passes). See `reviews/rounds/2026-05-18/synthesis.md` and `reviews/rounds/2026-05-18/closeout.md`.

## 0.1.0 - 2026-05-18

- Initial WordPress performance optimization guidance repository.
