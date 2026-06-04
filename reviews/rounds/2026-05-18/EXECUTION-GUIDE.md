# Execution Guide — Performance Editorial Review Round

## Before Running Models

1. Confirm the review round directory exists: `reviews/rounds/2026-05-18/`.
2. Read `reviews/rounds/2026-05-18/review-prompt.md`.
3. Use `reviews/rounds/2026-05-18/metrics-snapshot.md` and `docs/current-metrics.md` for repository inventory.
4. Treat version-sensitive claims as requiring authoritative verification before source edits.

## Internal Agent Passes

Completed/expected files:

- `phase1-developer-reference.md`
- `phase1-general-checklist.md`
- `phase1-enterprise-checklist.md`
- `phase1-transients-object-cache.md`
- `phase2-cross-document.md`
- `synthesis.md`

## External Multi-Model Pass

To run the same prompt through external model interfaces, submit this exact input package independently to each model, without sharing other model findings first:

- `reviews/rounds/2026-05-18/review-prompt.md`
- `AGENTS.md`
- `DEVELOPER_REFERENCE.md`
- `wordpress-performance-optimization-checklist.md`
- `wpvip-enterprise-performance-operational-checklist.md`
- `REFERENCE-WP-Transients-Persistent-Object-Cache.md`
- `docs/current-metrics.md`

Save model outputs as:

- `external-gemini-review.md`
- `external-claude-review.md`
- `external-codex-review.md` or `external-gpt-review.md`

Then rerun synthesis with those files included.

## Suggested CLI Pattern

If local CLIs are authenticated, use each tool's non-interactive mode to pass a combined prompt file. Keep each model independent:

```bash
ROUND="reviews/rounds/2026-05-18"
cat "$ROUND/review-prompt.md" AGENTS.md docs/current-metrics.md \
  DEVELOPER_REFERENCE.md \
  wordpress-performance-optimization-checklist.md \
  wpvip-enterprise-performance-operational-checklist.md \
  REFERENCE-WP-Transients-Persistent-Object-Cache.md \
  > "$ROUND/combined-model-input.md"
```

Use each CLI's help output to select its non-interactive flag before running. Do not paste one model's findings into another model's independent review session.

## Closeout

Each synthesized finding should end in one state after human review:

- `accepted`
- `rejected`
- `deferred`
- `needs external verification`
