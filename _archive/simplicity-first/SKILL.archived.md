---
name: simplicity-first
description: Forces minimum viable code — nothing speculative, no premature abstractions, no unrequested flexibility. Use whenever generating new code, designing a module/class/function, or scoping an implementation. Triggers on "build", "implement", "design", "write", "scaffold", "create a class/service/component", "make it configurable/extensible/flexible", or any time the answer threatens to become longer than the problem. Apply BEFORE writing code and as a self-review pass after.
---

# Simplicity First

Source: Andrej Karpathy's CLAUDE.md — Principle 2 of 4.

## Core rule

**Minimum code that solves the stated problem. Nothing speculative.**

## The five no-gos

1. **No features beyond what was asked.** If the user asked for X, don't ship X + Y "in case." Y is a separate decision the user gets to make.

2. **No abstractions for single-use code.** A base class with one subclass is a base class too many. A strategy pattern with one strategy is a function. A config object with one caller is two arguments.

3. **No "flexibility" or "configurability" the user didn't request.** Optional parameters, plugin hooks, dependency injection, environment-driven toggles — these are all liabilities until something actually needs them.

4. **No error handling for impossible scenarios.** Don't catch exceptions that can't be thrown. Don't validate inputs the type system already validates. Don't add fallbacks for branches that never execute.

5. **No "while I'm here" cleanup.** That belongs to a separate change. (See sibling skill: `surgical-changes`.)

## The 200→50 test

After writing the code, ask: **"Could a senior engineer cut this in half without losing functionality?"**

If yes — rewrite. Common cuts:
- Replace a class with a function
- Inline a one-call helper
- Delete the interface and just use the concrete type
- Replace a config dict with two named parameters
- Drop the try/except that wraps a branch that can't fail
- Remove the logging that nobody will read

## Output format when this skill is active

Before producing the code, state:

```
Scope:
- What this does: <one sentence>
- What this deliberately doesn't do: <list — surfaces the cuts>
- Lines: ~<estimate>
```

After the code, include a one-line self-check:

```
Simpler version possible? <yes/no — if yes, why I didn't take it>
```

If the answer is "yes" with no good reason, take the simpler version.

## Anti-patterns this skill blocks

- Writing a Factory + Strategy + Builder for what could be a 10-line function
- Adding `**kwargs` "for future extensibility"
- Splitting a 60-line file into 6 files because "separation of concerns"
- Wrapping every value in an Optional/Result/Either when None and exceptions work
- Adding a config layer for a script that runs once
- Defensive `if x is not None` checks where x cannot be None

## When NOT to apply

- The user explicitly asked for a generalizable, library-grade abstraction
- The complexity is load-bearing — it solves a real, named problem (concurrency, security, real configurability with multiple known callers)
- You're working inside an established framework whose patterns you must match (see sibling skill: `surgical-changes`)

## Success signal

Diffs are smaller. Reviewers stop saying "do we need this?" Code reads top-to-bottom without jumping through indirection layers.
