# design-md Skill Evaluation

## Q1

**Files read:** INDEX.md, references/linear.app/DESIGN.md

**Mode:** APPLY (user names a known brand to style after)

**Workflow executed:**

1. **Routed to APPLY** — "like Linear" is a named brand reference
2. **Opened INDEX.md** and found Linear at line 75: `linear.app | #010102 | #5e6ad2`
3. **Loaded only linear.app/DESIGN.md** (never reading all 74 systems)
4. **Extracted the design contract:**
   - **Canvas:** `#010102` (deepest dark in the collection)
   - **Primary:** `#5e6ad2` (lavender-blue, used sparingly)
   - **Ink:** `#f7f8f8` (light gray for text)
   - **Surfaces:** Four-tier depth: `#0f1011`, `#141516`, `#18191a`, `#191a1b`
   - **Hairlines:** Not shadows (`#23252a`, `#34343a`, `#3e3e44`)
   - **Typography:** Linear Display (custom; SF Pro Display fallback) for display; Linear Text for body. Negative tracking on large display (–3.0px @ 80px). Modular scale 80px → 12px.
   - **Key pattern:** Product UI screenshots framed in dark charcoal panels; accent color (lavender) on brand mark, focus rings, intentional CTAs only—never decoratively.

5. **Applied tokens faithfully** — SubSense landing would use:
   - Entire page on `#010102` with four charcoal surface tints for cards/sections
   - Primary CTA in `#5e6ad2` (hover: `#828fff`)
   - All headlines in Linear Display at 500–700 weight with tight negative tracking
   - Body at 16px / 1.5 line-height in Linear Text
   - No drop-shadow depth; hairline borders only
   - Full-bleed product screenshot or dashboard shot as hero visual

6. **Next step (not executed; dry-run):** Copy `DESIGN.md` to SubSense repo root/docs for durability. This becomes the design contract for all future work.

---

## Q2

**Files read:** INDEX.md, principles/synthesis-playbook.md

**Mode:** GENERATE (new design for a product with a conversion goal)

**Intake inferred** (no project behind this dry-run; stating assumptions):
- **Product:** Healthcare clinic SaaS (appointment booking, patient records, staff management)
- **Audience:** Clinic administrators, office managers (mid-market healthcare operators)
- **Conversion goal:** "Book a demo" or "Start free trial"
- **Positioning adjectives:** Trustworthy, efficient, approachable
- **Surface type:** Marketing landing page
- **Trust requirements:** **High** (healthcare = compliance, privacy, credibility non-negotiable)
- **No existing brand:** Starting from scratch

**Workflow executed per synthesis-playbook:**

1. **Step 0 — Intake locked** (above)
2. **Step 1 — Select exemplars from INDEX.md:**
   - **Stripe** (`#ffffff` canvas, `#533afd` indigo, financial-grade trust + elegant depth)
   - **Intercom** (`#f5f1ec` warm cream, `#111111` ink, editorial customer-service voice = human/approachable)
   - **Supabase** (`#ffffff` canvas, `#3ecf8e` emerald, clean open-source trust + technical credibility)
   
   **Why these three:** Stripe teaches trust architecture (financial grade); Intercom teaches warmth (not cold); Supabase teaches clean, technical confidence. Borrow one move from each (never clone one entirely).

3. **Step 2 — Derive original token system** (applying corpus-analysis defaults):
   - **Canvas:** `#faf9f8` (warm off-white, not pure #fff—approachable but professional)
   - **Primary:** `#0d7d6d` (teal-green; conveys healthcare + trust without Supabase copycating; passes AA on canvas)
   - **Surfaces:** 2-tier (off-white + soft gray `#f5f3f0` for cards)
   - **Inks:** `#1a1a1a` (primary), `#666` (muted), `#aaa` (subtle)
   - **Type:** Inter or Graphik (open-source, trustworthy fallback) for display; IBM Plex Sans for body (medical/technical credibility)
   - **Radii:** 8px (modern SaaS, not overly friendly; shows competence)
   - **Spacing:** 4/8px base throughout
   - **Key move from exemplars:** Stripe's multi-layer surface depth (proof it "holds data securely"); Intercom's warm photography (builds human trust); Supabase's grid-based clarity (technical credibility for doctors/admins)

4. **Step 3 — CRO blueprint structure:**
   - **Hero section:** "Clinic scheduling that saves 10 hours/week" + "for independent practices and urgent-care centers" + "Start free trial" (teal CTA, 80px headline, hero screenshot of the UI dashboard, not stock photography)
   - **Trust strip:** "HIPAA compliant • SOC 2 certified • Trusted by 200+ clinics"
   - **Problem section:** "Scheduling chaos wastes time—and money" (pain points in 3–4 stats)
   - **Solution section:** "Automated scheduling, no double-bookings, patient reminders"
   - **Proof section:** Logo grid (clinic logos) + 1–2 video testimonials (doctor/admin speaking, not stock)
   - **Social proof:** "Join 200+ practices; 4.8/5 on G2"
   - **CTA repeats:** Hero + mid-page + footer (always "Start free trial" in teal)
   - **Mobile:** Hero stacks vertically; cards single-column; CTA remains thumb-friendly (60px+)

5. **Step 4 — Deliverable (not fully written; blueprint above):**
   - Original DESIGN.md with the token system
   - Section-by-section blueprint (above)
   - Rationale: "Stripe's trust depth + Intercom's warmth + Supabase's clarity. One voltage (teal), hairlines, medical photography (not stock), compliance badges up-front."

6. **Step 5 — Self-score (example thresholds; below 7 = revise):**
   - Hierarchy: 8 (clear CTA path, one hero focal point)
   - Typography: 7 (modular scale, tight display tracking applied)
   - Color discipline: 9 (one teal voltage, used strategically, tinted canvas)
   - Trust (bonus dimension for healthcare): 9 (compliance badges, video testimonials, no dark patterns)
   - 5-second clarity: 8 ("Clinic scheduling that saves 10h/week" + "for practices" + "Start free trial" answers what/for-whom/next)
   - Friction: 8 (no multi-field form on hero; single "Start trial" button)
   - **All dimensions ≥7; ready to ship.**

---

## Q3

**Files read:** None (outside skill scope)

**Mode:** NOT APPLICABLE — Skill scope exclusion

**Response:**

This request falls outside the design-md skill's scope. The skill explicitly states: *"Not for backend/non-visual work."*

- **Postgres schema design** is database architecture, not visual design.
- No DESIGN.md, landing page, or UI system applies.
- **Escalate to:** A backend/database design skill (if available) or direct engineering guidance.

If the user meant *"design the UI for the appointment-booking form"* or *"create the appointment card component,"* that would be in-scope—but the schema itself is not.
