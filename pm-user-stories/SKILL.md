---
name: pm-user-stories
description: |
  Write sprint-ready user stories from a PRD or feature spec using the 3 C's + INVEST criteria.
  Triggers when:
  - A PRD or feature spec exists and needs to be broken into backlog items
  - User says "write user stories for", "break this into stories", "create backlog items"
  - Sprint planning is approaching and stories aren't written yet
  - Development team needs acceptance criteria before building

  Output: A complete set of user stories with 4-6 testable acceptance criteria each.
  Format: "As a [role], I want [action], so that [benefit]."

license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/pm-skills
  version: "1.0.0"
---

# PM Skill: User Stories

**Purpose:** Transform PRD features into sprint-ready backlog items with clear acceptance criteria. One story = one sprint. Every acceptance criterion = testable.

---

## Framework: 3 C's + INVEST

**3 C's:**
- **Card:** Simple title + one-liner (what the user does)
- **Conversation:** The intent behind the story — context the team needs to build it correctly
- **Confirmation:** Acceptance criteria — how we know it's done

**INVEST criteria** (every story must pass all 6):
- **I**ndependent — can be developed without another story being done first
- **N**egotiable — scope can be adjusted without breaking the core value
- **V**aluable — delivers value to a real user on its own
- **E**stimable — team can size it
- **S**mall — completable within one sprint
- **T**estable — acceptance criteria can be verified

---

## Story Format

```
Story: [Short title]
As a [specific user role],
I want [specific action or capability],
So that [tangible benefit to them].

Priority: P0 / P1 / P2
Design: [Link to Figma/prototype if available]
Notes: [Any context or constraints the developer needs]

Acceptance Criteria:
- [ ] [Normal operation: the happy path works as described]
- [ ] [Edge case 1: boundary condition is handled]
- [ ] [Edge case 2: another boundary]
- [ ] [Error state: what happens when something goes wrong]
- [ ] [Technical consideration: performance, security, or data requirement]
- [ ] [Accessibility or cross-device consideration if relevant]
```

---

## Process

### Step 1: Analyze the PRD
Read the PRD's Section 7 (features, P0/P1/P2). Identify all distinct user actions or capabilities.

### Step 2: Identify User Roles
From the PRD's market segment and value proposition sections, list the distinct roles interacting with this feature. Use specific roles ("clinic receptionist", "patient", "admin") not generic ones ("user").

### Step 3: Write Stories — One Action Per Story
Each story covers exactly one user action. If a story contains "and" in the want clause, split it.

### Step 4: Write Acceptance Criteria
For each story, write 4–6 acceptance criteria covering:
1. The primary happy path (normal operation)
2. At least one edge case
3. At least one error/failure state
4. One technical or non-functional requirement (performance, security, accessibility)

### Step 5: INVEST Check
Before finalizing, confirm each story is independently shippable, sized for one sprint, and has verifiable criteria.

---

## Example

```
Story: View appointment history
As a clinic receptionist,
I want to view a patient's full appointment history in one place,
So that I can answer patient questions without switching between screens.

Priority: P0
Design: [Figma link]

Acceptance Criteria:
- [ ] All past appointments display in reverse chronological order (most recent first)
- [ ] Each row shows: date, time, type, status, and assigned provider
- [ ] Cancelled appointments are shown with a "Cancelled" badge, not hidden
- [ ] If no appointments exist, an empty state message reads "No appointments yet"
- [ ] List loads within 1 second for patients with up to 500 appointments
- [ ] Only staff with "receptionist" or "admin" role can view this page
```

---

## Pairs With

- `pm-prd` — run first; stories are derived from the PRD's P0/P1 features
- `pm-job-stories` — use instead when focusing on user context/motivation rather than role
- `superpowers-write-plan` — convert stories into implementation tasks once approved
