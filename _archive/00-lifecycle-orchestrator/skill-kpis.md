# Skill KPI Registry

Defines target KPIs for every Dharma skill. Closes Gap #5 from `agent-architecture.md` — the "Target KPIs" component of the canonical Act framework.

> **Central registry, not per-skill frontmatter.** Same pattern as `tool-access-matrix.md` and `ownership-boundaries.md` — one file maps all 40+ skills, no individual skill files modified. Edit here when adding/changing skills.

---

## Why this exists

Without explicit KPIs, "did this skill do its job?" has no measurable answer. Implicit "exit evidence" is a gate, not a target. KPIs give skills a North Star: not just "did the skill produce output?" but "was the output good?"

Three reasons this matters:
1. **Self-correction** — KPIs let you see drift before it compounds
2. **Comparison** — same skill, two runs, which was better?
3. **Improvement signal** — when a skill underperforms its KPI consistently, that's a flag to revise the skill (or the KPI)

---

## KPI Categories

Five categories of measurable signal:

| Category | What it measures | Example |
|---|---|---|
| **Output Quality** | Did the artifact meet the standard? | PRD has all 8 sections; tests pass; design has all states |
| **Efficiency** | Time / tokens / cost | Time-to-draft; token usage per task; cost vs. budget |
| **Behavioral** | Did the skill follow its discipline? | Assumptions surfaced; alternatives offered; tests written first |
| **Gate Compliance** | Did the skill produce required evidence? | Phase exit evidence complete; release gate passed |
| **Outcome** | Did the work actually achieve the goal? | Bug stays fixed; feature adopted; no regression |

Most skills have 2–3 KPIs across these categories. More than 5 is over-engineering.

---

## KPI Defaults by Layer

When a skill has no explicit overrides below, these layer defaults apply.

| Layer | Default KPIs | How measured |
|---|---|---|
| **Layer 0 — Memory & Context** | Pre-flight memory loaded correctly · Post-flight writes complete · Staleness warnings surfaced | Spot-check audit |
| **Layer 1 — Product & Planning** | Output completeness (% of required sections) · Reviewer approval on first pass · Time-to-first-draft | Manual review |
| **Layer 2 — Engineering Discipline** | Assumptions surfaced count · Forbidden patterns avoided · Reviewer rejection rate | Behavioral audit |
| **Layer 3 — Execution Methodology** | Plan adherence (executed = planned) · Test pass rate · Evidence-contract compliance | Task-level evidence |
| **Layer 4 — Experience Quality** | All states covered (empty/loading/error/success) · WCAG compliance · Visual finding count | Audit findings |
| **Layer 5 — Testing** | Test pass rate · Flaky test rate · Coverage % on changed files | Test reports |
| **Layer 6 — AI & Economics** | Cost vs. budget · Token efficiency · Quality regression rate | Per-feature dashboards |
| **Layer 7 — Developer Experience** | Resolution rate · Match accuracy · User-confirmed value | Per-invocation feedback |

---

## Per-Skill KPI Overrides

Skills with unique targets that deviate from layer defaults. Listed by layer.

### Layer 0 — Memory & Context

| Skill | KPIs | Target |
|---|---|---|
| `memory-layer` | Pre-flight context loaded; post-flight writes accurate; staleness warning trigger rate | 100% load on every skill; 0 false-write events; warning on every >7-day gap |
| `episodic-memory` | Digest written for substantive sessions; digest brevity (≤1 page/session); retrieval relevance | 100% for substantive sessions; ≤1 page/session; ≥80% relevance on resume |
| `dharma-resume` | STATE.md accuracy; resume brief reflects reality; routes to correct phase | ≥95% state-accuracy on user feedback; correct phase routing |

### Layer 1 — Product & Planning

| Skill | KPIs | Target |
|---|---|---|
| `churney-os` | All 5 phases produce required output; review gate pass rate | 100% phase completeness; first-pass approval ≥80% |
| `pm-prd` | All 8 sections completed; revision rounds before approval | 100% completeness; ≤2 revision rounds |
| `pm-user-stories` | INVEST compliance per story; 3 C's coverage | 100% INVEST; 100% Card+Conversation+Confirmation |
| `pm-job-stories` | Situation+Motivation+Outcome present per story; user voice (no role mention) | 100% structure; 100% role-free |
| `pm-prioritization` | Framework selected matches use case; scoring methodology stated | Manual review on adoption |
| `goal-driven-execution` | Success criteria measurable; verification loop completed; goal achieved | ≥95% measurable; loop closes; 100% goal-achievement claim has evidence |
| `saral-build` | Layer 1 def doc has all 6 sections; Core 3 = exactly 3; PULSE has 5 metrics | 100% completeness; exactly 3 Core; 5 PULSE metrics defined |

### Layer 2 — Engineering Discipline

| Skill | KPIs | Target |
|---|---|---|
| `karpathy-discipline` | All 4 sub-skills triggered when applicable; behavior change observed | Triggered on every non-trivial coding task |
| `think-before-coding` | Assumptions surfaced count; alternatives offered count; ambiguity flagged | ≥3 assumptions per non-trivial task; ≥2 alternatives when applicable |
| `simplicity-first` | Speculative abstractions avoided; no premature flexibility; smallest viable code | 0 unrequested abstractions; reviewer-confirmed minimalism |
| `surgical-changes` | Only requested files modified; unrelated changes = 0 | 0 scope-creep modifications |

### Layer 3 — Execution Methodology

| Skill | KPIs | Target |
|---|---|---|
| `superpowers` | All 6 phases produce required evidence; phase-gate violations = 0 | 100% phase completeness; 0 gate skips |
| `superpowers-brainstorm` | Spec approved before code; options surfaced; user confirmation received | 100% approval-before-code; ≥2 options when meaningful |
| `superpowers-write-plan` | Tasks 2–5 min each; TDD test plan present; assumptions listed | 100% bite-sized; 100% test plan; 100% assumptions |
| `superpowers-tdd` | RED seen before GREEN; tests written first; refactor with tests passing | 100% RED-first; 0 test-after-code violations |
| `superpowers-execute` | Plan adherence (executed = planned); evidence per task; subagent quality | ≥95% plan adherence; 100% evidence per task |
| `superpowers-debug` | Root cause identified before fix; fix scope = root cause scope; reproduces in test | 100% root-cause-before-fix; reproduction test exists |
| `superpowers-verify` | All evidence types collected; no false-pass; banned lazy language used | 100% evidence; 0 "looks good" claims |
| `superpowers-finish` | Branch closes cleanly; PR description complete; risks stated | 100% clean close; 100% risks documented |

### Layer 4 — Experience Quality

| Skill | KPIs | Target |
|---|---|---|
| `uiux-designer` | UX gate output complete (flow + states + a11y + responsive + visual) | 100% all 5 elements |
| `uiux-design-intelligence` | Style + colors + fonts selected with rationale; design system coherent | 100% selections rationale-backed |
| `uiux-frontend-design-system` | Tokens defined; component library consistent | 100% tokens; reviewer-confirmed consistency |
| `uiux-accessibility-review` | WCAG 2.1 AA compliance; keyboard nav verified; contrast checked | 100% AA; 0 keyboard traps; 100% contrast pass |
| `uiux-responsive-review` | All breakpoints (375/768/1280/1440px) verified | 100% breakpoints |
| `uiux-interaction-review` | All states + transitions + feedback documented | 100% states; ≥2 feedback signals per state |
| `uiux-design-qa` | Visual finding count; design intent fidelity | ≤3 findings per major surface; ≥90% intent fidelity |
| `uiux-audit` | Vercel guideline compliance score | ≥90% compliance |
| `uiux-react-patterns` | 70-rule compliance score | ≥85% on changed files |
| `frontend-design` | Aesthetic intent → code fidelity; design tokens used | ≥90% intent fidelity; 100% token usage |

### Layer 5 — Testing

| Skill | KPIs | Target |
|---|---|---|
| `webapp-testing` | Browser flows pass; flaky test rate; runtime per flow | 100% pass; <5% flaky; ≤30s/flow |

### Layer 6 — AI & Economics

| Skill | KPIs | Target |
|---|---|---|
| `inference-economics` | Cost vs. budget; token efficiency; model selection rationale | ≤budget; tokens optimized; 100% rationale |
| `ai-safety-eval` | Phase 3 gate triggered for all AI features; critical findings count | 100% AI-feature gate; 0 critical at release |
| `ai-observability` | Pre-launch monitoring coverage; alert latency on incidents | 100% pre-launch coverage; alert <5min |
| `prompt-optimization` | Token reduction %; quality stability across prompt versions | ≥20% reduction; ±5% quality variance |
| `model-governance` | Deprecation incidents = 0; model registry up-to-date | 0 surprise deprecations; registry current |
| `benchmark-framework` | Regression detection rate; false alarms; cadence adherence | ≥95% true regression detection; <10% false; on schedule |

### Layer 7 — Developer Experience

| Skill | KPIs | Target |
|---|---|---|
| `find-skills` | Skill match accuracy; user-confirmed match value | ≥80% match adoption when surfaced |
| `react-best-practices` | 70-rule audit pass rate | ≥85% on changed files |

### Phase 5.5+ Release Gates (not skills, but tracked here for completeness)

| Gate | KPIs | Target |
|---|---|---|
| G6 `/review` | Findings caught before merge; false-positive rate | High catch rate; <15% false-positive |
| G6.5 `/ultrareview` | Critical findings caught; release halts due to G6.5 | 0 critical reaches production |
| G7 SME Review | Domain errors caught; SME response time | 0 domain errors at release; ≤5 business days response |
| G8 Lead Agent | Cross-skill drift caught; verdict accuracy | 100% drift catches; ≥95% verdict matches outcome |

---

## How to use this registry

### When adding a new skill
1. Decide its layer
2. Use the layer default KPIs unless the skill has unique targets
3. If unique, add a row in the per-skill overrides above
4. Define 2–3 KPIs (more is over-engineering)
5. Define the target — quantitative where possible, qualitative when not

### When measuring (per task / per quarter)
- **Per task:** Most KPIs surface naturally in evidence (test counts, finding counts, gate pass/fail). Lead Agent (G8) summary should reference the relevant skill KPIs in its verdict.
- **Per quarter:** Aggregate KPIs across tasks. Look for skills consistently below target — that's a signal to revise the skill OR adjust the KPI.

### When a KPI is consistently missed
Two diagnoses:
1. **The skill is underperforming.** Revise the skill (rewrite SKILL.md, add examples, tighten instructions).
2. **The KPI is wrong.** The target was unrealistic, or the skill's actual job differs from what the KPI measures. Update the KPI.

Either way, the gap surfaces an action. Without KPIs, the gap is invisible.

---

## Anti-patterns (don't do these)

| Anti-pattern | Why it fails |
|---|---|
| Adding KPIs for every skill action | Over-instrumentation; kills speed |
| Vanity KPIs ("usage count") | Measures activity, not quality |
| Hard-coded numerical targets without context | Targets ≠ skill quality; depends on task complexity |
| Ignoring qualitative KPIs | Some quality signals are subjective; don't pretend they're not |
| Adding a KPI per phase per skill | 6 phases × 40 skills × 3 KPIs = 720 metrics; nobody tracks 720 |

---

## What this registry does NOT do

- **It does not technically enforce KPIs.** Same governance model as the rest of Dharma — declared, surfaced, reviewed. Not runtime-gated.
- **It does not replace the evidence-contract.** Evidence is the proof a skill produced output; KPIs measure whether that output is good.
- **It does not require automated dashboards.** Most KPIs are spot-checked or qualitatively reviewed. A dashboard is optional, not required.
- **It does not need to be perfect from day one.** Treat as living document; revise as you learn what actually correlates with skill quality.

---

## Integration with existing files

| File | How KPIs interact |
|---|---|
| `evidence-contract.md` | Evidence is the *input* to KPI measurement. KPIs are the *output* — quality assessment of that evidence. |
| `phase-gates.md` | Phase exit evidence + KPI satisfaction together = gate passes. Evidence is necessary; KPI is the quality bar. |
| `lead-agent-evaluation.md` | Lead Agent (G8) summarizes which skills met/missed their KPIs in the Final Evaluation entry. |
| `tool-access-matrix.md` | KPIs include tool-access-violation rate (should be 0). |
| `agent-architecture.md` | KPI measurement is the "Act → Target KPIs" component of the canonical agent framework. |

---

## Recordkeeping

Per-task KPIs surface naturally in:
- Phase exit evidence (raw measurement)
- Lead Agent (G8) Final Evaluation entry (verdict-level summary)
- `[project]/memory/decisions.md` (when a KPI miss leads to a skill revision decision)

Aggregate KPIs (quarterly):
- `Product Dev/memory/tools-and-skills.md` — annotate skills with quarterly KPI status
- Optional: dedicated `kpi-tracker.md` per project if KPI tracking becomes a meaningful workflow

---

*Last updated: 2026-05-04*
*Living document. Revise when skills are added/changed, when measurement reveals a KPI is wrong, or when a category of work emerges that has no KPI yet.*
