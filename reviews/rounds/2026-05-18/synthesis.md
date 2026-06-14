# Synthesis — Editorial Review Round 2026-05-18

## Status

Internal varied-model, multi-agent review completed. External CLI model attempts were logged but did not produce usable independent findings in this session:

- Gemini CLI stopped after repeated capacity-exhaustion retries.
- Claude CLI exited without usable output.
- Local Codex CLI was not run because macOS reported a local binary quarantine/malware warning.

Usable inputs:

- `phase1-developer-reference.md`
- `phase1-general-checklist.md`
- `phase1-enterprise-checklist.md`
- `phase1-transients-object-cache.md`
- `phase2-cross-document.md`

## Executive Summary

The review surfaced a coherent set of high-value edits. Most are cross-document drift issues rather than isolated local mistakes. The top fixes should be handled together so the same unsafe or stale pattern is not corrected in one file and left in another.

Highest-priority themes:

1. Correct repeated Speculative Loading guidance.
2. Add persistent-object-cache preconditions to `wp_cache_add()` lock examples.
3. Make `DISABLE_WP_CRON` guidance safe by requiring a verified external scheduler first.
4. Refresh WordPress 6.8/May 2026 currency claims and decide how to cover WordPress 6.9 deltas.
5. Replace duplicated New Relic transaction examples.
6. Repair fragment/partial-output cache key guidance.

## Prioritized Revision Plan

### P0 — Correct production-risk or materially false guidance

#### P0.1 Correct Speculative Loading Core/plugin behavior

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** The docs describe WordPress Core 6.8 as defaulting to prerender-on-mousedown and point readers to a settings UI that belongs to the standalone plugin, not stock Core.
- **Action:** Create one canonical paragraph: Core uses conservative prefetch-style behavior under constrained frontend/logged-out/pretty-permalink conditions; filters/classes handle Core customization; plugin UI and aggressive prerender belong to the plugin/custom configuration path.
- **State:** needs edit; source verification already partly documented in `phase2-cross-document.md`.

#### P0.2 Add persistent-cache precondition to `wp_cache_add()` lock examples

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `REFERENCE-WP-Transients-Persistent-Object-Cache.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** Lock examples imply cross-request coordination on default WordPress. Default object cache is request-local unless a persistent `object-cache.php` drop-in is active.
- **Action:** State that `wp_cache_add()` locking requires a shared persistent object cache with atomic add semantics. Provide fallback options: DB-backed mutex, platform lock, stale-while-revalidate, pre-warming, or avoiding regeneration in user requests.
- **State:** needs edit.

#### P0.3 Make `DISABLE_WP_CRON` sequencing safe

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** Copy-pastable snippets can be read as disabling WP-Cron before a replacement runner is proven.
- **Action:** Standardize sequence everywhere: install/verify external runner → monitor due events/backlog → set `DISABLE_WP_CRON` → verify scheduled events continue → document rollback. Mention WooCommerce Action Scheduler where relevant.
- **State:** needs edit.

### P1 — Source-refresh and duplicated incorrect examples

#### P1.1 Refresh WordPress version currency and 6.9 performance deltas

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** “current to WordPress 6.8, May 2026” is stale for this review date.
- **Action:** Decide exact verified version/date wording. Add or defer a WordPress 6.9 delta section. Prefer `last verified on YYYY-MM-DD` stamps over broad currency claims.
- **State:** needs source refresh before edit.

#### P1.2 Replace New Relic transaction examples

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** `newrelic_start_transaction()` is used as though its argument names a custom transaction.
- **Action:** Replace with safe transaction naming/custom instrumentation examples guarded by `function_exists()`/extension checks. Reserve start/end lifecycle control for advanced queue-worker style use.
- **State:** needs edit after confirming preferred New Relic API pattern.

#### P1.3 Repair partial-output and personalized fragment cache guidance

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `enterprise-performance-operational-checklist.md`; related checklist guidance in `wordpress-performance-optimization-checklist.md`
- **Issue:** Examples under-specify cache keys or make per-user fragment caching sound too broadly safe.
- **Action:** Add shared cache-key checklist covering every output-varying dimension, privacy, key cardinality, TTLs, locale, multisite context, query args, auth state, role/capability changes, and invalidation triggers.
- **State:** needs edit.

#### P1.4 Refresh Performance Lab feature-plugin language

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** Static module lists use stale names and packaging assumptions.
- **Action:** Replace with dated, source-checked feature-plugin wording or avoid enumerating volatile lists. Use current names only after verification.
- **State:** needs source refresh before edit.

#### P1.5 Fix transient remote JSON example

- **Affected docs:** `REFERENCE-WP-Transients-Persistent-Object-Cache.md`
- **Issue:** Example can cache `null` after invalid JSON and poison the transient until expiry.
- **Action:** Validate decoded payload before `set_transient()`; do not cache invalid/null payloads.
- **State:** needs edit.

### P2 — Consistency and diagnostic reliability

#### P2.1 Normalize cache-layer/drop-in boundaries in checklists

- **Affected docs:** `wordpress-performance-optimization-checklist.md`, `enterprise-performance-operational-checklist.md`
- **Issue:** Checklists do not consistently distinguish `WP_CACHE`/`advanced-cache.php` from `object-cache.php`.
- **Action:** Add concise canonical wording from the transients/developer references.
- **State:** needs edit.

#### P2.2 Add WP-CLI package availability caveats

- **Affected docs:** `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`
- **Issue:** `wp profile` and `wp doctor` can be package-backed and unavailable on stock installs.
- **Action:** Add `wp cli has-command`/`wp profile --help` checks, package-install note where permitted, and Query Monitor/APM/custom timer fallbacks.
- **State:** needs edit.

#### P2.3 Normalize autoload guidance

- **Affected docs:** `wordpress-performance-optimization-checklist.md`; verify related language elsewhere.
- **Issue:** Guidance mixes legacy `yes`/`no` vocabulary with modern API/CLI wording.
- **Action:** Prefer `wp_set_option_autoload()` / `wp_set_options_autoload()` and CLI `on`/`off` examples; describe `yes`/`no` as legacy storage values.
- **State:** needs edit.

### P3 — Trust, polish, and isolated precision fixes

#### P3.1 Fix broken links and attribution tokens

- **Affected docs:** all four for stray `@dknauss`; general/enterprise/developer for links.
- **Issue:** Broken local cross-references and body-level attribution tokens reduce trust.
- **Action:** Decide link policy: in-repo root links vs full external companion URLs. Remove/move attribution tokens to metadata/changelog context.
- **State:** ready for mechanical cleanup.

#### P3.2 Split page UX metrics from API/backend endpoint baselines

- **Affected docs:** `wordpress-performance-optimization-checklist.md`
- **Issue:** `/wp-json/...` appears in a table with LCP/INP/CLS, blurring browser metrics and endpoint diagnostics.
- **Action:** Split page-render baseline table from API/server-route baseline table.
- **State:** needs edit.

#### P3.3 Improve isolated technical wording

- **Affected docs:** `DEVELOPER_REFERENCE.md`
- **Issues:** OPcache JIT caveat, critical CSS “14 KB first TCP packet” wording, Redis vs Memcached recommendation strength.
- **Action:** Add measurement caveats and conditional/platform-specific wording.
- **State:** needs edit.

## Recommended Execution Order

1. Mechanical cleanup: links, `@dknauss`, obvious navigation issues.
2. Source refresh: WordPress version, Speculative Loading, Performance Lab, WP-CLI packages, New Relic API.
3. Production-risk snippets: WP-Cron, object-cache locks, fragment keys, New Relic, transient JSON validation.
4. Canonical terminology normalization: cache layers, autoload, WP-CLI availability.
5. Appendix refresh and duplicate reduction.
6. Markdown/link verification and final review.

## Closeout Tracking

Current state: **closed for editorial approval; execution pending.**

Human editorial approval was obtained on 2026-05-18 for all P0/P1/P2/P3 findings. Per-finding decisions, source-origin classification, edit instructions for each accepted finding, and the post-edit verification plan now live in `closeout.md` in this same round directory.

See: [`closeout.md`](./closeout.md).

Execution status (see `.planning/ROADMAP.md` Phase 2):

- 2a Reviewer pass — complete
- 2b Closeout decisions — complete
- 2c–2h Execution passes 0–5 — pending
