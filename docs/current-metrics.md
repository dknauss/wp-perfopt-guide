# Current Metrics

Last updated: 2026-06-14

## Repository

- Primary Markdown guidance files: 5
- Planning phases: 3
- Completed planning phases: 3

> Phase counts reflect the inline plan tracked in `.planning/STATE.md` and `.planning/ROADMAP.md`, which are the source of truth. This project did not materialize per-phase directories under `.planning/phases/`, so the count is not derivable by listing folders — verify it against `STATE.md`/`ROADMAP.md`.

## Canonical Source Files

- `DEVELOPER_REFERENCE.md`
- `wordpress-performance-optimization-checklist.md`
- `enterprise-performance-operational-checklist.md`
- `REFERENCE-WP-Transients-Persistent-Object-Cache.md`
- `wordpress-performance-incident-runbook.md`

## Generated document artifacts

- PDF artifacts: 5
- DOCX artifacts: 5
- EPUB artifacts: 5
- Artifact validation: passed locally on 2026-06-14

## Generated artifact metadata

- Status: Released
- Versioning: per-document manifest values (`DEVELOPER_REFERENCE.md` 1.2; three companion guides 1.1; incident runbook 1.0)
- General Editor: Dan Knauss
- PDF running heads: per-document titles
- Stale inherited header check: passed locally on 2026-06-14
- Source-sensitive currency: refreshed against WordPress 7.0 on 2026-06-14

> The generated PDF/DOCX/EPUB artifacts in the repository root still embed the prior `DRAFT` status and runbook version `0.1`; they must be regenerated with `npm run docs:generate` (Pandoc + XeLaTeX) to match the `Released` / runbook-1.0 source metadata above.
