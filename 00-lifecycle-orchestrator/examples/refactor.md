# Example: Refactor

**Request:** "The appointment booking logic is spread across 4 files and impossible to follow — clean it up."

---

## Classification
```
Work type:    refactor
Surface area: backend
User impact:  none (internal — no user-visible change)
Risk level:   medium (core booking path, no behavior change intended)
Reversibility:easy (git revert if tests break)
Route:        E (Refactor)
```

---

## Phase Sequence

**Phase 0 — Intent Gate** → `karpathy-discipline` + `think-before-coding`

```
Goal: Consolidate appointment booking logic into a single service module.
User: Engineering team (faster onboarding, safer future changes)
Success: All existing booking tests pass before and after. Zero behavior change.
Out of scope: Performance optimization, new features, API changes, DB schema changes.
Risk: medium — core path touched; test suite must be the safety net.
Reversibility: easy — git history preserved.

Assumptions:
  - Existing tests cover the booking flow adequately
  - No external callers depend on internal module paths (only the API layer)
  - TypeScript — types will be preserved exactly

Before starting: run full test suite, record baseline.
  Baseline: 47 tests, 0 failures.
```

**Phase 2 — Planning Gate** → `simplicity-first`

```
Current state (4 files):
  - lib/booking.ts          (availability check)
  - lib/appointments.ts     (create/cancel logic)
  - utils/booking-helpers.ts (date calculations)
  - services/notification.ts (mixed with booking logic — needs extraction)

Target state:
  - lib/appointments/index.ts      (public API — what callers import)
  - lib/appointments/availability.ts
  - lib/appointments/operations.ts  (create, cancel, reschedule)
  - lib/appointments/scheduling.ts  (date/time calculations)
  - services/notification.ts        (notification only — booking logic removed)

Plan:
  Task 1: Run tests, confirm 47 passing → verify: 47 passed, 0 failed
  Task 2: Create new folder structure, move availability.ts → verify: imports resolve, tests still pass
  Task 3: Move operations.ts → verify: tests still pass
  Task 4: Move scheduling.ts → verify: tests still pass
  Task 5: Extract booking logic from notification.ts → verify: tests still pass
  Task 6: Update all callers to import from new paths → verify: build passes, tests pass
  Task 7: Delete old files → verify: no broken imports, tests pass
  Task 8: Final suite run → verify: 47 passed, 0 failed (or more if new tests added)
```

**Phase 3 — Build** → `surgical-changes`

```
Rules enforced:
  - Move code — do not rewrite it
  - Match existing style exactly (naming, spacing, comment style)
  - Do not add new abstractions while moving
  - Do not fix unrelated issues spotted during the move (surface them, don't fix)
  - Do not add or remove exports beyond what the refactor requires

Pre-existing issues noticed (NOT changed):
  - createAppointment() has a hardcoded timezone string "Asia/Kolkata" — surfaced, not fixed
  - utils/booking-helpers.ts has dead helper `roundToNearestSlot()` — surfaced, not deleted
```

**Phase 4 — Verification**
```
Before: 47 tests passed, 0 failed ✅
After:  47 tests passed, 0 failed ✅
Build:  ✅ (no import errors)
Typecheck: ✅
Behavior: identical (verified by test parity)
Diff: 7 files moved/renamed, 0 lines of logic changed
```

**Phase 5 — Finish**
```
Summary: Appointment booking logic consolidated from 4 files into lib/appointments/ module
Verified: identical test results before and after; build clean
Remaining risks: none — behavior unchanged, confirmed by tests
Pre-existing issues surfaced (for separate tasks):
  - Hardcoded timezone in createAppointment()
  - Dead helper roundToNearestSlot()
Next: PR → merge
```
