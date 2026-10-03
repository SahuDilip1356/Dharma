# CRO Principles — Designing for Conversion

## Contents

- [The one rule above all: one page, one job](#the-one-rule-above-all-one-page-one-job)
- [The above-the-fold contract (first 5 seconds)](#the-above-the-fold-contract-first-5-seconds)
- [Value proposition & message hierarchy](#value-proposition--message-hierarchy)
- [The persuasion levers (apply honestly)](#the-persuasion-levers-apply-honestly)
- [Friction reduction (every removed step is conversion gained)](#friction-reduction-every-removed-step-is-conversion-gained)
- [Trust & anxiety reduction (the conversion killers are doubts)](#trust--anxiety-reduction-the-conversion-killers-are-doubts)
- [Reading patterns & layout for conversion](#reading-patterns--layout-for-conversion)
- [Landing-page section blueprint (high-converting default order)](#landing-page-section-blueprint-high-converting-default-order)
- [Measurement mindset](#measurement-mindset)
- [The CRO anti-patterns](#the-cro-anti-patterns)

Conversion Rate Optimization is design with a measurable job: move the visitor to
take one action. Beauty that doesn't convert is decoration. This file encodes the
durable CRO laws and how they shape layout, copy, and components. Pair with
[design-principles.md](design-principles.md) — good CRO and good design rarely
conflict; when they seem to, clarity wins.

## The one rule above all: one page, one job

Every page has a **single primary conversion goal** (book a demo, start trial,
buy, subscribe, sign up). Define it before designing. Every element either moves
the visitor toward it or earns its place by reducing friction/anxiety. Competing
CTAs split intent and lower conversion.

## The above-the-fold contract (first 5 seconds)

A visitor must be able to answer three questions without scrolling:

1. **What is this?** — a clear headline stating the value proposition in the
   customer's language, not your internal jargon. Benefit > feature.
2. **Is it for me?** — a subhead that names the audience and the outcome.
3. **What do I do next?** — one prominent primary CTA, visually dominant
   (the voltage color, largest button, unmistakable).

Supporting above-the-fold: a product visual (real UI/screenshot/photo, not stock)
and a lightweight trust signal (logos, rating, "used by N teams").

**Rule:** if a stranger can't state what you do and what to click within 5
seconds of seeing the hero, the hero has failed.

## Value proposition & message hierarchy

- Lead with the **outcome the customer wants**, not the mechanism.
- Headline = the promise. Subhead = the proof/specificity. Body = the how.
- Quantify when you can ("cut close time 40%") — specifics out-convert
  adjectives.
- **Message match:** the headline must match the ad/link/source that brought them
  here. Mismatch spikes bounce.

## The persuasion levers (apply honestly)

Grounded in Cialdini + decades of CRO testing. Use them; don't fake them.

- **Social proof** — logos, testimonials with name/face/role, counts, ratings,
  case studies. The single most reliable conversion lever. Place near CTAs and
  the hero.
- **Authority** — credentials, security/compliance badges, expert endorsement,
  press. Especially vital for fintech, health, B2B.
- **Anchoring** — show the higher-value option first; frame pricing against value
  delivered.
- **Scarcity / urgency** — only when *real* (limited seats, deadline). Fake
  urgency erodes trust and can backfire.
- **Reciprocity** — give value first (free tool, template, guide) to earn the
  signup.
- **Commitment & consistency** — small yes before big yes (email before credit
  card; multi-step forms that start easy).
- **Loss aversion** — frame the cost of *not* acting, truthfully.

## Friction reduction (every removed step is conversion gained)

- **Forms:** ask for the minimum. Each field drops completion. Email-only beats
  email+password+company. Defer the rest to after the first yes.
- **Cognitive load (Hick's Law):** fewer choices = faster decisions. Limit nav
  items, pricing tiers (3 is the sweet spot), and competing links near the CTA.
- **Fitts's Law:** make the primary CTA big and easy to hit; repeat it down the
  page so it's always in reach.
- **Clarity of CTA copy:** action + value ("Start free trial", "Get my report"),
  not "Submit". First person ("Start *my* trial") often lifts clicks.
- **Speed is conversion:** every 100ms of latency measurably costs conversions.
  Performance (image weight, render time) is a CRO concern, not just eng.
- **Remove dead ends:** every page should offer a clear next step.

## Trust & anxiety reduction (the conversion killers are doubts)

Address the objections in the visitor's head at the moment of decision:

- Near the CTA, neutralize risk: "No credit card", "Cancel anytime", "30-day
  refund", "Your data is encrypted".
- Show security/compliance signals on fintech/health/B2B (SOC2, GDPR/DPDPA, SSL).
- Transparent pricing. Hidden pricing is a friction and a trust cost.
- Real human proof (faces, names, companies) beats anonymous quotes.

## Reading patterns & layout for conversion

- **F-pattern** for text-heavy pages, **Z-pattern** for sparse landing pages —
  place logo, headline, and CTA along the natural path.
- **Visual hierarchy = conversion hierarchy.** The thing you most want clicked
  must be the most visually dominant (size + voltage color + isolation/space).
- **Directional cues** — whitespace, arrows, a person's gaze, or a product angle
  pointing toward the CTA.
- **Repeat the CTA** at natural decision points (after the value prop, after
  social proof, after pricing, in the footer).
- **Mobile-first:** the majority convert (or bounce) on mobile. Thumb-reachable
  CTAs, single-column flow, tap targets ≥44px.

## Landing-page section blueprint (high-converting default order)

1. **Hero** — value-prop headline + subhead + primary CTA + product visual +
   trust strip.
2. **Social proof** — logos / rating / a standout metric.
3. **Problem → outcome** — name the pain, show the after-state.
4. **How it works** — 3 steps, scannable.
5. **Features as benefits** — each feature tied to a customer outcome.
6. **Proof** — testimonials / case study / data.
7. **Objection handling** — FAQ, security, guarantees.
8. **Pricing** — transparent, 3 tiers, recommended one anchored.
9. **Final CTA** — restate the promise, repeat the primary action.

Adapt to context (app dashboards, signup flows, and content pages have their own
shapes) — but the principles (one goal, clarity, proof, low friction) are
constant.

## Measurement mindset

- Define the **primary metric** (signup rate, demo bookings, purchases) and a
  guardrail (bounce, scroll depth).
- Design enables testing: isolate one variable per experiment; the hero headline
  and primary CTA are the highest-leverage things to test first.
- **Rule:** a design decision you can't tie to clarity, trust, friction, or
  motivation is decoration — justify it or cut it.

## The CRO anti-patterns

- Multiple competing primary CTAs. → One per viewport.
- Vague hero ("Welcome", "The future of X"). → Concrete value prop.
- Feature lists with no benefit framing. → Outcome-led.
- Long forms up front. → Progressive disclosure.
- No trust signals near the ask. → Proof + risk-reversal at the CTA.
- Fake urgency / countdown timers that reset. → Honest scarcity or none.
- Burying the CTA / showing it once. → Dominant and repeated.
- Slow, heavy hero images. → Optimize; speed converts.
