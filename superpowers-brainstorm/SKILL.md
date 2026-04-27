---
name: superpowers-brainstorm
description: |
  Design before code — structured Socratic dialogue to turn ideas into an approved spec before
  any implementation begins. Triggers when:
  - User has an idea but no written design yet
  - Starting a new feature, module, or system
  - User says "I want to build X", "let's design", "brainstorm", "what should we do for Y"
  - Before writing-plans is invoked (design must come first)

  Hard gate: No code or implementation until design is written and approved.
  This is Phase 1 of the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Brainstorm (Design Before Code)

**Hard gate: No code, no files, no changes until a design is presented and approved.**

---

## Process

### Step 1: Clarify (one question at a time)
Ask focused questions to understand purpose, constraints, and success criteria. Prefer multiple-choice over open-ended. Do not ask more than one question per message.

Cover:
- What problem does this solve for a real user?
- What does "done" look like — specifically and measurably?
- What should this explicitly NOT do in this version?
- What existing systems/patterns does this need to work with?
- What are the constraints (time, stack, dependencies)?

### Step 2: Explore Approaches
Propose 2–3 different approaches with trade-offs + a clear recommendation. Show the simpler path when one exists.

Format:
```
Option A: [name]
→ How it works: [one sentence]
→ Pros: [2-3 bullets]
→ Cons: [1-2 bullets]

Option B: [name]
...

Recommendation: Option [X] because [one sentence reason].
```

### Step 3: Present Design in Sections
Break the design into sections scaled to complexity (brief for simple, up to 300 words for nuanced areas). Seek approval after each section before proceeding to the next.

Required sections:
1. **Scope** — what this does and what it explicitly doesn't do
2. **Data Model** — entities, fields, relationships (even rough)
3. **API / Interface Contract** — method, path/signature, request/response shapes
4. **Error States** — validation failure, server error, empty state, permission failure
5. **Dependencies** — what must exist for this to work; what could this break?

### Step 4: Self-Review
Before presenting to user, check the spec for:
- Placeholders or TBD sections → fill them or flag them
- Contradictions between sections → resolve
- Ambiguous language → make concrete
- Scope that exceeds the stated goal → trim

### Step 5: Save and Commit
Save the approved spec to:
```
docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md
```
Commit it: `git add` + `git commit -m "docs: design spec for <topic>"`

### Step 6: Hand Off to Writing Plans
After design approval, say:
> "Design approved and saved. Ready to write the implementation plan. Invoke `superpowers-write-plan` to continue."

---

## Rules

- Never start implementation during brainstorming — the gate is real
- Follow the existing codebase patterns — design should fit, not fight, what's there
- Break systems into well-bounded units with clear purposes
- Treat even simple tasks as requiring design — the habit is the discipline
