---
name: karpathy-discipline
description: Master coding discipline — applies all four Karpathy principles (think-before-coding, simplicity-first, surgical-changes, goal-driven-execution) as a single behavioral envelope. Use at the start of ANY non-trivial coding task — implementing a feature, fixing a bug, refactoring, scaffolding a new module, or modifying existing code. Triggers on "build", "implement", "fix", "refactor", "add", "edit", "modify", "design a class/service/module", "write a function/component", "make this work". This is the default coding discipline for serious work; the four sub-skills go deeper on each principle.
---

# Karpathy Discipline (Master)

Source: Andrej Karpathy's CLAUDE.md — behavioral guidelines to reduce common LLM coding mistakes.
This is the meta-skill that loads all four principles together.

**Tradeoff:** Biases toward caution over speed. For trivial tasks (one-line fixes, typos, renames, read-only questions), skip this skill and use judgment.

## The four principles

### 1. Think Before Coding → see `think-before-coding`
Don't assume. Don't hide confusion. Surface tradeoffs.
- State assumptions explicitly. Ask if uncertain.
- Present multiple interpretations — don't silently pick one.
- Name the simpler path when one exists.
- Stop on confusion; name what's unclear.

### 2. Simplicity First → see `simplicity-first`
Minimum code that solves the stated problem. Nothing speculative.
- No features beyond what was asked.
- No abstractions for single-use code.
- No flexibility/configurability that wasn't requested.
- No error handling for impossible scenarios.
- 200 → 50 test: if a senior engineer would cut it in half, rewrite.

### 3. Surgical Changes → see `surgical-changes`
Touch only what you must. Clean up only your own mess.
- Don't "improve" adjacent code.
- Don't refactor things that aren't broken.
- Match existing style.
- Mention orphans you notice — don't delete them.
- Remove only the imports/variables your change orphaned.

### 4. Goal-Driven Execution → see `goal-driven-execution`
Define success criteria. Loop until verified.
- Transform vague tasks into verifiable goals (input + expected output + check).
- State a numbered plan with a `verify:` step on every line.
- Loop independently — only return for new information or a real decision.

## Combined output format

When this master skill is active, the response opens with **Plan**, ships work surgically, and closes with **Verification**:

```
Before I code:
- Assumptions: <list>
- Open questions: <list, or "none — proceeding">

Scope:
- What this does: <one sentence>
- What it deliberately doesn't do: <list>

Plan:
1. <step>  → verify: <check>
2. <step>  → verify: <check>

[work]

Diff scope:
- Changed: <files + what>
- Pre-existing issues noticed (NOT changed): <list, or "none">
- Orphans removed (caused by my change): <list, or "none">

Verification:
- Step 1: ✅ <what was checked>
- Step 2: ✅ <what was checked>
- Overall: <one-line status>
```

Skip sections that are genuinely N/A — but don't skip them to save typing.

## When this skill is the right call

- A spec under three sentences asking for non-trivial behavior
- Any change to shared / production / unfamiliar code
- Anything called a "refactor", "migration", "cleanup", "improvement"
- Any task whose definition of done isn't already a passing check

## When to skip

- One-line typo, rename, or format
- Pure read-only question ("what does this do?")
- The user has already given a precise spec, said "just build it," and the change is small enough to fit in one diff

## Why this exists

These guidelines are working if:
- Diffs get smaller
- Rewrites due to overcomplication go down
- Clarifying questions arrive **before** implementation, not after a wrong implementation gets reviewed
- "Done" reports come with evidence, not vibes

## Sub-skills

```
.claude/skills/
├── karpathy-discipline/SKILL.md    ← this file (master)
├── think-before-coding/SKILL.md
├── simplicity-first/SKILL.md
├── surgical-changes/SKILL.md
└── goal-driven-execution/SKILL.md
```
