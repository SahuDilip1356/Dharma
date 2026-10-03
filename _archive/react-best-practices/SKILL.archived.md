---
name: react-best-practices
description: |
  React and Next.js performance optimization skill for Dharma's Phase 3 (Build).
  70 rules across 8 categories, prioritized by impact — from critical (waterfalls,
  bundle size) to incremental (advanced patterns). Apply when writing, reviewing,
  or refactoring React/Next.js code to ensure optimal performance.

  Triggers at Phase 3 (Build) when:
  - Writing new React components or Next.js pages
  - Implementing data fetching (client or server-side)
  - Reviewing code for performance issues
  - Optimizing bundle size or load times
  - Frontend performance route (Route F)

  Complements (does NOT replace) `uiux-react-patterns`:
  - `uiux-react-patterns` owns: forms, accessibility patterns, component API design
  - `react-best-practices` owns: performance — waterfalls, bundle, re-renders, JS efficiency

  Source: https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
license: MIT
metadata:
  author: vercel-labs (adapted for Dharma by Dilip Sahu)
  version: "1.0.0"
---

# React Best Practices — Performance Optimization

**Companion to `uiux-react-patterns`. Apply both when building React/Next.js UI. They answer different questions.**

| Skill | Question answered |
|---|---|
| `uiux-react-patterns` | Does this React code follow good UX patterns? (forms, a11y, component API design) |
| `react-best-practices` | Is this React code performant? (waterfalls, bundle size, re-renders, JS efficiency) |

---

## Dharma Phase Placement

| Phase | Role |
|---|---|
| Phase 3 — Build | Primary phase — apply during code generation and review |
| Phase 4 — Verify | Secondary — flag violations found in browser profiling |

**Mandatory for:** Route A (New Product), Route B (New Feature with UI), Route F (Performance)
**Recommended for:** Route D (UI/UX Design, implementation phase), Route E (Refactor of React code)

---

## Rule Categories by Priority

Apply in priority order. Stop at the first violation and fix it before proceeding.

| Priority | Category | Impact | Rule Prefix |
|---|---|---|---|
| 1 | Eliminating Waterfalls | CRITICAL | `async-` |
| 2 | Bundle Size Optimization | CRITICAL | `bundle-` |
| 3 | Server-Side Performance | HIGH | `server-` |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | `client-` |
| 5 | Re-render Optimization | MEDIUM | `rerender-` |
| 6 | Rendering Performance | MEDIUM | `rendering-` |
| 7 | JavaScript Performance | LOW-MEDIUM | `js-` |
| 8 | Advanced Patterns | LOW | `advanced-` |

---

## Category 1: Eliminating Waterfalls — CRITICAL

Sequential async calls are the most common React performance killer. Always check this first.

| Rule | What it prevents | Pattern |
|---|---|---|
| `async-parallel` | N sequential fetches | `Promise.all([fetchA(), fetchB()])` |
| `async-cheap-condition-before-await` | Awaiting expensive flag before cheap check | Move sync conditions before `await` |
| `async-defer-await` | Awaiting in branches that don't need it | Move `await` into the branch where it's used |
| `async-api-routes` | Waterfall chains in API routes | Start promises early, `await` late |
| `async-suspense-boundaries` | Blocking render for all data | Use `<Suspense>` to stream content independently |

**Quick check:** Any time you see two consecutive `await` calls, ask: "Are these independent?" If yes → `Promise.all()`.

---

## Category 2: Bundle Size Optimization — CRITICAL

Every byte shipped is a byte the user downloads. Check bundle impact for every dependency added.

| Rule | What it prevents | Pattern |
|---|---|---|
| `bundle-barrel-imports` | Entire library pulled in for one export | `import { fn } from 'lib/fn'` not `import { fn } from 'lib'` |
| `bundle-dynamic-imports` | Heavy components in initial bundle | `next/dynamic(() => import('./HeavyChart'))` |
| `bundle-defer-third-party` | Analytics/logging blocking hydration | Load after `useEffect` or `requestIdleCallback` |
| `bundle-conditional` | Feature-flagged code in main bundle | `if (featureEnabled) { await import('./feature') }` |
| `bundle-analyzable-paths` | Non-tree-shakeable imports | Prefer static, analyzable import paths |
| `bundle-preload` | Perceived latency on intentional navigation | Preload on hover/focus, not on mount |

---

## Category 3: Server-Side Performance — HIGH

Server Components and RSC boundaries have unique performance rules. Apply these before any RSC code is reviewed.

| Rule | What it prevents | Pattern |
|---|---|---|
| `server-parallel-fetching` | Sequential fetches in Server Components | Restructure components to parallelize |
| `server-cache-react` | Duplicate DB calls per request | `React.cache()` for per-request deduplication |
| `server-cache-lru` | Duplicate DB calls across requests | LRU cache at module level |
| `server-hoist-static-io` | Font/logo fetches on every request | Hoist to module level (outside component) |
| `server-no-shared-module-state` | Request data leaking between users | Never store request-specific data in module scope |
| `server-dedup-props` | Duplicate serialization at RSC boundary | Don't pass the same data twice in RSC props |
| `server-serialization` | Oversized RSC payloads | Minimize data passed to `"use client"` components |
| `server-after-nonblocking` | Blocking response for non-critical ops | Use `after()` for analytics, logging, side effects |
| `server-auth-actions` | Unauthenticated Server Actions | Authenticate every Server Action like an API route |

---

## Category 4: Client-Side Data Fetching — MEDIUM-HIGH

| Rule | What it prevents | Pattern |
|---|---|---|
| `client-swr-dedup` | Duplicate API calls from sibling components | SWR with shared key deduplicates automatically |
| `client-event-listeners` | Multiple identical global listeners | Deduplicate with a registry or module-level reference |
| `client-passive-event-listeners` | Scroll jank | `addEventListener('scroll', fn, { passive: true })` |
| `client-localstorage-schema` | Stale localStorage data after deploys | Version your localStorage keys |

---

## Category 5: Re-render Optimization — MEDIUM

Optimize re-renders only after profiling confirms they're a bottleneck. Don't pre-optimize.

| Rule | Key principle |
|---|---|
| `rerender-memo` | Extract expensive computations into memoized child components |
| `rerender-memo-with-default-value` | Hoist non-primitive default props to constants outside component |
| `rerender-dependencies` | Use primitive (string, number) dependencies in `useEffect` — not objects |
| `rerender-derived-state` | Subscribe to derived booleans, not raw state objects |
| `rerender-derived-state-no-effect` | Derive state during render, not in a `useEffect` |
| `rerender-functional-setstate` | `setState(prev => prev + 1)` not `setState(count + 1)` in callbacks |
| `rerender-lazy-state-init` | `useState(() => expensiveComputation())` not `useState(expensiveComputation())` |
| `rerender-simple-expression-in-memo` | Don't wrap `a + b` in `useMemo` — the memo overhead costs more |
| `rerender-split-combined-hooks` | Split hooks with independent dependency arrays |
| `rerender-move-effect-to-event` | Move interaction logic from `useEffect` to event handlers |
| `rerender-transitions` | `startTransition` for non-urgent updates (search filtering, sorting) |
| `rerender-use-deferred-value` | `useDeferredValue` to keep input responsive during expensive renders |
| `rerender-use-ref-transient-values` | `useRef` for values that change frequently but don't need re-render |
| `rerender-no-inline-components` | Never define a component inside another component |
| `rerender-defer-reads` | Don't subscribe to state that's only read in callbacks |

---

## Category 6: Rendering Performance — MEDIUM

| Rule | Key principle |
|---|---|
| `rendering-hoist-jsx` | Extract static JSX (icons, headers) outside the component function |
| `rendering-content-visibility` | `content-visibility: auto` for long off-screen lists |
| `rendering-hydration-no-flicker` | Inline script for client-only data (theme, locale) to prevent flash |
| `rendering-conditional-render` | Use ternary `{a ? <A/> : <B/>}` not `{a && <A/>}` (avoids `0` render) |
| `rendering-usetransition-loading` | `useTransition` over manual `isLoading` boolean state |
| `rendering-activity` | `<Activity>` for show/hide to preserve state without DOM thrash |
| `rendering-resource-hints` | `preload`, `prefetchDNS` from `react-dom` for critical resources |
| `rendering-script-defer-async` | All `<script>` tags must use `defer` or `async` |
| `rendering-animate-svg-wrapper` | Animate a `<div>` wrapper, not the `<svg>` element directly |
| `rendering-svg-precision` | Reduce SVG coordinate decimal precision (4 → 1 decimal) |
| `rendering-hydration-suppress-warning` | `suppressHydrationWarning` for expected client/server mismatches |

---

## Category 7: JavaScript Performance — LOW-MEDIUM

| Rule | Key principle |
|---|---|
| `js-index-maps` | Build `Map<id, item>` once for O(1) repeated lookups instead of `Array.find` |
| `js-set-map-lookups` | Use `Set` for membership checks — O(1) vs O(n) |
| `js-combine-iterations` | One loop with `flatMap` instead of `filter` + `map` |
| `js-early-exit` | Return early from functions — reduce nesting |
| `js-hoist-regexp` | `RegExp` creation outside of loops |
| `js-cache-function-results` | Cache expensive function results in module-level `Map` |
| `js-cache-storage` | Cache `localStorage`/`sessionStorage` reads — avoid repeated parsing |
| `js-batch-dom-css` | Group CSS changes via class toggling, not individual property sets |
| `js-request-idle-callback` | Defer non-critical work: `requestIdleCallback(() => { ... })` |
| `js-flatmap-filter` | `arr.flatMap(x => condition ? [transform(x)] : [])` |
| `js-tosorted-immutable` | `arr.toSorted()` preserves original, `arr.sort()` mutates |
| `js-min-max-loop` | Loop for min/max; `Math.min(...arr)` is O(n) stack overhead on large arrays |

---

## Category 8: Advanced Patterns — LOW

Apply only when the lower-priority categories are clean.

| Rule | Key principle |
|---|---|
| `advanced-init-once` | App initialization logic runs once per app, not per component mount |
| `advanced-event-handler-refs` | Store event handlers in refs for stable references |
| `advanced-effect-event-deps` | `useEffectEvent` results must not appear in effect dependency arrays |

---

## How to Apply in Dharma Phase 3

**During code generation (superpowers-execute):**
1. Before writing any component, check: does it fetch data? → apply Category 1 + 3
2. Before adding any import: will this grow the bundle? → apply Category 2
3. After writing component: does it have `useEffect`? → check Category 5

**During code review (superpowers-verify):**
1. Run through Categories 1–2 as hard gates — any violation blocks approval
2. Categories 3–4 as soft flags — note but don't block
3. Categories 5–8 as advisory — report, don't block unless profiling shows measurable regression

**During performance route (Route F):**
- Categories 1, 2, 3 are primary investigation areas
- Run `react-best-practices` before `uiux-react-patterns` on Route F — performance is the priority

---

## Ownership Boundaries

| Owns | Does NOT Own |
|---|---|
| React/Next.js performance optimization rules (Categories 1–8) | UX patterns, form design, component variant API (that is `uiux-react-patterns`) |
| Bundle analysis guidance and import patterns | Accessibility patterns — aria-label, focus-visible, screen reader (that is `uiux-react-patterns`) |
| Server Component and RSC boundary performance | Design system tokens, visual styling (that is `uiux-frontend-design-system`) |
| Re-render profiling guidance | Browser-level functional verification — screenshots, console logs (that is `webapp-testing`) |
| JS micro-optimization patterns | Post-ship performance monitoring — p95 latency, error rates (that is `ai-observability`) |

**Boundary with `uiux-react-patterns`:** When a rule could be owned by either skill, apply this test:
- "Does it affect how fast the code runs?" → `react-best-practices`
- "Does it affect how good the UX feels or how accessible it is?" → `uiux-react-patterns`

---

## Quick Checklist for Phase 3 Exit

Before exiting Phase 3 (Build), confirm:

- [ ] No sequential `await` calls on independent operations (`async-parallel`)
- [ ] No barrel file imports for heavy libraries (`bundle-barrel-imports`)
- [ ] Heavy components use `next/dynamic` (`bundle-dynamic-imports`)
- [ ] Server Components parallelize their fetches (`server-parallel-fetching`)
- [ ] `React.cache()` used for per-request deduplication (`server-cache-react`)
- [ ] No module-level mutable state in RSC context (`server-no-shared-module-state`)
- [ ] Analytics/logging deferred to after hydration (`bundle-defer-third-party`)
- [ ] No inline component definitions (`rerender-no-inline-components`)
- [ ] Static JSX extracted outside component function (`rendering-hoist-jsx`)
