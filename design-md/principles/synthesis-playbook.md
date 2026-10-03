# Synthesis Playbook — Curate a New High-CRO Design

## Contents

- [Step 0 — Intake (gather or infer the brief)](#step-0--intake-gather-or-infer-the-brief)
- [Step 1 — Select 2–3 exemplars (never copy one)](#step-1--select-23-exemplars-never-copy-one)
- [Step 2 — Derive the token system (apply corpus defaults)](#step-2--derive-the-token-system-apply-corpus-defaults)
- [Step 3 — Lay out for conversion (apply the CRO blueprint)](#step-3--lay-out-for-conversion-apply-the-cro-blueprint)
- [Step 4 — Produce the deliverable](#step-4--produce-the-deliverable)
- [Step 5 — Self-critique against the scorecard (before presenting)](#step-5--self-critique-against-the-scorecard-before-presenting)
  - [Design quality (0–10 each)](#design-quality-010-each)
  - [Conversion quality (0–10 each)](#conversion-quality-010-each)
  - [Scoring discipline](#scoring-discipline)
- [Quick reference: the synthesis in one line](#quick-reference-the-synthesis-in-one-line)

This is the engine. It turns the **exemplar library** (`references/`), the
**measured defaults** ([corpus-analysis.md](corpus-analysis.md)), the **design
laws** ([design-principles.md](design-principles.md)), and the **conversion laws**
([cro-principles.md](cro-principles.md)) into a *new, original* design system and
page blueprint tuned for a specific product and conversion goal.

You are not copying a brand. You are doing what a senior designer does: drawing on
a deep mental library of what works, then composing something coherent and
original for *this* problem.

---

## Step 0 — Intake (gather or infer the brief)

Lock these before designing. Ask only what you can't reasonably infer; state your
assumptions for the rest.

- **Product & category** — what it is, what it does.
- **Audience** — who decides, their sophistication, their context (B2B buyer,
  consumer, developer, patient…).
- **Primary conversion goal** — the *one* action this surface must drive
  (start trial / book demo / purchase / subscribe / sign up).
- **Positioning adjectives** — pick 3 (e.g. "trustworthy, fast, human";
  "premium, precise, cinematic"; "playful, approachable, simple").
- **Brand constraints** — existing logo, colors, fonts, name. Honor what exists.
- **Surface type** — marketing landing page / app dashboard / signup flow /
  pricing / docs. (Determines the blueprint.)
- **Trust requirements** — fintech/health/B2B need heavier trust + compliance.

## Step 1 — Select 2–3 exemplars (never copy one)

From [INDEX.md](../INDEX.md), choose **2–3** systems whose *patterns* fit the
positioning and category — not to clone, but to learn from:

- Match on **category** (a fintech learns from `stripe`/`coinbase`/`wise`) AND on
  **vibe** (the "premium, cinematic" axis might also pull from `ferrari`).
- Read **only** those 2–3 full `references/<name>/DESIGN.md` files. Note *why*
  each works: its canvas choice, voltage discipline, type strategy, layout rhythm.
- Synthesize across them. Borrowing one move from three systems = original.
  Copying all moves from one = derivative.

## Step 2 — Derive the token system (apply corpus defaults)

Compose an **original** token set, starting from the evidence-backed defaults and
bending them to the positioning:

- **Canvas** — light off-white for broad/approachable; tinted near-black
  (`#0a0a0a`–`#121212`) for craft/luxury/dev. Never pure `#000`/`#fff`.
- **Voltage** — pick ONE accent that fits the positioning and passes AA on the
  canvas. Honor brand color if one exists. Half the corpus uses a near-monochrome
  primary — restraint is safe.
- **Surfaces** — 2–4 tints layered off the canvas, separated by **hairlines**
  (no shadows by default).
- **Inks** — primary / muted / subtle, all AA-compliant.
- **Type** — 2 families max (display/UI sans + optional mono). Modular scale,
  display ≥40px with negative tracking, body 16–18px / 1.5. Substitute a
  licensable web font for any custom brand face and say so.
- **Radii** — one 4-based scale; decide pill vs. sharp from the positioning
  (pill = friendly/modern; 0px = editorial/luxury).
- **Spacing** — 4 or 8px base, applied everywhere.
- **Motion** — 120–240ms, purposeful only.

Output this as a real **DESIGN.md** (same frontmatter shape as the references:
`colors`, `typography`, `rounded`, plus spacing/motion). This becomes the
project's durable design contract.

## Step 3 — Lay out for conversion (apply the CRO blueprint)

Using [cro-principles.md](cro-principles.md), structure the surface around the
single conversion goal:

- Write the **above-the-fold contract**: value-prop headline, audience subhead,
  one dominant CTA (voltage color), product visual, trust strip.
- Order the sections (default landing blueprint in cro-principles.md), adapting to
  the surface type.
- Place **proof and risk-reversal** next to every ask.
- Define the **mobile behavior** of each section.
- Specify CTA copy (action + value, first-person where it fits) and where the CTA
  repeats.

## Step 4 — Produce the deliverable

Default output bundle (scale to what was asked):

1. **`DESIGN.md`** — the synthesized token system (the contract).
2. **Page blueprint** — section-by-section structure with the conversion goal,
   hero copy, CTA placement, proof points, and mobile notes.
3. **Rationale** — 4–6 lines: which exemplars informed it, the core design bet,
   and the primary CRO levers used.
4. **(If asked) Code** — implement the blueprint with the tokens. Hairline
   borders, tight display tracking, one voltage, no drop shadows.

## Step 5 — Self-critique against the scorecard (before presenting)

Score the design 0–10 on each dimension. **Anything below 7 gets revised before
you show the user.** Report the weak dimensions honestly.

### Design quality (0–10 each)
1. **Hierarchy** — is there one clear focal point and a deliberate reading order?
2. **Typography** — modular scale, confident display, negative display tracking?
3. **Color discipline** — one voltage used as an event; tinted (not pure)
   canvas?
4. **Depth & restraint** — hairlines over shadows; whitespace as structure?
5. **Consistency** — tokens and component patterns reused, not ad-hoc?
6. **Accessibility** — AA contrast, visible focus, semantic structure, ≥44px
   targets?
7. **Responsive** — every section's mobile behavior defined?
8. **Originality / anti-slop** — passes the anti-slop checklist; not a template?

### Conversion quality (0–10 each)
9. **5-second clarity** — what/for-whom/next-action answered above the fold?
10. **Single goal** — one primary CTA per viewport, dominant and repeated?
11. **Value proposition** — outcome-led, specific, customer-language?
12. **Proof & trust** — social proof + risk-reversal near the asks?
13. **Friction** — minimal form fields, low cognitive load, fast assets?
14. **Persuasion** — at least 2 honest levers (proof, authority, reciprocity…)
    applied without dark patterns?

### Scoring discipline
- **< 7 on any dimension → revise that dimension, then re-score.**
- Don't average away a failure: a beautiful page that fails "5-second clarity"
  is a failed page. Clarity and trust gate everything.
- Present the final scores with the deliverable so the user sees the trade-offs.

---

## Quick reference: the synthesis in one line

> Pick the conversion goal → learn from 2–3 exemplars → compose an original token
> system on corpus-backed defaults → lay it out on the CRO blueprint → self-score
> and fix anything under 7 → ship a `DESIGN.md` + blueprint (+ code).
