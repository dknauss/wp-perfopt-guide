# Source corrections: where this guide improves on Remkus and WP VIP

This document explains, in plain terms, six issues that originate in the Remkus de Vries **Make WordPress Fast** course materials and/or the WP VIP Learn **Enterprise WordPress Performance** course materials, and how the guides in this repository correct them.

These aren't catastrophic errors in the source courses — both are excellent and substantially more accurate than most WordPress performance content. But six things are worth flagging because they can quietly mislead a careful reader, and because anyone using this guide alongside the original courses should know where the two diverge.

The editorial review that surfaced these is `reviews/rounds/2026-05-18/closeout.md`. Each item below maps to a closeout finding ID.

---

## 1. The WP-Cron disable snippet appears before its replacement

**Finding ID:** P0.3 · **Severity:** High · **Source:** Both Remkus and WP VIP

### What the source courses show

Both courses teach the standard performance pattern of disabling WordPress's request-triggered cron and replacing it with a real server cron. The Remkus operator checklist and the WP VIP WP-Cron lesson both present the change as:

1. Add `define( 'DISABLE_WP_CRON', true );` to `wp-config.php`.
2. Set up an external cron runner (`wp cron event run --due-now` via system cron, or a `wget`/`curl` of `wp-cron.php`).

### Why it's a problem

The order on the page matches the order an inattentive reader will apply the change. If you set the constant before the external runner is actually firing, you've stopped every scheduled event on the site until the runner is in place: scheduled posts don't publish, WooCommerce Action Scheduler jobs queue without running, plugin update checks stall, password-reset emails sit unsent. On a busy production site this can be visible to customers within minutes.

The risk is greater than it looks because copy-pasting from a checklist is exactly how this change typically gets applied in practice.

### What we do instead

Our guides reorder the steps: install the external cron runner first, verify it is firing (check `wp cron event list --due-now`, watch the runner's logs), then set the constant, then verify scheduled events still complete. We also include a rollback path (comment out the `define` line and clear OPcache) and a callout for Action Scheduler-heavy sites where cron backlog can build silently.

### Plain-language takeaway

If a guide tells you to "disable WP-Cron and use real cron," always set up real cron first. Never disable the existing scheduler before the replacement is proven to work.

---

## 2. The New Relic example uses the wrong API

**Finding ID:** P1.2 · **Severity:** Medium · **Source:** WP VIP

### What the source course shows

The WP VIP enterprise checklist includes a measurement example that wraps a function call with `newrelic_start_transaction( 'my_custom_transaction' )` to create a custom transaction in the APM tool.

### Why it's a problem

That isn't how `newrelic_start_transaction()` works. Per New Relic's PHP-agent documentation, the function takes an **application name** as its argument and is used for advanced patterns — like a long-running queue worker that wants to end one transaction and start another in a different New Relic application. It does not name the current transaction.

For naming a transaction so it appears as a distinct entry in the APM transaction list, the correct API is `newrelic_name_transaction()`. The original snippet won't crash, but it produces misleading APM data: transactions may be filed under unexpected application names, or the instrumentation may silently fail to do what the operator thinks it's doing. That's worse than no instrumentation — it leads to wrong conclusions during a performance investigation.

### What we do instead

We replace the snippet with `newrelic_name_transaction()` guarded by `extension_loaded( 'newrelic' )` and `function_exists()` so the code is safe whether the agent is loaded or not. We also add a sentence explaining the distinction between naming a transaction and starting/ending one, so a reader who is curious about `newrelic_start_transaction()` understands when it would be appropriate.

### Plain-language takeaway

If you copy a New Relic snippet from anywhere, double-check the API name against current New Relic documentation. The PHP agent has a surprising number of similarly-named functions with very different semantics.

---

## 3. The checklists don't fully distinguish the WordPress caching subsystems

**Finding ID:** P2.1 · **Severity:** Medium · **Source:** Both Remkus and WP VIP

### What the source courses teach

Both course checklists discuss page caching, object caching, transients, and the `WP_CACHE` constant — but they don't always pause to clarify how those subsystems relate. The deeper lessons in both courses cover the distinction; the operational checklists assume you already know.

### Why it's a problem

WordPress has three different cache-related drop-in files that often get conflated:

- **`WP_CACHE`** is a constant. When set to `true`, it tells WordPress to load `wp-content/advanced-cache.php` for page caching (saving complete HTML).
- **`advanced-cache.php`** is the page-cache drop-in. It serves complete rendered pages without running PHP.
- **`object-cache.php`** is a *different* drop-in, used by Redis/Memcached integrations for persistent object caching (caching database query results and application objects across requests).

These three are independent: `WP_CACHE` does not enable Redis. Object caching can work without `WP_CACHE`. And the Transients API uses object cache when persistent object caching is available, but falls back to the `wp_options` table otherwise.

When operators conflate these — for example, by assuming setting `WP_CACHE` will give them Redis — they make confidence-shaped configuration decisions on wrong premises.

### What we do instead

We borrow the precise paragraph from the standalone transients/object-cache reference and paste it into both operational checklists, so the distinction is stated up front rather than left to be inferred.

### Plain-language takeaway

`WP_CACHE`, `advanced-cache.php`, and `object-cache.php` are three different things. If a guide treats them as interchangeable, treat that guide with caution on cache-related guidance.

---

## 4. The `wp profile` and `wp doctor` commands aren't always available

**Finding ID:** P2.2 · **Severity:** Medium · **Source:** Both Remkus and WP VIP

### What the source courses show

Both courses prominently use `wp profile stage`, `wp profile hook`, and `wp doctor check` as first-line diagnostic commands, presented as if they're always available when WP-CLI is installed.

### Why it's a problem

They aren't bundled. `wp profile` is provided by the separate `wp-cli/profile-command` package, and `wp doctor` by `wp-cli/doctor-command`. On stock WP-CLI installs and on many managed WordPress hosts, these commands simply don't exist — and on many managed hosts, package installation is blocked.

For an operator working through a checklist sequentially, the first diagnostic step fails. That's a worse outcome than just not showing the command at all, because it creates uncertainty about what else in the guide might also not apply.

### What we do instead

We add an availability check at the first mention of these commands in each guide: `wp cli has-command profile`, with a note on the package-install path where permitted, and a fallback list (Query Monitor, APM traces, host-provided profilers, in-code `microtime()` timers) for environments where the commands aren't available and can't be installed.

### Plain-language takeaway

`wp profile` and `wp doctor` are powerful but not standard. Always check `wp cli has-command profile` first. If the answer is no and you can't install packages, fall back to Query Monitor or APM — they're available in more environments anyway.

---

## 5. The autoload vocabulary in Remkus's checklist is from before WordPress 6.6

**Finding ID:** P2.3 · **Severity:** Medium · **Source:** Remkus

### What the source course teaches

The Remkus operator checklist tells readers to "set large rarely-used options to `autoload = no`" and uses SQL queries that filter `WHERE autoload = 'yes'`.

### Why it's a problem

This was correct when the course was recorded. As of WordPress 6.6 (June 2024), the `autoload` column can hold one of five values: `'on'`, `'off'`, `'auto'`, `'auto-on'`, and `'auto-off'`. Old `'yes'`/`'no'` rows still exist on upgraded sites and are treated as `'on'`/`'off'`, but newly written rows use the new vocabulary. Queries that filter only on `'yes'` will silently miss a growing portion of autoloaded options as sites turn over.

WordPress 6.4 also introduced first-class API functions (`wp_set_option_autoload()`, `wp_set_options_autoload()`) and a WP-CLI command (`wp option set-autoload`) for managing the autoload state without hand-editing the database column. The course's guidance is honest for its recording date but is now stale.

### What we do instead

We've already updated the appendix of both checklists with the 6.6 vocabulary and the modern API/CLI. This fix completes the work by normalizing the **body** of the general checklist to match the appendix: replacing `autoload = yes/no` with `autoload = on/off`, preferring the API and CLI forms over raw SQL `UPDATE` statements, and noting the legacy vocabulary in passing.

### Plain-language takeaway

If a guide uses `autoload = 'yes'` SQL queries to inspect WordPress options on a modern (6.6+) site, the query is incomplete. Use `WHERE autoload IN ('yes', 'on', 'auto', 'auto-on')` or, better, use the modern API.

---

## 6. The baseline-measurement table mixes API endpoints with Core Web Vitals

**Finding ID:** P3.2 · **Severity:** Low · **Source:** Remkus

### What the source course shows

The Remkus operator checklist has a baseline-measurement table where readers record TTFB, LCP, INP, and CLS for a few key URLs. One of the example rows is `/wp-json/...`.

### Why it's a problem

REST API endpoints don't have LCP, INP, or CLS. Those are user-experience metrics for page renders — they describe how a browser draws a page and responds to interaction. A JSON endpoint returns text; it has TTFB and payload size, not a Largest Contentful Paint.

When the table puts `/wp-json/...` alongside page routes with browser metrics in the columns, two things go wrong: a reader recording metrics might think LCP applies to REST endpoints, and the diagnostics that actually matter for endpoints (TTFB, payload size, cacheability, headers) aren't given their own row format.

### What we do instead

We split the single table into two: a **page-render baseline** with TTFB and CWV columns for HTML routes, and a **server / API route baseline** with TTFB, payload size, and cache-status columns for `/wp-json/...`, `/wp-admin/admin-ajax.php`, and similar endpoints. Each table records the metrics that actually apply to the kind of request being measured.

### Plain-language takeaway

Browser metrics like LCP, INP, and CLS are for what users see. Server metrics like TTFB and payload size are for what the network returns. When you build a baseline table, separate the two — even if you measure them at the same time.

---

## Why these matter together

A pattern emerges across the six items: the source courses are strongest at *concepts* and weakest at *operational copy-paste*. Both Remkus and WP VIP teach the right mental model for performance work. The places they slip up are the boundaries between concept and execution — the snippet you paste, the API name you trust, the order of steps in a checklist.

Our guides try to keep both layers honest: the concepts faithful to the sources, the operational details corrected against current authoritative documentation (WordPress Developer Docs, Make/Core dev notes, New Relic agent docs, WP-CLI package docs). Where we diverge from the sources, this document is the audit trail.

## What this document is not

- It is **not** a critique of the source courses. Both are recommended; both are still better than most WordPress performance content. The corrections here are about specific places where time has moved on, or where operational details deserve more care than a course format allows.
- It is **not** complete. Future review rounds may surface more items; if so, they'll be added here with their finding IDs.

## Related

- Editorial review round: `reviews/rounds/2026-05-18/`
- Closeout decisions and execution plan: `reviews/rounds/2026-05-18/closeout.md`
- Editorial methodology: `reviews/methodology/performance-editorial-board.md`
- Agent guidance: `AGENTS.md`
