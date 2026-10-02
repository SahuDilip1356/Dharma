---
name: episodic-memory
description: |
  Episodic Memory — captures session digests (prompts, drafts, outputs, decisions) into
  [project]/memory/episodic/ so future sessions can retrieve and resume context. Closes
  the "interaction history" gap in Dharma's memory model.

  Activation:
  - Post-session (automatic): when a session ends with substantive output, write a digest
  - Pre-session (selective): when dharma-resume runs, retrieve recent relevant digests
  - Manual: user can invoke "save episodic memory" or "summarize this session"

  Scope:
  - Captures the conversational arc, not full transcripts (digest, not log)
  - Stores prompts that produced meaningful outputs (skip noise/exploration)
  - Indexes drafts that were saved or reviewed (not just brainstormed and discarded)
  - Retains key results/outputs as cross-references

  Distinct from memory-layer:
  - memory-layer writes decisions.md, learnings.md, deployment-pipeline.md (durable facts)
  - episodic-memory writes [project]/memory/episodic/YYYY-MM-DD-[slug].md (session digests)
  - Both run in the post-flight phase, in this order: episodic-memory FIRST (captures the
    arc), then memory-layer (extracts durable decisions from that arc)

license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Episodic Memory — Session Digest Capture and Retrieval

You are operating Dharma's Episodic Memory layer. This complements the existing `memory-layer` by capturing **what happened in a session**, not just **what was decided**.

---

## Why this exists

Memory-layer answers: "What were the decisions and learnings on this project?"

Episodic memory answers: "What did we discuss in the last session? What drafts existed? What prompt produced that output? Where were we when we paused?"

Without episodic memory, every session re-explains context that was just covered. Decision logs aren't enough — they capture conclusions, not the path.

---

## File location

```
[project]/memory/episodic/
└── YYYY-MM-DD-[topic-slug].md
```

One file per session-with-substantive-output. Sessions producing no durable output are not written.

**Naming convention:** `2026-05-04-context-mode-eval.md`, `2026-05-04-orchestrator-layer0plus.md`

---

## Digest format

Every episodic file follows this structure:

```markdown
# Session Digest: [Topic]
**Date:** YYYY-MM-DD
**Project:** [project name]
**Duration:** ~[N] minutes (rough)
**Outcome:** [decision-made | draft-produced | research-only | partial-blocked]

---

## Context entered with
[1-2 sentences: what was the state at session start?]

## Goal of this session
[What user wanted to accomplish]

## Key prompts (those that produced meaningful output)
1. "[prompt summary or excerpt]" → [output type]
2. "[prompt summary]" → [output type]
   (Skip exploratory prompts that didn't lead anywhere durable)

## Outputs produced
- [File path or description]
- [File path or description]

## Decisions made (cross-reference to decisions.md)
- [Decision summary] → see decisions.md [DATE]

## Open threads / next steps
- [What's still unresolved]
- [What was deferred and why]

## State at session end
[1-2 sentences: where did we stop? What's the next logical step?]
```

---

## Capture protocol (post-session)

Trigger when the session ends with substantive output. Substantive = at least one of:

- A file was created or meaningfully modified
- A decision was logged
- A multi-step plan was produced
- An evaluation/audit returned a verdict
- A new skill was built
- A debugging investigation reached a root cause

Skip if:

- Pure question-answering with no artifact
- Exploratory chat with no decision or draft
- Pure information lookup (use cache, not episodic memory)

### Digest writing rules

- **Brief, not transcript.** Aim for 1 page per session, not 10. The user already lived through it.
- **Lead with outcome.** First line should answer "what came out of this session?"
- **Reference, don't duplicate.** If a decision was logged in decisions.md, link to it; don't restate it.
- **Capture prompts that mattered.** A prompt is worth recording if its output is referenced in a file, a decision, or a plan. Otherwise skip it.
- **Note state at end.** This is the hand-off to the next session — be specific.

---

## Retrieval protocol (pre-session, when invoked by dharma-resume)

When `dharma-resume` runs or the user says "where were we?" / "continue from yesterday":

### Step 1: Identify recency
Read the last 3 episodic digests by date. If the most recent is >7 days old, surface a warning that context may be stale.

### Step 2: Identify relevance
Filter the loaded digests by:
- Same topic/project area as the current request
- Same user-stated goal
- Open threads from those digests that match the current request

### Step 3: Surface state
Output a short brief:

```
Resuming from [latest digest date]:
- Last session outcome: [outcome from digest]
- Open threads: [list from digest]
- State at end: [from digest]
- Suggested next step: [based on roadmap/state]
```

### Step 4: Load STATE.md
Read `[project]/memory/STATE.md` for current live state (separate from episodic — STATE.md is working memory, episodic is history).

---

## What episodic-memory does NOT own

- **Full conversation transcripts** — those live in Claude Code's session JSONL files; episodic memory is a digest, not a log
- **Decisions** — those are written to `decisions.md` by `memory-layer`; episodic memory cross-references them
- **Working memory** — that lives in `STATE.md` and Phase 0 evidence
- **Code outputs** — those live in the project's actual source tree; episodic memory references the paths

---

## Coordination with memory-layer

```
Session ends with substantive output
        ↓
1. episodic-memory POST-FLIGHT (run FIRST)
   - Identify the session arc
   - Write [project]/memory/episodic/YYYY-MM-DD-[slug].md
        ↓
2. memory-layer POST-FLIGHT (run SECOND)
   - Extract durable decisions → decisions.md
   - Extract failure patterns → learnings.md
   - Update deployment-pipeline.md if shipped
        ↓
3. STATE.md update (if dharma-resume is wired in)
   - Update current-phase, next-step, blockers
        ↓
Done
```

This ordering matters: episodic captures the raw arc; memory-layer distills durable facts FROM that arc.

---

## New project initialization

When a project's `memory/` directory is created (by `memory-layer`), also create:

1. `memory/episodic/` directory (empty)
2. Add `episodic/` reference to `MEMORY.md` index

No initial digest is written until the first substantive session ends.

---

## Manual invocation

User says "save episodic memory" or "summarize this session" → write a digest immediately, regardless of whether the session "ended."

User says "what happened last time?" or "where were we?" → run retrieval protocol, surface the brief.

---

## Pruning policy

Episodic memory grows over time. Recommended pruning:

- **Keep all digests for 90 days.** Recent context is highest value.
- **After 90 days:** if a digest's open threads are all closed AND its decisions are all logged in decisions.md, archive to `memory/episodic/archive/[year]/`.
- **Never delete.** Archive is a move, not a delete — historical context can be valuable for retrospectives.

Pruning is a manual operation, not automatic. Run quarterly.

---

## Relationship to memory-sync

| | `memory-sync` | `episodic-memory` |
|---|---|---|
| **Trigger** | Manual: `/memory-sync <summary>` | Automatic post-flight + manual |
| **Output** | Multi-file batch update across MEMORY.md, decisions.md, learnings.md | Single session digest in `episodic/` |
| **Purpose** | Force a full memory refresh after long sessions | Capture session-by-session continuity |
| **Frequency** | After major sprints or sessions | Every substantive session |

They complement each other. `episodic-memory` runs every session quietly. `memory-sync` is the manual override for full refreshes.
