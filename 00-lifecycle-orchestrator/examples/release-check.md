# Example: Release Preparation

**Request:** "We're ready to ship the appointment reminder feature — prepare the release."

---

## Routing Decision Tree

**Step 1 — High-risk surface area?**
Depends on what's included. Check the files changed in the release.
Appointment reminders → backend + third-party API (Twilio/SendGrid) → medium risk.
No auth, payments, or schema changes in this release.
→ Classify as `risk: medium`.

**Step 2 — User-facing?**
Yes — patients receive SMS/email. Clinic staff configure the toggle.
→ Phase 5 finish gate includes design-qa if UI changed.

**Steps 3–6 — Not broken, not a new feature, not new product, not refactor.**

**Step 7 — Release?**
Yes — preparing to merge and deploy.
→ Primary route: **H (Release)**

---

## Route Receipt

```
Route Receipt
─────────────────────────────────────────────
Request:        Ship appointment reminder feature
Classification: release | backend + api | user-facing | medium | moderate
Primary route:  H — Release
Supporting:     none

Skills selected:
  Phase 4: superpowers-verify (full suite + smoke test)
  Phase 5: uiux-design-qa (user-facing changes included) + superpowers-finish

Skills intentionally skipped:
  All Phase 0–3 skills — reason: release phase only; implementation is complete

Evidence required:
  - Full test suite passing
  - Build passing
  - UI smoke test (reminder toggle + email template)
  - Known risks stated
  - Rollback procedure confirmed
  - No unrelated changes bundled into this release

Stop conditions:
  🚫 Stop if: any test is failing — do not release with failing tests
  🚫 Stop if: unrelated changes are staged — scope to reminder feature only
  ⚠️ Stop if: Twilio/SendGrid credentials are not configured in production env
─────────────────────────────────────────────
```

---

## Phase Sequence

**Phase 4 — Verification** → `superpowers-verify`

```
Pre-release checklist:

Command: npm test
Output: Tests: 59 passed, 0 failed
Exit code: 0 ✅

Command: npm run build
Output: ✓ Compiled successfully
Exit code: 0 ✅

Command: npm run typecheck
Output: No errors
Exit code: 0 ✅

Environment check:
  TWILIO_ACCOUNT_SID: set in Vercel production ✅
  SENDGRID_API_KEY: set in Vercel production ✅
  CRON_SECRET: set ✅

Files in this release (git diff main..HEAD --name-only):
  lib/reminders.ts
  app/api/cron/reminders/route.ts
  components/AppointmentSettings.tsx
  db/migrations/20240127_add_reminder_sent.sql

Unrelated files staged: none ✅

Smoke test (on staging):
  - Triggered cron manually → reminder queued ✅
  - SMS received within 60s ✅
  - Email received within 90s ✅
  - Staff toggle saves and reflects correctly ✅
```

**Phase 5 — Design QA + Finish** → `uiux-design-qa` + `superpowers-finish`

```
Design QA:
  - Reminder toggle UI matches design spec ✅
  - Loading state shown during save ✅
  - Success/error states render correctly ✅
  - Email template renders on mobile (tested Gmail iOS) ✅

Known risks:
  - Twilio/SendGrid delivery rate unknown in production — monitor first 48h
  - Reminder cron fires at 8am IST — first run after deploy will be at next 8am
  - Patients who opted out before this feature existed will not have an opt-out record
    (default: opted in; will need comms if required by compliance)

Rollback procedure:
  1. Disable cron by removing CRON_SECRET from Vercel env
  2. Revert via Vercel dashboard (instant rollback to previous deploy)
  3. No DB rollback needed — reminder_sent column is additive; old code ignores it

Release summary:
  Feature: Appointment reminders (SMS via Twilio, email via SendGrid)
  Tests: 59 passing ✅
  Build: clean ✅
  Smoke: staging verified ✅
  Risk: medium — monitor delivery logs 48h post-deploy

Status: ✅ Implemented and verified with 59 passing tests, staging smoke test, and
        build + typecheck clean.
```
