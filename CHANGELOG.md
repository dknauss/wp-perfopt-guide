# Changelog

All notable changes to this repository are documented here.

## Unreleased

### Changed
- Normalized the Performance series source map by renaming the enterprise operational checklist to `enterprise-performance-operational-checklist.md` and aligning repo metadata, generation config, and internal links with the new canonical filename.
- Updated artifact validation to read per-document version and status metadata from `.github/documents.json` instead of assuming every source document is `Version 1.0` / `DRAFT`.
- Regenerated and revalidated the full PDF, DOCX, and EPUB publication set after the Performance series filename normalization so release inputs and committed artifacts are back in sync.

- Prepare the repository for publication: keep local planning state and Claude handoff guidance untracked, and align the README/AGENTS workflow notes with that boundary.
- Updated generated document metadata and PDF running heads so each artifact shows its own title, DRAFT status, version 1.0, and Dan Knauss as General Editor.
- Generated and validated PDF, DOCX, and EPUB artifacts for all four guide documents.
- Applied the 2026-05-18 editorial review fixes across the performance guide documents: Speculative Loading, WP-Cron sequencing, object-cache locks, New Relic instrumentation, autoload vocabulary, cache-layer boundaries, Performance Lab feature-plugin naming, and fragment-cache safety.
- Added Pandoc-based PDF, Word, and EPUB generation workflows for all four guide documents.
- Added repository management scaffolding for AI-assisted editorial work, issue/PR governance, and GSD-style planning state.
- Completed editorial review round 2026-05-18 (phase-1 per-document reviews, phase-2 cross-document audit, synthesis). See `reviews/rounds/2026-05-18/synthesis.md`.
- Closeout decisions recorded with per-finding source-origin classification and Codex-executable edit plan. See `reviews/rounds/2026-05-18/closeout.md`. All P0/P1/P2/P3 findings accepted; pending execution across passes 0–5.
- Scheduled corrections for source-derived issues inherited from Remkus and WP VIP source material: `DISABLE_WP_CRON` sequencing (P0.3), New Relic transaction API misuse (P1.2), WP-CLI package availability caveats (P2.2), autoload vocabulary in body text (P2.3), and `/wp-json` in Core Web Vitals baseline table (P3.2).
- Scheduled corrections for synthesis-introduced issues: Speculative Loading Core vs plugin behavior (P0.1), WordPress 6.8 → 6.9 currency refresh (P1.1), Performance Lab feature-plugin list refresh (P1.4), broken sibling-folder cross-references and stray attribution tokens (P3.1), OPcache JIT and Critical CSS 14 KB wording and Redis recommendation framing (P3.3).

## 0.1.0 - 2026-05-18

- Initial WordPress performance optimization guidance repository.
