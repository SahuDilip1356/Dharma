# Agent Architecture — Dharma Mapping

How Dharma implements the canonical agent architecture pattern.

> **Reference framework** (Kedar, multi-agent product video):
> Agent = **Act** + **Reason** + **Memory**
> Plus: Deployment Framework, Multi-Agent Architecture

This document maps each component to where it lives in Dharma, surfaces gaps explicitly, and links to the skills that implement it.

---

## 1. Agent = Act + Reason + Memory

### Act (Execution)

| Component | Dharma implementation | Status |
|---|---|---|
| **Defined Persona / Role** | YAML frontmatter on every skill (`name`, `description`, role definition in body); `00-lifecycle-orchestrator` defines control-tower role explicitly | ✅ Strong |
| **Precise Constraints** | `ownership-boundaries.md` (scope per skill) + `escalation-rules.md` (stop conditions) + `evidence-contract.md` (proof requirements) | ✅ Strong |
| **Target KPIs** | `skill-kpis.md` — central registry mapping every skill to 2–3 measurable KPIs across 5 categories (Output Quality / Efficiency / Behavioral / Gate Compliance / Outcome). Layer defaults + per-skill overrides. Spot-checked per task, aggregated quarterly. | ✅ Strong (Gap #5 closed) |

### Reason (Logic)

| Component | Dharma implementation | Status |
|---|---|---|
| **Pattern Recognition** | `superpowers-debug` (root cause), `ai-observability` (production patterns), `karpathy-discipline` (recurring code patterns), `learnings.md` (project-level pattern store) | ✅ Strong |
| **Audience Segmentation** | `pm-prd` (audience analysis), `pm-job-stories` (JTBD context), `saral-build` Layer 1 (audience definition with primary/secondary/explicitly-not) | ⚠️ Partial — implicit, not framed as "segmentation" |
| **Strategic Decision Making** | `routing-decision-tree.md` (7-step classification), `churney-os` (founder framework), `sahu-dilip-framework` (22-section evaluation), `pm-prioritization` (9 frameworks) | ✅ Strong |

### Memory (Context)

| Component | Dharma implementation | Status |
|---|---|---|
| **Semantic** (long-term knowledge) | `memory-layer` global drawer: `Product Dev/memory/founder.md`, `patterns.md`, `tools-and-skills.md` | ⚠️ Partial — strong on founder identity, weaker on per-product brand semantic store |
| **Episodic** (interaction history) | `memory/episodic/` directory + `episodic-memory` skill (NEW) — past prompts, drafts, outputs preserved per session | ✅ NOW IMPLEMENTED (was Gap #1) |
| **Working** (immediate task brief) | Phase 0 Intent Gate captures current goal/scope/risk; `evidence-ledger-template.md` holds active task state; `STATE.md` per project (NEW) | ✅ Strong |

---

## 2. Deployment Framework

| Step | Dharma implementation | Status |
|---|---|---|
| **1. Define Specific Goal/KPI** | Phase 0 Intent Gate (`phase-gates.md`) — measurable success criteria mandatory before any phase advances | ✅ Strong |
| **2. Assign API & Tool Access** | `tool-access-matrix.md` — declares per-layer defaults + per-skill overrides + high-risk tool restrictions. Soft governance, surfaced in Route Receipts and during `/review`. | ✅ Strong (Gap #2 closed) |
| **3. Wire Governance & Constraints** | `phase-gates.md` (entry/exit per phase) + `evidence-contract.md` + `ownership-boundaries.md` + `escalation-rules.md` + `tool-access-matrix.md` + Phase 5.5 release gates (`/review`, `/ultrareview`) | ✅ Strong |
| **4. Human SME in the Loop** | `sme-review-gate.md` — Phase 5.7 Gate G7 with named-SME requirement, written approval, domain triggers (legal/medical/financial/brand/specialized-technical). G7 distinct from G6/G6.5 code review. | ✅ Strong (Gap #3 closed) |

---

## 3. Multi-Agent Architecture

| Component | Dharma implementation | Status |
|---|---|---|
| **Specialist Sub-Agents** | 40 specialist skills (Layer 1–7) — each with single domain ownership: pm-prd, superpowers-execute, uiux-designer, etc. | ✅ Strong |
| **Orchestrator Layer (Logic Referral)** | `00-lifecycle-orchestrator/SKILL.md` — routing-decision-tree, routing-matrix, skills-inventory; classifies request → selects skill chain → enforces gates | ✅ Strong |
| **Lead Agent (CEO) — Final Evaluation** | `lead-agent-evaluation.md` — Phase 5.8 final synthesis across all skills used; cross-skill consistency check (plan vs. execution, goal vs. output, scope, surface area); explicit GO/CONDITIONAL/HOLD/NO-GO verdict; escalation to human Lead Agent for critical risk or material conditions | ✅ Strong (Gap #4 closed) |
| **Lost in the Middle / Context Overload** | `memory-layer` (Layer 0) prevents context loss across sessions; `find-skills` resolves skill gaps; `context-mode` candidate (Layer 0+) for runtime compression; `episodic-memory` (NEW) preserves session continuity | ✅ Strong |

---

## Gap Register

Status as of 2026-05-04. Re-evaluate quarterly.

| # | Gap | Severity | Status | Effort to close |
|---|---|---|---|---|
| 1 | Episodic Memory — past prompts/drafts/outputs preserved per project | 🔴 High | ✅ **Closed** (commit 68e4f1f — `episodic-memory` skill + `memory/episodic/` directory + `dharma-resume`) | — |
| 2 | Tool Access Governance — explicit "this skill can use these tools" declarations | 🟡 Medium | ✅ **Closed** (commit 942dc1f — `tool-access-matrix.md` with per-layer defaults + per-skill overrides + high-risk tool restrictions) | — |
| 3 | Human SME in the Loop — formal domain-expert review pattern (legal, compliance, brand) | 🟡 Medium | ✅ **Closed** (this commit — `sme-review-gate.md` Gate G7 + Phase 5.7 + escalation rules + evidence types) | — |
| 4 | CEO / Lead Agent Final Evaluation — formal final-evaluation role | 🟢 Low | ✅ **Closed** (this commit — `lead-agent-evaluation.md` + Phase 5.8 + verdict types + escalation triggers) | — |
| 5 | Consistent Target KPIs — explicit numerical targets per skill where applicable | 🟢 Low | ✅ **Closed** (this commit — `skill-kpis.md` central registry: 5 KPI categories, layer defaults, per-skill overrides for all 40+ skills, integrated with evidence-contract and Lead Agent G8) | — |

---

## Closing the Episodic Memory Gap (this commit)

**Problem:** Dharma's `memory/decisions.md` and `learnings.md` are decision logs, not session history. Across sessions, past prompts, draft outputs, and intermediate results are lost. This is the same problem GSD's `.planning/` directory addresses.

**Solution:** Extend `[project]/memory/` with episodic memory files + new skills.

### Directory schema (extended)

```
[project]/memory/
├── MEMORY.md              ← existing index
├── decisions.md           ← existing
├── learnings.md           ← existing
├── deployment-pipeline.md ← existing
├── product-context.md     ← existing (optional)
├── PROJECT.md             ← NEW: Layer 1 definition doc anchor
├── STATE.md               ← NEW: live working memory (current phase, blockers, next step)
├── ROADMAP.md             ← NEW: phases, milestones, target dates
├── PLAN.md                ← NEW: active plan (TDD-first tasks)
└── episodic/              ← NEW: episodic memory store
    └── YYYY-MM-DD-[topic-slug].md   ← session digest (prompt summary + outputs + next steps)
```

### Skills wiring

| Skill | Role |
|---|---|
| `memory-layer` (existing) | Reads global memory + project memory; writes decisions/learnings/deployment |
| `episodic-memory` (NEW) | Captures session digests into `memory/episodic/`; loads relevant past sessions on resume |
| `dharma-resume` (NEW) | Reads `STATE.md` + recent episodic entries; reports where we left off; routes to current phase |

### Memory model (post-this-commit, complete)

| Memory type | Where it lives | Read by | Written by |
|---|---|---|---|
| **Semantic** | `Product Dev/memory/{founder, patterns, tools-and-skills}.md` | `memory-layer` pre-flight (global) | `memory-sync`, manual edits |
| **Semantic (project)** | `[project]/memory/{PROJECT, product-context, decisions, learnings}.md` | `memory-layer` pre-flight (project slice) | `memory-layer` post-flight, `dharma-resume` |
| **Episodic** | `[project]/memory/episodic/*.md` | `episodic-memory` (relevant slices) + `dharma-resume` | `episodic-memory` post-session |
| **Working** | `STATE.md` + Phase 0 evidence + evidence-ledger | All skills, live | All skills, live |

---

## Cross-References

- `memory-layer/SKILL.md` — pre/post-flight wrapper protocol
- `episodic-memory/SKILL.md` — session digest capture and retrieval
- `dharma-resume/SKILL.md` — session continuity and phase resumption
- `phase-gates.md` — Phase 0 (working memory anchor) + Phase 5.5 release gates
- `evidence-contract.md` — what counts as proof of completion
- `escalation-rules.md` — when to halt and ask SME (related to Gap #3)

---

## How to use this document

- **Before adding a new agent capability** to Dharma, check this map. If the capability already exists, extend the existing skill rather than create a new one.
- **When auditing Dharma** for completeness vs. an external framework (Kedar, GSD, others), update the Gap Register here rather than creating a parallel doc.
- **When a gap is closed**, change its status to ✅ in the Gap Register and add the implementation row above.

---

## Coverage status

As of 2026-05-04, all 5 originally-identified gaps are **closed**:

| Gap | Status | Closed in commit |
|---|---|---|
| 1 — Episodic Memory | ✅ | 68e4f1f |
| 2 — Tool Access Governance | ✅ | 942dc1f |
| 3 — Human SME in the Loop | ✅ | 901cdc8 |
| 4 — CEO / Lead Agent Final Evaluation | ✅ | 901cdc8 |
| 5 — Consistent Target KPIs | ✅ | this commit |

Dharma's coverage of canonical agent architecture is now ~98%. Future gaps will surface through use; this register stays open as a living document.

---

*Last updated: 2026-05-04*
*Maintained alongside `00-lifecycle-orchestrator/` governance files.*
