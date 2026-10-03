# Reviewing-UI Skill Test — Haiku 4.5

## Q1

**Files read:** SKILL.md, audit.md (referenced for guideline categories), accessibility-review.md, responsive-review.md, interaction-review.md, design-qa.md

### What I would do

For a consent banner component before shipping, I'd run a full five-step review:

**1. Guideline Audit** — Check focus management, form labeling, dark mode support, keyboard navigation, color contrast, i18n readiness (since privacy policies vary by region).

**2. Accessibility** — WCAG 2.1 AA compliance: dialog role and focus trap, button labels ("Accept", "Decline"), no color-only differentiation, 44×44px minimum touch targets, keyboard escape to dismiss, arrow keys if multi-button.

**3. Responsive** — Test banner layout at 375px (mobile), 768px (tablet), 1280/1440px (desktop). Buttons must not stack under text on mobile, scroll not required, dismiss button reachable on touch.

**4. Interaction** — Verify hover/focus states (visible outlines), active button press feedback, loading state if consent tracking delays, Escape and Enter keyboard shortcuts, edge case: second dismissal or preference change.

**5. Final Visual QA** — Screenshot check: layout matches intent, text readable, all interactive states visible, no console errors. Ship/hold decision based on findings.

### Output format

Since no actual component exists, I'd produce findings like:
```
[critical] components/ConsentBanner.tsx:45 — dialog missing aria-label — add aria-label="Privacy consent"
[serious] components/ConsentBanner.tsx:62 — button 36×36px < 44px minimum — increase padding
[moderate] components/ConsentBanner.tsx:30 — dark mode text contrast 3.5:1 < 4.5:1 — lighten text
[minor] components/ConsentBanner.tsx:51 — no focus indicator on Decline button — add outline:2px on :focus-visible
```

---

## Q2

**Files read:** SKILL.md, responsive-review.md

### What I would do

For a mobile check at 375px, I'd focus the responsive-review step:

**Viewport & Layout** — Confirm `<meta viewport>` present, no horizontal overflow, content fits 375px width.

**Touch Targets** — All buttons/links 44×44px or larger. On a pricing page: CTA buttons, toggle switches (annual/monthly), expand/collapse tier details must be tap-friendly.

**Readability** — Font sizes ≥12px effective, line-height ≥1.5, text doesn't require horizontal scroll.

**Responsive Images** — Prices and feature icons scale appropriately, don't break layout.

**Pricing Page Specifics** — Tier cards stack vertically (not side-by-side), feature comparison tables either stack or scroll horizontally with context, price numbers prominent, CTAs remain tappable below fold.

### Output format

Findings would be:
```
[critical] components/PricingPage.tsx:78 — comparison table overflows 375px viewport — add horizontal scroll or stack rows
[serious] components/PricingCard.tsx:42 — "Choose Plan" button 40×40px < 44px minimum — increase height/width
[moderate] components/PricingPage.tsx:15 — price font-size 14px at 375px, hard to read on mobile — increase to 18px
```

---

## Q3

**Files read:** SKILL.md

### Outcome

**This request is outside the skill's scope.**

The reviewing-ui skill audits **built UI before shipping** — it reviews accessibility, responsiveness, interaction states, and visual correctness of existing components.

**This request asks me to design a new landing page from scratch**, which is a creative design task, not a review/verification task. The skill is not intended for that.

**Appropriate response to the user:** "I can review a landing page design after it's built—checking for accessibility, mobile responsiveness, interaction states, and shipping readiness. To design a new page, you'd use a design skill. Once you have a draft, bring it to me for review."

