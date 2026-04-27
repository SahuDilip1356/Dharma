# Phase Gates

Entry criteria and exit evidence for each phase.
A phase cannot start until the previous phase's exit evidence exists.

---

## Phase 0: Intent Gate
**Purpose:** Establish what we're building and why before anything else.
**Applies to:** All work types.

### Entry Criteria
- A request exists (any form — idea, ticket, complaint, instruction)

### Checklist
- [ ] User identified (who is affected or benefits)
- [ ] Problem identified (what pain or gap exists)
- [ ] Desired outcome defined (what success looks like)
- [ ] Non-goals stated (what this will NOT do)
- [ ] Success criteria defined (measurable, not vague)
- [ ] Risk level classified
- [ ] Reversibility classified

### Exit Evidence
```
Goal: [one sentence]
User: [who]
Success: [measurable criteria]
Out of scope: [explicit cuts]
Risk: [low | medium | high | critical]
Reversibility: [easy | moderate | hard]
```

### Block Condition
Do not advance to Phase 1 if:
- Goal is contradictory or undefined
- Risk is `critical` without explicit user approval
- Destructive action requested without confirmation

---

## Phase 1: UX Gate
**Purpose:** Define user experience intent before design or code.
**Applies to:** All user-facing work (mandatory). Optional for internal/backend-only.

### Entry Criteria
- Phase 0 exit evidence exists

### Checklist
- [ ] User flow defined (steps the user takes)
- [ ] Primary action identified (the one thing the screen/feature must do well)
- [ ] Information hierarchy clear (what's most important, what's secondary)
- [ ] All states designed: empty / loading / error / success / disabled
- [ ] Accessibility concerns identified (contrast, keyboard, ARIA, semantic HTML)
- [ ] Responsive behavior planned (mobile / tablet / desktop breakpoints)
- [ ] Visual direction selected (style, colors, fonts via `uiux-design-intelligence`)

### Exit Evidence
```
User flow: [steps or screen names]
Primary action: [one thing]
States covered: empty ✅ / loading ✅ / error ✅ / success ✅
Accessibility notes: [key concerns]
Responsive plan: [behavior at 375 / 768 / 1280px]
Visual direction: [style name + color + font]
```

### Block Condition
Do not advance to Phase 2 if:
- User-facing feature has no defined states (empty/error/success)
- Accessibility has not been considered at all
- No visual direction has been chosen (no style + color decision)

---

## Phase 2: Planning Gate
**Purpose:** Produce a verifiable implementation plan before writing code.
**Applies to:** All work types except `release` and `research-only`.

### Entry Criteria
- Phase 0 exit evidence exists
- Phase 1 exit evidence exists (if user-facing)

### Checklist
- [ ] Assumptions listed (all implicit choices named)
- [ ] Files / components likely affected identified
- [ ] Risks listed (what could go wrong)
- [ ] Implementation steps defined (2–5 min each, independently verifiable)
- [ ] Test approach defined (what tests will prove this works)
- [ ] Dependencies identified (what must exist before this can run)

### Exit Evidence
```
Assumptions: [list]
Files affected: [list]
Risks: [list]
Plan: [numbered steps with verify: checks]
Test approach: [unit | integration | e2e | manual]
```

### Block Condition
Do not advance to Phase 3 if:
- No implementation plan exists for non-trivial work
- High-risk work has no test approach defined

---

## Phase 3: Build Gate
**Purpose:** Enforce discipline during implementation.
**Applies to:** All work types that produce code or design output.

### Entry Criteria
- Phase 2 exit evidence exists (plan)

### Checklist
- [ ] Smallest viable change — no over-engineering
- [ ] No speculative abstractions added
- [ ] No unrelated code modified (surgical changes)
- [ ] Existing behavior preserved unless explicitly changing it
- [ ] TDD followed: failing test written before production code
- [ ] User-facing changes follow design direction from Phase 1
- [ ] React patterns followed for frontend work

### Exit Evidence
```
Changed files: [list]
TDD status: RED seen ✅ / GREEN achieved ✅
Scope note: [what was deliberately not changed]
```

### Block Condition
Do not advance to Phase 4 if:
- Production code was written without a failing test first (TDD violation)
- Unrelated files were modified without justification

---

## Phase 4: Verification Gate
**Purpose:** Require evidence before claiming work is done.
**Applies to:** All work types.

### Entry Criteria
- Phase 3 exit evidence exists

### Checklist

**Code verification:**
- [ ] Unit/integration tests run — pass count recorded
- [ ] Build passes (no compile errors)
- [ ] Typecheck passes (if TypeScript)
- [ ] Lint passes

**UI verification (if user-facing):**
- [ ] Accessibility audit run (`uiux-accessibility-review`)
- [ ] Responsive behavior checked at 375 / 768 / 1280 / 1440px
- [ ] All states verified: empty / loading / error / success
- [ ] Keyboard navigation tested (Tab, Enter, Escape)
- [ ] Focus states visible

**Performance verification (if performance work):**
- [ ] Before metric recorded
- [ ] After metric recorded (same method)
- [ ] Improvement confirmed

### Exit Evidence
```
Tests: [N passed / M failed]
Build: ✅ / ❌
Typecheck: ✅ / ❌
UI checks: [accessibility ✅ | responsive ✅ | states ✅]
Screenshots: [attached or described]
Known risks: [list or "none"]
```

### Block Condition
Do not advance to Phase 5 if:
- Tests are failing
- Build is broken
- User-facing work has not been accessibility-checked

---

## Phase 5: Finish Gate
**Purpose:** Clean close — summary, risks stated, next step clear.
**Applies to:** All work types.

### Entry Criteria
- Phase 4 exit evidence exists

### Checklist
- [ ] Summary written (what changed and why)
- [ ] Remaining risks stated (or confirmed none)
- [ ] Next step identified (merge / PR / monitor / follow-up)
- [ ] Worktree / branch cleaned up if applicable
- [ ] memory-sync triggered if decisions were made

### Exit Evidence
```
Summary: [what was built / fixed / changed]
Verified: [evidence reference]
Remaining risks: [list or "none"]
Next: [merge | PR | monitor | follow-up task]
```
