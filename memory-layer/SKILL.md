---
name: memory-layer
description: |
  Cross-cutting Memory Layer — loads project context before every Dharma skill and
  captures durable outputs after. The "two-drawer" filing system: global memory
  (founder identity, build patterns, Dharma rules) always loads; project memory
  (decisions, learnings, deployment state) loads based on the active project folder.

  Activation: automatic — pre-flight runs before every Dharma skill; post-flight
  runs after if the skill produced a durable output (decision, learning, deployment).
  Not invoked directly by the user.

  Pre-flight (READ):
  - Load global memory: Product Dev/memory/*.md (always)
  - Detect active project from cwd or nearest CLAUDE.md / memory/ folder
  - Load project memory: [project]/memory/*.md (relevant slices per skill type)
  - If project memory is >7 days stale, surface a warning before proceeding

  Post-flight (WRITE — only when triggered):
  - Decision made → append to [project]/memory/decisions.md
  - Failure pattern identified → append to [project]/memory/learnings.md
  - Deployment completed → update [project]/memory/deployment-pipeline.md
  - Exploratory/research only → no write

license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Memory Layer — Dharma Cross-Cutting Context System

You are operating the Memory Layer. This is not a skill in the traditional sense —
it is a wrapper protocol that runs before and after every Dharma skill invocation.

---

## The Two-Drawer Model

```
┌─────────────────────────────────────────────────────────────────────┐
│  TOP DRAWER — GLOBAL (always open, every project)                   │
│  Product Dev/memory/                                                 │
│  ├── founder.md            Who Dilip is, how he builds              │
│  ├── patterns.md           Build patterns that apply across all     │
│  ├── tools-and-skills.md   All tools and Dharma skills built        │
│  └── MEMORY.md             Global memory index                      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│  BOTTOM DRAWER — PROJECT (opens for the active project only)        │
│  [project-root]/memory/                                             │
│  ├── MEMORY.md             Project memory index + last-updated      │
│  ├── decisions.md          Decisions made + rationale               │
│  ├── learnings.md          What failed, what worked                 │
│  └── deployment-pipeline.md  How this project ships                 │
└─────────────────────────────────────────────────────────────────────┘
```

**Global drawer** = founder identity, build philosophy, cross-project patterns.
Never changes per project. Always loaded first.

**Project drawer** = specific decisions, failures, deployment state for THIS project.
Starts empty on new projects. Fills as work accumulates.

---

## Pre-Flight Protocol (READ)

Runs automatically before every Dharma skill executes.

### Step 1: Load Global Memory

Always load these before any skill:

| File | What it provides |
|---|---|
| `Product Dev/memory/founder.md` | Working style, principles, communication preferences |
| `Product Dev/memory/patterns.md` | Recurring build patterns and pitfalls across all projects |
| `Product Dev/memory/tools-and-skills.md` | Available tools, what's been built |

### Step 2: Detect Active Project

1. Check current working directory
2. Walk up the tree — find the nearest `CLAUDE.md` or `memory/` folder
3. That folder's parent is the active project root
4. If ambiguous: ask — *"Which project are we working on?"*

### Step 3: Load Project Memory (selective slices)

Load only what the invoked skill needs — not the full memory dump:

| Skill category | Load these project files |
|---|---|
| Planning (`churney-os`, `pm-prd`, `goal-driven-execution`) | `decisions.md`, `product-context.md` |
| Engineering (`karpathy-discipline`, `execute`, `tdd`) | `decisions.md`, `learnings.md` |
| Debug (`superpowers-debug`) | `learnings.md`, `patterns.md` |
| Ship (`superpowers-finish`, `superpowers-verify`) | `deployment-pipeline.md`, `decisions.md` |
| Design (`uiux-designer`, `frontend-design`) | `product-context.md`, `decisions.md` |
| AI features (`inference-economics`, `ai-safety-eval`) | `decisions.md`, `product-context.md` |

### Step 4: Staleness Check

Check the `<!-- Last updated: YYYY-MM-DD -->` timestamp in project `MEMORY.md`.

If last updated **> 7 days ago**:
> ⚠️ **Memory Warning:** Project memory last updated [DATE] ([N] days ago).
> Context may be stale. Proceeding with existing memory.
> Run `/memory-sync` to refresh if significant changes have been made since then.

**Do NOT block** — warn once, then proceed. Staleness is a signal, not a gate.

---

## Post-Flight Protocol (WRITE)

Runs after the Dharma skill completes. Write only when the skill produced something
durable. Most runs produce no write — that is correct behaviour.

### Write Triggers

| What happened | Write target | Entry format |
|---|---|---|
| A product or architecture decision was made | `[project]/memory/decisions.md` | `- [DATE] Decision: ... Rationale: ... Alternative: ...` |
| A failure pattern was identified or confirmed | `[project]/memory/learnings.md` | `- [DATE] What failed: ... Why: ... Fix applied: ...` |
| A deployment completed | `[project]/memory/deployment-pipeline.md` | Update the relevant section inline |
| A new tool or skill was built | `Product Dev/memory/tools-and-skills.md` | `- [DATE] [Tool name] — description` |

### No-Write Conditions (skip cleanly)

- Research-only or exploratory sessions with no outcome
- Bug fixes already covered by an existing `learnings.md` entry
- Tasks where no new decision was made
- Brainstorming that didn't result in an approved path

---

## New Project Initialization

When Dharma is invoked in a project with no `memory/` folder:

1. Create `[project-root]/memory/` directory
2. Create `MEMORY.md` with timestamp, project name, and section stubs
3. Create `decisions.md` with header
4. Create `learnings.md` with header
5. Create `deployment-pipeline.md` with header
6. Confirm to user:
   > Memory initialized for [project]. Global memory loaded.
   > Project memory starts empty — it will fill as decisions and learnings accumulate.

---

## Full Invoke Sequence

```
User invokes Dharma skill
        ↓
Memory Layer PRE-FLIGHT
  → Load global memory (always)
  → Detect active project
  → Load relevant project memory slices
  → Check staleness — warn if >7 days
        ↓
Lifecycle Orchestrator
  → Routing decision tree
  → Route receipt
  → Skill sequence + phase gates
        ↓
Memory Layer POST-FLIGHT
  → Decision made? → write to decisions.md
  → Failure identified? → write to learnings.md
  → Deployment done? → update deployment-pipeline.md
  → Otherwise → no write
        ↓
Done
```

---

## What Memory Layer Does NOT Own

- The memory files themselves — they belong to the project, not to Dharma
- What to build or prioritize — that is Layer 1 (Product & Planning)
- Commit messages or PR descriptions — that is `superpowers-finish`
- The manual `/memory-sync` command — that stays as a human-triggered force-sync
  for capturing a full session's worth of context outside of skill execution

---

## Memory File Structure Per Project

```
[project-root]/
  memory/
    MEMORY.md                ← index + last-updated timestamp
    decisions.md             ← architecture and product decisions
    learnings.md             ← failure patterns and what worked
    deployment-pipeline.md   ← how this project ships (CI/CD, env, gotchas)
    product-context.md       ← product vision, personas, features (optional)
```

Start with `MEMORY.md`, `decisions.md`, and `learnings.md`.
Add `deployment-pipeline.md` when the project first ships.
Add `product-context.md` when the product definition is stable.

---

## Relationship to memory-sync Skill

| | `memory-sync` | `memory-layer` |
|---|---|---|
| **Trigger** | Human — `/memory-sync <summary>` | Automatic — wraps every skill |
| **Scope** | Full session capture | Skill-level, selective |
| **When to use** | After a long session, major sprint, or debugging run | Always (background) |
| **Writes** | Everything accumulated in session | Only what the current skill produced |

They are complementary. `memory-layer` keeps memory current automatically.
`memory-sync` is the manual override for bulk captures and session closures.
