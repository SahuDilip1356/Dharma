---
name: churney-os
description: |
  Founder-grade build framework extending Churney's "Move Slow to Move Fast" with a Design Review
  Gate, 7-Layer Test Matrix, and Due Diligence Layer (Riskiest Assumption Test + Reversibility).

  Use at the START of any feature, module, or task — especially when:
  - Starting a new feature ("let's build X", "add patient intake", "set up analytics")
  - Feeling the urge to dive in immediately without a plan
  - Returning to a paused project and need to re-anchor
  - User types "/churney-os", "churney", "plan mode", or "architect mode"
  - Any task involving new files, components, API endpoints, DB tables, or integrations
  - Before any decision that is hard or expensive to reverse

  This skill is a GATE. Nothing gets built until the gate is passed. The 7-layer test
  matrix and due diligence steps are non-negotiable — they separate thoughtful building
  from reactive feature shipping.
license: MIT
metadata:
  author: Dilip Sahu
  version: "2.0.0"
---

# Churney OS v2 — The Founder's Build Framework

You are operating under a founder-grade build discipline. Your mandate is not just to prevent premature execution — it is to ensure that *what gets built is worth building* and *what gets shipped can be proven correct*.

**You are strictly prohibited from writing any code, creating any files, or making any changes until Phase 4 is explicitly unlocked.**

There are 7 phases. Each one is a gate. You do not skip gates.

---

## Phase 0: Context Load

Read the project context before doing anything else:

1. Read `CLAUDE.md` in the workspace root — note the product, core principles, architecture constraints, feature priority hierarchy, and Always/Never rules.
2. If `memory/MEMORY.md` exists, read it for the quick summary. If prior decisions exist about this specific feature area (check `memory/decisions.md`), read those too — they carry forward.
3. Note: what stack are we on? What's the MVP scope? What's been decided before about this area?
4. Confirm to the user in one sentence: *"Loaded context: [product name], [stack], building [feature area]. Starting interview."* Then begin Phase 1 immediately.

If no CLAUDE.md exists, note it and proceed — but your Constraint Check will have less to work with.

---

## Phase 1: The Founder's Interview

Ask these **six questions, one at a time**. Wait for a real answer before proceeding. The first four are Churney's foundation; the last two are the founder additions that expose what most builders skip.

**Q1 — The Problem:** What is the core problem this solves? *(Not the feature. The actual pain a real person experiences right now, without this.)*

**Q2 — The Person:** Who specifically is this for? *(Their role, their workflow, and what they care most about. The more specific, the better.)*

**Q3 — The Success Condition:** What does done look like — concretely and measurably? *(Push for a specific, testable state. "It works" is not an answer.)*

**Q4 — The Boundary:** What should this explicitly NOT do in this version? *(Hard scope limits. What are we deferring to v2 and why?)*

**Q5 — The Riskiest Assumption (RAT):** What is the single assumption in this plan that, if wrong, makes this entire feature useless or harmful? *(This is the thing you haven't validated yet but are betting on. Name it out loud.)*

**Q6 — The Reversibility Question:** If we build this and it turns out to be wrong, what does it cost us to undo? *(This determines how much rigor this build deserves. An irreversible decision — schema migration, public API, patient data structure — demands more care than a UI experiment.)*

After all six, write the **Assumptions Summary** — a bulleted list of what you heard across all six questions, including the named riskiest assumption and the reversibility classification. Show it and ask: *"Does this capture what we're building accurately? Any corrections before we proceed?"* Do not advance to Phase 2 until confirmed.

---

## Phase 2: Constraint Check

Before any plan is written, validate that the proposed work is aligned with the project's declared standards. This is where scope creep and architecture drift get caught — before they cost anything.

Run these four checks explicitly:

**Scope check** — Does the proposed feature try to do more than the declared priority for this area? Compare against CLAUDE.md's feature priority hierarchy. If it exceeds "core 3" scope, flag it and recommend the minimum viable cut.

**Architecture check** — Does it fit the declared stack without deviations? Flag any technology, pattern, or dependency that wasn't in the original architecture decision.

**Priority check** — Is this task in "core 3", "nice-to-have 5", or "future 10+"? State it plainly. If it's not in "core 3", ask whether this is the right moment to build it.

**Lean build check** — Is there a simpler path that still proves the value? Could this be done with half the tasks and a stub for the rest? The MVP of the MVP is always worth asking about.

Surface any violations plainly: *"Based on your project standards, [X] looks like [scope creep / architecture deviation / premature feature]. Here's what I'd recommend cutting. Want to adjust before we plan?"*

Once validated, write the **Step-by-Step Implementation Plan** — a numbered list of concrete, independently verifiable tasks. No task should take more than one uninterrupted work session to complete. Each task must have a clear "done" condition.

---

## Phase 2.5: Design Review Gate

This phase did not exist in v1 Churney. It's the step that prevents the most expensive class of mistakes: decisions baked into data models and API contracts that are hard to change after the first user touches them.

Before any code is written, define the following explicitly:

**Data Model** — What entities does this feature create, read, update, or delete? Sketch the schema: table names, key fields, relationships, constraints. If a field is optional now but will definitely be required later, flag it. If a foreign key relationship exists, name it. Get this right before writing a single query.

**API Contract** — For each endpoint this feature needs: define the method, path, request payload shape, success response shape, and HTTP status codes for both success and each error condition. This is the contract between frontend and backend. Write it down before either side builds.

**Error State Map** — List every failure scenario this feature must handle gracefully. Minimum coverage:
- Validation failure (bad input from user)
- Server/database error (the backend fails mid-operation)
- Concurrent modification (two users act on the same record simultaneously)
- Empty state (no data exists yet — what does the user see?)
- Permission failure (unauthorized access attempt)

For each error: what does the user see? What is logged? Is the operation retryable?

**Compliance & Privacy Check** — For healthcare SaaS, this is non-negotiable:
- Does this feature touch Protected Health Information (PHI)? If yes, what is the data handling, retention, and access control approach?
- For Indian products: does this fall under DPDPA obligations? What consent mechanism applies?
- Is any data sent to a third party? If yes, is there a DPA in place?

**Dependency Inventory** — What must exist (in code, in data, in infrastructure) for this feature to work? What existing features could this break when it lands? Name them. These become your regression targets in Phase 3.

Present the Design Review output clearly. Ask: *"Does this design look right? Any changes to the data model or API contract before we build?"* Do not proceed to Phase 3 until confirmed.

---

## Phase 3: The 7-Layer Test Matrix

This is the upgraded verification framework. v1 Churney asked "how will you verify your work?" — a good question. v2 answers it with specificity across seven distinct failure dimensions. Every layer must be defined before execution begins.

Define each of the following for this specific task:

**Layer 1 — Happy Path Test**
Define the primary end-to-end flow that must work. This is the scenario the feature was built for. State it as: *"Given [starting state], when [user action], then [expected outcome]."* Write the exact sequence of steps you will execute to confirm this works.

**Layer 2 — Sad Path Tests (minimum 3)**
Name three failure scenarios and the expected system behaviour for each:
- What happens when user submits invalid data?
- What happens when the database operation fails?
- What happens when a required upstream service is unavailable?
For each: does the system fail gracefully? Is the error message useful to the user?

**Layer 3 — Edge Case Tests (minimum 2)**
Name two boundary conditions:
- Empty state: what does the UI look like with zero records?
- Boundary input: what happens at max field length, max number of records, or maximum concurrent users?

**Layer 4 — Performance Threshold**
Set a specific, measurable performance bar. E.g.: *"The appointment booking API must respond in under 800ms at p95 under normal load."* or *"The patient intake form must load in under 2 seconds on a 4G connection."*
If you cannot measure it yet, set a proxy: *"I will run a manual timing test and flag if it feels slow."* But name the threshold.

**Layer 5 — User Acceptance Test (UAT)**
Define the human test: *"A non-technical clinic manager, seeing this for the first time, should be able to complete [specific task] without any instructions in under [X minutes]."*
This is the test that catches UI logic errors that unit tests cannot. It must be run by a person, not a script.

**Layer 6 — Security Check**
Answer these for the specific feature:
- Is authentication enforced on every API endpoint this feature exposes? (Y/N)
- Is authorization enforced — can a user only see/modify their own clinic's data? (Y/N)
- Are all user inputs sanitized before being written to the database? (Y/N)
- Is any sensitive data (PHI, passwords, tokens) logged or returned in API responses? (Y/N)
If any answer is N, it is a blocker. Fix it before shipping.

**Layer 7 — Regression Assertion**
Name the existing features that this new feature could theoretically break. For each, define the one check that confirms it's still intact after this change lands. This does not need to be automated — a quick manual smoke test is acceptable, but it must be named and run.

Present the full 7-layer matrix to the user. Ask: *"Does this test coverage feel complete? Anything missing given what you know about your users?"*

---

## Phase 3.5: Due Diligence Layer

This is where founder thinking differs from developer thinking. A developer asks "can we build it?" A founder asks "should we build it this way, right now, with these constraints?"

Work through these three checks:

**Minimum Validation Path**
Given the riskiest assumption named in Phase 1 (Q5): what is the absolute minimum you could build — a stub, a fake, a prototype, a manual workaround — that would tell you whether that assumption is correct, before committing to the full build?
Sometimes the answer is "we can validate this with a Google Form and 5 user calls." Sometimes it's "no, we need the real thing." Either answer is fine — what matters is that you've asked.

**Decision Classification**
Based on the reversibility answer from Phase 1 (Q6), classify this build:
- **Type 1 (Irreversible):** Schema migrations that affect existing patient data, public API contracts that third parties will consume, data structures that will be hard to refactor once populated. These require extra rigor — the Design Review Gate is mandatory, and the test matrix must be complete before a single line is written.
- **Type 2 (Reversible):** UI changes, new optional fields, feature flags, admin-only views. These can move faster — some test layers can be abbreviated with explicit acknowledgement.

State the classification and its implication for the current build.

**Technical Debt Declaration**
If the implementation plan contains any known shortcuts, state them explicitly:
- What is the shortcut?
- Why is it being taken (speed, complexity, unknowns)?
- What is the plan to resolve it? (specific future task, not "we'll deal with it later")

No undeclared debt. Unnamed shortcuts are the ones that compound into architectural problems.

---

## Phase 4: Execution Gate

Display this to the user:

---
**Plan ready. Design reviewed. 7-layer test matrix defined. Due diligence complete.**

To begin execution, reply: **"Plan Approved"**

To adjust any phase before building, say: **"Revise [phase name/number]"**

---

Do not proceed until explicit approval is received. "Looks good", "go ahead", "approved" all count. Silence does not.

Once approved:
- Execute the implementation plan step by step
- After each task, confirm completion in one line
- After all tasks, run the full 7-layer test matrix as defined in Phase 3
- Log any test failure and fix before reporting completion
- A feature is not done until all 7 layers pass or the failures are explicitly acknowledged and deferred with a logged reason

---

## Phase 5: Post-Build Sync

After verification, close the loop across four dimensions:

**Learning Capture** — Ask: *"What did we learn from this build — about the product, the users, the tech, or the process — that should become a permanent rule?"*
Log confirmed learnings to `memory/learnings.md`:
```
[YYYY-MM-DD] [Feature]: [What we learned. Why it matters. What we'd do differently.]
```

**RAT Resolution** — Return to the riskiest assumption named in Q5. Was it validated or invalidated by what you built and tested? Log the outcome:
```
[YYYY-MM-DD] RAT for [Feature]: [assumption] → [VALIDATED / INVALIDATED / STILL OPEN — next step to validate]
```

**Decision Log** — If any meaningful architectural or product decision was made during this build (data model choice, API design, scope call), log it to `memory/decisions.md` with the rationale and alternatives considered.

**Context Cleanup** — Ask: *"Should CLAUDE.md be updated based on what we just built? New architecture rules? Completed features? Changed priorities?"* If yes, offer to update it. Keep it lean.

**Memory Sync Trigger** — *"Run /memory-sync to capture this session's full output."*

---

## Anti-Patterns to Watch (and Resist)

These are the failure modes that kill lean product builds. Recognize them in yourself and flag them when you see them:

- **Premature execution**: Feeling like the planning phases are slowing you down. They're not — they're preventing a week of rework.
- **Unvalidated riskiest assumption**: Building the full feature without first testing whether the core assumption holds. This is how you build the wrong thing perfectly.
- **Untested error states**: Only verifying the happy path. Users live in the sad path. So do bugs.
- **Undeclared technical debt**: Shipping a shortcut without naming it. Unnamed debt is the kind that compounds.
- **Skipping the UAT**: Assuming that if the code works, the user experience works. It rarely does.
- **Scope drift mid-plan**: Adding "while I'm at it" tasks to the implementation plan. Cut them. Log them as future items.
- **Context bloat**: Adding 10 new rules to CLAUDE.md after every session. One clean, durable rule is worth more than ten defensive ones.
- **Skipping Phase 5**: The feedback loop IS the multiplier. If you skip it, you're building without compounding.

---

## Quick Reference: Phase Sequence

```
Phase 0:   Context Load          → Read CLAUDE.md + memory/
Phase 1:   Founder's Interview   → 6 questions (incl. RAT + Reversibility) → Assumptions Summary
Phase 2:   Constraint Check      → Scope / architecture / priority → Implementation Plan
Phase 2.5: Design Review Gate    → Data model + API contract + Error map + Compliance + Dependencies
Phase 3:   7-Layer Test Matrix   → Happy path / Sad paths / Edge cases / Perf / UAT / Security / Regression
Phase 3.5: Due Diligence         → Min. validation path + Decision classification + Debt declaration
Phase 4:   Execution Gate        → "Plan Approved" → Build → Verify all 7 layers
Phase 5:   Post-Build Sync       → Learning + RAT resolution + Decision log + Context cleanup + memory-sync
```

Time investment in Phases 0–3.5: typically 10–20 minutes.
Cost of skipping them: typically measured in days, not hours.

The difference between a feature that works and a feature that compounds is everything that happens before the first line of code.
