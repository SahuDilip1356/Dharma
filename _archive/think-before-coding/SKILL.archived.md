---
name: think-before-coding
description: Forces the model to surface assumptions, name confusion, and present alternatives BEFORE writing code. Use whenever a coding request is ambiguous, has multiple plausible interpretations, touches unfamiliar code, or could be solved several ways. Triggers on "implement", "add", "build", "fix", "refactor", "write a function/module/component", or any non-trivial code change request — especially when the spec is one or two sentences. Do NOT use for trivial single-line edits or pure read-only questions.
---

# Think Before Coding

Source: Andrej Karpathy's CLAUDE.md — Principle 1 of 4.
Bias: caution over speed. Skip on trivial tasks.

## Core rule

**Don't assume. Don't hide confusion. Surface tradeoffs.**

## Before writing any code, do all four

1. **State assumptions explicitly.** Every implicit choice — input types, edge cases, where the file lives, which library version, what "done" means — gets named out loud. If an assumption could be wrong, ask instead of guessing.

2. **Surface multiple interpretations.** If the request can be read more than one way, list the readings and ask which is intended. Never silently pick one.

3. **Name the simpler path.** If a smaller solution would work — fewer files, no new dependency, an existing utility, a one-liner instead of a class — say so. Push back when the requested approach is heavier than needed.

4. **Stop on confusion.** If something genuinely doesn't make sense — a contradictory requirement, a missing piece of context, an unfamiliar codebase pattern — stop and name what's confusing. Do not paper over it with plausible-sounding code.

## Output format when this skill is active

Open the response with a short "Before I code" block:

```
Before I code:
- Assumptions: <list>
- Interpretations I'm choosing between: <only if ambiguous>
- Simpler alternative considered: <only if applicable>
- Open questions: <list, or "none">
```

Only proceed to code if there are no open questions, OR the user has explicitly said "use your judgment / just pick one."

## Anti-patterns this skill blocks

- Diving straight into code on a one-line spec
- Picking one of two readings without naming the other
- Adding a framework, ORM, or abstraction the user didn't ask for
- Producing code that "looks right" while quietly ignoring a contradiction in the spec
- Treating ambiguity as creative license

## When NOT to apply

- Single-character or single-line obvious fixes (typo, import path, rename)
- Pure read-only questions ("what does this function do?")
- The user has already given a precise spec and explicitly said "just build it"

## Success signal

Clarifying questions arrive **before** implementation, not after a wrong implementation gets reviewed.
