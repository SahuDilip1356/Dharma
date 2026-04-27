---
name: superpowers-tdd
description: |
  Test-Driven Development — enforces RED-GREEN-REFACTOR as the mandatory implementation cycle.
  Triggers when:
  - Writing any production code for a feature or bug fix
  - User says "write the code", "implement this", "add this function/component/endpoint"
  - Any task from an implementation plan is being executed
  - superpowers-execute delegates a coding task

  THE NON-NEGOTIABLE RULE: No production code without a failing test first.
  If code exists before its test, delete it and start over.
  This is the execution core of Phase 4 in the Superpowers methodology.
license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/superpowers
  version: "1.0.0"
---

# Superpowers: Test-Driven Development

**Core rule: Write the test first. Watch it fail. Write minimal code to pass.**

---

## The RED-GREEN-REFACTOR Cycle

### 🔴 RED — Write a Failing Test

Write the minimal test that demonstrates the desired behavior. The test must:
- Be specific to one behavior (not testing multiple things)
- Use the exact function/component signature from the plan
- Fail for the RIGHT reason (not a syntax error or missing import)

```
Run: [test command]
Expected output: 1 failing test
Failure reason: [name of missing function/component] is not defined
```

**Verify RED:** If the test passes immediately, stop. The test is wrong — it proves nothing.  
**Verify RED:** If the test errors on syntax or import, fix that before counting it as a valid RED.

---

### 🟢 GREEN — Implement the Minimum

Write the simplest code that makes the test pass. No more.

Forbidden in GREEN phase:
- Adding functionality not tested yet
- Abstracting for "future flexibility"
- Handling error cases not tested
- Refactoring — that comes next

```
Run: [test command]
Expected output: all tests pass, 0 warnings
```

If GREEN fails, go back to implementation — do not add more tests yet.

---

### 🔵 REFACTOR — Clean Up

With tests green, now improve the code structure:
- Remove duplication
- Extract to well-named functions
- Improve readability
- Match existing codebase patterns

```
Run: [test command] after every change
Required: all tests still pass after refactor
```

Commit: `git commit -m "feat: [behavior] with tests"`

---

## Common Rationalizations to Reject

| Rationalization | Why it's wrong |
|----------------|----------------|
| "I'll write tests after" | Tests written after code always pass — they prove nothing |
| "This is too simple to need a test" | Simple code breaks in simple ways |
| "I'll test it manually" | Manual testing isn't systematic and doesn't prevent regression |
| "Keeping the code as reference while writing tests" | Keeping unverified code = technical debt day one |
| "We don't have time for TDD" | TDD is faster than debugging production failures |

---

## TDD for Different Code Types

**Functions / Services:**
```
test("returns X when given Y") → implement function → verify → commit
```

**React Components:**
```
test("renders [element] when [condition]") → implement component → verify → commit
```

**API Endpoints:**
```
test("POST /endpoint returns 201 with [shape]") → implement route → verify → commit
```

**Bug Fixes:**
```
test("reproduces the bug") [must FAIL first] → fix → test passes → commit
```

For bug fixes: the failing test IS the proof the bug existed. If you can't write a test that reproduces the bug, investigate further before fixing.

---

## Success Signals

TDD is working when:
- You catch bugs during RED phase, before a line of production code is written
- Refactoring feels safe because tests catch regressions immediately
- Code design improves — TDD surfaces bad APIs before they're baked in
- "Done" means "tests pass", not "I think it works"
