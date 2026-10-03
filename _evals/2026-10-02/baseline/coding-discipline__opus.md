## Q1

Files read: SKILL.md, think-before-coding.md, goal-driven-execution.md, simplicity-first.md, surgical-changes.md

First I'd read `lib/api.ts` (and grep for `fetchConsents(` and any existing retry/backoff helper such as `withRetry`, `p-retry`, `axios-retry`) before writing anything.

```
Before I code:
- Assumptions:
  - fetchConsents() is async and returns a Promise (fetch or axios under the hood).
  - "Retry" means retry on transient failures only: network errors and 5xx/429.
    4xx such as 401/403/404 are not retried, because retrying them hides real bugs.
  - 3 attempts total, short fixed backoff (e.g. 300ms, 600ms). No jitter, no config.
  - The retry goes inside fetchConsents, so every caller gets it and no call sites change.
  - fetchConsents is a GET (idempotent), so it is safe to retry.
- Interpretations I'm choosing between:
  (a) wrap the one fetchConsents call inside lib/api.ts, or
  (b) add a generic retry utility for all API calls.
  I'm choosing (a). You asked about one function.
- Simpler alternative considered: if the repo already has a retry helper or
  a client with retry support (axios-retry, react-query `retry`), I'd use that
  instead of writing a loop.
- Open questions:
  1. Should 429/5xx only be retried, or every error?
  2. Is 3 attempts / ~1s total budget OK, or does a UI spinner need it faster?
```

If you say "use your judgment", I'll go with the assumptions above.

```
Scope:
- What this does: retries fetchConsents up to 3 times on network errors or 5xx/429.
- What this deliberately doesn't do: no generic retry util, no config options,
  no jitter/exponential schedule, no logging, no changes to other API functions.
- Lines: ~12
```

Proposed edit to `lib/api.ts` (I'd match the file's existing style; this assumes it uses `fetch`):

```ts
export async function fetchConsents(/* existing params unchanged */) {
  for (let attempt = 1; ; attempt++) {
    try {
      return await fetchConsentsOnce(/* same args */); // the existing body, unchanged
    } catch (err) {
      const status = (err as { status?: number }).status;
      const retryable = status === undefined || status === 429 || status >= 500;
      if (!retryable || attempt === 3) throw err;
      await new Promise((r) => setTimeout(r, 300 * attempt));
    }
  }
}
```

If the existing body is short, I'd inline the loop around it and skip the `fetchConsentsOnce` split. If it already throws an error that carries `status`, I'd use that and not add new error types.

```
Plan:
1. Add retry loop                         → verify: `npx tsc --noEmit` passes
2. Test: mock fails 2x with 503, then OK  → verify: resolves; called 3 times
3. Test: mock returns 404                 → verify: rejects; called 1 time
4. Test: mock fails 3x with 503           → verify: rejects; called 3 times
5. Run the existing suite                 → verify: `npm test -- lib/api` green
```
(Tests use fake timers so they don't actually wait.)

Simpler version possible? No. One loop, inside the one function you named.

```
Diff scope:
- Changed: lib/api.ts (fetchConsents only); lib/api.test.ts (3 new cases)
- Pre-existing issues noticed (NOT changed): <listed here if seen, e.g. other
  API calls with no retry. I'd mention them, not change them>
- Orphans removed: none
```

## Q2

Files read: SKILL.md, think-before-coding.md, goal-driven-execution.md

```
Before I code:
- Assumptions: none safe to make. "Better" has no observable success criterion.
- Interpretations I'm choosing between:
  1. Performance: it loads slowly (e.g. slow first render, too many API calls)
  2. Visual/UX: layout, hierarchy, spacing, mobile, empty/loading states
  3. Content: wrong or missing metrics/widgets, data people actually need
  4. Correctness: numbers are wrong, stale, or inconsistent
  5. Accessibility: contrast, keyboard nav, screen reader labels
  6. Code quality: the dashboard component is hard to maintain
- Simpler alternative considered: pick the one thing that hurts most and fix
  only that, not a broad redesign.
- Open questions:
  1. Which dashboard? (file/route, e.g. app/dashboard/page.tsx)
  2. What's the biggest complaint right now, from you or from users?
  3. What would tell you it's "better"? (a number, a screenshot, a specific behaviour)
  4. Any constraints: design system, no new dependencies, deadline?
```

I won't write code until we agree on a goal. "Make it better" is the "clean it up" case: I shouldn't take it as creative license.

What I'd do in the meantime (read-only): open the dashboard route and components, and come back with a short list of concrete issues I can see, each one tied to a check. For example:

| If you mean... | Verifiable goal I'd propose |
|---|---|
| Faster | Measure LCP/TTI before (Lighthouse or a timed load); target e.g. under 2s; measure again after |
| Clearer UX | Name 2-3 specific issues (e.g. no loading state, KPI cards cut off at 375px); before/after screenshots at 375px and 1280px |
| Correct data | Write a test that reproduces the wrong number, then make it pass |
| Accessible | axe/Lighthouse a11y run: zero critical violations |

Once you pick one, I'd give a plan in this shape:

```
Plan:
1. <specific change>  → verify: <runnable check>
2. <specific change>  → verify: <runnable check>
```

Then I'd work through it and finish with a verification ledger. I would not do a "general improvement" pass.

## Q3

Files read: SKILL.md, surgical-changes.md

A single rename is a trivial task, so I skip the "Before I code" block and the multi-step plan. I'd still check two things first so the rename doesn't break anything:

1. `grep -n "\busr\b" components/Profile.tsx`: find every occurrence.
2. Check that `user` isn't already defined in the same scope (e.g. a `user` prop, an import, or `const { user } = useAuth()`). If it is, renaming would shadow it or cause a collision. I'd stop and ask before going ahead.

Also, if `usr` is exported, or is a prop/key name that other files use (e.g. `<Profile usr={...}>`, or `usr` as an object key in an API payload), then this is no longer a local rename. I'd flag that and ask, not edit other files without telling you.

Assuming `usr` is a local variable in that file only, the edit is to replace each identifier `usr` with `user` in `components/Profile.tsx`. That means the declaration and every reference, nothing else. Example:

```diff
-  const usr = useCurrentUser();
-  if (!usr) return null;
-  return <h1>{usr.name}</h1>;
+  const user = useCurrentUser();
+  if (!user) return null;
+  return <h1>{user.name}</h1>;
```

I don't change strings or comments that merely contain "usr", I don't touch other short names nearby, I don't reformat, and I don't reorder imports.

Verify: `grep -n "\busr\b" components/Profile.tsx` returns nothing, and `npx tsc --noEmit` passes.

```
Diff scope:
- Changed: components/Profile.tsx (identifier usr -> user, N occurrences)
- Pre-existing issues noticed (NOT changed): <e.g. other abbreviated names
  like `prf`, unused import. Mentioned only>
- Orphans removed: none
```
