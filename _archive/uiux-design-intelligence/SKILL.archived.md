---
name: uiux-design-intelligence
description: |
  Design system selection engine — choose the right visual style, color palette, typography,
  and motion system for any product. Powered by UI UX Pro Max's 161 reasoning rules,
  71 design styles, 99 UX guidelines, and curated color/font databases. Triggers when:
  - User says "what style should I use", "suggest a design direction", "pick colors/fonts"
  - Starting a new product or feature and need a visual language
  - uiux-designer master skill needs to select design direction (Step 5 of design process)
  - Inconsistent or undifferentiated visual design needs a system

  Output: Named style + color palette + font pairing + motion spec + anti-patterns to avoid.

license: MIT
metadata:
  author: Dilip Sahu
  source: UI UX Pro Max / Antigravity Kit design intelligence database
  version: "1.0.0"
---

# UI/UX Design Intelligence (UI UX Pro Max)

**Purpose:** Match product type → proven visual system. No guessing. No generic purple gradients.

---

## Decision Framework: Product Type → Design System

### Step 1: Identify Product Category

| Product Type | Recommended Style | Why |
|-------------|------------------|-----|
| SaaS Dashboard | Glassmorphism + flat data density | Trust + data clarity |
| Healthcare App | Clean Minimalism + WCAG-AAA | Safety, compliance, accessibility |
| Fintech / Banking | Dark mode + glassmorphism | Premium, focus, data-dense |
| E-commerce | Conversion-optimized + clean | CTA prominence, trust signals |
| Developer Tools | Monochrome + code-dark | Reduces cognitive load, respects terminal roots |
| AI Product | Soft gradients + ambient animation | Future-forward without neon gimmicks |
| Enterprise Admin | Information Architecture first | Efficiency, scannability, density |
| Landing Page (B2B SaaS) | Swiss/Minimalism + bold type | Trust, clarity, conversion |
| Landing Page (Consumer) | Neubrutalism OR Glassmorphism | Memorability, brand personality |
| Mobile App | Bauhaus OR Minimalist Monochrome | Touch-first, thumb zones |
| Gaming / Entertainment | Cyberpunk OR Dark Neon | Immersion, energy |
| Legal / Insurance | Classic Corporate + high contrast | Trust, formality |

---

## The 71 Design Style Database (Key Entries)

### Tier 1: Production-Proven (High Conversion, Accessible)

**1. Swiss / International Style (Minimalism)**
- Keywords: White space, grid-based, sans-serif, geometric, high contrast
- Colors: Pure white `#FFFFFF` + near-black `#111111` + one accent (red `#FF0000` or electric blue `#0057FF`)
- Effects: Subtle hover transitions 150–200ms ease-out; no decorative animation
- Best for: B2B SaaS, enterprise, developer tools, documentation
- Avoid for: Consumer entertainment, gaming, youth brands
- Accessibility: WCAG AAA ✓ | Performance: ⚡ Excellent

**2. Glassmorphism**
- Keywords: Frosted glass, backdrop-filter blur, semi-transparent panels, layered depth
- Colors: Dark background `#0A0A0F` + glass `rgba(255,255,255,0.08)` + accent `#6C63FF` or `#00D9FF`
- CSS: `backdrop-filter: blur(20px) saturate(180%); background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15)`
- Effects: 300–400ms transitions; subtle glow on hover
- Best for: SaaS dashboards, fintech, AI products, premium apps
- Avoid for: Healthcare (trust concerns), legal/insurance, very performance-sensitive pages
- Performance: ⚡ Good (use sparingly — `backdrop-filter` is GPU-intensive)

**3. Flat Design 2.0**
- Keywords: Clean, minimal shadows, bold color blocks, strong typography
- Colors: Primary `#0057FF` + neutral `#F5F5F5` + text `#1A1A1A`
- Effects: Color-only transitions, no blur/shadow animation
- Best for: Productivity apps, mobile apps, admin panels
- Accessibility: WCAG AA ✓ | Performance: ⚡ Excellent

**4. Neumorphism (Soft UI)**
- Keywords: Extruded plastic, soft shadows, same-hue highlights, tactile
- CSS: `box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #ffffff`
- Colors: Light gray base `#E0E5EC` only — never dark mode
- Effects: Pressed state reverses shadow direction
- Best for: Audio/music apps, calculator UIs, niche tactile products
- Avoid for: Data-dense dashboards, text-heavy content, dark mode
- Accessibility: Low contrast risk — requires careful audit ⚠️

**5. Neubrutalism**
- Keywords: Bold borders, bright pop colors, hard box shadows, raw typography, no blur
- CSS: `border: 2px solid #000; box-shadow: 4px 4px 0px #000`
- Colors: Yellow `#FFE000` + black `#000000` + white `#FFFFFF` + one pop accent
- Effects: Transform on hover: `transform: translate(-2px, -2px)`; shadow expands
- Best for: Gen Z brands, creative agencies, startups wanting personality
- Avoid for: Healthcare, finance, enterprise, anything trust-critical
- Accessibility: Excellent contrast naturally | Performance: ⚡ Excellent

**6. Dark Minimal (Developer / Terminal)**
- Keywords: Near-black background, monospace type, subtle grid, code-native
- Colors: `#0D1117` (GitHub dark) + `#C9D1D9` text + accent `#58A6FF` (blue) or `#3FB950` (green)
- Effects: Cursor blink animations; 150ms transitions only
- Best for: Developer tools, CLI products, code editors, technical SaaS
- Avoid for: Consumer apps, B2C, anything non-technical

**7. Corporate Clean (Enterprise SaaS)**
- Keywords: Blue-dominant, structured layout, data tables, side navigation
- Colors: Navy `#1B2B4B` + white `#FFFFFF` + blue `#0066CC` + gray `#6B7280`
- Effects: Minimal — subtle hover states, no decorative motion
- Best for: Enterprise software, admin panels, B2B SaaS
- Accessibility: WCAG AA ✓ | Performance: ⚡ Excellent

**8. Spatial UI (VisionOS / Immersive)**
- Keywords: Frosted glass panels, Z-depth layering, ambient glow, eye-gaze responsive
- CSS: `backdrop-filter: blur(40px) saturate(180%); background: rgba(255,255,255,0.12)`
- Effects: Scale on gaze hover; depth offset on pinch interaction
- Best for: VisionOS apps, immersive web experiences
- Avoid for: Standard web/mobile — severe performance cost

---

## Color Palette Logic (from 161-palette database)

### By Product Mood

| Mood | Primary | Secondary | Accent | Background |
|------|---------|-----------|--------|------------|
| Trust (Finance/Healthcare) | Navy `#1B3A6B` | Cool gray `#F2F4F7` | Teal `#00A896` | White `#FFFFFF` |
| Energy (Consumer/Gaming) | Electric blue `#0057FF` | Black `#0A0A0A` | Neon green `#39FF14` | Dark `#0D0D0D` |
| Premium (SaaS/AI) | Deep purple `#6C63FF` | Dark `#0A0A0F` | Gold `#FFD700` | `#0A0A0F` |
| Calm (Wellness/Health) | Sage green `#5B8C5A` | Off-white `#F8F6F2` | Warm sand `#E8D5B7` | `#FAFAF8` |
| Minimal (Dev Tools) | Pure black `#000000` | White `#FFFFFF` | Blue `#0057FF` | `#FAFAFA` |
| Conversion (E-commerce) | Orange `#FF5722` | White `#FFFFFF` | Black `#111111` | White `#FFFFFF` |

### Contrast Requirements (Non-Negotiable)
- Normal text (< 18px or < 14px bold): minimum **4.5:1** (WCAG AA)
- Large text (≥ 18px or ≥ 14px bold): minimum **3:1**
- UI components (buttons, inputs, focus rings): minimum **3:1**
- WCAG AAA target (healthcare, accessibility-critical): **7:1**

---

## Typography Pairings (from 57-font database)

| Product Type | Heading | Body | Code | Import |
|-------------|---------|------|------|--------|
| SaaS / Enterprise | Inter | Inter | JetBrains Mono | `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700')` |
| B2B Landing | Sora or Plus Jakarta Sans | Inter | — | Google Fonts |
| Developer Tools | JetBrains Mono | Inter | JetBrains Mono | — |
| Consumer / Brand | Clash Display | Satoshi | — | Custom / CDN |
| Premium SaaS | Instrument Serif | Inter | — | Google Fonts |
| Healthcare | Nunito | Source Sans Pro | — | High readability focus |
| Editorial / Blog | Playfair Display | Lora | — | Serif pair |

### Typography Scale (Modular — 1.25 ratio)
```
xs:   12px
sm:   14px
base: 16px
lg:   20px
xl:   24px
2xl:  30px
3xl:  38px
4xl:  48px
5xl:  60px
```

Line height: **1.5** for body, **1.2** for headings. Max line length: **65–75ch**.

---

## Motion System

### Timing Conventions (from UI UX Pro Max reasoning rules)
| Interaction Type | Duration | Easing |
|-----------------|----------|--------|
| Micro-interaction (hover, focus) | 150ms | ease-out |
| Component enter/exit | 200–250ms | ease-in-out |
| Page transition | 300–400ms | ease-in-out |
| Premium/brand moments | 400–600ms | custom cubic-bezier |
| Loading skeleton | 1500ms | linear (loop) |

**Rule:** Animate `transform` and `opacity` only. Never animate `width`, `height`, `top`, `left` — triggers layout.

**Always:** `@media (prefers-reduced-motion: reduce)` → disable or set to instant.

---

## Reasoning Rules by UI Category (Key Patterns)

| UI Category | Pattern | Style Priority | Anti-Patterns |
|-------------|---------|----------------|---------------|
| SaaS Dashboard | Data-dense + dark mode | Glassmorphism + flat | Excessive animation, poor contrast |
| Healthcare App | Clean + accessible | WCAG-AAA + minimal | Bright neon, complex animation |
| Fintech / Trading | Real-time numbers + dark | Dark glassmorphism | Color-only data encoding |
| E-commerce | Conversion-first | CTA-dominant, clean | Slow load, unclear hierarchy |
| AI Product | Streaming text + ambient | Soft gradients + glow | Generic AI purple on non-AI apps |
| Developer Tool | Code-native + efficient | Dark minimal | Decorative elements, slow load |
| Onboarding Flow | Progressive disclosure | Minimal + guided | Too many steps, no skip option |
| Admin Panel | Scannable + structured | Table-first, sidebar nav | Excessive white space, poor density |
| Landing Page | Conversion-optimized | Bold hero, clear CTA | Weak hierarchy, vague headlines |

---

## Design System Variables Template

```css
:root {
  /* Colors */
  --color-primary: #0057FF;
  --color-primary-hover: #0047D0;
  --color-bg: #FFFFFF;
  --color-surface: #F5F7FA;
  --color-border: #E2E8F0;
  --color-text: #1A1A1A;
  --color-text-muted: #6B7280;
  --color-error: #DC2626;
  --color-success: #16A34A;

  /* Spacing (4px base) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);

  /* Motion */
  --motion-fast: 150ms ease-out;
  --motion-base: 200ms ease-in-out;
  --motion-slow: 300ms ease-in-out;
}
```

---

## Output Format

When recommending a design system, deliver:

```
Product type: [identified]
Recommended style: [name from database]
Why: [one sentence — product/user fit]

Color palette:
  Primary:    #[hex] — [role]
  Background: #[hex]
  Surface:    #[hex]
  Text:       #[hex]
  Accent:     #[hex]
  Error:      #[hex]

Font pairing:
  Heading: [family] [weights]
  Body:    [family] [weights]
  Import:  [Google Fonts URL or package]

Motion:
  Micro:   150ms ease-out
  Default: 200ms ease-in-out
  Page:    300ms ease-in-out
  Reduced: instant (prefers-reduced-motion)

Anti-patterns to avoid: [3-5 specific to this style/product type]
```
