---
name: pm-prd
description: |
  Professional-grade Product Requirements Document (PRD) creation using an 8-section framework
  grounded in Teresa Torres, Marty Cagan, and Dan Olsen methodology. Triggers when:
  - User wants to write, draft, or create a PRD
  - Starting a new feature, product, or initiative that needs specification
  - User says "write a PRD for", "draft requirements for", "spec out", "document this feature"
  - Churney OS has run and the approved plan needs to be formalized as a PRD
  - Stakeholder alignment is needed before development begins

  Output: A production-ready PRD saved as docs/PRD-[product-name].md
  
  Approach: Ask clarifying questions before writing — tight scope beats vague expansion.
  Non-goals must be explicit. Success metrics must be measurable. Assumptions must be flagged.

license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/pm-skills
  version: "1.0.0"
---

# PM Skill: Create PRD

**Purpose:** Produce an authoritative, stakeholder-ready PRD that aligns teams and guides development. Built on proven PM frameworks — not a template dump, a structured thinking process.

---

## Before Writing: Ask These Questions (One at a Time)

Ask in order of importance. Stop when you have enough to write with confidence.

1. **Problem:** What specific problem does this solve? For whom exactly?
2. **Users:** Which user segments are affected? What are their current workarounds?
3. **Success:** How do we measure success? What are the SMART metrics?
4. **Constraints:** What are the technical, timeline, or resource constraints?
5. **Market:** Are there existing solutions? What's our differentiation?
6. **Scope:** Full launch or phased? What's in v1 vs. later?

---

## The 8-Section PRD Template

### 1. Summary
Two to three sentences maximum. What is this, and why does it matter now?

```
[Product/Feature Name] is [what it is] that [solves what problem] for [who].
We're building this because [trigger — what changed or what opportunity emerged].
Success looks like [one-line outcome].
```

### 2. Contacts
| Role | Name | Responsibility |
|------|------|----------------|
| PM | | Owns the spec and delivery |
| Engineering Lead | | Technical decisions |
| Design Lead | | UX/UI |
| Stakeholder | | Final approval |

### 3. Background
- **Context:** What's the current state? What's broken or missing?
- **Trigger:** What changed that makes this the right time? (user research, data signal, market shift, compliance)
- **Prior work:** What has already been tried or decided? Link to relevant decisions.

### 4. Objective
**Goal:** [One clear, outcome-focused statement]

**Business benefits:**
- [Benefit 1]
- [Benefit 2]

**SMART Metrics:**
| Metric | Baseline | Target | Timeline | How Measured |
|--------|----------|--------|----------|--------------|
| | | | | |

**Non-goals (explicit scope cuts):**
- We are NOT building [X] in this version because [reason]
- We are NOT solving [Y] — that is a separate initiative

### 5. Market Segment(s)
Define users by the **problem they face**, not demographics.

**Primary users:** [Who faces this problem most acutely? Their role, context, frequency of the pain]

**Secondary users:** [Who is affected but not the primary beneficiary]

**Constraints and considerations:**
- [Accessibility, localization, compliance, device requirements]

### 6. Value Proposition(s)
Grounded in Jobs-to-be-Done (JTBD):

**Customer jobs addressed:**
- Functional: [What task are they trying to accomplish?]
- Emotional: [How do they want to feel?]
- Social: [How do they want to be perceived?]

**Gains we deliver:**
- [Gain 1 — specific and measurable where possible]
- [Gain 2]

**Pains we relieve:**
- [Pain 1]
- [Pain 2]

**Competitive advantage:** [Why us, why now, why better than existing alternatives]

### 7. Solution

**UX / Prototypes:**
- [Link to Figma, mockups, or describe the key flows]
- Key screens: [list]

**Features (prioritized):**
| Priority | Feature | Description | Notes |
|----------|---------|-------------|-------|
| P0 (must-have) | | | |
| P1 (should-have) | | | |
| P2 (nice-to-have) | | | |

**Technology:**
- Stack: [relevant components]
- Integrations: [APIs, third-party services]
- Performance requirements: [latency, scale, availability targets]

**Assumptions flagged for validation:**
- [ ] [Assumption 1] — validate by [method]
- [ ] [Assumption 2] — validate by [method]

**Open questions:**
- [Genuinely unresolved question 1]
- [Genuinely unresolved question 2]

### 8. Release

**Timeline:**
| Phase | Scope | Target Date |
|-------|-------|-------------|
| v1 (MVP) | [what's in] | |
| v2 | [what's deferred] | |

**Rollout plan:**
- [Internal testing / Beta / Staged rollout / Full launch]

**Dependencies:**
- [What must be ready before this ships]

**Risks:**
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| | | | |

---

## Output

Save as: `docs/PRD-[product-name].md`

Commit: `git commit -m "docs: PRD for [product name]"`

---

## Quality Check (Run Before Sharing)

- [ ] Every metric in Section 4 is SMART (Specific, Measurable, Achievable, Relevant, Time-bound)
- [ ] Non-goals are explicit — what we're NOT building is stated
- [ ] All P0 features are genuinely must-haves, not nice-to-haves
- [ ] Assumptions are listed and each has a validation method
- [ ] Open questions are genuinely unresolved (not things you already know the answer to)
- [ ] A non-technical stakeholder could read this and understand what's being built and why
- [ ] No jargon that hasn't been defined

---

## Pairs With

- `churney-os` — run first to validate the riskiest assumption and classify reversibility before writing the PRD
- `pm-user-stories` — break P0/P1 features into sprint-ready stories after PRD is approved
- `pm-job-stories` — use for JTBD-style backlog items when focusing on context over role
- `pm-prioritization` — use to decide P0/P1/P2 assignment before finalizing Section 7
