---
version: "1.0"
name: SaralPrivacy-design-system
description: "A calm, operator-grade trust interface for DPDPA privacy readiness. Light Cloud canvas (#F7F9FC) carries the page; Trust Navy (#121A2E) anchors exactly two dark moments (Journey strip + Final CTA) for rhythm, not weight. Verification Green (#07B981) is the single voltage, primary CTAs and trust affirmations only, never decoration. The system reads as a practical tool, not a policy site: a product snapshot card in the hero, output-preview cards in Assess, hairline borders instead of shadows, tight-tracked Inter Display headlines in sentence case, and generous whitespace. Trust is engineered into the order, discover the problem, assess seriousness, fix first gaps, trust the operator, then ask for help."

# Source: design-md GENERATE mode. Exemplars referenced: stripe (clean fintech
# trust), intercom (warm operator editorial), linear.app (restraint + hairlines).
# Brand tokens: SaralPrivacy brand skill (locked). Founder review corrections applied.

colors:
  # voltage
  primary: "#07B981"          # Verification Green, CTAs, active, trust affirmations (~one role)
  on-primary: "#ffffff"
  primary-hover: "#05A271"
  primary-tint: "#E6F7F0"     # soft green wash for Get-help section
  # dark anchor (2 moments only)
  navy: "#121A2E"             # Trust Navy, Journey strip, Final CTA, headings
  navy-surface: "#1B2540"     # raised cards on navy
  navy-hairline: "#2B3654"
  on-navy: "#F7F9FC"
  on-navy-muted: "#A9B2C7"
  # light system
  canvas: "#F7F9FC"           # Cloud 50, page floor
  surface-1: "#ffffff"        # cards / sections
  surface-tint: "#F1F5FB"     # founder-proof subtle tint
  ink: "#121A2E"              # headings (navy as ink)
  ink-body: "#334155"         # Slate 700, body
  ink-muted: "#64748B"        # secondary / hints
  hairline: "#E2E8F0"         # 1px borders (no shadows)
  hairline-strong: "#CBD5E1"
  # secondary accent + semantics (sparse)
  teal: "#35B6AE"             # hover cues, charts, secondary accent (~10%)
  gold: "#E8AB42"             # single emphasis word / certification edge only (~5%)
  risk-high: "#E24B4A"        # risk band "High" pill
  risk-high-bg: "#FCEBEB"
  success: "#07B981"

typography:
  display-xl:                 # H1 hero
    fontFamily: Inter Display
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -1.4px
  display-lg:                 # section H2
    fontFamily: Inter Display
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.8px
  headline:                   # H3 / card titles
    fontFamily: Inter
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  subhead:
    fontFamily: Inter
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.1px
  body:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  eyebrow:                    # section kicker / step label
    fontFamily: Inter
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px      # the one place tracking opens (uppercase kicker)
  pill:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px       # cards
  xl: 16px       # hero snapshot, output preview
  pill: 9999px   # buttons, step badges, metric pills

spacing:
  base: 8px      # 8px scale; 4px for component-internal gaps
  section-y: 96px       # desktop vertical section padding
  section-y-mobile: 56px
  container-max: 1120px
  gutter: 24px

elevation:
  # No drop shadows. Depth = hairline borders + surface tint layering.
  card: "1px solid #E2E8F0"
  card-float: "1px solid #CBD5E1"   # hero snapshot / output preview (slightly stronger hairline)

motion:
  duration: 200ms
  easing: cubic-bezier(0.2, 0.8, 0.2, 1)
  rules: "Purposeful only. Journey strip = subtle progress fill on the connector. No scroll-jacking, no rotating cards, no animated number counters, respect prefers-reduced-motion."

# ---- Component rules ----
components:
  button-primary: "Verification Green bg + white label, pill radius, 600 weight. The single dominant action per viewport. Repeated at Hero, Discover, Assess, Final CTA."
  button-secondary: "Transparent bg, 1px navy hairline, navy label. Used for the secondary hero action and 'Download guide'. Never a second green button."
  cta-link: "Inline text link in green with a trailing arrow (ti-arrow-right) for in-section step CTAs (Discover/Assess/Fix)."
  card: "White surface, 1px hairline, lg radius, no shadow. Used for steps, deliverables, output preview."
  snapshot-card: "Hero right-side 'DPDPA Data Snapshot', white, xl radius, card-float hairline. Lists found data with ti-check rows, a High risk pill (risk-high), and a recommended next step. Demonstrates the product outcome above the fold."
  trust-strip: "Compact single row of honest metrics + press names directly under hero. Never inflated. 'Sector assessments live for priority industries' until all 12 are verified live."
  dark-band: "Navy bg, on-navy text, green CTA. Used ONLY twice: Journey strip and Final CTA."

# ---- Conversion contract ----
conversion:
  primary-goal: "Start free Data Discovery scan (then route to sector assessment)."
  one-cta-per-viewport: true
  trust-before-ask: "Founder proof renders BEFORE Get help (consultation CTA)."
  five-second-answers: ["What is this? Find your DPDPA risk", "Is it for me? Indian businesses, sector-specific", "What next? Start with Data Discovery"]
  honesty: "No metric inflation. Risk explained calmly, never fear theatre (brand non-negotiable)."

# ---- Section order (founder-locked) ----
page-order:
  - nav
  - hero
  - trust-strip
  - journey-strip      # dark
  - discover
  - assess
  - fix
  - founder-proof      # tinted, moved BEFORE get-help
  - get-help           # soft green tint
  - briefings
  - newsletter
  - final-cta          # dark
  - footer             # resources moved here: FAQ, Glossary, Blog, Media, About, Legal
