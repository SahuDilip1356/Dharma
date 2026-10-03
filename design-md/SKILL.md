---
name: design-md
description: |
  Design-intelligence engine with 74 production-grade brand design systems plus
  design and conversion (CRO) principles. APPLIES a known visual language or
  GENERATES an original, high-converting design system and page blueprint. Use
  when the user wants UI "in the style of" / "like" a known brand ("make this look
  like Linear", "Stripe-style landing page", "dark like Vercel"); wants a new
  design, landing page, or site that looks great and converts ("design a
  high-converting landing page", "improve CRO of this page"); wants to pick, apply,
  or browse a design system or aesthetic; or wants a design critique grounded in
  real principles. Not for backend/non-visual work, users with their own complete
  design system, or full brand identity (logo/name/voice) creation.
license: MIT
metadata:
  author: Dilip Sahu
  source: "VoltAgent/awesome-design-md (github.com/VoltAgent/awesome-design-md) & getdesign.md — DESIGN.md collection (Google Stitch format), extended with a corpus analysis, design-principles, CRO-principles, and a synthesis playbook."
  version: "2.0.0"
  systems: 74
---

# design-md — Design Intelligence Engine

A library of 74 real-world brand design systems (one `DESIGN.md` token spec each)
plus principle files — corpus analysis, design laws, CRO laws and a synthesis playbook —
for composing an original, high-converting design. Each system's identity lives in its
specifics: one accent "voltage" color, light/dark canvas, type scale and tracking, radii
and shadow discipline, component rules.

## Pick the mode first

Route the request before doing anything:

- **APPLY** — the user names a brand/product to look like, or wants a specific
  known aesthetic. → Use the **Apply workflow** below.
- **GENERATE** — the user wants a *new* design / landing page / site that should
  look great **and convert**, or wants to improve a page's conversion. → Run the
  **Generate workflow** (`principles/synthesis-playbook.md`). This is the deep
  path: it composes an original system from the library + principles, not a copy.
- **CRITIQUE** — the user wants a design judged. → Score it with the scorecard in
  `principles/synthesis-playbook.md` (Step 5), grounded in the design + CRO
  principle files.

When in doubt between Apply and Generate: if they named a brand, Apply; if they
described a product and a goal, Generate. If the user already has their own
complete tokens, defer to those.

## The knowledge base

The skill's depth lives in `principles/` — read what the task needs:

- **[principles/corpus-analysis.md](principles/corpus-analysis.md)** — what the 74
  systems *measurably* do (shadows extinct, tight display tracking, one voltage,
  4-based radii…). The evidence-backed defaults.
- **[principles/design-principles.md](principles/design-principles.md)** — the
  visual-design laws + an anti-slop checklist.
- **[principles/cro-principles.md](principles/cro-principles.md)** — conversion
  laws: the 5-second contract, persuasion levers, friction reduction, the
  high-converting landing-page blueprint.
- **[principles/synthesis-playbook.md](principles/synthesis-playbook.md)** — the
  end-to-end engine for GENERATE, with the self-critique scorecard.

---

## APPLY workflow — build in a known brand's language

### 1. Identify the target aesthetic
Either the user names a brand directly, or they describe a feeling. Translate the
feeling into a candidate system.

### 2. Pick from the index — never read all 74
Open **[INDEX.md](INDEX.md)**. It lists every system grouped by category with its
**canvas** (light/dark), **primary voltage** color, and a one-line essence. Scan
it, pick the best match. If two are close, name both to the user and pick a
default; don't read both full files to decide — the index is enough.

### 3. Load only the chosen system
Read `references/<name>/DESIGN.md` (e.g. `references/linear.app/DESIGN.md`).
Each file is ~20–35 KB of structured tokens. Load **one**. Loading several at
once wastes context and blends incompatible languages.

### 4. Apply the tokens faithfully
When generating UI, treat the DESIGN.md as a contract, not inspiration:
- **Colors** — use the exact hex tokens. Respect the canvas (don't put a dark
  system on a white page). Use the primary as the *single* accent — most of
  these systems are deliberately restrained; one voltage color, used sparingly.
- **Typography** — match the named scale (display / headline / body / caption),
  including weights, line-heights, and letter-spacing. Tracking is often the
  signature; don't drop it. Substitute a close web/system font when the brand
  font isn't licensable, and say so.
- **Spacing, radii, shadows** — pull from the system's scale. Many of these
  brands are defined as much by their restraint (hairline borders, near-zero
  shadows) as by color.
- **Component rules** — follow documented patterns for buttons, cards, inputs,
  and layout rhythm.

### 5. (Optional) Persist the contract
If this UI work continues across sessions or hands off to other agents, copy the
chosen `DESIGN.md` into the target repo (root or `docs/`). That makes the design
language durable and lets any future coding agent stay consistent.

---

## GENERATE workflow — curate a new high-CRO design

This is the deep mode: synthesize an **original** design system and a
conversion-optimized layout for a specific product. Follow
**[principles/synthesis-playbook.md](principles/synthesis-playbook.md)** in full.
The short version:

1. **Intake** — product, audience, the *one* conversion goal, 3 positioning
   adjectives, brand constraints, surface type, trust requirements. Infer what
   you can; state assumptions.
2. **Select 2–3 exemplars** from [INDEX.md](INDEX.md) matching the category AND
   vibe. Read only those full `DESIGN.md` files. Borrow one move from each —
   never clone one.
3. **Compose original tokens** on the corpus-backed defaults
   (`principles/corpus-analysis.md`): tinted canvas, one voltage, hairlines not
   shadows, modular type scale with tight display tracking, 4-based radii. Output
   a real **`DESIGN.md`**.
4. **Lay out for conversion** with `principles/cro-principles.md`: the 5-second
   above-the-fold contract, the landing blueprint, proof + risk-reversal at every
   ask, mobile behavior per section.
5. **Self-score** against the design + CRO scorecard (playbook Step 5). **Fix any
   dimension under 7** before presenting. Report the final scores.

**Deliverable:** a synthesized `DESIGN.md` (the contract) + a section-by-section
page blueprint + a short rationale (which exemplars, the core design bet, the CRO
levers) + code if asked. The design is original and conversion-aware — not a
template, not a clone.

## Picking by vibe — quick map

| You want… | Reach for |
|---|---|
| Dark, technical, software-craft | `linear.app`, `vercel`, `framer`, `warp`, `x.ai` |
| Clean fintech / trust | `stripe`, `coinbase`, `wise`, `mastercard` |
| Warm editorial | `claude`, `intercom`, `cursor`, `replicate`, `elevenlabs` |
| Gallery / photography-first minimal | `apple`, `tesla`, `nike` |
| Cinematic luxury (dark) | `ferrari`, `lamborghini`, `bugatti`, `bmw-m` |
| Friendly, illustration-rich SaaS | `notion`, `miro`, `slack`, `zapier`, `clay` |
| Bold single-voltage on dark | `clickhouse`, `binance`, `composio`, `nvidia` |
| Retro nostalgia | `dell-1996`, `nintendo-2001`, `playstation` |

For everything else, scan [INDEX.md](INDEX.md).

## Notes

- These are *inspired interpretations* of public brand languages for building
  your own product UI — not official brand assets, and not for impersonating a
  brand. Swap brand colors/fonts for your own once the structure is in place if
  the product isn't that brand.
- Source: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md),
  MIT-licensed, DESIGN.md format pioneered by Google Stitch.
