## Q1

Files read: SKILL.md, INDEX.md, references/linear.app/DESIGN.md

**Mode: APPLY.** You named a brand, so I'm using the `linear.app` system as written. I'm not mixing it with anything else.

**Before I touch code, a few quick checks** (I'll go with the defaults below unless you tell me otherwise):
1. Does SubSense already have a logo or brand color that has to stay? Linear's system allows only **one** accent color. If SubSense has its own, it takes the place of Linear's lavender `#5e6ad2` and everything else stays the same.
2. Are you OK going fully dark? Linear has no light marketing mode, so the whole page goes dark.
3. Do you have real product screenshots? Linear's pages are built around framed product UI.

**Assumptions:** SubSense has no set brand color yet, so I'm using Linear's lavender. The page goes fully dark, and I'll put in screenshot placeholders where your product UI will go.

**Tokens to apply (exact values from the Linear DESIGN.md):**
```css
:root{
  --canvas:#010102; --surface-1:#0f1011; --surface-2:#141516; --surface-3:#18191a;
  --hairline:#23252a; --hairline-strong:#34343a;
  --ink:#f7f8f8; --ink-muted:#d0d6e0; --ink-subtle:#8a8f98; --ink-tertiary:#62666d;
  --primary:#5e6ad2; --primary-hover:#828fff; --primary-focus:#5e69d1; --success:#27a644;
  --r-xs:4px; --r-md:8px; --r-lg:12px; --r-xl:16px; --r-pill:9999px;
  --s-xs:8px; --s-md:16px; --s-lg:24px; --s-xl:32px; --s-xxl:48px; --s-section:96px;
  --font: "Inter", "SF Pro Display", -apple-system, system-ui, sans-serif; /* Linear's typeface is proprietary; Inter is the closest free match */
  --mono: "JetBrains Mono", ui-monospace, monospace;
}
```
Type scale: display-xl 80/1.05, weight 600, tracking −3px. display-lg 56/−1.8px. display-md 40/−1px. headline 28/−0.6px. card-title 22/500/−0.4px. body-lg 18. body 16/1.5. button 14/500. eyebrow 13/500/+0.4px.

**Page blueprint for SubSense:**
- **Top nav** (56px, `--canvas`): SubSense wordmark on the left, 4 links at most, then "Sign in" as a secondary button (surface-1 with a hairline border) and "Get started" as the primary lavender button. Below 768px the links collapse into a hamburger menu.
- **Hero:** display-xl headline in `--ink`, body-lg subhead in `--ink-muted`, one lavender primary CTA plus a tertiary text link. Underneath is a full-width `product-screenshot-card` (surface-1, 16px radius, 1px hairline) showing the SubSense dashboard. On mobile the headline drops from 80px to about 36px.
- **Logo strip:** customer logos about 24px tall in `--ink-subtle`, with no borders. 6 across, 3 across on mobile.
- **Feature sections:** each one opens with a screenshot. Feature cards go 3 across, then 2, then 1, on surface-1 with a 12px radius and 24px padding.
- **Testimonials:** surface-1 cards with 32px padding and body-lg text.
- **Pricing:** pill-shaped tab toggle, 3 tier cards, and the featured tier lifted to surface-2 with `--hairline-strong`.
- **CTA banner** (surface-1, 48px padding, headline type) → footer on `--canvas` in `--ink-subtle` captions.

**Rules I'll hold to:** no drop shadows (depth comes only from the surface steps and hairlines). Lavender appears only on the logo mark, the primary CTA, focus rings and link emphasis. No gradients and no second accent color. CTAs get an 8px radius and are never pill-shaped. The canvas is `#010102`, never pure `#000`. Focus is a 2px lavender ring at 50% opacity. Tap targets are at least 44px on touch.

**Note:** this borrows Linear's *visual structure* for SubSense's own product. Linear's logo, copy and screenshots stay out. If this work will continue or be handed off, I'd copy the DESIGN.md into `docs/DESIGN.md` so later work stays consistent with it.

## Q2

Files read: SKILL.md, principles/synthesis-playbook.md, INDEX.md, principles/corpus-analysis.md, principles/cro-principles.md, principles/design-principles.md, references/cal/DESIGN.md, references/intercom/DESIGN.md, references/stripe/DESIGN.md

**Mode: GENERATE** (a new design aimed at conversion, with no brand yet).

**Intake. Please confirm these; my working assumptions are in brackets:**
1. What's the product name, and what does it do? [Scheduling, intake and reminders for small outpatient clinics]
2. Who buys it? [Clinic owners or practice managers at 1–10 provider clinics, in the US]
3. What is the *one* action the page should drive? [Start a 14-day free trial, no card needed. If you sell through sales, I'd change this to "Book a 20-min demo"]
4. Which compliance claims are actually true for you (HIPAA plus a BAA, SOC 2)? I'll only show badges you confirm.
5. Pick 3 adjectives for the brand. [Calm, trustworthy, efficient]

**Reference systems, one idea from each:**
- **Cal:** calendar-first SaaS that shows small pieces of the real product inside cards.
- **Intercom:** a warm, tinted canvas and a restrained editorial feel.
- **Stripe:** handles trust at the level fintech needs, with tabular figures for numbers.

**Synthesized DESIGN.md (excerpt):**
```yaml
colors:
  canvas: "#f7f6f2"      # warm off-white; clinical without the cold hospital look
  surface-1: "#ffffff"
  surface-2: "#efeee8"
  hairline: "#dedcd4"
  ink: "#10202a"         # deep blue-ink
  ink-muted: "#4a5560"   # passes AA on canvas
  ink-subtle: "#6b7580"
  primary: "#0f766e"     # calm clinical teal, the only accent color (~5:1 contrast on canvas)
  primary-hover: "#0b5f58"
  on-primary: "#ffffff"
  success: "#15803d"; warning: "#b45309"; error: "#b91c1c"
typography:   # Inter for everything; tabular figures for times and stats
  display-xl: {size: 64px, weight: 600, lh: 1.05, tracking: -2px}
  display-lg: {size: 48px, weight: 600, lh: 1.1, tracking: -1.4px}
  display-md: {size: 36px, weight: 600, lh: 1.15, tracking: -0.8px}
  title: {size: 22px, weight: 600, tracking: -0.3px}
  body-lg: 18/1.5/400; body: 16/1.5/400; button: 15/500; caption: 13/500
rounded: {sm: 6px, md: 8px, lg: 12px, xl: 16px, pill: 9999px}  # buttons are pills (approachable); cards 12px
spacing: 4px base, scale 4 8 12 16 24 32 48 96
elevation: none. Depth = surface tint + 1px hairline
motion: 160ms ease-out, state changes only; respects prefers-reduced-motion
```

**Page blueprint:**
1. **Hero:** "Fewer no-shows. Fuller schedules. Less front-desk chaos." The subhead names who it's for: "Online booking, digital intake and automatic reminders for independent clinics, set up in an afternoon." The CTA is a teal pill reading "Start my free trial", with the risk reducers "No credit card · HIPAA-ready · Cancel anytime" right below it. The visual is the real UI: a day schedule with a reminder-sent chip. Trust strip: confirmed badges plus "Used by N clinics" (placeholder, real number only). On mobile everything goes to one column, the CTA spans the full width, and the image moves below the CTA.
2. **Social proof:** one standout metric, such as "−38% no-shows" (placeholder until you have real data), plus clinic logos.
3. **Problem → outcome:** phone tag, paper forms and empty slots, each paired with what changes. Two columns that stack on mobile.
4. **How it works:** 3 steps (Connect calendar → Share booking link → Patients self-serve).
5. **Features as benefits:** 3 cards across (reminders, intake, waitlist auto-fill), each showing a small piece of the UI. They stack on mobile.
6. **Testimonial:** a named practice manager with photo, role and clinic name. Real quotes only.
7. **Security and FAQ:** BAA, encryption and data ownership, in an accordion.
8. **Pricing:** 3 tiers with the middle one marked recommended, priced per provider. Risk reducers sit under each CTA.
9. **Final CTA:** repeats the main promise and the same "Start my free trial" button. The signup form asks only for email and clinic name.

**Rationale:** The bet is that warm, calm restraint builds more trust than the usual "medical blue plus stock doctors" look. A single teal is the only color moment, and real UI stands in for illustration. The conversion levers are social proof, authority (compliance), honest risk reversal, and a low-friction trial.

**Self-score:**

| Area | Scores |
|---|---|
| Design | Hierarchy 8 · Typography 8 · Color 9 · Depth 9 · Consistency 8 · A11y 8 · Responsive 8 · Originality 7 |
| Conversion | 5-sec clarity 9 · Single goal 9 · Value prop 8 · Proof 7 · Friction 8 · Persuasion 8 |

Proof started at 6 because there were no proof elements yet. I fixed that by putting a proof element and risk reducers next to every CTA, and it's now at 7 on placeholders. It only goes higher once real testimonials and metrics are in.

## Q3

Files read: SKILL.md

This skill doesn't apply. design-md covers visual design and conversion, and SKILL.md explicitly excludes "backend/non-visual work." So I'm answering this as a normal engineering task rather than through the design workflow.

**Questions first:**
- Can one appointment involve more than one provider or room?
- Are recurring appointments in scope?
- Is this multi-tenant, with several clinics in one database?
- Does any PHI end up in notes? That decides whether we need encryption or access controls on that column.

**Assumptions:** multi-tenant, one provider per appointment, no recurrence yet.

```sql
CREATE EXTENSION IF NOT EXISTS btree_gist;
CREATE TYPE appointment_status AS ENUM ('scheduled','confirmed','checked_in','completed','cancelled','no_show');

CREATE TABLE appointments (
  id           uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  clinic_id    uuid NOT NULL REFERENCES clinics(id),
  provider_id  uuid NOT NULL REFERENCES providers(id),
  patient_id   uuid NOT NULL REFERENCES patients(id),
  starts_at    timestamptz NOT NULL,
  ends_at      timestamptz NOT NULL,
  status       appointment_status NOT NULL DEFAULT 'scheduled',
  reason       text,
  created_at   timestamptz NOT NULL DEFAULT now(),
  updated_at   timestamptz NOT NULL DEFAULT now(),
  CHECK (ends_at > starts_at),
  EXCLUDE USING gist (provider_id WITH =, tstzrange(starts_at, ends_at) WITH &&)
    WHERE (status NOT IN ('cancelled','no_show'))   -- no double-booking
);
CREATE INDEX ON appointments (clinic_id, starts_at);
CREATE INDEX ON appointments (patient_id, starts_at DESC);
```

Next steps: row-level security keyed on `clinic_id`, and an audit-log table if PHI is involved. Once you answer the questions above, I'll turn this into a migration for your stack (Prisma, Drizzle or plain SQL).
