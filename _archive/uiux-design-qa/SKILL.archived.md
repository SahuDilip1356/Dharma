---
name: uiux-design-qa
description: |
  Final visual quality assurance — the last gate before any user-facing feature ships.
  Screenshot-based inspection against design intent, visual consistency, and polish standards.
  Triggers when:
  - A user-facing feature has passed all other verification gates and is ready to ship
  - User says "design QA", "visual QA", "final review", "does this look right", "check before PR"
  - lifecycle-orchestrator routes A, B, D reach Phase 5 (Finish Gate) for user-facing work
  - After accessibility-review and responsive-review have both passed

  Output: Structured QA report — critical visual issues, consistency gaps, polish notes,
  and a final ship/hold recommendation.

license: MIT
metadata:
  author: Dilip Sahu
  source: Anthropic enterprise-uiux-designer pattern + UI UX Pro Max
  version: "1.0.0"
---

# Design QA — Final Visual Inspection

**This is the last gate.** It runs after code is complete, accessibility passes, and responsive review passes. Its job is to catch what automated checks cannot: visual inconsistency, polish gaps, and intent drift.

---

## How to Run Design QA

### Step 1: Capture Screenshots
Take screenshots at:
- `375px` — mobile
- `768px` — tablet
- `1280px` — desktop

For each major state:
- Default (with realistic content — not Lorem ipsum)
- Loading (skeleton or spinner)
- Empty state
- Error state
- Success/completed state

### Step 2: Compare Against Design Intent
If a spec or design direction exists (from `uiux-designer` Phase 1 output), compare directly.
If no spec exists, compare against the project's established visual system.

### Step 3: Run All 14 QA Checks Below

---

## The 14 QA Checks

### 1. Visual Hierarchy
- [ ] The most important element is visually dominant
- [ ] Secondary elements are clearly subordinate
- [ ] There is one clear CTA — not competing CTAs of equal weight
- [ ] The eye knows where to go first, second, third

**Failure signal:** Everything looks equally important. The page has no clear focal point.

### 2. Spacing Rhythm
- [ ] Spacing is consistent — elements use the same 4px-scale values throughout
- [ ] Related elements grouped closer; unrelated elements have more breathing room
- [ ] No cramped areas (elements touching or < 8px apart when they shouldn't be)
- [ ] No islands of excessive white space that break visual flow

**Failure signal:** Some sections are cramped, others have too much space. No rhythm.

### 3. Typography
- [ ] Heading hierarchy is clear — h1 visually larger than h2, h2 visually larger than h3
- [ ] Max 3 font weights used on the page
- [ ] Body text is readable (16px+, 1.5 line height, max 75ch)
- [ ] No walls of text — long content broken with headings, lists, or white space
- [ ] `…` ellipsis character (not `...`) for truncated text

**Failure signal:** Headings same size as body text. Or five different font weights.

### 4. Color Consistency
- [ ] Only tokens from the design system used (no ad-hoc hex values)
- [ ] Primary color used for primary actions only — not decorative elements
- [ ] Error red only on error states — not warnings or neutral states
- [ ] Dark mode: all surfaces correctly themed (no light elements on dark background)

**Failure signal:** Primary blue used on decorative borders. Error red used on info badges.

### 5. Component Consistency
- [ ] Same component variant used for same purpose across the feature
- [ ] Button sizes consistent within a context (don't mix sm and lg in the same form)
- [ ] Border radius consistent — cards don't mix 8px and 12px
- [ ] Icon sizes consistent — 16px icons and 24px icons not mixed without reason

**Failure signal:** Same type of action uses different button variants on different screens.

### 6. Realistic Content Test
- [ ] UI tested with realistic data length (long names, long addresses, long email addresses)
- [ ] No Lorem ipsum in the implementation
- [ ] Number formatting: "1,234" not "1234"; "₹1,234.00" not "1234"
- [ ] Date formatting: "27 Apr 2026" or "Apr 27, 2026" — locale-appropriate

**Failure signal:** Layout breaks when "Thiruvananthapuram General Hospital" is the clinic name.

### 7. Empty States
- [ ] Every list, table, or data view has an empty state
- [ ] Empty state includes: illustration or icon + message + primary action CTA
- [ ] Message is helpful ("No appointments today — schedule one") not generic ("No data")
- [ ] Empty state does not look like a loading state

**Failure signal:** List renders nothing. No message. User thinks the page is broken.

### 8. Loading States
- [ ] Skeleton screens used for content areas (not spinners for whole-page content)
- [ ] Skeleton matches the approximate shape of the content it replaces
- [ ] Loading state does not cause layout shift when content arrives
- [ ] Buttons show spinner during async operation

**Failure signal:** Page goes blank then content appears, causing CLS. Or spinner alone with no skeleton.

### 9. Error States
- [ ] Error messages explain what happened and what to do
- [ ] Error messages appear near the source of the error (inline, not top-of-page only)
- [ ] Retry action available when appropriate
- [ ] Error state does not break layout or overflow containers

**Failure signal:** "Something went wrong" with no next step and no retry.

### 10. CTA Clarity
- [ ] Primary CTA is the most visually prominent button on the screen
- [ ] CTA label is specific to the action ("Book Appointment" not "Continue")
- [ ] No more than one primary CTA per screen section
- [ ] Destructive actions visually distinguished (red or outlined — not primary style)

**Failure signal:** Three blue buttons on the same form. User unsure what to do.

### 11. Mobile Polish (at 375px)
- [ ] Content does not overflow or require horizontal scroll
- [ ] Touch targets large enough (44×44px minimum)
- [ ] Text readable without zooming
- [ ] Navigation accessible and collapsed appropriately
- [ ] Modals either full-screen or bottom sheet (not tiny desktop modal)

**Failure signal:** Desktop modal on mobile with text cut off and tiny close button.

### 12. Focus and Keyboard Indicators (Visual Check)
- [ ] Focus ring visible when tabbing through the interface
- [ ] Focus ring color contrasts clearly against background
- [ ] Active/hover states visible and intentional

**Failure signal:** Tab through the form and focus ring is invisible.

### 13. Microcopy and Labels
- [ ] Button labels in Title Case
- [ ] Error messages in sentence case
- [ ] Placeholders end with `…`
- [ ] Counts use numerals: "3 appointments" not "three appointments"
- [ ] Active voice: "Save changes" not "Changes will be saved"
- [ ] No jargon visible to end users (no "HTTP 500", no "null", no stack traces)

**Failure signal:** "Submit" button. "Error 422" message. Placeholder says "Enter value".

### 14. Generic AI UI Check
- [ ] No default purple/pink gradients without a defined visual direction reason
- [ ] No glassmorphism overuse (more than 2 layered blur surfaces on one screen)
- [ ] No icon clutter (icons only where they add information, not decoration)
- [ ] No identical-card grid layouts where all cards have equal visual weight
- [ ] Visual direction is intentional and consistent (matches design intelligence output)

**Failure signal:** The UI looks like every other AI-generated SaaS product.

---

## QA Report Format

```
## Design QA: [feature name]
Screenshots reviewed at: 375px / 768px / 1280px
States reviewed: default / loading / empty / error / success

### 🚫 Ship Blockers (Must Fix Before Merge)
[check #] [component] — [finding]
  → [specific fix]

### ⚠️ Fix Before PR (Polish Issues)
[check #] [component] — [finding]
  → [specific fix]

### 📝 Backlog (Note for Next Sprint)
[check #] [component] — [finding]
  → [specific fix]

### ✅ Passing
- Visual hierarchy: clear ✅
- Spacing rhythm: consistent ✅
- ...

### Final Recommendation
SHIP ✅ — All blockers resolved, Polish issues acceptable for this release.
  OR
HOLD ❌ — [N] ship blockers must be resolved first.
```

---

## QA Principles

1. **Be specific.** "The button is too small" is not a finding. "Button height 32px at 375px — below 44px touch target minimum" is.
2. **Test with real content.** Lorem ipsum hides the real layout problems.
3. **Check all states.** Most QA failures are on error and empty states, not the happy path.
4. **The goal is shippable, not perfect.** Ship blockers must be fixed. Polish notes are for the backlog.
