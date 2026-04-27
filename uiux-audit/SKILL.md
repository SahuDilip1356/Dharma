---
name: uiux-audit
description: |
  Audit UI code against Vercel Web Interface Guidelines + UI UX Pro Max UX rules. Triggers when:
  - User says "review my UI", "audit this", "check accessibility", "is this up to standard"
  - Reviewing a PR or component before shipping
  - A build task is complete and needs a quality gate before reporting done
  - uiux-designer master skill triggers a self-audit at end of build tasks

  Covers 18 rule categories: accessibility, focus states, forms, animation, typography,
  content handling, images, performance, navigation/state, touch, safe areas, dark mode,
  locale/i18n, hydration safety, hover states, content/copy, anti-patterns, + 99 UX guidelines.

  Output: file:line format — concise, actionable, prioritized by severity.

license: MIT
metadata:
  author: Dilip Sahu
  source: Vercel web-interface-guidelines + UI UX Pro Max ux-guidelines.csv
  version: "1.0.0"
---

# UI/UX Audit (Vercel Guidelines + UX Rules)

**Source:** Fetch fresh guidelines before each review from:
```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

**Fallback (if WebFetch unavailable):** Apply the full ruleset below.

---

## How to Run an Audit

1. Read the files specified (or ask user which files to review)
2. Check every rule in the 18 categories below
3. Cross-reference with the 99 UX guidelines in the severity table
4. Output findings in `file:line` format — terse, VS Code clickable
5. Group by file, sorted by severity within each file

---

## The 18 Rule Categories

### 1. Accessibility
- Icon-only buttons → must have `aria-label`
- Form controls → must have `<label>` or `aria-label`
- Interactive elements → need keyboard handlers (`onKeyDown`/`onKeyUp`)
- `<button>` for actions, `<a>`/`<Link>` for navigation — never `<div onClick>`
- Images → `alt` required (or `alt=""` if purely decorative)
- Decorative icons → `aria-hidden="true"`
- Async updates (toasts, validation) → `aria-live="polite"`
- Semantic HTML before ARIA: `<button>`, `<a>`, `<label>`, `<table>`
- Heading hierarchy: `<h1>`–`<h6>` sequential; skip link for main content
- `scroll-margin-top` on heading anchors

### 2. Focus States
- Every interactive element → visible focus: `focus-visible:ring-*` or equivalent
- Never `outline-none` / `outline: none` without a replacement focus indicator
- Use `:focus-visible` not `:focus` (avoids focus ring on mouse click)
- Compound controls → `:focus-within` for group focus

### 3. Forms
- Inputs → `autocomplete` and meaningful `name` attributes
- Correct `type`: `email`, `tel`, `url`, `number` + `inputmode` for mobile
- Never block paste (`onPaste` + `preventDefault`)
- Labels clickable: `htmlFor` matching input `id` or label wrapping input
- Disable spellcheck on emails, codes, usernames: `spellCheck={false}`
- Checkbox/radio: label and control share a single hit target
- Submit button disabled while request is in flight; spinner during request
- Errors inline next to fields; focus first error field on submit
- Placeholders end with `…` and show pattern example
- `autocomplete="off"` on non-auth fields to avoid password manager interference
- Warn before navigation with unsaved changes (`beforeunload` or router guard)

### 4. Animation
- `prefers-reduced-motion` must be honored — provide reduced variant or disable
- Animate `transform`/`opacity` only (compositor-friendly, no repaints)
- Never `transition: all` — list properties explicitly
- Correct `transform-origin` on animated elements
- SVG transforms: use `<g>` wrapper with `transform-box: fill-box; transform-origin: center`
- Animations must be interruptible — respond to user input mid-animation
- Duration: 150-300ms for micro-interactions; never >500ms for UI transitions

### 5. Typography
- `…` not `...` (ellipsis character, not three dots)
- Curly quotes `"` `"` not straight `"`
- Non-breaking spaces: `10&nbsp;MB`, `⌘&nbsp;K`, brand names
- Loading states end with `…`: `"Loading…"`, `"Saving…"`
- `font-variant-numeric: tabular-nums` for number columns
- `text-wrap: balance` or `text-pretty` on headings (prevents widows)
- Body text: 16px minimum on mobile, line-height 1.5–1.75
- Text containers: max-width 65–75ch

### 6. Content Handling
- Text containers → `truncate`, `line-clamp-*`, or `break-words` for long content
- Flex children with text → `min-w-0` to allow truncation
- Empty states must be handled — never render broken UI for empty arrays/strings
- User-generated content: design for short, average, and very long inputs

### 7. Images
- `<img>` → explicit `width` and `height` to prevent CLS
- Below-fold images → `loading="lazy"`
- Above-fold critical images → `priority` or `fetchpriority="high"`
- Format: WebP preferred; use `<picture>` for fallbacks

### 8. Performance
- Lists >50 items → virtualize (`virtua`, `content-visibility: auto`)
- No layout reads in render: `getBoundingClientRect`, `offsetHeight`, `scrollTop`
- Batch DOM reads/writes; never interleave
- Prefer uncontrolled inputs; controlled inputs must be cheap per keystroke
- `<link rel="preconnect">` for CDN/asset domains
- Critical fonts → `<link rel="preload" as="font">` + `font-display: swap`
- Images → optimized size and format; no unoptimized full-size images
- Large JS bundles → code split by route/feature

### 9. Navigation & State
- URL reflects state: filters, tabs, pagination, expanded panels → query params
- Links use `<a>`/`<Link>` (supports Cmd/Ctrl+click, middle-click, right-click)
- Deep-link all stateful UI (if `useState`, consider URL sync via `nuqs`)
- Destructive actions → confirmation modal or undo window — never immediate delete

### 10. Touch & Interaction
- `touch-action: manipulation` (removes 300ms double-tap zoom delay)
- `-webkit-tap-highlight-color` set intentionally (not left as browser default)
- `overscroll-behavior: contain` in modals, drawers, sheets
- Drag operations: disable text selection; `inert` on dragged elements
- `autoFocus`: desktop only, single primary input; avoid on mobile
- Minimum touch target: 44×44px; minimum 8px gap between adjacent targets

### 11. Safe Areas & Layout
- Full-bleed layouts → `env(safe-area-inset-*)` for device notches
- Unwanted scrollbars → `overflow-x-hidden` on containers
- Use flex/grid over JS measurement for layout

### 12. Dark Mode & Theming
- `color-scheme: dark` on `<html>` for dark themes (fixes scrollbar, inputs)
- `<meta name="theme-color">` matches page background
- Native `<select>` → explicit `background-color` and `color` for Windows dark mode

### 13. Locale & i18n
- Dates/times → `Intl.DateTimeFormat` not hardcoded formats
- Numbers/currency → `Intl.NumberFormat` not hardcoded formats
- Language detection via `Accept-Language` / `navigator.languages`, not IP
- Brand names, code tokens → `translate="no"` to prevent garbled auto-translation

### 14. Hydration Safety
- Inputs with `value` → need `onChange` (or use `defaultValue`)
- Date/time rendering → guard against server/client hydration mismatch
- `suppressHydrationWarning` only where genuinely needed

### 15. Hover & Interactive States
- Buttons/links → need `hover:` state (visual feedback)
- Interactive states must increase contrast on hover/active/focus vs rest state

### 16. Content & Copy
- Active voice: "Install the CLI" not "The CLI will be installed"
- Title Case for headings/buttons (Chicago style)
- Numerals for counts: "8 deployments" not "eight deployments"
- Specific labels: "Save API Key" not "Continue"
- Error messages include the fix/next step, not just the problem description
- Second person; avoid first person
- `&` over "and" where space-constrained

### 17. Color Contrast (from UX Guidelines)
- Normal text: minimum 4.5:1 contrast ratio (WCAG AA)
- Large text (18px+ or 14px+ bold): minimum 3:1
- Never convey information by color alone — always add icon or text
- Error/success states: red/green + icon + text (never color only)

### 18. Anti-Patterns (Flag These)
- `user-scalable=no` or `maximum-scale=1` disabling zoom
- `onPaste` with `preventDefault`
- `transition: all`
- `outline-none` without `focus-visible` replacement
- `onClick` navigation without `<a>`
- `<div>` or `<span>` with click handlers (should be `<button>`)
- Images without `width`/`height`
- Large arrays `.map()` without virtualization
- Form inputs without labels
- Icon buttons without `aria-label`
- Hardcoded date/number formats (use `Intl.*`)
- `autoFocus` without clear justification
- Infinite animations on decorative elements
- Horizontal scroll on mobile

---

## Output Format

Group by file. `file:line` format — VS Code clickable. Terse. No preamble.

```
## src/components/Button.tsx

src/components/Button.tsx:42  [HIGH] icon button missing aria-label
src/components/Button.tsx:18  [HIGH] input lacks associated label
src/components/Button.tsx:55  [MED]  animation missing prefers-reduced-motion
src/components/Button.tsx:67  [MED]  transition: all → list properties explicitly

## src/components/Modal.tsx

src/components/Modal.tsx:12   [MED]  missing overscroll-behavior: contain
src/components/Modal.tsx:34   [LOW]  "..." → "…" (ellipsis character)

## src/components/Card.tsx

✓ pass
```

**Severity:** `[HIGH]` = ship blocker | `[MED]` = fix before merge | `[LOW]` = note for backlog

State the issue + location. Explain the fix only if non-obvious. No preamble or summary prose.
