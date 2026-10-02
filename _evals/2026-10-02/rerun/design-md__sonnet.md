## Q1

Files read: SKILL.md, INDEX.md, references/linear.app/DESIGN.md

**Mode: APPLY.** The user named a brand (Linear). I checked INDEX.md, where `linear.app` is the obvious match (canvas `#010102`, voltage `#5e6ad2`). I loaded only that one DESIGN.md.

**Questions I would ask (not blocking):**
1. Does SubSense already have brand tokens, a logo color or a font? If it has a complete system, I defer to it and borrow only the structure.
2. What stack is the page in (Next/Tailwind, plain HTML)?
3. What is the single conversion goal (trial, demo, waitlist)?

**Assumptions I proceed on:** there is no locked brand. The stack is React with Tailwind. The goal is "Start free trial". This is an inspired interpretation for SubSense's own product, not a Linear clone. I would swap the lavender for SubSense's own color once the structure is in place.

**Key tokens, applied as a contract (from the Linear DESIGN.md):**
```
canvas #010102 (never #000, never a light page)   surface-1 #0f1011  surface-2 #141516  surface-3 #18191a
hairline #23252a  hairline-strong #34343a
ink #f7f8f8  ink-muted #d0d6e0  ink-subtle #8a8f98
primary #5e6ad2  hover #828fff  focus-ring 2px #5e69d1 @50%
success #27a644 (the only other chroma)
```
**Type:**
- Display-xl is 80/1.05, weight 600, tracking -3px.
- Display-lg is 56, tracking -1.8px.
- Body is 16/1.5 at weight 400.
- The eyebrow is 13px with +0.4px tracking.
- Linear's custom font is proprietary, so I substitute **Inter** (500/600) and JetBrains Mono. I say so to the user.

**Shape and depth:**
- Radii are 8px on buttons and inputs, 12px on cards and 16px on screenshot panels. CTAs are not pill-shaped.
- There are no shadows and no gradients. Depth comes from the surface ladder, hairlines and a faint white top-edge highlight.
- Spacing is on a 4px base with 96px between sections.
- The max width is 1280px. Card grids go 3, then 2, then 1 column at 1024 and 768px.

**Page blueprint (every section led by a product UI screenshot in a surface-1 panel):**
1. Nav at 56px: wordmark, links, a secondary "Sign in" and a primary "Start free trial".
2. Hero: an outcome headline at 80px, a body-lg subhead, one lavender CTA with a ghost secondary, and a framed product shot.
3. Logo strip, with small logos on canvas and no borders.
4. Three feature cards (surface-1, 12px radius, 24px padding), each with a screenshot.
5. Testimonial card at 32px padding.
6. Pricing in 3 tiers, with the featured tier lifted to surface-2.
7. Closing CTA banner at 48px padding.
8. Footer in ink-subtle.

Lavender appears only on the brand mark, the primary CTA, focus rings and links, never as a fill.

**Mobile:** display scales from 80px to about 36px. The nav collapses to a hamburger below 768px. Tap targets are at least 44px.

Tailwind sketch: `bg-[#010102] text-[#f7f8f8] border-[#23252a] rounded-lg tracking-[-0.04em]`

Optional: copy the chosen DESIGN.md into the repo's `docs/` so later sessions stay consistent.

## Q2

Files read: SKILL.md, principles/synthesis-playbook.md, principles/cro-principles.md, principles/corpus-analysis.md, principles/design-principles.md, INDEX.md, references/cal/DESIGN.md (partial), references/intercom/DESIGN.md (partial)

**Mode: GENERATE.** There is no named brand and the goal is "high-converting". I follow the playbook.

**Step 0 intake (questions, with assumptions below):**
1. What is the one conversion goal: book a demo or start a trial?
2. Who is the buyer: a practice owner, a clinic manager, or patients?
3. What is the region? DPDPA, HIPAA and GDPR change the trust badges.
4. Do you have a name or logo?

**Assumptions:** the buyer is a small or mid-size clinic owner or manager. The goal is "Book a demo". The three positioning adjectives are *trustworthy, calm, efficient*. The audience is in India, so DPDPA is relevant. Health means heavy trust requirements. Since there is no brand, I will create a design system but not a name or logo, and I say that this is outside the skill.

**Exemplars (one move from each, no cloning):**
- `cal`: booking-product UI shown inside cards, black CTA discipline, Inter plus a display face.
- `intercom`: warm off-white canvas (`#f5f1ec`) with hairline-bordered white tiles, which feels human and calm.
- Trust and authority patterns come from the CRO file. I did not load a third file.

**Original DESIGN.md (key tokens):**
```
canvas #f6f7f4 (tinted, not #fff)   surface-1 #ffffff   surface-2 #eceee9   hairline #dcdfd8
ink #14201c   ink-muted #4a5a54   ink-subtle #66746e   (all AA on canvas)
voltage #0f766e (deep teal, AA with white text)  hover #115e59  focus ring 2px voltage
semantic: success #15803d  warn #b45309  error #b91c1c
type: Inter (UI) + Fraunces-free: single family, display 56/1.08 w600 tracking -1.6px; h2 40 -1px; body 17/1.55; button 15 w600
radii 4/8/12/16 (buttons 8px, cards 12px)   spacing 4px base, sections 96px
shadows: none. Motion 160ms ease-out. Honor prefers-reduced-motion.
```

**Page blueprint (the one goal is "Book a demo"):**
1. **Hero.** Headline: "Fill your schedule. Cut the no-shows." Subhead: "Appointments, reminders and records for independent clinics, set up in a day." The CTA is "Book my 20-minute demo", with a risk line "No credit card. Your patient data stays encrypted." Beside it sits a real product shot of the scheduling UI, and a trust strip with a DPDPA badge and "Used by N clinics".
2. Social proof: a logo or clinic count and one standout metric.
3. Problem to outcome: phone tag, no-shows and paper records, set against the after-state.
4. How it works, in 3 steps: connect the calendar, send reminders, see the day at a glance.
5. Features as benefits, each tied to an outcome with a hairline card.
6. Proof: a named doctor's testimonial with a photo and a case-study number.
7. Objections: FAQ, security and compliance, data ownership, migration.
8. Pricing: 3 transparent tiers, with the middle tier anchored.
9. Final CTA, repeating the demo action.

The CTA repeats after the hero, after proof, after pricing and in the footer. On mobile the layout is single-column with a sticky bottom CTA, and tap targets are at least 44px.

**Rationale:** the core bet is calm trust over flashy "health-tech" color. Levers are social proof, authority (compliance), risk reversal and low-friction form (email and clinic name only).

**Self-score (fix below 7):** hierarchy 8, type 8, color 8, depth 8, consistency 8, accessibility 8, responsive 8, originality 7, 5-second clarity 8, single goal 9, value prop 7, proof 6 then raised to 7 by placing a named testimonial beside the pricing ask, friction 8, persuasion 8. Proof is the weakest area, because real testimonials are needed from the user.

## Q3

Files read: SKILL.md (no other files read)

The skill does not apply. The description says it is "Not for backend/non-visual work", and a Postgres appointments schema is backend data modeling. I would not load INDEX.md, the principles or any DESIGN.md. I would hand the request to a database or engineering approach, such as the supabase-postgres skill or system-design if available.

**Clarifying questions I would ask:**
1. Single clinic or multi-tenant (a `clinic_id` on every table)?
2. Which entities exist: patients, providers, services, locations?
3. Do you need recurring appointments, time zones or double-booking prevention?
4. Is it Supabase (RLS) or plain Postgres?
5. Is PHI or PII in scope, which affects encryption and audit?

**Assumptions I proceed on:** multi-tenant, Postgres 15 or newer.
```sql
create extension if not exists btree_gist;
create table appointments (
  id uuid primary key default gen_random_uuid(),
  clinic_id uuid not null references clinics(id),
  patient_id uuid not null references patients(id),
  provider_id uuid not null references providers(id),
  during tstzrange not null,
  status text not null default 'scheduled'
    check (status in ('scheduled','confirmed','completed','cancelled','no_show')),
  created_at timestamptz not null default now(),
  exclude using gist (provider_id with =, during with &&)
    where (status in ('scheduled','confirmed'))
);
create index on appointments (clinic_id, lower(during));
```
The exclusion constraint prevents double-booking. I would add row-level security per clinic and run the migration in a branch first.
