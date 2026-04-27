---
name: superpowers-write-plan
description: |
  Create a comprehensive, bite-sized implementation plan before coding begins. Triggers when:
  - A design/spec has been approved (via Churney OS or superpowers-brainstorm)
  - User says "write the plan", "create implementation plan", "plan out the tasks"
  - Ready to move from design into structured task breakdown
  - Before superpowers-execute or superpowers-tdd is invoked

  Each task in the plan is 2–5 minutes of real work. No TBD. No placeholders.
  This is Phase 3 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Write Plan

**Purpose:** Turn an approved design into a precise, executable task list where every step has actual code, exact paths, and verifiable outcomes.

---

## Before Starting

1. Read the approved spec: `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`
2. Read CLAUDE.md for stack and architectural constraints
3. Map file responsibilities — for each file this plan will touch, state its current purpose

---

## Plan Structure

Save to: `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

```markdown
# Plan: <feature-name>
Date: YYYY-MM-DD
Spec: docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md

## File Map
- `path/to/file.ts` — [current purpose, what this plan will add/change]
- ...

## Tasks

### Task 1: [Action verb + what]
**Goal:** [one sentence, what done looks like]
**File:** `exact/path/to/file`

Step 1: Write failing test
\`\`\`typescript
// exact test code — not a placeholder
\`\`\`
Run: `npm test path/to/test.spec.ts`
Expected: 1 failing test (reason: function doesn't exist yet)

Step 2: Implement
\`\`\`typescript
// exact implementation code
\`\`\`

Step 3: Verify
Run: `npm test path/to/test.spec.ts`
Expected: all tests pass, no warnings

Step 4: Commit
Run: `git add exact/path && git commit -m "feat: [what]"`

### Task 2: ...
```

---

## Quality Rules

Every task must:
- Start with a failing test step (RED phase) — except pure config/infra tasks
- Have exact file paths — never "the relevant file" or "the component"
- Have exact commands with expected output or exit code
- Have a commit step at the end
- Be completable in 2–5 minutes

Banned language:
- "TBD" / "TODO" / "placeholder" / "similar to Task N" / "add error handling" (be specific)
- Vague expected outputs: "should work", "it passes"

Types and function signatures must be consistent across tasks — if Task 1 defines a type, Task 3 must use the exact same type name.

---

## Self-Review Before Handing Off

Check the plan for:
- [ ] Every task has actual code, not descriptions of code
- [ ] File paths are exact and consistent across tasks
- [ ] Test steps come before implementation steps
- [ ] No task takes more than 5 minutes
- [ ] Commit messages follow the project's format
- [ ] Types/interfaces defined in Task N are used correctly in Task N+1

---

## Hand Off to Execution

After the plan is written and passes self-review:
> "Plan ready. Saved to `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`. Ready to execute. Invoke `superpowers-execute` to begin."
