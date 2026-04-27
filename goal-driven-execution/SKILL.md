---
name: goal-driven-execution
description: Converts vague tasks into verifiable goals with explicit success criteria, then loops until verified. Use whenever a task is multi-step, the definition of "done" is fuzzy, or the work involves making something pass a test (bug fixes, validation, refactors, migrations). Triggers on "fix", "make it work", "add X", "refactor", "migrate", "improve", "ensure", "validate", or any task where success can be checked rather than just declared. Apply BEFORE writing code so the loop has a target.
---

# Goal-Driven Execution

Source: Andrej Karpathy's CLAUDE.md — Principle 4 of 4.

## Core rule

**Define success criteria. Loop until verified.**

A goal you can check independently is a goal you can finish independently. A goal you can only check by asking the user is a goal that requires constant clarification.

## Transform tasks into verifiable goals

| Vague task | Verifiable goal |
|---|---|
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after; no behavior change" |
| "Make it faster" | "Benchmark before; target N% improvement; benchmark after" |
| "Improve error handling" | "Enumerate the failure modes; each one has a test" |
| "Clean it up" | Reject — ask the user what specifically. (See `think-before-coding`.) |

The pattern: **input + expected output + how to check.**

## Plan format for multi-step tasks

State a brief, numbered plan with a verification check on every step:

```
1. <Step>  → verify: <check>
2. <Step>  → verify: <check>
3. <Step>  → verify: <check>
```

Each `verify` must be something you can run yourself: a test command, a grep, a build, an output diff, an HTTP response check. **Not** "verify it looks right" or "verify it works."

## The loop

```
while not verified:
    do the next step
    run the verification
    if it fails → diagnose, revise, retry
    if it passes → mark done, move on
```

Loop independently. Only return to the user when:
- All checks pass (success)
- A check fails in a way that needs new information or a real decision
- The plan turned out to be wrong and a new plan is needed

Do NOT return to the user after every step asking "should I continue?"

## Output format when this skill is active

Open with the plan. Close with the verification ledger:

```
Plan:
1. <step>  → verify: <check>
2. <step>  → verify: <check>

[work happens]

Verification:
- Step 1: ✅ <what was checked, what passed>
- Step 2: ✅ <what was checked, what passed>
- Overall: <one-line status>
```

## Anti-patterns this skill blocks

- "Done!" with no evidence anything was checked
- "Should work" / "I think this is right" — declaring success on vibes
- Asking the user after every micro-step
- Writing code without first deciding how you'd know it's correct
- Tests that only assert "the function returned" — passing for the wrong reason
- Marking a step complete because the code compiled (compiling ≠ correct)

## When NOT to apply

- Single-step trivial tasks (typo, rename, format)
- Pure information requests where there's nothing to verify
- The verification is more expensive than the change and the change is reversible (use judgment)

## Pairs well with

- `think-before-coding` — defines the goal correctly before the loop starts
- `simplicity-first` — keeps each step's diff small enough that a single `verify` actually proves it works
- `surgical-changes` — keeps the loop's blast radius narrow

## Success signal

You report "done" with a verification ledger, not a hope. The user can reproduce every check. The number of "did you actually test it?" follow-ups goes to zero.
