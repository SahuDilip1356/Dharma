---
name: pm-prioritization
description: |
  Reference guide to 9 prioritization frameworks with formulas, when-to-use guidance, and
  decision logic. Triggers when:
  - Deciding which features belong in P0/P1/P2 for a PRD
  - Choosing between competing initiatives or roadmap items
  - User says "how should we prioritize", "which framework should I use", "RICE vs ICE"
  - Comparing opportunities or features before committing to a sprint or roadmap
  - Need to justify prioritization decisions to stakeholders

  Core principle: Prioritize problems (opportunities), not features.
  Recommended default: Opportunity Score for customer problems, ICE for ideas/initiatives.

license: MIT
metadata:
  author: Dilip Sahu
  source: https://github.com/SahuDilip1356/pm-skills
  version: "1.0.0"
---

# PM Skill: Prioritization Frameworks

**Core principle: Never allow customers to design solutions. Prioritize problems (opportunities), not features.**

---

## How to Choose a Framework

| Situation | Use |
|-----------|-----|
| Prioritizing customer problems from research | Opportunity Score |
| Quick triage of ideas or initiatives | ICE |
| Larger team needing more granularity | RICE |
| Sorting feature requirements for a sprint | MoSCoW |
| Choosing between major strategic bets | Weighted Decision Matrix |
| Understanding which features users expect vs. delight them | Kano Model |
| Managing your own PM task queue | Eisenhower Matrix |

---

## The Recommended Frameworks

### Opportunity Score (Dan Olsen — *The Lean Product Playbook*)
**Best for:** Prioritizing customer problems from discovery research.

Survey customers on **Importance** (1–10) and **Satisfaction** (1–10) for each need. Normalize to 0–1.

```
Opportunity Score = Importance × (1 − Satisfaction)
```

High Importance + Low Satisfaction = highest opportunity. Plot on an Importance vs. Satisfaction chart — upper-left quadrant is the sweet spot.

**Why it wins:** Forces you to prioritize underserved problems, not just what's loudly requested.

---

### ICE Score
**Best for:** Quick prioritization of ideas, initiatives, and backlog items.

```
ICE Score = Impact × Confidence × Ease
```

| Factor | What it measures | Scale |
|--------|-----------------|-------|
| Impact | Opportunity Score × number of customers affected | Numeric |
| Confidence | How confident are we this will work? | 1–10 |
| Ease | How easy to implement? | 1–10 |

Higher score = prioritize first. Simple to run in a meeting.

---

### RICE Score
**Best for:** Teams needing more precision than ICE; larger backlogs.

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

| Factor | Definition |
|--------|-----------|
| Reach | Number of customers affected per period |
| Impact | Opportunity Score per customer (0–1 scale) |
| Confidence | How confident? (0–100%) |
| Effort | Person-months to implement |

**RICE vs ICE:** RICE splits Impact into Reach + Impact per customer. Use RICE when scale of customer reach differs significantly between options.

---

### MoSCoW
**Best for:** Sorting requirements within a defined scope (sprint, release).

| Tier | Meaning |
|------|---------|
| **Must-have** | P0 — launch fails without it |
| **Should-have** | P1 — high value, not blocking |
| **Could-have** | P2 — nice-to-have if time allows |
| **Won't-have** | Explicitly out of scope for this version |

**Caution:** MoSCoW is from project management, not product management. It describes priority within a fixed scope, not which problems to solve. Combine with Opportunity Score to pick what goes into scope first.

---

## All 9 Frameworks at a Glance

| Framework | Best For | Key Formula / Logic |
|-----------|----------|-------------------|
| Eisenhower Matrix | PM's personal task triage | Urgent vs. Important 2×2 |
| Impact vs. Effort | Quick team triage | Simple 2×2 — not rigorous for strategy |
| Risk vs. Reward | Initiatives with uncertainty | Like Impact/Effort + accounts for risk |
| **Opportunity Score** | Customer problems ← recommended | Importance × (1 − Satisfaction) |
| Kano Model | Understanding feature expectations | Must-be / Performance / Attractive / Indifferent |
| Weighted Decision Matrix | Multi-criteria strategic bets | Weight each criterion, score each option |
| **ICE** | Ideas and initiatives ← recommended | Impact × Confidence × Ease |
| **RICE** | Ideas at scale ← recommended for larger teams | (Reach × Impact × Confidence) / Effort |
| MoSCoW | Sprint/release scoping | Must / Should / Could / Won't |

---

## Applying to a PRD (P0/P1/P2 Assignment)

When filling out Section 7 of a PRD:

1. Run **Opportunity Score** on the customer problems first — this sets which problems deserve features at all
2. For each problem that scores high, list potential features
3. Score features with **ICE** or **RICE** to rank them
4. Map to P0/P1/P2:
   - P0 = top ICE/RICE scorers that directly address the highest-Opportunity-Score problems
   - P1 = next tier — high value but not blocking launch
   - P2 = good ideas that can wait for v2

---

## Pairs With

- `pm-prd` — use to assign P0/P1/P2 in Section 7 before finalizing the PRD
- `churney-os` — the Constraint Check (Phase 2) uses this to validate scope decisions
- `pm-user-stories` — prioritization determines which stories go into the current sprint
