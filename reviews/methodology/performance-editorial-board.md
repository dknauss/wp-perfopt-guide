# Performance Editorial Board Methodology

This repository adapts the `ai-assisted-docs` multi-model editorial review process for a five-document WordPress performance guide.

## Phases

1. **Preflight:** Confirm round files, document inventory, and metrics snapshot.
2. **Independent document reviews:** Each reviewer audits one document without seeing other reviewers' findings.
3. **Cross-document audit:** Compare overlapping guidance and identify contradictions, missing caveats, and repeated-but-divergent recommendations.
4. **Synthesis:** Merge findings into a prioritized human-editable revision plan.
5. **Closeout:** Mark each accepted finding as applied, rejected, or deferred/stale.

## Reviewer Roles

- **Developer Reference Reviewer:** architecture, mental model, source hierarchy, diagnostic workflow.
- **General Checklist Reviewer:** practical triage order, frontend/backend coverage, verification steps.
- **Enterprise Checklist Reviewer:** WP VIP/platform specificity, operational safety, high-traffic readiness.
- **Transients/Object Cache Reviewer:** Transients API, object cache semantics, expiration, stampede/race risks.
- **Incident Runbook Reviewer:** active-incident response flow, operational safety, escalation, rollback, and evidence capture.
- **Cross-Document Auditor:** overlap, terminology drift, sequence conflicts, and version-sensitive claims across all documents.
- **Synthesis Editor:** prioritizes findings and proposes an implementation sequence.

## Output Contract

Every finding should include document, location, severity, recommendation, and verification. The synthesis should preserve reviewer attribution and identify whether the finding needs external source verification before editing.
