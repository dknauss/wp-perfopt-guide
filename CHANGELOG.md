# Changelog

All notable changes to this repository are documented here.

## Unreleased

### Changed
- Moved the general “do not start by installing another performance plugin” guidance out of the enterprise checklist, replaced it with enterprise-focused evidence/approval/rollback framing, and fixed generated document task-list rendering by enabling Pandoc task-list parsing.
- Promoted the full Performance series from `DRAFT` to `Released` status and raised the incident runbook to version 1.0 (parity with its 1.1/1.2 siblings) in both the document headers and `.github/documents.json`. Generated PDF/DOCX/EPUB artifacts must be regenerated to embed the new status/version.
- Updated the editorial-board methodology to the current five-document series and added an Incident Runbook Reviewer role (shareable with the Enterprise Checklist Reviewer).
- Normalized the archived 2026-05-18 review round to repo-relative/`~`-relative paths and added a historical banner noting the enterprise-checklist rename and four-to-five document expansion.
- Clarified in `docs/current-metrics.md` that planning phase counts derive from inline `STATE.md`/`ROADMAP.md` tracking rather than materialized phase directories.
- Aligned the PHP-version recommendation wording in `DEVELOPER_REFERENCE.md` with the rest of the series ("recommended baseline for modern performance work").
- Added follow-up incident-runbook hardening from skill forward-testing: communications cadence, estimated procedure times, bounded curl timeouts, fail-closed dynamic verification, clarified WP-CLI profile URL targeting, and approval-gated rollback examples.
- Hardened the incident runbook for multisite and production incident use: site-specific WP-CLI arguments, derived options-table detection, evidence directories, known-good URL capture, authenticated/dynamic verification placeholders, and approval-gated cron execution examples.
- Tightened WordPress 6.9/7.0 chronology for the Abilities API, WP AI Client, Connectors, WordPress 6.9 release date, and WordPress 6.4/6.6 autoload API/vocabulary changes.
- Added pull-request artifact validation coverage and release-time artifact validation before generated documents are published.
- Neutralized source-correction and acknowledgement wording so source courses remain credited without being over-identified as document titles or primary authority.
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
