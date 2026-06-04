# Phase 1 Review Findings

Scope: `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/REFERENCE-WP-Transients-Persistent-Object-Cache.md`

## 1) `wp_cache_add()` lock is not a cross-request lock without a persistent cache

- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/REFERENCE-WP-Transients-Persistent-Object-Cache.md`
- **Location:** Section 8, “Race conditions and cache stampedes” (`lines 240-260`)
- **Finding:** The lock example uses `wp_cache_add()` as if it coordinates concurrent requests generally. In default WordPress, the object cache is non-persistent and request-local, so this lock does not protect against stampedes across page loads unless a persistent shared object cache is active.
- **Severity:** High
- **Recommendation:** Add an explicit caveat that this pattern only works with a shared persistent object cache or another cross-request locking primitive. If the site does not have persistent object caching, recommend a database-backed mutex or stale-while-revalidate fallback instead of implying `wp_cache_add()` alone is sufficient.
- **Verification:** Confirm against the `WP_Object_Cache` docs that the default object cache persists only for the duration of a request, then simulate concurrent requests with and without `wp-content/object-cache.php` and compare how many times regeneration runs.

## 2) The regeneration example can cache `null` and poison the transient

- **Document:** `/Users/danknauss/Developer/GitHub/wp-perfopt-guide/REFERENCE-WP-Transients-Persistent-Object-Cache.md`
- **Location:** Section 5, “Expiration semantics” code block (`lines 156-170`)
- **Finding:** The example calls `json_decode()` and writes the result to the transient without validating the payload. If the upstream body is malformed or empty, `json_decode()` returns `null`, which is then cached. Subsequent calls will no longer enter the `false === $data` miss path, so the transient can hold a broken value until it expires.
- **Severity:** Medium
- **Recommendation:** Validate the decoded payload before calling `set_transient()`; if the body is invalid, return the fallback and do not write the transient. Prefer storing a normalized array/object payload and explicitly reject `null` or other unexpected shapes.
- **Verification:** Reproduce with an invalid JSON response body, confirm the current code stores `null`, then add the validation and confirm the transient is only written for valid data.
