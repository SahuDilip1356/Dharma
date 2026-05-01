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
| 3 | `aesthetic-code-gen` | `frontend-design` | ✅ Mandatory (user-facing UI) — runs first in Phase 3 |
| 3 | `react-performance` | `react-best-practices` | ✅ Mandatory (React/Next.js) — runs after frontend-design |
| 3 | `react-patterns` | `uiux-react-patterns` | ✅ Mandatory (user-facing) — runs after frontend-design |
| 3 | `ai-safety-eval` | `ai-safety-eval` | ✅ If AI/LLM component present |
| 3 | `prompt-optimization` | `prompt-optimization` | ✅ If AI/LLM component present |
| 4 | `accessibility-review` | `uiux-accessibility-review` | ✅ Mandatory |
| 4 | `responsive-design-review` | `uiux-responsive-review` | ✅ Mandatory |
| 4 | `webapp-testing` | `webapp-testing` | ✅ Mandatory (user-facing) |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `design-qa` | `uiux-design-qa` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |
| 5 | `ai-observability` | `ai-observability` | ✅ If AI/LLM component present |

**Optional:** `interaction-design-review`, `content-ux-review`, `prioritization`

**Required Evidence:**
- Problem + user + goal (churney-os output)
- UX flow + visual direction (uiux-designer + uiux-design-intelligence output)
- Design system tokens (uiux-frontend-design-system output)
- Aesthetic direction statement (frontend-design output — style, palette, distinctive choice, anti-patterns rejected)
- Implementation plan
- Inference economics summary (if AI/LLM component present)
- Passing tests (superpowers-tdd)
- AI safety evaluation report (if AI/LLM component present)
- Browser verification screenshots + console log (webapp-testing)
- Observability checklist complete (if AI/LLM component present)
- Accessibility audit findings
- Responsive behavior verified
- Screenshots (design-qa — validates against aesthetic direction statement)
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
| 3 | `aesthetic-code-gen` | `frontend-design` | ✅ If user-facing — runs first in Phase 3 |
| 3 | `react-performance` | `react-best-practices` | ✅ If React/Next.js UI — runs after frontend-design |
| 3 | `react-patterns` | `uiux-react-patterns` | ✅ If user-facing — runs after frontend-design |
| 3 | `ai-safety-eval` | `ai-safety-eval` | ✅ If AI/LLM component present |
| 3 | `prompt-optimization` | `prompt-optimization` | ✅ If AI/LLM component present |
| 4 | `webapp-testing` | `webapp-testing` | ✅ If user-facing |
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
- Browser verification screenshots + console log (webapp-testing, if user-facing)
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
| 4 | `webapp-testing` | `webapp-testing` | ✅ If bug is UI/browser-visible |
| 4 | `execution-verify` | `superpowers-verify` | ✅ Mandatory |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Optional:** `accessibility-review` if bug is UI/a11y related

**Required Evidence:**
- Reproduction steps
- Root cause statement
- Failing test (written before fix)
- Fix applied
- Regression test passing
- Browser before/after screenshots (webapp-testing, if UI bug)
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
| 3 | `tdd` | `superpowers-tdd` | ✅ Mandatory |
| 3 | `execution-subagents` | `superpowers-execute` | ✅ Mandatory |
| 3 | `aesthetic-code-gen` | `frontend-design` | ✅ Mandatory — runs first in Phase 3; consumes Phase 1 design brief |
| 3 | `react-performance` | `react-best-practices` | ✅ Mandatory — runs after frontend-design |
| 3 | `react-patterns` | `uiux-react-patterns` | ✅ Mandatory — runs after frontend-design |
| 4 | `accessibility-review` | `uiux-accessibility-review` | ✅ Mandatory |
| 4 | `responsive-design-review` | `uiux-responsive-review` | ✅ Mandatory |
| 4 | `webapp-testing` | `webapp-testing` | ✅ Mandatory |
| 5 | `design-qa` | `uiux-design-qa` | ✅ Mandatory — validates against aesthetic direction statement from frontend-design |
| 5 | `branch-finish` | `superpowers-finish` | ✅ Mandatory |

**Required Evidence:**
- User goal statement
- UX flow or screen structure
- Visual direction (style + colors + fonts from uiux-design-intelligence)
- Aesthetic direction statement (from frontend-design — style name, palette, distinctive choice, anti-patterns rejected)
- 4-state coverage: loading / empty / error / success
- Accessibility audit findings
- Responsive behavior verified at 375/768/1280/1440px
- Browser state verification screenshots (webapp-testing)
- Screenshot review (design-qa output — validates against aesthetic direction statement)

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
| 3 | `react-performance` | `react-best-practices` | ✅ If frontend (CRITICAL — primary skill for React perf) |
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
