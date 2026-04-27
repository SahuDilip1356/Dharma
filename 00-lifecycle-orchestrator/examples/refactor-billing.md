# Example: Refactor — Billing Module

**Request:** "The billing module is a mess — split it into smaller, focused files."

---

## Routing Decision Tree

**Step 1 — High-risk surface area?**
Yes — billing/payments is explicitly listed as high-risk.
→ Classify as `risk: high`. Apply Route G checks alongside primary route.
→ Stop condition: no schema mutation without explicit approval.

**Step 2 — User-facing?**
Billing module is backend logic — not directly user-facing in UI.
→ UX Gate: optional (no UI changes planned).

**Step 3 — Broken?**
No reported failure. Quality issue, not a bug.
→ Continue.

**Steps 4–5 — New feature? New product?**
No new capability. Improving structure of existing code.
→ Continue to Step 6.

**Step 6 — Refactor?**
Yes — improving structure without changing behavior.
→ Primary route: **E (Refactor)**

**Tie-breaker:** Primary intent = refactor (Route E) + high-risk billing surface (Route G supplement)

---

## Route Receipt

```
Route Receipt
─────────────────────────────────────────────
Request:        Split billing module into smaller, focused files
Classification: refactor | payments | internal | high | hard
Primary route:  E — Refactor
Supporting:     G — Security (payments surface area, hard reversibility)

Skills selected:
  Phase 0: karpathy-discipline + think-before-coding
  Phase 1: skipped — no UI changes
  Phase 2: simplicity-first + superpowers-write-plan
  Phase 3: surgical-changes + superpowers-tdd
  Phase 4: superpowers-verify
  Phase 5: superpowers-finish

Skills intentionally skipped:
  uiux-designer — reason: no user-facing changes
  goal-driven-execution — reason: scope is a refactor, not a feature; think-before-coding covers intent

Evidence required:
  - All billing tests pass BEFORE refactor begins (baseline)
  - All same billing tests pass AFTER refactor (behavior unchanged)
  - No new tests added that wouldn't have passed on the old code (no scope creep)
  - Zero DB schema changes
  - Zero API contract changes (same endpoints, same request/response shapes)

Stop conditions:
  🚫 HARD STOP: Do not modify any DB schema — this requires a separate migration task
  🚫 HARD STOP: Do not change any API endpoint signature — billing integrations depend on these
  ⚠️ Stop if: behavior must change to complete the refactor — classify as bug-fix or new-feature instead
─────────────────────────────────────────────
```

---

## Phase Sequence

**Phase 0 — Intent Gate** → `karpathy-discipline` + `think-before-coding`
```
Goal: Reduce cognitive load when working in billing — split one 800-line file into
      focused modules so changes are scoped and reviewable.
Non-goals: Fix bugs, add features, change pricing logic, modify DB schema
Success: Same tests pass before and after; file count increases; each file has one responsibility
Risk: high — billing logic is critical path; any behavior change causes financial errors

Assumptions:
  - No behavior change is acceptable — any bug found during refactor must be filed separately
  - Tests exist for all billing paths (verify before starting)
  - DB schema and API contracts are frozen for this task

Constraints (from karpathy-discipline):
  - Do not add abstractions — extract existing code, do not create new patterns
  - Do not add dependencies — move code, do not introduce new libraries
  - Each extracted file must be independently testable
```

**Phase 2 — Planning Gate** → `simplicity-first` + `superpowers-write-plan`
```
Current structure (before):
  lib/billing.ts — 812 lines covering: invoice generation, payment processing,
                   subscription management, webhook handling, tax calculation

Target structure (after):
  lib/billing/invoice.ts     — invoice creation, line items, PDF generation
  lib/billing/payments.ts    — Stripe charge, refund, payment method management
  lib/billing/subscriptions.ts — plan changes, upgrades, downgrades, cancellations
  lib/billing/webhooks.ts    — Stripe webhook handler, event routing
  lib/billing/tax.ts         — tax calculation, GST handling
  lib/billing/index.ts       — re-exports everything for backwards compatibility

Plan:
  Task 0: Run tests, capture baseline (must be 0 failures before refactor starts)
  Task 1: Extract invoice.ts → run tests → 0 failures
  Task 2: Extract payments.ts → run tests → 0 failures
  Task 3: Extract subscriptions.ts → run tests → 0 failures
  Task 4: Extract webhooks.ts → run tests → 0 failures
  Task 5: Extract tax.ts → run tests → 0 failures
  Task 6: Create index.ts re-exports → run tests → 0 failures
  Task 7: Delete original billing.ts (after all imports updated) → run tests → 0 failures

One file at a time. Test after each extraction. Never extract two files in the same step.
```

**Phase 3 — Build** → `surgical-changes` + `superpowers-tdd`
```
Baseline confirmed: 31 billing tests pass / 0 fail (captured before first line changed)

Surgical discipline:
  - Each commit covers exactly one extracted file
  - No logical changes — only moves, re-exports, and import path updates
  - No new test files — existing tests run against refactored structure
  - If a test fails mid-refactor: stop, revert the last extraction, investigate before continuing

Files changed: 7 (5 new extracted files + index.ts + original billing.ts deleted)
Files NOT changed: API routes, DB models, UI components, auth, analytics
```

**Phase 4 — Verification** → `superpowers-verify`
```
Command run: npm test lib/billing/
Output: Tests: 31 passed, 0 failed (same count as baseline)
Exit code: 0

Command run: npm test (full suite)
Output: Tests: 89 passed, 0 failed
Exit code: 0

Schema check: no migration files created ✅
API contract check: no endpoint signatures changed ✅
Import check: no external references to old lib/billing.ts path remain ✅
```

**Phase 5 — Finish** → `superpowers-finish`
```
Summary: Billing module split into 5 focused files — behavior unchanged, 31 tests unchanged
Verified: baseline 31/31 → post-refactor 31/31; full suite 89/89; no schema or API changes
Rollback: git revert the 7 commits — all behavior restores exactly; no DB changes to undo
Remaining risks: None — all tests pass, no behavior changed, all contracts preserved
Next: PR → peer review (billing changes require review per escalation rules) → merge
```
