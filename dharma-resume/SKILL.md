---
name: dharma-resume
description: |
  Session continuity skill — picks up exactly where a previous session left off by reading
  STATE.md and recent episodic memory. Reports current phase, blockers, open threads, and
  suggested next step. Then routes back into the lifecycle-orchestrator at the right phase.

  Activation:
  - Triggers on: "resume", "continue", "where were we", "pick up where we left off",
    "what's next on [project]", "back to [project]"
  - Auto-invoked when a project's STATE.md exists and last-modified > 1 hour ago

  Outputs:
  - Resume Brief: previous outcome, open threads, current state, suggested next step
  - Updated STATE.md (after user confirms next step)
  - Hand-off to the right phase in 00-lifecycle-orchestrator

  Skip when:
  - First-ever session on a project (no STATE.md exists yet — go to Phase 0)
  - User explicitly says "start fresh" or "ignore previous state"

license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Dharma Resume — Session Continuity

You are operating Dharma's session-continuity skill. Your job: read what happened before, surface it cleanly, and put the user back at the right point in the lifecycle.

This skill saves the most expensive thing in product work: re-establishing context. Without it, every session re-explains itself. With it, work compounds.

---

## When this skill runs

### Auto-trigger
Any time the lifecycle-orchestrator is invoked AND:
- `[project]/memory/STATE.md` exists
- `STATE.md` last-modified > 1 hour ago
- The current request is not "start fresh" / "new project" / "ignore previous state"

### Manual trigger
User says any of:
- "resume", "continue", "pick up where we left off"
- "where were we?", "what's next?", "what's the state of [project]?"
- "back to [project]"

---

## Protocol

### Step 1: Locate state files

```
Read in order:
1. [project]/memory/STATE.md            (current live working state)
2. [project]/memory/episodic/*.md       (last 3 by date — episodic context)
3. [project]/memory/PLAN.md             (active plan, if exists)
4. [project]/memory/ROADMAP.md          (phase positioning)
5. [project]/memory/decisions.md        (recent decisions, last 5 entries only)
```

If `STATE.md` doesn't exist:
- Check `episodic/` — if recent digests exist, propose reconstructing STATE.md from them
- If no episodic either: this is effectively a new project; route to Phase 0

### Step 2: Build the Resume Brief

Output this structure to the user:

```markdown
## Resume Brief — [Project name]

**Last active:** [date from STATE.md or latest episodic file]
**Last session outcome:** [from latest episodic digest]
**Current phase:** [from STATE.md — e.g., "Phase 3 Build Gate, mid-implementation"]

### What's done since last session
[from STATE.md "completed since last update" or latest episodic digest]

### Open threads
- [list from STATE.md or last episodic digest]

### Current blockers (if any)
- [list from STATE.md]

### Suggested next step
[Based on STATE.md "next-step" + ROADMAP.md current milestone]

### Files of interest
- [list from latest episodic digest's "Outputs produced"]
```

### Step 3: Confirm with user

Ask: **"Pick up here, or shift direction?"**

Options:
- **Continue:** "Yes, continue with [suggested next step]" → proceed to Step 4
- **Shift:** "I want to do [something else]" → re-route through routing-decision-tree
- **Question state:** "Why is [X] blocked?" → answer from the loaded context, don't proceed yet

### Step 4: Hand off to orchestrator

Once user confirms direction, route to the appropriate phase in `00-lifecycle-orchestrator`:

```
If continuing the same task:
  → resume at the phase noted in STATE.md
  → load relevant project memory slice
  → continue without re-running classification

If shifting to a new task on the same project:
  → re-run routing-decision-tree (Step 0)
  → state continues to load existing memory
  → episodic-memory captures both threads in next digest
```

### Step 5: Update STATE.md (after work resumes)

Once the new work makes progress, update `[project]/memory/STATE.md`:

```markdown
# Project State — [Project name]

**Last updated:** YYYY-MM-DD HH:MM
**Current phase:** [Phase N — gate name]
**Active plan:** [link to PLAN.md, if exists]

## Working on now
[what the user is currently building / debugging / designing]

## Open threads
- [thread 1]
- [thread 2]

## Blockers
- [blocker 1, if any]

## Completed since last update
- [recent work, last 5 items max]

## Next step
[the next thing to do — be specific]
```

---

## STATE.md structure

The single source of truth for "where are we right now?" Lives at `[project]/memory/STATE.md`.

Updated by:
- `dharma-resume` at session resume + after work begins
- `superpowers-write-plan` when a plan is approved
- `superpowers-execute` after each task completes
- `superpowers-finish` when a phase ends

Read by:
- `dharma-resume` (this skill)
- Lifecycle orchestrator at session start
- `episodic-memory` for context when writing digests

**Rule:** Always update STATE.md before ending a session if work is incomplete. Never let it go stale.

---

## Edge cases

### Multiple recent sessions on different topics
If the last 3 episodic digests cover different topics, ask: **"Last sessions touched [X], [Y], [Z]. Which are we resuming?"**

Don't assume — episodic memory is a list, not a stack.

### Stale state (STATE.md > 30 days old)
Surface a warning:
> ⚠️ STATE.md last updated [DATE] ([N] days ago). Context may be very stale.
> Recommend a fresh `/memory-sync` pass or starting from Phase 0 with current goals.

Don't block — let user decide.

### State conflicts with episodic
If STATE.md says "Phase 3 Build" but the latest episodic digest says "blocked at Phase 2 Plan", flag the conflict to the user. Episodic is usually more recent than STATE.md if STATE.md wasn't updated at session end.

### No project memory at all
- This is a brand-new project. Don't run dharma-resume — instead route to Phase 0 directly via the orchestrator's normal flow.

---

## What dharma-resume does NOT do

- **Replay full transcripts** — that's not the goal; the digest is the right level of detail
- **Re-execute past work** — it surfaces state, doesn't rebuild outputs
- **Make decisions for the user** — it surfaces options, the user picks
- **Bypass routing-decision-tree** — if the user shifts direction, classification re-runs

---

## Coordination with episodic-memory

```
Session N ends
   → episodic-memory writes session-N digest
   → STATE.md updated if work incomplete
   → memory-layer writes any decisions/learnings

[time passes]

Session N+1 begins
   → User invokes Dharma OR says "resume"
   → dharma-resume reads STATE.md + last 3 episodic digests + recent decisions
   → Outputs Resume Brief
   → User confirms → orchestrator picks up at right phase
   → Work resumes
```

---

## Comparison to /clear, /resume in Claude Code

| | Claude Code `/resume` | Dharma `dharma-resume` |
|---|---|---|
| **Scope** | Resumes a Claude Code session by ID | Resumes Dharma project work across sessions |
| **State source** | Claude Code session JSONL | Dharma's `STATE.md` + `episodic/` digests |
| **Output** | Re-attaches to session transcript | Brief summary + suggested next step |
| **Cross-session** | No (one session at a time) | Yes (across days/weeks/machines) |
| **Project-aware** | No | Yes (per-project state) |

Use Claude Code's `/resume` to reconnect to an interrupted session. Use Dharma's `dharma-resume` to pick up project work across any sessions, on any machine, any day.

---

## Example interaction

```
User: continue working on saralprivacy hindi PRD

Dharma (dharma-resume invoked):

## Resume Brief — SaralPrivacy

**Last active:** 2026-03-29 (35 days ago)
**Last session outcome:** Hindi PRD + dev plan complete; session closed
**Current phase:** Phase 0/1 — definition complete, awaiting kick-off

### What's done since last session
- Full PRD written and saved at /Users/sahudilip/Desktop/Product Dev/SaralPrivacy_Hindi_PRD.md
- Architecture decisions logged (same-URL approach, publish flags per namespace, legal review gate mandatory)
- ~12,580 words to translate, 4 days engineering, 12-14 days calendar

### Open threads
- Translation has not started yet
- Legal review process not yet defined
- No Hindi pages have been built

### Suggested next step
Move to Phase 2 (Plan): create implementation plan for Phase 1 namespaces
(per-namespace publish-gate review → translation → legal review → live)

### Files of interest
- SaralPrivacy_Hindi_PRD.md (PRD)
- memory/decisions.md [2026-03-29] (architecture)

Pick up here, or shift direction?
```

The user can now make a one-line decision instead of re-explaining 35 days of context.
