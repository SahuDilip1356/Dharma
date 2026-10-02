## Q1

Files read: SKILL.md, INDEX.md, references/linear.app/DESIGN.md

**Mode: APPLY.** You named a brand, so I'll rebuild the SubSense landing page in Linear's visual language. I picked `linear.app` from the index: near-black canvas `#010102`, one lavender voltage `#5e6ad2`, and product-screenshot-led pages. I loaded only that system.

**Two quick questions (I've assumed answers so I can keep going):**
1. Does SubSense have its own brand color? *Assumption: no, so I'll keep Linear's structure and swap the lavender for a SubSense accent of the same hue weight. That way the page borrows Linear's discipline without passing itself off as Linear's brand.* If you do have a color, it goes in the `primary` slot.
2. Do you have real product screenshots? Linear's pages lead with real UI in every section. *Assumption: yes, a subscription dashboard and a renewal-alert view.*

**Tokens (to be followed exactly, not loosely):**
```yaml
colors:
  canvas: "#010102"        # never #000
  surface-1: "#0f1011"     # cards, screenshot panels
  surface-2: "#141516"     # featured / hovered card
  surface-3: "#18191a"     # dropdowns, sub-nav
  hairline: "#23252a"      # 1px borders, no shadows anywhere
  hairline-strong: "#34343a"
  ink: "#f7f8f8"
  ink-muted: "#d0d6e0"
  ink-subtle: "#8a8f98"
  primary: "#5e6ad2"       # or SubSense accent; CTA, focus ring, brand mark, link emphasis ONLY
  primary-hover: "#828fff"
  success: "#27a644"       # status pills only
typography:   # Linear Display/Text are proprietary → using Inter (500/600) + JetBrains Mono
  display-xl: 80px / 600 / 1.05 / -3.0px     # hero; scales to ~36–40px on mobile
  display-lg: 56px / 600 / 1.10 / -1.8px     # section openers
  display-md: 40px / 600 / 1.15 / -1.0px
  card-title: 22px / 500 / 1.25 / -0.4px
  body-lg:    18px / 400 / 1.50 / -0.1px     # hero subhead
  body:       16px / 400 / 1.50 / -0.05px
  button:     14px / 500
  eyebrow:    13px / 500 / +0.4px
rounded: { md: 8px (buttons, inputs), lg: 12px (cards), xl: 16px (screenshot panels), pill: tabs/badges only }
spacing: 4px base · card padding 24px · section gap 96px · max width 1280px
```

**Section blueprint:**
1. **Top nav**: 56px, canvas background. Wordmark on the left, 4 links in the center, then `Sign in` (secondary, surface-1 with hairline) and `Get started` (primary, 8px radius, 8×14 padding).
2. **Hero**: display-xl headline in ink, body-lg subhead in ink-muted, one primary CTA plus a tertiary text link. Below it, a full-width `product-screenshot-card` (surface-1, 16px radius) showing the SubSense dashboard.
3. **Logo marquee**: logos at about 24px tall in ink-subtle on canvas, with no borders. 6-up, dropping to 3-up on mobile.
4. **Feature sections (×3)**: each opens with an eyebrow and a display-lg heading, then a product screenshot, then a 3-up grid of `feature-card`s (surface-1, hairline, 12px). No icons-in-circles and no gradients.
5. **Testimonial**: `testimonial-card` with 32px padding, body-lg text, and a 40px avatar.
6. **Pricing**: pill tab toggle (selected tab = surface-2). Three `pricing-card`s, with the recommended tier lifted to surface-2 and hairline-strong. No colored fill.
7. **CTA banner**: surface-1, 48px padding, headline token, one primary button.
8. **Footer**: dense link grid, caption type in ink-subtle.

**What the page must avoid:** a light mode, lavender used as a background fill, a second accent color, drop shadows, pill-rounded CTAs, or atmospheric gradients.

**Responsive:** grids go from 3-up to 2-up at 1024px and 1-up below 768px. The nav becomes a hamburger below 768px. Pricing turns into an accordion on mobile. CTAs keep a tap height of at least 40–44px.

If more work on this page will follow, I'd copy this `DESIGN.md` into the repo (`docs/DESIGN.md`) so future agents stay consistent with it.

---

## Q2

Files read: SKILL.md, principles/synthesis-playbook.md, INDEX.md, principles/corpus-analysis.md, principles/cro-principles.md, principles/design-principles.md, references/cal/DESIGN.md, references/intercom/DESIGN.md, references/stripe/DESIGN.md (I read only the token frontmatter of the three exemplars)

**Mode: GENERATE.** You described a product and a goal but no brand, so I'll compose an original system.

**Intake (my assumptions; correct any of them):**
- **Product:** scheduling, intake and reminders for small-to-mid outpatient clinics.
- **Buyer:** clinic owner or practice manager. Not technical, short on time, and anxious about compliance.
- **The one goal:** **Book a 20-minute demo.** I'd swap this for "Start free trial" if you're self-serve.
- **Adjectives:** calm, trustworthy, human.
- **Trust needs:** heavy. HIPAA, BAA availability, encryption, uptime.
- **Name:** "ClinicName" as a placeholder.

**Exemplars and the one move taken from each:**
- `cal`: product UI fragments shown inside cards, because scheduling is shown working rather than described.
- `intercom`: a warm off-white canvas with ink-black type, so the page reads as human rather than clinical.
- `stripe`: tabular figures and a single confident saturated primary, borrowed for institutional trust.

**DESIGN.md (excerpt):**
```yaml
colors:
  canvas: "#f7f5f1"        # warm off-white, not #fff
  surface-1: "#ffffff"     # cards
  surface-2: "#efebe4"     # alt bands, featured tier
  hairline: "#dcd6cc"
  ink: "#14201f"           # body 15.8:1 on canvas
  ink-muted: "#4a5553"     # AA ✓
  ink-subtle: "#6b7472"    # captions, ≥4.5:1 ✓
  primary: "#0f6e66"       # deep clinical teal, the ONE voltage; white text on it ≈6:1
  primary-hover: "#0b5852"
  focus-ring: "#0f6e66"    # 2px, 2px offset
  success: "#1f8a4c"  warning: "#b26b00"  error: "#b42318"   # paired with icons, never color alone
typography:   # Inter (display + UI), JetBrains Mono not needed; tnum for stats
  display-xl: 64px / 600 / 1.05 / -2px      # mobile 40px
  display-lg: 48px / 600 / 1.10 / -1.4px
  display-md: 36px / 600 / 1.15 / -0.8px
  title:      22px / 600 / 1.30 / -0.3px
  body-lg:    18px / 400 / 1.55
  body:       16px / 400 / 1.50
  caption:    13px / 500 / 1.40
  button:     15px / 500
rounded: { sm: 6px, md: 8px (buttons/inputs), lg: 12px (cards), xl: 16px (UI frames), pill: badges only }
spacing: 8px base · section 96px desktop / 64px mobile
elevation: none, hairlines + surface tint only
motion: 160ms ease-out, respects prefers-reduced-motion
```

**Page blueprint:**
1. **Hero:** "Fill every appointment slot, without the phone tag." Subhead: "Online booking, digital intake and automatic reminders for independent clinics. HIPAA-compliant, live in a week." Primary CTA: **Book my 20-min demo**. Next to the CTA: "No contract · BAA included · Setup done for you". Visual: the real booking calendar inside a 16px surface-1 frame. *Mobile:* stack the content, put a full-width CTA above the visual, and add a sticky bottom CTA after the first scroll.
2. **Trust strip:** "Trusted by 400+ clinics", a star rating, and HIPAA / SOC 2 / 256-bit encryption badges in ink-subtle.
3. **Problem → outcome:** no-shows and phone queues set against the after-state. Use a tabular stat: "−38% no-shows" (*placeholder; use a real figure only*).
4. **How it works:** three numbered steps (connect calendar → share booking link → reminders run themselves). 1-up on mobile.
5. **Features as benefits:** 3×2 cards, each with a small UI fragment. *Mobile:* single column.
6. **Proof:** two testimonials from a named practice manager and a clinician, with photo, clinic name and city.
7. **Security & FAQ:** a BAA, data-residency and migration accordion, then the CTA repeated.
8. **Pricing:** 3 tiers by provider count, "Most clinics choose" anchored on surface-2, with "Book my demo" on each tier.
9. **Final CTA band:** surface-2 background, the promise restated, one teal button, and the risk-reversal line again.

**Rationale:** the core bet is calm over clinical. A warm canvas and one deep-teal voltage signal care and competence without looking like a hospital. Conversion rests on proof and compliance next to every ask, a demo CTA that is low-commitment and first-person, and real UI in place of stock photos of doctors.

**Self-score (after one revision):** Hierarchy 8 · Typography 8 · Color 9 · Depth 9 · Consistency 8 · A11y 8 · Responsive 8 · Originality 7 · 5-sec clarity 9 · Single goal 9 · Value prop 8 · Proof & trust 8 · Friction 8 · Persuasion 8.
- *Revision made:* Proof had scored 6 because the logo strip was weak for an unknown brand. I added named testimonials and compliance badges at each CTA.
- *Still to watch:* originality. Once you settle the name, add one ownable brand moment, such as a custom wordmark or illustration style.

---

## Q3

Files read: SKILL.md

This is outside what design-md covers. The skill is for visual and UI design, and its description excludes backend and non-visual work, so I'm not using it here. I'll handle this as a normal engineering task. The `supabase:supabase-postgres-best-practices` or `engineering:system-design` skill would be the better fit if you want a guided pass.

**Questions first (assumed answers in italics):** Single clinic or multi-tenant? *Multi-tenant.* Do appointments need recurring slots? *Not yet.* Do you need overlap prevention per provider? *Yes.*

```sql
create extension if not exists btree_gist;

create type appointment_status as enum
  ('scheduled','confirmed','checked_in','completed','cancelled','no_show');

create table appointments (
  id            uuid primary key default gen_random_uuid(),
  clinic_id     uuid not null references clinics(id) on delete cascade,
  provider_id   uuid not null references providers(id),
  patient_id    uuid not null references patients(id),
  service_id    uuid references services(id),
  starts_at     timestamptz not null,
  ends_at       timestamptz not null,
  status        appointment_status not null default 'scheduled',
  notes         text,                 -- PHI: restrict via RLS / column grants
  cancelled_at  timestamptz,
  created_at    timestamptz not null default now(),
  updated_at    timestamptz not null default now(),
  check (ends_at > starts_at),
  -- no double-booking a provider (ignores cancelled/no-show)
  exclude using gist (
    provider_id with =,
    tstzrange(starts_at, ends_at, '[)') with &&
  ) where (status not in ('cancelled','no_show'))
);

create index on appointments (clinic_id, starts_at);
create index on appointments (patient_id, starts_at desc);
```

**Notes:**
- Store all times as `timestamptz` and keep each clinic's timezone on `clinics`.
- Turn on RLS scoped by `clinic_id`, because this table holds PHI.
- Add an `updated_at` trigger and an audit log table for HIPAA.
- Reminders go in a separate `appointment_reminders` table rather than in columns here.

I can write the full migration next if you confirm the assumptions.
