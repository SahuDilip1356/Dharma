---
name: uiux-interaction-review
description: |
  Interaction design review — states, transitions, feedback loops, and microinteractions.
  Triggers when:
  - A component or feature needs its interaction quality assessed
  - User says "review the interactions", "check states", "the feedback feels off", "transitions"
  - Route D (UI design) reaches Phase 1 or Phase 4
  - Any form, button, modal, dropdown, or multi-step flow is being reviewed
  - A feature works but feels unpolished or unresponsive to the user

  Covers: all component states, animation quality, feedback timing, error recovery UX,
  loading patterns, and destructive action safeguards.

license: MIT
metadata:
  author: Dilip Sahu
  source: UI UX Pro Max ux-guidelines.csv + Vercel web-interface-guidelines
  version: "1.0.0"
---

# Interaction Design Review

**Purpose:** Ensure every interactive element communicates clearly — before, during, and after each user action. Interactions that feel broken or unresponsive destroy trust faster than any visual issue.

---

## The State Matrix (Every Interactive Component Must Have These)

For every button, input, link, toggle, card, or interactive region — verify all applicable states:

| State | What It Should Show | Common Failure |
|-------|-------------------|----------------|
| Default | Resting — clearly interactive | Looks like static text |
| Hover | Visual shift — color, shadow, or underline change | No feedback, user unsure it's clickable |
| Focus | Visible ring — keyboard-accessible | `outline: none` with no replacement |
| Active / Pressed | Depressed — color darkens, slight scale | No feedback on click |
| Disabled | Reduced opacity + `not-allowed` cursor + `disabled` attr | Same as default — user tries to click |
| Loading | Spinner or skeleton + interaction disabled | Double-submission possible |
| Error | Inline message + visual indicator (border, icon) | No message, or message too far from field |
| Success | Confirmation — checkmark, toast, or state change | Silent — user unsure if action worked |
| Empty | Helpful message + CTA | Blank screen — user thinks it's broken |

---

## Checklist by Component Type

### Buttons
- [ ] Default, hover, focus, active, disabled, loading states all present
- [ ] Loading: button disabled (`disabled` attr) + spinner visible + `aria-busy="true"`
- [ ] Destructive buttons: visually distinct (red / warning color) from primary actions
- [ ] Destructive actions: confirmation required before execution
- [ ] Submit button: stays enabled until request starts; disables during request
- [ ] Label specific: "Save API Key" not "Save"; "Delete Account" not "Delete"

### Form Inputs
- [ ] Default, focus, filled, error, disabled, read-only states all present
- [ ] Error: red border + error icon + inline error message below field
- [ ] Error message: tells the user what to do, not just what went wrong
  - ❌ "Invalid email"
  - ✅ "Enter a valid email address (example: you@clinic.com)"
- [ ] Success/validated: green checkmark or border when appropriate
- [ ] Inline validation: fires on blur (not on every keystroke — too aggressive)
- [ ] On submit with errors: focus jumps to first error field
- [ ] Unsaved changes warning: `beforeunload` or router guard if form has data

### Modals and Drawers
- [ ] Opens with focus trapped inside
- [ ] Escape key closes
- [ ] Backdrop click closes (unless destructive confirmation — lock backdrop)
- [ ] `overscroll-behavior: contain` (prevents page scrolling behind modal)
- [ ] Closes with smooth exit animation
- [ ] On close: focus returns to the trigger element that opened it

### Dropdowns and Selects
- [ ] Opens with keyboard (Enter/Space on trigger)
- [ ] Arrow keys navigate options
- [ ] Enter/Space selects; Escape closes without selecting
- [ ] Selected option indicated (checkmark, highlight)
- [ ] Long lists: virtualized or searchable (>10 options)

### Navigation
- [ ] Active state: current page clearly indicated (color + weight, not just underline)
- [ ] Hover state on all nav items
- [ ] Keyboard: Tab navigates, Enter activates
- [ ] Mobile: back button behavior predictable

### Tables and Lists
- [ ] Row hover state (if rows are interactive)
- [ ] Selected row state (if multi-select)
- [ ] Empty state: message + CTA (never just blank)
- [ ] Loading state: skeleton rows (not spinner for content areas)
- [ ] Sort: arrows indicate current sort direction + which column
- [ ] Bulk actions: only appear when items are selected

---

## Feedback Timing

The right feedback arrives at the right speed:

| Interaction | Max Response Time | Feedback Required |
|-------------|-----------------|-------------------|
| Button click | Instant (< 100ms) | Visual press state |
| Form submission start | Instant | Button enters loading state |
| API response (< 1s) | As data arrives | Success/error state |
| API response (1–3s) | Immediately | Loading indicator (spinner or skeleton) |
| API response (> 3s) | Immediately | Progress indicator with % or description |
| Background task | Immediately | "Working in background" + notification on complete |

**Never:** Leave the UI frozen with no feedback. The user will retry, creating duplicates.

---

## Animation Quality

Animations should aid comprehension, not decorate:

### Timing Rules (from UI UX Pro Max)
| Type | Duration | Easing |
|------|----------|--------|
| Hover / focus | 150ms | ease-out |
| Modal open | 200ms | ease-out |
| Modal close | 150ms | ease-in |
| Toast enter | 200ms | ease-out |
| Toast exit | 150ms | ease-in |
| Page transition | 250–300ms | ease-in-out |
| Skeleton shimmer | 1500ms | linear (loop) |

### Rules
- [ ] Max 1–2 animated elements per view (not everything animates simultaneously)
- [ ] Animate `transform` and `opacity` only — never `width`, `height`, `top`, `left`
- [ ] `transition: all` forbidden — list properties explicitly
- [ ] `prefers-reduced-motion: reduce` disables or minimizes all animations
- [ ] Animations interruptible — user input cancels mid-animation
- [ ] No infinite animations on decorative elements (content focus lost)

---

## Destructive Action Safeguards

Any action that deletes, archives, or permanently modifies data:

- [ ] Clearly labeled as destructive (red button, warning icon, "Delete" not "Remove")
- [ ] Requires confirmation before execution:
  - Modal: "Are you sure? This cannot be undone." + "Delete" + "Cancel"
  - OR: Undo window (5–10 seconds after action, with cancel option)
- [ ] Never immediate on first click
- [ ] After destructive action: clear confirmation message ("Patient record deleted")

---

## Error Recovery UX

Good errors tell the user exactly what happened and what to do next:

| Scenario | Bad | Good |
|----------|-----|------|
| Form validation | "Invalid input" | "Phone number must be 10 digits" |
| Network failure | "Error 500" | "Couldn't save — check your connection and try again" |
| Empty search | "No results" | "No patients named 'Rahul' — try a different spelling or ID" |
| Permission denied | "403 Forbidden" | "You don't have permission to view this patient's record" |
| Session expired | Silent redirect | "Your session expired — please sign in again" |

---

## Output Format

```
## Interaction Review: [feature / component name]

### Missing States
components/Button.tsx:12   [HIGH] loading state missing — double submission possible
  → Add: isLoading prop → disabled={isLoading} + aria-busy={isLoading} + <Spinner />

components/Input.tsx:34    [HIGH] error state present but no success state on validated field
  → Add: green border + check icon when field is valid after user interaction

### Feedback Timing
components/Form.tsx:88     [HIGH] no feedback between submit click and API response
  → Disable submit immediately on click; show loading state during request

### Animation Issues
components/Modal.tsx:6     [MED] no exit animation — modal disappears abruptly
  → Add: opacity 0 + scale 95 on exit, 150ms ease-in

components/Card.tsx:22     [MED] transition: all — should list properties explicitly
  → Change to: transition-colors duration-150 ease-out

### Destructive Actions
components/DeleteBtn.tsx:5 [HIGH] deletes immediately on click — no confirmation
  → Add confirmation modal or 5s undo window before executing delete

### Error Messages
components/SearchBar.tsx:67 [MED] empty state shows "No results" with no recovery path
  → Add: suggestion to clear filters or broaden search

### Passing
components/Dropdown.tsx     ✓ all states present, keyboard navigation correct
components/Toast.tsx        ✓ enter/exit animation correct, aria-live polite
```
