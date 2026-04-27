# Example: New Feature

**Request:** "Add appointment reminders — SMS and email — 24 hours before the appointment."

---

## Classification
```
Work type:    new-feature
Surface area: backend + frontend + api (Twilio / SendGrid integration)
User impact:  user-facing (patient receives reminder, receptionist configures it)
Risk level:   medium (new third-party integration, user data used for messaging)
Reversibility:moderate (can disable the cron job, but messages already sent can't be recalled)
Route:        B (New Feature)
```

---

## Phase Sequence

**Phase 0 — Intent Gate** → `goal-driven-execution` + `think-before-coding`
```
Goal: Reduce appointment no-shows by sending automated reminders 24h before scheduled time.
User: Patients (receive reminder), clinic staff (configure on/off per patient)
Success: ≥80% reminder delivery rate; no-show rate drops by measurable % within 4 weeks
Out of scope: Reminders <24h, WhatsApp, custom reminder timing (v2)
Risk: medium — third-party delivery, patient contact data used
Reversibility: moderate — disable cron, messages already sent are irreversible
```

**Phase 1 — UX Gate** → `uiux-designer`
```
User flow:
  Patient → receives SMS/email at T-24h → taps link → sees appointment detail
  Staff → appointment settings → toggle "Enable reminders" per appointment
Primary action: reminder delivery (automated); staff toggle (manual)
States: reminder sent ✅ / delivery failed ⚠️ / patient opted out / no contact on file
Accessibility: email must be readable without images; SMS plain text only
Responsive: email template mobile-first (60%+ open on mobile)
```

**Phase 2 — Planning Gate** → `superpowers-write-plan`
```
Assumptions:
  - Twilio for SMS, SendGrid for email (already have accounts)
  - Appointment data in existing DB with patient contact fields
  - Cron runs daily at 8am IST

Files affected:
  - lib/reminders.ts (new — reminder logic)
  - app/api/cron/reminders/route.ts (new — cron endpoint)
  - components/AppointmentSettings.tsx (add toggle)
  - db/schema.sql (add reminder_sent boolean)

Plan:
  Task 1: Schema migration → verify: migration runs without error
  Task 2: Write reminder service (lib/reminders.ts) → verify: unit tests pass
  Task 3: Write cron endpoint → verify: triggers correctly in test env
  Task 4: Add staff toggle to UI → verify: toggle saves, renders all states
  Task 5: Email template → verify: renders correctly on mobile
```

**Phase 3 — Build** → `superpowers-tdd` + `surgical-changes`
- Write failing test for reminder service first (patient gets reminder 24h before)
- Implement minimal service — no extra features
- Do not modify unrelated appointment logic

**Phase 4 — Verification** → `superpowers-verify` + `uiux-accessibility-review`
```
Tests: 12 passed / 0 failed
Build: ✅
Typecheck: ✅
Email template: tested on Gmail mobile (✅), Gmail desktop (✅), Outlook (✅)
Accessibility: email alt text ✅, SMS plain text ✅
Manual test: triggered reminder in test env, received SMS + email within 60s
```

**Phase 5 — Finish** → `superpowers-finish`
```
Summary: Appointment reminder system — SMS via Twilio, email via SendGrid, cron at 8am IST
Verified: 12 tests passing, manual delivery confirmed, email template tested
Remaining risks: Twilio/SendGrid delivery rate not measured yet; monitor first week
Next: PR → merge → monitor delivery logs for 7 days
```
