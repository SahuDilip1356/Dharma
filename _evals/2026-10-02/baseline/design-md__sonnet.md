## Q1

Files read: SKILL.md, INDEX.md, references/linear.app/DESIGN.md

**Mode: APPLY** (user named a brand: Linear). I scanned INDEX.md, picked `linear.app` (canvas `#010102`, voltage `#5e6ad2`, dark software-craft) and loaded only that file. No other system was opened.

**Quick questions (I'd ask, but proceed on assumptions below):**
1. Is there an existing SubSense codebase/stack (Next/Tailwind?) and existing tokens? If you already have a complete design system, I defer to it.
2. Do you want Linear's lavender as your accent, or SubSense's own brand color in that slot?
3. Do you have real product screenshots? Linear's language depends on them.

**Assumptions:** SubSense is a software product, there is no complete design system yet, and the existing page keeps its copy and structure; only the visual language changes. Dark marketing page, as Linear ships no light mode (its Don'ts say so).

**Tokens I'd apply (from the contract, used exactly):**
```
canvas #010102 (never #000)   surface-1 #0f1011  surface-2 #141516  surface-3 #18191a
hairline #23252a  hairline-strong #34343a
ink #f7f8f8  ink-muted #d0d6e0  ink-subtle #8a8f98
primary #5e6ad2  hover #828fff  focus-ring 2px #5e69d1 @50%
success #27a644 (only semantic color)
```
- **Type:** display-xl 80/1.05, 600, tracking -3.0px; display-lg 56, -1.8px; body 16/1.5 at 400, -0.05px; eyebrow 13px/500 with +0.4px tracking; button 14px/500. Linear's faces are proprietary, so I substitute **Inter** (500/600) and JetBrains Mono. I'd say so explicitly.
- **Radii/spacing:** buttons and inputs 8px (not pill), cards 12px, screenshot panels 16px; 4px base, 96px between sections, 1280px max width.
- **Depth:** no drop shadows. Hierarchy comes from the surface ladder plus 1px hairlines, and a faint top-edge highlight on lifted panels.
- **Lavender is scarce:** only the brand mark, primary CTA, focus ring and link emphasis. Never a section background or card fill. No second accent, no gradients or spotlight cards.

**Layout moves:** sticky 56px top nav (secondary "Sign in" + primary "Get started"); hero with display-xl headline and one primary CTA; a full-width product screenshot in a surface-1 / 16px panel as the protagonist of every section; 3-up feature cards (2-up at 1024, 1-up below 768); customer logos on canvas at ~24px height; closing CTA banner on surface-1 at 48px padding.

**Responsive:** display-xl scales 80px to about 36px on mobile; nav collapses to a hamburger below 768px; tap targets of at least 40px (44px for inputs).

**Persisting:** since this will likely span sessions, I'd offer to copy `linear.app/DESIGN.md` into the repo at `docs/DESIGN.md`, then rename it to SubSense.

**Caveat:** this is an inspired interpretation for your own product, not Linear's assets. Since SubSense isn't Linear, once the structure is in place I'd swap in a SubSense-specific accent hue, keeping the same discipline of one voltage color used sparingly. I'd also avoid copying Linear's wordmark, copy or screenshots.

---

## Q2

Files read: SKILL.md, INDEX.md, principles/synthesis-playbook.md, principles/corpus-analysis.md, principles/cro-principles.md, principles/design-principles.md, references/stripe/DESIGN.md (first 140 lines), references/intercom/DESIGN.md (first 140 lines)

**Mode: GENERATE** (no brand named, a product and a goal). Following the synthesis playbook; I'm producing an original system, not a clone.

**Step 0, intake (questions + assumptions):**
Questions I'd ask: What is the one conversion goal (book a demo vs free trial)? Who buys (practice owner, office manager, clinician)? Which region and compliance regime (HIPAA, DPDPA, GDPR)? Any name, logo or colors?
Assumptions: B2B SaaS for small and mid-size clinics (scheduling, records, billing). Goal is **Book a demo**. Positioning is *trustworthy, calm, efficient*. Surface is a marketing landing page. Trust requirements are high (health).
Since there is no brand, I use a placeholder wordmark, "[Clinic SaaS]". Naming and logo are out of scope, as the skill excludes full brand identity creation.

**Step 1, exemplars (borrow one move each):**
- `stripe`: trust through restraint, tabular numerics, light-weight display type, a navy ink.
- `intercom`: warm tinted canvas plus white floating tiles with hairlines, which humanizes a service product.
- Linear's product-screenshot-as-hero idea (from the corpus: product UI over stock art).

**Step 2, original DESIGN.md (key content):**
```yaml
colors:
  canvas: "#f4f7f6"        # cool-mint-tinted off-white, never #fff
  surface-1: "#ffffff"
  surface-2: "#e9efed"
  hairline: "#d5dedb"
  ink: "#10201f"  ink-muted: "#41524f"  ink-subtle: "#5c6d6a"   # all >=4.5:1 on canvas
  primary: "#0f766e"       # deep teal, the single voltage; white text ~5.5:1
  primary-hover: "#0b5f58"
  semantic-success "#1a7f4b"  semantic-error "#b42318"
typography:  # 2 families: Inter (UI/display) + JetBrains Mono for data
  display-xl: 56/1.08, 600, -1.4px   display-lg: 40/1.15, -0.9px
  body-lg: 18/1.5, 400   body: 16/1.5   caption: 13/1.4   button: 15/500
rounded: {sm: 6, md: 8, lg: 12, xl: 16}   # buttons 8px; no pills
spacing: base 4px; section 96px (64px mobile)
elevation: none; hairlines + surface tint only. motion: 160ms ease-out
```
Core bet: calm clinical trust through tinted canvas, one teal voltage, real product UI, and no stock-photo-of-doctors clichés.

**Step 3, page blueprint (goal: Book a demo):**
1. **Hero:** "Fill every slot. Cut front-desk admin by 10 hours a week." (hedge the number until validated). Subhead names clinic owners and managers. One teal CTA, "Book my 20-min demo", with risk-reversal beneath ("No credit card. Set up in a day."). Product UI screenshot of the schedule. Trust strip: HIPAA/DPDPA, encryption, "used by N clinics" (only if real).
2. **Social proof:** clinic logos plus one metric.
3. **Problem to outcome:** no-shows, double bookings, paper charts, and the after-state.
4. **How it works:** 3 steps.
5. **Features as benefits.**
6. **Proof:** named clinician testimonials with faces and roles.
7. **Objections:** security and compliance, data migration, FAQ.
8. **Pricing:** 3 transparent tiers, middle one anchored.
9. **Final CTA:** repeat the demo ask. The CTA also repeats after proof and pricing.
Mobile: single column, display scales to about 36px, sticky bottom CTA, 44px targets, demo form with email plus clinic size only.

**Rationale / levers:** social proof, authority (compliance), reciprocity (optional free no-show calculator), and low friction. No fake urgency.

**Step 5 self-score:** Hierarchy 8, Type 8, Color 8, Depth 8, Consistency 8, A11y 8, Responsive 8, Originality 7, 5-sec clarity 8, Single goal 9, Value prop 7 (needs real numbers), Proof 6 then revised to 7 (placeholder logos and testimonials flagged as must-be-real), Friction 8, Persuasion 8. I'd flag that proof is only as strong as the real data supplied.

---

## Q3

Files read: SKILL.md only (to check scope; no further files needed)

This request is out of scope for design-md. The skill's description excludes backend and non-visual work, and a Postgres appointments schema has no visual-design component. So I would not run APPLY, GENERATE or CRITIQUE, and I would not load any principles or reference files.

What I'd do instead: say briefly that this is a database/backend task, not a design-system one, and handle it with the appropriate path (for example a data-modeling or Postgres skill such as `engineering:system-design` or `supabase-postgres-best-practices`, or answer directly).

Clarifying questions I'd ask before writing the schema: single-clinic or multi-tenant? Which entities already exist (patients, providers, locations, services)? Timezone handling? Recurring appointments? Do you need overlap prevention per provider? Any PHI or retention requirements?

Under stated assumptions (multi-tenant clinic SaaS, existing `clinics`, `patients`, `providers` tables), I would propose a schema along these lines (sketch only, nothing created):
```sql
create table appointments (
  id uuid primary key default gen_random_uuid(),
  clinic_id uuid not null references clinics(id),
  patient_id uuid not null references patients(id),
  provider_id uuid not null references providers(id),
  during tstzrange not null,
  status text not null check (status in ('scheduled','confirmed','completed','cancelled','no_show')),
  created_at timestamptz not null default now(),
  exclude using gist (provider_id with =, during with &&) where (status in ('scheduled','confirmed'))
);
create index on appointments (clinic_id, provider_id, lower(during));
```
It would use the `btree_gist` extension for the exclusion constraint and row-level security by `clinic_id`.
