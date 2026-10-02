## Q1
Files read: SKILL.md, audit.md, accessibility-review.md, responsive-review.md, interaction-review.md, design-qa.md

This is a "before we ship" review of a single component, so the skill applies. I run the steps in order (SKILL.md), and a consent banner touches all five.

**Setup (dry run, so I only state what I would do)**
- Read `components/ConsentBanner.tsx` in full, plus its CSS/Tailwind and the place it mounts (layout/root), so findings have real `file:line` numbers. I will not invent line numbers here.
- audit.md says to fetch the Vercel guidelines first (`WebFetch https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`) and fall back to the built-in 18 categories if that fails.
- Assumption: no spec exists, so Design QA compares against the project's existing visual system. I would ask once: "Is there a design spec or Figma for the banner, and which regions (India DPDPA, EU) must it cover?"

**Step 1, Guideline audit (audit.md).** Things I would specifically check on a banner:
- Accept/Reject/Manage are `<button>`, not `<div onClick>`.
- Visible `:focus-visible` ring, no bare `outline-none`.
- `transition: all`, and `prefers-reduced-motion` honored on the slide-in.
- `touch-action: manipulation`.
- Safe-area padding for a fixed bottom bar.
- Dark mode surfaces.
- Hydration safety: reading the consent cookie or localStorage during render causes a server/client mismatch.
- Button labels are specific and in Title Case ("Accept All Cookies", not "OK").
- Reject has equal visual weight to Accept (anti-dark-pattern; compliance-relevant).

**Step 2, Accessibility (accessibility-review.md).**
- Non-modal vs modal: if it is `role="dialog"`, it needs `aria-labelledby`. If it blocks the page, it needs a focus trap and Escape handling. If it is non-blocking, use `role="region"` with `aria-label`.
- Focus must not be stolen on load, but the banner must be early in tab order or reachable via a skip link.
- Contrast: 4.5:1 minimum, and the healthcare rule asks for 7:1 on clinical text, so I would hold patient-facing copy to that.
- Links to the privacy policy need an underline.
- Toggle switches in "Manage" need a label and state beyond color.

**Step 3, Responsive (responsive-review.md).** 375/768/1280/1440: banner must not cover content or be taller than ~40% of the viewport at 375px. Buttons are at least 44x44px with an 8px gap. No `100vh`; use `100dvh`. Stack buttons full-width on mobile, and use 16px text.

**Step 4, Interaction (interaction-review.md).** State matrix for every button (hover, active, disabled, loading if it POSTs consent). Feedback after a choice (the banner dismisses, and a polite `aria-live` message confirms "Preferences saved"). Exit animation of 150ms ease-in. Error path if saving consent fails.

**Step 5, Design QA (design-qa.md).** Runs last, and only if steps 2 and 3 pass. I would take screenshots at 375/768/1280 in default, manage-preferences, and error states, then run the 14 checks (CTA clarity, generic-AI-UI check, and so on).

**Output format (SKILL.md), shown with placeholders because I haven't read the file:**
```
## components/ConsentBanner.tsx
[critical] components/ConsentBanner.tsx:<n> — Reject button hidden behind "Manage" (equal-weight rule) — add a Reject All button with the same size and style as Accept
[serious]  components/ConsentBanner.tsx:<n> — <div onClick> as Accept button — replace with <button type="button">
[moderate] components/ConsentBanner.tsx:<n> — transition: all — transition-[transform,opacity] duration-200 ease-out
[minor]    components/ConsentBanner.tsx:<n> — "..." in copy — use "…"

Final recommendation: SHIP / HOLD (N blockers)
```
Note: the skill has two severity vocabularies (critical/serious/moderate/minor in SKILL.md and accessibility-review.md, but HIGH/MED/LOW in audit.md). I would normalize to the SKILL.md scale.

## Q2
Files read: SKILL.md, responsive-review.md

"Check if the pricing page works on mobile" maps to the skill's trigger "check mobile", so this is a quick review. SKILL.md says to run only the steps the change touches, which is step 3 (Responsive). Steps 1, 2 and 4 are skipped unless I spot something along the way. Step 5 is not run, since it only follows passing steps 2 and 3 and this is not a ship call.

**Clarifying questions (brief):** Where is the page (file path or URL)? Is a dev server running? I would assume `app/pricing/page.tsx` plus a local dev URL.

**What I would do**
1. Read the pricing page and its components (plan cards, comparison table, toggle for monthly/annual, CTA buttons).
2. If a dev server is up, load it at 375 and 768 (and 1280/1440 for regression) and screenshot (for example with the browser tooling, or webapp-testing). Without a running page, do a static code review only and say so.
3. Run the responsive-review.md checklist, with the pricing-specific hot spots:
   - Viewport meta present, no `user-scalable=no`.
   - 375px: no horizontal scroll. Plan cards stack to one column. The feature comparison table is in an `overflow-x-auto` wrapper or has a card alternative. Prices and currency (₹1,299) do not overflow. Monthly/annual toggle is at least 44px.
   - 768px: transitions to 2 columns; table usable.
   - 1280/1440: max-width container centered.
   - Touch: CTA buttons are 44x44px with an 8px gap, no hover-only tooltips for feature explanations, `touch-action: manipulation`.
   - Typography: 16px body and inputs, heading scale reduced, `text-wrap: balance`.
   - Anti-patterns: `100vh`, fixed px widths, sticky header covering the content.
   - Sticky "Choose Plan" bar uses `env(safe-area-inset-bottom)`.

**Output (responsive-review format; placeholders since there is no real file):**
```
## Responsive Review: Pricing page

### 375px (Mobile)
app/pricing/page.tsx:<n> [HIGH] comparison table overflows viewport
  → Wrap in <div className="overflow-x-auto">
components/PlanCard.tsx:<n> [HIGH] CTA button 36px tall — below 44px
  → min-h-[44px]

### 768px (Tablet)  / 1280px / 1440px
✓ pass or findings

### Touch Targets
...
```
Verdict: "Works on mobile" only if there are no HIGH items at 375px. Otherwise I say which ones fail. I would also say that because I only ran the responsive pass, accessibility and states were not covered, and offer to run them.

## Q3
Files read: SKILL.md

This is not a review task. reviewing-ui "reviews built UI before it ships". Its description and flow assume existing code or screens to audit. "Design a landing page for the Healthcare Clinic SaaS" is a creation task, so I would not run the review workflow, and I would not read the checklist files.

**What I would do instead**
- Say plainly that reviewing-ui doesn't apply to designing from scratch, and hand off to the creation-side skills in this environment: `designing-ui` (or `plan-design-review` for a design spec, `frontend-design` for building it).
- Ask the questions a landing page actually needs (and that no review skill answers): Who is the buyer (clinic owner, receptionist, doctor)? Region and compliance (India/DPDPA, HIPAA)? Primary conversion (book demo, free trial)? Brand colors/logo? Existing copy or screenshots?
- Under stated assumptions, I could proceed with `designing-ui`: single primary CTA ("Book a Demo"), hero, social proof, feature sections, pricing teaser, FAQ, footer.

**How reviewing-ui would come in later:** once a draft is built, I would run it as a pre-ship gate. Accessibility steps would use the healthcare rules in accessibility-review.md (target WCAG AAA, 7:1 contrast for clinical text, status never by color alone, no auto-advancing carousels). I would then run responsive at 375/768/1280/1440 and a final Design QA with a SHIP/HOLD call.

Short reply to the user: "Designing a page is outside the review skill. I'll switch to the design workflow. A few quick questions first: [questions above]. When there's a build, I'll review it with the reviewing-ui checklist."
