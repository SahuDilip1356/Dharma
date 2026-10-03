# Responsive Design Review

## Contents

- [Audit Checklist](#audit-checklist)
  - [1. Viewport and Meta](#1-viewport-and-meta)
  - [2. Layout at Each Breakpoint](#2-layout-at-each-breakpoint)
  - [3. Touch Targets (Mobile)](#3-touch-targets-mobile)
  - [4. Typography at Mobile](#4-typography-at-mobile)
  - [5. Safe Areas (Notch/Island Devices)](#5-safe-areas-notchisland-devices)
  - [6. Forms on Mobile](#6-forms-on-mobile)
  - [7. Scroll Behavior](#7-scroll-behavior)
  - [8. Images and Media](#8-images-and-media)
  - [9. Navigation Patterns](#9-navigation-patterns)
  - [10. Overflow and Clipping](#10-overflow-and-clipping)
- [CSS Anti-Patterns to Flag](#css-anti-patterns-to-flag)
- [Output Format](#output-format)


**Breakpoints tested:**
- `375px` — mobile (iPhone SE / small Android)
- `768px` — tablet (iPad portrait)
- `1280px` — desktop (laptop)
- `1440px` — wide desktop (external monitor)

---

## Audit Checklist

### 1. Viewport and Meta
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">` present
- [ ] No `user-scalable=no` or `maximum-scale=1` — pinch zoom must not be disabled
- [ ] `color-scheme` meta tag matches the page theme

### 2. Layout at Each Breakpoint

**375px (mobile):**
- [ ] No horizontal scroll — content fits within viewport width
- [ ] Text does not overflow container
- [ ] Images scale (`max-width: 100%` or Next.js `<Image>` fills)
- [ ] Tables: horizontal scroll container or card layout alternative
- [ ] Sidebar/navigation: collapsed (hamburger, bottom nav, or drawer)
- [ ] Multi-column layouts stack to single column
- [ ] Forms: single-column input layout
- [ ] Modals: full-screen or bottom sheet on mobile

**768px (tablet):**
- [ ] Layout transitions from single to multi-column appropriately
- [ ] Navigation: visible or semi-collapsed (depends on design)
- [ ] Tables: usable without horizontal scroll (or clearly scrollable)
- [ ] Images maintain correct aspect ratios

**1280px (desktop):**
- [ ] Content max-width applied (not full 1280px for text)
- [ ] Sidebar visible and functional
- [ ] Multi-column layout correct
- [ ] Hover states work (desktop-only states active)

**1440px (wide):**
- [ ] Content does not stretch unreadably wide
- [ ] Max-width container centered
- [ ] No layout breakage from extra space

### 3. Touch Targets (Mobile)
- [ ] All interactive elements: minimum **44×44px** tap target
- [ ] Adjacent interactive elements: minimum **8px gap**
- [ ] `touch-action: manipulation` on interactive elements (removes 300ms tap delay)
- [ ] No hover-only interactions (hover states invisible on touch)
- [ ] `-webkit-tap-highlight-color` set intentionally (not default blue flash)

### 4. Typography at Mobile
- [ ] Body text: minimum **16px** on mobile (prevents iOS auto-zoom on focus)
- [ ] Line length: max **65–75ch** (also applies to mobile — narrower container)
- [ ] Headings: reduce scale on mobile (display headings too large for 375px)
- [ ] `text-wrap: balance` on headings (prevents single-word orphan lines)

### 5. Safe Areas (Notch/Island Devices)
- [ ] Full-bleed layouts use `env(safe-area-inset-top/bottom/left/right)`
- [ ] Fixed bottom bars: `padding-bottom: env(safe-area-inset-bottom)`
- [ ] Side-edge full-bleed: `padding-left: env(safe-area-inset-left)`

### 6. Forms on Mobile
- [ ] Inputs use correct `type` and `inputMode` for appropriate keyboard:
  - Email → `type="email"` → email keyboard
  - Phone → `type="tel"` → numeric keyboard
  - Number → `inputMode="numeric"` → numeric keyboard
  - Search → `type="search"` → search keyboard with return key
- [ ] Input font-size: minimum **16px** (prevents iOS auto-zoom on focus)
- [ ] Labels visible above input (not inside — mobile has no hover label reveal)
- [ ] Submit button: full-width on mobile, or at least 44px height

### 7. Scroll Behavior
- [ ] `overscroll-behavior: contain` on modals, drawers, and sheets
- [ ] No scroll-jacking (custom scroll that overrides native behavior)
- [ ] Sticky elements account for scroll offset (`scroll-margin-top`)
- [ ] Long lists (>50 items): virtualized or paginated on mobile

### 8. Images and Media
- [ ] All images: explicit `width` and `height` (prevents layout shift)
- [ ] Below-fold images: `loading="lazy"`
- [ ] Hero/above-fold images: `fetchpriority="high"`
- [ ] No auto-playing video on mobile (data consumption + distraction)
- [ ] `<picture>` or srcset for responsive image sizes

### 9. Navigation Patterns
- [ ] Mobile nav: bottom nav / hamburger / drawer — never force desktop nav on mobile
- [ ] Active state visible in mobile nav
- [ ] Back button behavior predictable (history preserved correctly)
- [ ] Deep links work on mobile (URL reflects state)

### 10. Overflow and Clipping
- [ ] No `overflow-x: hidden` on `<body>` without testing — it can kill sticky positioning
- [ ] Flex children containing text: `min-w-0` to allow text truncation
- [ ] Long words: `overflow-wrap: break-word` on content containers
- [ ] Z-index: fixed elements don't clip modal overlays

---

## CSS Anti-Patterns to Flag

| Found | Problem | Fix |
|-------|---------|-----|
| `100vh` on mobile | Browser chrome causes content cut-off | Use `100dvh` or `min-h-screen` with Tailwind |
| Fixed `px` widths | Doesn't adapt to viewport | Use `%`, `vw`, `max-width` |
| `hover:` only interactions | Invisible on touch | Add `active:` or `focus:` alternatives |
| `overflow: hidden` on container | Clips focus rings | Use `overflow: clip` or test carefully |
| `position: fixed` nav + `100vh` content | Content hidden behind nav | Use `padding-top` or `calc` |

---

## Output Format

```
## Responsive Review: [feature / component name]

### 375px (Mobile)
components/Dashboard.tsx:34  [HIGH] horizontal scroll — content overflows at 375px
  → Wrap table in: <div className="overflow-x-auto">

components/Modal.tsx:12      [HIGH] modal not full-screen on mobile
  → Add: sm:max-w-full sm:h-full sm:rounded-none sm:m-0

components/Input.tsx:8       [MED]  font-size 14px causes iOS auto-zoom on focus
  → Change to: text-base (16px minimum)

### 768px (Tablet)
components/Nav.tsx:22        [MED]  sidebar still hidden at 768px — appears at 1024px
  → Consider showing collapsed sidebar at 768px

### 1280px (Desktop)
components/Layout.tsx:5      [LOW]  content stretches full 1280px — no max-width cap
  → Add: max-w-screen-xl mx-auto

### 1440px (Wide)
✓ pass — max-width container centered correctly

### Touch Targets
components/IconButton.tsx:18 [HIGH] touch target 24×24px — below 44×44px minimum
  → Add: p-3 to increase hit area, or min-w-[44px] min-h-[44px]
```
