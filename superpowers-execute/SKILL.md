---
name: superpowers-execute
description: |
  Execute an implementation plan using subagents for speed and quality. Triggers when:
  - A written plan exists (superpowers-write-plan has run)
  - User says "execute the plan", "start building", "implement per the plan", "run the tasks"
  - Ready to work through the task list from docs/superpowers/plans/

  Each task gets a fresh subagent. Two review stages per task: spec compliance → code quality.
  Never skip review stages. Never start on main without explicit approval.
  This is Phase 4 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Execute Plans

**Purpose:** Work through a written implementation plan systematically, with fresh subagents per task and two-stage review to maintain quality.

---

## Before Starting

1. Read the plan: `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`
2. Raise any concerns with the user before starting — better to fix the plan than discover problems mid-task
3. Create a TodoWrite list from all plan tasks
4. Confirm you are on a feature branch, not main/master

---

## For Each Task

### Step 1: Mark In Progress
Update TodoWrite: mark task as in-progress.

### Step 2: Dispatch Implementer Subagent
Provide complete context — the subagent has no session history. Include:
- The specific task description from the plan
- Exact file paths to read
- The TDD steps to follow
- The verification command
- The commit message format

Model selection:
- 1–2 file changes, mechanical work → use a lighter model (Haiku)
- Architecture decisions, complex logic → use the most capable model (Sonnet/Opus)

### Step 3: Spec Compliance Review
After implementation, dispatch a reviewer subagent:
- Provide: what was built, the original spec/plan task, starting and ending commit hashes
- Ask: does this implementation match the spec? Are there gaps or deviations?
- If fails: loop back to implementer with specific gaps to fix. Re-review after fix.

### Step 4: Code Quality Review
Dispatch a second reviewer subagent:
- Provide: the diff, the project's CLAUDE.md constraints
- Ask: code quality issues — readability, patterns, performance, security, test coverage
- Severity tiers: Critical (fix now) → Important (fix before merge) → Minor (note for later)
- If critical/important: loop back to implementer. Re-review after fix.

### Step 5: Mark Complete
Both reviews passed → mark task complete in TodoWrite → commit.

---

## Safety Rules

- **Stop when blocked.** Ask for clarification rather than guessing and proceeding.
- **Never start on main/master** without explicit user approval.
- **Re-review whenever fixes are implemented** — never skip the re-review after a fix.
- **Never ignore subagent questions** — they surface blockers early.
- **Preserve controller context** — subagents handle tasks, the controller handles coordination.

---

## After All Tasks Complete

Run the full test suite. Then invoke `superpowers-finish` to complete the branch.

---

## Subagent Dispatch Template

When dispatching an implementer subagent, include:

```
You are implementing Task [N] from the plan at docs/superpowers/plans/YYYY-MM-DD-<feature>.md.

Context:
- Stack: [from CLAUDE.md]
- Working branch: [branch name]
- Files to work in: [exact paths]

Task:
[paste the exact task section from the plan]

Rules:
- Follow TDD strictly: write failing test → verify RED → implement → verify GREEN → refactor → commit
- Do not modify any file not listed above
- Report: what you built, what tests pass, the commit hash

Do not proceed if you hit a blocker — report it immediately.
```
