# Phase 1 Editorial Review — General Checklist

Scope: audited only `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`.

## Finding 1
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 10 and 732
- **Finding:** The two cross-reference links point to paths that do not exist in this repository. The checklist promises a companion WP VIP runbook and a deeper developer reference, but both links currently resolve outside the current repo layout instead of to the sibling files that actually exist at repo root.
- **Severity:** Medium
- **Recommendation:** Update both links to the current in-repo paths for `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wpvip-enterprise-performance-operational-checklist.md` and `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/DEVELOPER_REFERENCE.md`, or move the files so the published paths are real.
- **Verification:** From repo root, `ls` shows both target files exist in the root directory, not under `../wpvip-enterprise-performance/` or `../wordpress-performance-master-reference/`. Re-render the Markdown and confirm both links open the intended local documents.

## Finding 2
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 86–90
- **Finding:** The baseline table mixes page-render metrics and endpoint diagnostics in one structure. Including `/wp-json/...` in a table whose primary columns are `LCP`, `INP`, and `CLS` blurs the distinction between browser UX metrics for rendered pages and backend/API measurements for non-HTML routes.
- **Severity:** Medium
- **Recommendation:** Split frontend-page baselines from API/background-route baselines, or add an explicit note that non-HTML targets should generally record server metrics only (`TTFB`, cache headers, response codes, query/profile data) rather than Core Web Vitals.
- **Verification:** Test a JSON route such as `/wp-json/` in DevTools or Lighthouse: there is no normal page-render context for `LCP`, `INP`, or `CLS`. Confirm that separate frontend and endpoint tables remove the ambiguity.

## Finding 3
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 68–74 and 266–270
- **Finding:** The checklist says “If WP-CLI is available” and then immediately uses `wp profile` and `wp doctor`, but those commands are not included in a stock WP-CLI install. On many systems this guidance will fail with “command not found” even though WP-CLI itself is present.
- **Severity:** Medium
- **Recommendation:** Change the prerequisite to something like “If WP-CLI and the relevant packages are available,” and add package checks or install instructions such as `wp package install wp-cli/profile-command`. If `wp doctor` remains in scope, note that it also requires the doctor package, or tell readers to check command availability first.
- **Verification:** The official `wp profile stage` docs state that the command is installed via `wp package install wp-cli/profile-command`. The official `wp cli has-command` docs use `doctor` as an example of a package-backed command to check/install. Confirm that a stock WP-CLI environment lacks these commands until packages are installed.

## Finding 4
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 303–334 and 745–755
- **Finding:** The autoload guidance mixes legacy storage vocabulary with the newer API-first guidance. The checklist says to set options to `autoload = no`, then later says to use the 6.4+ APIs instead of hand-editing the column. It also uses `wp option set-autoload ... no` while current core documentation deprecates `'yes'`/`'no'` values in the PHP APIs as of WordPress 6.7.
- **Severity:** Medium
- **Recommendation:** Normalize this section around the modern interface: recommend `wp_set_option_autoload()` / `wp_set_options_autoload()` in PHP and `wp option set-autoload <key> off` in CLI examples. Reserve `'yes'`/`'no'` for explaining legacy rows, not as the preferred action syntax.
- **Verification:** Check the official code reference for `wp_set_option_autoload()` and `wp_set_options_autoload()`, which notes `'yes'`/`'no'` are deprecated for backward compatibility. Check the official `wp option set-autoload` docs, which still accept multiple values, and confirm that using modern `on`/`off` wording removes the internal contradiction.

## Finding 5
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 159–160, 171–192, and 343–344
- **Finding:** The checklist distinguishes full-page caching from object caching in broad terms, but it never explicitly states the WordPress drop-in boundary that operators commonly confuse: `WP_CACHE` / `advanced-cache.php` relate to page-cache integration, while `object-cache.php` indicates an external object cache. Because the doc does call out `object-cache.php`, the missing page-cache counterpart leaves a common misconception uncorrected.
- **Severity:** Medium
- **Recommendation:** Add one short clarification in §§4–5 that `define( 'WP_CACHE', true )` loads `wp-content/advanced-cache.php` and does **not** enable Redis/Memcached by itself; keep §9 focused on `wp-content/object-cache.php` as the persistent object-cache drop-in.
- **Verification:** The WordPress `wp-config.php` handbook says `WP_CACHE` includes `wp-content/advanced-cache.php`. The `_get_dropins()` reference identifies `advanced-cache.php` as the “Advanced caching plugin” drop-in and `object-cache.php` as the “External object cache” drop-in. The `wp_start_object_cache()` reference confirms `object-cache.php` is what enables external object cache behavior.

## Finding 6
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 521–560
- **Finding:** The production `wp-config.php` snippet includes `define( 'DISABLE_WP_CRON', true );` before the checklist gives an explicit verification step for a functioning replacement scheduler. Readers who copy the snippet first can silently stop scheduled publishing, cleanup, email, and queue processing.
- **Severity:** High
- **Recommendation:** Add an explicit guardrail immediately above the snippet: only set `DISABLE_WP_CRON` after a verified system cron or equivalent is already in place. Add a verification step such as checking due events before/after with `wp cron event list` / `wp cron event run --due-now`, and for WooCommerce sites confirm Action Scheduler processing still advances.
- **Verification:** The official `wp-config.php` handbook says `DISABLE_WP_CRON` disables cron entirely. The Plugin Handbook page on hooking WP-Cron into the system task scheduler documents disabling WP-Cron only when a real scheduler is configured. Verify on staging by enabling the constant without a replacement cron and confirming due events stop progressing.

## Finding 7
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 758–766
- **Finding:** The Speculative Loading section tells readers to verify the feature under **Settings → Reading** on WordPress 6.8+ installs, but the official core 6.8 dev note describes default frontend enablement and filter-based customization, not a stock core settings UI. The Settings → Reading UI belongs to the standalone Speculative Loading plugin.
- **Severity:** High
- **Recommendation:** Rewrite the verification step so core 6.8+ sites are checked via frontend behavior/output and site conditions (logged-out frontend, pretty permalinks, excluded URLs), and mention Settings → Reading only when the Speculative Loading plugin is installed.
- **Verification:** The official Make/Core post “Speculative Loading in 6.8” describes core defaults: frontend only, logged-out only, disabled without pretty permalinks, with filter-based customization. The official Speculative Loading plugin page says the plugin provides a “Speculative Loading” section on **Settings > Reading**. Confirm a stock core 6.8+ install does not rely on that plugin UI.

## Finding 8
- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/wordpress-performance-optimization-checklist.md`
- **Location:** lines 768–780
- **Finding:** The Performance Lab guidance is stale relative to the current plugin layout. It tells readers to enable “WebP Uploads” inside Performance Lab, but the current Performance Lab plugin now surfaces a broader set of feature plugins and the modern image feature is represented as **Modern Image Formats**. The current UI path is also `Settings > Performance`, not an older module framing.
- **Severity:** High
- **Recommendation:** Update the section to current plugin names and settings paths. If the intended recommendation is modern image generation, reference **Modern Image Formats** explicitly and clarify whether it is being enabled through Performance Lab or installed/configured as a standalone plugin. Keep the staging-first caveat, but align the feature names with current WordPress Performance Team packaging.
- **Verification:** The current Performance Lab plugin page lists featured plugins including Modern Image Formats, Image Placeholders, Image Prioritizer, Enhanced Responsive Images, and Speculative Loading, and says activation/configuration happens from `Settings > Performance`. The current Modern Image Formats plugin page documents its own `Settings > Media` controls and describes WebP/AVIF behavior.
