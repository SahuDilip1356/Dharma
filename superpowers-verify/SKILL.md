---
name: superpowers-verify
description: |
  Verification before completion — evidence must precede any claim of "done". Triggers when:
  - About to report that a task, feature, or fix is complete
  - About to commit, create a PR, or merge
  - Claiming tests pass, bugs are fixed, or features work
  - User asks "is this done?", "does it work?", "is it ready?"

  THE NON-NEGOTIABLE RULE: No completion claims without fresh verification evidence.
  "Should work", "probably passes", "I believe it's fixed" = not done.
  This is Phase 5 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Verification Before Completion

**Core rule: Run it. See the output. Then and only then claim it's done.**

Skipping verification is misrepresentation, not efficiency.

---

## The 5-Step Verification Process

Before claiming any work is complete:

### Step 1: Identify
Name the exact command that proves your assertion.
> "To prove this works, I will run: `[command]`"

### Step 2: Execute
Run the command completely and freshly. Not from a previous run's output. Not from memory.

### Step 3: Review
Read the full output. Check the exit code. Don't skim.

### Step 4: Validate
Ask: does this output actually support the claim?
- `0 failing tests` proves tests pass — but does it prove the feature works end to end?
- A 200 response proves the endpoint responds — but does it return the right shape?
- No error in the console proves no crash — but does the UI render correctly?

### Step 5: Report
Only after Steps 1–4, make the assertion — with the evidence.

---

## Verification by Claim Type

| Claim | What to verify | What to report |
|-------|---------------|----------------|
| "Tests pass" | Run the test suite | Pass/fail counts, any skipped tests |
| "Bug is fixed" | Run the reproduction case | Before: fails. After: passes |
| "Feature works" | Execute the happy path manually or via test | What you did, what you saw |
| "API endpoint works" | Make the actual request | Status code, response body excerpt |
| "No regressions" | Run the full test suite + smoke test adjacent features | Suite output, specific checks |
| "Ready to merge" | Run all of the above | Summary with evidence for each |

---

## Banned Phrases

Never use these to describe work status:

- "should work"
- "probably passes"
- "seems to"
- "I believe it's fixed"
- "it worked last time"
- "the tests should be fine"
- "I'm confident this is correct"

These are guesses. The standard is evidence.

---

## What "Done" Looks Like

```
Verification complete:

Command run: npm test src/features/appointment.test.ts
Output: Tests: 8 passed, 0 failed (0 skipped)
Exit code: 0

Command run: npm test (full suite)
Output: Tests: 47 passed, 0 failed
Exit code: 0

Manual check: [what was tested, what was observed]

Status: ✅ Done — all checks pass, ready to proceed.
```

If any check fails, status is not done. Debug first (`superpowers-debug`), then re-verify.

---

## When to Skip

There is no "when to skip" for this skill. The only exception is if the user explicitly acknowledges a check cannot be run (e.g., a third-party API in a test environment) and explicitly accepts the risk in writing.

Exhaustion, time pressure, and "just this once" are not exceptions.
