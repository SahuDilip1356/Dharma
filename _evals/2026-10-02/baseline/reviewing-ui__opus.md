## Q1

Files read: SKILL.md, audit.md, accessibility-review.md, responsive-review.md, interaction-review.md, design-qa.md

This is a new component that ships to every visitor, so I'd run the full five-step review in the order SKILL.md gives, not the quick one.

**What I'd run (dry run, nothing executed):**
1. Read `components/ConsentBanner.tsx`, plus its styles and any `useConsent` hook or cookie helper it imports.
2. **Audit (audit.md):** fetch the current guidelines from `https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md` with WebFetch. If that fails, use the 18 built-in categories.
3. **Accessibility:** `npx @axe-core/cli http://localhost:3000` with the banner showing, then a manual keyboard pass.
4. **Responsive:** take screenshots at 375, 768, 1280 and 1440px with Playwright (the webapp-testing skill).
5. **Interaction:** go through the state matrix for each button.
6. **Design QA:** only after steps 2 and 3 pass.

**Checks that matter most for a consent banner:**
- **Semantics/ARIA:** it should be `role="dialog"` or `role="region"` with `aria-labelledby` pointing at the heading. Accept, Reject and Manage must be `<button>` elements, not `<div onClick>`. The privacy policy link must be a real `<a href>`.
- **Keyboard:** the banner must be reachable early in tab order and must not trap focus unless it's a modal. If it is a modal, focus stays inside it, Escape is handled deliberately, and focus goes back to the page when it closes.
- **Equal choice:** "Reject All" needs the same visual weight as "Accept All". A greyed-out link-style reject is a dark pattern (check 10, CTA clarity, plus regulatory risk under GDPR and DPDPA). I'd call this a ship blocker.
- **Contrast:** 4.5:1 for body text and 3:1 for button borders and the focus ring.
- **Mobile at 375px:** no horizontal scroll, buttons at least 44×44px with an 8px gap, `padding-bottom: env(safe-area-inset-bottom)` on a fixed bottom bar, and the banner must not cover the whole viewport with no way to scroll.
- **States:** a loading/disabled state while consent is being saved, and an error state if the save fails. Check the banner doesn't reappear after a choice (hydration: read the cookie on the client without a server/client mismatch).
- **Animation:** honour `prefers-reduced-motion`. Slide-in should be 200ms and animate transform only, never `transition: all`.
- **Copy:** Title Case, specific button labels ("Accept All Cookies", not "OK"), and `…` instead of `...`.

**Output:** findings in the SKILL.md format, sorted by severity:
```
[critical] components/ConsentBanner.tsx:<line> — <rule> — <exact fix>
```
followed by the design-qa report ending in **SHIP** or **HOLD**.

**One thing to settle first:** the files use different severity scales. SKILL.md uses critical/serious/moderate/minor, audit.md uses [HIGH]/[MED]/[LOW], and accessibility-review.md uses CRITICAL/SERIOUS. I'd convert everything to the SKILL.md scale (HIGH→critical/serious, MED→moderate, LOW→minor).

I can't give real `file:line` findings without the file. Once you share it, or confirm the repo path, I'll run the steps above.

## Q2

Files read: SKILL.md, responsive-review.md, design-qa.md

This is a quick review ("check mobile"), so I'd run step 3 (responsive) and then step 5 (design QA), as SKILL.md requires.

**Clarifying questions:**
1. Which file or route is the pricing page (for example `app/pricing/page.tsx`), and is a dev server running?
2. Mobile only, or all four breakpoints?

**Assumptions if you don't answer:** route `/pricing` on `localhost:3000`, and I check all four breakpoints with the emphasis on 375px.

**What I'd run:** a Playwright script (webapp-testing) that sets the viewport to 375×812, 768×1024, 1280×800 and 1440×900, takes full-page screenshots, and logs `document.documentElement.scrollWidth > innerWidth` to catch horizontal overflow. Then I'd read the page source against responsive-review.md.

**Pricing-page specifics I'd check:**
- Plan cards: 3–4 columns must stack to one at 375px. Fixed `px` widths on cards cause overflow.
- Feature comparison table: needs an `overflow-x-auto` wrapper or a card or accordion layout on mobile.
- Monthly/annual toggle: 44×44px target, works without hover, `touch-action: manipulation`.
- Prices: `tabular-nums` and `Intl.NumberFormat` for currency.
- Highlighted "Most Popular" plan: still visually dominant when stacked, ideally first or clearly marked.
- CTAs: full-width or at least 44px tall, one primary per card.
- Tooltips on feature rows: hover-only tooltips don't work on touch, so they need a tap or focus alternative.
- `100vh` hero → `100dvh`. Check the viewport meta and that pinch-zoom isn't disabled.

**Output:** grouped by breakpoint, per responsive-review.md:
```
### 375px (Mobile)
app/pricing/page.tsx:<line> [HIGH] comparison table overflows → wrap in overflow-x-auto
### Touch Targets
...
```
Then the design-qa report with SHIP or HOLD.

**Caveat:** SKILL.md says step 5 runs only after steps 2 (accessibility) **and** 3 pass. This request only covers responsive, so I'd either run a light accessibility pass too or mark the SHIP/HOLD call provisional pending an accessibility review.

## Q3

Files read: SKILL.md

This skill reviews UI that's already built: accessibility, responsive, interaction and visual QA with a ship/hold call. It doesn't design new pages, so I won't force a landing-page design through it.

**What I'd do instead:** switch to the **designing-ui** skill (or frontend-design), which is the right tool for creating a Healthcare Clinic SaaS landing page. Before that, a few questions:
1. Who's the primary audience: clinic owners and admins, doctors, or patients?
2. What's the one primary conversion: book a demo, start a free trial, or something else?
3. Is there an existing brand or design system (colors, type, logo)?
4. What's the target stack (Next.js + Tailwind?) and where should the file live?
5. Are there compliance messages to lead with (HIPAA, DPDPA, data residency)?

**Where this skill comes back in:** once the page is built, rerun `reviewing-ui` on it. Its healthcare rules will apply (accessibility-review.md has a healthcare section: AAA/7:1 contrast for clinical text, never status by color alone, no auto-advancing carousels), then responsive at 4 breakpoints, then design QA for the ship/hold call.

Do you want me to start the design with the designing-ui skill?
