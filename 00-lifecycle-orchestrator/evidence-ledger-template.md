# Evidence Ledger Template

Fill this ledger at the start of a task (Task + Route sections) and update it continuously
as gates are cleared. Never claim completion without a completed ledger.

Copy the template below for each task. Do not leave fields blank — write "N/A" or "not applicable" if a field genuinely doesn't apply, and state why.

---

## Template

```
╔══════════════════════════════════════════════════════════════════╗
║  EVIDENCE LEDGER                                                 ║
╠══════════════════════════════════════════════════════════════════╣
║  TASK                                                            ║
╠══════════════════════════════════════════════════════════════════╣
  Request:        [one-line description of what was asked]
  Work type:      [new-product | new-feature | ui-ux-design | bug-fix | debugging |
                   refactor | performance | security | integration | data-migration |
                   release | documentation | research-only | incident]
  Surface area:   [frontend | backend | database | auth | infra | ai | api | payments |
                   analytics | design-system]
  User impact:    [none | internal | user-facing | revenue-critical | compliance-critical]
  Risk level:     [low | medium | high | critical]
  Reversibility:  [easy | moderate | hard]
╠══════════════════════════════════════════════════════════════════╣
║  ROUTE                                                           ║
╠══════════════════════════════════════════════════════════════════╣
  Primary route:    [A | B | C | D | E | F | G | H] — [name]
  Supporting routes:[routes added via tie-breaker rule, or "none"]
  
  Skills invoked:
    Phase 0: [skill name]
    Phase 1: [skill name | "skipped — reason"]
    Phase 2: [skill name | "skipped — reason"]
    Phase 3: [skill name]
    Phase 4: [skill name]
    Phase 5: [skill name]
  
  Skills intentionally skipped:
    [skill] — [reason it doesn't apply to this task]
╠══════════════════════════════════════════════════════════════════╣
║  GATES                                                           ║
╠══════════════════════════════════════════════════════════════════╣
  Gate              Status    Evidence
  ──────────────────────────────────────────────────────────────
  Intent            [ ]       Goal + success criteria stated
  Assumptions       [ ]       Unknowns listed; constraints stated
  Design            [ ]       UX flow / plan reviewed (if applicable)
  Plan              [ ]       Implementation plan approved
  Execution         [ ]       Code written, tests written first (TDD)
  Verification      [ ]       Command run, output reviewed, evidence cited
  Finish            [ ]       Commit / PR / merge summary complete

  [ ] = Pending  [✅] = Passed  [—] = Skipped (reason required)
╠══════════════════════════════════════════════════════════════════╣
║  EVIDENCE                                                        ║
╠══════════════════════════════════════════════════════════════════╣
  Code evidence:
    Files changed:     [list files]
    Files not changed: [confirm scope discipline]
    Tests written:     [test names or count]
    Test result:       [X passed / Y failed / Z skipped]
    Build result:      [✅ clean | ❌ errors: list]
    Typecheck result:  [✅ clean | ❌ errors: list]

  Runtime evidence:
    Command run:    [exact command]
    Output:         [relevant excerpt — not "it worked"]
    Exit code:      [0 = pass | non-zero = explain]
    Manual check:   [what was done manually, what was observed]

  UX evidence (if user-facing):
    Accessibility:  [audit result — pass / findings]
    Responsive:     [375px | 768px | 1280px | 1440px — pass / issues]
    Interaction:    [states tested: loading / error / empty / success]
    Design QA:      [screenshot comparison — pass / issues]

  Risk evidence:
    Rollback plan:  [how to revert if production issues appear]
    Known risks:    [residual risks not yet mitigated]
    Escalations:    [any stop conditions triggered and how they were resolved]
╠══════════════════════════════════════════════════════════════════╣
║  COMPLETION STATUS                                               ║
╠══════════════════════════════════════════════════════════════════╣
  Status: [choose exactly one]

  ✅  Implemented and verified with [specific evidence citation].
  ⚠️  Implemented but not runtime-verified — [what's missing and why].
  📋  Planned only; no code changed.
  🔶  Partially complete; remaining risks: [list].
  🚫  Blocked: [specific blocker — what is needed to unblock].

  Sign-off: [your name or "Claude"] | [date]
╚══════════════════════════════════════════════════════════════════╝
```

---

## Lightweight Ledger (Low-Risk Tasks Only)

For low-risk, non-user-facing, easily reversible tasks (typo fixes, comment updates,
config changes, local-only tests), use the compressed form:

```
Ledger (lightweight):
  Request:     [one-line]
  Route:       [letter] | Risk: low | Reversible: easy
  Evidence:    [command run + output or manual check]
  Status:      ✅ Implemented and verified with [evidence].
```

Do NOT use the lightweight form for: any user-facing change, any auth/payments/ai/compliance
surface area, any hard-to-reverse operation, or any medium/high/critical risk level.

---

## Gate Status Definitions

| Status | Meaning |
|---|---|
| `[ ]` Pending | Gate has not yet been checked |
| `[✅]` Passed | Gate criteria met — evidence exists |
| `[—]` Skipped | Gate intentionally skipped — reason must be stated |

A skipped gate requires explicit justification. "Not applicable" is a valid reason only if the skip
does not increase risk. "Time pressure" and "probably fine" are never valid reasons to skip a gate.

---

## What "Evidence" Means Per Gate

| Gate | What counts as evidence |
|---|---|
| **Intent** | Written goal statement + success criteria |
| **Assumptions** | Bullet list of assumptions made; unknowns acknowledged |
| **Design** | UX flow output, plan document, or explicit "design phase not applicable — reason" |
| **Plan** | Implementation plan with task list and file manifest |
| **Execution** | Code exists; tests exist; TDD cycle documented |
| **Verification** | Command run + output excerpt + exit code |
| **Finish** | Commit hash or PR URL or explicit "code not committed — reason" |

"I believe it passed" is not evidence. "The test output says 0 failing" is evidence.
