# Ownership Boundaries

Each skill has one primary responsibility. Skills must not expand outside their boundary.
When a skill discovers something outside its scope, it must report it as a blocker, risk,
follow-up recommendation, or out-of-scope flag — not absorb it and act.

---

## Anti-Overlap Rule

If you are operating as a specialist skill and discover an issue outside your boundary:

| Discovery Type | What to do |
|---|---|
| **Blocker** — the out-of-scope issue prevents you from completing your task | Stop. Report the blocker and the specific skill that owns it. Do not proceed until resolved. |
| **Risk** — the issue could cause harm if ignored but doesn't block you | Flag it with a risk label. Complete your scope. Let the orchestrator decide if the risk skill should be invoked. |
| **Follow-up** — something worth fixing in a separate task | Note it as a follow-up recommendation. Do not fix it in-scope. |
| **Out-of-scope observation** — interesting but not actionable in this task | Mention it briefly. Do not act on it. |

Do NOT re-plan the whole lifecycle from inside a specialist skill.
Do NOT invoke other skills unless the orchestrator has explicitly delegated that authority.

---

## Routing Rule

When multiple skills could apply, use the most specific one available:

| Instead of | Use when |
|---|---|
| `uiux-audit` | `uiux-accessibility-review` (for keyboard navigation, contrast, screen reader) |
| `uiux-audit` | `uiux-interaction-review` (for states, transitions, feedback loops) |
| `uiux-audit` | `uiux-responsive-review` (for breakpoint behavior) |
| `superpowers` (master) | The specific sub-skill that matches the phase |
| `karpathy-discipline` | `simplicity-first` or `surgical-changes` for targeted single-principle work |

Use the general skill only when no specific skill covers the need.

---

## Skill Ownership Table

### Product & Planning Layer

| Skill | Owns | Does NOT Own |
|---|---|---|
| `churney-os` | Product vision, problem-solution fit, go-to-market framing, founder-level decisions | Engineering approach, UI layout, implementation details |
| `goal-driven-execution` | Feature goal, success criteria, scope boundaries, verify loop | Design process, code implementation, test writing |
| `pm-prd` | Product requirements document structure and completeness | Competitive analysis (unless asked), engineering estimates |
| `pm-user-stories` / `pm-job-stories` | Acceptance criteria, story format | Implementation plan, technical approach |
| `pm-prioritization` | ICE/RICE scoring, opportunity ranking | Resource allocation decisions, tech debt triage |

---

### Engineering Discipline Layer

| Skill | Owns | Does NOT Own |
|---|---|---|
| `karpathy-discipline` | Applying all 4 Karpathy principles: avoid complexity, avoid dependencies, start simple, write tests | UX decisions, design system, product scope, prioritization |
| `think-before-coding` | Surfacing assumptions, listing unknowns, stating constraints before writing code | Writing the code, designing the UI, planning the product |
| `simplicity-first` | Minimum viable implementation, removing unnecessary abstractions | Feature scope decisions, test strategy, design quality |
| `surgical-changes` | Minimal file/function blast radius per change | Architectural decisions, test coverage, design review |

---

### Execution Methodology Layer

| Skill | Owns | Does NOT Own |
|---|---|---|
| `superpowers` (master) | Phase sequencing, methodology orchestration | Re-classifying work type (that belongs to lifecycle-orchestrator) |
| `superpowers-brainstorm` | Design alternatives before implementation | Final design decisions, engineering approach |
| `superpowers-write-plan` | Implementation plan, task breakdown, file manifest | Prioritization across features, product roadmap |
| `superpowers-tdd` | RED-GREEN-REFACTOR cycle, test-first discipline | Test strategy choices (unit vs. integration — that's engineering discipline) |
| `superpowers-execute` | Subagent delegation, parallel execution | Overriding the plan, changing scope mid-execution |
| `superpowers-debug` | Root cause investigation, reproduction, hypothesis | Writing the fix (that's surgical-changes after debug) |
| `superpowers-verify` | Verification evidence, running the proof | Choosing what to build, code review |
| `superpowers-finish` | Commit, PR, merge, cleanup | Deployment decisions, rollback execution |

---

### Experience Quality Layer

| Skill | Owns | Does NOT Own |
|---|---|---|
| `uiux-designer` | UX intent, user flows, states (empty/loading/error/success), design process | Final visual direction (that's uiux-design-intelligence), code implementation |
| `uiux-design-intelligence` | Style guide, color palette, typography, visual direction | UX flow, interaction patterns, layout structure |
| `uiux-frontend-design-system` | Design tokens, component inventory, layout system | Feature-level UX decisions, accessibility audit |
| `uiux-accessibility-review` | WCAG compliance, keyboard navigation, screen reader, contrast | Responsive layout, visual style, component architecture |
| `uiux-responsive-review` | Mobile/tablet/desktop breakpoint behavior (375/768/1280/1440px) | Accessibility compliance, visual style, interaction design |
| `uiux-interaction-review` | State transitions, hover/focus/active states, feedback loops, motion | Accessibility, responsive, visual direction |
| `uiux-audit` | Vercel guidelines compliance, labels, errors, copy quality | Deep a11y audit, responsive QA, interaction design |
| `uiux-design-qa` | Final visual QA, screenshot review, design-to-implementation fidelity | Code correctness, test coverage, product scope |
| `uiux-react-patterns` | React/Next.js component patterns, performance patterns in UI | Product design, accessibility, responsive layout |

---

### AI & Economics Layer

| Skill | Owns | Does NOT Own |
|---|---|---|
| `ai-safety-eval` | Risk profiling, adversarial testing, hallucination detection (pre-ship gate), bias audit, cost/latency validation (Phase 3 gate), quality spot-check | Model selection, prompt engineering, post-ship monitoring, regression tracking |
| `inference-economics` | Model selection, token budget design, cost ceiling definition, cost-per-feature calculation, cache strategy — Phase 2 (planning) only | Cost/latency validation against constraints (that is ai-safety-eval Step 6); post-ship cost monitoring (that is ai-observability) |
| `prompt-optimization` | Prompt versioning, token reduction, consistency testing, prompt regression testing, prompt change management | Safety thresholds, quality gates (that is ai-safety-eval); post-ship prompt monitoring (that is ai-observability) |
| `model-governance` | Model versioning, deprecation handling, audit trails for model decisions, model change management, rollback procedures | Safety evaluation (that is ai-safety-eval); cost analysis (that is inference-economics) |
| `ai-observability` | Post-ship monitoring — latency, error rate, hallucination drift, token cost, user satisfaction signals, alerting thresholds, incident response | Pre-ship testing and gates (that is ai-safety-eval); pre-ship quality spot-check (that is ai-safety-eval Step 7) |
| `benchmark-framework` | Scheduled quality regression tracking, drift detection over time, benchmark suite design, post-ship hallucination rate trending | Pre-ship hallucination gate (that is ai-safety-eval Step 4); one-time spot checks (that is ai-safety-eval Step 7) |

---

## What "Reporting Out-of-Scope" Looks Like

```
⚠️ Out-of-Scope Observation (from uiux-accessibility-review)

While auditing keyboard navigation, I noticed the color contrast on the error state
fails WCAG AA (3.2:1 ratio vs. required 4.5:1). This is within my scope and flagged
as a violation in the accessibility report.

I also noticed the mobile layout breaks at 320px width. This is NOT within my scope.
→ Flagged as a follow-up recommendation for uiux-responsive-review.

I also noticed a potential SQL injection vector in the search parameter. This is NOT
within my scope.
→ Flagged as a blocker — do not ship until reviewed by security (Route G).
```

The specialist completes its own scope, reports the out-of-scope finding with a clear label, and returns control to the orchestrator.
