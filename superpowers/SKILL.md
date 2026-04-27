---
name: superpowers
description: |
  Master software development methodology — systematic, disciplined execution for any non-trivial
  coding task. Enforces a 6-phase workflow: Design → Prepare → Plan → Implement → Test → Ship.

  Activate at the START of any coding work, especially when:
  - Churney OS has completed (plan approved, ready to build)
  - Starting implementation of a feature, fix, or refactor
  - User types "let's build", "implement", "execute the plan", "start coding", "ship it"
  - Any task that involves writing production code, not just reading or explaining
  - Subagent or parallel work is needed for speed

  This is the EXECUTION counterpart to Churney OS (which handles design & planning).
  Churney OS = What to build. Superpowers = How to build it correctly.

  The non-negotiable rules:
  - NO production code without a failing test first (TDD)
  - NO completion claims without fresh verification evidence
  - NO fixes without root cause investigation first (debugging)
  - SYSTEMATIC over ad-hoc — every task has a verify step

license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers — Execution Methodology

You are operating under a systematic development discipline. Superpowers is the execution layer — it governs HOW code gets written, tested, debugged, reviewed, and shipped.

This pairs with **Churney OS** (planning gate). If Churney OS hasn't run for this task, ask the user to run it first unless they've already confirmed a plan.

---

## The 6-Phase Execution Workflow

### Phase 1: Design (Brainstorm)
*Sub-skill: `superpowers-brainstorm`*

Before writing any code:
1. Ask clarifying questions one at a time — prefer multiple-choice over open-ended
2. Propose 2–3 approaches with trade-offs + a recommendation
3. Present the design in sections, seek approval after each
4. Save approved design to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
5. **Hard gate:** No code or implementation until design is written and approved

---

### Phase 2: Prepare (Git Worktree)
*Sub-skill: `superpowers-finish` handles cleanup*

Before coding:
1. Never work on `main` or `master` without explicit user approval
2. Create a git worktree for isolated work: `git worktree add ../worktrees/<feature-name> -b feature/<name>`
3. Establish a clean test baseline — run the test suite, note any pre-existing failures

---

### Phase 3: Plan (Write the Plan)
*Sub-skill: `superpowers-write-plan`*

Break the approved design into tasks:
- Each task: 2–5 minutes of actual work
- Format: write failing test → run to see RED → implement → verify GREEN → commit
- Include exact file paths, commands, and expected outputs
- No TBD, no placeholders, no "similar to Task N"
- Save to: `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

---

### Phase 4: Implement (Execute with Subagents)
*Sub-skill: `superpowers-execute`*

For each task in the plan:
1. Mark task in progress (TodoWrite)
2. Follow TDD strictly:
   - Write the failing test first (RED)
   - Confirm it fails for the right reason
   - Write minimal code to pass (GREEN)
   - Refactor while keeping green (REFACTOR)
3. Use subagents for parallel tasks — each gets complete context, no session history inheritance
4. Two-stage review per task: spec compliance → code quality
5. Loop until both reviews pass before moving to next task

---

### Phase 5: Test (Verification)
*Sub-skill: `superpowers-verify`*

Before claiming anything is done:
1. Run the full test suite — record pass/fail counts
2. Run the specific verification for the task (the command that proves the assertion)
3. Check output and exit codes — don't claim success without seeing the evidence
4. Banned phrases: "should work", "probably", "seems to", "I believe"
5. If tests fail: stop, debug systematically (`superpowers-debug`), fix, re-verify

---

### Phase 6: Review and Complete (Finish Branch)
*Sub-skill: `superpowers-finish`*

After all tasks verify:
1. Request code review via subagent (`superpowers-review`)
2. Address all critical and important feedback before proceeding
3. Present exactly 4 options to the user:
   - Merge to base branch locally
   - Push and create a Pull Request
   - Keep branch as-is
   - Discard this work
4. Execute chosen option with the correct git commands
5. Clean up the worktree (for options 1, 2, 4 only)

---

## Non-Negotiable Rules

| Rule | Applies When |
|------|-------------|
| No production code without a failing test first | Every implementation task |
| No completion claims without fresh verification evidence | Before reporting "done" |
| No fixes without root cause investigation first | Every bug fix |
| Never work on main/master without explicit approval | Every session |
| Always use git worktrees for isolation | Every feature branch |
| Stop when blocked — don't guess | Whenever stuck |

---

## Sub-Skill Map

| When you need to... | Use skill |
|---------------------|-----------|
| Design before coding | `superpowers-brainstorm` |
| Write an implementation plan | `superpowers-write-plan` |
| Apply TDD correctly | `superpowers-tdd` |
| Execute a plan (with subagents) | `superpowers-execute` |
| Debug systematically | `superpowers-debug` |
| Verify before claiming done | `superpowers-verify` |
| Finish and ship a branch | `superpowers-finish` |

---

## Combined Output Format

When this master skill is active, every task response follows this structure:

```
Phase: [current phase name]
Task: [what we're doing]

TDD step: RED / GREEN / REFACTOR
Command run: [exact command]
Output: [actual output excerpt]

Result: [what passed / what failed]
Next: [what comes next]
```

Never skip the command and output lines. Evidence is the standard.

---

## How This Pairs With Churney OS

```
Churney OS handles:              Superpowers handles:
─────────────────────            ────────────────────
Q1–Q6 Founder Interview    →     Phase 1: Design refinement
Constraint Check           →     Phase 2: Worktree setup
Design Review Gate         →     Phase 3: Task-level planning
7-Layer Test Matrix        →     Phase 5: Verification per layer
Due Diligence Layer        →     Phase 6: Branch completion
Execution Gate (approval)  →     Phase 4: TDD implementation
Post-Build Sync            →     memory-sync after Phase 6
```

If Churney OS ran, skip Phase 1 design and go straight to Phase 2 (worktree) → Phase 3 (write-plan).
