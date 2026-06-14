# Phase 1 Review — `DEVELOPER_REFERENCE.md`

Scope: independent audit of `DEVELOPER_REFERENCE.md` only. Source document was not edited.

Review principles applied: measurement-first recommendations, cache-layer precision, WordPress API accuracy, version-sensitive verification, operational safety.

## Findings

### 1. Currency note is stale for a May 2026 reference

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 14–19, 98–100, 110, 1220–1251, 1555–1561
- **Finding:** The document says the reference is “current through WordPress 6.8” in a May 2026 currency note. As of May 18, 2026, the WordPress release archive lists 6.9.4 as the latest stable release, and the 6.9 Field Guide documents material performance changes that are absent here, including 6.9 frontend performance work, updated query cache handling, and cron spawning changes. This makes the currency statement inaccurate and leaves the developer reference missing current Core performance behavior.
- **Severity:** High
- **Recommendation:** Update the currency note to state the exact reviewed core version, e.g. “current through WordPress 6.9.4 as of May 18, 2026” if re-reviewed. Add a short WP 6.9 delta section covering at least frontend performance improvements, query cache key changes/new cache helper functions, WP-Cron spawn timing, and any relevant 6.9 security/maintenance caveats. If the document intentionally remains 6.8-scoped, remove “May 2026” currency language and label it as requiring refresh.
- **Verification:** Check the official WordPress release archive (`https://wordpress.org/download/releases/`) and WordPress 6.9/6.9.4 release notes; check the Make/Core 6.9 Field Guide and “WordPress 6.9 Frontend Performance Field Guide” for performance deltas.

### 2. Speculative loading default behavior is described incorrectly

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 1235–1242, especially “Default behavior is conservative: prerender on `mousedown`” and “Configurable via Settings → Reading.”
- **Finding:** WordPress 6.8 Core did not default to prerendering. The Core dev note describes the default as `prefetch` with `conservative` eagerness, enabled on frontend requests except for logged-in users and sites without pretty permalinks. It also says a dedicated Core UI like the feature plugin’s UI was out of scope; customization is via filters and block-level CSS classes, while the standalone plugin provides its own UI and more aggressive modes. The current text overstates Core’s default side effects and points readers to a settings screen that may not exist in Core.
- **Severity:** High
- **Recommendation:** Change the Core description to: default `mode`/`eagerness` are effectively `prefetch`/`conservative` as of 6.8, disabled for logged-in users and sites without pretty permalinks, and subject to future Core changes. Move prerender analytics warnings under “when opting into prerender” or “standalone plugin / custom filter configuration.” Replace “Settings → Reading” with the actual configuration mechanisms: `wp_speculation_rules_configuration`, `wp_speculation_rules_href_exclude_paths`, `wp_load_speculation_rules`, and block CSS classes such as `no-prefetch` / `no-prerender`.
- **Verification:** Confirm against Make/Core “Speculative Loading in 6.8” and a clean WordPress 6.8+ install by viewing generated speculation rules while logged out, logged in, with pretty permalinks on/off, and with the standalone Speculative Loading plugin disabled/enabled.

### 3. Cache-stampede lock pattern is unsafe without a persistent object cache

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 835–879, especially the transient form at lines 856–879
- **Finding:** The examples use `wp_cache_add()` as a lock and the prose says to keep the lock in the object cache even when using transients with their database fallback. In default WordPress, the object cache is non-persistent and request-local unless a persistent cache drop-in is installed. On a site without persistent object cache, this lock does not coordinate concurrent requests and does not prevent a cross-request stampede, even though the transient value may be shared through the database.
- **Severity:** High
- **Recommendation:** Add an explicit precondition: `wp_cache_add()` locking only works across requests when a persistent object cache backend supports atomic add semantics. For non-persistent-cache environments, recommend a different lock primitive, such as a short-lived option/transient lock created with atomic database semantics, a platform lock service, or avoiding hot-key regeneration in user requests. Include fallback behavior for failed lock acquisition and lock cleanup.
- **Verification:** Confirm WordPress object cache docs state the default cache is non-persistent. Reproduce with two concurrent requests on a site without `object-cache.php`: both requests can acquire the `wp_cache_add()` lock because each has its own runtime cache. Repeat with Redis/Memcached drop-in and verify only one request acquires the lock.

### 4. Performance Lab section uses stale module names and omits current feature-plugin model

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 1224–1233 and line 1124
- **Finding:** The document describes “current notable modules” including **WebP Uploads** and **SQLite Database Integration** and refers to Performance Lab modules as if they are still the primary unit. The current Performance Lab plugin page describes Performance Lab as a collection/discovery layer for feature plugins and lists current featured plugins such as Embed Optimizer, Enhanced Responsive Images, Image Placeholders, Image Prioritizer, Instant Back/Forward, Modern Image Formats, Optimization Detective, Performant Translations, Speculative Loading, and View Transitions. The stale list can send readers to outdated names or features that are no longer featured.
- **Severity:** Medium
- **Recommendation:** Replace “Current notable modules” with a dated “featured performance plugins as of [date]” list or avoid enumerating a volatile list in the reference. Use current plugin names, e.g. **Modern Image Formats** rather than **WebP Uploads**, and explain that Performance Lab’s featured plugins change as features merge into Core, graduate, or are removed.
- **Verification:** Check `https://wordpress.org/plugins/performance-lab/` and the plugin changelog before publishing. Verify names from the WordPress.org plugin directory rather than old course notes.

### 5. New Relic PHP example uses transaction-start API as if it named a custom transaction

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 1384–1394
- **Finding:** The example calls `newrelic_start_transaction( 'my_custom_transaction' )` around a function. In New Relic’s PHP agent API, `newrelic_start_transaction()` starts a new transaction and its required parameter is the New Relic application name, not the transaction name. Used as written, the snippet can create misleading APM data or fail to instrument the intended segment.
- **Severity:** Medium
- **Recommendation:** Replace the example with a safe transaction-naming or custom-instrumentation pattern, such as guarding New Relic function calls with `function_exists()`, using `newrelic_name_transaction()` to name a request/transaction, or using custom spans/attributes as supported by the deployed agent. If the intent is timing arbitrary code inside a request, prefer New Relic custom instrumentation guidance rather than manually ending/starting transactions.
- **Verification:** Check New Relic’s official PHP agent API docs for `newrelic_start_transaction()` and `newrelic_name_transaction()`. Test on a staging site with the PHP agent enabled and verify the transaction appears with the expected app and transaction names.

### 6. OPcache sample encourages JIT without a WordPress-specific measurement caveat

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 469–485
- **Finding:** The sample OPcache configuration includes `opcache.jit_buffer_size=100M` as “optional, PHP 8+” without explaining that JIT is not generally a default WordPress web-request optimization and can consume memory that may be more valuable for OPcache bytecode storage or PHP workers. This weakens the document’s measurement-first discipline and can lead operators to enable JIT by copy/paste.
- **Severity:** Medium
- **Recommendation:** Remove JIT from the default sample or add a clear caveat: leave JIT off unless representative benchmarks show a benefit for the specific workload. Keep the core OPcache guidance focused on `opcache.enable`, memory consumption, accelerated files, timestamp validation, and deployment-safe invalidation.
- **Verification:** Benchmark representative cached/uncached WordPress requests with JIT off/on using the same PHP version, worker count, OPcache memory, and traffic profile. Confirm OPcache memory headroom and recompilation rates before and after.

### 7. Fragment caching guidance is too permissive for per-user cached fragments

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 1070–1075
- **Finding:** The guidance says that if a fragment varies per user, “key on the user ID — or don’t cache it.” Keying on user ID can be safe in narrow cases, but the text does not warn about high-cardinality cache growth, private-data exposure through shared keys, retention after account changes, or invalidation on permission/profile changes. This is especially risky in persistent object caches shared across many users or multisite contexts.
- **Severity:** Medium
- **Recommendation:** Add caveats before recommending per-user fragment caching: use it only for expensive fragments with bounded user counts, short TTLs, non-sensitive output, correct group/blog/site scoping, and explicit invalidation when user capabilities/profile data change. Prefer not caching personalized fragments unless there is measured benefit and a privacy review.
- **Verification:** Review cache key cardinality and memory usage in Redis/Memcached, verify no private content appears under shared keys, and test role/account/profile changes to ensure cached fragments invalidate correctly.

### 8. Critical CSS “14 KB first TCP packet” explanation is technically imprecise

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 1156–1163
- **Finding:** The text says to keep critical CSS under ~14 KB “so it fits in the first TCP packet.” A single TCP packet is not ~14 KB; this rule of thumb refers to the initial congestion window across multiple TCP segments and is further affected by TLS, HTTP/2, HTTP/3/QUIC, server configuration, and competing response bytes. The current wording is likely to confuse readers about why the budget exists.
- **Severity:** Low
- **Recommendation:** Reword to “keep critical CSS small; ~14 KB is an old initial-congestion-window rule of thumb, not a universal packet limit.” Emphasize measuring LCP/FCP and HTML transfer size rather than treating 14 KB as a hard protocol rule.
- **Verification:** Confirm with a network waterfall and server timing on HTTP/2 and HTTP/3 connections. Validate that inlined CSS improves render timing without bloating HTML or hurting repeat views.

### 9. `wp profile` commands need an availability caveat

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 517–525 and 1347–1351
- **Finding:** The document lists `wp profile stage` and `wp profile hook` as if they are always available WP-CLI commands. In many environments, `wp profile` is provided by the separate WP-CLI profile command package rather than a stock WP-CLI install. Readers may fail at the first diagnostic step on production or managed hosts.
- **Severity:** Low
- **Recommendation:** Add a note that `wp profile` may require the WP-CLI profile package or a host-provided equivalent, and provide a fallback path: Query Monitor, APM traces, custom timers, or host profiling tools when the command is unavailable.
- **Verification:** Run `wp profile --help` on a clean WP-CLI install and on the target host. If unavailable, verify whether package installation is permitted or whether the host exposes an alternative profiler.

### 10. Redis recommendation is more universal than the source hierarchy supports

- **Document:** `DEVELOPER_REFERENCE.md`
- **Location:** Lines 818–827
- **Finding:** The object-cache backend section says Redis is “usually a better fit” for WordPress workloads. Redis has operational and introspection advantages, but the recommendation is presented more universally than the document’s platform-specific principles allow. Many managed WordPress platforms standardize on Memcached or host-provided drop-ins; the best backend depends on platform support, persistence policy, eviction behavior, network latency, observability, and operational ownership.
- **Severity:** Low
- **Recommendation:** Make the recommendation conditional: Redis can be preferable when the team needs richer observability, data structures, and managed Redis operations; Memcached can be appropriate when it is the platform-supported, simpler ephemeral cache. Emphasize using the host-supported drop-in and measuring hit rate, latency, evictions, and failure behavior before switching.
- **Verification:** Check the target host’s object-cache documentation and compare Redis/Memcached under representative traffic using hit rate, p95/p99 cache latency, eviction rate, memory pressure, and outage/fallback behavior.
