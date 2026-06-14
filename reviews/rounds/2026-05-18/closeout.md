# Closeout — Editorial Review Round 2026-05-18

## Status

Human editorial approval obtained on 2026-05-18 for all P0, P1, P2, and P3 findings in `synthesis.md`. Codex applied the accepted findings on 2026-05-18 across all four source documents.

Verification completed after application: stale-pattern grep, sibling-link grep, relative Markdown link check, code-fence parity counts, and `.github/documents.json` marker checks all passed. Generated artifacts were not built locally because Pandoc/XeLaTeX are not installed in this desktop environment; the GitHub Actions workflow installs them.

## Execution result

- P3.1 mechanical cleanup: applied.
- P0.1/P0.2/P0.3/P1.5 production-risk fixes: applied.
- P1.1/P1.2/P1.4 source-verification edits: applied against official sources listed in this file.
- P2.1/P2.2/P2.3 consistency normalization: applied.
- P1.3/P3.2/P3.3 polish and precision fixes: applied.
- Pass 5 verification sweep: passed.

## Source-origin summary

Roughly half of the findings derive from the Remkus and WP VIP source materials and half from synthesis-introduced wording. This is meaningful context: source-derived fixes improve on the upstream course material; synthesis-introduced fixes correct recent additions to this repository's docs.

| Finding | Origin |
|---|---|
| P0.1 Speculative Loading | synthesis-introduced |
| P0.2 `wp_cache_add()` lock precondition | mixed (VIP source + synthesis propagation) |
| P0.3 `DISABLE_WP_CRON` sequencing | source-derived (Remkus + VIP) |
| P1.1 WordPress 6.8 currency framing | synthesis-introduced |
| P1.2 New Relic transaction example | source-derived (VIP) |
| P1.3 Fragment cache key under-specification | mixed (VIP pattern + synthesis wording) |
| P1.4 Performance Lab module list | synthesis-introduced |
| P1.5 Transient JSON validation | pre-existing in standalone REFERENCE.md |
| P2.1 Cache-layer boundaries in checklists | source-derived (Remkus + VIP) |
| P2.2 WP-CLI package availability | source-derived (Remkus + VIP) |
| P2.3 Autoload `yes/no` body wording | source-derived (Remkus) |
| P3.1 `@dknauss` tokens, broken links | synthesis-introduced |
| P3.2 `/wp-json/...` in CWV baseline table | source-derived (Remkus) |
| P3.3 OPcache JIT / 14 KB / Redis preference | synthesis-introduced |

## Execution order

The execution agent should work the passes in this order. Items within a pass are independent and may be done in any order.

1. **Pass 0 — Mechanical cleanup:** P3.1
2. **Pass 1 — P0 production-risk fixes:** P0.1, P0.2, P0.3, P1.5
3. **Pass 2 — Source-verification edits:** P1.1, P1.2, P1.4
4. **Pass 3 — Consistency normalization:** P2.1, P2.2, P2.3
5. **Pass 4 — Polish and isolated precision:** P1.3, P3.2, P3.3
6. **Pass 5 — Verification sweep**

After each pass, the agent should:

- Run `grep -n` for any stale patterns the pass should have removed.
- Update `CHANGELOG.md` Unreleased section.
- Tick the corresponding ROADMAP checkbox.

---

## Findings — accepted

### P0.1 — Correct Speculative Loading Core vs plugin behavior

- **Status:** `accepted`
- **Origin:** synthesis-introduced.
- **Severity:** High. Factual error repeated across three docs; can propagate incorrect operational guidance.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (lines 1235–1242 of the synthesis-time version; current line numbers may differ — search for `Speculative Loading` and `prerender` / `mousedown`).
  - `wordpress-performance-optimization-checklist.md` (Modern additions appendix, Speculative Loading subsection).
  - `enterprise-performance-operational-checklist.md` (Modern additions appendix, Speculative Loading subsection).
- **What is wrong:** Three docs describe Core 6.8 as defaulting to `prerender` on `mousedown` and refer readers to `Settings → Reading`. Both are wrong. Per the Make/Core dev note, Core 6.8 effectively defaults to `prefetch` with `conservative` eagerness, is disabled for logged-in users and sites without pretty permalinks, and exposes customization via filters and block CSS classes — not a Core UI. The settings UI belongs to the standalone Speculative Loading plugin.
- **Edit instructions:** Replace the Speculative Loading subsection in each doc with a shared canonical paragraph. Draft replacement text:

  > **Speculative Loading (Core in WordPress 6.8)**
  >
  > WordPress 6.8 (April 2025) merged speculative-loading support into Core via the [Speculation Rules API](https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/). Core's effective default is **`prefetch`** with **`conservative`** eagerness, enabled on frontend requests only when pretty permalinks are on and the user is logged out. Core does not ship a dedicated settings UI for speculation rules in 6.8; customization happens through filters such as `wp_speculation_rules_configuration` and `wp_load_speculation_rules`, plus block-level CSS classes like `no-prefetch` and `no-prerender`.
  >
  > The standalone [Speculative Loading plugin](https://wordpress.org/plugins/speculation-rules/) extends Core with a Settings → Reading admin screen and more aggressive modes (including `prerender`). When you opt into prerender, audit your analytics SDKs for prerender-aware behavior and confirm that prerendered visits do not double-count or fire third-party scripts on hidden documents.
  >
  > Enterprise considerations: edge cache hit ratio will rise on sites with predictable navigation patterns because prefetch hits cache. Confirm session-keyed and personalized pages are excluded from speculative loading via `data-speculationrules-no-href` or filter predicates. (Note: the standalone-plugin documentation provides the correct opt-out attribute; the data-prefetch="false" wording in earlier doc versions is not the recommended Core opt-out form.)

  Apply the same canonical paragraph in all three files. The checklist appendices may shorten it; the developer reference keeps the long form.

- **Verification sources:**
  - Make/Core: <https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/>
  - Plugin page: <https://wordpress.org/plugins/speculation-rules/>
- **Acceptance criteria:**
  - All three docs use the same canonical Core/plugin paragraph.
  - No remaining instance of `prerender on mousedown` as the Core default.
  - No remaining reference to `Settings → Reading` as a Core 6.8 UI.

---

### P0.2 — Add persistent-cache precondition to `wp_cache_add()` lock examples

- **Status:** `accepted`
- **Origin:** mixed. VIP operational checklist §14 has the lock pattern without precondition; the synthesis propagated it.
- **Severity:** High. Unsafe production guidance: the lock does not coordinate cross-request work on default WordPress.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (lines 835–879 — cache stampede object-cache form and transient form).
  - `REFERENCE-WP-Transients-Persistent-Object-Cache.md` (Section 8 stampede example).
  - `enterprise-performance-operational-checklist.md` (§14 race conditions and cache stampedes).
- **What is wrong:** Examples use `wp_cache_add()` as a lock without stating that the default WordPress object cache is request-local (non-persistent). Without a persistent `object-cache.php` drop-in with atomic-add semantics (Redis/Memcached integration), the "lock" doesn't lock anything — each PHP process has its own runtime cache.
- **Edit instructions:** Add an explicit precondition note above each lock example and offer fallbacks for non-persistent environments. Suggested wording to insert directly before the existing lock code block:

  > These lock patterns assume a **persistent object cache** with atomic add semantics (Redis or Memcached via `object-cache.php`). On default WordPress with no persistent object cache, `wp_cache_add()` is request-local — every concurrent request can "acquire" the lock simultaneously, providing no cross-request coordination. Confirm a persistent object cache is in place before relying on this pattern.
  >
  > Fallbacks when persistent object caching is not available:
  >
  > - Use the Transients API as a coarse cross-request lock (with the falsey-pitfall caveat in mind), accepting that database-backed transient writes carry their own load.
  > - Use a platform-provided distributed lock service if the host offers one.
  > - Use stale-while-revalidate: serve the previous value while a single warmer regenerates the cache asynchronously.
  > - Pre-warm hot keys outside of user requests (cron, deploy hook, scheduled action).
  > - Restructure so the expensive operation never runs inside a user request.

- **Verification sources:**
  - `WP_Object_Cache`: <https://developer.wordpress.org/reference/classes/wp_object_cache/> (states default is non-persistent)
  - Reproducible check: two concurrent requests on a site without `object-cache.php` — both will acquire the lock. With Redis/Memcached drop-in active, only one will.
- **Acceptance criteria:**
  - Every doc that shows a `wp_cache_add()` lock has the precondition paragraph directly above the example.
  - REFERENCE.md becomes the canonical longform; shorter docs may summarize and link there.

---

### P0.3 — Make `DISABLE_WP_CRON` sequencing safe

- **Status:** `accepted`
- **Origin:** source-derived. Both Remkus checklist (line ~514) and VIP lesson 034 (line ~26) show `define( 'DISABLE_WP_CRON', true );` before any external runner is verified. Our docs inherited this order.
- **Severity:** High. Copy-paste risk: a reader applying the snippet top-to-bottom can stop scheduled events before the replacement runs.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (§16 WP-Cron section).
  - `wordpress-performance-optimization-checklist.md` (§15 / §16, also wp-config.php block at line ~511).
  - `enterprise-performance-operational-checklist.md` (§15 WP-Cron section).
- **What is wrong:** Snippet order presents the disabling constant first and the external runner second. The safe order is the inverse.
- **Edit instructions:** Reorder every WP-Cron production-pattern block so the sequence is:

  1. Install the external runner (`wp cron event run` via system cron, or `wget`/`curl` of `wp-cron.php`).
  2. Verify it is running on schedule (check `wp cron event list --due-now`, monitor for backlog).
  3. **Only then** set `define( 'DISABLE_WP_CRON', true )`.
  4. Re-verify: confirm scheduled events still complete on time after disabling request-triggered cron.
  5. Have a rollback path: remove the `define` line and clear OPcache if scheduled events stop.

  Suggested explicit prose for the canonical block:

  > **Sequence matters.** Set up and verify the external runner *before* disabling request-triggered cron. If you flip the order, scheduled events stop running until the runner is in place.
  >
  > ```bash
  > # Step 1: install external runner (example: every 5 minutes)
  > */5 * * * * cd /path/to/site && wp cron event run --due-now --quiet
  > ```
  >
  > ```bash
  > # Step 2: verify the runner is firing
  > wp cron event list --due-now
  > # tail any cron / web-server log for the runner invocation
  > ```
  >
  > ```php
  > // Step 3: only after verification, disable request-triggered cron in wp-config.php
  > define( 'DISABLE_WP_CRON', true );
  > ```
  >
  > Step 4: confirm scheduled events continue to fire (`wp cron event list`, application logs, WooCommerce Action Scheduler dashboard if relevant).
  >
  > Rollback: comment out the `define` line and clear OPcache if events stop.

  For WooCommerce / Action Scheduler-heavy sites, add a callout that Action Scheduler depends on cron firing — backlog can build silently if the external runner stalls.

- **Verification sources:**
  - WP Plugin Handbook: <https://developer.wordpress.org/plugins/cron/hooking-wp-cron-into-the-system-task-scheduler/>
- **Acceptance criteria:**
  - All three broader docs present the sequence in the verified order.
  - The `define()` block is never the first snippet under any WP-Cron heading.

---

### P1.5 — Fix transient remote JSON example so invalid JSON is not cached

- **Status:** `accepted`
- **Origin:** pre-existing in `REFERENCE-WP-Transients-Persistent-Object-Cache.md` (predates synthesis edits).
- **Severity:** High. The doc explicitly warns against the falsey-value pitfall and then commits the same pitfall in its own example.
- **Affected files:**
  - `REFERENCE-WP-Transients-Persistent-Object-Cache.md` (Section 5 — Expiration semantics, the `wp_remote_get` example).
- **What is wrong:** The example calls `json_decode( wp_remote_retrieve_body( $response ), true )` and then `set_transient()` without validating the decoded result. If the remote API returns invalid JSON, `json_decode` returns `null`. `set_transient()` caches `null`. The next `get_transient()` returns `false` (looks like a miss), causes a re-fetch, which fails the same way — for the full expiration window.
- **Edit instructions:** Replace the current example with a validation-aware version:

  ```php
  $data = get_transient( 'myplugin_remote_data' );

  if ( false === $data ) {
      $response = wp_remote_get( 'https://api.example.com/data', array(
          'timeout' => 3,
      ) );

      if ( is_wp_error( $response ) ) {
          return array();
      }

      $body    = wp_remote_retrieve_body( $response );
      $decoded = json_decode( $body, true );

      // Do not cache invalid or empty payloads — caching null would
      // poison the cache for the full expiration window.
      if ( null === $decoded || ! is_array( $decoded ) ) {
          return array();
      }

      $data = $decoded;
      set_transient( 'myplugin_remote_data', $data, 15 * MINUTE_IN_SECONDS );
  }
  ```

  Add a one-line caption directly under the example: *Validate the decoded payload before caching. The Transients API treats `null`, `false`, and `0` as cache misses on read, so caching any of those values poisons the cache until expiry.*

- **Verification sources:**
  - PHP `json_decode` behavior on invalid input: returns `null`. <https://www.php.net/manual/en/function.json-decode.php>
  - `get_transient()` returns `false` for both miss and certain falsey-stored values. <https://developer.wordpress.org/reference/functions/get_transient/>
- **Acceptance criteria:**
  - Example contains a `null === $decoded` (or equivalent) guard before `set_transient()`.
  - The caption text appears below the example.

---

### P1.1 — Refresh WordPress 6.8 currency claim; add 6.9 deltas

- **Status:** `accepted` with scope limit.
- **Origin:** synthesis-introduced.
- **Severity:** High for currency claim; Medium for missing 6.9 deltas.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (top-of-doc currency note; appendix WP 6.6/6.8 sections; any `current to WordPress 6.8` strings).
  - `wordpress-performance-optimization-checklist.md` (Modern additions appendix).
  - `enterprise-performance-operational-checklist.md` (Modern additions appendix).
- **What is wrong:** Three docs frame May 2026 material as "current through WordPress 6.8." Per the WordPress release archive, **6.9.4** is the current stable as of May 2026, with material performance changes documented in the 6.9 Field Guide.
- **Scope limit:** The body of these docs is about the practice of performance work and is not version-sensitive in most places. Only version-specific content (Speculation Rules, autoload, Performance Lab, query cache, cron spawn) needs active refresh. Do **not** rewrite untouched guidance just because the version stamp changed.
- **Edit instructions:**
  1. Change every `current to WordPress 6.8, May 2026` (or equivalent) to: `Last verified against WordPress 6.9.4 on 2026-05-18`.
  2. Rename "Modern additions" appendices to "Modern additions (verified against WordPress 6.9.4, 2026-05-18)".
  3. Add a new subsection in the developer reference appendix and brief notes in both checklist appendices titled **WordPress 6.9 performance deltas**:

     > **WordPress 6.9 performance deltas (Field Guide, November 2025)**
     >
     > WordPress 6.9 (released for general availability November 2025; current patch 6.9.4 as of 2026-03-11) added or changed several performance-relevant behaviors. The most material for this guide:
     >
     > - **Frontend performance:** see the [WordPress 6.9 Frontend Performance Field Guide](https://make.wordpress.org/core/2025/11/18/wordpress-6-9-frontend-performance-field-guide/) for the full inventory. Notable: continued image-loading improvements building on 6.6/6.8 work, refinements to block render performance.
     > - **Query cache and helper functions:** 6.9 introduces additional cache helper functions and refines query cache key handling. Audit any plugin code that intercepts query cache behavior.
     > - **WP-Cron spawn timing:** 6.9 changes when cron spawn is attempted relative to request lifecycle. Sites that already use external cron runners (see §16) are unaffected; sites relying on default request-triggered cron may see a behavior shift.
     >
     > For the full delta list, see the [WordPress 6.9 Field Guide](https://make.wordpress.org/core/2025/11/25/wordpress-6-9-field-guide/).

- **Verification sources:**
  - WP.org release archive: <https://wordpress.org/download/releases/>
  - WP 6.9.4 release notes: <https://wordpress.org/documentation/wordpress-version/version-6-9-4/>
  - 6.9 Field Guide: <https://make.wordpress.org/core/2025/11/25/wordpress-6-9-field-guide/>
  - 6.9 Frontend Perf Field Guide: <https://make.wordpress.org/core/2025/11/18/wordpress-6-9-frontend-performance-field-guide/>
- **Acceptance criteria:**
  - No remaining `current to WordPress 6.8, May 2026` strings.
  - Each doc has a per-section `last verified on YYYY-MM-DD` where claims were rechecked.
  - WordPress 6.9 deltas subsection appears in the developer reference appendix.

---

### P1.2 — Replace New Relic transaction examples

- **Status:** `accepted`
- **Origin:** source-derived (VIP operational checklist §20).
- **Severity:** Medium. Misleading instrumentation; duplicated incorrect snippet.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (§26 measurement tools, New Relic example).
  - `enterprise-performance-operational-checklist.md` (§20 New Relic subsection).
- **What is wrong:** Both copies call `newrelic_start_transaction( 'my_custom_transaction' )` as if the argument names a custom transaction. The argument is the **New Relic application name**, used for advanced cases like queue workers that end one transaction and start another in a different app. For naming the current request's transaction, the correct API is `newrelic_name_transaction()`.
- **Edit instructions:** Replace both copies with this snippet:

  ```php
  // Guard so the code is safe whether the New Relic PHP agent is loaded or not.
  if ( extension_loaded( 'newrelic' ) && function_exists( 'newrelic_name_transaction' ) ) {
      // Name the current transaction so it appears as a distinct entry
      // in the New Relic APM transaction list.
      newrelic_name_transaction( 'my_custom_transaction' );
  }

  // Optional: add custom attributes for filtering and querying in NR Insights/NRQL.
  if ( function_exists( 'newrelic_add_custom_parameter' ) ) {
      newrelic_add_custom_parameter( 'plugin_context', 'myplugin_expensive_path' );
  }
  ```

  Replace the surrounding prose to read approximately: *Use `newrelic_name_transaction()` to give a request a distinct name in APM. The `newrelic_start_transaction()` API takes a New Relic application name (not a transaction name) and is reserved for advanced patterns such as queue workers manually ending one transaction and starting another in a different application.*

- **Verification sources:**
  - <https://docs.newrelic.com/docs/apm/agents/php-agent/php-agent-api/newrelic_start_transaction/>
  - <https://docs.newrelic.com/docs/apm/agents/php-agent/php-agent-api/newrelic_name_transaction/>
- **Acceptance criteria:**
  - Both files use `newrelic_name_transaction()` for naming and guard with `extension_loaded`/`function_exists`.
  - No remaining call to `newrelic_start_transaction()` with a transaction-name string argument.

---

### P1.4 — Refresh Performance Lab feature-plugin language

- **Status:** `accepted`
- **Origin:** synthesis-introduced.
- **Severity:** Medium. Stale operational guidance.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (§22 Performance Lab subsection).
  - `wordpress-performance-optimization-checklist.md` (Modern additions appendix).
  - `enterprise-performance-operational-checklist.md` (Modern additions appendix).
- **What is wrong:** Lists use stale module names (e.g. "WebP Uploads") and mix the older "modules inside Performance Lab" framing with the current feature-plugin model.
- **Edit instructions:** Replace the static feature-plugin list with dated, source-checked wording:

  > **Performance Lab feature plugins (verified against the plugin directory on 2026-05-18)**
  >
  > [Performance Lab](https://wordpress.org/plugins/performance-lab/) is the Core team's feature-plugin discovery and management layer. As features mature inside the Performance Lab ecosystem they either graduate into Core or remain as standalone plugins; the catalog rotates over time. Verify the current featured plugins on the Performance Lab plugin page before recommending any specific module.
  >
  > Featured plugins as of the verification date above include:
  >
  > - **Modern Image Formats** — formerly "WebP Uploads"; stores additional WebP/AVIF versions of uploaded images and serves the modern format to supporting browsers.
  > - **Image Placeholders** — formerly "Dominant Color Images"; CSS background placeholder while the image loads.
  > - **Image Prioritizer** — automated `fetchpriority` adjustments for likely LCP candidates.
  > - **Enhanced Responsive Images** — refined `sizes` attribute computation, including for lazy-loaded images.
  > - **Speculative Loading** — Settings UI and additional eagerness modes on top of Core's 6.8 speculation rules support.
  > - **Optimization Detective** — opt-in RUM that informs Core/Performance Lab decisions.
  > - **Modern Polyfills, View Transitions, Performant Translations, Embed Optimizer, Instant Back/Forward** — additional featured plugins, individual relevance depends on site.
  >
  > Recommendation: evaluate Performance Lab on staging, look at the current Featured Plugins list at the verification time, and adopt specific plugins by name only when they match the site's documented performance need.

  Keep the verification-date language in the heading so future readers know the list is volatile and dated.

- **Verification sources:**
  - <https://wordpress.org/plugins/performance-lab/>
  - Individual featured plugins (each has its own plugin-directory page).
- **Acceptance criteria:**
  - No remaining reference to "WebP Uploads" as a current module name.
  - Each appendix list is prefaced with a verification date.
  - The plain-language "verify before recommending" note appears in the developer reference subsection.

---

### P2.1 — Normalize cache-layer boundaries in checklists

- **Status:** `accepted`
- **Origin:** source-derived (Remkus and VIP checklists were always thinner than reference docs on this).
- **Severity:** Medium. Reduces a common operator misconception; canonical wording already exists in the reference docs.
- **Affected files:**
  - `wordpress-performance-optimization-checklist.md`
  - `enterprise-performance-operational-checklist.md`
- **What is wrong:** The two checklists do not consistently distinguish `WP_CACHE`/`advanced-cache.php` from `object-cache.php`. The reference docs do.
- **Edit instructions:** Insert this concise canonical paragraph into both checklists at the start of any cache-related section (good candidates: §5 Full-page caching in the Remkus checklist; §12 Object caching in the VIP checklist):

  > **Cache-layer terminology**
  >
  > Three distinct WordPress caching subsystems are often conflated. `WP_CACHE` is a constant that allows WordPress to load the `wp-content/advanced-cache.php` drop-in for **page caching** (saving complete rendered HTML). `wp-content/object-cache.php` is a separate drop-in for **persistent object caching** (Redis/Memcached, caching database/query/application objects across requests). The Transients API uses object cache when persistent caching is configured, otherwise falls back to the `wp_options` table. See `REFERENCE-WP-Transients-Persistent-Object-Cache.md` and `DEVELOPER_REFERENCE.md` §4 for full treatment.

- **Verification sources:**
  - Already-validated text in `DEVELOPER_REFERENCE.md` §4 and `REFERENCE-WP-Transients-Persistent-Object-Cache.md` §4.
- **Acceptance criteria:**
  - Both checklists contain the canonical paragraph or a verbatim equivalent.
  - Subsequent mentions of `WP_CACHE` in either checklist do not contradict the paragraph.

---

### P2.2 — Add WP-CLI package availability caveats

- **Status:** `accepted`
- **Origin:** source-derived (both Remkus and VIP source materials show these commands without caveats).
- **Severity:** Medium. Prevents failed diagnostic steps on stock WP-CLI installs.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (any section showing `wp profile` or `wp doctor`; specifically §10 hook profiling and §26 measurement tools).
  - `wordpress-performance-optimization-checklist.md` (§1 baseline measurement / WP-CLI block).
- **What is wrong:** Both docs present `wp profile stage`, `wp profile hook`, and `wp doctor check` as if they are always available. They are package-backed (`wp-cli/profile-command` and `wp-cli/doctor-command`); stock WP-CLI installs do not include them.
- **Edit instructions:** Insert this caveat directly above the first example block of these commands in each file:

  > **Availability check.** `wp profile` and `wp doctor` are not bundled with WP-CLI; they ship as separate command packages. Check availability before using:
  >
  > ```bash
  > wp cli has-command profile && echo "profile available"
  > wp cli has-command doctor && echo "doctor available"
  > # Install if missing and your environment allows package installs:
  > # wp package install wp-cli/profile-command
  > # wp package install wp-cli/doctor-command
  > ```
  >
  > If neither command nor package install is available (common on managed hosts), fall back to Query Monitor, APM traces, host-provided profilers, or in-code `microtime()` timers as described in §26.

- **Verification sources:**
  - <https://developer.wordpress.org/cli/commands/profile/>
  - <https://github.com/wp-cli/profile-command>
  - <https://github.com/wp-cli/doctor-command>
- **Acceptance criteria:**
  - The first occurrence of `wp profile` or `wp doctor` in each doc is preceded by the availability check.
  - Subsequent occurrences do not need to repeat the caveat.

---

### P2.3 — Normalize autoload guidance in general checklist body

- **Status:** `accepted`
- **Origin:** source-derived (Remkus checklist predates WP 6.6).
- **Severity:** Medium. Internal contradiction — modern API in appendix, legacy `yes`/`no` in body.
- **Affected files:**
  - `wordpress-performance-optimization-checklist.md` (primary). Also verify `enterprise-performance-operational-checklist.md` for the same issue; the developer reference should already be consistent.
- **What is wrong:** Body says things like "set large rarely-used options to `autoload = no` where safe" (legacy SQL vocabulary). The appendix already added 6.6 vocabulary and `wp_set_option_autoload()`/`wp option set-autoload`. The body should match.
- **Edit instructions:** In every operational bullet that mentions autoload:
  - Replace `autoload = no` with `autoload = off`.
  - Replace `autoload = yes` with `autoload = on`.
  - Add a parenthetical the first time the new vocabulary appears: `(WordPress 6.6+ vocabulary; older rows may still use 'yes'/'no' — see appendix)`.
  - Prefer `wp_set_option_autoload( $name, false )` or `wp option set-autoload $name off` over raw SQL `UPDATE` statements.
- **Verification sources:**
  - Make/Core: <https://make.wordpress.org/core/2024/06/18/options-api-disabling-autoload-for-large-options/>
  - `wp_set_option_autoload()`: <https://developer.wordpress.org/reference/functions/wp_set_option_autoload/>
- **Acceptance criteria:**
  - No `autoload = yes` / `autoload = no` strings in the body (appendix may retain them as legacy-vocabulary explanation).
  - All operational examples use the new API or CLI form.

---

### P1.3 — Repair partial-output / personalized fragment cache guidance

- **Status:** `accepted`
- **Origin:** mixed (VIP pattern + synthesis wording).
- **Severity:** Medium. Prevents cache bleed, high-cardinality growth, and stale personalized output.
- **Affected files:**
  - `DEVELOPER_REFERENCE.md` (§18 partial-output / fragment caching).
  - `enterprise-performance-operational-checklist.md` (§7 partial output caching).
  - `wordpress-performance-optimization-checklist.md` — verify related cache-key guidance.
- **What is wrong:** Developer reference says "key on user ID — or don't cache it"; enterprise example keys only on `get_current_blog_id()`. Neither warns about cardinality, privacy exposure, or invalidation triggers.
- **Edit instructions:** Add a shared **Cache-key safety checklist** to the developer reference §18 (canonical home) and reference it from the enterprise checklist. Draft text:

  > **Cache-key safety checklist for fragment / partial-output caching**
  >
  > Before caching a fragment with `wp_cache_set()` or `set_transient()`, verify that the key includes every dimension that varies the output:
  >
  > - **Site / blog scope:** `get_current_blog_id()` on multisite.
  > - **Locale:** `get_locale()` or `determine_locale()` if locale affects content.
  > - **Currency / region:** any active currency, region, or store context.
  > - **Auth state:** logged-in vs logged-out as separate keys.
  > - **User identity:** only when the fragment is intentionally per-user and you have evaluated the privacy and cardinality implications below.
  > - **Role / capability:** if the fragment differs by role or capability, include the relevant subset.
  > - **A/B / personalization bucket:** include the bucket identifier.
  > - **Query parameters that change output:** explicit allowlist, never the raw `$_GET`.
  >
  > Privacy and cardinality:
  >
  > - **Never** cache personalized output under a shared key. Even one shared-key mistake can leak one user's content to another.
  > - Per-user keys grow cache footprint linearly with active users. Bound this with short TTLs and only for fragments where the regenerate cost dominates.
  > - On persistent object caches, monitor key cardinality and memory pressure for any per-user fragment cache group.
  >
  > Invalidation triggers:
  >
  > - Source content change: `save_post`, custom post type hooks, ACF/CMB2 update hooks.
  > - User profile / role / capability change: `set_user_role`, `profile_update`.
  > - Locale / settings change.
  > - Multisite blog switch / domain change.

  After the new checklist, update the existing partial-output examples in both docs to use a cache key that demonstrates several of these dimensions (e.g., `recent_posts_sidebar_v2_blog{N}_locale{L}_role{R}`), and add a comment on invalidation.

- **Verification sources:**
  - Already-validated transients guidance in `REFERENCE-WP-Transients-Persistent-Object-Cache.md` §10 and §12.
- **Acceptance criteria:**
  - Developer reference §18 contains the Cache-key safety checklist.
  - Enterprise checklist §7 references the checklist and the example demonstrates multi-dimensional keying.
  - No remaining "key on user ID — or don't cache it" wording without the surrounding caveats.

---

### P3.2 — Split API endpoint baselines from Core Web Vitals baselines

- **Status:** `accepted`
- **Origin:** source-derived (Remkus checklist baseline table mixes the two).
- **Severity:** Low. Clarity issue isolated to one document.
- **Affected files:**
  - `wordpress-performance-optimization-checklist.md` (§1 baseline measurement table, lines ~84–88).
- **What is wrong:** Baseline table mixes `/wp-json/...` (a REST endpoint with no LCP/INP/CLS) into the same table as page routes (which do have CWV).
- **Edit instructions:** Replace the single table with two:

  > Page-render baseline:
  >
  > | Target | State | TTFB | LCP | INP | CLS | Cache status | Notes |
  > |---|---:|---:|---:|---:|---:|---|---|
  > | `/` | logged out, warm cache |  |  |  |  |  |  |
  > | `/shop/` | logged out, warm cache |  |  |  |  |  |  |
  > | (other key page routes) |  |  |  |  |  |  |  |
  >
  > Server / API route baseline:
  >
  > | Target | State | TTFB | Payload size | Cache status | Notes |
  > |---|---:|---:|---:|---|---|
  > | `/wp-json/...` | logged in/out |  |  |  |  |
  > | `/wp-admin/admin-ajax.php?action=...` | varies |  |  |  |  |
  > | Other dynamic endpoints |  |  |  |  |  |

- **Verification sources:** internal consistency only.
- **Acceptance criteria:**
  - Two tables under §1.
  - `/wp-json/` rows no longer appear under LCP/INP/CLS columns.

---

### P3.3 — Isolated technical wording fixes (OPcache JIT, 14 KB packet, Redis preference)

- **Status:** `accepted` (all three sub-items).
- **Origin:** synthesis-introduced.
- **Severity:** Low. Precision improvements.
- **Affected files:** `DEVELOPER_REFERENCE.md`
- **Sub-items:**

  **P3.3a OPcache JIT caveat (lines ~469–485):** Add a caveat after the sample `php.ini` block:

  > Note on `opcache.jit_buffer_size`: PHP's JIT compiler is not a clear win for WordPress web-request workloads in most measurements. It consumes memory that may be more valuable for OPcache bytecode storage or PHP-FPM workers. Leave JIT off unless representative benchmarks of the specific site (cached + uncached paths, p95 TTFB, worker saturation) show a measurable benefit.

  Either keep the example with the caveat or remove `opcache.jit_buffer_size` from the example entirely.

  **P3.3b Critical CSS "14 KB" wording (lines ~1156–1163):** Replace "Keep critical CSS under ~14 KB so it fits in the first TCP packet." with:

  > Keep critical CSS small. The ~14 KB figure is a rule of thumb derived from the standard initial congestion window (10 × MSS ≈ 14 KB across multiple segments), not a single-packet limit. Real behavior depends on TCP/TLS/HTTP-version setup, server configuration, and competing response bytes. Treat 14 KB as an order-of-magnitude budget; measure LCP and HTML transfer time on representative connections to choose the actual size.

  **P3.3c Redis vs Memcached (lines ~818–827):** Soften the universal recommendation. Replace with:

  > **Backend selection.** Use the host-supported `object-cache.php` drop-in first; the most common production-grade options are Redis (via Object Cache Pro, the bundled WP VIP drop-in, or open-source plugins) and Memcached (via Memcached Redux or platform-bundled drop-ins). Absent a platform constraint, Redis is generally a better match for WordPress workloads because of richer observability (per-key TTLs, hot-key detection), data structures useful for cache groups, and atomic operations used by some lock patterns. Memcached is appropriate when it is the platform-supported, well-instrumented default — switching backends has operational cost and should be justified by measured cache hit-rate, latency, eviction, and failure behavior on the target host.

- **Verification sources:**
  - PHP JIT discussion: <https://wiki.php.net/rfc/jit>
  - Initial congestion window: RFC 6928 (10 × MSS recommendation).
  - Already-validated platform-conditional language in `AGENTS.md` authority hierarchy.
- **Acceptance criteria:**
  - JIT line either removed or annotated with measure-first caveat.
  - "14 KB first TCP packet" wording removed.
  - Redis recommendation framed as conditional rather than universal.

---

### P3.1 — Mechanical cleanup: `@dknauss` tokens and broken cross-reference links

- **Status:** `accepted`
- **Origin:** synthesis-introduced.
- **Severity:** Low. Trust polish.
- **Affected files:** all four source documents.
- **What is wrong:** Stray `@dknauss` attribution tokens appear in body text where they don't belong. Cross-reference links to sibling folders (e.g., `../remkus-make-wordpress-fast/`, `../wpvip-enterprise-performance/`, `../wordpress-transients-object-cache/`) point at paths that don't exist in this repo.
- **Edit instructions:**
  1. Search every source doc for `@dknauss` and either remove (if appearing as a stray attribution) or move to a clearly metadata-only context (CHANGELOG or front-matter comment).
  2. Search every source doc for `../remkus-make-wordpress-fast/`, `../wpvip-enterprise-performance/`, `../wordpress-transients-object-cache/`, and `../wordpress-performance-master-reference/`.
  3. For each match, decide the new link target:
     - **In-repo:** if the referenced content now lives in this repo, point to the in-repo file (e.g., `./REFERENCE-WP-Transients-Persistent-Object-Cache.md` or `./wordpress-performance-optimization-checklist.md`).
     - **External companion repo:** if the link is to material that lives elsewhere, use a full URL or remove the link if no public URL exists.
  4. After editing, run `grep -rn 'remkus-make-wordpress-fast\|wpvip-enterprise-performance\|wordpress-transients-object-cache\|wordpress-performance-master-reference\|@dknauss' .` to confirm no stale matches remain.
- **Verification sources:** none external; internal grep.
- **Acceptance criteria:**
  - Zero `@dknauss` matches in body text of source docs.
  - Zero sibling-folder relative paths matching the pre-move locations.
  - All in-repo cross-references resolve to existing files.

---

## Findings — declined

None. All P0–P3 findings in `synthesis.md` are accepted.

## Findings — deferred

None. All accepted findings are scheduled for the current edit pass.

## Findings — needs external verification before editing

The following accepted findings require external verification by the executing agent before applying edits. Sources to consult are listed in each finding above.

- **P0.1** — verify Speculation Rules Core defaults on a clean WP 6.8+ install or against Make/Core documentation before pasting the canonical paragraph.
- **P1.1** — verify the current WordPress stable release and the 6.9 Field Guide contents on the verification date used in the stamp.
- **P1.2** — verify the New Relic PHP agent API signatures against current New Relic documentation.
- **P1.4** — verify the current Performance Lab featured plugins on the WordPress.org plugin directory on the verification date.

## Post-edit verification

After all passes complete, run:

```bash
# Stale patterns that should be gone
grep -rn "prerender on \`mousedown\`\|Settings → Reading\|WebP Uploads\|autoload = 'yes'\|autoload = 'no'\|newrelic_start_transaction\|@dknauss\|current to WordPress 6.8, May 2026" \
  DEVELOPER_REFERENCE.md \
  REFERENCE-WP-Transients-Persistent-Object-Cache.md \
  wordpress-performance-optimization-checklist.md \
  enterprise-performance-operational-checklist.md

# Sibling-folder relative paths that should be repointed
grep -rn "\.\./remkus-make-wordpress-fast\|\.\./wpvip-enterprise-performance\|\.\./wordpress-transients-object-cache\|\.\./wordpress-performance-master-reference" \
  *.md

# Should produce no matches.
```

Then update `CHANGELOG.md` with the actual edits made and tick the corresponding ROADMAP checkboxes.
