# Coding Discipline Skill Evaluation

## Q1

Files read: SKILL.md, surgical-changes.md

**Before I code:**
- Assumptions: `fetchConsents()` is an async call in lib/api.ts that can fail transiently; retry logic should use exponential backoff or a standard retry utility; we're adding retry at the call site (not inside fetchConsents itself); retries should stop after a reasonable number of attempts (3-5 likely).
- Interpretations I'm choosing between: none - the request is clear.
- Open questions: none.

**What I would do:**

I would edit lib/api.ts to wrap the fetchConsents() call with retry logic. Working under surgical-changes principle, I would touch only the specific call location and not refactor adjacent code.

Example of what would be written (pseudocode):

```typescript
// lib/api.ts
import { retry } from './utils/retry'; // assuming this exists

// Inside the function that calls fetchConsents():
const consents = await retry(
  () => fetchConsents(),
  { maxAttempts: 3, delayMs: 1000 }
);
```

**Diff scope:**
- Changed: lib/api.ts — wrapped fetchConsents() call with retry; added import of retry utility if it doesn't exist
- Pre-existing issues noticed (NOT changed): none
- Orphans removed: none

---

## Q2

Files read: SKILL.md, think-before-coding.md

**Before I code:**

This request is ambiguous and violates the first principle — I cannot proceed without clarifying what "better" means.

**Assumptions I'm NOT making:**
- Which dashboard (which file, URL, or component)?
- Better in what way? Performance, UX/design, features, code quality, accessibility, data accuracy?
- For whom? End users, admins, data analysts?
- What's the success metric? (load time <500ms, improved click-through, reduced errors, accessibility WCAG AA compliance?)

**Interpretations I'm choosing between:**
1. Performance optimization (faster load, fewer API calls)
2. UX/UI improvements (clearer layout, better visual hierarchy, accessibility)
3. Feature additions (new metrics, filters, export options)
4. Data accuracy (fix stale queries, sync issues)
5. Code quality (refactor, unit test, documentation)

**Open questions:**
1. Which dashboard are we improving?
2. What specific problem are users or stakeholders facing with it today?
3. What is the measurable definition of "better"?
4. Are there constraints (time, dependencies, backward compatibility)?

**My response to the user:**

I'd stop here and ask: "To help you improve the dashboard, I need to understand:
- Which dashboard? (file path or name)
- What's the main issue? (slow loading, confusing layout, missing data, errors?)
- How will we know it's better? (e.g., load time under 1s, no accessibility warnings, users spend 20% less time finding what they need)

Once I know these, I can make surgical, focused changes that trace back to your goal."

---

## Q3

Files read: SKILL.md, surgical-changes.md

**Before I code:**
- Assumptions: `usr` is a local/parameter variable in components/Profile.tsx (not imported from elsewhere, not a global); renaming it to `user` does not conflict with existing bindings; this is a code-quality improvement, not a bug fix, but the request is explicit and the change is narrow.
- Interpretations I'm choosing between: none - this is a straightforward variable rename.
- Open questions: none.

**What I would do:**

Under surgical-changes principle, I would:

1. Search for all occurrences of `usr` in components/Profile.tsx
2. Replace each with `user` (not touching any adjacent code)
3. Verify no other files reference this variable (if they do, rename there too — that's part of finishing the change)

I would NOT touch:
- Comments unrelated to this variable
- Whitespace or formatting elsewhere in the file
- Anything that doesn't directly trace to the rename

Example of what would be written:

```typescript
// Before:
const Profile = ({ usr }) => {
  return <div>{usr.name}</div>;
};

// After:
const Profile = ({ user }) => {
  return <div>{user.name}</div>;
};
```

**Diff scope:**
- Changed: components/Profile.tsx — renamed parameter/variable `usr` to `user` throughout (X occurrences)
- Pre-existing issues noticed (NOT changed): none
- Orphans removed: none
