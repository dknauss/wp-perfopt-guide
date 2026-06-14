# AGENTS.md — WordPress Performance Optimization Guide

Agent configuration for AI-assisted editorial and documentation work in this repository. Agents operate under human editorial authority; do not make substantive guidance changes without preserving source-grounded rationale.

## 1. Project Context

- **Project type:** Technical documentation — WordPress performance optimization guidance.
- **Primary audience:** WordPress developers, performance engineers, SREs, technical leads, and enterprise WordPress operators.
- **Goal:** Maintain practical, source-grounded guidance for diagnosing and improving WordPress performance across hosting, caching, database, runtime, frontend, and operational layers.
- **Repository role:** Canonical local source repository for the Performance series and its companion references.

## 2. Current Performance Series

| Document | Purpose |
|---|---|
| `DEVELOPER_REFERENCE.md` | Unified developer reference and mental model for performance work. |
| `wordpress-performance-optimization-checklist.md` | General WordPress performance checklist and triage flow. |
| `enterprise-performance-operational-checklist.md` | Enterprise/WP VIP-oriented operational checklist. |
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

- Local planning state may live in `.planning/`, but that directory is intentionally local-only unless a human editor decides it belongs in the published repository.
- Update `CHANGELOG.md` for meaningful documentation, governance, or workflow changes.
- Do not commit generated exports, logs, screenshots, or local environment files unless explicitly requested.
- Keep source Markdown documents readable in plain GitHub rendering.
- If external facts may have changed, verify them before updating guidance.

## 8. Browser/Playwright Handoff

If a task requires browser automation, screenshots, page interaction, or browser-only inspection and the current session does not have browser tooling, state that a fresh browser-capable session is required. Do not imply browser mode can be enabled mid-session.
