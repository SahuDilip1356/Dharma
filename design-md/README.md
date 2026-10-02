# design-md — Design Intelligence Engine

A Claude skill that does two things:

1. **APPLY** — packages **74 production-grade brand design systems** so a coding
   agent can generate UI in a chosen visual language (Linear, Stripe, Claude,
   Apple, Vercel, Ferrari, Notion, +67) instead of generic defaults.
2. **GENERATE** — uses a corpus analysis of those 74 systems + design laws + CRO
   laws to **curate a new, original, high-converting design** for a specific
   product: an original `DESIGN.md` token system plus a conversion-optimized page
   blueprint, self-scored against a design + CRO scorecard.

Each reference system is a `DESIGN.md` — a full token spec (color palette,
typography scale, spacing, radii, shadows, component rules).

## Structure

```
design-md/
├── SKILL.md                       # mode routing (Apply / Generate / Critique) + workflows
├── INDEX.md                       # catalog: 74 systems by category, with canvas + primary + essence
├── references/
│   └── <name>/DESIGN.md           # 74 token specs (load only the one(s) you need)
└── principles/                    # the "design brain"
    ├── corpus-analysis.md         # what the 74 systems measurably do (data-backed defaults)
    ├── design-principles.md       # visual-design laws + anti-slop checklist
    ├── cro-principles.md          # conversion laws + high-converting landing blueprint
    └── synthesis-playbook.md      # the GENERATE engine + self-critique scorecard
```

## Usage

**Apply mode** — "make it look like Linear", "Stripe-style landing page":
the agent scans `INDEX.md`, picks the closest system, loads only that
`references/<name>/DESIGN.md`, and applies the tokens.

**Generate mode** — "design a high-converting landing page for my product":
the agent runs `principles/synthesis-playbook.md` — intake the conversion goal,
learn from 2–3 exemplars, compose an original token system on corpus-backed
defaults, lay it out on the CRO blueprint, self-score, and ship a `DESIGN.md` +
blueprint (+ code).

Browse the catalog: [INDEX.md](INDEX.md). Start with the engine:
[principles/synthesis-playbook.md](principles/synthesis-playbook.md).

## The corpus, in numbers

Mined directly from the 74 systems (see `principles/corpus-analysis.md`): only
**1 of 64** structured systems uses drop-shadow tokens; **65%** of display
letter-spacing is negative; ~**half** use a monochrome primary; radii cluster on
a 4-based scale with pills; display headlines median **56px**. These are the
evidence-backed defaults the generator builds on.

## Source & license

Design systems sourced from
[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) /
[getdesign.md](https://getdesign.md) (MIT), using the DESIGN.md format pioneered
by Google Stitch. The corpus analysis, principles, and synthesis engine were
authored by Dilip Sahu on top of that library.

The reference systems are inspired interpretations of public brand languages for
building your own product UI — not official brand assets, and not for
impersonating a brand.
