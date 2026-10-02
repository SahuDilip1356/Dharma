---
name: uiux-frontend-design-system
description: |
  Define and enforce a frontend design system — tokens, component library, layout rules,
  and visual consistency standards. Triggers when:
  - Starting a new product or major UI surface that needs a visual foundation
  - Components look inconsistent across pages
  - User says "create a design system", "define tokens", "standardize components", "our UI is inconsistent"
  - Route A (new product) or Route D (UI redesign) reaches Phase 1 or Phase 2
  - uiux-designer has selected a visual direction and it needs to be codified into code

  Output: Token definitions, component inventory, layout grid, spacing scale,
  and a usage contract — all as implementable code, not just design principles.

license: MIT
metadata:
  author: Dilip Sahu
  source: UI UX Pro Max + Vercel react-best-practices
  version: "1.0.0"
---

# Frontend Design System

**Purpose:** Translate a chosen visual direction (from `uiux-design-intelligence`) into a concrete, implementable system — tokens, components, layout rules, and consistency contracts.

---

## Step 1: Audit Existing State

Before defining anything new:

```bash
# Find existing token files
find . -name "tokens*" -o -name "theme*" -o -name "tailwind.config*" | head -20

# Find existing component patterns
find . -path "*/components/ui/*" -name "*.tsx" | head -20
```

Answer:
- Do design tokens exist? (CSS variables, Tailwind config, theme file)
- Is there an existing component library? (shadcn/ui, custom, mixed)
- Are there inconsistencies? (multiple border-radius values, ad-hoc color hex values)

---

## Step 2: Define the Token Set

Based on the visual direction from `uiux-design-intelligence`, codify these tokens:

### Color Tokens
```css
/* globals.css or tokens.css */
:root {
  /* Brand */
  --color-primary:        #0057FF;
  --color-primary-hover:  #0047D0;
  --color-primary-active: #0039A6;

  /* Semantic */
  --color-success:        #16A34A;
  --color-warning:        #D97706;
  --color-error:          #DC2626;
  --color-info:           #0284C7;

  /* Neutral */
  --color-bg:             #FFFFFF;
  --color-surface:        #F8FAFC;
  --color-surface-raised: #FFFFFF;
  --color-border:         #E2E8F0;
  --color-border-strong:  #CBD5E1;

  /* Text */
  --color-text:           #1A1A1A;
  --color-text-secondary: #64748B;
  --color-text-disabled:  #94A3B8;
  --color-text-inverse:   #FFFFFF;

  /* Dark mode */
  --color-bg-dark:        #0F172A;
  --color-surface-dark:   #1E293B;
  --color-border-dark:    #334155;
  --color-text-dark:      #F1F5F9;
}
```

### Spacing Scale (4px base)
```css
:root {
  --space-px:  1px;
  --space-0-5: 2px;
  --space-1:   4px;
  --space-2:   8px;
  --space-3:   12px;
  --space-4:   16px;
  --space-5:   20px;
  --space-6:   24px;
  --space-8:   32px;
  --space-10:  40px;
  --space-12:  48px;
  --space-16:  64px;
  --space-20:  80px;
  --space-24:  96px;
}
```

### Typography Scale
```css
:root {
  --font-sans:  'Inter', system-ui, sans-serif;
  --font-mono:  'JetBrains Mono', monospace;

  --text-xs:    0.75rem;   /* 12px */
  --text-sm:    0.875rem;  /* 14px */
  --text-base:  1rem;      /* 16px */
  --text-lg:    1.25rem;   /* 20px */
  --text-xl:    1.5rem;    /* 24px */
  --text-2xl:   1.875rem;  /* 30px */
  --text-3xl:   2.25rem;   /* 36px */
  --text-4xl:   3rem;      /* 48px */

  --leading-tight:  1.2;
  --leading-normal: 1.5;
  --leading-loose:  1.75;

  --font-normal:   400;
  --font-medium:   500;
  --font-semibold: 600;
  --font-bold:     700;
}
```

### Border Radius
```css
:root {
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-full: 9999px;
}
```

### Shadow Scale
```css
:root {
  --shadow-xs: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.05);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.08), 0 4px 6px rgba(0,0,0,0.04);
  --shadow-xl: 0 20px 25px rgba(0,0,0,0.08), 0 8px 10px rgba(0,0,0,0.04);
}
```

### Motion
```css
:root {
  --motion-fast:   150ms ease-out;
  --motion-base:   200ms ease-in-out;
  --motion-slow:   300ms ease-in-out;
  --motion-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-fast:   0ms;
    --motion-base:   0ms;
    --motion-slow:   0ms;
  }
}
```

---

## Step 3: Component Inventory

List which components exist, which need creation, which need standardization:

| Component | Status | Variants | Notes |
|-----------|--------|---------|-------|
| Button | Existing | primary / secondary / ghost / destructive | Standardize focus ring |
| Input | Existing | default / error / disabled | Add success state |
| Badge / Status | Missing | success / warning / error / info | Must use icon + color + text |
| Card | Existing | flat / raised | Remove inconsistent border-radius |
| Modal | Existing | — | Add `overscroll-behavior: contain` |
| Toast | Missing | — | Create with `aria-live="polite"` |
| Skeleton | Missing | — | For loading states, replace spinners |
| Empty State | Missing | — | Consistent illustration + CTA pattern |

---

## Step 4: Layout Grid

```css
/* Page layout */
.container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-4);  /* 16px mobile */
}

@media (min-width: 768px) {
  .container { padding: 0 var(--space-6); }   /* 24px tablet */
}

@media (min-width: 1280px) {
  .container { padding: 0 var(--space-8); }   /* 32px desktop */
}

/* Content max-width for readability */
.prose { max-width: 65ch; }
```

---

## Step 5: Consistency Contract (Rules That Cannot Be Broken)

```
TOKEN RULES
  ✅ Use CSS variables / Tailwind tokens — never hardcode hex in components
  ✅ Spacing from the 4px scale — no arbitrary values without justification
  ✅ Shadows from the shadow scale — no custom box-shadow strings

COMPONENT RULES
  ✅ Status/state always uses icon + color + text — never color alone
  ✅ Every interactive element has hover + focus + active + disabled state
  ✅ Loading states use skeleton, not spinner (for content areas)
  ✅ Empty states always include a primary action CTA

TYPOGRAPHY RULES
  ✅ Max 3 font weights per surface (400, 500/600, 700)
  ✅ Body text min 16px on mobile
  ✅ Heading hierarchy sequential (h1 → h2 → h3, no skipping)
  ✅ Line length max 65–75ch for reading content

FORBIDDEN
  ❌ Hardcoded hex values in component files
  ❌ Arbitrary Tailwind values without comment justification
  ❌ Color-only status indicators (red badge with no icon or text)
  ❌ Multiple border-radius values not from the scale
  ❌ transition: all (always list properties explicitly)
```

---

## Output Format

When this skill runs, deliver:

```
Design system status:
  Existing tokens: [found / not found]
  Existing components: [list]
  Gaps identified: [list]

Token definitions: [CSS variables block]
New components needed: [list with variants]
Layout grid: [code block]
Consistency contract: [rules relevant to this product]
```
