---
name: pm-job-stories
description: |
  Write JTBD-style job stories that focus on user context and motivation instead of role.
  Triggers when:
  - User says "write job stories", "JTBD stories", "situation-motivation-outcome"
  - The feature is context-dependent (triggered by a situation, not just a user type)
  - Exploring user motivations before writing a PRD or spec
  - User stories feel too role-centric and miss the "why" behind the action

  Format: "When [situation], I want to [motivation], so I can [outcome]."
  Use this instead of user stories when the triggering situation matters as much as the role.

license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/pm-skills
  version: "1.0.0"
---

# PM Skill: Job Stories (JTBD)

**Purpose:** Write requirement backlog items grounded in the situations and motivations that drive user behavior — not just who the user is, but what's happening when they reach for the product.

**When to use over user stories:** When the triggering context matters more than the user's role. A clinic receptionist checking appointment history before a call has a very different motivation than checking it during patient intake — same role, different job.

---

## Format

```
Story: [Short title]
When [triggering situation — what just happened or is about to happen],
I want to [motivation — what the user is trying to accomplish or avoid],
So I can [desired outcome — the result they're after].

Priority: P0 / P1 / P2
Design: [Link to Figma/prototype if available]

Acceptance Criteria:
- [ ] [Observable behavior in the triggering situation]
- [ ] [Motivation is served — the action they want is easy and clear]
- [ ] [Outcome is achieved — the result is visible/confirmed]
- [ ] [Edge case: what if the situation occurs with incomplete data]
- [ ] [Edge case: what if the situation occurs for the first time / empty state]
- [ ] [Non-functional: performance, security, or accessibility in this context]
```

---

## Core Principle

Jobs-to-be-Done shifts focus from **who the user is** to **what they're trying to accomplish in a specific moment**.

| User Story | Job Story |
|-----------|-----------|
| As a receptionist... | When a patient calls to reschedule... |
| As a doctor... | When reviewing a patient's chart before a consult... |
| As an admin... | When preparing the monthly billing report... |

The situation changes what "good" looks like. Design for the situation, not just the role.

---

## Process

### Step 1: Identify Triggering Situations
List the real-world moments that lead a user to need this feature. Think: "What just happened right before they open the app?" or "What are they about to do?"

### Step 2: Identify the Motivation (Not the Action)
The motivation is deeper than the action. Distinguish:
- Action: "view appointment history"
- Motivation: "not look uninformed when the patient is on the phone"

Ask "why does this matter to them right now?" until you reach the real motivation.

### Step 3: Define the Outcome
The outcome is the state the user wants to be in after completing the job. It should be observable or confirmable.

### Step 4: Write Acceptance Criteria
6–8 criteria covering:
1. The primary situation is handled correctly
2. The motivation is served (the action is obvious and fast)
3. The outcome is confirmed (user knows they succeeded)
4. At least two edge cases (incomplete data, first time, error)
5. Performance or accessibility in this context

---

## Example

```
Story: Avoid billing surprises at appointment end
When a patient is checking out and asks about their balance,
I want to see their outstanding amount and recent charges in one view,
So I can give them an accurate answer without putting them on hold.

Priority: P0

Acceptance Criteria:
- [ ] Outstanding balance and last 3 charges display on the patient card in under 2 seconds
- [ ] Charges show service description, date, and amount — no billing codes the receptionist can't explain
- [ ] If balance is zero, shows "No outstanding balance" — not a blank
- [ ] If charges are still processing, shows "Pending" with expected date
- [ ] Receptionist can tap to email a summary to the patient from this view
- [ ] Only roles with billing_read permission can see this data
```

---

## Pairs With

- `pm-prd` — run first; job stories enrich the Value Proposition section and inform feature scope
- `pm-user-stories` — use when role-based framing is clearer than situation-based
- `churney-os` — the Riskiest Assumption Test (Q5) often maps to an unvalidated job story
