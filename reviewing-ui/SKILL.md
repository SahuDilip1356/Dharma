---
name: reviewing-ui
description: |
  Reviews built UI before it ships: accessibility (WCAG, keyboard, screen reader),
  responsive behavior at 375/768/1280/1440px, interaction states and feedback, guideline
  compliance, and final visual QA with a ship/hold call. Use when a user-facing feature
  reaches verification, or when the user says "review my UI", "a11y audit", "check
  mobile", "check states", "design QA", or "does this look right". Outputs file:line
  findings sorted by severity.
license: MIT
metadata:
  author: Dilip Sahu
  version: "2.0.0"
---

# Reviewing UI

Run the reviews in this order. Each file holds its own checklist and output format.

| Review | Read |
|---|---|
| 1. Guideline audit — 18 rule categories (focus, forms, dark mode, i18n…) | [audit.md](audit.md) |
| 2. Accessibility — WCAG, keyboard, ARIA, contrast | [accessibility-review.md](accessibility-review.md) |
| 3. Responsive — behavior per breakpoint | [responsive-review.md](responsive-review.md) |
| 4. Interaction — states, transitions, feedback, destructive-action safeguards | [interaction-review.md](interaction-review.md) |
| 5. Final visual QA — screenshot check against intent, ship/hold call | [design-qa.md](design-qa.md) |

For a quick review, run only the steps the change touches. Step 5 always runs last,
and only after steps 2 and 3 pass.

## Output

```
[severity] file:line — rule violated — exact fix
```

Severity order: critical (ship blocker) → serious → moderate → minor.
