---
name: frontend-design
description: |
  Aesthetic code generation — creates distinctive, production-grade frontend interfaces
  with intentional visual character. Bridges Phase 1 design decisions into Phase 3
  implementation by translating the design brief (style, colors, fonts from
  uiux-design-intelligence) and design tokens (from uiux-frontend-design-system)
  into visually striking, non-generic React/HTML/CSS code.

  Triggers at Phase 3 (Build) when:
  - Implementing a new user-facing screen, component, page, or flow
  - A design brief + design system tokens already exist from Phase 1
  - The task involves UI styling, visual beautification, or aesthetic lift
  - superpowers-execute delegates aesthetic code generation to a subagent

  Complements (does NOT replace):
  - uiux-design-intelligence chooses the aesthetic (style/color/font) — frontend-design executes it
  - uiux-react-patterns handles UX patterns, forms, accessibility (runs after frontend-design)
  - react-best-practices handles performance optimization (runs after frontend-design)
  - uiux-design-qa validates visual fidelity at Phase 5

  Source: https://github.com/anthropics/skills (adapted for Dharma by Dilip Sahu)
license: MIT
metadata:
  author: Anthropic (adapted for Dharma by Dilip Sahu)
  version: "1.0.0"
---

# Frontend Design — Aesthetic Code Generation

**This skill generates the code. `uiux-design-intelligence` made the aesthetic decision. Execute it with precision.**

The gap this fills: Dharma's design layer decides *what* the UI should look like (styles, palettes, fonts, tokens). This skill executes that decision into actual code with genuine visual character — not generic AI output.

---

## Dharma Phase Placement

| Phase | Role |
|---|---|
| Phase 1 — Design | **Consumes** output from `uiux-design-intelligence` + `uiux-frontend-design-system` |
| Phase 3 — Build | **Primary phase** — aesthetic code generation, runs before react-best-practices + uiux-react-patterns |
| Phase 5 — Finish | Aesthetic direction statement passed to `uiux-design-qa` for fidelity validation |

---

## Agent Calling Position in Phase 3

`superpowers-execute` orchestrates Phase 3 as a sequential chain — `frontend-design` runs **first** because subsequent agents need generated code to optimize.

```
Phase 3 agent chain (for UI features):

  Step 3a — frontend-design (this skill)
    Input:  design brief (style + palette + fonts) from uiux-design-intelligence
            design tokens (CSS variables) from uiux-frontend-design-system
            UX states + flows from uiux-designer
    Output: aesthetic React/HTML/CSS code + aesthetic direction statement

  Step 3b — in parallel, after 3a completes:
    Agent → react-best-practices    (performance optimization on generated code)
    Agent → uiux-react-patterns     (UX patterns, forms, accessibility on generated code)
    Agent → superpowers-tdd         (write tests against the generated code)

  Step 3c — superpowers-verify synthesizes 3a + 3b outputs
```

**Never run `react-best-practices` or `uiux-react-patterns` before `frontend-design`** — they need code to optimize and pattern-check. If there's no code yet, this skill generates it first.

---

## What to Consume from Phase 1

Before writing any code, read and internalize the Phase 1 outputs:

**From `uiux-design-intelligence` output:**
- Chosen style (e.g. "soft UI evolution", "editorial brutalism", "luxury minimal")
- Color palette (primary, secondary, CTA, background, text hex values)
- Typography pair (display font + body font + Google Fonts import)
- Motion timing (transition durations, easing)

**From `uiux-frontend-design-system` output:**
- CSS custom properties (color tokens, spacing scale, radius, shadow, motion)
- Component inventory (what already exists — don't rebuild)
- Consistency contract (rules that cannot be broken)

**From `uiux-designer` output:**
- User flows
- 4-state coverage plan: loading / empty / error / success

If Phase 1 output doesn't exist, **stop and request it** before proceeding. Do not invent a design direction mid-implementation.

---

## Step 1: Commit to the Aesthetic Direction

Before writing code, output an explicit aesthetic direction statement:

```
Aesthetic Direction
──────────────────────────────────────────────────
Style:       [style name from design brief]
Palette:     Primary [#hex] / Accent [#hex] / BG [#hex]
Typography:  [Display font] + [Body font]
Character:   [One sentence — what makes this unforgettable]
Anti-patterns avoided: [3 specific generic choices rejected]
──────────────────────────────────────────────────
```

This statement is:
- Used by `uiux-design-qa` at Phase 5 to validate visual fidelity
- Added to the evidence ledger as Phase 3 entry evidence
- Shared with `uiux-react-patterns` so accessibility patterns don't override the visual intent

---

## Step 2: Design Thinking Before Code

Answer these before writing a single line:

1. **Purpose**: What problem does this interface solve? Who is looking at it?
2. **Tone**: Which extreme fits the context? (refined luxury, brutal minimal, warm editorial, clinical precision, etc.)
3. **The one thing**: What is the single visual element someone will remember?
4. **Constraints**: Framework (React/Next.js), existing tokens, state requirements

**CRITICAL**: Intentionality over intensity. Bold maximalism and quiet minimalism both work — the failure mode is neither (undefined middle).

---

## Step 3: Generate Aesthetic Code

Implement production-grade code (React TSX, HTML/CSS, or as specified) that:
- Uses the design tokens from `uiux-frontend-design-system` as CSS variables (never hard-code raw hex values)
- Matches the exact style, palette, and typography from the design brief
- Covers all 4 required states: loading skeleton, empty state, error message, success confirmation
- Has genuine visual character — not a template, not a starter kit reskin

### Typography Rules

```css
/* ✅ Distinctive: chosen from design brief */
font-family: var(--font-display);  /* e.g. 'Cormorant Garamond', serif */
font-family: var(--font-body);     /* e.g. 'Montserrat', sans-serif */

/* ❌ Never use these — generic AI defaults */
font-family: Inter, system-ui, -apple-system;
font-family: Roboto, Arial, sans-serif;
font-family: 'Space Grotesk', sans-serif; /* overused across generations */
```

### Color Rules

```css
/* ✅ Always use design tokens */
color: var(--color-primary);
background: var(--color-bg);
border-color: var(--color-border);

/* ❌ Never hard-code in components */
color: #6366f1;            /* bypasses token system */
background: #ffffff;       /* not from design system */
```

### Motion Rules

```css
/* ✅ From design-intelligence output — specific, purposeful */
transition: all var(--motion-duration) var(--motion-ease);
animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;

/* ❌ Generic defaults */
transition: all 0.3s ease;  /* no character */
animation: none;            /* dead interface */
```

### Spatial Composition Rules

- Avoid symmetrical, centered-everything layouts — they read as "AI default"
- Use asymmetry intentionally: off-center headers, bleeding images, diagonal dividers
- Generous negative space OR intentional density — never accidental in-between
- Grid-breaking elements for hero moments (a card that overlaps a section boundary, etc.)

### Anti-AI-Slop Checklist

Before outputting code, verify none of these are present:

```
[ ] Purple gradients on white background — the most common AI aesthetic
[ ] Inter/Roboto/Arial as the primary font
[ ] Symmetrical hero with centered h1 + subtitle + CTA button
[ ] Blue-on-white color scheme with no character
[ ] Card grid with identical padding, border-radius, box-shadow on every card
[ ] Generic loading spinner (replace with skeleton that matches layout)
[ ] Empty state = just text with no visual treatment
```

---

## Step 4: 4-State Coverage

Every component must handle all 4 states with intentional visual design — not afterthoughts:

| State | What good looks like |
|---|---|
| **Loading** | Skeleton that mirrors the actual layout shape — same grid, same proportions, pulsing with the palette's neutral |
| **Empty** | Branded empty state — illustration or icon in the palette, copy that feels like the product voice |
| **Error** | Error message styled with the palette's accent, inline near the failure point, actionable (retry button) |
| **Success** | Confirmation with motion — a subtle entrance animation or color wash that feels satisfying |

---

## Step 5: Output Aesthetic Direction Statement for Phase 5

After generating code, output:

```
✅ Aesthetic Code Generated
────────────────────────────────────────────────────
Component:   [what was built]
Style:       [style name]
Distinctive choice: [the one thing that makes it memorable]
Token compliance: All colors/spacing from CSS variables ✅
4-state coverage: loading ✅ | empty ✅ | error ✅ | success ✅
Anti-slop check: [3 generic patterns that were specifically rejected]

Pass to uiux-react-patterns: [list any accessible pattern needs flagged]
Pass to react-best-practices: [list any performance concerns flagged]
Pass to uiux-design-qa: Aesthetic direction statement above for fidelity check
────────────────────────────────────────────────────
```

---

## Routes

**Mandatory for:** Route A (New Product), Route D (UI/UX Design or Redesign)
**Mandatory if user-facing:** Route B (New Feature)
**Not used for:** Route C (Bug Fix), Route E (Refactor), Route F (Performance), Route G (Security), Route H (Release)

---

## Ownership Boundaries

| Owns | Does NOT Own |
|---|---|
| Translating design brief + tokens into aesthetic, non-generic UI code | Choosing the aesthetic direction — style, colors, fonts (that is `uiux-design-intelligence`) |
| Anti-AI-slop visual intentionality — distinctive typography, composition, motion | UX patterns, form design, accessibility (that is `uiux-react-patterns`) |
| 4-state visual design (loading/empty/error/success appearance) | Performance optimization — waterfalls, bundle, re-renders (that is `react-best-practices`) |
| Design token compliance — using CSS variables, never raw hex | Final visual QA — design-to-implementation fidelity (that is `uiux-design-qa`) |
| Outputting aesthetic direction statement for Phase 5 | Test writing (that is `superpowers-tdd`) |

**Disambiguation from `uiux-design-qa`:**
- `frontend-design` generates code with visual intent at Phase 3
- `uiux-design-qa` validates at Phase 5 whether the generated code actually matches the design brief
- They run at different phases and answer different questions — neither replaces the other

**Disambiguation from `uiux-react-patterns`:**
- `frontend-design` runs first — it creates the code
- `uiux-react-patterns` runs after — it applies UX/form/accessibility patterns to that code
- Sequence matters: generate → then pattern-check → then performance-check
