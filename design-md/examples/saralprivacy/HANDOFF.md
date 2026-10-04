# SaralPrivacy Landing Page: Developer Handoff

**Version:** 1.0 · **Date:** 2026-06-21 · **Owner:** Dilip Sahu
**Reference build:** `landing-page.html` (single-file, self-contained, responsive)
**Design tokens:** `DESIGN.md` · **Structure rationale:** `blueprint.md`

This document is everything a developer needs to build the SaralPrivacy landing
page. The reference HTML is the visual source of truth; this doc explains the
tokens, components, motion, copy, routing, and the facts that must stay accurate.

---

## 1. Goal & strategy

- **Primary conversion goal:** start a **free Data Discovery** scan, which routes
  into the **free Readiness Assessment**. One goal, repeated; everything else
  reduces friction or builds trust toward it.
- **Spine:** a guided journey the visitor is walked through, **Discover → Readiness
  → Fix → Signal trust → Stay ready**, not a passive marketing scroll.
- **Tone (brand-locked):** trustworthy, practical, sharp, calm, expert. Lead with
  business consequence, then the fix. No fear theatre. Sentence case. Active voice.
  Never the phrase "legal compliance."

---

## 2. Facts & claims register (DO NOT change without re-verifying live)

Every number on the page was reconciled against **the live saralprivacy.com on
2026-06-21**. Keep them in sync with the live product; conversion sites cannot
afford metric inflation.

| Claim | Use as | Status |
|---|---|---|
| Time to complete | **3-5 minutes** (never "10 minutes") | ✅ live: "3-5 minute readiness check / assessment" |
| Sector assessments | **12** | ✅ live |
| Business types mapped | **276** | ✅ live |
| Briefings published | **200+** | ✅ live |
| Indian languages (guide) | **7** | ✅ live |
| Resources | **50+** (optional, not on current page) | ✅ live |
| Press / "Seen in" | **ANI, Business Standard, The Tribune, Lokmat Times, Latestly** | ✅ live (all five) |
| Consultation | **Free 30-minute consultation** | ✅ live (advisory CTA should book this) |
| Readiness score "72" + gap rows | **Illustrative example** (recruitment sample) | ⚠️ label as "example" so it doesn't read as the visitor's own result |
| Verified Digital Trust badge | Step 3 / outcome 03 | ⚠️ confirm the badge product is shippable before launch; if not, soften to roadmap |

> Use a hyphen ("3-5 minutes"), not an en-dash or em-dash. **No em-dashes anywhere**
> in copy (founder preference).

---

## 3. Design tokens

Full spec in `DESIGN.md`. Dev-ready summary:

### Colour (CSS custom properties, already in the file `:root`)
| Token | Hex | Role | Budget |
|---|---|---|---|
| `--navy` | `#121A2E` | Trust Navy, headings/ink + the 2 dark bands | ~45% |
| `--navy-2` | `#1B2540` | raised navy surface | - |
| `--navy-line` | `#2B3654` | hairline on navy | - |
| `--green` | `#07B981` | Verification Green, **primary CTA only** | ~20% |
| `--green-d` | `#059669` | green hover / green text-on-light | - |
| `--green-tint` | `#E6F7F0` | soft green wash (tags, get-help) | - |
| `--teal` | `#35B6AE` | links, eyebrows, diagram support | ~10% |
| `--gold` | `#E8AB42` | "Start here" / ceremonial only | ~5% |
| `--slate` | `#334155` | body text | ~10% |
| `--slate-2` | `#5B6B82` | secondary text | - |
| `--muted` | `#94A3B8` | hints/labels | - |
| `--cloud` | `#F7F9FC` | page floor / light sections | ~10% |
| `--cloud-2` | `#EEF2F8` | alt light surface (founder band) | - |
| `--line` | `#E4E9F1` | hairline borders on light | - |
| `--risk` / `--risk-bg` | `#E24B4A` / `#FCEBEB` | risk "High" pill | - |

**CTA button is locked:** Verification Green background + white label. Never an
outline/ghost green button. Forbidden combos: gold text on white, green bg + teal
text, navy bg + slate text, any gradient as a primary background.

### Typography
- Family: **Inter** (`400, 500, 600, 700`), fallback `system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif`.
- Headings: weight 700, `letter-spacing: -.02em`, `line-height: 1.12`.
- Scale (responsive `clamp`): H1 36→58px · H2 28→40px · H3 20→25px · body 17px/1.6 · lead 17→19px · eyebrow 12.5px uppercase `.13em`.

### Spacing, radius, motion
- Base rhythm 8px. Section padding `clamp(56px, 8vw, 104px)`.
- Radii: `--r-md 14px`, `--r-lg 20px` (cards), `--pill 100px` (buttons/chips).
- **Depth = hairline borders + surface tint, not shadows.** One soft shadow is
  allowed on the floating hero snapshot card only.
- Motion: `--ease cubic-bezier(.22,.61,.36,1)`, durations 200-700ms.

### Layout
- Container `--maxw 1160px`, side padding `clamp(20px, 5vw, 56px)`.
- Breakpoints used: **860px** (hero/founder/cards stack), **820px** (steps/grids), **780px** (journey rail → vertical), **720px** (progress-rail labels hide).

---

## 4. Page structure (order, IDs, stage, background)

Two dark moments only (navy): **Journey** and **Final CTA**. Everything else light.

| # | Section | `id` | Journey stage | Background |
|---|---|---|---|---|
| - | Sticky nav | - | - | white/blur |
| - | Sticky progress rail ("you are here") | `#prail` | tracks scroll | navy |
| 1 | Hero + Discovery snapshot | `#discovery` | Discover | cloud→white |
| 2 | Trust strip (metrics + press) | - | - | cloud |
| 3 | Outcomes ("three things in hand") | - | Readiness | white |
| 4 | **Journey motion graphic** | `#how` | Readiness | **navy (dark #1)** |
| 5 | The 4 steps in full | - | Fix | white |
| 6 | Tool Rail (7 tools, 3 states) | `#toolkit` | - | white/cloud |
| 7 | Mid CTA | - | - | navy card on white |
| 8 | Founder proof | `#proof` | Signal trust | cloud-2 (tinted) |
| 9 | Testimonials | - | - | white |
| 10 | Briefings | `#briefings` | Stay ready | white |
| 11 | Newsletter | - | - | cloud |
| 12 | **Final CTA** | - | - | **navy (dark #2)** |
| 13 | Footer (resources, legal) | `#resources` | - | near-black |
| - | Sticky conversion bar | `#cbar` | appears after 700px scroll | navy |

---

## 5. Component specs

### Buttons
- **Primary** `.btn`: green bg, white label, pill, 600 weight, hover darkens + lifts 1px, arrow nudges right. One per viewport.
- **Ghost** `.btn--ghost`: transparent, 1.5px `#CBD5E1` border, navy label. Secondary actions only.
- **Text/link CTA** `.tool__cta`, `.linklike`: green-d label + trailing arrow, for in-section steps.

### Hero Discovery snapshot (`.snap`)
Floating card demonstrating the product outcome: readiness **ring** (conic-gradient
`--p`), verdict, 4 data rows with status chips (`Mapped` / `Often missed`, green /
amber / risk), and a "Fix first" footer. **Add an "Example" label** (see §2).

### Journey motion graphic (`.motion`), the centerpiece
A ~13s auto-looping rail (replays when scrolled into view):
- **Comet** travels left→right across 5 nodes (`@keyframes travel`), fading in/out at loop ends.
- **Track fill** draws a gold→green→teal progress line (`@keyframes fill`).
- **Nodes activate in sequence**, JS adds `.act` at marks `[0, 2.6s, 5.2s, 7.8s, 10.4s]` synced to the comet; active node scales 1.12, lights green, glows.
- **Readiness milestone (node 2)** fills a ring and **counts 0→72** via JS when the comet lands.
- **Reduced-motion:** all nodes shown active, track full, no movement (`@media (prefers-reduced-motion)` + JS guard). **Required.**
- **Mobile (<780px):** comet/track hidden, stages stack as a clean vertical list.

### Tool Rail (`.toolrail`, `.tool`), status-aware
7 cards across 3 states; the badge (`.tbadge`) and CTA change by state:
- **Live** (Assessment, Data discovery): badge "Live", CTA routes to the tool.
- **In build** (Privacy notice generator, Data rights form): badge "In build", CTA "Get early access" (email capture).
- **Roadmap** (Vendor & DPA tracker, Retention plan, Advisory & Pro): badge "Roadmap", CTA "Notify me / Join waitlist".
Detailed product specs for the In-build tools live in `spec-notice-generator-and-dsar.md`.
The `data-tool="…"` attribute on each waitlist button identifies which tool was requested, wire it to your capture endpoint.

### Other
- **Sticky progress rail** (`.prail`): 5 steps; JS `IntersectionObserver` lights the step matching the section in view (`rootMargin: -45% 0 -45%`). Labels hide <720px.
- **Accordion** (`.acc`, single-open): used in Step 2. JS sets `max-height` for smooth open.
- **Sticky conversion bar** (`.cbar`): slides up after 700px scroll, dismissible.
- **Scroll reveal** (`.reveal` → `.in`): fade/translate on enter, `threshold .14`.

---

## 6. CTA & routing map (wire these URLs)

| CTA | Appears | Destination (confirm exact URLs) |
|---|---|---|
| Start free Discovery | nav, hero, journey, mid-CTA, final, cbar | Free Data Discovery tool |
| Take readiness assessment | hero secondary, tool rail | Free Readiness Assessment |
| Get the DPDPA guide / Download the Guide | hero, final | DPDPA Guide (7 languages) |
| Get early access (In-build tools) | tool rail | email capture + `data-tool` value |
| Notify me / Join waitlist (Roadmap) | tool rail | waitlist + `data-tool` value |
| Read brief / See all briefings | briefings | Daily Briefings |
| Subscribe | newsletter | newsletter signup (email + optional name + consent) |
| Advisory / Get help | step 4, tool rail #7 | **Free 30-minute consultation** booking |

Nav items (match live): Free Data Discovery · Free Assessment · Industries ·
Learn DPDPA · Daily Briefings · Blog · Templates · DPDPA Guide.
Footer/resources: FAQ · Glossary · About · Media · Privacy Notice · Terms ·
Consent Preferences · Data access/erasure.

---

## 7. Accessibility (must pass before launch)

- Text/bg contrast ≥ **4.5:1** (AA). Re-check `--teal` links and `--muted` labels on their backgrounds.
- Visible focus states on every interactive element (green focus ring is on-brand).
- Semantic landmarks (`header`, `nav`, `main`, `section`, `footer`); one `h1`; ordered headings.
- Hit targets ≥ 44px; labels on all inputs; `aria-label` on icon-only buttons; decorative SVGs `aria-hidden`.
- Honour `prefers-reduced-motion` (journey, comet, reveals).
- Don't encode meaning in colour alone (status chips also carry text).

---

## 8. SEO / meta

- `<title>` SaralPrivacy · Know your gaps. Fix what matters. Signal trust.
- Meta description: lead with the value prop + "DPDPA readiness in 3-5 minutes, in plain English, India-first."
- Add Open Graph + Twitter card (title, description, image 1200×630), canonical URL, favicon.
- JSON-LD: `Organization` + `WebSite` (+ `FAQPage` if the FAQ ships). Press mentions can feed `sameAs`/citations.

---

## 9. Analytics events to instrument

`cta_click` (with `cta_id`), `discovery_start`, `assessment_start`,
`guide_download`, `tool_waitlist_submit` (`data-tool`), `newsletter_submit`,
`consultation_book`, `journey_view`, `scroll_depth` (25/50/75/100),
`cbar_impression`/`cbar_dismiss`. Primary metric = Discovery/Assessment starts;
guardrails = bounce + scroll depth.

---

## 10. Assets

| Asset | Status |
|---|---|
| Logo | `assets/saralprivacy-logo.png` (provided; current header uses an inline shield SVG, swap to logo if preferred) |
| Founder photo | **Needed**, replace the `DS` placeholder tile in the founder section (Dilip Sahu) |
| Press logos | Optional, currently rendered as text names (cleaner; keep unless real logos are licensed) |
| Inter font | Google Fonts (already linked); self-host for performance if desired |
| Favicon + OG image | **Needed** |

---

## 11. Build notes

- The reference is a **single self-contained HTML file** (CSS in `<style>`, JS in
  `<script>`, no build step), open it directly to see the full motion.
- **Recommended port:** React (project stack is React + Node/PostgreSQL). Map each
  `<section>` to a component; lift `:root` tokens into CSS variables or a theme;
  the journey/progress-rail/cbar JS becomes small `useEffect` + `IntersectionObserver`
  hooks. Keep the CSS-keyframe motion as-is (robust, cheap).
- An earlier interactive prototype of the journey (`rail / ascend / ledger`
  treatments) exists in the original build's `app.js` if you want a configurable
  variant; the handoff build uses the single "rail" motion.
- **Performance:** optimise the founder photo + any hero imagery (speed is a
  conversion lever); lazy-load below-the-fold; self-hosting Inter trims a request.

---

## 12. Open items for founder

1. Confirm exact destination URLs for each CTA (§6).
2. Provide the founder photo + favicon + OG image (§10).
3. Confirm the **Verified Digital Trust badge** is a shippable product, or move it to roadmap framing (§2).
4. Confirm the advisory CTA books the **free 30-minute consultation** (and the booking link).
5. Add the "example" label to the hero snapshot's score/gaps (§2, §5).

---

## File manifest

```
saralprivacy/
├── HANDOFF.md          ← this document
├── landing-page.html   ← reference build (visual source of truth)
├── DESIGN.md           ← full token spec
├── blueprint.md        ← section order + dark-band rhythm + scorecard
├── spec-notice-generator-and-dsar.md  ← product specs for the In-build tools
└── assets/
    └── saralprivacy-logo.png
```
