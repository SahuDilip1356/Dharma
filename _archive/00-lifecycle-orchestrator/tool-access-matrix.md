# Tool Access Matrix

Declares which tools each skill (and skill layer) is permitted to use. Closes Gap #2 from `agent-architecture.md` — the Deployment Framework's "Assign API & Tool Access" step.

> **Governance model:** Declarative, not runtime-enforced. Same pattern as `ownership-boundaries.md` and `escalation-rules.md` — these are review and audit boundaries, not technical sandboxes. Violations surface during review (`/review`) or routing audits.

---

## Why this matrix exists

Without explicit tool-access boundaries, skills can drift in scope. A planning skill could write code; a verification skill could mutate state; a memory skill could shell out. This matrix:

- **Documents intent** — what each skill is supposed to touch
- **Surfaces violations during review** — if a planning skill calls Bash, that's a flag
- **Prevents scope creep** — "should I add this tool?" has an answer per skill
- **Maps to security risk surface** — which skills can mutate vs. read-only

---

## Tool Categories

Tools available in Claude Code grouped by capability and risk:

| Category | Tools | Risk surface |
|---|---|---|
| **Read** | `Read`, `Glob`, `Grep`, `NotebookRead` | None — pure inspection |
| **Write** | `Write`, `NotebookEdit` | Creates new files; medium risk |
| **Edit** | `Edit` | Modifies existing files; medium risk |
| **Bash** | `Bash` (with `run_in_background`) | Shell execution; HIGH risk — can mutate state, run arbitrary code, network requests |
| **Web** | `WebFetch`, `WebSearch` | Network read; low–medium risk (data egress) |
| **Agent** | `Agent`, `ToolSearch` | Spawns sub-agents with their own tool surface; risk inherits |
| **Plan** | `EnterPlanMode`, `ExitPlanMode`, `TodoWrite` | Workflow state; low risk |
| **Schedule** | `ScheduleWakeup`, `CronCreate`, `CronDelete`, `CronList` | Background scheduling; medium risk |
| **MCP** | `mcp__*` (per-server) | External system access; risk depends on MCP server |
| **Browser** | `mcp__Claude_in_Chrome__*`, `mcp__computer-use__*` | UI automation; HIGH risk — can interact with apps, websites |
| **Skill** | `Skill` | Invoke other skills; risk inherits from invoked skill |
| **Question** | `AskUserQuestion` | Solicit user input; no risk |

---

## Default Tool Access by Layer

Default access per layer. Skills inherit unless explicitly overridden below.

| Layer | Default ALLOWED | Explicitly FORBIDDEN | Why |
|---|---|---|---|
| **Layer 0 — Memory & Context** | Read, Write, Edit (memory/* and project files only), Glob, Grep | Bash, Agent, Browser | Memory is data, not execution. No shell. |
| **Layer 0+ — External Runtime Plugins** | Plugin-defined per server | (depends on plugin) | Defined by the external plugin's MCP manifest |
| **Layer 1 — Product & Planning** | Read, Write (specs/PRDs), Glob, Grep, WebFetch, AskUserQuestion | Bash, Edit (production code), Browser | Planning produces docs, not code. No shell. |
| **Layer 2 — Engineering Discipline** | Read, Glob, Grep, AskUserQuestion | Write, Edit, Bash, Agent | Discipline skills are advisory — they shape behavior, not produce artifacts |
| **Layer 3 — Execution Methodology** | Full surface (Read, Write, Edit, Bash, Agent, Skill, MCP) | none (subject to per-skill overrides below) | Execution is the layer that DOES the work; needs full toolkit |
| **Layer 4 — Experience Quality** | Read, Write (design docs), Glob, Grep, WebFetch, Browser, AskUserQuestion | Bash | Design and review; UI inspection allowed via browser |
| **Layer 5 — Testing** | Read, Write (test files), Edit (test files only), Bash, Browser | Edit (production code), Agent | Tests need shell; production code edits belong in Layer 3 |
| **Layer 6 — AI & Economics** | Read, Write (configs/prompts), Edit (configs/prompts), WebFetch, MCP | Bash (except cost calc), Browser | AI work is config-heavy, not shell-heavy |
| **Layer 7 — Developer Experience** | Read, Glob, Grep, WebFetch, WebSearch, AskUserQuestion | Bash, Edit, Write | Meta-tools that help find or analyze, not produce |

---

## Per-Skill Overrides

Skills that genuinely need different access than their layer default.

### Layer 3 — Execution Methodology (overrides)

| Skill | Allowed | Forbidden | Reason |
|---|---|---|---|
| `superpowers-brainstorm` | Read, Glob, Grep, WebFetch, AskUserQuestion | Write, Edit, Bash, Agent | Brainstorm is exploration, not production |
| `superpowers-write-plan` | Read, Write (PLAN.md only), Glob, Grep, WebFetch | Edit (production code), Bash, Agent | Plan writing produces ONE file (the plan), not code |
| `superpowers-debug` | Read, Bash, Glob, Grep | Write, Edit, Agent | Debug is investigation; the FIX is a separate skill |
| `superpowers-verify` | Read, Bash, Glob, Grep | Write, Edit, Agent | Verify is read-only validation; cannot mutate during verification |
| `superpowers-finish` | Read, Bash (git commands), Edit (commit/PR descriptions only), Agent | Edit (source code) | Finish is release prep, not code authoring |

### Layer 4 — Experience Quality (overrides)

| Skill | Allowed | Forbidden | Reason |
|---|---|---|---|
| `uiux-audit` | Read, Glob, Grep, WebFetch, Browser | Write, Edit, Bash | Audit is read-only review |
| `uiux-accessibility-review` | Read, Glob, Grep, Browser | Write, Edit, Bash | Review only |
| `uiux-responsive-review` | Read, Glob, Grep, Browser | Write, Edit, Bash | Review only |
| `uiux-interaction-review` | Read, Glob, Grep, Browser | Write, Edit, Bash | Review only |
| `uiux-design-qa` | Read, Glob, Grep, Browser | Write, Edit, Bash | Final visual gate; pure inspection |
| `frontend-design` | Read, Write, Edit, Glob, Grep, WebFetch | Bash | Generates UI code; no shell needed |

### Layer 0 — Memory & Context (overrides)

| Skill | Allowed | Forbidden | Reason |
|---|---|---|---|
| `memory-layer` | Read, Write (memory/*), Edit (memory/*), Glob | Bash, Agent, Browser, Edit (non-memory files) | Memory writes to memory/ directory only |
| `episodic-memory` | Read, Write (memory/episodic/*), Glob | Edit (anywhere), Bash, Agent | Episodic captures NEW digests; never edits past ones |
| `dharma-resume` | Read, Write (memory/STATE.md only), Glob, Skill | Edit (anywhere except STATE.md), Bash | Resume reads everything, writes only STATE.md |

### Layer 6 — AI & Economics (overrides)

| Skill | Allowed | Forbidden | Reason |
|---|---|---|---|
| `inference-economics` | Read, Write (cost-config docs), Bash (cost calc scripts), WebFetch | Edit (production code), Agent | Cost analysis sometimes needs Bash for calculations |
| `ai-observability` | Read, Write (monitoring config), Edit (monitoring config), MCP, WebFetch | Bash, Edit (production code) | Configs only, not code |
| `ai-safety-eval` | Read, Glob, Grep, WebFetch, Browser | Write, Edit, Bash | Safety eval is read-only review |

---

## High-Risk Tool Restrictions

Some tool combinations require additional escalation regardless of skill:

| Tool | When it requires explicit user approval (per `escalation-rules.md`) |
|---|---|
| `Bash` running `git push --force`, `git reset --hard`, `rm -rf` | Always |
| `Bash` modifying production data | Always |
| `Edit` to auth/secrets/payment-flow files | Always |
| `Browser` with computer-use clicking irreversible buttons (purchase, send, publish) | Always |
| `mcp__*__authenticate` for new platform | Always |
| `Write` to `.env`, credentials, or secret files | NEVER (prohibited regardless of approval) |

---

## Enforcement Model

**Soft governance** — declared, reviewed, not runtime-enforced. Same model as `ownership-boundaries.md`.

### Where this matrix is consulted

1. **At routing time** (orchestrator Step 0) — when the route receipt is built, the orchestrator can compare planned skill invocations against this matrix and surface mismatches.
2. **At review time** (`/review`, `/ultrareview`) — reviewers should flag tool calls that violate a skill's declared access.
3. **At skill authoring time** — when adding a new skill or changing existing ones, this matrix is the reference point for "what tools should this need?"
4. **At evidence-contract time** (Phase 4 verification) — if a skill produced output via tools outside its allowed set, that's an evidence violation worth surfacing.

### When violations surface

| Scenario | Action |
|---|---|
| Skill needs a tool not in its access list (legitimate) | Update this matrix with rationale; commit the change |
| Skill called a tool not in its access list (review finding) | Surface in `/review` output; fix in the skill or update matrix |
| New tool category appears in Claude Code | Add to "Tool Categories" section above; map to existing skills as appropriate |
| Plugin adds new MCP server | Document in skills-inventory.md Layer 0+; declare its tool category |

### What this matrix does NOT do

- **It does not technically prevent tool calls.** Skills are markdown; they cannot enforce execution-time constraints. Enforcement happens through review, not runtime gating.
- **It does not replace `ownership-boundaries.md`.** Ownership is about *what work* a skill does; tool access is about *which tools* it uses to do that work. Both matter, both are declarative.
- **It does not replace `escalation-rules.md`.** Escalation is about high-risk *categories of work* (auth, payments, etc.) regardless of skill; tool access is about *which tools per skill*.

---

## Routing Integration

When the orchestrator builds a Route Receipt (per `routing-decision-tree.md`), it should now include a Tool Surface section:

```
Route Receipt
─────────────────────────────────────────────
Request:        [task]
Classification: [type] | [surface] | [user-impact] | [risk] | [reversibility]
Primary route:  [letter]
Skills selected: [phase-by-phase list]
Tool surface required: [union of allowed tools across all skills in the chain]
Tool surface flagged: [any tool that triggers escalation per high-risk table above]
Evidence required: [...]
```

This makes the trust surface visible at routing time, before any skill executes.

---

## Updating the Matrix

This matrix evolves with Dharma. Update it when:

- A new skill is added (add row to per-skill overrides if it deviates from layer default)
- A skill's scope materially changes (update its row)
- A new tool appears in Claude Code (add to Tool Categories; review impact on skills)
- A new MCP plugin is installed (document in Layer 0+ section of skills-inventory.md)
- A review finding surfaces a tool that should have been forbidden

Treat this matrix as a living document, not a one-time declaration.

---

*Last updated: 2026-05-04*
*Maintained alongside `ownership-boundaries.md` and `escalation-rules.md` — together these three files form Dharma's governance triangle: WHAT (ownership), WHEN (escalation), HOW (tool access).*
