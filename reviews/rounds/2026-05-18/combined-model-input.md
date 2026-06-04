# WordPress Performance Guide Editorial Review Prompt

You are reviewing the WordPress Performance Optimization Guide for technical accuracy, practical utility, editorial consistency, and source-grounded WordPress performance guidance.

## Instructions

Review the assigned document independently. Do not assume another reviewer will catch issues in your scope.

For each finding, provide:

- **Document:** File containing the issue.
- **Location:** Heading, section, or quote-sized anchor. Use line numbers if practical.
- **Finding:** What is inaccurate, stale, unsafe, duplicated, contradictory, or unclear.
- **Severity:** Critical, High, Medium, Low.
  - Critical: likely to cause broken production behavior, data loss, severe operational harm, or materially false guidance.
  - High: factual error, serious cross-document contradiction, unsafe generalized advice, or version-sensitive claim requiring correction.
  - Medium: incomplete, imprecise, missing caveat, weak verification, or duplicated guidance likely to confuse readers.
  - Low: polish, structure, wording, or minor style issue.
- **Recommendation:** Specific fix or editorial action.
- **Verification:** How to confirm the issue is real and the recommendation is correct.

## Review Focus

Prioritize issues that require technical judgment:

1. **Measurement discipline:** Does the document consistently start with baselines, traces, and verification?
2. **Cache layer precision:** Are page cache, edge cache, browser cache, object cache, transients, OPcache, `WP_CACHE`, `advanced-cache.php`, and `object-cache.php` kept distinct?
3. **WordPress API accuracy:** Are WordPress hooks, constants, cache APIs, Options API, Transients API, REST/admin-ajax behavior, WP-Cron, and query APIs described correctly?
4. **Version-sensitive claims:** Flag claims tied to WordPress, PHP, MySQL/MariaDB, Core Web Vitals, or WP VIP behavior that need current verification.
5. **Enterprise/platform specificity:** Are WP VIP, host-specific, CDN-specific, Redis/Memcached, and plugin-dependent recommendations clearly labeled?
6. **Operational safety:** Are rollback, staging, cache invalidation, high-traffic events, ecommerce flows, logged-in users, personalization, and editor/admin behavior handled safely?
7. **Frontend performance accuracy:** Are LCP, INP, CLS, render-blocking resources, images, fonts, third parties, and browser main-thread work separated correctly?
8. **Database/query guidance:** Are unbounded queries, `WP_Query`, meta queries, taxonomy exclusions, `LIKE`, `EXPLAIN`, indexes, object-cache misses, and N+1 patterns handled precisely?
9. **Cross-document drift:** If guidance overlaps with another document, note any conflicting terminology, order of operations, severity, or recommendation.
10. **Readability:** Flag only readability issues that affect technical comprehension or safe execution.

## Constraints

- Do not suggest broad rewrites unless they fix a technical problem.
- Do not convert conditional guidance into universal rules.
- Do not invent citations. If a claim needs a source, say what authority should be checked.
- If current external verification is required, state the exact claim to verify and the likely authority source.

## Authority Hierarchy

When sources conflict:

1. WordPress core source and WordPress Developer Documentation.
2. WordPress Performance Team and official WordPress.org performance materials.
3. WP VIP documentation for VIP-specific operational guidance.
4. Host/CDN/plugin documentation for platform-specific behavior.
5. Measured evidence from logs, traces, headers, APM, query plans, and reproducible benchmarks.
6. Community/expert guidance as context only, verified against higher authorities.


# Repository Guidance

# AGENTS.md — WordPress Performance Optimization Guide

Agent configuration for AI-assisted editorial and documentation work in this repository. Agents operate under human editorial authority; do not make substantive guidance changes without preserving source-grounded rationale.

## 1. Project Context

- **Project type:** Technical documentation — WordPress performance optimization guidance.
- **Primary audience:** WordPress developers, performance engineers, SREs, technical leads, and enterprise WordPress operators.
- **Goal:** Maintain practical, source-grounded guidance for diagnosing and improving WordPress performance across hosting, caching, database, runtime, frontend, and operational layers.
- **Repository role:** Local source repository for performance guidance and companion references.

## 2. Current Document Set

| Document | Purpose |
|---|---|
| `DEVELOPER_REFERENCE.md` | Unified developer reference and mental model for performance work. |
| `wordpress-performance-optimization-checklist.md` | General WordPress performance checklist and triage flow. |
| `wpvip-enterprise-performance-operational-checklist.md` | Enterprise/WP VIP-oriented operational checklist. |
| `REFERENCE-WP-Transients-Persistent-Object-Cache.md` | Focused reference on transients, object cache, expiration semantics, and cache behavior. |

## 3. Editorial Principles

1. **Measure before prescribing.** Prefer baselines, traces, and verification steps over generic optimization advice.
2. **Keep recommendations conditional.** Tie guidance to request type, traffic pattern, hosting architecture, cache layer, and business constraint.
3. **Distinguish cache layers.** Be precise about page cache, edge cache, browser cache, object cache, transients, OPcache, and database query cache-like behavior.
4. **Avoid cargo-cult performance advice.** Do not recommend removing features, plugins, scripts, or queries without a measured reason.
5. **Protect correctness.** Performance changes must not break authentication, personalization, publishing workflows, editor behavior, ecommerce flows, or security controls.
6. **Prefer reproducible checks.** Include commands, headers, metrics, tools, and expected evidence where possible.

## 4. Voice and Style

- **Practical:** Give the next useful diagnostic step.
- **Candid:** State limitations, trade-offs, and when a change is platform-specific.
- **Precise:** Use exact WordPress, PHP, HTTP, and database terminology.
- **Accessible:** Define uncommon terms on first use and avoid unexplained acronyms.
- **Source-grounded:** Cite authoritative sources for behavior that may change across WordPress versions or platforms.

Formatting rules:

- Markdown throughout. Use `##` for main sections and `###` for subsections.
- Monospace for machine-readable identifiers: `wp-config.php`, `WP_CACHE`, `advanced-cache.php`, `object-cache.php`, `set_transient()`, `Cache-Control`.
- PHP snippets should omit closing `?>` unless the closing tag is the point of discussion.
- Shell commands should be directly runnable or clearly marked as examples.
- Tables are preferred for structured comparisons, layer responsibilities, and triage matrices.

## 5. Authority Hierarchy

When sources conflict, use this precedence:

1. **WordPress core source and Developer Documentation** — behavior of APIs, hooks, constants, and version-specific features.
2. **WordPress Performance Team materials and official WordPress.org performance guidance** — current platform direction and plugin/module behavior.
3. **WP VIP documentation** — enterprise operational guidance, especially for VIP-hosted environments.
4. **Hosting/platform documentation** — authoritative only for that platform.
5. **Measured local evidence** — traces, headers, logs, query plans, APM output, and reproducible benchmarks.
6. **Community articles and expert guidance** — useful context, but verify against higher-precedence sources before presenting as general guidance.

Flag any recommendation that depends on a specific host, CDN, cache plugin, object cache backend, or WordPress version.

## 6. Technical Accuracy Checklist

Before finalizing edits, verify:

- WordPress version references are current for the document's stated date.
- Cache terms are not conflated: `WP_CACHE` does not enable Redis/Memcached by itself; `advanced-cache.php` and `object-cache.php` serve different roles.
- Transients are described correctly with and without persistent object caching.
- HTTP caching guidance accounts for personalization, cookies, query strings, logged-in users, ecommerce carts, previews, and REST/admin-ajax requests.
- Database guidance distinguishes slow queries, unbounded queries, missing indexes, object-cache misses, and inefficient query shapes.
- Frontend guidance separates LCP, INP, CLS, render-blocking resources, image priority, third-party scripts, and browser main-thread work.
- Every optimization includes a way to verify improvement and detect regression.

## 7. Repository Workflow

- Keep planning state in `.planning/` when using GSD-style project management.
- Update `CHANGELOG.md` for meaningful documentation, governance, or workflow changes.
- Do not commit generated exports, logs, screenshots, or local environment files unless explicitly requested.
- Keep source Markdown documents readable in plain GitHub rendering.
- If external facts may have changed, verify them before updating guidance.

## 8. Browser/Playwright Handoff

If a task requires browser automation, screenshots, page interaction, or browser-only inspection and the current session does not have browser tooling, state that a fresh browser-capable session is required. Do not imply browser mode can be enabled mid-session.


# Metrics

# Current Metrics

Last updated: 2026-05-18

## Repository

- Primary Markdown guidance files: 4
- Planning phases: 3
- Completed planning phases: 1

## Canonical Source Files

- `DEVELOPER_REFERENCE.md`
- `wordpress-performance-optimization-checklist.md`
- `wpvip-enterprise-performance-operational-checklist.md`
- `REFERENCE-WP-Transients-Persistent-Object-Cache.md`


--- BEGIN DOCUMENT: DEVELOPER_REFERENCE.md ---

# WordPress Performance Optimization: Unified Developer Reference

A unified, developer-oriented reference for diagnosing and optimizing WordPress performance across ordinary hosting, managed WordPress platforms, and enterprise/VIP-style environments.

This reference synthesizes four source sets:

- Remkus de Vries’ **Make WordPress Fast** course notes.
- WP VIP Learn’s **Enterprise WordPress Performance** course notes.
- WordPress.org developer documentation on transients, object caching, cache bootstrap behavior, the Options API, and modern Core performance features.
- The cache clarification work in `WordPress/Advanced-administration-handbook#485`.

It is written for developers who need to decide **what to measure, where to look, what to change, and how to verify the result**.

> **Currency note (May 2026):** This reference is current through WordPress 6.8. Two areas in WordPress core have changed materially in ways the sources do not address in detail in their present state: 

1. The `wp_options.autoload` vocabulary expanded in WP 6.6 (June 2024). 
2. Speculative loading was merged into Core in WP 6.8 (April 2025). 

Both are included below, and I've noted where the sources are silent or out of date.

@dknauss
---

## 1. Mental model: performance is the result of work

WordPress performance is not one number and not one layer. It is the cumulative result of work performed by:

1. DNS and connection setup.
2. TLS and HTTP negotiation.
3. CDN/edge cache.
4. Origin web server.
5. PHP runtime and OPcache.
6. WordPress bootstrap.
7. MU plugins, normal plugins, and theme code.
8. Database queries.
9. Object cache and transient storage.
10. Template rendering.
11. HTTP response headers.
12. Browser parsing, layout, paint, JavaScript, CSS, images, fonts, and third-party resources.
13. Follow-up requests such as REST, AJAX, media, tracking, personalization, and background calls.

The practical rule is simple:

> Performance improves when you remove work, cache work safely, move work out of the critical path, or make unavoidable work cheaper.

A fast site is not merely a site with a good Lighthouse score or a low TTFB. Users experience:

- how quickly useful content appears;
- how soon the page responds to interaction;
- whether layout remains stable;
- whether the page feels trustworthy and ready.

Backend metrics explain where delays originate. Frontend metrics explain how delays are experienced. You need both.

---

## 2. Source strengths and how to use them

### Remkus / Make WordPress Fast is strongest for

- whole-stack performance thinking;
- user-centric performance and Core Web Vitals;
- request-to-render diagnosis;
- DNS, TLS, and HTTP/2 vs HTTP/3 protocol tradeoffs;
- resource hints (`dns-prefetch`, `preconnect`, `preload`);
- frontend rendering, images, fonts, CSS, JavaScript, and third-party assets;
- plugin stack simplification;
- page builders and DOM bloat;
- WooCommerce and Action Scheduler considerations;
- Multisite resource amplification;
- DevTools and TRACE-style debugging;
- `wp-config.php` as policy (revisions, Heartbeat, debug constants);
- practical operator checklists and client communication.

### WP VIP / Enterprise WordPress Performance is strongest for

- enterprise request-cycle analysis;
- cacheability, edge cache, TTL, invalidation, and cache misses;
- application-level bottlenecks;
- hooks, templates, uncached functions, AJAX, redirects, search, and sitemaps;
- `WP_Query` best practices at production scale;
- unbounded queries;
- taxonomy, post meta, `NOT IN`, `LIKE`, and SQL `EXPLAIN`;
- Elasticsearch/OpenSearch-style query offloading;
- partial-output / fragment caching with `ob_start()` + object cache;
- object-cache race conditions and cache stampedes;
- traffic patterns, high-traffic event prep, load testing, New Relic, and alerting.

Both courses cover Query Monitor heavily; treat it as a tool that belongs to both, not just one.

### WordPress.org developer docs are authoritative for

- Transients API semantics;
- `get_transient()` and `set_transient()` behavior;
- `WP_Object_Cache` behavior;
- `wp_start_object_cache()` and object-cache drop-in loading;
- distinction between `advanced-cache.php`, `object-cache.php`, and `WP_CACHE`;
- the WP 6.6+ Options API autoload vocabulary (`on`/`off`/`auto`/`auto-on`/`auto-off`);
- the Speculation Rules / speculative loading work merged into Core 6.8;
- WP-Cron alternatives and the system task scheduler integration.

### Advanced Admin Handbook PR clarification is strongest for

- explaining that `WP_CACHE` is not a general “turn caching on” switch;
- distinguishing `advanced-cache.php` page-cache drop-ins from `object-cache.php` persistent object-cache drop-ins;
- clarifying that transients are not always memory-backed.

### A note on source freshness

Both source courses were recorded before WordPress 6.4 added helper functions for managing option autoload state, before WordPress 6.6 changed the Options API autoload vocabulary, and before WordPress 6.8 merged the Speculation Rules API. The Remkus operator checklist still filters `autoload = 'yes'`, which is now incomplete (see §12). Neither source course covers Performance Lab modules, modern autoload helper APIs, or Speculation Rules. Where this reference adds material that is not in the source courses, it is marked **Core-only** in the relevant section heading.

---

## 3. Optimization workflow

Use this sequence for almost every performance investigation.

### Step 1: Define the symptom

Classify the problem before touching code.

- High TTFB?
- Slow cached page?
- Slow uncached page?
- Slow admin screen?
- Slow REST endpoint?
- Slow `admin-ajax.php` call?
- Poor LCP?
- Poor INP?
- Poor CLS?
- Search is slow?
- Sitemap generation is slow?
- Cron/background jobs cause spikes?
- Site fails during traffic surges?

### Step 2: Identify the request context

Record:

- exact URL or route;
- logged-in or anonymous;
- cacheable or intentionally dynamic;
- device/network conditions;
- expected traffic level;
- whether the issue is constant, sporadic, traffic-dependent, or deployment-dependent.

### Step 3: Capture a baseline

Do not optimize from memory.

```bash
curl -s -o /dev/null -D headers.txt \
  -w "dns:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total}\n" \
  https://example.com/target/
```

Record:

| Target | User state | Expected cacheability | Cache status | TTFB | LCP | INP | CLS | Notes |
|---|---|---|---|---:|---:|---:|---:|---|
| `/` | anonymous | cacheable |  |  |  |  |  |  |
| `/shop/` | anonymous | cacheable/dynamic |  |  |  |  |  |  |
| `/wp-json/...` | varies | endpoint-specific |  |  |  |  |  |  |

### Step 4: Decide whether WordPress should run

For anonymous public pages, ask first:

- Can this HTML be served from edge/page cache?
- Did it actually hit cache?
- If it missed or bypassed cache, why?

If the page should be cacheable but WordPress is executing, fix cacheability before optimizing PHP or SQL.

### Step 5: If WordPress runs, locate the dominant cost

Check:

- WordPress bootstrap and hooks;
- plugin/theme callbacks;
- database query count and slow queries;
- object-cache hit rate;
- transient usage;
- external HTTP requests;
- template rendering;
- REST/AJAX follow-up requests;
- cron/background tasks.

### Step 6: If the server is fast but the page feels slow, inspect the browser

Check:

- LCP element and timing;
- render-blocking CSS;
- blocking or long-running JavaScript;
- image size and priority;
- font loading;
- layout shifts;
- third-party scripts;
- DOM size and page-builder output;
- main-thread work in DevTools.

### Step 7: Change one thing and verify

Every change needs before/after evidence. If the measured bottleneck does not move, you either fixed the wrong thing or measured the wrong target.

### Naming this discipline: TRACE

Remkus’s course frames this method as **TRACE**: follow the signal through the stack, narrow the pattern, gather evidence before acting. TRACE is not an acronym in the course — it is a discipline of refusing to optimize from guesswork. The decision trees in §27 implement it explicitly.

---

## 4. Cache layers and responsibilities

Caching is not one mechanism. Each layer solves a different problem.

| Layer | Typical mechanism | What it avoids | Common failure |
|---|---|---|---|
| Browser cache | HTTP headers | re-downloading static assets | bad headers or unversioned assets |
| CDN/edge cache | CDN, edge rules | long-distance origin trips | cookies/query strings bypass cache |
| Full-page cache | edge/server/plugin page cache | PHP + database execution | stale content, broad purges, personalization |
| Object cache | Redis/Memcached via `object-cache.php` | repeated DB/application work | poor hit rate, evictions, stampedes |
| Transients | Transients API | repeated expensive computation | unaware of DB fallback, too many keys, stale data |
| OPcache | PHP OPcache | recompiling PHP | stale bytecode, memory exhaustion |
| Runtime/request cache | static variables, non-persistent object cache | repeated work in one request | mistaken for cross-request persistence |

The transients “failure” is not the database fallback itself — the fallback is by design. The failure is writing transient-heavy code without checking whether a persistent object cache is present, so the database silently absorbs work it should not have to do.

### Important distinction

```php
define( 'WP_CACHE', true );
```

`WP_CACHE` allows WordPress to load:

```text
wp-content/advanced-cache.php
```

This is commonly used by page-cache drop-ins.

Persistent object caching is different and uses:

```text
wp-content/object-cache.php
```

`WP_CACHE` does not enable Redis, Memcached, browser caching, or OPcache by itself.

---

## 5. Full-page cache and edge cache

Full-page caching is often the largest backend performance win because it can prevent WordPress from running at all.

### Cacheable candidates

- homepage;
- posts and pages;
- category/tag archives;
- landing pages;
- public product/archive pages when not personalized;
- public documentation pages;
- anonymous GET endpoints that return identical data.

### Bypass candidates

- WordPress admin;
- logged-in personalized views;
- cart;
- checkout;
- account pages;
- previews;
- nonce-sensitive forms;
- private API responses;
- pages that vary by permission, session, cart, or account state.

### Cache miss triage

If a page should be cached but misses, check:

- `Set-Cookie` headers;
- `Cache-Control: no-store`, `private`, or overly conservative directives;
- `Vary: Cookie` or unnecessary variation;
- query strings such as `utm_*`, `fbclid`, `gclid`;
- authentication headers;
- short TTLs;
- frequent full-site purges;
- plugin rules that mark the response uncacheable;
- CDN/origin rule mismatch.

### Query-string fragmentation examples

```text
/shop?utm_source=newsletter&utm_medium=email&utm_campaign=spring_sale
/shop?fbclid=IwAR1XyZExampleValue
/shop?gclid=EAIaIQobChMIExample
/shop?utm_source=facebook&utm_content=carousel_ad_3
/shop?lang=en
/shop?preview=true
/shop?utm_source=newsletter&utm_medium=email&fbclid=IwAR1XyZExampleValue
```

Normalize or ignore marketing parameters when they do not change content. Do not normalize parameters that actually change language, currency, region, personalization, previews, or permissions.

### Platform warning

On enterprise platforms with edge caching, do not blindly add plugin page caching. Combining plugin page cache with platform edge cache can complicate invalidation and increase stale-content risk. Prefer one authoritative full-page cache layer per responsibility.

---

## 6. HTTP headers, TTL, and invalidation

Headers define cache behavior.

Inspect:

```bash
curl -I https://example.com/page/
```

Review:

- `Cache-Control`;
- `Expires`;
- `Vary`;
- `Set-Cookie`;
- CDN cache status headers;
- redirect headers;
- security headers that might affect resource loading.

### TTL guidance

- Use long TTLs for versioned static assets.
- Use shorter TTLs for frequently changing HTML.
- Prefer precise invalidation over universally short TTLs.
- Avoid full-site purges for small content changes when targeted purges are available.
- Watch for invalidation storms during deploys or high-traffic events.

### Redirect diagnostics

```bash
curl -IL https://example.com/some-url/
```

Look for `x-redirect-by` (the diagnostic pattern below originates in VIP’s operational guidance; see VIP operational checklist §4):

```text
x-redirect-by: WordPress
x-redirect-by: Polylang Pro
```

Debugging redirect source in a safe environment:

```php
add_filter( 'x_redirect_by', function( $x_redirect_by, $status, $location ) {
    wp_die( var_dump( array(
        $x_redirect_by,
        $status,
        $location,
        wp_debug_backtrace_summary(),
    ) ) );
}, 10, 3 );
```

---

## 7. DNS, TLS, and HTTP transport

A page cannot be fast if connection setup is slow. The transport layer is the first place a request spends time, and a misconfigured edge can add hundreds of milliseconds before WordPress even runs. Remkus’s Modules 2–3 dedicate twelve lessons to this; the developer-relevant takeaways are below.

### DNS

- Use a reputable DNS provider with fast global resolution (Anycast routing is the standard).
- Avoid long CNAME chains; each indirection adds a lookup.
- Remove stale records.
- Lower TTLs before planned migrations; raise them for stable records.
- Confirm IPv4 and IPv6 behavior are both intentional.

### TLS

- Enforce HTTPS site-wide and end-to-end (origin and CDN).
- Use TLS 1.3 where supported — it cuts a round-trip compared to TLS 1.2.
- Enable session resumption and OCSP stapling at the edge to reduce handshake cost on repeat visits.
- Enable HSTS only after HTTPS is fully correct across subdomains.
- Keep certificates auto-renewing; expired certs are a uniquely catastrophic outage.

### HTTP/2 vs HTTP/3

- HTTP/2 multiplexes streams over one TCP connection and removes head-of-line blocking at the application layer; it is a baseline expectation for production WordPress in 2026.
- HTTP/3 runs over QUIC (UDP) and removes head-of-line blocking at the transport layer too. It helps most on lossy or mobile networks.
- Most CDNs support both; verify that your edge actually negotiates HTTP/3 (`alt-svc` advertised, then a follow-up request actually using `h3`).

### Redirect chains

A single redirect costs a round-trip. Two or three chained redirects can dominate TTFB for the first paint.

- Remove `http://` → `https://` chains by configuring HTTPS directly at the edge.
- Resolve apex vs `www` canonicalization in one hop.
- Resolve trailing-slash canonicalization in one hop.
- Verify with `curl -IL`.

### Useful checks

```bash
curl -I -L https://example.com/
curl -w "namelookup:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} starttransfer:%{time_starttransfer} total:%{time_total}\n" \
  -o /dev/null -s https://example.com/
```

---

## 8. Resource hints: `dns-prefetch`, `preconnect`, `preload`

Resource hints tell the browser to start work before it would otherwise. Used precisely, they shave hundreds of milliseconds off LCP. Used carelessly, they create connection storms and waste mobile bandwidth.

### `dns-prefetch`

Resolves the DNS for an origin in advance. Cheap; safe to use for any third-party origin the page will actually contact.

```html
<link rel="dns-prefetch" href="//fonts.gstatic.com">
```

### `preconnect`

Resolves DNS **and** completes the TCP and TLS handshake in advance. More expensive than `dns-prefetch`, but pays off for origins the browser will hit early.

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Use `crossorigin` for origins that serve credentialed or CORS resources (fonts are the classic example). Without it, the preconnect won’t be reused for the font fetch and you pay the cost twice.

### `preload`

Tells the browser to download a specific resource at high priority. Reserve this for resources that are (a) on the critical rendering path and (b) discovered late by the parser.

```html
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
```

For the LCP image specifically, use `imagesrcset` and `imagesizes` so the preload respects the responsive image strategy:

```html
<link rel="preload" as="image"
      href="/hero-1600.webp"
      imagesrcset="/hero-800.webp 800w, /hero-1600.webp 1600w"
      imagesizes="100vw">
```

### Overuse warnings

- Don’t preconnect to more than ~3–4 origins per page. Each open connection has CPU and memory cost on the client.
- Don’t preload anything the browser would have discovered on its own from the HTML — that just shifts the cost earlier and clutters the network tab.
- Preloaded fonts must match the `type` and `crossorigin` of the actual fetch, or the browser will fetch the font twice.

### Modern alternative: speculative loading

For navigation hints (not resource hints), see §22 — WP 6.8 ships Speculation Rules support that can prefetch or prerender the next likely page.

---

## 9. PHP runtime, OPcache, and worker capacity

When WordPress executes, PHP runtime configuration sets the floor on how fast it can possibly run.

### OPcache

OPcache caches compiled PHP bytecode in memory so each request does not re-parse and re-compile every PHP file. It is the single largest PHP-level perf win, and it is often misconfigured.

- Confirm OPcache is enabled for web requests (check `phpinfo()` or a Site Health module).
- Confirm `opcache.memory_consumption` is not exhausted. A full cache silently degrades — old entries get evicted and re-compiled on each request.
- Confirm `opcache.max_accelerated_files` is large enough for your codebase (WordPress core alone has ~3,000 PHP files; a heavy WooCommerce site can pass 30,000).
- Set `opcache.validate_timestamps` based on your deploy workflow: leave it on (with a sane `revalidate_freq`) for hosts where files change in place; turn it off only if you reset OPcache as part of deploys.

```ini
opcache.enable=1
opcache.memory_consumption=256
opcache.max_accelerated_files=20000
opcache.validate_timestamps=1
opcache.revalidate_freq=60
opcache.jit_buffer_size=100M   ; optional, PHP 8+
```

### PHP workers

PHP workers (php-fpm pool size, Apache MPM workers, etc.) set the concurrency ceiling. If you run out of workers, requests queue and TTFB collapses for everyone — even cached pages can stall if the CDN is forced back to origin.

- Size workers based on observed concurrent uncached requests, not total traffic. A site that fully edge-caches 99 % of traffic needs few workers; one that runs PHP on every request needs many.
- Monitor worker saturation as a primary signal, not just CPU.
- If workers are spending time on slow plugins or external HTTP calls, the fix is to shorten those calls (or move them to background work) rather than adding workers indefinitely.

### PHP version

Use a supported PHP version (8.2+ in 2026; 8.3/8.4 give meaningful perf wins over 7.x without WordPress code changes). Older PHP is slower, less secure, and increasingly unsupported by plugin authors.

---

## 10. WordPress runtime and plugin/theme cost

When WordPress executes, every plugin, theme, hook, query, and external call can add cost.

### Developer checklist

- Are hooks scoped to only the contexts that need them?
- Does code run on every request when it only belongs on one template?
- Are admin-only features loading on the frontend?
- Are frontend assets loaded globally?
- Are queries inside loops?
- Are remote HTTP calls made during page rendering?
- Are expensive computations cached?
- Are plugin modules disabled when unused?
- Are multiple optimization plugins modifying the same assets or cache layers?

### Hook profiling

Use Query Monitor, WP-CLI profile, APM traces, or targeted timing to identify expensive callbacks.

```bash
wp profile stage --url="https://example.com/target/"
wp profile hook --url="https://example.com/target/" --all
wp doctor check
```

### Plugin-stack guidance

Plugin count is not the performance metric. Plugin behavior is.

Review:

- global asset loading;
- database queries;
- remote calls;
- cron jobs;
- autoloaded options;
- cache bypass headers;
- duplicate features across plugins;
- page-builder extensions and widget libraries;
- security and maintenance quality.

---

## 11. Database performance

Database optimization is not “cleaning the database.” It is reducing expensive reads/writes and making unavoidable queries efficient.

### Primary signals

- high query count;
- slow queries;
- duplicate queries;
- full table scans;
- filesorts;
- temporary tables;
- unbounded result sets;
- high autoloaded option size;
- repeated queries that should be cached;
- search/filtering that belongs in a search index.

### `WP_Query` best practices

Use explicit limits:

```php
$query = new WP_Query(
    array(
        'post_type'      => 'post',
        'posts_per_page' => 10,
        'orderby'        => 'date',
        'order'          => 'DESC',
        'no_found_rows'  => true,
    )
);
```

The `no_found_rows => true` flag is mainstream WordPress core guidance, not a VIP-specific recommendation. It suppresses the `SQL_CALC_FOUND_ROWS` clause that powers pagination counts; if you are not using pagination, skipping it is a meaningful win on large `wp_posts` tables. (See WordPress Trac #10469 for the history of why `SQL_CALC_FOUND_ROWS` is now considered an anti-pattern.)

Avoid unbounded queries:

```php
'posts_per_page' => -1
```

This may appear harmless in development and fail at production scale.

### Dangerous patterns

- broad meta queries;
- sorting by unindexed meta values;
- high-cardinality taxonomy filtering;
- large `NOT IN` lists;
- leading-wildcard `LIKE`;
- search implemented with SQL over large content tables;
- accidental broad queries from falsey IDs;
- `switch_to_blog()` in loops on Multisite;
- repeated queries in template partials.

### `NOT IN` example to scrutinize

```sql
SELECT * FROM wp_posts
WHERE post_type = 'post'
  AND post_status = 'publish'
  AND ID NOT IN (1, 2, 3);
```

Large exclusions often scale poorly. Prefer positive selection, precomputed sets, or different data modeling when possible.

### `LIKE` examples

```sql
SELECT * FROM wp_posts WHERE post_title LIKE '%WordPress%';
```

```sql
SELECT * FROM wp_posts WHERE post_title LIKE 'WordPress%';
```

The second form is more index-friendly than a leading wildcard, but serious search workloads should usually move to dedicated search infrastructure.

### `EXPLAIN`

Use `EXPLAIN` on slow SQL:

```sql
EXPLAIN SELECT * FROM wp_posts WHERE post_date > '2023-01-01';
```

```sql
EXPLAIN
SELECT wp_posts.*, wp_postmeta.meta_value
FROM wp_posts
JOIN wp_postmeta ON wp_posts.ID = wp_postmeta.post_id
WHERE wp_posts.post_date > '2023-01-01';
```

Inspect:

- table;
- access type;
- possible keys;
- key actually used;
- estimated rows;
- `Extra` details such as filesort or temporary table usage.

---

## 12. Autoloaded options and `wp_options` (updated for WP 6.6+)

Autoloaded options are loaded early and can affect every request.

### What changed in WordPress 6.6

Before WordPress 6.6 (June 2024), the `wp_options.autoload` column held one of two string values: `'yes'` or `'no'`. As of WordPress 6.6, newly written options use a richer vocabulary:

| Value | Meaning |
|---|---|
| `'on'` | Explicitly marked to autoload (caller passed `true`). |
| `'off'` | Explicitly marked not to autoload (caller passed `false`). |
| `'auto'` | Caller did not pass a value; WordPress decides. Currently autoloads in 6.6; default may change. |
| `'auto-on'` | Dynamically determined to autoload. |
| `'auto-off'` | Dynamically determined not to autoload (e.g., the option is too large). |

Older `'yes'`/`'no'` rows still exist on upgraded sites and are treated as `'on'`/`'off'`. There is no migration; both vocabularies coexist indefinitely.

**WP 6.6 also added automatic skip-autoload behavior for large options** and a Site Health check (“Autoloaded options could affect performance”) that warns when total autoload size exceeds ~800 KB.

### Review queries (6.6-aware)

Old guidance — including the Remkus operator checklist this reference inherits — filters `WHERE autoload = 'yes'`. That misses everything written under the new vocabulary. Use this instead:

```sql
SELECT option_name, LENGTH(option_value) AS size, autoload
FROM wp_options
WHERE autoload IN ('yes', 'on', 'auto', 'auto-on')
ORDER BY size DESC
LIMIT 20;
```

Total autoload footprint:

```sql
SELECT SUM(LENGTH(option_value)) AS autoload_bytes
FROM wp_options
WHERE autoload IN ('yes', 'on', 'auto', 'auto-on');
```

### Changing autoload state

Don’t hand-edit the `autoload` column. Use the WP 6.4+ API:

```php
wp_set_option_autoload( 'my_huge_option', false );      // singular
wp_set_options_autoload( array( 'opt_a', 'opt_b' ), false ); // bulk
```

Or the WP-CLI command:

```bash
wp option set-autoload my_huge_option no
```

### Guidance

- Autoload only small, frequently needed options.
- Do not autoload large serialized blobs.
- Do not treat `wp_options` as a general cache table.
- Watch the Site Health check; address it before it becomes critical.
- Remove orphaned plugin options only after backup and verification.
- Changing autoload flags can break plugins if done blindly; test on staging.

---

## 13. Transients and object cache

Transients are temporary cached values with expiration, but their backend depends on the environment.

### Core rule

- With persistent object cache: transients can be stored in Redis/Memcached/object cache.
- Without persistent object cache: transients fall back to the database, typically `wp_options`.

Therefore:

> Transients are a cache abstraction with a database fallback, not guaranteed memory storage.

This is the design, not a bug. The bug is writing transient-heavy code without checking which backend is in use.

### Database-backed transient row pairs

When transients fall back to the database, an expiring transient typically writes **two** option rows:

```text
_transient_{name}
_transient_timeout_{name}
```

The `_timeout_` row stores the Unix epoch at which the transient expires. On Multisite, network-wide transients use analogous `_site_transient_{name}` / `_site_transient_timeout_{name}` keys (see §24).

### The falsey-value pitfall

`get_transient()` returns `false` for both a cache miss **and** an expired transient. If the cached value itself can legitimately be `false`, `0`, an empty string, or `null`, you cannot distinguish a hit from a miss using the return value alone. Wrap the value or use a sentinel:

```php
$wrapped = get_transient( 'myplugin_result' );

if ( false === $wrapped ) {
    $value   = myplugin_compute();          // could legitimately be 0 or ''
    $wrapped = array( 'value' => $value );
    set_transient( 'myplugin_result', $wrapped, HOUR_IN_SECONDS );
}

$value = $wrapped['value'];
```

### Safe transient pattern

```php
$cache_key = 'myplugin_expensive_result_' . md5( $context_id );
$result    = get_transient( $cache_key );

if ( false === $result ) {
    $result = myplugin_build_expensive_result( $context_id );
    set_transient( $cache_key, $result, HOUR_IN_SECONDS );
}
```

### Use transients for

- expensive query results;
- remote API responses;
- rendered fragments;
- computed values that can be regenerated;
- short-lived shared results.

### Avoid transients for

- permanent settings;
- canonical data;
- values that cannot disappear early;
- huge blobs on sites without persistent object cache;
- per-request or high-cardinality keys;
- private data under shared keys;
- data that changes so frequently it rarely hits cache.

### Inspect database-backed transients

```sql
SELECT option_name, LENGTH(option_value) AS size, autoload
FROM wp_options
WHERE option_name LIKE '\_transient\_%'
ORDER BY size DESC
LIMIT 20;
```

```sql
SELECT COUNT(*) AS transient_rows,
       SUM(LENGTH(option_value)) AS transient_bytes
FROM wp_options
WHERE option_name LIKE '\_transient\_%';
```

### Object cache monitoring

Persistent object cache is valuable only if hit rates are healthy and memory pressure is controlled. Monitor:

- hit rate;
- miss rate;
- evictions;
- memory usage;
- slow cache operations;
- cache flush frequency;
- hot keys;
- network/service errors.

### Redis vs Memcached, and Object Cache Pro

WordPress works with both Redis and Memcached as persistent object cache backends, but the choice has practical consequences:

- **Memcached** is a pure in-memory key/value store. Fast, simple, ephemeral. Eviction is LRU; there is no persistence and no advanced data structures. This is the historical default on VIP-style platforms.
- **Redis** offers richer data structures, optional persistence, pub/sub, atomic operations, and far better introspection. For WordPress workloads, Redis is usually a better fit — particularly when you want to track hot keys, set per-key TTLs, or use the cache for more than naive get/set.

For the integration layer, **Object Cache Pro** (commercial) is the most common production-grade Redis drop-in for WordPress, offering monitoring, async writes, group prefetching, and per-group serialization choices. Free alternatives include the Redis Object Cache plugin and host-provided drop-ins.

Whichever backend you choose, the drop-in lives at `wp-content/object-cache.php` and is loaded early in the WordPress boot.

---

## 14. Race conditions and cache stampedes

Cache stampedes happen when many requests miss the same expensive cache key and all regenerate it simultaneously.

### Object-cache form

```php
$cache_key = 'myplugin_expensive_data';
$lock_key  = 'myplugin_expensive_data_lock';

$data = wp_cache_get( $cache_key, 'myplugin' );

if ( false === $data ) {
    $lock_acquired = wp_cache_add( $lock_key, 1, 'locks', 30 );

    if ( $lock_acquired ) {
        $data = myplugin_generate_expensive_data();
        wp_cache_set( $cache_key, $data, 'myplugin', HOUR_IN_SECONDS );
        wp_cache_delete( $lock_key, 'locks' );
    } else {
        $data = myplugin_get_safe_fallback();
    }
}
```

### Transient form

When you specifically want the transient layer (and its database fallback on non-persistent environments), keep the lock in the object cache (it should be ephemeral) but store the result in a transient:

```php
$cache_key = 'myplugin_expensive_data';
$lock_key  = 'myplugin_expensive_data_lock';

$data = get_transient( $cache_key );

if ( false === $data ) {
    $lock_acquired = wp_cache_add( $lock_key, 1, 'locks', 30 );

    if ( $lock_acquired ) {
        $data = myplugin_generate_expensive_data();
        set_transient( $cache_key, $data, HOUR_IN_SECONDS );
        wp_cache_delete( $lock_key, 'locks' );
    } else {
        $data = myplugin_get_safe_fallback();
    }
}
```

The lock’s ephemerality (`wp_cache_add` with a TTL) is the safety property — even if the lock-holder crashes, the lock auto-expires.

### Additional tactics

- add TTL jitter so keys do not all expire at once;
- refresh hot keys before expiry (proactive regeneration);
- serve stale while regenerating where acceptable;
- batch object-cache requests with `wp_cache_get_multiple()`;
- avoid cache calls in tight loops when one multi-get would work.

---

## 15. REST API, AJAX, and follow-up requests

Cached HTML can still be followed by uncached dynamic requests.

Check for:

- `/wp-json/...` calls;
- `/wp-admin/admin-ajax.php` calls;
- WooCommerce cart fragments;
- personalization endpoints;
- search/autocomplete;
- analytics or marketing calls;
- polling.

### REST guidance

- Public GET endpoints returning identical data can be cache candidates.
- Authenticated endpoints usually bypass edge cache.
- Nonces and cookies introduce state.
- Expensive endpoint callbacks should cache internally.
- Avoid polling when event-driven updates are possible.

### AJAX guidance

- Avoid `POST` for cacheable reads.
- Prefer REST endpoints over `admin-ajax.php` for structured APIs.
- Cache public GET responses when safe.
- Move expensive work out of synchronous user requests.

---

## 16. WP-Cron, Action Scheduler, and background work

Request-triggered WP-Cron can create unpredictable user-facing latency.

### Production pattern

Disable request-triggered cron:

```php
define( 'DISABLE_WP_CRON', true );
```

Run due events externally. Pick the interval based on your shortest acceptable lag — one minute for jobs that need to be timely, five minutes for general housekeeping:

```bash
*/5 * * * * cd /path/to/site && wp cron event run --due-now --quiet
```

If WP-CLI is not available, hit the cron endpoint over HTTP. Either `curl` or `wget` works:

```bash
*/5 * * * * curl -s https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

```bash
*/5 * * * * wget -q --delete-after https://example.com/wp-cron.php?doing_wp_cron
```

The source courses disagree on the interval (VIP uses `* * * * *` / every minute, Remkus uses `*/5 * * * *` / every five minutes); the right answer depends on what is scheduled. If you have second-counts-late jobs, run every minute; otherwise five minutes is the calmer default.

### Review

- due and overdue events;
- slow recurring jobs;
- duplicate scheduled events;
- Action Scheduler backlog;
- failed jobs;
- jobs running during peak traffic;
- cache purge or regeneration jobs;
- remote API jobs.

### Action Scheduler monitoring

WooCommerce and many other plugins ship Action Scheduler for background work. On busy stores it accumulates millions of rows and becomes a perf liability of its own.

- Monitor queue length and failure rate as a primary signal.
- Watch for jobs that fail and immediately reschedule themselves (failure storms).
- Batch long-running work; one Action Scheduler job that processes 10,000 items is far worse than 100 jobs that process 100 items each.
- Add locking around expensive jobs to prevent overlap.
- Purge or archive completed actions on a schedule; the `wp_actionscheduler_actions` table is not self-maintaining at scale.

WP-CLI helpers:

```bash
wp action-scheduler run --batch-size=50
wp action-scheduler queue
```

---

## 17. `wp-config.php` as policy

Defaults are safe, not optimal. `wp-config.php` is where you encode site-level performance and operational policy. Remkus’s Module 15 frames this well: treat the wp-config as policy, not as a place to dump constants you copied from a forum.

```php
// Debug — production-safe.
define( 'WP_DEBUG', false );
define( 'WP_DEBUG_LOG', false );
define( 'SCRIPT_DEBUG', false );

// Editorial — limit revision sprawl and trash retention.
define( 'WP_POST_REVISIONS', 10 );          // or false to disable
define( 'AUTOSAVE_INTERVAL', 120 );          // seconds
define( 'EMPTY_TRASH_DAYS', 14 );

// Cron — run from system scheduler instead (see §16).
define( 'DISABLE_WP_CRON', true );

// File modifications — disable on platforms that deploy code via CI/CD.
define( 'DISALLOW_FILE_MODS', true );

// Cache — page-cache drop-in opt-in (see §4 for what this does NOT enable).
define( 'WP_CACHE', true );
```

### Heartbeat API

The Heartbeat API powers admin features like autosave and dashboard widgets but polls aggressively. On large editorial sites it can be a real source of admin-side load.

```php
// Slow Heartbeat on the frontend; keep it normal in the editor.
add_filter( 'heartbeat_settings', function( $settings ) {
    if ( ! is_admin() ) {
        $settings['interval'] = 60;
    }
    return $settings;
} );
```

### XML-RPC

Unused on most modern sites. Disable if you do not use Jetpack, the WordPress mobile app, or remote-publishing clients.

```php
add_filter( 'xmlrpc_enabled', '__return_false' );
```

### Emojis and embeds

Both inject scripts and styles on the frontend. Removable on sites that don’t need them; the savings are small but cumulative.

```php
remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
remove_action( 'wp_print_styles', 'print_emoji_styles' );
remove_action( 'wp_head', 'wp_oembed_add_discovery_links' );
```

Use these with judgment. Don’t paste configuration blindly — align it with editorial, hosting, and maintenance needs.

---

## 18. Partial-output / fragment caching

When full-page caching is impossible (logged-in views, mixed content, frequently changing components) but a specific expensive fragment is reused across many requests, cache the fragment. VIP’s operational checklist §7 calls this out explicitly; the pattern is `ob_start()` plus the object cache.

```php
<?php
$cache_key = 'recent_posts_sidebar_' . get_current_blog_id();

$recent_posts_html = wp_cache_get( $cache_key, 'page_fragments' );

if ( false === $recent_posts_html ) {
    ob_start();
    // Generate the expensive sidebar output here.
    get_template_part( 'partials/recent-posts-sidebar' );
    $recent_posts_html = ob_get_clean();

    wp_cache_set(
        $cache_key,
        $recent_posts_html,
        'page_fragments',
        HOUR_IN_SECONDS
    );
}

echo $recent_posts_html;
```

Guidance:

- Pick cache keys that include only the variables that actually change output (locale, current blog, A/B test bucket).
- Set an expiration that matches freshness requirements; invalidate on relevant `save_post` / data-change hooks if necessary.
- Never cache personalized fragments under a shared key. If the fragment varies per user, key on the user ID — or don’t cache it.
- Use cache groups (`'page_fragments'` above) to make targeted flushes possible.

---

## 19. Frontend and browser performance

A fast origin response does not guarantee a fast experience.

### Core Web Vitals thresholds

| Metric | Good | Needs improvement | Poor |
|---|---:|---:|---:|
| LCP — Largest Contentful Paint | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| INP — Interaction to Next Paint | ≤ 200 ms | 200–500 ms | > 500 ms |
| CLS — Cumulative Layout Shift | ≤ 0.1 | 0.1–0.25 | > 0.25 |

Thresholds are evaluated at the **75th percentile** across a site’s real users. INP replaced FID as a Core Web Vital on March 12, 2024.

### LCP checklist

- Identify the LCP element.
- Improve TTFB if HTML arrives late.
- Optimize the LCP image.
- Do not lazy-load the LCP image.
- Set dimensions.
- Reduce render-blocking CSS/JS.
- Preload only truly critical resources (see §8).

### INP checklist

- Reduce long JavaScript tasks (anything over 50 ms is suspect).
- Remove unnecessary third-party scripts.
- Defer or delay non-critical JavaScript.
- Avoid heavy page-builder runtime logic.
- Reduce DOM size and layout recalculation.
- Split work and avoid blocking the main thread.

### CLS checklist

- Set image/video dimensions.
- Reserve space for ads, embeds, banners, notices.
- Stabilize font loading.
- Avoid injecting content above existing content after render.

### Images

- Use correct sizes.
- Use `srcset` and `sizes`.
- Compress appropriately.
- Use WebP/AVIF where suitable; the Performance Lab plugin’s **WebP Uploads** module converts uploaded JPEG/PNG to WebP on the fly (see §22).
- Lazy-load below-fold images. (Core auto-adds `loading="lazy"` to most `<img>` tags.)
- Preload the true LCP image only when necessary.

### Fonts — FOIT vs FOUT

When a browser needs a font it doesn’t yet have, it picks one of two unhappy states:

- **FOIT — Flash Of Invisible Text:** text is hidden until the font arrives. Bad LCP, but no shift.
- **FOUT — Flash Of Unstyled Text:** fallback font renders, then swaps when the web font arrives. Good LCP, but causes layout shift (a CLS hit).

Control the choice with `font-display`:

- `font-display: swap` — fast first paint, accepts CLS. Usually the right call for body text.
- `font-display: optional` — fast first paint, only uses the web font if it arrives quickly. Best for sites where layout stability matters more than typography fidelity.
- `font-display: block` — short FOIT, then swap. Use only when the brand font is visually critical and you can self-host with minimal latency.

Other font guidance:

- Reduce families, weights, and variants ruthlessly. Each is a separate download.
- Self-host when it improves control and caching (`fonts.gstatic.com` adds a third-party DNS/TLS round-trip — see §7).
- Preload only critical above-fold fonts, with matching `type` and `crossorigin` (see §8).

### CSS and JavaScript

- Remove unused assets.
- Scope enqueues to pages that need them.
- Avoid duplicate libraries.
- Defer non-critical scripts (`defer`/`async`).
- Avoid broad minify/combine settings that break dependencies.
- Trace every asset back to the plugin/theme that enqueued it.

### Critical CSS

Inline a small block of CSS sufficient to render above-the-fold content, then load the rest asynchronously. This shortens LCP at the cost of some maintenance complexity.

- Generate critical CSS from the actual rendered viewport, not from a manual guess.
- Keep critical CSS under ~14 KB so it fits in the first TCP packet.
- Load non-critical CSS with `media="print"` swap or `<link rel="preload">` + `onload` swap.
- Re-generate when the design changes; stale critical CSS is worse than none.

### Delay-until-interaction for third-party scripts

For scripts that aren’t needed for first paint — chat widgets, analytics, A/B testing, marketing tags — defer execution until the first user interaction (scroll, click, key). This trades some attribution accuracy for substantial INP and CPU savings on first load. Most performance plugins offer this as a configurable strategy; Perfmatters, FlyingScripts, and WP Rocket all implement it.

---

## 20. Page builders, themes, and DOM bloat

Page builders are not automatically slow, but they often raise the performance cost floor.

Review:

- DOM node count;
- wrapper depth;
- inline CSS volume;
- global CSS/JS frameworks;
- runtime layout engines;
- animation libraries;
- duplicate widgets/extensions;
- builder assets loaded on pages that do not use them.

Strategic rule:

> A page builder is a performance budget decision, not a moral choice.

Use builders where editorial flexibility justifies the cost. Prefer lean templates or native blocks for high-traffic, performance-critical pages where flexibility is less important.

---

## 21. Search, sitemaps, and large content sets

### Search

WordPress database search does not scale well for large, complex search experiences.

Consider Elasticsearch/OpenSearch when:

- search traffic is high;
- filters/facets are complex;
- content volume is large;
- relevance ranking matters;
- SQL search creates load.

### Sitemaps

At scale:

- paginate sitemaps;
- cache generated output;
- avoid generating deep archives on every request;
- exclude unnecessary post types/taxonomies;
- pre-generate where appropriate.

---

## 22. Core-only: WordPress Performance Lab and Core innovations (current to WP 6.8)

This section covers WordPress Core and Performance Lab capabilities that **are not in the source courses** because they shipped after recording. They are the most important things to add to a 2026 WordPress performance stack.

### Performance Lab plugin

The Performance Lab plugin ([wordpress.org/plugins/performance-lab](https://wordpress.org/plugins/performance-lab/)) is the core team’s incubator for performance features. Features mature inside the plugin, then either get merged into Core or graduate to standalone plugins. Worth installing on staging to evaluate.

Current notable modules:

- **Image Placeholders (Dominant Color Images):** Computes a dominant color at upload time and uses it as a CSS background while the image loads. Reduces perceived layout shift and is invisible when working correctly.
- **WebP Uploads:** Stores a WebP version of uploaded JPEG/PNG and serves the WebP to supporting browsers. Substantial bandwidth and LCP wins on image-heavy sites.
- **Enhanced Responsive Images / Auto-sizes for Lazy-Loaded Images:** Sets `sizes="auto"` on lazy-loaded `<img>` elements so the browser can pick the right `srcset` candidate after layout.
- **SQLite Database Integration:** Experimental SQLite backend; primarily for low-traffic / single-user installs and demos.

### Speculation Rules / Speculative Loading (Core in WP 6.8)

WP 6.8 (April 2025) merged the Speculation Rules API into Core. This tells the browser to prefetch or prerender pages the user is likely to navigate to next.

- Default behavior is conservative: prerender on `mousedown` for same-site links.
- Configurable via Settings → Reading.
- The standalone Speculative Loading plugin ([wordpress.org/plugins/speculation-rules](https://wordpress.org/plugins/speculation-rules/)) offers more aggressive eagerness modes (prerender on `mouseover`, prefetch all links).
- Watch for over-prerender on metered connections and on pages with heavy analytics; prerendered pages fire analytics as if visited.

### WP 6.6+ Options API improvements

Already covered in §12: WP 6.6 added `wp_set_option_autoload()`, expanded the autoload vocabulary, and added the Site Health autoload check. WP 6.8 continued to tune the auto-skip heuristics.

### Auto-image-sizes and `fetchpriority`

WP 6.3+ adds `fetchpriority="high"` to the LCP image when it can identify one (typically the first large in-content image). For most sites this removes the need for manual LCP preload — verify in DevTools before adding a preload yourself.

---

## 23. WooCommerce and dynamic commerce flows

WooCommerce sites often mix cacheable marketing/catalog pages with uncacheable cart, checkout, and account flows.

Checklist:

- Cache anonymous catalog and marketing pages aggressively.
- Bypass cart, checkout, and account pages.
- Audit cart fragments and AJAX calls.
- Avoid unnecessary session creation for anonymous visitors.
- Optimize product archive queries and filters.
- Monitor Action Scheduler (see §16).
- Avoid expensive personalization on every page view.
- Test logged-in, logged-out, cart, checkout, coupon, and account flows after cache changes.

---

## 24. Multisite

Multisite is not inherently slow. It amplifies shared-resource pressure.

Review:

- network-activated plugins;
- per-site options and transients;
- network-wide (“site”) transients — `_site_transient_{name}` keys on the network options table — which behave like transients but with network scope and the same fallback semantics described in §13;
- object-cache memory and eviction behavior;
- database query volume;
- `switch_to_blog()` use (avoid in loops);
- domain mapping and redirects;
- site-specific vs network-wide bottlenecks.

Avoid heavy network-wide logic that every site inherits whether it needs it or not.

---

## 25. High-traffic events and load testing

High-traffic events require pre-work.

### Preflight

- Identify expected traffic source and timing.
- Identify landing pages.
- Confirm edge cache hit ratio.
- Warm caches.
- Remove query-string cache fragmentation.
- Freeze risky deploys.
- Move cron/heavy jobs away from peak windows.
- Monitor origin, database, object cache, CDN, error rates.
- Prepare rollback and escalation.

### Load testing

Only load test with approval.

```bash
k6 run --vus 100 --duration 5m script.js
```

Record:

- requests per second;
- p50/p95/p99 latency;
- error rate;
- cache hit ratio;
- origin CPU/memory;
- PHP workers;
- database load;
- object-cache hit rate;
- external dependency latency.

---

## 26. Measurement tools

### Browser/lab tools

- Lighthouse;
- PageSpeed Insights;
- WebPageTest;
- Chrome DevTools;
- performance profiles;
- network waterfalls.

### Field/user tools

- [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux);
- [`web-vitals` JavaScript library](https://github.com/GoogleChrome/web-vitals) for in-page RUM;
- Real User Monitoring providers (Scanfully, Sentry, New Relic Browser, etc.);
- analytics performance timing;
- Core Web Vitals reports.

### WordPress/backend tools

- Query Monitor (both source courses lean on this heavily);
- WP-CLI profile (`wp profile stage`, `wp profile hook`);
- WP-CLI doctor (`wp doctor check`);
- PHP logs;
- custom timers;
- New Relic/APM;
- host/platform metrics;
- CDN logs/analytics;
- object-cache stats.

### PHP timing example

```php
function my_custom_function() {
    $start_time = microtime( true );

    // Code to be measured here.

    $execution_time = microtime( true ) - $start_time;
    error_log( 'my_custom_function took ' . $execution_time . ' seconds' );
}
```

### Query Monitor custom timer

```php
do_action( 'qm/start', 'mytimer' );

foreach ( range( 1, 10 ) as $i ) {
    function_to_measure_time_spent( $i );
}

do_action( 'qm/stop', 'mytimer' );
```

### New Relic example

```php
function my_custom_function() {
    // Code to be measured.
}

newrelic_start_transaction( 'my_custom_transaction' );
my_custom_function();
newrelic_end_transaction();
```

---

## 27. Decision trees

These are TRACE in checklist form (see §3): follow the signal, narrow the pattern, change one thing, verify.

### High TTFB on anonymous public page

1. Should the page be full-page cached?
2. Is it a cache hit?
3. If miss/bypass, inspect cookies, headers, query strings, TTL, purge behavior.
4. If truly uncacheable, profile PHP, database, object cache, external calls.
5. Verify with repeated warm/cold measurements.

### High TTFB on logged-in/admin page

1. Full-page cache likely does not apply.
2. Profile hooks and callbacks.
3. Check query count and slow queries.
4. Check autoloaded options (§12 — use the 6.6-aware query).
5. Check object-cache hit rate.
6. Check external HTTP calls.
7. Check cron/background jobs.

### Poor LCP

1. Is TTFB high?
2. What is the LCP element?
3. Is the LCP image optimized and prioritized (`fetchpriority`)?
4. Is CSS/JS blocking render?
5. Are fonts delaying visible text (FOIT)?
6. Are third parties delaying the first view?

### Poor INP

1. Capture main-thread profile.
2. Identify long tasks (over 50 ms).
3. Attribute scripts to plugins/themes/third parties.
4. Remove, defer, delay-until-interaction (§19), or split work.
5. Reduce DOM/layout complexity.

### Poor cache hit ratio

1. Are URLs fragmented by query strings?
2. Are cookies forcing variation or bypass?
3. Are TTLs too short?
4. Are purges too broad/frequent?
5. Are personalized pages mixed with public pages?
6. Are REST/AJAX calls bypassing the intended cache strategy?

### Slow database

1. Identify the slow query.
2. Run `EXPLAIN`.
3. Check indexes and rows scanned.
4. Check for unbounded query patterns.
5. Check meta/taxonomy misuse.
6. Cache result if safe.
7. Consider search/offloaded storage if SQL is the wrong tool.

### Site fails under traffic but is fine when quiet

1. Which shared resource saturates first — PHP workers, database connections, object-cache memory, CDN egress?
2. Are cache misses concentrated on a small set of URLs?
3. Are background jobs running during the peak?
4. Is there a stampede pattern on a hot key?

---

## 28. Developer anti-pattern checklist

Avoid or review carefully:

- global plugin initialization doing expensive work;
- remote HTTP calls during render;
- `posts_per_page => -1`;
- broad meta queries;
- large `NOT IN` lists;
- leading-wildcard `LIKE`;
- high-cardinality transients without persistent object cache;
- large autoloaded options (and pre-6.6 review queries that miss the new vocabulary);
- object-cache keys with poor reuse;
- cache regeneration without locks;
- `admin-ajax.php` polling;
- frontend scripts enqueued globally;
- multiple plugins modifying the same CSS/JS/cache layer;
- page-builder templates on performance-critical landing pages without budget;
- full-site cache purges for small changes;
- treating Lighthouse score as the only goal;
- optimizing before measuring.

### Common transient misconceptions

These are myths worth flagging — they appear in the sibling transients reference and routinely catch developers:

- **“Transients are always memory cache.”** No — without persistent object caching, they’re database rows.
- **“`WP_CACHE` enables Redis or Memcached.”** No — `WP_CACHE` relates to `advanced-cache.php`. Persistent object caching is `object-cache.php`.
- **“A transient will always exist until its expiration time.”** No — expiration is a maximum lifetime, not a minimum. Cache eviction, flushes, and storage pressure can remove a transient early. Always have a regeneration path.
- **“Expired transients always disappear immediately.”** No — on database-backed sites, expired transient rows can sit in `wp_options` until accessed or until a cleanup runs.
- **“Transients are safe for unlimited per-user/per-request data.”** No — high-cardinality keys create either huge database growth or low cache hit rates, depending on backend.
- **“Deleting expired transients is performance optimization.”** Sometimes it helps hygiene, but it does not fix code that keeps creating excessive transient rows.

---

## 29. Definition of done

A performance fix is done when:

- the bottleneck was measured;
- the fix targets that bottleneck directly;
- before/after measurements use the same URL, user state, cache state, and environment;
- cache behavior is safe and intentional;
- no private content is cached publicly;
- critical user flows still work;
- error logs are clean;
- monitoring can detect regression;
- remaining risks are documented.

### Client/stakeholder reporting

A performance pass is not communicated by score deltas alone. Frame the work as:

- What was slow?
- What work was reduced, cached, or moved?
- What changed in measured results (at the same percentile, same user state)?
- What risks remain?
- What should be monitored next?

| Area | Before | After | Impact | Next action |
|---|---:|---:|---|---|
| Homepage TTFB | 900 ms | 180 ms | HTML cache now hitting | Watch cache hit ratio |
| Product LCP | 4.2 s | 2.5 s | Hero image resized/preloaded | Audit remaining images |
| Admin order screen | 6.8 s | 3.1 s | Slow query removed | Monitor during peak |

---

## 30. Source map and external references

### Local source folders

- Remkus guide: [`../remkus-make-wordpress-fast/`](../remkus-make-wordpress-fast/)
- WP VIP guide: [`../wpvip-enterprise-performance/`](../wpvip-enterprise-performance/)
- Transients reference: [`../wordpress-transients-object-cache/`](../wordpress-transients-object-cache/)

### WordPress.org developer documentation

- [Transients API](https://developer.wordpress.org/apis/transients/)
- [`get_transient()`](https://developer.wordpress.org/reference/functions/get_transient/)
- [`set_transient()`](https://developer.wordpress.org/reference/functions/set_transient/)
- [`WP_Object_Cache`](https://developer.wordpress.org/reference/classes/wp_object_cache/)
- [`wp_start_object_cache()`](https://developer.wordpress.org/reference/functions/wp_start_object_cache/)
- [`wp_set_option_autoload()`](https://developer.wordpress.org/reference/functions/wp_set_option_autoload/)
- [`wp_set_options_autoload()`](https://developer.wordpress.org/reference/functions/wp_set_options_autoload/)
- [`wp option set-autoload` (WP-CLI)](https://developer.wordpress.org/cli/commands/option/set-autoload/)
- [WP_Query class reference](https://developer.wordpress.org/reference/classes/wp_query/)
- [Advanced Administration Handbook — Cache](https://developer.wordpress.org/advanced-administration/performance/cache/)
- [Advanced Administration Handbook — Performance](https://developer.wordpress.org/advanced-administration/performance/)
- [Plugin Handbook — Hooking WP-Cron into the system task scheduler](https://developer.wordpress.org/plugins/cron/hooking-wp-cron-into-the-system-task-scheduler/)

### WordPress Core blog posts

- [Options API: Disabling autoload for large options (June 2024)](https://make.wordpress.org/core/2024/06/18/options-api-disabling-autoload-for-large-options/)
- [New option functions in 6.4 (October 2023)](https://make.wordpress.org/core/2023/10/17/new-option-functions-in-6-4/)
- [WordPress 6.6 Performance Improvements](https://make.wordpress.org/core/2024/07/29/wordpress-6-6-performance-improvements/)
- [Speculative Loading in 6.8 (March 2025)](https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/)
- [WordPress 6.8 Performance Improvements (April 2025)](https://make.wordpress.org/core/2025/04/16/wordpress-6-8-performance-improvements/)

### Performance Lab and standalone plugins

- [Performance Lab](https://wordpress.org/plugins/performance-lab/)
- [Speculative Loading](https://wordpress.org/plugins/speculation-rules/)
- [Image Placeholders / Dominant Color Images](https://wordpress.org/plugins/dominant-color-images/)

### Web platform / Core Web Vitals

- [web.dev — Learn Core Web Vitals](https://web.dev/explore/learn-core-web-vitals)
- [web.dev — Web Vitals overview](https://web.dev/articles/vitals)
- [web.dev — Interaction to Next Paint](https://web.dev/articles/inp)
- [web.dev — Defining Core Web Vitals thresholds](https://web.dev/articles/defining-core-web-vitals-thresholds)
- [`web-vitals` JavaScript library](https://github.com/GoogleChrome/web-vitals)
- [MDN — Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)
- [MDN — `font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)

### Advanced Admin Handbook PR

- [WordPress/Advanced-administration-handbook PR #485](https://github.com/WordPress/Advanced-administration-handbook/pull/485)


--- END DOCUMENT: DEVELOPER_REFERENCE.md ---


--- BEGIN DOCUMENT: wordpress-performance-optimization-checklist.md ---

# WordPress Performance Optimization Checklist

A practical, operations-oriented guide for improving WordPress performance without guessing. Work through this in order: measure first, reduce unnecessary work, cache safely, optimize delivery, then verify with the same measurements.

> Principle: performance is not a score. Optimize for the user experience: fast response, quick interactivity, stable layout, and predictable behavior across real devices and networks.


## Companion cross-reference: WP VIP Enterprise Performance

Use this checklist as the broad WordPress/operator workflow. When the target site is enterprise-scale, VIP-hosted, or dominated by backend/database/cache behavior, cross-check the companion WP VIP runbook at [`../wpvip-enterprise-performance/wpvip-enterprise-performance-operational-checklist.md`](../wpvip-enterprise-performance/wpvip-enterprise-performance-operational-checklist.md). It goes deeper on `WP_Query`, `NOT IN`, `LIKE`, post meta, taxonomies, `EXPLAIN`, Elasticsearch/offloaded search, object-cache race conditions, cache stampedes, load testing, New Relic/APM, and high-traffic events.

@dknauss
---

## 0. Safety and scope

Before changing anything, define the target and guardrails.

- [ ] Identify the environment: local, staging, production, multisite, WooCommerce, membership, LMS, or other dynamic site type.
- [ ] Identify the slow experience:
  - [ ] public page
  - [ ] logged-in page
  - [ ] WordPress admin screen
  - [ ] WooCommerce cart/checkout/account
  - [ ] REST API endpoint
  - [ ] `admin-ajax.php` request
  - [ ] WP-Cron or background job
- [ ] Pick 1–3 exact URLs or routes to test repeatedly.
- [ ] Decide what changes are allowed:
  - [ ] read-only diagnostics
  - [ ] configuration changes
  - [ ] plugin/theme changes
  - [ ] database cleanup
  - [ ] hosting/CDN changes
- [ ] Confirm rollback options:
  - [ ] database backup
  - [ ] file backup or git branch
  - [ ] ability to disable new rules/plugins
  - [ ] cache/CDN rule rollback

---

## 1. Baseline measurement

Capture current behavior before optimizing.

### User-facing metrics

- [ ] Measure Core Web Vitals for important templates:
  - [ ] LCP — Largest Contentful Paint
  - [ ] INP — Interaction to Next Paint
  - [ ] CLS — Cumulative Layout Shift
- [ ] Compare lab and field data:
  - [ ] Lighthouse/PageSpeed Insights for controlled testing
  - [ ] CrUX or real user monitoring for real-user data where available
- [ ] Record device/network assumptions: desktop, mobile, throttled mobile, logged-in, logged-out.

### Server/backend metrics

- [ ] Measure uncached and cached TTFB separately.
- [ ] Run the same request multiple times to separate cold-cache from warm-cache behavior.
- [ ] Check response headers:
  - [ ] cache status: `HIT`, `MISS`, `BYPASS`, `DYNAMIC`, etc.
  - [ ] `Cache-Control`
  - [ ] cookies
  - [ ] redirects
  - [ ] CDN headers
- [ ] If WP-CLI is available, collect profiling data:

```bash
wp profile stage --url="https://example.com/target-page/"
wp profile hook --url="https://example.com/target-page/"
wp doctor check
```

- [ ] If Query Monitor is available, inspect:
  - [ ] total query count
  - [ ] slow queries
  - [ ] duplicate queries
  - [ ] HTTP API calls
  - [ ] hooks/components responsible for time
  - [ ] object cache statistics

Record baseline values in a small table:

| Target | State | TTFB | LCP | INP | CLS | Cache status | Notes |
|---|---:|---:|---:|---:|---:|---|---|
| `/` | logged out, warm cache |  |  |  |  |  |  |
| `/shop/` | logged out, warm cache |  |  |  |  |  |  |
| `/wp-json/...` | logged in/out |  |  |  |  |  |  |

---

## 2. Request path and DNS

A page cannot be fast if connection setup is slow or unreliable.

- [ ] Use a reputable DNS provider with fast global resolution.
- [ ] Check DNS records for unnecessary indirection.
- [ ] Keep the DNS path simple:
  - [ ] avoid long CNAME chains
  - [ ] remove stale records
  - [ ] ensure apex/root and `www` behavior is intentional
- [ ] Set TTLs intentionally:
  - [ ] lower TTL before planned migrations
  - [ ] higher TTL for stable records
- [ ] Confirm IPv4/IPv6 behavior if both are configured.
- [ ] Use DNS prefetch only for origins the page will actually use.
- [ ] Use preconnect sparingly for critical third-party origins that are needed early.

Examples:

```html
<link rel="dns-prefetch" href="//fonts.gstatic.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Checklist:

- [ ] Remove preconnects for non-critical third parties.
- [ ] Do not preconnect to many domains; each connection has a cost.
- [ ] Confirm third-party origins are still needed before optimizing around them.

---

## 3. TLS, HTTP, and redirects

Transport setup affects TTFB and resource delivery.

- [ ] Enforce HTTPS consistently.
- [ ] Remove redirect chains:
  - [ ] `http://` → `https://`
  - [ ] apex → `www` or `www` → apex
  - [ ] trailing slash canonicalization
- [ ] Confirm the final canonical URL is reached in one redirect or fewer.
- [ ] Ensure HTTP/2 or HTTP/3 support is enabled where appropriate.
- [ ] Keep certificates valid and automatically renewed.
- [ ] Use HSTS only when HTTPS is fully correct across subdomains.
- [ ] Check that CDN and origin TLS settings are compatible.

Useful checks:

```bash
curl -I -L https://example.com/
curl -w "namelookup:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} starttransfer:%{time_starttransfer} total:%{time_total}\n" -o /dev/null -s https://example.com/
```

---

## 4. Hosting and server layer

Good hosting reduces the amount of work WordPress has to fight through.

- [ ] Confirm adequate PHP workers for traffic and dynamic pages.
- [ ] Use a supported PHP version and modern database version.
- [ ] Enable PHP OPcache.
- [ ] Verify memory limits are sufficient but not hiding runaway code.
- [ ] Check error logs for repeated warnings, fatals, retries, or timeouts.
- [ ] Confirm server-level page cache or CDN cache integration.
- [ ] Check whether object cache is available and persistent.
- [ ] Confirm backups, security scans, and maintenance tasks are not running during peak traffic.

OPcache checks to discuss with hosting/ops:

- [ ] OPcache enabled for web requests.
- [ ] OPcache memory not exhausted.
- [ ] OPcache revalidation settings appropriate for the deployment workflow.

---

## 5. Full-page caching / HTML caching

Full-page caching is powerful because it can skip WordPress execution entirely for cacheable requests.

- [ ] Identify which pages can be cached as full HTML:
  - [ ] homepage
  - [ ] posts/pages
  - [ ] category/tag archives
  - [ ] product listing pages when not personalized
  - [ ] landing pages
- [ ] Identify which pages should bypass full-page cache:
  - [ ] `/wp-admin/`
  - [ ] cart
  - [ ] checkout
  - [ ] account pages
  - [ ] pages with user-specific private content
  - [ ] preview URLs
- [ ] Confirm cache headers are intentional.
- [ ] Confirm logged-out pages get `HIT` after warming.
- [ ] Confirm logged-in or personalized pages do not leak private HTML.
- [ ] Warm important pages after deploys or cache purges.
- [ ] Avoid global cache purges unless necessary.

### Query-string cache fragmentation

Ignore or normalize marketing query strings when they do not change page content.

Examples that commonly fragment cache keys:

```text
/shop?utm_source=newsletter&utm_medium=email&utm_campaign=spring_sale
/shop?fbclid=IwAR1XyZExampleValue
/shop?gclid=EAIaIQobChMIExample
/shop?utm_source=facebook&utm_content=carousel_ad_3
/shop?lang=en
/shop?preview=true
/shop?utm_source=newsletter&utm_medium=email&fbclid=IwAR1XyZExampleValue
```

Checklist:

- [ ] Ignore `utm_*` parameters for HTML cache when content does not vary.
- [ ] Ignore ad click IDs such as `fbclid` and `gclid` when safe.
- [ ] Never cache preview URLs as public canonical HTML.
- [ ] Treat language, currency, region, and personalization parameters carefully; they may change content.

### Cookie cache fragmentation

- [ ] List cookies set on public pages.
- [ ] Remove cookies that are not required before interaction.
- [ ] Configure cache bypass only for cookies that truly indicate personalization/session state.
- [ ] Audit plugins that set cookies globally.
- [ ] Avoid letting analytics or marketing cookies bypass HTML cache.

---

## 6. CDN and edge delivery

A CDN helps when it caches the right assets and avoids unnecessary trips to origin.

- [ ] Put static assets behind the CDN:
  - [ ] images
  - [ ] CSS
  - [ ] JavaScript
  - [ ] fonts
- [ ] Confirm immutable/static assets have long cache lifetimes.
- [ ] Use file versioning or hashed filenames for assets that change.
- [ ] Configure HTML cache rules intentionally; do not rely on defaults blindly.
- [ ] Track cache hit ratio.
- [ ] Investigate low hit ratio:
  - [ ] too many query strings
  - [ ] unnecessary cookies
  - [ ] short TTLs
  - [ ] frequent purges
  - [ ] personalized HTML
  - [ ] inconsistent cache keys
- [ ] Confirm origin shielding or tiered caching if traffic is global/high-volume.
- [ ] Verify CDN does not break admin, checkout, REST, or logged-in flows.

---

## 7. WordPress runtime

Optimize what WordPress loads and executes for each request.

- [ ] Profile request stages: bootstrap, main query, template, hooks.
- [ ] Identify slow hooks/callbacks.
- [ ] Remove unnecessary plugins or modules.
- [ ] Disable plugin features not used on the site.
- [ ] Prevent frontend loading of admin-only functionality.
- [ ] Avoid running expensive logic on every request.
- [ ] Move heavy work to background jobs where appropriate.
- [ ] Cache expensive computed results.
- [ ] Avoid remote HTTP calls during page generation unless cached and timeout-protected.

WP-CLI profiling examples:

```bash
wp profile stage --url="https://example.com/sample-page/"
wp profile hook --url="https://example.com/sample-page/" --all
```

Code review checklist:

- [ ] Are hooks scoped to the pages where they are needed?
- [ ] Are queries run inside loops?
- [ ] Are external APIs called during render?
- [ ] Are transients/object cache used for expensive repeat work?
- [ ] Are cache keys specific enough but not over-fragmented?
- [ ] Are large options autoloaded unnecessarily?

---

## 8. Database and query performance

Database optimization is about reducing expensive work, not just “cleaning tables.”

- [ ] Check total query count per request.
- [ ] Find slow queries.
- [ ] Find duplicate queries.
- [ ] Identify N+1 patterns.
- [ ] Review `WP_Query`, meta queries, taxonomy queries, and search queries.
- [ ] Avoid broad unbounded queries.
- [ ] Paginate large result sets.
- [ ] Cache expensive query results when safe.
- [ ] Avoid using post meta as a high-volume relational query system.
- [ ] Add indexes only after confirming query patterns and testing impact.

Autoloaded options:

- [ ] Measure total autoloaded option size.
- [ ] Identify the largest autoloaded options.
- [ ] Set large rarely-used options to `autoload = no` where safe.
- [ ] Remove orphaned plugin/theme options only after backup and verification.

Useful SQL inspection examples (updated for WordPress 6.6+):

> **Note:** As of WordPress 6.6 (June 2024), the `autoload` column can hold five values: `'on'`, `'off'`, `'auto'`, `'auto-on'`, `'auto-off'`. Older rows still use `'yes'`/`'no'`. Filters that only look for `'yes'` miss everything written under the new vocabulary. The queries below cover both. See the **Modern additions** appendix at the end of this checklist for the full 6.6 / 6.8 update list.

```sql
SELECT option_name, LENGTH(option_value) AS size, autoload
FROM wp_options
WHERE autoload IN ('yes', 'on', 'auto', 'auto-on')
ORDER BY size DESC
LIMIT 20;
```

```sql
SELECT SUM(LENGTH(option_value)) AS autoload_bytes
FROM wp_options
WHERE autoload IN ('yes', 'on', 'auto', 'auto-on');
```

To change autoload state, use the WP 6.4+ API rather than hand-editing the column:

```php
wp_set_option_autoload( 'my_huge_option', false );
wp_set_options_autoload( array( 'opt_a', 'opt_b' ), false );
```

Or via WP-CLI:

```bash
wp option set-autoload my_huge_option no
```

---

## 9. Object caching and transients

Object caching reduces repeated database work. Persistent object caching keeps those benefits across requests.

- [ ] Check whether a persistent object cache drop-in exists: `wp-content/object-cache.php`.
- [ ] Confirm Redis or Memcached is healthy if used.
- [ ] Monitor object cache hit/miss ratio.
- [ ] Cache expensive computations and query results.
- [ ] Avoid caching highly personalized data with broad keys.
- [ ] Use stable, explicit cache keys.
- [ ] Set appropriate expirations.
- [ ] Avoid storing huge objects if they cause memory pressure.

Transients checklist:

- [ ] Use transients for expensive results that can expire.
- [ ] Do not autoload large transient-like data unnecessarily.
- [ ] Clean up expired transient buildup if the database is accumulating it.
- [ ] Remember that transients may live in the database or object cache depending on the environment.

Example pattern:

```php
$cache_key = 'myplugin_expensive_result_' . md5( $context_id );
$result = get_transient( $cache_key );

if ( false === $result ) {
    $result = myplugin_build_expensive_result( $context_id );
    set_transient( $cache_key, $result, HOUR_IN_SECONDS );
}
```

---

## 10. REST API, admin-ajax, cookies, and headers

Background requests can reintroduce server load after the initial page is cached.

- [ ] Inspect frontend network requests after page load.
- [ ] Identify calls to:
  - [ ] `/wp-json/...`
  - [ ] `/wp-admin/admin-ajax.php`
  - [ ] cart fragments
  - [ ] analytics/marketing scripts
  - [ ] personalization endpoints
- [ ] Remove polling that is not required.
- [ ] Increase polling intervals where possible.
- [ ] Cache REST responses when safe.
- [ ] Use nonces and authentication correctly for private endpoints.
- [ ] Avoid using `admin-ajax.php` for public high-traffic frontend features when REST endpoints or static rendering would be better.
- [ ] Review headers that prevent caching:
  - [ ] `Cache-Control: no-store`
  - [ ] `Set-Cookie`
  - [ ] `Vary: Cookie`

---

## 11. Images

Images are often the largest contributor to LCP and page weight.

- [ ] Identify the LCP image on each key template.
- [ ] Ensure LCP image is not lazy-loaded.
- [ ] Serve correctly sized images using `srcset` and `sizes`.
- [ ] Compress images appropriately.
- [ ] Use modern formats where supported: WebP or AVIF.
- [ ] Set explicit width/height to avoid layout shift.
- [ ] Lazy-load below-the-fold images.
- [ ] Avoid huge background images for critical hero content unless intentionally optimized.
- [ ] Preload only the true critical LCP image when needed.

Example:

```html
<link rel="preload" as="image" href="/path/to/hero.webp" imagesrcset="/hero-800.webp 800w, /hero-1600.webp 1600w" imagesizes="100vw">
```

Checklist for WordPress themes:

- [ ] Use WordPress image functions where possible so responsive attributes are generated.
- [ ] Avoid hardcoded full-size images.
- [ ] Confirm featured image sizes match actual display requirements.
- [ ] Audit sliders/carousels; they often load multiple large images before interaction.

---

## 12. CSS, JavaScript, and rendering

Frontend optimization is about reducing render-blocking work and unnecessary main-thread execution.

CSS:

- [ ] Remove unused CSS where practical.
- [ ] Avoid loading site-wide CSS for components used on one page.
- [ ] Inline only small critical CSS when it improves LCP and does not create maintenance risk.
- [ ] Avoid excessive CSS frameworks or duplicate design systems.

JavaScript:

- [ ] Remove unused scripts.
- [ ] Defer non-critical scripts.
- [ ] Delay third-party scripts until interaction when appropriate.
- [ ] Avoid long main-thread tasks.
- [ ] Split heavy functionality by page/template.
- [ ] Prevent duplicate libraries from loading.

WordPress asset checklist:

- [ ] Confirm plugins enqueue assets only where needed.
- [ ] Dequeue unnecessary assets carefully and test affected pages.
- [ ] Avoid breaking dependencies by blindly combining/minifying everything.
- [ ] Check for duplicate jQuery, slider, icon, analytics, or builder assets.

---

## 13. Fonts and third parties

Fonts and third-party scripts often block rendering or delay interactivity.

Fonts:

- [ ] Use fewer font families, weights, and styles.
- [ ] Prefer system fonts where acceptable.
- [ ] Self-host fonts when it simplifies delivery and caching.
- [ ] Use `font-display: swap` or another intentional strategy.
- [ ] Preload only critical fonts actually used above the fold.
- [ ] Ensure preloaded fonts use matching `type` and `crossorigin` attributes.

Example:

```html
<link rel="preload" href="/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
```

Third-party scripts:

- [ ] Inventory analytics, ads, chat, maps, embeds, A/B testing, and social widgets.
- [ ] Remove tools that are no longer used.
- [ ] Load third parties after consent or interaction where appropriate.
- [ ] Avoid third-party scripts on templates that do not need them.
- [ ] Measure INP impact after enabling/disabling each major third party.

---

## 14. Plugins, themes, and page builders

Plugin count alone is not the metric; plugin behavior is.

- [ ] Inventory plugins by function and business value.
- [ ] Identify overlapping plugins.
- [ ] Identify plugins that load assets globally.
- [ ] Identify plugins that run expensive queries or remote calls.
- [ ] Replace heavy plugins with lighter alternatives when the feature is simple.
- [ ] Disable unused modules inside large plugins.
- [ ] Test performance before and after each plugin change.

Page builders and visual editors:

- [ ] Check DOM size.
- [ ] Check nested wrapper depth.
- [ ] Check duplicate CSS/JS libraries.
- [ ] Avoid builder widgets for simple static content when native blocks or theme templates are enough.
- [ ] Rebuild high-traffic landing pages with leaner markup where ROI is clear.

Plugin reduction plan:

1. [ ] List every plugin and its purpose.
2. [ ] Mark must-have, replaceable, unused, and unknown.
3. [ ] Disable one candidate on staging.
4. [ ] Test functionality.
5. [ ] Measure performance delta.
6. [ ] Remove only after confirming no regressions.

---

## 15. WordPress core configuration

Default WordPress behavior is safe and flexible, but not always optimal for every production site.

- [ ] Disable or limit post revisions only if editorial requirements allow it.
- [ ] Configure autosaves and heartbeat carefully; do not break editing workflows.
- [ ] Disable XML-RPC if not needed.
- [ ] Move WP-Cron to real server cron on production/high-traffic sites.
- [ ] Confirm debug settings are production-safe.
- [ ] Keep core, plugins, and themes updated after testing.

Production `wp-config.php` review:

```php
define( 'WP_DEBUG', false );
define( 'SCRIPT_DEBUG', false );
define( 'WP_POST_REVISIONS', 10 );
define( 'DISABLE_WP_CRON', true );
```

Use with judgment. Do not paste configuration blindly; align it with editorial, hosting, and maintenance needs.

---

## 16. Cron and background jobs

Scheduled work should not surprise frontend visitors.

- [ ] Identify due and overdue cron events.
- [ ] Move WP-Cron to server cron where appropriate.
- [ ] Avoid heavy cron tasks during peak traffic.
- [ ] Deduplicate scheduled events.
- [ ] Check failed Action Scheduler jobs.
- [ ] For WooCommerce, monitor Action Scheduler queue length and failure rate.
- [ ] Batch long-running jobs.
- [ ] Add locking to prevent overlapping expensive jobs.

Server cron example:

```bash
*/5 * * * * cd /path/to/site && wp cron event run --due-now --quiet
```

Or via HTTP if WP-CLI is unavailable:

```bash
*/5 * * * * curl -s https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

---

## 17. WooCommerce and dynamic sites

WooCommerce, membership, LMS, and community sites need careful cache boundaries.

- [ ] Cache catalog and marketing pages aggressively when logged out.
- [ ] Bypass cart, checkout, account, and personalized pages.
- [ ] Check cart fragments or AJAX cart behavior.
- [ ] Reduce unnecessary session creation for anonymous visitors.
- [ ] Optimize product queries and filters.
- [ ] Monitor Action Scheduler.
- [ ] Avoid expensive stock, pricing, or personalization calculations on every page view.
- [ ] Test with real logged-in and logged-out flows after cache changes.

WooCommerce-specific checks:

- [ ] product archive TTFB
- [ ] single product LCP image
- [ ] cart fragments
- [ ] checkout AJAX calls
- [ ] Action Scheduler backlog
- [ ] slow order/admin screens

---

## 18. Multisite

Multisite performance problems often come from network-wide assumptions.

- [ ] Identify whether slowness is site-specific or network-wide.
- [ ] Audit network-activated plugins.
- [ ] Check global tables and large options.
- [ ] Avoid expensive network-wide queries during normal requests.
- [ ] Review object cache groups and cache segmentation.
- [ ] Confirm domain mapping and redirects are clean.
- [ ] Measure representative subsites separately.

---

## 19. Monitoring and reporting

Optimization is incomplete without ongoing monitoring.

- [ ] Monitor uptime and response time.
- [ ] Monitor Core Web Vitals over time.
- [ ] Monitor PHP errors and fatals.
- [ ] Monitor database slow queries where supported.
- [ ] Monitor object cache health.
- [ ] Monitor cron/action queues.
- [ ] Monitor CDN cache hit ratio.
- [ ] Keep a change log of performance-related changes.

Client/stakeholder reporting should explain experience, not just scores:

- [ ] What was slow?
- [ ] What work was reduced or moved?
- [ ] What changed in measured results?
- [ ] What risks remain?
- [ ] What should be monitored next?

Example report table:

| Area | Before | After | Impact | Next action |
|---|---:|---:|---|---|
| Homepage TTFB | 900ms | 180ms | HTML cache now hitting | Watch cache hit ratio |
| Product LCP | 4.2s | 2.5s | Hero image resized/preloaded | Audit remaining images |
| Admin order screen | 6.8s | 3.1s | Slow query removed | Monitor during peak |

---

## 20. Verification checklist

After each change, retest the same target under the same conditions.

- [ ] Re-run baseline measurements.
- [ ] Compare before/after TTFB.
- [ ] Compare before/after Core Web Vitals.
- [ ] Confirm cache status changed as expected.
- [ ] Confirm no private content is cached publicly.
- [ ] Confirm logged-in workflows still work.
- [ ] Confirm checkout/account/admin flows still work.
- [ ] Check PHP error logs.
- [ ] Check browser console for asset errors.
- [ ] Check visual layout stability.
- [ ] Document the change and result.

If there is no improvement:

- [ ] Confirm you tested the same URL.
- [ ] Confirm caches were warmed or cleared intentionally.
- [ ] Confirm the change reached production/staging.
- [ ] Confirm the bottleneck you fixed was actually dominant.
- [ ] Re-profile instead of stacking more optimizations.

---

## 21. Recommended optimization order

Use this order to avoid premature or risky changes.

1. [ ] Measure and profile.
2. [ ] Fix redirects, DNS, TLS, and obvious transport issues.
3. [ ] Make full-page cache work for safe public pages.
4. [ ] Remove cache fragmentation from query strings and cookies.
5. [ ] Optimize hosting/runtime bottlenecks.
6. [ ] Fix database, autoload, object cache, and remote HTTP issues.
7. [ ] Optimize images, fonts, CSS, and JavaScript.
8. [ ] Reduce plugin/theme/page-builder overhead.
9. [ ] Move cron/background work out of user requests.
10. [ ] Add monitoring and reporting.

---

## 22. Quick triage decision tree

### High TTFB on logged-out pages

- [ ] Is full-page cache enabled and hitting?
- [ ] Are cookies or query strings bypassing cache?
- [ ] Is the CDN reaching origin unnecessarily?
- [ ] Is WordPress executing for cacheable HTML?

### High TTFB on logged-in/admin pages

- [ ] Profile hooks and queries.
- [ ] Check object cache.
- [ ] Check autoloaded options.
- [ ] Check remote HTTP calls.
- [ ] Check plugin-specific admin overhead.

### Poor LCP

- [ ] Identify the LCP element.
- [ ] Optimize/preload the LCP image if appropriate.
- [ ] Remove render-blocking CSS/JS.
- [ ] Improve TTFB if the document arrives late.

### Poor INP

- [ ] Identify long JavaScript tasks.
- [ ] Reduce third-party scripts.
- [ ] Remove unnecessary frontend plugin assets.
- [ ] Delay non-critical scripts.

### Poor CLS

- [ ] Add image/video dimensions.
- [ ] Reserve space for ads/embeds/notices.
- [ ] Avoid late-injected banners above content.
- [ ] Stabilize font loading.

---

## 23. Definition of done

A performance optimization pass is done when:

- [ ] Key URLs have documented before/after measurements.
- [ ] Improvements are tied to specific causes, not vague plugin changes.
- [ ] Cache behavior is intentional and safe.
- [ ] No critical user flows regressed.
- [ ] Monitoring is in place for the optimized areas.
- [ ] Remaining risks and next steps are documented.

---

## Appendix A: Modern additions (current to WordPress 6.8, May 2026)

The Make WordPress Fast course was recorded before several material WordPress Core performance changes shipped. This appendix covers the most important ones an operator should fold into the checklist above. The unified developer reference at [`../wordpress-performance-master-reference/DEVELOPER_REFERENCE.md`](../wordpress-performance-master-reference/DEVELOPER_REFERENCE.md) covers each topic in more depth.

### Options API: new autoload functions (WordPress 6.4)

WordPress 6.4 introduced first-class functions for managing the autoload state of options. Hand-editing the `autoload` column was always risky; these functions invalidate the right caches and respect the API:

```php
wp_set_option_autoload( 'my_huge_option', false );        // singular
wp_set_options_autoload( array( 'opt_a', 'opt_b' ), false ); // bulk
```

Operator workflow:

- [ ] When you find a fat option in §8, flip it via `wp_set_option_autoload()` (or `wp option set-autoload` in WP-CLI), not via raw SQL.
- [ ] Confirm the change with the autoload-size query in §8 — total `autoload_bytes` should drop.

### Autoload vocabulary expansion (WordPress 6.6)

As of WordPress 6.6 the `autoload` column holds one of five values: `'on'`, `'off'`, `'auto'`, `'auto-on'`, `'auto-off'`. Old `'yes'`/`'no'` rows persist on upgraded sites and are treated as `'on'`/`'off'`. WordPress 6.6 also added automatic skip-autoload for options larger than ~150 KB by default.

Operator workflow:

- [ ] Replace any `WHERE autoload = 'yes'` filters in saved queries, dashboards, or monitoring with `WHERE autoload IN ('yes', 'on', 'auto', 'auto-on')`.
- [ ] Check Site Health → Performance for the “Autoloaded options could affect performance” warning. It triggers at ~800 KB total autoload size.
- [ ] On sites you suspect have stale options, prefer the API/CLI fix over raw deletes; orphaned-option cleanup is a separate maintenance task and should still be done with backups.

### Speculation Rules / Speculative Loading (WordPress 6.8)

WordPress 6.8 (April 2025) merged the [Speculation Rules API](https://wordpress.org/plugins/speculation-rules/) into Core. The browser is told to prefetch or prerender same-site links the user is likely to visit next. Default behavior is conservative (prerender on `mousedown`, same-origin only).

Operator workflow:

- [ ] Verify the feature is active under Settings → Reading on managed installs that upgraded to 6.8+.
- [ ] On sites with heavy analytics or ads, audit whether prerendered visits are double-counting or firing third-party scripts on hidden pages.
- [ ] For more aggressive eagerness (prerender on hover, prefetch on hover, etc.), install the standalone [Speculative Loading plugin](https://wordpress.org/plugins/speculation-rules/) and tune it per template.

### Performance Lab plugin

The [Performance Lab plugin](https://wordpress.org/plugins/performance-lab/) is the Core team’s feature incubator. Modules ship inside it, then either graduate to Core or to standalone plugins. Worth evaluating on staging:

- **WebP Uploads** — stores WebP alongside JPEG/PNG and serves WebP to supporting browsers. Significant LCP and bandwidth wins on image-heavy sites.
- **Image Placeholders (Dominant Color Images)** — computes a dominant color at upload time and uses it as a background while the image loads; reduces perceived layout shift.
- **Enhanced Responsive Images / Auto-sizes for Lazy-Loaded Images** — sets `sizes="auto"` on lazy-loaded `<img>` so the browser picks the right `srcset` candidate after layout.

Operator workflow:

- [ ] Install Performance Lab on staging; enable WebP Uploads and Image Placeholders.
- [ ] Reupload a representative set of hero/feature images to compare delivered sizes and LCP.
- [ ] Promote to production only after verifying no theme/page-builder breakage with the new image strategy.

### LCP and `fetchpriority` (WordPress 6.3+)

WordPress 6.3 added automatic `fetchpriority="high"` on the LCP image when Core can identify one. Verify in DevTools before adding manual `<link rel="preload">` for the hero image — Core may already have done it for you.

### Core Web Vitals thresholds (post-INP, March 2024)

For reference when reading any current performance report:

| Metric | Good | Needs improvement | Poor |
|---|---:|---:|---:|
| LCP | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| INP | ≤ 200 ms | 200–500 ms | > 500 ms |
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |

INP replaced FID as a Core Web Vital on March 12, 2024. Any report still talking about FID is operating on a 2023 definition.

### References

- [Options API: Disabling autoload for large options (Make WP Core, June 2024)](https://make.wordpress.org/core/2024/06/18/options-api-disabling-autoload-for-large-options/)
- [New option functions in 6.4 (Make WP Core)](https://make.wordpress.org/core/2023/10/17/new-option-functions-in-6-4/)
- [WordPress 6.6 Performance Improvements](https://make.wordpress.org/core/2024/07/29/wordpress-6-6-performance-improvements/)
- [Speculative Loading in 6.8 (Make WP Core)](https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/)
- [WordPress 6.8 Performance Improvements](https://make.wordpress.org/core/2025/04/16/wordpress-6-8-performance-improvements/)
- [`wp_set_option_autoload()`](https://developer.wordpress.org/reference/functions/wp_set_option_autoload/)
- [Performance Lab plugin](https://wordpress.org/plugins/performance-lab/)
- [web.dev — Interaction to Next Paint](https://web.dev/articles/inp)


--- END DOCUMENT: wordpress-performance-optimization-checklist.md ---


--- BEGIN DOCUMENT: wpvip-enterprise-performance-operational-checklist.md ---

# Enterprise WordPress Performance Operational Checklist

A checklist-oriented runbook based on the WP VIP Learn **Enterprise WordPress Performance** course. Use it to diagnose, optimize, and verify performance on high-traffic WordPress sites where backend execution, cacheability, database access, object caching, traffic events, and measurement discipline matter.

> Operating rule: do not start by installing another performance plugin. Start by identifying where time is spent, whether WordPress is executing at all, and whether the response can safely be cached.


## Companion cross-reference: Remkus De Vries' "Make WordPress Fast" 

Use this runbook as the enterprise/backend/platform workflow. When a performance symptom is user-facing or frontend-heavy, cross-check the checklist based on Remkus' guidance at [`../remkus-make-wordpress-fast/wordpress-performance-optimization-checklist.md`](../remkus-make-wordpress-fast/wordpress-performance-optimization-checklist.md). It goes deeper on Core Web Vitals, LCP/INP/CLS, images, fonts, third-party scripts, CSS/JavaScript loading, page builders, DOM bloat, WooCommerce, Multisite, plugin stack simplification, DevTools, and performance reporting.

@dknauss
---

## 0. Define the performance problem

- [ ] Identify the affected surface:
  - [ ] public anonymous page
  - [ ] logged-in page
  - [ ] editorial/admin workflow
  - [ ] API endpoint
  - [ ] AJAX endpoint
  - [ ] search results
  - [ ] sitemap generation
  - [ ] redirect path
  - [ ] high-traffic event page
- [ ] Identify the failure mode:
  - [ ] high TTFB
  - [ ] slow PHP execution
  - [ ] slow MySQL queries
  - [ ] too many database queries
  - [ ] cache misses
  - [ ] object-cache pressure
  - [ ] cache stampede/race condition
  - [ ] slow third-party/external request
  - [ ] client-side JavaScript delay
  - [ ] load-test failure
- [ ] Confirm the test target URL or route.
- [ ] Record whether the request is anonymous or authenticated.
- [ ] Record whether the page should be cacheable.
- [ ] Confirm rollback path before changing production behavior.

---

## 1. Trace the request cycle

For each target request, walk the full path.

- [ ] User enters URL.
- [ ] DNS resolves the hostname.
- [ ] Browser sends HTTP request.
- [ ] Edge/CDN checks for cached response.
- [ ] Origin web server receives request if edge misses or bypasses.
- [ ] WordPress core loads.
- [ ] MU plugins load.
- [ ] Plugins and theme code run.
- [ ] Database and object cache are queried.
- [ ] Template is selected and rendered.
- [ ] HTTP response is sent to browser.
- [ ] Browser parses HTML, downloads assets, executes JavaScript, renders the page.
- [ ] Additional requests fire: AJAX, REST, media, tracking, personalization.

Decision point:

- [ ] If the edge cache returns a valid `HIT`, focus on payload, browser rendering, and post-load requests.
- [ ] If the request reaches origin, focus on cacheability, PHP, database, object cache, hooks, templates, and external calls.

---

## 2. Establish a baseline

Run the same measurements before and after every change.

- [ ] Measure uncached TTFB.
- [ ] Measure warm-cache TTFB.
- [ ] Capture cache headers.
- [ ] Capture response status and redirects.
- [ ] Capture PHP/application timing.
- [ ] Capture database query count and slow queries.
- [ ] Capture object-cache behavior when available.
- [ ] Capture frontend impact if browser rendering is part of the symptom.

Useful command:

```bash
curl -s -o /dev/null -D headers.txt \
  -w "dns:%{time_namelookup} connect:%{time_connect} tls:%{time_appconnect} ttfb:%{time_starttransfer} total:%{time_total}\n" \
  https://example.com/target/
```

Baseline table:

| Target | User state | Expected cacheability | Cache status | TTFB | PHP time | DB time | Notes |
|---|---|---|---|---:|---:|---:|---|
| `/` | anonymous | cacheable |  |  |  |  |  |
| `/search/?s=x` | anonymous | maybe dynamic |  |  |  |  |  |
| `/wp-json/...` | varies | endpoint-specific |  |  |  |  |  |

---

## 3. DNS and HTTP request setup

- [ ] Confirm DNS resolves quickly and predictably.
- [ ] Avoid unnecessary DNS indirection and stale records.
- [ ] Confirm final canonical URL does not require multiple redirects.
- [ ] Confirm HTTPS works without certificate or protocol negotiation issues.
- [ ] Confirm HTTP/2 or HTTP/3 support where appropriate.
- [ ] Check request headers that may vary cache behavior:
  - [ ] cookies
  - [ ] authorization
  - [ ] query strings
  - [ ] user-agent variation
  - [ ] language/country headers

Redirect check:

```bash
curl -IL https://example.com/some-url/
```

- [ ] If multiple redirects occur, identify the source: WordPress, plugin, CDN, web server, localization, or application code.
- [ ] Look for `x-redirect-by` when WordPress generates redirects.

Examples seen in the course:

```text
x-redirect-by: WordPress
x-redirect-by: Polylang Pro
```

Debug filter example:

```php
add_filter( 'x_redirect_by', function( $x_redirect_by, $status, $location ) {
    wp_die( var_dump( array(
        $x_redirect_by,
        $status,
        $location,
        wp_debug_backtrace_summary(),
    ) ) );
}, 10, 3 );
```

Use that only in safe debugging contexts, not as a production-facing change.

---

## 4. Full-page cache and edge cache

Full-page caching is the first major enterprise performance boundary: if the edge can serve HTML, WordPress and MySQL may not need to run.

- [ ] Identify pages that should be edge-cacheable.
- [ ] Identify pages that must bypass cache:
  - [ ] logged-in personalized views
  - [ ] carts
  - [ ] checkout
  - [ ] account pages
  - [ ] previews
  - [ ] nonce-sensitive forms
  - [ ] private API responses
- [ ] Check cache status response headers.
- [ ] Confirm `Cache-Control` behavior is intentional.
- [ ] Confirm cookies are not causing broad cache bypasses.
- [ ] Confirm query parameters are not fragmenting the cache key unnecessarily.
- [ ] Confirm TTL is appropriate for content volatility.
- [ ] Confirm invalidation/purge logic is precise enough.
- [ ] Investigate cache misses before tuning PHP.

Edge-cache triage:

- [ ] Is the response cacheable?
- [ ] Does it include `Set-Cookie`?
- [ ] Does it vary by cookie or authorization?
- [ ] Is the TTL too short?
- [ ] Is a plugin sending no-cache headers?
- [ ] Is the request URL unique because of query strings?
- [ ] Are purges too broad or too frequent?

---

## 5. TTL, headers, and invalidation

- [ ] Set long TTLs for stable public content.
- [ ] Set shorter TTLs for content that changes frequently.
- [ ] Use purge/invalidation for freshness rather than universally short TTLs.
- [ ] Avoid sending no-cache/no-store on pages that should be public-cacheable.
- [ ] Verify generated headers from WordPress, plugins, CDN, and server rules.
- [ ] Ensure invalidation happens when content changes.
- [ ] Avoid purging the whole site for small content updates when targeted purges are possible.

Header review:

```bash
curl -I https://example.com/page/
```

Look for:

- [ ] `Cache-Control`
- [ ] `Expires`
- [ ] `Vary`
- [ ] `Set-Cookie`
- [ ] CDN cache status headers
- [ ] custom platform cache headers

---

## 6. Application optimization

If a request reaches WordPress, optimize the application path.

- [ ] Identify expensive hooks, filters, and actions.
- [ ] Confirm callbacks run only where needed.
- [ ] Avoid global work during every request.
- [ ] Avoid excessive template complexity.
- [ ] Avoid template over-use where many partials perform redundant work.
- [ ] Cache expensive partial output when safe.
- [ ] Eliminate uncached functions on hot paths.
- [ ] Avoid remote HTTP calls during page rendering.
- [ ] Move non-critical work to async/background processing.

Hook review checklist:

- [ ] Does this callback run on frontend, admin, REST, AJAX, or all contexts?
- [ ] Does it execute database queries?
- [ ] Does it call external services?
- [ ] Does it build data that could be cached?
- [ ] Does it run for users/pages that do not need it?

---

## 7. Partial output caching

Use partial output caching for expensive fragments that cannot be solved by full-page cache alone.

- [ ] Identify repeated expensive fragments: sidebars, related posts, navigation, widgets, API-derived blocks.
- [ ] Create cache keys that include only the context that changes output.
- [ ] Set an expiration appropriate to freshness needs.
- [ ] Invalidate when source data changes where necessary.
- [ ] Avoid caching personalized fragments under shared keys.

Example pattern:

```php
<?php
$cache_key = 'recent_posts_sidebar_' . get_current_blog_id();

$recent_posts_html = wp_cache_get( $cache_key, 'page_fragments' );

if ( false === $recent_posts_html ) {
    ob_start();
    // Generate the expensive sidebar output here.
    get_template_part( 'partials/recent-posts-sidebar' );
    $recent_posts_html = ob_get_clean();

    wp_cache_set( $cache_key, $recent_posts_html, 'page_fragments', HOUR_IN_SECONDS );
}

echo $recent_posts_html;
```

---

## 8. MySQL query optimization

Slow database work is one of the most common origin-side bottlenecks.

- [ ] Count total queries for the request.
- [ ] Identify slow queries.
- [ ] Identify duplicate queries.
- [ ] Identify unbounded queries.
- [ ] Identify queries that scan too many rows.
- [ ] Avoid expensive meta queries on high-cardinality data.
- [ ] Avoid taxonomy over-use for query patterns that do not scale.
- [ ] Avoid `NOT IN` when it forces inefficient exclusion scans.
- [ ] Avoid leading-wildcard `LIKE` searches on large tables.
- [ ] Use search infrastructure such as Elasticsearch/OpenSearch for heavy search workloads.
- [ ] Use `EXPLAIN` to understand execution plans.

WP_Query baseline example:

```php
$query = new WP_Query(
    array(
        'post_type'      => 'post',
        'posts_per_page' => 5,
        'orderby'        => 'date',
        'order'          => 'DESC',
    )
);
```

Query anti-pattern checks:

- [ ] `posts_per_page => -1` on large datasets.
- [ ] missing pagination.
- [ ] meta queries used as primary filters at scale.
- [ ] taxonomy queries stacked into complex intersections/exclusions.
- [ ] `post__not_in` or SQL `NOT IN` against large sets.
- [ ] `LIKE '%term%'` on large text columns.
- [ ] ordering by unindexed or computed values.

---

## 9. Unbounded queries

Unbounded queries are dangerous because they look safe during development and fail at enterprise scale.

- [ ] Search code for `posts_per_page => -1`.
- [ ] Search code for `numberposts => -1`.
- [ ] Search code for falsy IDs accidentally becoming broad queries.
- [ ] Add explicit limits.
- [ ] Paginate large result sets.
- [ ] Use caching for expensive repeated query results.
- [ ] Validate IDs and input before building queries.

Examples:

```php
$post_id = intval( $my_unexpectedly_falsy_post_id );
$query_args = array(
    'p'              => $post_id,
    'posts_per_page' => -1,
);
```

```php
$args = array(
    'post_type' => 'post',
    'date_query' => array(
        'after'  => '2021-01-01',
        'before' => '2021-12-31',
    ),
);

$query = new WP_Query( $args );
```

Safer pattern:

```php
function limit_news_scope_query_filter( $query ) {
    if ( is_admin() || ! $query->is_main_query() ) {
        return;
    }

    if ( $query->is_category( 6 ) ) {
        $query->set( 'posts_per_page', 20 );
    }
}
add_action( 'pre_get_posts', 'limit_news_scope_query_filter' );
```

---

## 10. Taxonomies, exclusions, post meta, and LIKE

### Taxonomies

- [ ] Use taxonomies for classification, not arbitrary high-cardinality data.
- [ ] Avoid overly complex taxonomy intersections/exclusions.
- [ ] Keep term relationships manageable.
- [ ] Use dedicated indexes/search systems for large faceted search use cases.

Example scope limiter:

```php
function limit_news_scope_query_filter( $query ) {
    if ( is_admin() || ! $query->is_main_query() ) {
        return;
    }

    if ( $query->is_category() ) {
        $query->set( 'posts_per_page', 20 );
    }
}
add_action( 'pre_get_posts', 'limit_news_scope_query_filter' );
```

### NOT IN

- [ ] Avoid large `NOT IN` exclusions.
- [ ] Prefer positive selection rules where possible.
- [ ] Cache exclusion sets if they must be computed.
- [ ] Test with production-scale data.

Example to scrutinize:

```sql
SELECT * FROM wp_posts
WHERE post_type = 'post'
  AND post_status = 'publish'
  AND ID NOT IN (1, 2, 3);
```

### Post meta

- [ ] Do not treat post meta as a general-purpose relational store at scale.
- [ ] Avoid sorting/filtering large result sets by arbitrary meta values.
- [ ] Consider custom tables or search infrastructure for high-volume structured data.

### LIKE

- [ ] Avoid leading wildcard searches on large columns.
- [ ] Prefer indexed prefix searches if acceptable.
- [ ] Use search infrastructure for real search workloads.

Examples:

```sql
SELECT * FROM wp_posts WHERE post_title LIKE '%WordPress%';
```

```sql
SELECT * FROM wp_posts WHERE post_title LIKE 'WordPress%';
```

The second pattern can be more index-friendly than the first, but still needs production-scale testing.

---

## 11. EXPLAIN-driven query review

Use `EXPLAIN` to verify how MySQL plans to execute a query.

- [ ] Run `EXPLAIN` on slow queries.
- [ ] Check which table is scanned.
- [ ] Check access type.
- [ ] Check possible keys.
- [ ] Check the key actually used.
- [ ] Check estimated rows scanned.
- [ ] Look for filesort or temporary table usage.
- [ ] Compare plans before and after query/index changes.

Examples:

```sql
EXPLAIN SELECT * FROM wp_posts WHERE post_date > '2023-01-01';
```

```sql
EXPLAIN
SELECT wp_posts.*, wp_postmeta.meta_value
FROM wp_posts
JOIN wp_postmeta ON wp_posts.ID = wp_postmeta.post_id
WHERE wp_posts.post_date > '2023-01-01';
```

---

## 12. Object caching

Object caching reduces repeated computation and repeated database access.

- [ ] Confirm a persistent object cache exists when the site needs one.
- [ ] Confirm cache service health.
- [ ] Track hit rate and miss rate.
- [ ] Cache expensive query results and computed values.
- [ ] Use cache groups intentionally.
- [ ] Keep keys stable and specific.
- [ ] Avoid excessive cache calls in tight loops.
- [ ] Avoid storing huge objects that increase memory pressure.
- [ ] Avoid caching personalized/private data with shared keys.

---

## 13. Transients and in-memory caching

Transients:

- [ ] Use transients for data that can expire.
- [ ] Set realistic expiration times.
- [ ] Account for either database-backed or object-cache-backed storage.
- [ ] Avoid relying on transients for data that must always exist.
- [ ] Clean up transient buildup when needed.

In-memory request-level caching:

- [ ] Use static variables for repeat computations within one request.
- [ ] Do not use request-local cache as a substitute for persistent cache across requests.

Example:

```php
function getExpensiveComputationResult( $input ) {
    static $cache = array();

    if ( isset( $cache[ $input ] ) ) {
        return $cache[ $input ];
    }

    $result = perform_expensive_computation( $input );
    $cache[ $input ] = $result;

    return $result;
}
```

---

## 14. Race conditions and cache stampedes

Race conditions occur when multiple requests try to rebuild the same cache item at once. Cache stampedes happen when many requests miss simultaneously and all perform the expensive work.

- [ ] Add locking around expensive cache regeneration.
- [ ] Use soft TTL/hard TTL patterns where appropriate.
- [ ] Refresh important cache entries before they expire during high traffic.
- [ ] Avoid synchronized expiration for many hot keys.
- [ ] Add jitter to expirations where useful.
- [ ] Serve stale data briefly when freshness requirements allow it.

Lock example:

```php
$lock_key = 'my_cache_lock';
$lock_acquired = wp_cache_add( $lock_key, true, 'locks', 30 );

if ( $lock_acquired ) {
    $data = regenerate_expensive_cache_value();
    wp_cache_set( 'my_cache_key', $data, 'my_group', HOUR_IN_SECONDS );
    wp_cache_delete( $lock_key, 'locks' );
} else {
    $data = wp_cache_get( 'my_cache_key', 'my_group' );
}
```

---

## 15. WP-Cron and scheduled work

WP-Cron can create request-time spikes if scheduled work runs during user traffic.

- [ ] Identify due cron events.
- [ ] Identify slow recurring jobs.
- [ ] Disable request-triggered WP-Cron where appropriate.
- [ ] Run cron through real server cron.
- [ ] Avoid heavy jobs during peak traffic.
- [ ] Batch large jobs.
- [ ] Ensure jobs are idempotent.
- [ ] Monitor failures and backlog.

Configuration:

```php
define('DISABLE_WP_CRON', true);
```

WP-CLI cron runner:

```bash
* * * * * wp cron event run --due-now > /dev/null 2>&1
```

Fallback PHP runner:

```bash
* * * * * php /path/to/wordpress/wp-cron.php > /dev/null 2>&1
```

HTTP fallback:

```bash
* * * * * curl -s https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

---

## 16. AJAX, REST, sitemaps, redirects, and external requests

### AJAX and REST

- [ ] Identify `admin-ajax.php` calls on public pages.
- [ ] Identify REST API calls after initial render.
- [ ] Remove unnecessary polling.
- [ ] Cache public endpoint responses where safe.
- [ ] Move heavy endpoint work out of synchronous user requests.
- [ ] Authenticate private endpoints correctly.

### Sitemaps

- [ ] Ensure sitemap generation does not perform expensive unbounded queries.
- [ ] Cache sitemap output when possible.
- [ ] Paginate large sitemaps.
- [ ] Avoid regenerating large sitemap structures on every request.

### External requests

- [ ] Identify remote HTTP calls during page generation.
- [ ] Add strict timeouts.
- [ ] Cache remote responses.
- [ ] Fail gracefully when the remote service is slow.
- [ ] Move non-critical requests to background processing.

---

## 17. Client-side JavaScript and browser rendering

Even when backend performance is good, the browser can still feel slow.

- [ ] Identify heavy frontend scripts.
- [ ] Remove duplicate libraries.
- [ ] Avoid loading plugin scripts globally when only one page needs them.
- [ ] Defer non-critical JavaScript.
- [ ] Reduce long main-thread tasks.
- [ ] Measure interaction delay after script changes.
- [ ] Watch for AJAX calls triggered by frontend scripts after load.

---

## 18. Traffic patterns and high-traffic events

High-traffic events require preparation, not just reaction.

- [ ] Identify expected traffic sources and timing.
- [ ] Estimate peak requests per minute/second.
- [ ] Identify pages that will receive traffic.
- [ ] Pre-warm caches.
- [ ] Freeze risky deployments before the event.
- [ ] Audit cacheability of campaign landing pages.
- [ ] Remove avoidable query-string cache fragmentation.
- [ ] Confirm origin can survive expected cache misses.
- [ ] Confirm monitoring and alerting are active.
- [ ] Prepare rollback and incident contacts.

High-traffic preflight:

- [ ] CDN/edge cache hit ratio acceptable.
- [ ] Origin TTFB acceptable under warm cache.
- [ ] No heavy uncached widgets on landing page.
- [ ] No slow external dependency in critical path.
- [ ] No scheduled jobs during peak window.
- [ ] Load test completed in a safe environment.

---

## 19. Load testing

Load testing should be coordinated and scoped; never surprise production.

- [ ] Get explicit approval.
- [ ] Define target URLs and traffic model.
- [ ] Define acceptable limits and stop conditions.
- [ ] Test cacheable and uncached paths separately.
- [ ] Monitor origin, database, object cache, and CDN during the test.
- [ ] Compare behavior to expected real traffic.

Example:

```bash
k6 run --vus 100 --duration 5m script.js
```

Record:

- [ ] requests per second
- [ ] p50/p95/p99 latency
- [ ] error rate
- [ ] cache hit ratio
- [ ] PHP/application time
- [ ] database pressure
- [ ] object-cache pressure

---

## 20. Measuring time spent

Use multiple tools because each sees a different layer.

### PHP logging

- [ ] Use targeted timing around suspected code paths.
- [ ] Remove noisy debug logging after investigation.
- [ ] Do not expose timing details publicly.

Example:

```php
function my_custom_function() {
    $start_time = microtime( true );

    // Code to be measured here.

    $end_time = microtime( true );
    $execution_time = $end_time - $start_time;

    error_log( 'my_custom_function took ' . $execution_time . ' seconds' );
}
```

### New Relic

- [ ] Use APM traces to find slow transactions.
- [ ] Group by transaction type: page, admin, REST, AJAX, cron.
- [ ] Inspect database, external service, and PHP segment timing.

Example:

```php
function my_custom_function() {
    // Code to be measured.
}

newrelic_start_transaction( 'my_custom_transaction' );
my_custom_function();
newrelic_end_transaction();
```

### Query Monitor

- [ ] Inspect query count and slow queries.
- [ ] Inspect hooks and component timing.
- [ ] Inspect HTTP API calls.
- [ ] Use custom timers for targeted sections.

Example:

```php
do_action( 'qm/start', 'mytimer' );

foreach ( range( 1, 10 ) as $i ) {
    function_to_measure_time_spent( $i );
}

do_action( 'qm/stop', 'mytimer' );
```

---

## 21. Performance alerting

- [ ] Alert on high TTFB.
- [ ] Alert on elevated error rate.
- [ ] Alert on database saturation or slow queries.
- [ ] Alert on object-cache service failures.
- [ ] Alert on CDN cache hit ratio drops.
- [ ] Alert on queue/cron backlogs.
- [ ] Alert on external dependency latency.
- [ ] Alert on sudden traffic spikes.

Good alerts should include:

- [ ] affected URL or transaction
- [ ] severity
- [ ] current value vs threshold
- [ ] duration
- [ ] likely owner
- [ ] first diagnostic link
- [ ] rollback/escalation instructions

---

## 22. Verification and definition of done

After each optimization:

- [ ] Re-run the same measurement from the baseline.
- [ ] Confirm the same user state and URL were tested.
- [ ] Confirm cache status is expected.
- [ ] Confirm no private data is cached publicly.
- [ ] Confirm no critical functionality regressed.
- [ ] Confirm no new PHP errors.
- [ ] Confirm query count/time improved if database was targeted.
- [ ] Confirm cache hit ratio improved if caching was targeted.
- [ ] Document before/after values.
- [ ] Document remaining bottlenecks.

Done means:

- [ ] The bottleneck has been identified, not guessed.
- [ ] The fix addresses that bottleneck directly.
- [ ] The improvement is measurable.
- [ ] The change is safe under expected traffic.
- [ ] Monitoring can detect regression.

---

## Appendix A: Modern additions (current to WordPress 6.8, May 2026)

The WP VIP Learn Enterprise WordPress Performance course was recorded before several WordPress Core performance changes that matter at platform scale. This appendix covers them in enterprise terms. The unified developer reference at [`../wordpress-performance-master-reference/DEVELOPER_REFERENCE.md`](../wordpress-performance-master-reference/DEVELOPER_REFERENCE.md) has fuller treatment.

### Options API expansion (WordPress 6.4 and 6.6)

WordPress 6.4 added `wp_set_option_autoload()` and `wp_set_options_autoload()` for managing autoload state without touching the database directly. WordPress 6.6 expanded the `autoload` column to five values: `'on'`, `'off'`, `'auto'`, `'auto-on'`, `'auto-off'`. Legacy `'yes'`/`'no'` rows persist on upgraded sites.

Enterprise / platform implications:

- [ ] Any saved monitoring queries, dashboards, or platform health checks filtering `autoload = 'yes'` need to switch to `autoload IN ('yes', 'on', 'auto', 'auto-on')`. This is a silent miss otherwise — newly written 6.6+ options stop showing up.
- [ ] WP 6.6 automatically marks options larger than ~150 KB as `'auto-off'`. Custom platform code that writes large options with explicit autoload should respect this signal rather than fight it.
- [ ] Site Health adds a check labeled “Autoloaded options could affect performance” at ~800 KB total autoload size. Surface this in platform telemetry alongside `alloptions` size.
- [ ] On `alloptions` cache stampedes (the classic VIP issue), the WP 6.6 auto-skip heuristics reduce — but do not eliminate — the risk. Continue to set explicit `autoload => false` for known-large platform options.

```php
// Platform code: prefer explicit autoload over relying on heuristics.
add_option( 'my_platform_large_option', $value, '', false );

// To flip an existing option:
wp_set_option_autoload( 'my_platform_large_option', false );
```

### Speculation Rules / Speculative Loading (WordPress 6.8)

Core 6.8 (April 2025) ships the [Speculation Rules API](https://wordpress.org/plugins/speculation-rules/) with conservative defaults: prerender on `mousedown`, same-origin links only. The standalone Speculative Loading plugin offers more aggressive eagerness.

Enterprise / platform implications:

- [ ] Prerendered visits execute JavaScript on hidden documents. Audit analytics SDKs for prerender-aware behavior; otherwise expect inflated pageviews and impressions on hidden prerenders.
- [ ] Edge cache hit ratio will rise on sites with predictable navigation patterns — prefetch hits cache. Plan for cache footprint changes if your platform caps per-domain cache memory.
- [ ] Personalized or session-keyed pages must remain excluded from speculative prefetch via `data-prefetch="false"` or speculation-rule predicates. Confirm any platform-level scripting that injects per-user state does not accidentally pollute prerendered documents.
- [ ] Background work fired by prerender (e.g., heartbeat, cart fragments) can amplify origin load. Confirm WP-Cron, REST personalization, and Action Scheduler are insulated.

### `fetchpriority` on LCP image (WordPress 6.3+)

Core now sets `fetchpriority="high"` on the detected LCP image automatically. At enterprise scale this affects how the platform should advise on hero-image preload patterns:

- [ ] Audit any platform-level theme/plugin that emits `<link rel="preload" as="image">` for hero images — it may now be redundant or, worse, may compete with Core’s `fetchpriority` heuristic by preloading a different candidate.
- [ ] Confirm AMP / Block Theme combinations correctly identify the LCP candidate after 6.3.

### Performance Lab plugin

[Performance Lab](https://wordpress.org/plugins/performance-lab/) is the Core team’s feature incubator. At enterprise scale the relevant modules are:

- **WebP Uploads** — additional storage and CDN footprint to consider; LCP/bandwidth payoff is usually worth it for image-heavy publishers. Coordinate with media-pipeline owners on storage costs and CDN cache key strategy.
- **Enhanced Responsive Images** — improves lazy-loaded image sizing decisions; minimal platform impact, big perceived-perf payoff.
- **Optimization Detective** — opt-in module that collects RUM-style data on real users to identify LCP elements per URL. Useful for platforms that want to drive automatic `fetchpriority` decisions per-template.

### Core Web Vitals: INP replaced FID (March 2024)

INP is now the responsiveness metric of record, replacing FID. Thresholds at the 75th percentile across real users:

| Metric | Good | Needs improvement | Poor |
|---|---:|---:|---:|
| LCP | ≤ 2.5 s | 2.5–4.0 s | > 4.0 s |
| INP | ≤ 200 ms | 200–500 ms | > 500 ms |
| CLS | ≤ 0.1 | 0.1–0.25 | > 0.25 |

Enterprise platform reporting should retire FID dashboards and ensure RUM SDKs report INP. INP is more sensitive to JavaScript main-thread work than FID was, so customer-success conversations about “suddenly worse mobile” often trace to long-running scripts that FID would not have penalized.

### Editorial correction to source lesson

WP VIP Learn lesson 34 (WP Cron) shows the cron URL as `http://yourdomain.com/wp-cron.php?doing_wp_cron`. That is insecure for any modern production site — credentials, cookies, and the WP-Cron token would travel in cleartext. Use `https://` matching the site’s canonical scheme. (This operational checklist at §15 already uses HTTPS.)

### References

- [Options API: Disabling autoload for large options (Make WP Core)](https://make.wordpress.org/core/2024/06/18/options-api-disabling-autoload-for-large-options/)
- [New option functions in 6.4 (Make WP Core)](https://make.wordpress.org/core/2023/10/17/new-option-functions-in-6-4/)
- [WordPress 6.6 Performance Improvements](https://make.wordpress.org/core/2024/07/29/wordpress-6-6-performance-improvements/)
- [Speculative Loading in 6.8](https://make.wordpress.org/core/2025/03/06/speculative-loading-in-6-8/)
- [WordPress 6.8 Performance Improvements](https://make.wordpress.org/core/2025/04/16/wordpress-6-8-performance-improvements/)
- [`wp_set_option_autoload()`](https://developer.wordpress.org/reference/functions/wp_set_option_autoload/)
- [Performance Lab plugin](https://wordpress.org/plugins/performance-lab/)
- [web.dev — Interaction to Next Paint](https://web.dev/articles/inp)
- [Introducing INP to Core Web Vitals (Google Search Central)](https://developers.google.com/search/blog/2023/05/introducing-inp)


--- END DOCUMENT: wpvip-enterprise-performance-operational-checklist.md ---


--- BEGIN DOCUMENT: REFERENCE-WP-Transients-Persistent-Object-Cache.md ---

# WordPress Transients and Persistent Object Cache Reference

A practical reference for understanding how the WordPress Transients API behaves with and without a persistent object cache, and how that affects performance, database growth, and enterprise-scale WordPress operations.

## Executive summary

WordPress transients are a temporary caching API. They are often described as “cached data with an expiration time,” but the important operational detail is that **their storage backend is environment-dependent**.

- With a persistent object cache drop-in such as Redis or Memcached, transient values can be stored in the external object cache.
- Without persistent object caching, WordPress stores transient values in the database, typically in the `wp_options` table.
- Therefore, transients should not be assumed to be memory-backed on all WordPress sites.
- Heavy transient usage on a site without persistent object caching can increase database reads/writes and contribute to options table growth.
- Transients are appropriate for expensive data that is safe to regenerate, but they are not a replacement for durable storage.

### For further reference

This document synthesizes Remkus de Vries’ **Make WordPress Fast** lessons for the Within WordPress Guild, WP VIP Learn’s **Enterprise WordPress Performance** course, WordPress.org developer documentation, and my (pending) cache clarification work in [WordPress/Advanced-administration-handbook#485](https://github.com/WordPress/Advanced-administration-handbook/pull/485). Use those sources for deeper context on the specific layers discussed here.

@dknauss
---

## 1. What transients are

The Transients API provides a standardized way to store temporary data with an expiration time. Common use cases include caching:

- expensive query results
- rendered markup fragments
- third-party API responses
- computed data that can be regenerated
- short-lived results shared across requests

Basic example:

```php
$cache_key = 'myplugin_expensive_result_' . md5( $context_id );
$result    = get_transient( $cache_key );

if ( false === $result ) {
    $result = myplugin_build_expensive_result( $context_id );
    set_transient( $cache_key, $result, HOUR_IN_SECONDS );
}
```

Important detail: `get_transient()` returns `false` when the transient is missing or expired. If the cached value itself may be falsey, such as `0`, an empty string, or `false`, code must distinguish a cache miss from a valid falsey value.

---

## 2. Where transients are stored

### Default WordPress behavior

On a default WordPress installation without a persistent object cache, transients are stored in the database, usually in the `wp_options` table.

For expiring transients, WordPress commonly stores two option rows:

```text
_transient_{name}
_transient_timeout_{name}
```

For network-wide transients on Multisite, analogous site transient keys are used.

These option rows are not autoloaded when the transient has an expiration, so they grow the options table but not the autoload footprint loaded on every request. Transients set without an expiration are autoloaded — one more reason to always set an explicit expiration.

### With persistent object caching

When a persistent object cache drop-in such as Redis or Memcached is active, WordPress can store transients in the object cache instead of the database. This makes transients behave much more like an in-memory cache across requests.

This is why transients can be thought of as a **cache abstraction with a database fallback**, not as guaranteed memory storage.

---

## 3. Relationship to the WordPress Object Cache

WordPress has a built-in object cache API exposed through functions such as:

```php
wp_cache_get();
wp_cache_set();
wp_cache_add();
wp_cache_delete();
wp_cache_get_multiple();
wp_cache_set_multiple();
```

By default, WordPress’ object cache is **non-persistent**. It stores data in memory only for the duration of the current request. Data does not persist across page loads unless a persistent object cache drop-in is installed.

A persistent object cache normally uses:

```text
wp-content/object-cache.php
```

Examples include Redis and Memcached integrations.

The Transients API interacts with this system:

- if persistent object caching is active, transients can use the persistent object cache;
- if persistent object caching is not active, transients fall back to database-backed storage.

This means the same `set_transient()` call can have very different performance characteristics on two different environments.

---

## 4. Relationship to `WP_CACHE`, `advanced-cache.php`, and `object-cache.php`

A common source of confusion is the `WP_CACHE` constant.

```php
define( 'WP_CACHE', true );
```

`WP_CACHE` does **not** enable Redis, Memcached, or persistent object caching by itself. Its main role is to allow WordPress to load the page-cache-style drop-in:

```text
wp-content/advanced-cache.php
```

Persistent object caching is separate and uses:

```text
wp-content/object-cache.php
```

These are different cache layers:

| Cache layer | Typical implementation | Purpose |
|---|---|---|
| Page cache | `advanced-cache.php`, server cache, CDN/edge cache | Serve complete rendered pages/HTML |
| Object cache | `object-cache.php`, Redis, Memcached | Cache database/query/application objects |
| Transients | Transients API, object cache or `wp_options` fallback | Temporary data with expiration |
| Opcode cache | PHP OPcache | Cache compiled PHP bytecode |
| Browser/CDN cache | HTTP headers, CDN rules | Cache assets/responses outside WordPress |

Key point from the Advanced Admin Handbook PR: **transients are not always stored in memory; without persistent object caching, they are stored in the database.**

---

## 5. Expiration semantics

Transient expiration is a maximum lifetime, not a guaranteed minimum lifetime.

A transient may disappear before its expiration time because of:

- object cache eviction
- cache flushes
- database upgrades
- manual deletion
- storage pressure
- plugin or host behavior

But WordPress should not return the transient value after its expiration time.

Therefore, code must always be able to regenerate the transient value:

```php
$data = get_transient( 'myplugin_remote_data' );

if ( false === $data ) {
    $response = wp_remote_get( 'https://api.example.com/data', array(
        'timeout' => 3,
    ) );

    if ( is_wp_error( $response ) ) {
        return array();
    }

    $data = json_decode( wp_remote_retrieve_body( $response ), true );

    set_transient( 'myplugin_remote_data', $data, 15 * MINUTE_IN_SECONDS );
}
```

---

## 6. Performance implications without persistent object caching

When no persistent object cache is present, transients use the database. This is useful because it gives WordPress a built-in fallback, but it has limits.

Potential problems include:

- growth of the `wp_options` table
- additional database writes when transients are set or refreshed
- additional database reads when transients are fetched
- buildup of expired transient rows
- slow options-table operations on large sites
- poor scalability for high-cardinality transient keys

This is especially important on sites that create many unique transients, such as transients keyed by:

- user ID
- session ID
- request URL
- arbitrary query strings
- search terms
- personalization context
- API parameters with many possible combinations

Avoid patterns like this unless you understand the cardinality and storage backend:

```php
set_transient(
    'myplugin_result_' . md5( $_SERVER['REQUEST_URI'] ),
    $data,
    HOUR_IN_SECONDS
);
```

On a high-traffic site without persistent object caching, this can create many database rows and a low reuse rate.

---

## 7. Performance implications with persistent object caching

With Redis, Memcached, or another persistent object cache, transients can avoid repeated database storage and retrieval. This makes them more suitable for frequently reused expensive data.

Benefits include:

- fewer repeated database queries
- faster access to cached values
- better reuse across requests
- less pressure on `wp_options`
- improved scalability under concurrency

However, persistent object caching introduces its own operational concerns:

- cache hit rate matters more than cache presence
- cache keys must be well designed
- memory limits and evictions must be monitored
- cache stampedes and race conditions must be avoided
- some object cache groups may be non-persistent
- flushing the cache can cause sudden backend load

Persistent object cache is not “set and forget.” It should be monitored.

---

## 8. Race conditions and cache stampedes

If many requests miss the same transient at once, they may all attempt to regenerate the expensive value. This is a cache stampede.

Use a lock when regenerating expensive values:

```php
$cache_key = 'myplugin_expensive_data';
$lock_key  = 'myplugin_expensive_data_lock';

$data = get_transient( $cache_key );

if ( false === $data ) {
    $lock_acquired = wp_cache_add( $lock_key, 1, 'locks', 30 );

    if ( $lock_acquired ) {
        $data = myplugin_generate_expensive_data();
        set_transient( $cache_key, $data, HOUR_IN_SECONDS );
        wp_cache_delete( $lock_key, 'locks' );
    } else {
        // Another request is regenerating the value.
        // Optionally return stale data, a fallback, or a lightweight default.
        $data = array();
    }
}
```

This pattern is most useful when the regeneration path is expensive and traffic is concurrent.

---

## 9. Autoload and options-table concerns

Modern WordPress transient behavior varies depending on whether an expiration is set and whether an external object cache is active. Operationally, the safest guidance is:

- always set an expiration for transient data;
- do not manually create transient rows with `add_option()` or `update_option()`;
- understand the autoload behavior: transients set with an expiration time are not autoloaded; transients set without an expiration (or with `0`) are autoloaded;
- audit large or numerous transient rows in `wp_options` on sites without persistent object caching;
- avoid storing large blobs in transients if they will fall back to the database.

The autoload distinction is the practical reason for the "always set an expiration" guidance. An expiring transient adds two rows to `wp_options` (`_transient_{name}` and `_transient_timeout_{name}`) but does not contribute to the autoload footprint loaded on every request. A non-expiring transient does — which makes it indistinguishable from a regular autoloaded option, and usually means you should have used the Options API directly instead.

Useful inspection query:

```sql
SELECT option_name, LENGTH(option_value) AS size, autoload
FROM wp_options
WHERE option_name LIKE '\_transient\_%'
ORDER BY size DESC
LIMIT 20;
```

Total transient footprint estimate:

```sql
SELECT COUNT(*) AS transient_rows,
       SUM(LENGTH(option_value)) AS transient_bytes
FROM wp_options
WHERE option_name LIKE '\_transient\_%';
```

Expired transient cleanup is maintenance, not a guaranteed performance fix. If transients constantly rebuild and repopulate the table, the root issue is likely the caching strategy or lack of persistent object cache.

---

## 10. When to use transients

Use transients when:

- the data is expensive to compute or fetch;
- the data can safely expire;
- stale data is acceptable for a known period;
- the value can be regenerated on demand;
- the key has controlled cardinality;
- the data is not private unless the key is scoped safely;
- the storage backend is understood.

Good candidates:

- remote API responses
- expensive aggregate counts
- rendered sidebar fragments
- slow but reusable query results
- computed navigation or recommendation data
- non-critical external service data

Poor candidates:

- permanent settings
- canonical business records
- data that must never disappear early
- user-private data under shared keys
- high-cardinality per-request data
- large values on sites without persistent object cache
- data that changes so often the cache rarely hits

---

## 11. Transients vs options vs object cache

| Need | Prefer | Why |
|---|---|---|
| Permanent site setting | Options API | Durable configuration storage |
| Temporary value with expiration and database fallback | Transients API | Portable across environments |
| Temporary value only for current request | Static variable or runtime object cache | Avoids unnecessary persistence |
| Cross-request cache on known persistent object-cache environment | `wp_cache_*` or Transients API | Avoids repeated database work |
| Large/searchable structured data | Custom table or search index | Avoids abusing `wp_options`/post meta |
| Heavy search/filtering | Elasticsearch/OpenSearch or custom indexed storage | Better scaling characteristics |

---

## 12. Operational checklist

Before adding or reviewing transient usage:

- [ ] Is there a persistent object cache drop-in active?
- [ ] If not, is database-backed transient storage acceptable?
- [ ] Is the cached value safe to regenerate?
- [ ] Is the expiration explicit?
- [ ] Is the key cardinality bounded?
- [ ] Could many users create unique transient keys?
- [ ] Is the value too large for `wp_options` fallback?
- [ ] Is the data private or user-specific?
- [ ] Is there a cache stampede risk?
- [ ] Is there a fallback if the transient disappears early?
- [ ] Are expired transient rows accumulating?
- [ ] Is the object cache hit rate being monitored?

For enterprise/high-traffic sites:

- [ ] Use persistent object caching for transient-heavy workloads.
- [ ] Monitor Redis/Memcached memory and eviction behavior.
- [ ] Monitor object cache hit rate.
- [ ] Avoid unbounded transient creation.
- [ ] Pre-warm critical transient-backed data where appropriate.
- [ ] Use locks or stale-while-revalidate patterns for expensive regeneration.

---

## 13. Combined guidance from Remkus, WP VIP, WordPress.org, and the handbook PR

### Remkus / Make WordPress Fast

Remkus’ lessons emphasize the conceptual distinction: the Transients API prevents repeated work, but its performance profile depends on whether persistent object caching exists. Without persistent object caching, transients are database-backed; with persistent object caching, they can live in memory. The course also warns about expired transient buildup, misuse, and the need to treat persistent object caching as foundational on larger systems.

### WP VIP Learn / Enterprise WordPress Performance

WP VIP’s course gives the enterprise warning: transients are useful, but database-backed transients in `wp_options` are not desirable at enterprise scale. VIP’s guidance favors persistent object caching, such as Memcached/Redis-backed object-cache drop-ins, and emphasizes hit rates, race conditions, cache stampedes, and traffic-event readiness.

### WordPress.org Developer Documentation

The WordPress.org Transients API documentation describes transients as temporary cached data, commonly database-backed through `wp_options`, and notes that a Memcached-style object cache can move transient values into fast memory. The `WP_Object_Cache` documentation states that the default object cache is non-persistent and that transients use object-cache functions when persistent caching is configured; otherwise they fall back to the options table.

### Advanced Administration Handbook PR #485

The PR clarifies that `WP_CACHE`, `advanced-cache.php`, and `object-cache.php` are separate concerns. It adds the important operational warning that transients are not always stored in memory; without persistent object caching, they are stored in the database.

---

## 14. Common misconceptions

### “Transients are always memory cache.”

No. They are memory-backed only when the environment provides persistent object caching. Otherwise they are database-backed.

### “`WP_CACHE` enables Redis or Memcached.”

No. `WP_CACHE` relates to loading `advanced-cache.php`. Persistent object caching is handled by `object-cache.php`.

### “A transient will always exist until its expiration time.”

No. Expiration is a maximum lifetime, not a minimum. Transients can disappear early.

### “Expired transients always disappear immediately.”

No. Database-backed expired transient rows may remain until cleanup or until accessed and deleted.

### “Transients are safe for unlimited per-user/per-request data.”

No. High-cardinality transient keys can create large storage footprints and low cache hit rates.

### “Deleting expired transients is performance optimization.”

Sometimes it helps database hygiene, but it does not fix the root cause if code continually creates excessive transient rows or if the site lacks persistent object caching for transient-heavy workloads.

### “Transient option rows in `wp_options` are always autoloaded.”

No. Transients with an expiration are not autoloaded. Only transients set without an expiration (or with `0`) are autoloaded. This is why the “always set an expiration” guidance matters: it keeps transient data out of the per-request autoload footprint.

---

## References

- [WordPress.org Developer Docs: Transients API](https://developer.wordpress.org/apis/transients/)
- [WordPress Developer Blog: An introduction to the Transients API](https://developer.wordpress.org/news/2024/06/11/an-introduction-to-the-transients-api/)
- [WordPress.org Developer Docs: `get_transient()`](https://developer.wordpress.org/reference/functions/get_transient/)
- [WordPress.org Developer Docs: `set_transient()`](https://developer.wordpress.org/reference/functions/set_transient/)
- [WordPress.org Developer Docs: `WP_Object_Cache`](https://developer.wordpress.org/reference/classes/wp_object_cache/)
- [WordPress.org Developer Docs: `wp_start_object_cache()`](https://developer.wordpress.org/reference/functions/wp_start_object_cache/)
- [WordPress/Advanced-administration-handbook PR #485](https://github.com/WordPress/Advanced-administration-handbook/pull/485)
- Local extracted notes: `remkus-make-wordpress-fast/make-wordpress-fast-lessons.jsonl`
- Local extracted notes: `wpvip-enterprise-performance/wpvip-enterprise-performance-lessons.jsonl`


--- END DOCUMENT: REFERENCE-WP-Transients-Persistent-Object-Cache.md ---


Return a structured editorial revision plan. Do not edit files.
