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
| `aesthetic-code-gen` | `frontend-design` | ✅ Installed | Phase 3 — aesthetic UI code generation; runs first in Phase 3 chain, consumes Phase 1 design brief + tokens; anti-AI-slop intentionality |

---

---

## Testing Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `webapp-testing` | `webapp-testing` | ✅ Installed | Phase 4 browser verification — Playwright (Python); multi-agent subagent for UI flows |

---

## Developer Experience Layer

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `react-performance` | `react-best-practices` | ✅ Installed | Phase 3 — 70 performance rules (waterfalls, bundle, re-renders, JS efficiency); complements `uiux-react-patterns` |
| `skill-gap-resolver` | `find-skills` | ✅ Installed | Pre-Phase 0 — searches skills.sh ecosystem when no installed Dharma skill covers a domain; meta-orchestrator tool |

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

## Memory & Context Layer (Layer 0)

Cross-cutting — runs before and after every Dharma skill invocation. Not routed to directly.

| Functional Name | Actual Skill | Status | Notes |
|----------------|-------------|--------|-------|
| `memory-layer` | `memory-layer` | ✅ Installed | Pre/post-flight wrapper — loads global + project memory before skills; writes decisions/learnings after. Owns semantic memory (global + project). |
| `episodic-memory` | `episodic-memory` | ✅ Installed | Captures session digests into `[project]/memory/episodic/`. Owns episodic memory — past prompts, drafts, outputs, open threads. Runs post-flight before memory-layer. |
| `dharma-resume` | `dharma-resume` | ✅ Installed | Session continuity — reads STATE.md + recent episodic digests; outputs Resume Brief; routes back into orchestrator at the right phase. Triggers on "resume", "continue", "where were we". |

**Three memory types covered:**
- Semantic (long-term): `memory-layer` (global + project-level facts)
- Episodic (interaction history): `episodic-memory` (session digests)
- Working (immediate): `dharma-resume` + `STATE.md` + Phase 0 evidence

See `00-lifecycle-orchestrator/agent-architecture.md` for the full mapping to canonical agent architecture.

---

## External Runtime Plugins (Layer 0+, Optional Candidates)

External plugins/runtimes that operate beneath skills. Distinct from Layer 0 (Memory) — these are **external**, **optional**, and **project-scoped by default**. Not invoked directly; they modify how tools behave when present.

| Functional Name | Plugin / Source | Status | Notes |
|----------------|----------------|--------|-------|
| `context-compression` | `mksglu/context-mode` v1.0.107 (Elastic-2.0) | 🟡 Candidate (project-scoped, sandbox only) | MCP server installed at `~/sandboxes/context-mode-test/` without hooks. Tools available but NOT auto-redirected — `WebFetch` still bypasses Context Mode. Decision log: `decisions.md` [2026-05-04]. |

---

## Candidate Skills (Under Evaluation)

Skills created on demand via `skill-creator` (Step 0.5 Tier 2 fallback). Each starts here until promoted to its target layer.

| Skill | Created | Source brief | Eval status | Promotion target layer |
|---|---|---|---|---|
| _(none yet)_ | — | — | — | — |

### Lifecycle of a candidate skill
1. **Created** by `anthropic-skills:skill-creator` after find-skills returned nothing AND user approved building
2. **Saved** to this section with creation date and the gap brief
3. **Evaluated** per skill-creator's eval framework (≥80% pass rate target)
4. **Validated** in 3+ real Dharma tasks (no incorrect outputs)
5. **Annotated** with KPIs (per `skill-kpis.md`) + tool access (per `tool-access-matrix.md`) + ownership boundaries (per `ownership-boundaries.md`)
6. **Promoted** to its target layer when all five conditions hold

### What flags a candidate skill in evidence
While in Candidate status, any output produced by the skill is flagged in the evidence ledger as `[candidate skill output — verify carefully]`. Lead Agent (G8) Final Evaluation must explicitly review candidate-skill outputs before passing the verdict.

### Demotion / removal
A candidate skill is removed if:
- Eval pass rate stays below 80% after 2+ revision rounds
- Produces incorrect output in 2+ real tasks
- Better-fit installed or external skill is found via `find-skills` after creation
- User explicitly removes (e.g., "this skill isn't pulling its weight")

### Promotion criteria (Candidate → Installed)
Move from "Candidate" to "Installed" only when ALL true:
- Run in 3+ real Dharma projects without breaking existing skills
- Measurable context reduction in real workloads (not synthetic tests)
- Hook deployment question resolved (project-scoped MCP install does NOT auto-redirect tools — would require global plugin install which has higher trust surface)

### Demotion / removal triggers
- Plugin upgrade introduces breaking changes to MCP protocol
- Maintainer becomes unresponsive (>60 days no activity)
- Security advisory published

---

## Phase 5 — Release Review Gates

Slash commands invoked at release time. Not skills — gates that produce evidence.

| Functional Name | Command | Status | When to invoke |
|----------------|---------|--------|---------------|
| `code-review-gate` (G6) | `/review` | ✅ Installed (`code-review` plugin, Anthropic official) | Every meaningful change before merge — bugs, edge cases, code quality |
| `high-risk-review-gate` (G6.5) | `/ultrareview` | ✅ Installed (Claude Code built-in) | High-stakes changes only: auth, payments, data migration, security, AI safety, production infra. Cloud-based parallel multi-agent deep review. |

### When G6.5 (`/ultrareview`) is mandatory
| Trigger | Reason |
|---------|--------|
| Auth/RBAC changes | Privilege escalation risk |
| Payment flow changes | Financial / regulatory risk |
| Database migrations | Data loss / corruption risk |
| Security-sensitive code | Vulnerability surface |
| AI safety changes | Compliance / harm risk |
| Production infrastructure | Outage risk |
| Compliance-critical paths (DPDPA, GDPR, etc.) | Legal exposure |

### Routing rule
- All PRs run G6 (`/review`) by default
- If `Risk level: high | critical` from Step 0 classification → ALSO run G6.5 (`/ultrareview`)
- G6 failures block merge until resolved
- G6.5 critical findings halt the release entirely; resolve and rerun

---

## Skill Count Summary

| Layer | Installed | Planned / Candidate |
|-------|-----------|---------------------|
| Memory & Context (Layer 0) | 3 | 0 |
| External Runtime Plugins (Layer 0+) | 0 | 1 candidate (context-mode) |
| Product & Planning | 5 | 0 |
| Engineering Discipline | 4 | 0 |
| Execution Methodology | 8 | 0 |
| Experience Quality | 11 | 0 |
| Testing | 1 | 0 |
| AI & Economics | 6 | 0 |
| Developer Experience | 2 | 0 |
| Phase 5 Release Gates | 2 | 0 |
| **Total** | **42** | **1 candidate** |

---

## Skill Location

All skills at: `/Users/sahudilip/Desktop/Product Dev/.claude/skills/`

Available globally across all sub-projects under Product Dev.
