---
name: superpowers-debug
description: |
  Systematic debugging — root cause investigation before any fix is attempted. Triggers when:
  - Something is broken and the cause isn't immediately obvious
  - User says "it's not working", "this is broken", "there's a bug", "fix this error"
  - A test is failing unexpectedly
  - An error or exception appears
  - superpowers-verify finds a failure

  THE NON-NEGOTIABLE RULE: No fixes without root cause investigation first.
  Symptom fixes mask underlying problems. Find the root cause.
  This is the debugging protocol within Phase 4 and Phase 5 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Systematic Debugging

**Core rule: No fixes without root cause investigation first.**

Expected outcome when followed: 95% first-time fix success rate in 15–30 minutes.  
Without it: 2–3 hours of ad-hoc thrashing.

---

## Phase 1: Root Cause Investigation

1. **Read the error message completely.** Not a skim — every line, every stack trace entry.
2. **Reproduce the issue consistently.** If you can't reproduce it, you don't understand it yet.
3. **Check what changed recently.** `git log --oneline -10` and `git diff HEAD~1` are your first tools.
4. **Trace data flow backward.** Start at the failure point. Work backward through the call stack to find where the bad value originates.
5. **Gather evidence at component boundaries.** Log/inspect values at each layer boundary (API → service → DB). Don't guess where the problem is — find where the contract breaks.

---

## Phase 2: Pattern Analysis

1. Find a working example of the same pattern in the codebase (`grep`, `git log`, similar features)
2. Compare the working example against the broken code line by line
3. List all assumptions the broken code makes — which one is violated?
4. Check all dependencies: correct version? correct import path? correct configuration?

---

## Phase 3: Hypothesis and Testing

Form a **single, specific hypothesis**:
> "The bug is [exact location] because [exact reason]. Proof: [what I observed that supports this]."

Test it with the **smallest possible change**:
- Change one thing
- Run the reproduction case
- Observe the result

If the hypothesis is wrong: form a new hypothesis. Do not pile on more changes.

**After 3+ failed hypotheses:** Stop and question the architecture. The problem may not be where you're looking.

---

## Phase 4: Fix Implementation

Once root cause is confirmed:

1. Write a failing test that reproduces the bug — this must FAIL before the fix
2. Implement a single, targeted fix for the root cause
3. Verify the test passes
4. Run the full test suite — confirm no regressions
5. Commit: `git commit -m "fix: [what was broken and why] — root cause: [one sentence]"`

---

## Red Flags (Stop and Investigate Harder)

These indicate you've abandoned systematic debugging:

- "Quick fix for now, investigate later" — this is how bugs hide for months
- Proposing multiple changes simultaneously — you don't know which one fixed it
- "I'll just try X and see what happens" — randomness is not a debugging strategy
- Adding defensive code around the symptom without understanding the cause
- Making assumptions about the root cause without evidence

---

## Debugging Output Format

Before making any fix, report:

```
Error: [exact error message]
Location: [file:line]
Root cause: [what is actually wrong — be specific]
Evidence: [what I observed that confirms this diagnosis]
Hypothesis tested: [what I tried and what it showed]

Proposed fix: [one sentence — the single change that addresses root cause]
Test to verify: [the command and expected output]
```

Never propose a fix without filling this out completely. "Evidence" is the gate.
