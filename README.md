# Dharma — AI-Native Product Development Framework

> Build with discipline. Ship with evidence. Govern with intention.

Dharma is a 38-skill, 8-route product development framework that runs inside Claude Code. It replaces ad-hoc AI-assisted development with a structured lifecycle: classify the work, select the right specialist skills, enforce phase gates, and require verifiable evidence before any completion claim.

Every feature, bug fix, refactor, UI redesign, performance improvement, security change, or release runs through the same disciplined process — regardless of size or complexity.

### Interactive skills picker (cards)

Browse all skills in a visual card grid, filter by layer, select the ones you need, and **copy a ready-made prompt** for your AI session.

| | |
|:---|:---|
| **Live site (GitHub Pages)** | **[https://sahudilip1356.github.io/Dharma/](https://sahudilip1356.github.io/Dharma/)** — if you see the README instead of cards, open **[docs/index.html](https://sahudilip1356.github.io/Dharma/docs/index.html)** or set Pages to folder **`/docs`** (recommended). |
| **Source in repo** | [`docs/index.html`](docs/index.html) — regenerate with `python3 scripts/generate-skills-picker.py` |

**Enable GitHub Pages:** Repository **Settings → Pages → Build and deployment → Source:** Deploy from branch **`main`**, folder **`/docs`**, then save. The site URL will match your username and repo name (above).

---

## The Problem It Solves

AI coding assistants are fast. They are also undisciplined by default.

Without a framework, the same AI session that writes clean code will also:
- Skip UX thinking and ship broken empty states
- Miss accessibility entirely on user-facing screens
- Claim "it's done" based on belief rather than evidence
- Write tests after the code instead of before
- Change production auth logic without a rollback plan
- Ship an LLM-powered feature without adversarial testing

These are not model failures. They are process failures. Dharma solves process failures.

---

## Architecture Overview

Dharma has three structural components:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LIFECYCLE ORCHESTRATOR                           │
│  Classifies work → selects route → enforces phase gates →          │
│  requires evidence → controls completion language                   │
└───────────────────┬─────────────────────────────────────────────────┘
                    │ reads
        ┌───────────▼───────────┐
        │   GOVERNANCE LAYER    │
        │  routing-decision-tree│
        │  ownership-boundaries │
        │  evidence-ledger      │
        │  golden-examples      │
        └───────────┬───────────┘
                    │ invokes
┌───────────────────▼─────────────────────────────────────────────────┐
│                        8 SKILL LAYERS                               │
│                                                                     │
│  Layer 7 — Developer Experience  (2 skills)                         │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 6 — AI & Economics  (6 skills)                               │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 5 — Testing  (1 skill)                                       │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 4 — Experience Quality  (11 skills)                          │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 3 — Execution Methodology  (8 skills)                        │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 2 — Engineering Discipline  (4 skills)                       │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 1 — Product & Planning  (5 skills)                           │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 0 — Memory & Context  (3 skills)  ← cross-cutting wrapper    │
│    memory-layer · episodic-memory · dharma-resume                   │
│  ─────────────────────────────────────────────────────────────────  │
│  Layer 0+ — External Runtime Plugins  (1 candidate)  ← optional     │
│    context-mode (project-scoped, sandbox-only)                      │
└─────────────────────────────────────────────────────────────────────┘
```

The orchestrator is the control tower. It does not fly every aircraft — it decides which runway, what sequence, when to hold, and when to clear for landing. The skill layers are the specialists it invokes.

Layer 0 is the foundation — three skills wrap every skill invocation:
- `memory-layer` loads global + project memory and writes durable decisions/learnings
- `episodic-memory` captures session digests so past prompts/drafts/outputs survive across sessions
- `dharma-resume` reads `STATE.md` + recent episodic digests to pick up exactly where you left off

Together these provide all three canonical agent memory types: **semantic** (long-term knowledge), **episodic** (interaction history), and **working** (current task brief). The engine always starts from current context, never from zero.

Layer 0+ is **optional, project-scoped**: external plugins like `context-mode` that operate beneath skills. Distinct from the internal Layer 0 — these are external candidates, opt-in per project, and not required for Dharma to work.

See `00-lifecycle-orchestrator/agent-architecture.md` for the full mapping to canonical agent architecture (Act + Reason + Memory + Deployment + Multi-Agent) and the Gap Register.

---

## The Lifecycle: 6 Phases + Release Gates

Every task moves through 6 phases. Phase gates are mandatory — a phase cannot start until the previous phase's exit evidence exists.

```
Phase 0 — Intent        Define goal, success criteria, assumptions, scope
Phase 1 — Design        UX flows, accessibility, responsive, states (mandatory if user-facing)
Phase 2 — Plan          Implementation plan, file manifest, bite-sized tasks
Phase 3 — Build         TDD (RED → GREEN → REFACTOR), surgical changes, AI safety gate
Phase 4 — Verify        Evidence-first: run it, read the output, cite the proof
Phase 5 — Finish        Commit, PR, merge, observability setup (AI features)
Phase 5.5 — Release     G6: /review (every change) + G6.5: /ultrareview (high-risk only)
```

The UX Gate at Phase 1 is **non-negotiable** for all user-facing work. No user-facing feature advances past Phase 1 without defined states, accessibility consideration, and responsive behavior planned.

**Phase 5.5 release gates** wrap external code review around every PR before merge:
- **G6 (`/review`)** — Standard code review for every meaningful change. Skip only for doc edits or trivial low-risk changes.
- **G6.5 (`/ultrareview`)** — Cloud-based parallel multi-agent deep review. Mandatory for high-risk changes: auth, payments, data migrations, security, AI safety, production infrastructure, compliance-critical paths.

Critical findings at G6.5 halt the release. See `00-lifecycle-orchestrator/phase-gates.md` for full gate specs.

---

## The 8 Routes

The orchestrator maps every work request to one of 8 routes. Routes determine the skill sequence and evidence requirements.

| Route | Work Type | Entry Skill | Key Constraint |
|---|---|---|---|
| **A** | New Product | `churney-os` | Full stack — all phases mandatory |
| **B** | New Feature | `goal-driven-execution` | UX gate if user-facing; AI gate if LLM present |
| **C** | Bug Fix | `superpowers-debug` | Root cause before fix; test before code |
| **D** | UI/UX Design | `uiux-designer` | Full UX stack mandatory |
| **E** | Refactor | `karpathy-discipline` | Zero behavior change; tests prove it |
| **F** | Performance | `goal-driven-execution` | Baseline metric before and after |
| **G** | Security / Compliance | `think-before-coding` | Rollback plan; no destructive action without approval |
| **H** | Release | `superpowers-verify` | All tests pass; risks stated; rollback documented |

**Routing is deterministic.** A 7-step decision tree runs before any route is selected. The tree checks risk surface area first — auth, payments, AI, compliance — and overlays Route G checks on any route that touches those surfaces.

---

## The 8 Skill Layers

### Layer 1 — Product & Planning (5 skills)

Defines what to build and why before any engineering begins.

| Skill | Purpose |
|---|---|
| `churney-os` | Phase 0–5 founder framework — problem → solution → go-to-market |
| `goal-driven-execution` | Success criteria + verify loop for features |
| `pm-prd` | 8-section product requirements document |
| `pm-user-stories` / `pm-job-stories` | Role-based or JTBD acceptance criteria |
| `pm-prioritization` | Opportunity Score, ICE, RICE scoring |

**Why this layer exists first:** Building the right thing is more important than building the thing right. This layer prevents the most expensive mistake in product development — spending weeks executing on a poorly defined goal.

---

### Layer 2 — Engineering Discipline (4 skills)

Governs how engineers think before and during implementation.

| Skill | Purpose |
|---|---|
| `karpathy-discipline` | Master of 4 principles: avoid complexity, avoid dependencies, start simple, write tests |
| `think-before-coding` | Surface assumptions and unknowns before touching code |
| `simplicity-first` | Minimum viable implementation — no premature abstraction |
| `surgical-changes` | Minimize blast radius — touch only what the task requires |

**Why this layer exists:** AI assistants default to over-engineering. They add abstractions, introduce new dependencies, and expand scope without being asked. This layer enforces restraint. Every skill in this layer is about what NOT to do as much as what to do.

---

### Layer 3 — Execution Methodology (8 skills)

The operational engine — how work moves from idea to shipped code.

| Skill | Purpose |
|---|---|
| `superpowers` | Master orchestrator for the 6-phase execution cycle |
| `superpowers-brainstorm` | Design alternatives gate before implementation |
| `superpowers-write-plan` | Bite-sized implementation plan with file manifest |
| `superpowers-tdd` | RED → GREEN → REFACTOR — test-first discipline |
| `superpowers-execute` | Subagent-driven parallel execution |
| `superpowers-debug` | Root cause investigation before fix |
| `superpowers-verify` | Evidence-first verification — run it, read it, cite it |
| `superpowers-finish` | Commit, PR, merge, cleanup |

**Why this layer exists:** Process without execution discipline produces good plans and bad code. This layer enforces test-first development, prevents "done" claims without evidence, and structures how subagents delegate and parallelize work.

The `superpowers-verify` skill enforces a hard rule: **never use "should work", "probably passes", or "I believe it's fixed" as completion language.** Evidence is the only valid claim.

---

### Layer 4 — Experience Quality (11 skills)

Ensures every user-facing output meets a professional standard of design, accessibility, and responsiveness. Eleven skills cover the **full design lifecycle**: decide the aesthetic → generate the code → apply patterns → audit and verify.

| Skill | Phase | Purpose |
|---|---|---|
| `uiux-designer` | 1 | UX intent, user flows, 4-state design (loading/empty/error/success) |
| `uiux-design-intelligence` | 1 | Style selection, color palette, typography — the aesthetic decision |
| `uiux-frontend-design-system` | 1–2 | Design tokens (CSS variables), component inventory, consistency contract |
| `uiux-interaction-review` | 1 | State transitions, hover/focus/active, feedback loops |
| `uiux-audit` | 1 | Vercel guidelines compliance, copy quality, labels, errors |
| `frontend-design` | **3** | **Aesthetic code generation** — translates Phase 1 brief + tokens into distinctive, non-generic UI code; anti-AI-slop intentionality; runs first in Phase 3 chain |
| `uiux-react-patterns` | 3 | UX patterns, forms, accessibility (runs after frontend-design) |
| `uiux-accessibility-review` | 4 | WCAG compliance, keyboard navigation, screen reader, contrast |
| `uiux-responsive-review` | 4 | Breakpoint behavior at 375 / 768 / 1280 / 1440px |
| `uiux-design-qa` | 5 | Final visual QA — validates code against aesthetic direction statement from frontend-design |

**The Phase 3 UI code chain:**
```
frontend-design (generate)  →  react-best-practices  }  parallel
                            →  uiux-react-patterns   }  after generate
```

**Phase 1 → 3 → 5 design pipeline:**
```
uiux-design-intelligence  decides  the aesthetic  (Phase 1)
frontend-design           executes the aesthetic  (Phase 3)
uiux-design-qa            validates the aesthetic (Phase 5)
```

**Why this layer exists:** Design quality is a retention and trust signal. This layer prevents two failure modes: (1) technically correct code with no visual character — the generic AI aesthetic users immediately recognize and distrust, (2) beautiful design decisions that never make it into the actual code because no skill bridges the gap between "chose the style" and "wrote the component." `frontend-design` is that bridge.

---

### Layer 5 — Testing (1 skill)


Browser-level functional UI verification — the gap between unit tests and visual QA.

| Skill | Phase | Purpose |
|---|---|---|
| `webapp-testing` | Phase 4 | Playwright (Python) browser automation — state verification, console error detection, before/after screenshots as functional evidence |

**Multi-agent Phase 3 chain (Build)** — `superpowers-execute` sequences Phase 3 for UI features:
```
Step 3a  →  frontend-design          (aesthetic code generation — runs first)
              ↓ code produced
Step 3b  →  react-best-practices     }  parallel, after 3a completes
         →  uiux-react-patterns      }
         →  superpowers-tdd          }
```
`frontend-design` must complete before the others — they optimize code that needs to exist first.

**Multi-agent verification pattern** — `superpowers-execute` runs these specialists in parallel at Phase 4:
```
Agent 1 → superpowers-tdd              (unit + integration tests)
Agent 2 → webapp-testing               (browser functional verification)
Agent 3 → uiux-accessibility-review    (a11y on live UI)
Agent 4 → uiux-design-qa               (visual fidelity vs aesthetic direction statement)
```
All four produce evidence. `superpowers-verify` synthesizes into a single completion claim.

**Why this layer exists:** Unit tests prove logic. Design QA proves visual fidelity. `webapp-testing` fills the gap: does the UI actually work in a real browser, across all four states (loading / empty / error / success)?

---

### Layer 7 — Developer Experience (2 skills)

Extends Dharma's reach — one skill resolves ecosystem gaps dynamically; one governs React performance discipline.

| Skill | Phase | Purpose |
|---|---|---|
| `react-best-practices` | Phase 3 | 70 performance rules (waterfalls, bundle, re-renders, JS efficiency) — Vercel Engineering, companion to `uiux-react-patterns` |
| `find-skills` | Pre-Phase 0 | Ecosystem gap resolver — searches skills.sh when no Dharma skill covers a domain; meta-orchestrator tool |

**How they complement each other and the existing stack:**

`react-best-practices` pairs with `uiux-react-patterns` — they split React knowledge by concern:
- `uiux-react-patterns` owns: forms, accessibility patterns (aria, focus), component API design (variant system) — the *UX quality* of React code
- `react-best-practices` owns: waterfalls, bundle size, re-renders, server performance, JS micro-optimizations — the *performance* of React code

`find-skills` activates only when `skills-inventory.md` has no match — it's a safety valve, not a primary tool. It never runs if the existing 38 skills cover the need.

**Why this layer exists:** React performance is a dedicated discipline — 70 rules across 8 categories that live outside UX concerns. And no framework is complete; `find-skills` ensures Dharma can extend itself when the ecosystem has something better than general capability for a novel domain.

---

### Layer 6 — AI & Economics (6 skills)

Governs the full lifecycle of AI/LLM-powered features — from cost design to post-ship quality.

| Skill | Phase | Purpose |
|---|---|---|
| `inference-economics` | Phase 2 | Model selection, token budget, cost ceiling — before writing the prompt |
| `prompt-optimization` | Phase 3 | Prompt versioning, token efficiency, consistency testing |
| `ai-safety-eval` | Phase 3 | Pre-ship gate: adversarial testing, hallucination detection, bias audit, cost validation |
| `ai-observability` | Phase 5 | Post-ship monitoring: 5-layer stack covering latency, errors, cost, quality, drift |
| `model-governance` | Ongoing | Model registry, deprecation handling, audit trails (activate at 2+ AI features) |
| `benchmark-framework` | Ongoing | Scheduled quality regression tracking (activate at 3+ AI features) |

**Why this layer exists:** AI features have failure modes that traditional software skills cannot catch. A prompt that works on your test cases may hallucinate on edge cases. A model that passes safety review today may degrade silently when the provider updates it. This layer treats AI features as first-class production systems — with their own economics, safety requirements, observability, and governance.

**The AI feature lifecycle in Dharma:**
```
Phase 2: inference-economics designs the cost envelope and selects the model
Phase 3: prompt-optimization prepares and versions the prompt
Phase 3: ai-safety-eval gates on safety, hallucination, bias, cost constraints
Phase 5: ai-observability sets up post-ship monitoring before go-live
Ongoing: model-governance maintains the model registry + deprecation playbook
Ongoing: benchmark-framework tracks quality regression on a schedule
```

---

### Layer 0 — Memory & Context (3 skills)

The foundation that every other layer runs on top of. A cross-cutting wrapper — not invoked directly, but active on every skill call. Together these three skills provide all three canonical agent memory types.

| Skill | Trigger | Purpose | Memory type owned |
|---|---|---|---|
| `memory-layer` | Automatic — pre/post every skill | Two-drawer context: global (founder, patterns) + project (decisions, learnings, deployment) | Semantic |
| `episodic-memory` | Automatic post-session + manual | Session digests stored at `[project]/memory/episodic/` — preserves past prompts, drafts, outputs, open threads | Episodic |
| `dharma-resume` | "resume", "continue", "where were we", auto when STATE.md exists | Reads STATE.md + recent episodic digests; outputs Resume Brief; routes back to right phase | Working |

**The three-drawer model:**

```
TOP DRAWER — GLOBAL (always loaded, every project)
  Product Dev/memory/founder.md       — who Dilip is, how he builds
  Product Dev/memory/patterns.md      — build patterns across all projects
  Product Dev/memory/tools-and-skills.md — what's been built

MIDDLE DRAWER — PROJECT (loaded per active project folder)
  [project]/memory/PROJECT.md         — Layer 1 definition doc anchor
  [project]/memory/decisions.md       — decisions made + rationale
  [project]/memory/learnings.md       — failures + what worked
  [project]/memory/deployment-pipeline.md — how this project ships
  [project]/memory/STATE.md           — live working memory: current phase, blockers, next step
  [project]/memory/ROADMAP.md         — phases, milestones, target dates
  [project]/memory/PLAN.md            — active plan (TDD-first tasks)

BOTTOM DRAWER — EPISODIC (interaction history)
  [project]/memory/episodic/YYYY-MM-DD-slug.md — session digests
```

**Three memory types, fully covered:**
- **Semantic (long-term):** Global + project-level facts via `memory-layer`
- **Episodic (interaction history):** Session digests via `episodic-memory` — what was discussed, what drafts existed, what prompt produced what output
- **Working (immediate):** STATE.md + Phase 0 evidence via `dharma-resume`

**Pre-flight:** `memory-layer` loads global + relevant project memory slices before any skill runs.
**Post-flight order:** `episodic-memory` first (captures the session arc), then `memory-layer` (extracts durable decisions/learnings from that arc). STATE.md updated last if work is incomplete.
**Staleness check:** if project memory is >7 days old, surfaces a warning once, then proceeds — never blocks.
**New project:** creates `memory/` scaffold automatically on first invocation.

**Why this layer exists:** Without it, every Dharma session starts from zero — no knowledge of what was decided, what failed, what was being worked on, or how this specific project ships. Layer 0 makes the engine stateful and resumable. The three-skill set closes the same gap that GSD's `.planning/` directory addresses, but inside Dharma's existing memory pattern.

**Relationship to memory-sync, dharma-resume, episodic-memory:**

| Skill | Trigger | Scope |
|---|---|---|
| `memory-sync` | Manual — `/memory-sync <summary>` | Full session bulk capture |
| `memory-layer` | Automatic — wraps every skill | Skill-level, selective decisions/learnings |
| `episodic-memory` | Automatic post-session + manual | Session digest |
| `dharma-resume` | Trigger phrases or auto when STATE.md exists | Read-side: surface state, route to phase |

They are complementary. Together they provide complete memory coverage.

---

## The Governance Layer

Four meta-control files that tell the orchestrator **when and how** to use skills — not more skills, but conductor-level controls.

| File | Purpose |
|---|---|
| `routing-decision-tree.md` | 7-step classification that runs before every task. Produces a Route Receipt. |
| `ownership-boundaries.md` | Defines what each skill owns and explicitly does NOT own. Prevents scope creep. |
| `evidence-ledger-template.md` | Structured receipt: task classification + gate status + evidence + constrained completion language |
| `examples/` | 8 golden reference scenarios showing correct classification, route, skill selection, and evidence |

**Why governance comes after skills:** You cannot write boundaries until you have the skills to bound. The governance layer is the score sheet, not the instruments. It makes the framework consistent and self-correcting — skills stay in their lane, routing is deterministic, and completion claims are always backed by evidence.

---

## How the Orchestrator Works in Practice

When a task arrives, the orchestrator runs in sequence:

**Step 0 — Run the routing decision tree**
7 questions in order: Is this high-risk (auth/payments/AI/compliance)? Is it user-facing? Is something broken? Is it a new feature? New product? Refactor? Release? First match determines the route.

**Step 0.5 — Resolve skill gaps (find-skills)**
Check every functional skill in the planned route against `skills-inventory.md`. If any domain has no installed skill, `find-skills` searches the open ecosystem (skills.sh) for a quality match. Installed skills always take precedence — `find-skills` only activates on a genuine gap.

**Step 1 — Output the Route Receipt**
Before any code is touched:
```
Route Receipt
─────────────────────────────────────────────
Request:        Add Google OAuth login
Classification: new-feature | auth | user-facing | high | hard
Primary route:  B — New Feature
Supporting:     G — Security (auth surface area)
Skills selected: [phase-by-phase list]
Evidence required: [what must exist to claim done]
Stop conditions: [what halts progress and requires approval]
─────────────────────────────────────────────
```

**Steps 2–5 — Execute phases in sequence**
Each phase gate requires exit evidence before the next phase starts. The evidence ledger tracks gate status. No phase is skipped without an explicit reason on record.

**Step 6 — Claim completion with evidence**
Five valid completion states — and only five:
- `Implemented and verified with [evidence].`
- `Implemented but not runtime-verified — [what's missing].`
- `Planned only; no code changed.`
- `Partially complete; remaining risks: [list].`
- `Blocked: [specific blocker].`

"Should work", "probably passes", and "I believe it's fixed" are not valid completion states.

---

## Complete Skill Inventory

### Layer 1 — Product & Planning
| Skill | File |
|---|---|
| `churney-os` | `churney-os/SKILL.md` |
| `goal-driven-execution` | `goal-driven-execution/SKILL.md` |
| `pm-prd` | `pm-prd/SKILL.md` |
| `pm-user-stories` | `pm-user-stories/SKILL.md` |
| `pm-job-stories` | `pm-job-stories/SKILL.md` |
| `pm-prioritization` | `pm-prioritization/SKILL.md` |

### Layer 2 — Engineering Discipline
| Skill | File |
|---|---|
| `karpathy-discipline` | `karpathy-discipline/SKILL.md` |
| `think-before-coding` | `think-before-coding/SKILL.md` |
| `simplicity-first` | `simplicity-first/SKILL.md` |
| `surgical-changes` | `surgical-changes/SKILL.md` |

### Layer 3 — Execution Methodology
| Skill | File |
|---|---|
| `superpowers` | `superpowers/SKILL.md` |
| `superpowers-brainstorm` | `superpowers-brainstorm/SKILL.md` |
| `superpowers-write-plan` | `superpowers-write-plan/SKILL.md` |
| `superpowers-tdd` | `superpowers-tdd/SKILL.md` |
| `superpowers-execute` | `superpowers-execute/SKILL.md` |
| `superpowers-debug` | `superpowers-debug/SKILL.md` |
| `superpowers-verify` | `superpowers-verify/SKILL.md` |
| `superpowers-finish` | `superpowers-finish/SKILL.md` |

### Layer 4 — Experience Quality
| Skill | Phase | File |
|---|---|---|
| `uiux-designer` | 1 | `uiux-designer/SKILL.md` |
| `uiux-design-intelligence` | 1 | `uiux-design-intelligence/SKILL.md` |
| `uiux-frontend-design-system` | 1–2 | `uiux-frontend-design-system/SKILL.md` |
| `uiux-interaction-review` | 1 | `uiux-interaction-review/SKILL.md` |
| `uiux-audit` | 1 | `uiux-audit/SKILL.md` |
| `frontend-design` | **3** | `frontend-design/SKILL.md` |
| `uiux-react-patterns` | 3 | `uiux-react-patterns/SKILL.md` |
| `uiux-accessibility-review` | 4 | `uiux-accessibility-review/SKILL.md` |
| `uiux-responsive-review` | 4 | `uiux-responsive-review/SKILL.md` |
| `uiux-design-qa` | 5 | `uiux-design-qa/SKILL.md` |

### Layer 5 — Testing
| Skill | File |
|---|---|
| `webapp-testing` | `webapp-testing/SKILL.md` |

### Layer 6 — AI & Economics
| Skill | File |
|---|---|
| `inference-economics` | `inference-economics/SKILL.md` |
| `prompt-optimization` | `prompt-optimization/SKILL.md` |
| `ai-safety-eval` | `ai-safety-eval/SKILL.md` |
| `ai-observability` | `ai-observability/SKILL.md` |
| `model-governance` | `model-governance/SKILL.md` |
| `benchmark-framework` | `benchmark-framework/SKILL.md` |

### Layer 7 — Developer Experience
| Skill | File |
|---|---|
| `react-best-practices` | `react-best-practices/SKILL.md` |
| `find-skills` | `find-skills/SKILL.md` |

### Layer 0 — Memory & Context
| Skill | File |
|---|---|
| `memory-layer` | `memory-layer/SKILL.md` |
| `episodic-memory` | `episodic-memory/SKILL.md` |
| `dharma-resume` | `dharma-resume/SKILL.md` |

### Orchestrator & Governance
| File | Purpose |
|---|---|
| `00-lifecycle-orchestrator/SKILL.md` | Master orchestrator |
| `00-lifecycle-orchestrator/routing-decision-tree.md` | 7-step classification |
| `00-lifecycle-orchestrator/routing-matrix.md` | Route → skills → evidence map |
| `00-lifecycle-orchestrator/ownership-boundaries.md` | Skill scope limits |
| `00-lifecycle-orchestrator/phase-gates.md` | Phase entry/exit criteria (incl. Phase 5.5 release gates) |
| `00-lifecycle-orchestrator/evidence-contract.md` | What counts as valid evidence |
| `00-lifecycle-orchestrator/evidence-ledger-template.md` | Task receipt template |
| `00-lifecycle-orchestrator/escalation-rules.md` | When to stop and escalate |
| `00-lifecycle-orchestrator/agent-architecture.md` | Maps Dharma to canonical agent architecture (Act+Reason+Memory + Deployment + Multi-Agent) with Gap Register |
| `00-lifecycle-orchestrator/examples/` | 8 golden reference scenarios |

---

## Quick Start

### Prerequisites
- Claude Code CLI installed
- A project with a `.claude/` directory

### Installation

```bash
# Clone into your .claude/skills directory
git clone https://github.com/SahuDilip1356/dharma.git .claude/skills

# That's it. The orchestrator reads from this directory automatically.
```

### Using the Framework

Every task starts the same way. Open Claude Code and describe what you want to build:

```
"Add a patient search feature to the clinic dashboard"
```

The lifecycle orchestrator will:
1. Run the routing decision tree and output a Route Receipt
2. Invoke the appropriate specialist skills in phase sequence
3. Enforce gate checks before advancing phases
4. Require evidence before claiming completion

No commands to memorize. No configuration to write. The framework activates from the `SKILL.md` files — Claude Code reads them automatically when present in `.claude/skills/`.

### Customizing for Your Stack

Each skill file is a Markdown document. Customize:
- Technology references (React → Vue, PostgreSQL → MongoDB, etc.)
- Cost thresholds in `inference-economics`
- Alert thresholds in `ai-observability`
- Compliance requirements in `ai-safety-eval`

The framework is stack-agnostic by design. The principles hold regardless of your technology choices.

---

## Design Principles

Five principles shaped every decision in the framework:

**1. Evidence over assertion**
No completion claim without proof. Running the code and observing the output is the only valid verification. "Should work" is not a completion state.

**2. Specialization over generalization**
One skill, one responsibility. A UX skill does not re-plan the architecture. An engineering discipline skill does not do accessibility audits. Specialist skills stay in their lane — discoveries outside that lane are reported as blockers or follow-up recommendations, never absorbed and acted on.

**3. Gate before advancing**
A phase cannot start until the previous phase's exit evidence exists. The gate is not a suggestion. Time pressure and "just this once" are not exceptions to gate requirements.

**4. Governance before complexity**
When a framework has many skills, the risk shifts from "not enough capability" to "capability applied in the wrong place." The governance layer (routing tree, ownership boundaries, evidence ledger) solves that risk. It was built after the skills, not before.

**5. AI features are production systems**
LLM-powered features are not ordinary features. They have unique failure modes (hallucination, drift, cost explosions, adversarial misuse) that require their own lifecycle layer. The AI & Economics layer treats AI features with the rigor they require.

---

## License

MIT — use freely, customize for your stack, contribute improvements back.

---

*Built by [Dilip Sahu](https://github.com/SahuDilip1356) — founder, product builder, and firm believer that great software is an act of service.*
