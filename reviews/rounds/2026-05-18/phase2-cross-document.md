# Phase 2 Cross-Document Audit — 2026-05-18

Scope: cross-document consistency audit for the four source documents, using `AGENTS.md`, `reviews/rounds/2026-05-18/review-prompt.md`, and the four Phase 1 review outputs.

Source documents audited:

- `DEVELOPER_REFERENCE.md`
- `wordpress-performance-optimization-checklist.md`
- `enterprise-performance-operational-checklist.md`
- `REFERENCE-WP-Transients-Persistent-Object-Cache.md`

No source documents were edited in this phase.

## Executive summary

The Phase 1 reviews converge on a small set of high-value fixes that should be handled as coordinated cross-document edits rather than isolated patches:

1. **Modern Core appendices are stale and duplicated.** Three documents frame the material as “current to WordPress 6.8, May 2026,” while Phase 1 reviewers flagged WordPress 6.9.x as current for the stated date and identified missing 6.9 performance deltas.
2. **Speculative Loading is consistently wrong across the broader guides.** `DEVELOPER_REFERENCE.md`, the general checklist, and the enterprise checklist all describe Core 6.8 as `prerender` on `mousedown` and point to UI/configuration affordances that belong to the standalone plugin, not stock Core.
3. **Copy-pastable safety snippets need coordinated repair.** The `wp_cache_add()` lock examples, `DISABLE_WP_CRON` snippets, New Relic transaction examples, and partial-output cache-key examples are repeated or echoed across documents with unsafe or under-specified preconditions.
4. **Cache-layer boundaries are strong in the transients reference and developer reference but weaker in the checklists.** The checklist documents should inherit the same `WP_CACHE` / `advanced-cache.php` / `object-cache.php` distinction instead of relying on scattered mentions.
5. **Several overlaps are not contradictions but drift risks.** Performance Lab feature lists, WP-CLI profiling commands, autoload guidance, and source cross-reference links appear in multiple places and should be normalized to one canonical wording pattern.

## Authority notes checked during Phase 2

These checks were used only to validate the cross-document synthesis; they do not replace a full source refresh before editing:

- WordPress.org documents **WordPress 6.9.4** as released on March 11, 2026: <https://wordpress.org/documentation/wordpress-version/version-6-9-4/>.
- Make/Core’s WordPress 6.9 Field Guide and Frontend Performance Field Guide describe material 6.9 performance changes: <https://make.wordpress.org/core/2025/11/25/wordpress-6-9-field-guide/> and <https://make.wordpress.org/core/2025/11/18/wordpress-6-9-frontend-performance-field-guide/>.
- Make/Core’s “Speculative Loading in 6.8” confirms Core’s effective default is `prefetch` + `conservative`, disabled for logged-in users and sites without pretty permalinks, with filter-based customization: <https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/>.
- WordPress.org’s Performance Lab plugin page presents Performance Lab as a feature-plugin discovery/collection layer and lists current featured plugins such as Modern Image Formats: <https://wordpress.org/plugins/performance-lab/>.
- WordPress Developer Reference states the default object cache is non-persistent: <https://developer.wordpress.org/reference/classes/wp_object_cache/>.
- WP-CLI documents `wp profile` as package-backed: <https://developer.wordpress.org/cli/commands/profile/>.
- New Relic documents `newrelic_start_transaction()` as taking an application name and usually being used after manually ending a transaction: <https://docs.newrelic.com/docs/apm/agents/php-agent/php-agent-api/newrelic_start_transaction/>.
- WordPress Plugin Handbook documents disabling request-triggered WP-Cron only after wiring an external scheduler: <https://developer.wordpress.org/plugins/cron/hooking-wp-cron-into-the-system-task-scheduler/>.

## 1. Convergent findings

| Theme | Documents affected | Phase 1 attribution | Cross-document finding | Consolidated recommendation |
|---|---|---|---|---|
| Stale WordPress version framing | `DEVELOPER_REFERENCE.md`; `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md` | Developer Finding 1; Enterprise row “Appendix title”; indirectly General Appendix A | Three documents present May 2026 material as current through WP 6.8. Phase 1 reviewers identify this as stale for the stated date and note missing 6.9 performance changes. | Do one source-grounded refresh pass for “Modern Core additions.” Update each document with a `last verified on YYYY-MM-DD` stamp and either (a) make the scope current through the verified version, or (b) explicitly label the material as WP 6.8-scoped and requiring refresh. |
| Speculative Loading behavior | `DEVELOPER_REFERENCE.md`; `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md` | Developer Finding 2; General Finding 7; Enterprise row “Speculative Loading subsection” | All three broader guides repeat the same factual drift: Core 6.8 is described as `prerender` on `mousedown`, with `Settings → Reading` as if it were a Core UI. The enterprise checklist also mentions `data-prefetch="false"`, which is not the recommended Core opt-out framing. | Create one canonical Core-vs-plugin paragraph. Core: effectively `prefetch` + `conservative`, frontend/logged-out/pretty-permalink constrained, customized via filters/classes. Plugin: UI and more aggressive prerender modes. Move analytics/prerender warnings under “when opting into prerender/plugin/custom config.” |
| Performance Lab feature list drift | `DEVELOPER_REFERENCE.md`; `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md` | Developer Finding 4; General Finding 8; Enterprise row “Performance Lab module list” | The three lists are duplicated and divergent. They mention stale names such as “WebP Uploads,” mix old module language with current feature-plugin language, and differ on whether Optimization Detective or SQLite belongs in the current recommendation set. | Avoid static undated lists where possible. If listing examples, date-qualify them and use current plugin names. Prefer a short recommendation: evaluate Performance Lab/featured plugins on staging, verify current WordPress.org plugin details, then select specific feature plugins such as Modern Image Formats only when they match the site need. |
| `wp_cache_add()` lock precondition | `DEVELOPER_REFERENCE.md`; `REFERENCE-WP-Transients-Persistent-Object-Cache.md`; also present in `enterprise-performance-operational-checklist.md` | Developer Finding 3; Transients Finding 1; Phase 2 additional cross-doc observation for enterprise §14 | The developer reference and transients reference both use `wp_cache_add()` as a lock without first requiring a shared persistent object cache. The enterprise checklist has the same lock pattern in its race/stampede section, even though the Phase 1 enterprise review did not flag it. | Update every lock example together: `wp_cache_add()` only coordinates across requests when backed by a persistent object cache with atomic add semantics. For non-persistent environments, recommend a DB-backed mutex, platform lock, stale-while-revalidate, pre-warming, or avoiding user-request regeneration. |
| `DISABLE_WP_CRON` sequencing | `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md`; also present in `DEVELOPER_REFERENCE.md` | General Finding 6; Enterprise row “DISABLE_WP_CRON and cron runner”; Phase 2 additional cross-doc observation for developer §16 | The general and enterprise checklists were flagged because they show `DISABLE_WP_CRON` before making the external scheduler precondition explicit. The developer reference has the same order: “Disable request-triggered cron” before showing the runner. | Standardize the sequence everywhere: verify external cron/runner exists, is monitored, and can run due events; only then set `DISABLE_WP_CRON`; include rollback and Action Scheduler/WooCommerce checks. |
| New Relic transaction API misuse | `DEVELOPER_REFERENCE.md`; `enterprise-performance-operational-checklist.md` | Developer Finding 5; Enterprise row “New Relic example” | The same example appears in both documents and uses `newrelic_start_transaction( 'my_custom_transaction' )` as if the argument names a custom transaction. | Replace both copies with a safer APM example: guard calls with `extension_loaded()`/`function_exists()`, use transaction naming or custom tracers/attributes for normal request instrumentation, and reserve start/end transaction lifecycle control for advanced cases like queue workers. |
| Fragment / partial-output cache-key safety | `DEVELOPER_REFERENCE.md`; `enterprise-performance-operational-checklist.md`; related caution in `wordpress-performance-optimization-checklist.md` | Developer Finding 7; Enterprise row “partial output cache example” | The developer reference says user-specific fragments can be keyed by user ID “or don’t cache it,” while the enterprise example keys only on blog ID. Both need stronger cardinality, privacy, and invalidation caveats. | Add a shared cache-key checklist: include every output-varying dimension; avoid shared keys for personalized/private output; bound key cardinality; use short TTLs; invalidate on content, profile, role, locale, query, A/B bucket, and multisite context changes as applicable. |
| Cache layer / drop-in boundaries | `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md`; already strong in `DEVELOPER_REFERENCE.md` and `REFERENCE-WP-Transients-Persistent-Object-Cache.md` | General Finding 5; Enterprise row “cache layer terminology coverage” | The reference documents correctly distinguish `WP_CACHE`, `advanced-cache.php`, and `object-cache.php`; the two checklists do not consistently make that boundary explicit. | Reuse the concise wording from the transients reference in both checklists: `WP_CACHE` allows loading `advanced-cache.php` for page-cache-style integration and does not enable Redis/Memcached; persistent object caching is the `object-cache.php` drop-in. |
| WP-CLI package-backed commands | `DEVELOPER_REFERENCE.md`; `wordpress-performance-optimization-checklist.md` | Developer Finding 9; General Finding 3 | Both documents imply `wp profile`/`wp doctor` are available when WP-CLI is available. | Add an availability check before examples: `wp cli has-command profile` / `wp profile --help`, package install where permitted, and Query Monitor/APM/custom timers as fallback. |
| Broken or external cross-reference links | `wordpress-performance-optimization-checklist.md`; `enterprise-performance-operational-checklist.md`; related source-map links in `DEVELOPER_REFERENCE.md` | General Finding 1; Enterprise row “companion cross-reference links”; Phase 2 grep found developer source-map links to sibling repos | The two checklists link to sibling paths that do not exist in this checkout. The developer reference also points to sibling source folders. These may be intended external companion repos, but the current repo presents them as local links. | Decide repository policy: either link to in-repo files at repo root, or label external companion repos with full URLs/access expectations. Then update all cross-reference links consistently. |

## 2. Contradictions and drift risks

### 2.1 Direct contradictions with authoritative behavior

1. **Speculative Loading defaults:** Three documents say Core 6.8 defaults to prerendering on `mousedown`; Make/Core says Core effectively defaults to prefetching with conservative eagerness. This is the clearest factual contradiction and should be corrected in the same edit across all three documents.
2. **Speculative Loading UI:** The general and developer references point readers to `Settings → Reading`; Phase 1 reviewers attribute that UI to the standalone plugin rather than stock Core. Separate Core verification from plugin configuration.
3. **New Relic API semantics:** Two documents use `newrelic_start_transaction()` as a transaction-name API; New Relic’s PHP agent docs describe the required parameter as the New Relic application name.
4. **Object-cache lock semantics:** The lock examples imply cross-request coordination; WordPress’ default object cache is non-persistent, so this is only true with a persistent cache drop-in or another shared lock primitive.

### 2.2 Internal or cross-document tensions

1. **Cron safety vs snippet order:** The guides generally value operational safety, but the `DISABLE_WP_CRON` snippets appear before the replacement scheduler is proven. This does not contradict a stated principle; it contradicts the repository’s “protect correctness” workflow.
2. **Redis preference vs platform specificity:** `DEVELOPER_REFERENCE.md` says Redis is “usually a better fit,” while the enterprise/VIP framing acknowledges platform-standard Memcached-like environments. Make the backend recommendation host- and operations-dependent rather than universal.
3. **Autoload vocabulary:** The general checklist tells readers to set `autoload = no` and uses `wp option set-autoload ... no`, while the same document’s appendix promotes the modern API and expanded vocabulary. Normalize on API/CLI `on`/`off` wording, with `yes`/`no` described as legacy rows.
4. **Baseline metrics for non-HTML routes:** The general checklist puts `/wp-json/...` into a table with `LCP`, `INP`, and `CLS`, while the developer reference’s measurement workflow distinguishes request context. Split page-render metrics from server/API endpoint diagnostics.
5. **Transient examples vs falsy/null guidance:** The developer reference explains the falsey-value pitfall, while the transients reference’s remote-data example can cache `null` after invalid JSON. The focused reference should apply the safer wrapper/validation pattern it recommends conceptually.
6. **Attribution tokens in document bodies:** Phase 1 flagged `@dknauss` in the enterprise checklist; Phase 2 grep also found the same token in `DEVELOPER_REFERENCE.md`, `wordpress-performance-optimization-checklist.md`, and `REFERENCE-WP-Transients-Persistent-Object-Cache.md`. Treat attribution consistently, either remove from body copy or move to metadata/changelog context.

## 3. Duplicated recommendations that should be consolidated

| Duplicated area | Current duplication pattern | Risk | Consolidation approach |
|---|---|---|---|
| Modern Core appendices | Three documents maintain overlapping WP 6.4/6.6/6.8 material. | Staleness multiplies; same speculative-loading error appears three times. | Make `DEVELOPER_REFERENCE.md` the canonical deep reference; keep checklist appendices as short operational summaries that link to the canonical section. |
| Performance Lab recommendations | Three separate feature lists with stale/different names. | Readers may enable deprecated/renamed features or infer static module availability. | Replace with a short dated note and source-check instruction; list only examples that are verified during the edit. |
| Cron configuration | `DISABLE_WP_CRON` plus cron examples appear in developer, general, and enterprise docs. | Copy/paste can disable scheduling without replacement. | Use one repeated safe pattern: “install/verify runner → monitor due events/backlog → set constant → rollback plan.” |
| Cache stampede locks | Developer, enterprise, and transients docs all show `wp_cache_add()` locking patterns. | Readers may assume it works on default WordPress. | Use the focused transients reference as the canonical explanation; shorter docs should link or summarize the persistent-cache precondition. |
| New Relic instrumentation | Developer and enterprise documents duplicate the same incorrect snippet. | APM data can be misleading or instrumentation can be misapplied. | Replace both with a single safe snippet/pattern and refer readers to New Relic docs for transaction lifecycle control. |
| Cache-layer boundaries | Correct explanation exists in reference docs but not checklists. | Operators conflate page cache, object cache, and `WP_CACHE`. | Copy a concise version into both checklists; avoid re-explaining at length. |
| WP-CLI profiling commands | Developer and general docs list `wp profile` without package caveat. | Diagnostic first step fails in many environments. | Add a small reusable “command availability” note and fallback tooling list. |
| Companion/source links | Checklists and developer source map link to old sibling paths. | Broken rendered links reduce trust and navigation. | Decide one link policy and update all cross-references in one pass. |

## 4. Recommended implementation ordering

### Pass 0 — Mechanical safety and navigation cleanup

Rationale: low editorial risk, easy to verify, and reduces confusion before substantive edits.

1. Fix broken cross-reference links in the general and enterprise checklists; review developer source-map links for the same policy.
2. Remove or relocate stray `@dknauss` tokens from all four source documents.
3. Add a note in the changelog once substantive documentation fixes are made.

### Pass 1 — Source verification for volatile claims

Rationale: the repository requires source-grounded guidance, and several edits depend on current external behavior.

1. Verify the exact WordPress version/date scope to use for May 18, 2026.
2. Verify WordPress 6.9 performance deltas that should be added or intentionally deferred.
3. Verify current Performance Lab/featured plugin names and settings paths.
4. Verify Speculative Loading Core-vs-plugin behavior and opt-out mechanisms.
5. Verify WP-CLI package availability language for `profile` and `doctor`.
6. Verify New Relic PHP API examples before replacing snippets.

### Pass 2 — Fix copy-pastable production-risk snippets

Rationale: these are the highest-risk reader actions because they can affect live scheduling, cache correctness, personalization, and APM data.

1. Update `DISABLE_WP_CRON` guidance in all three broader docs so external cron is verified before the constant is set.
2. Update `wp_cache_add()` lock examples in `DEVELOPER_REFERENCE.md`, `REFERENCE-WP-Transients-Persistent-Object-Cache.md`, and the enterprise checklist.
3. Fix partial-output/fragment cache key examples and personalized-fragment caveats.
4. Replace the New Relic examples in developer and enterprise docs.
5. Fix the transients reference remote-data example so invalid JSON/`null` is not cached.

### Pass 3 — Normalize canonical technical explanations

Rationale: once dangerous snippets are safe, align terminology so future edits do not reintroduce drift.

1. Make `DEVELOPER_REFERENCE.md` the canonical explanation for modern Core performance additions.
2. Make `REFERENCE-WP-Transients-Persistent-Object-Cache.md` the canonical explanation for transient/object-cache storage and lock preconditions.
3. Copy concise cache-layer boundary language into both checklists.
4. Normalize autoload wording and CLI examples in the general checklist; ensure enterprise/developer wording remains compatible.
5. Add WP-CLI package caveats in developer/general docs.

### Pass 4 — Refresh duplicated appendices and remove drift

Rationale: these sections are version-sensitive and should be updated only after the canonical wording is settled.

1. Update all “current to WordPress 6.8, May 2026” headings/notes.
2. Add or link to WordPress 6.9 performance deltas as appropriate for each document’s audience.
3. Rewrite Speculative Loading sections from the shared canonical paragraph.
4. Replace Performance Lab module lists with dated, source-checked feature-plugin language.
5. Keep checklist appendices shorter than the developer reference to avoid reintroducing parallel long-form explanations.

### Pass 5 — Verification after edits

1. Run a Markdown link check from repository root.
2. Search for stale terms: `prerender on`, `Settings → Reading`, `WebP Uploads`, `DISABLE_WP_CRON`, `newrelic_start_transaction`, `wp_cache_add`, `autoload = no`, and `@dknauss`.
3. Preview rendered Markdown for the four source documents.
4. For code snippets, prefer syntax checks or local sandbox verification where practical.
5. Confirm no source recommendation was made universal when it depends on host, CDN, cache backend, plugin, or WordPress version.

## 5. Prioritized merged issue list for synthesis

| Priority | Merged issue | Affected docs | Why this priority |
|---:|---|---|---|
| P0 | Correct Speculative Loading Core/plugin behavior | Developer, general, enterprise | High-severity factual drift repeated across three docs; easy to propagate wrong operational guidance. |
| P0 | Add persistent-cache precondition to `wp_cache_add()` locks | Developer, enterprise, transients | Unsafe production behavior under default non-persistent object cache. |
| P0 | Make `DISABLE_WP_CRON` sequencing safe | Developer, general, enterprise | Copy/paste risk can stop scheduled events and queues. |
| P1 | Update stale WordPress 6.8/May 2026 currency claims and add 6.9 delta plan | Developer, general, enterprise | Document trust and version-sensitive accuracy. |
| P1 | Replace New Relic examples | Developer, enterprise | Misleading instrumentation and duplicated incorrect snippet. |
| P1 | Repair partial-output/personalized fragment cache guidance | Developer, enterprise; related general cache guidance | Prevent cache bleed, high-cardinality growth, and stale personalized output. |
| P1 | Refresh Performance Lab feature-plugin language | Developer, general, enterprise | Repeated stale operational advice. |
| P2 | Normalize cache-layer boundaries in checklists | General, enterprise | Reduces common operator misconception; canonical wording already exists. |
| P2 | Add WP-CLI package availability caveats | Developer, general | Prevents failed diagnostic steps. |
| P2 | Normalize autoload guidance | General primarily; verify developer/enterprise | Removes internal contradiction and aligns with modern APIs. |
| P3 | Fix broken links and attribution tokens | All four for attribution tokens; general/enterprise/developer for links | Low-risk polish/trust cleanup; should be done early but does not drive technical correctness. |
| P3 | Split API endpoint baselines from Core Web Vitals page baselines | General | Medium clarity issue isolated to one document. |
| P3 | Reword Critical CSS “14 KB packet” explanation and OPcache JIT caveat | Developer | Isolated technical precision improvements. |
