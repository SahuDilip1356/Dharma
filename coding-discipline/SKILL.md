---
name: coding-discipline
description: |
  Karpathy-style coding discipline: surface assumptions before coding, write the minimum
  code that solves the problem, touch only what was asked, and turn vague tasks into
  verifiable goals. Use when writing, editing, or refactoring code; when a request is
  ambiguous; when tempted to add abstractions, flexibility, or "while I'm here" cleanups;
  or when a task lacks a clear definition of done.
license: MIT
metadata:
  author: Dilip Sahu
  version: "2.0.0"
---

# Coding Discipline

Four principles, applied in order. Read the matching file when that principle is in play.

| Principle | Apply when | Read |
|---|---|---|
| **Think before coding** | Requirements are ambiguous, or more than one reasonable interpretation exists | [think-before-coding.md](think-before-coding.md) |
| **Goal-driven execution** | The task has no observable success criterion yet | [goal-driven-execution.md](goal-driven-execution.md) |
| **Simplicity first** | Designing the change — no speculative abstraction or unrequested flexibility | [simplicity-first.md](simplicity-first.md) |
| **Surgical changes** | Editing existing code — no opportunistic refactors or style "improvements" | [surgical-changes.md](surgical-changes.md) |

[karpathy-discipline.md](karpathy-discipline.md) is the combined checklist for a full pass.

## Quick check before reporting done

- [ ] Assumptions were stated, not silently chosen
- [ ] A verifiable success criterion exists and was met
- [ ] No code exists that the task didn't need
- [ ] Every changed line traces back to the request
