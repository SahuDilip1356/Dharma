# Routing Matrix

Maps work type to required skill sequence, optional skills, and evidence.
Functional names used here — resolve to actual skills via `skills-inventory.md`.

---

## Route A: New Product

**Trigger:** New product, MVP, startup idea, major module from scratch.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `product-planning-gate` | `churney-os` | ✅ Mandatory |
| 1 | `uiux-product-designer` | `uiux-designer` | ✅ Mandatory |
| 1 | `design-intelligence` | `uiux-design-intelligence` | ✅ Mandatory |
| 1 | `frontend-design-system` | `uiux-frontend-design-system` | ✅ Mandatory |
| 2 | `engineering-discipline` | `karpathy-discipline` | ✅ Mandatory |
| 2 | `implementation-plan` | `superpowers-write-plan` | ✅ Mandatory |
| 2 | `inference-economics` | `inference-economics` | ✅ If AI/LLM component present |
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory |
| 3 | `execution-subagents` | `superpowers-execute` | ✅ Mandatory |
| 3 | `ai-safety-eval` | `ai-safety-eval` | ✅ If AI/LLM component present |
| 3 | `prompt-optimization` | `prompt-optimization` | ✅ If AI/LLM component present |
| 4 | `accessibility-review` | `uiux-accessibility-review` | ✅ Mandatory |
| 4 | `responsive-design-review` | `uiux-responsive-review` | ✅ Mandatory |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `design-qa` | `uiux-design-qa` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |
| 5 | `ai-observability` | `ai-observability` | ✅ If AI/LLM component present |

**Optional:** `interaction-design-review`, `content-ux-review`, `prioritization`

**Required Evidence:**
- Problem + user + goal (churney-os output)
- UX flow + visual direction
- Design system tokens
- Implementation plan
- Inference economics summary (if AI/LLM component present)
- Passing tests
- AI safety evaluation report (if AI/LLM component present)
- Observability checklist complete (if AI/LLM component present)
- Accessibility audit findings
- Responsive behavior verified
- Screenshots (design-qa)
- PR/commit summary

---

## Route B: New Feature

**Trigger:** Adding a capability to an existing product.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `goal-driven-execution` | `goal-driven-execution` | ✅ Mandatory |
| 0 | `think-before-coding` | `think-before-coding` | ✅ Mandatory |
| 1 | `uiux-product-designer` | `uiux-designer` | ✅ If user-facing |
| 1 | `frontend-design-system` | `uiux-frontend-design-system` | ✅ If new components |
| 2 | `implementation-plan` | `superpowers-write-plan` | ✅ Mandatory |
| 2 | `simplicity-first` | `simplicity-first` | ✅ Mandatory |
| 2 | `inference-economics` | `inference-economics` | ✅ If AI/LLM component present |
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory |
| 3 | `execution-subagents` | `superpowers-execute` | ✅ Mandatory |
| 3 | `ai-safety-eval` | `ai-safety-eval` | ✅ If AI/LLM component present |
| 3 | `prompt-optimization` | `prompt-optimization` | ✅ If AI/LLM component present |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 4 | `design-qa` | `uiux-design-qa` | ✅ If user-facing |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |
| 5 | `ai-observability` | `ai-observability` | ✅ If AI/LLM component present |

**Optional:** `accessibility-review`, `responsive-design-review`

**Required Evidence:**
- Feature goal + acceptance criteria
- Assumptions listed
- Implementation plan
- Inference economics summary (if AI/LLM component present)
- Tests passing
- AI safety evaluation report (if AI/LLM component present)
- Observability checklist complete (if AI/LLM component present)
- UI screenshots if user-facing
- PR/commit summary

---

## Route C: Bug Fix

**Trigger:** Something is broken and root cause is suspected.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `root-cause-debug` | `superpowers-debug` | ✅ Mandatory |
| 0 | `think-before-coding` | `think-before-coding` | ✅ Mandatory |
| 3 | `surgical-changes` | `surgical-changes` | ✅ Mandatory |
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Optional:** `accessibility-review` if bug is UI/a11y related

**Required Evidence:**
- Reproduction steps
- Root cause statement
- Failing test (written before fix)
- Fix applied
- Regression test passing
- Full suite passing

---

## Route D: UI/UX Design or Redesign

**Trigger:** Improving screens, flows, layout, visual quality, accessibility, usability.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 1 | `uiux-product-designer` | `uiux-designer` | ✅ Mandatory |
| 1 | `design-intelligence` | `uiux-design-intelligence` | ✅ Mandatory |
| 1 | `frontend-design-system` | `uiux-frontend-design-system` | ✅ Mandatory |
| 1 | `content-ux-review` | `uiux-audit` | ✅ Mandatory |
| 1 | `interaction-design-review` | `uiux-interaction-review` | ✅ Mandatory |
| 4 | `accessibility-review` | `uiux-accessibility-review` | ✅ Mandatory |
| 4 | `responsive-design-review` | `uiux-responsive-review` | ✅ Mandatory |
| 5 | `design-qa` | `uiux-design-qa` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Optional:** `react-patterns` for implementation quality

**Required Evidence:**
- User goal statement
- UX flow or screen structure
- Visual direction (style + colors + fonts)
- Component structure
- Accessibility audit findings
- Responsive behavior verified at 375/768/1280/1440px
- Screenshot review (design-qa output)

---

## Route E: Refactor

**Trigger:** Improving structure or quality without changing behavior.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `engineering-discipline` | `karpathy-discipline` | ✅ Mandatory |
| 0 | `think-before-coding` | `think-before-coding` | ✅ Mandatory |
| 2 | `simplicity-first` | `simplicity-first` | ✅ Mandatory |
| 3 | `surgical-changes` | `surgical-changes` | ✅ Mandatory |
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory (behavior preservation) |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Required Evidence:**
- Refactor purpose and non-goals
- Tests passing before refactor starts
- Same tests passing after refactor
- Minimal changed files (diff scope)
- No behavior change confirmed

---

## Route F: Performance

**Trigger:** Speed, bundle size, rendering, database query, latency, or resource optimization.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `goal-driven-execution` | `goal-driven-execution` | ✅ Mandatory |
| 0 | `root-cause-debug` | `superpowers-debug` | ✅ Mandatory |
| 0 | `think-before-coding` | `think-before-coding` | ✅ Mandatory |
| 3 | `surgical-changes` | `surgical-changes` | ✅ Mandatory |
| 3 | `react-patterns` | `uiux-react-patterns` | ✅ If frontend |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Required Evidence:**
- Baseline metric (before)
- Bottleneck identified (root cause)
- Change made
- After metric (same measurement method)
- Risk assessment

---

## Route G: Security / Compliance

**Trigger:** Auth, permissions, secrets, privacy, audit logs, payments, regulated data.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 0 | `goal-driven-execution` | `goal-driven-execution` | ✅ Mandatory |
| 0 | `think-before-coding` | `think-before-coding` | ✅ Mandatory |
| 2 | `engineering-discipline` | `karpathy-discipline` | ✅ Mandatory |
| 3 | `surgical-changes` | `surgical-changes` | ✅ Mandatory |
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Required Evidence:**
- Threat / risk statement
- Data touched (what, who can access it)
- Permission model confirmed
- Tests covering auth paths
- Rollback notes
- Review requirement flagged

---

## Route H: Release

**Trigger:** PR preparation, merge, deployment, or cleanup.

| Phase | Skill (Functional) | Actual Skill | Required? |
|-------|-------------------|-------------|-----------|
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `design-qa` | `uiux-design-qa` | ✅ If user-facing |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Required Evidence:**
- All tests run + passing
- Known risks stated
- Files changed summary
- Deployment / rollback notes
- Final status

---

## UX Mandatory Rule

For any route where `User impact = user-facing` or `revenue-critical`:

Phase 1 UX Gate is **non-negotiable**. No user-facing feature advances past Phase 1 without:
- UX intent defined
- Accessibility concerns identified
- Responsive behavior planned
- States designed (empty / loading / error / success)
