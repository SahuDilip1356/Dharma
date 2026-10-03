# Design Principles — The Laws Behind Good UI

## Contents

- [1. Hierarchy — guide the eye in a deliberate order](#1-hierarchy--guide-the-eye-in-a-deliberate-order)
- [2. Contrast — earn attention, ensure legibility](#2-contrast--earn-attention-ensure-legibility)
- [3. Color — one voltage, used as an event](#3-color--one-voltage-used-as-an-event)
- [4. Typography — the primary instrument](#4-typography--the-primary-instrument)
- [5. Space & rhythm — whitespace is structure, not emptiness](#5-space--rhythm--whitespace-is-structure-not-emptiness)
- [6. Depth — borders and layering, not shadows](#6-depth--borders-and-layering-not-shadows)
- [7. Consistency — a system, not a collection of screens](#7-consistency--a-system-not-a-collection-of-screens)
- [8. Motion — restraint and purpose](#8-motion--restraint-and-purpose)
- [9. Accessibility is design quality, not an add-on](#9-accessibility-is-design-quality-not-an-add-on)
- [10. Responsive — design the small screen as a first-class case](#10-responsive--design-the-small-screen-as-a-first-class-case)
- [The anti-slop checklist (what makes AI design look generic)](#the-anti-slop-checklist-what-makes-ai-design-look-generic)

Durable visual-design principles, organized for *application*, not theory. Pair
these with the measured defaults in [corpus-analysis.md](corpus-analysis.md).
Each principle ends with an operational rule you can act on.

## 1. Hierarchy — guide the eye in a deliberate order

Every screen should answer "where do I look first, second, third?" before color
or polish. Build hierarchy with **size, weight, color, and space** — in that
order of strength.

- One dominant element per view (the hero headline, the primary CTA).
- A clear 3-level type scale: display → heading → body. If everything is bold,
  nothing is.
- **Rule:** there is exactly **one** primary CTA per viewport. Everything else
  is secondary (outline/ghost) or tertiary (text link).

## 2. Contrast — earn attention, ensure legibility

Contrast creates focus and accessibility simultaneously.

- Body text vs. background: **≥ 4.5:1** (WCAG AA). Large text: ≥ 3:1. Never ship
  light-gray body on white "because it looks minimal" — it fails AA and tanks
  readability.
- The voltage color should be the highest-contrast interactive element on the
  page so the CTA wins the eye.
- **Rule:** check every text/background pair against AA. Muted ≠ illegible.

## 3. Color — one voltage, used as an event

The corpus is decisive here: **one accent, applied sparingly.**

- Structure the palette as: **canvas → surfaces (1–4) → inks (primary/muted/
  subtle) → hairlines → one voltage → semantic (success/warn/error)**.
- 90% of the page is canvas + ink + hairline. Color appears on CTAs, focus,
  links, and one brand moment. More color ≠ more design.
- Near-black canvas, not `#000`. Off-white canvas, not `#fff`. (See corpus.)
- **Rule:** if the voltage color appears more than ~3 distinct *roles* on a
  screen, you're diluting it.

## 4. Typography — the primary instrument

With decoration stripped, type carries the design.

- **Display:** large (≥40px, up to 144), weight 500–700, **negative tracking**
  (~−0.02 to −0.04em), line-height 1.0–1.2.
- **Body:** 16–18px, weight 400, line-height 1.5, tracking ~0, measure 60–75
  characters.
- Limit to **2 families** (a display/UI sans + optionally a mono for technical
  credibility). A serif display can signal editorial warmth (Claude).
- **Rule:** set a modular scale and snap every size to it. No one-off font sizes.

## 5. Space & rhythm — whitespace is structure, not emptiness

- Build everything on a consistent base unit (**4 or 8px**). All spacing,
  padding, and gaps are multiples.
- Group related elements tight, separate unrelated elements with generous gaps
  (proximity = relationship — Gestalt).
- Section padding should breathe: marketing sections commonly 80–160px vertical
  on desktop.
- **Rule:** never use arbitrary spacing values. If it's not on the scale, it's
  wrong.

## 6. Depth — borders and layering, not shadows

Corpus finding: **1 of 64 systems uses shadow tokens.** Premium depth comes from:

- **Hairline borders** (1px, low-contrast: a faint lighter line on dark, faint
  darker line on light).
- **Surface tint layering** — each elevation is a slightly different background
  tint, not a shadow.
- **Rule:** default `box-shadow: none`. If you genuinely need elevation (a
  popover, a dropdown), use the *smallest* possible shadow, once.

## 7. Consistency — a system, not a collection of screens

- Reuse tokens and components everywhere; identical things look identical.
- Establish patterns (button anatomy, card anatomy, input states) once and
  repeat. Variation should be meaningful, never incidental.
- **Rule:** before inventing a new component, check whether an existing pattern
  covers it.

## 8. Motion — restraint and purpose

- Motion clarifies state change (hover, focus, enter/exit), it doesn't decorate.
- Fast and subtle: 120–240ms, ease-out for entrances. Respect
  `prefers-reduced-motion`.
- **Rule:** if an animation doesn't communicate a state change or relationship,
  cut it.

## 9. Accessibility is design quality, not an add-on

- Visible focus states (the voltage color as a focus ring is common and good).
- Real semantic HTML, hit targets ≥ 44px, labels on inputs, alt text.
- Don't encode meaning in color alone.
- **Rule:** keyboard-navigate and AA-check the design before calling it done.

## 10. Responsive — design the small screen as a first-class case

- Most traffic is mobile. Reflow, don't shrink. Stack, increase tap targets,
  collapse nav.
- Display type scales down hard (a 96px hero becomes ~40px on mobile).
- **Rule:** specify the mobile behavior of every section, not just desktop.

## The anti-slop checklist (what makes AI design look generic)

Avoid these tells — they're the opposite of every system in the corpus:
- Drop shadows on cards. → Use hairline borders.
- Three+ gradients and a rainbow of accent colors. → One voltage.
- Pure `#000` / `#fff`. → Tinted near-black / off-white.
- Loose or default letter-spacing on big headlines. → Tighten display tracking.
- Timid 24–32px "hero" headlines. → Go ≥40px, confident.
- Inconsistent radii and ad-hoc spacing. → Snap to a scale.
- Center-everything with no clear hierarchy. → One focal point, deliberate order.
- Generic emoji/stock-illustration filler. → Real product UI or photography.
