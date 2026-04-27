---
name: uiux-accessibility-review
description: |
  Dedicated accessibility audit — WCAG compliance, keyboard navigation, screen reader
  correctness, color contrast, semantic HTML, and ARIA. Triggers when:
  - A user-facing feature or redesign reaches Phase 4 verification
  - User says "check accessibility", "a11y audit", "WCAG review", "is this keyboard accessible"
  - lifecycle-orchestrator routes D (UI design) or A/B (user-facing features) reaches verify phase
  - Any component that handles forms, modals, tables, navigation, or status indicators

  Output: file:line findings sorted by WCAG severity — critical (ship blocker) → serious →
  moderate → minor. Each finding includes the rule violated and the exact fix.

license: MIT
metadata:
  author: Dilip Sahu
  source: WCAG 2.1 AA + Vercel web-interface-guidelines accessibility rules
  version: "1.0.0"
---

# Accessibility Review

**Standard:** WCAG 2.1 AA minimum. WCAG AAA for healthcare and compliance-critical interfaces.
**Output format:** `file:line [severity] rule — finding → fix`

---

## Audit Checklist (Run All Categories)

### 1. Color Contrast
- [ ] Normal text (< 18px regular, < 14px bold): minimum **4.5:1**
- [ ] Large text (≥ 18px regular, ≥ 14px bold): minimum **3:1**
- [ ] UI components (buttons, inputs, focus rings, icons with meaning): minimum **3:1**
- [ ] Disabled elements: exempt, but must still be distinguishable
- [ ] Check: light text on light background, gray on white, blue on purple

Tool: contrast ratio = (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter luminance.

### 2. Color as the Only Indicator
- [ ] Status badges: use icon + color + text — never color alone
- [ ] Form errors: use text message + icon + red border — not red border alone
- [ ] Charts/graphs: use pattern or label in addition to color
- [ ] Links in body text: must have underline or other non-color distinction

### 3. Keyboard Navigation
- [ ] All interactive elements reachable via Tab key
- [ ] Tab order matches visual reading order (left-to-right, top-to-bottom)
- [ ] No keyboard trap: Tab can always leave every component
- [ ] Modal/drawer: Tab cycles within the modal while open; Escape closes
- [ ] Dropdown/menu: Arrow keys navigate options; Enter/Space selects; Escape closes
- [ ] Date picker: Arrow keys navigate calendar; Enter selects date
- [ ] Forms: Tab moves field-to-field; Enter submits; no unexpected form submissions

### 4. Focus States
- [ ] Every interactive element has a **visible** focus indicator when focused via keyboard
- [ ] Never `outline: none` or `outline: 0` without a CSS replacement
- [ ] Use `:focus-visible` not `:focus` (avoids focus ring on mouse click)
- [ ] Focus ring contrast: minimum 3:1 against adjacent colors
- [ ] Focus ring: at least 2px solid, clearly visible

### 5. Semantic HTML
- [ ] `<button>` for actions (submit, open modal, toggle, etc.)
- [ ] `<a href>` for navigation (links that change URL or open new page)
- [ ] Never `<div onClick>` or `<span onClick>` for interactive elements
- [ ] `<form>` wraps all form inputs
- [ ] `<table>` with `<thead>`, `<tbody>`, `<th scope>` for tabular data
- [ ] `<nav>` for navigation landmarks; `<main>` for main content; `<aside>` for sidebars
- [ ] `<h1>` → `<h2>` → `<h3>` — sequential, no skipping levels

### 6. ARIA (Use Semantic HTML First — ARIA Only When Necessary)
- [ ] Icon-only buttons: `aria-label="[action]"` on the button
- [ ] Decorative icons: `aria-hidden="true"`
- [ ] Error messages: `aria-describedby="[error-id]"` on input + `role="alert"` or `aria-live="polite"` on error
- [ ] Loading states: `aria-busy="true"` on the container during load
- [ ] Modal: `role="dialog"` + `aria-modal="true"` + `aria-labelledby="[title-id]"`
- [ ] Custom dropdowns: `role="combobox"` + `aria-expanded` + `aria-controls`
- [ ] Progress indicators: `role="progressbar"` + `aria-valuenow` + `aria-valuemin` + `aria-valuemax`

### 7. Images and Icons
- [ ] Meaningful images: `alt="[descriptive text]"` — not filename, not "image of"
- [ ] Decorative images: `alt=""` (empty string, not omitted)
- [ ] Icon fonts: wrap in `<span aria-hidden="true">` with adjacent visible text or `aria-label` on parent
- [ ] SVG icons: `aria-hidden="true"` on decorative; `role="img"` + `<title>` on meaningful

### 8. Forms
- [ ] Every input has an associated `<label>` (via `htmlFor` or wrapping)
- [ ] Placeholder text is supplementary, never the only label
- [ ] Required fields: marked with `required` attribute + visible indicator
- [ ] Error messages: appear inline below the field; reference the field by name
- [ ] Submit button: descriptive label ("Save Changes" not "Submit")
- [ ] Autocomplete: `autocomplete` attribute on name, email, phone, address fields
- [ ] No blocking paste (`onPaste` + `preventDefault` is forbidden)

### 9. Motion and Animation
- [ ] `@media (prefers-reduced-motion: reduce)` honored — all animations disabled or instant
- [ ] No content flashing more than 3 times per second (seizure risk)
- [ ] Auto-playing animation: must have pause control if > 5 seconds
- [ ] Parallax and scroll-jacking: disabled under `prefers-reduced-motion`

### 10. Skip Links and Landmarks
- [ ] Skip-to-main-content link as first focusable element on page
- [ ] `<main>` landmark present and wraps primary content
- [ ] Navigation landmark: `<nav aria-label="Main navigation">`
- [ ] Multiple navs on one page: each has a unique `aria-label`

---

## Severity Scale

| Severity | WCAG Level | Meaning |
|----------|-----------|---------|
| **Critical** | Fail AA | Ship blocker — excludes users from core functionality |
| **Serious** | Fail AA | Fix before merge — significant barrier for assistive tech users |
| **Moderate** | Fail AA or best practice | Fix in current sprint |
| **Minor** | Best practice | Note for backlog |

---

## Output Format

```
## Accessibility Review: [file or feature name]

### Critical (Ship Blockers)
src/components/IntakeForm.tsx:84  [CRITICAL] WCAG 1.3.1 — input#email has no label
  → Add: <label htmlFor="email">Email address</label>

src/components/StatusBadge.tsx:12 [CRITICAL] WCAG 1.4.1 — status conveyed by color only
  → Add icon + text alongside color: <CheckIcon aria-hidden /> Confirmed

### Serious
src/components/Modal.tsx:6        [SERIOUS] WCAG 2.1.2 — keyboard trap in modal
  → Add: Tab cycling scoped to modal; Escape closes

### Moderate
src/components/Button.tsx:23      [MODERATE] WCAG 2.4.7 — focus ring removed (outline-none)
  → Replace with: focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500

### Minor
src/components/Nav.tsx:44         [MINOR] Best practice — multiple <nav> elements lack aria-label
  → Add: aria-label="Main navigation" and aria-label="Footer navigation"

### Passing
src/components/Card.tsx           ✓ pass
src/components/Input.tsx          ✓ pass (with label, error state, autocomplete)
```

---

## Healthcare-Specific Rules (This Product)

For clinic-facing and patient-facing screens, WCAG AA is the floor, not the target:

- Target **WCAG AAA** for all clinical screens (doctors, nurses, receptionists reading data)
- Minimum contrast: **7:1** for clinical text (patient names, dosages, appointment times)
- All status indicators: color + icon + text — **never color alone** (colorblind clinicians)
- All forms: visible labels always shown — never placeholder-only (screen readers, cognitive accessibility)
- No auto-advancing UI (carousels, auto-refreshing content without manual control)
