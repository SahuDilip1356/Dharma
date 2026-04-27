# Example: Bug Fix

**Request:** "The patient intake form is submitting twice — I'm seeing duplicate records in the database."

---

## Classification
```
Work type:    bug-fix
Surface area: frontend + backend
User impact:  user-facing (data integrity issue — duplicate patient records)
Risk level:   high (production data affected, existing records corrupted)
Reversibility:hard (duplicate records may need manual cleanup)
Route:        C (Bug Fix)
```

## Escalation
```
⚠️ Escalation: medium → high

Trigger: Production data affected (duplicate patient records)
Risk: Existing records in production may be duplicated; deduplication may be required
Scope: Patient intake form submission handler + DB write path
Rollback: Disable form submission endpoint, revert to previous deploy
```

---

## Phase Sequence

**Phase 0** → `superpowers-debug` + `think-before-coding`

```
Root cause investigation:
1. Read error: no explicit error — symptom is duplicate DB rows
2. Reproduce: submit intake form once → check DB → 2 rows appear
3. Recent changes: last commit touched the form submit handler
4. Trace backward:
   - Form onSubmit fires → calls submitPatient() → POST /api/patients
   - Network tab shows: two POST requests fire on one button click
5. Hypothesis: button not disabled during request → double-click or React StrictMode double-invoke

Evidence: Network tab captured — 2x POST /api/patients with identical payloads, 180ms apart
Root cause: Submit button remains enabled during async request; double-submit possible
```

**Phase 3 — Build** → `surgical-changes` + `superpowers-tdd`

```
Failing test (written first):
  test("prevents double submission") {
    render(<IntakeForm />)
    fireEvent.submit(form)
    fireEvent.submit(form)  // second submit
    expect(mockApi).toHaveBeenCalledTimes(1)  // FAILS before fix
  }

Fix: Disable button on first submit, re-enable on success/error
  - Add `isSubmitting` state to form
  - Set button `disabled={isSubmitting}` + `aria-busy={isSubmitting}`
  - Add server-side idempotency key as secondary protection

Files changed:
  - components/IntakeForm.tsx (isSubmitting state + disabled button)
  - app/api/patients/route.ts (idempotency check on request)

Not changed: unrelated form validation, patient data schema, auth logic
```

**Phase 4 — Verification**
```
Tests: failing test now passes ✅
Full suite: 47 passed / 0 failed ✅
Manual: submitted form, clicked submit 3x rapidly → 1 DB record created ✅
Network: only 1 POST request fires ✅
Regression: existing form validation still works ✅
```

**Phase 5 — Finish**
```
Summary: Double-submit bug fixed — button disabled during request + server idempotency key
Verified: regression test passes, manual verification on dev env
Remaining risks: Existing duplicate records in production need manual audit
Next: PR → merge → run deduplication query on production (separate task)
```
