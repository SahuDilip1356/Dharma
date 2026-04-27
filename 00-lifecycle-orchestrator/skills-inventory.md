# Skills Inventory

Maps functional names used in the orchestrator to actual installed skill files.
Update this file when skills are added, renamed, or replaced — never update routing-matrix.md for name changes.

---

## Product & Planning Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `product-planning-gate` | `churney-os` | ✅ Installed | Phase 0–5 founder framework |
| `product-requirements` | `pm-prd` | ✅ Installed | 8-section PRD |
| `acceptance-criteria` | `pm-user-stories` / `pm-job-stories` | ✅ Installed | Role-based or JTBD stories |
| `prioritization` | `pm-prioritization` | ✅ Installed | Opportunity Score, ICE, RICE |
| `goal-driven-execution` | `goal-driven-execution` | ✅ Installed | Success criteria + verify loop |

---

## Engineering Discipline Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `engineering-discipline` | `karpathy-discipline` | ✅ Installed | Master of all 4 Karpathy principles |
| `think-before-coding` | `think-before-coding` | ✅ Installed | Surface assumptions first |
| `simplicity-first` | `simplicity-first` | ✅ Installed | Minimum viable code |
| `surgical-changes` | `surgical-changes` | ✅ Installed | Touch only what's required |

---

## Execution Methodology Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `execution-methodology` | `superpowers` | ✅ Installed | Master 6-phase execution |
| `design-before-code` | `superpowers-brainstorm` | ✅ Installed | Design gate |
| `implementation-plan` | `superpowers-write-plan` | ✅ Installed | Bite-sized plan |
| `tdd` | `superpowers-tdd` | ✅ Installed | RED-GREEN-REFACTOR |
| `execution-subagents` | `superpowers-execute` | ✅ Installed | Subagent-driven execution |
| `root-cause-debug` | `superpowers-debug` | ✅ Installed | Debug before fix |
| `execution-verify` | `superpowers-verify` | ✅ Installed | Evidence before done |
| `branch-finish` | `superpowers-finish` | ✅ Installed | Tests → merge/PR/discard |

---

## Experience Quality Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `uiux-product-designer` | `uiux-designer` | ✅ Installed | Design process + output format |
| `design-intelligence` | `uiux-design-intelligence` | ✅ Installed | Style / color / font selection |
| `frontend-design-system` | `uiux-frontend-design-system` | ✅ Installed | Tokens, components, layout |
| `accessibility-review` | `uiux-accessibility-review` | ✅ Installed | WCAG, keyboard, contrast |
| `responsive-design-review` | `uiux-responsive-review` | ✅ Installed | Mobile/tablet/desktop |
| `interaction-design-review` | `uiux-interaction-review` | ✅ Installed | States, transitions, feedback |
| `content-ux-review` | `uiux-audit` | ✅ Installed | Labels, errors, copy (via audit) |
| `design-qa` | `uiux-design-qa` | ✅ Installed | Final visual QA |
| `ui-audit` | `uiux-audit` | ✅ Installed | Vercel guidelines compliance |
| `react-patterns` | `uiux-react-patterns` | ✅ Installed | React/Next.js best practices |

---

---

## AI & Economics Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `ai-safety-eval` | `ai-safety-eval` | ✅ Installed | Mandatory Phase 3 gate for any AI/LLM feature |
| `inference-economics` | `inference-economics` | ✅ Installed | Phase 2 — model selection, token budget, cost ceiling |
| `ai-observability` | `ai-observability` | ✅ Installed | Post-ship monitoring — 5-layer stack; set up before go-live |
| `prompt-optimization` | `prompt-optimization` | ✅ Installed | Prompt versioning, token efficiency, consistency testing |
| `model-governance` | `model-governance` | ✅ Installed | Model registry, deprecation, audit trails — activate at 2+ AI features |
| `benchmark-framework` | `benchmark-framework` | ✅ Installed | Quality regression tracking — activate at 3+ AI features |

---

## Governance Files (Orchestrator Meta-Controls)

These are not skills — they are conductor-level controls for the orchestrator itself.

| File | Purpose |
|------|---------|
| `routing-decision-tree.md` | 7-step classification before route selection — run before every task |
| `ownership-boundaries.md` | Scope limits per skill — prevents overlap and scope creep |
| `evidence-ledger-template.md` | Structured receipt for task classification + gate status + evidence |
| `examples/` | Golden reference scenarios — classification, route, skills, evidence required |

---

## Skill Count Summary

| Layer | Installed | Planned |
|-------|-----------|---------|
| Product & Planning | 5 | 0 |
| Engineering Discipline | 4 | 0 |
| Execution Methodology | 8 | 0 |
| Experience Quality | 10 | 0 |
| AI & Economics | 6 | 0 |
| **Total** | **33** | **0** |

---

## Skill Location

All skills at: `/Users/sahudilip/Desktop/Product Dev/.claude/skills/`

Available globally across all sub-projects under Product Dev.
