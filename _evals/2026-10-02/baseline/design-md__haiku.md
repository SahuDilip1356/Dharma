# design-md Skill Eval — Haiku 4.5

## Q1

**Files read:** INDEX.md, references/linear.app/DESIGN.md

**Mode:** APPLY — you named a brand (Linear), so I'm applying its visual language to SubSense.

**What I'd do:**

Linear's signature is a *software-craft aesthetic* — a near-black canvas (`#010102`), single lavender-blue accent (`#5e6ad2`), and dense, technical typography with negative tracking on display text. It reads luxurious because it's restrained: one voltage color, hairline borders instead of shadows, no decoration.

**For SubSense:**

1. **Canvas & colors** — adopt Linear's near-black `#010102` as your background. Swap the lavender (`#5e6ad2`) for SubSense's brand color if you have one; if not, keep the lavender as a "borrowed voltage" until your brand solidifies. Use the hairline system (`#23252a`, `#34343a`) for borders between panels.

2. **Typography** — if SubSense has a custom display font, match Linear's negative tracking (display at 60–80px with -1.8 to -3.0px letter-spacing). If not, substitute SF Pro Display (or Inter with -0.8px tracking on headlines). Body text stays at 16–18px / 1.5 line-height in a clean sans.

3. **Components** — product screenshots framed in dark panels (`#0f1011` surface) with hairline borders. CTAs in your voltage color, not overused. No shadows; depth comes from surface tints.

4. **Page structure** — above-the-fold: value headline (tight tracking), subhead, single dominant CTA, product screenshot. Sections below build on the screenshot-in-panel motif.

**Output:** A DESIGN.md contract (to persist in your codebase) + a section-by-section landing blueprint applying the Linear language to SubSense's positioning. Code if asked.

---

## Q2

**Files read:** principles/synthesis-playbook.md

**Mode:** GENERATE — you described a new product (healthcare clinic SaaS), no named brand, so I run the full synthesis engine.

**Intake (what I'd lock first):**

Before designing, I'd ask or assume:
- **Audience** — clinic staff? patients? both? (B2B or B2C? or both?)
- **Primary CTA** — book appointment / request demo / sign up for trial? (This gates everything.)
- **Positioning** — e.g., "trustworthy, fast, human" or "clinical-grade, secure, accessible"?
- **Constraints** — existing logo/colors? compliance needs (HIPAA)?
- **Surface** — marketing landing page or sign-up flow?

Assumptions if not answered: B2B (clinic managers), book demo CTA, positioning = "trustworthy + practical + modern", landing page surface, HIPAA-aware trust signals needed.

**Exemplar selection:**

From INDEX.md, I'd pick 2–3 systems that match *healthcare SaaS positioning* + *high conversion*:
- `stripe` (fintech trust model; clean, institutional)
- `intercom` (warm editorial + service framing; accessible)
- `coinbase` (institutional trust without coldness)

I'd read only those 3 DESIGN.md files, extract: how each builds trust (Stripe: dark ink + indigo, clean tables; Intercom: cream canvas + charcoal, human touch; Coinbase: white canvas + electric blue, institutional clarity).

**Synthesis (the original design):**

Compose a **DESIGN.md** combining moves from all three:
- Canvas: tinted off-white (`#f9f8f6`), not pure white — warmer, more human than enterprise.
- Voltage: healthcare-appropriate blue (`#0066cc`) or teal (`#00a099`) — one only, never both.
- Typography: confident headline font at 48–64px with -0.8px tracking; readable body sans at 16px / 1.6 line-height (accessible for vision-impaired clinic users).
- Surfaces: 3 tints off the canvas with hairline borders (no shadows).
- Spacing: 8px base (modular, crisp).

**CRO blueprint:**

Section order for a healthcare clinic SaaS landing:
1. **Hero** — "Book & manage clinic appointments in one place" + clinic photo or screenshot + "Start Free Trial" CTA + trust strip (HIPAA-compliant, 500+ clinics, etc.).
2. **Problem** — clinic scheduling chaos, no-shows, manual reminders.
3. **Solution** — 3 proof points (automated reminders ↓ no-shows by 40%, integrates EHR, staff love it).
4. **Features** — 4–5 cards (appointment booking, automated SMS, patient intake, staff management).
5. **Social proof** — customer logos + 1 quote from clinic manager.
6. **Risk reversal** — "Free forever plan for solo clinics" + "30-day full-featured trial".
7. **CTA repeat** — "Start Your 30-Day Trial" in voltage color.
8. **Mobile** — hero compresses, CTAs become full-width, cards stack.

**Deliverable** (if scope allows): DESIGN.md (the contract) + section blueprint with copy stubs + rationale (3 exemplars borrowed one move each) + React/HTML code if requested.

**Self-score before ship:** Would check design hierarchy (clear focal point?), 5-second clarity (new visitor: *what* is this, *for whom*, *what's the ask*?), proof placement (risk-reversal next to every CTA?), and AA contrast (text on background ≥4.5:1).

---

## Q3

**Files read:** (none — out of scope)

**Out of scope.** design-md is for *visual design* — landing pages, UI systems, design critiques. Backend schema design (Postgres appointments table) is not a design-md task.

**Redirect:** For Postgres schema guidance, consult:
- A backend/database agent (e.g., Supabase MCP tools for schema management).
- The project's data design skill or an engineer focused on schema modeling.

**What I'd note:** If you're building the *frontend* for appointment booking (landing page, patient intake form, scheduler UI), that *is* in scope — design-md can produce a DESIGN.md + component specs for how those forms and calendar should look and behave. Backend schema stays separate.

