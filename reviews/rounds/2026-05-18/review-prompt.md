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
