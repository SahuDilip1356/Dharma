# Corpus Analysis — What 74 Best-in-Class Systems Actually Do

This is the empirical backbone of the skill. The patterns below were **mined
directly from the 74 DESIGN.md files** in `references/`, not asserted from
general design lore. When you synthesize a new design, these are the defaults
the best brands converge on — deviate only with a reason.

## The numbers (measured across the corpus)

| Finding | Data | What it means for you |
|---|---|---|
| **Shadows are nearly extinct** | Only **1 of 64** structured systems defines shadow/elevation tokens | Premium UI separates surfaces with **hairline borders + subtle background-tint layering**, not drop shadows. Default to `box-shadow: none`. A drop shadow is a tell of generic/AI design. |
| **Tight display tracking is the signature** | **65%** of display letter-spacing values are negative; tightest −5.5px | Large headlines get **negative letter-spacing** (roughly −0.02em to −0.04em). Body stays at 0 or slightly negative. Never track display type loose. |
| **One voltage, often achromatic** | ~**half** of primaries are monochrome (black/white/gray); rest skew blue/violet (14), red/orange (9), green (6), magenta (5) | Most systems commit to a **single accent color used sparingly** — and nearly half make the primary CTA literally black or white. Restraint reads as premium. |
| **Confident, large display type** | Display sizes 40–144px, **median 56px** | Heroes are big. Don't be timid — the median hero headline is ~56px, scaling to 80–144px on large display. |
| **A 4px-based radius scale, plus pills** | Pill (9999px) used 86×; then 8, 4, 6, 0, 12, 16px | Radii cluster on a **4-based scale**. Buttons are frequently **fully pill-rounded**. Sharp 0px corners appear in 38 places — sharpness is a deliberate, valid choice (editorial/luxury). |
| **Restrained weight range** | Weights 400 (311×), 500 (236×), 600 (158×), 700 (132×); 300 rare, 900 almost never | Live in **400 / 500 / 600 / 700**. Medium (500) is the workhorse for UI labels and CTAs. Ultra-thin (300) and black (900) are exceptions, not defaults. |
| **Rich palette, sparse use** | ~**23 color tokens** per system on average | Define many tokens (surfaces, inks, hairlines, semantics) but **paint with few** — most of the page is canvas + ink + hairlines; color is an event. |
| **Canvas: light dominates marketing, dark signals craft** | 45 light vs 9 dark among captured (more dark exist in prose-format files like Tesla, Spotify, Lamborghini) | Light canvas is the safe, broad default. **Near-black canvas (#0a0a0a–#121212, not pure #000)** is the move for developer-tools, luxury, and "software craft" positioning. |

## Cross-cutting patterns (qualitative, observed in the files)

1. **Single voltage color.** Nearly every system names exactly one brand accent
   ("voltage") and uses it only on primary CTAs, focus rings, links, and one or
   two brand moments. Linear's lavender, Stripe's indigo, Supabase's emerald,
   ClickHouse's yellow. The discipline *is* the brand.

2. **Surface layering over shadow.** Dark systems stack `canvas → surface-1 →
   surface-2 → surface-3` as progressively lighter near-black tints, separated by
   `hairline` borders (e.g. Linear: canvas `#010102`, surfaces `#0f1011`/`#141516`,
   hairline `#23252a`). Light systems do the inverse with faint warm/cool tints.

3. **Near-black, not pure black; off-white, not pure white.** The best dark
   canvases are `#0a0a0a`–`#121212`; the best light canvases carry a faint warm or
   cool tint (Claude `#faf9f5`, Cursor `#f7f7f4`, Intercom `#f5f1ec`). Pure
   `#000`/`#fff` reads cheap. Reserve true black/white for ink and voltage.

4. **Type does the heavy lifting.** With shadows and decoration stripped, the
   visual interest comes from a **strong type scale** — big tracked-tight display,
   a clear step down to body, and a mono face for technical credibility. Many
   systems ship a custom display face (substitute a close web font and note it).

5. **Generous whitespace + a clear rhythm.** Sections breathe. Vertical rhythm is
   built on a consistent spacing scale (commonly a 4/8px base). Density is a
   choice: SaaS/dev tools run tighter; luxury/editorial run airy.

6. **Photography or product UI as the hero, not stock illustration.** Consumer and
   luxury brands lead with full-bleed photography; dev tools lead with framed
   product screenshots. Decorative stock art is largely absent.

7. **Restraint is the throughline.** Across categories, "premium" correlates with
   *fewer* colors, *fewer* effects, *tighter* type, and *more* space — not more
   ornament. This is the single most transferable lesson in the corpus.

## How to use this file

When you build a new system in [synthesis-playbook.md](synthesis-playbook.md),
start from these convergent defaults and adjust per the product's positioning.
Every default here is a safe, evidence-backed starting point that already reads
as "designed by someone who knows what they're doing."
