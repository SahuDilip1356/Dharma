---
name: surgical-changes
description: Forces edits to existing code to touch only what the user asked for — no opportunistic refactors, no style "improvements", no deletion of pre-existing dead code. Use whenever editing, modifying, fixing, refactoring, or extending an existing file or module. Triggers on "fix", "edit", "modify", "update", "change", "patch", "adjust", "tweak", or any diff-producing operation on code that already exists. Critical when working in unfamiliar codebases or shared repositories.
---

# Surgical Changes

Source: Andrej Karpathy's CLAUDE.md — Principle 3 of 4.

## Core rule

**Touch only what you must. Clean up only your own mess.**

## The four restraints when editing existing code

1. **Don't "improve" adjacent code.** That comment formatting you'd do differently, that variable name you'd rather rename, that function you'd split — leave them alone. They are not what you were asked to change.

2. **Don't refactor things that aren't broken.** Working code is working code. Refactor is a separate, named decision the user makes — not a side effect of a bug fix.

3. **Match existing style, even if you'd write it differently.** snake_case in a snake_case file. Tabs in a tab file. The codebase's idioms over your preferences. Consistency beats taste.

4. **Mention orphans you notice — don't delete them.** If you spot dead code, an unused import, a stale comment that wasn't yours: surface it in the response, leave it in the file. The user decides whether to remove it.

## The orphan rule (the one exception)

**Remove imports/variables/functions that YOUR change made unused.** If you delete the only caller of `helper()`, delete `helper()` too. If you remove a parameter, remove its import. That's not opportunistic cleanup — it's finishing your own change.

**Do NOT remove pre-existing dead code unless asked.** If `helper()` was already unused before you arrived, it stays.

## The diff test

For every changed line, ask: **"Does this line trace directly to the user's request?"**

If no — revert that line. Three buckets to revert:
- Reformatted whitespace in regions you didn't need to touch
- Renamed variables/functions outside the scope of the request
- "Improved" comments, docstrings, or imports unrelated to the change

## Output format when this skill is active

After the change, include:

```
Diff scope:
- Changed: <list of files + what>
- Pre-existing issues noticed (NOT changed): <list, or "none">
- Orphans removed (caused by my change): <list, or "none">
```

This makes the restraint visible and gives the user a queue of follow-ups they can choose to take on.

## Anti-patterns this skill blocks

- Bug fix PRs that include a 200-line "while I was in there" reformat
- Auto-renaming variables to your preferred convention
- "Modernizing" code (e.g., switching to f-strings, arrow functions, optional chaining) when not asked
- Deleting a function because you don't see it called (it might be used by reflection, dynamic dispatch, or external callers)
- Reorganizing imports as a side effect
- Updating dependency versions you weren't asked to update

## When NOT to apply

- The user explicitly asked for a refactor, cleanup, or style pass
- You are creating a new file (no existing style to preserve)
- The "adjacent" change is genuinely required to make the requested change compile/pass tests

## Success signal

PRs are reviewable in under five minutes. Reviewers don't ask "why did this line change?" The blast radius of every change matches its stated intent.
