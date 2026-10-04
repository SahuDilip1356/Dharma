---
name: designing-ui
description: |
  Designs and builds product UI — app screens, dashboards, forms, settings, onboarding
  flows: picks a visual direction, codifies it as design tokens and components, and
  implements distinctive, non-generic React/HTML/CSS. Use when building or redesigning
  in-app interfaces, when the user says "build UI", "make this screen better", "pick
  colors/fonts", or "create a design system", or when UI looks inconsistent. For
  marketing/landing pages or "make it look like Linear/Stripe" use design-md; for reviewing
  finished UI use reviewing-ui.
license: MIT
metadata:
  author: Dilip Sahu
  version: "2.0.0"
---

# Designing UI

Work through the steps in order. Read only the file for the step you're on.

| Step | Read |
|---|---|
| 1. Design process + quality rules (user goal, hierarchy, states) | [designer.md](designer.md) |
| 2. Choose the visual direction — style, palette, fonts, motion | [design-intelligence.md](design-intelligence.md) |
| 3. Codify it — tokens, component inventory, layout grid, spacing | [frontend-design-system.md](frontend-design-system.md) |
| 4. Implement with intentional visual character | [frontend-design.md](frontend-design.md) |
| 5. React/Next.js component patterns (forms, data fetching, boundaries) | [react-patterns.md](react-patterns.md) |

For React performance rules, use the `vercel:react-best-practices` skill.
Before presenting any UI, run the pre-flight check in [ai-tells.md](ai-tells.md) — it lists the patterns that make output look AI-generated.

When the build is done, hand off to `reviewing-ui`.
