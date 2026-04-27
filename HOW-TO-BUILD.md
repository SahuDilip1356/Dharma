# How to Build Dharma From Scratch

A reverse-engineered guide to recreating this framework — the reasoning behind every layer, the order they were built, and the decisions made at each stage.

If you follow this guide, you will arrive at the same architecture. More importantly, you will understand *why* it is structured this way — which means you can adapt it confidently for your own context.

---

## The Founding Problem

Before writing a single skill, you need to be clear about what problem you are solving.

AI coding assistants — Claude, GPT, Copilot — are fast and capable. Left unstructured, they are also undisciplined. They will:

- Skip design thinking and produce technically correct but unusable UI
- Claim completion based on belief ("I think this should work") rather than evidence
- Write tests after the code, which defeats the purpose of testing
- Over-engineer solutions — adding abstractions, introducing dependencies, expanding scope
- Ship AI-powered features without any adversarial testing or safety validation
- Miss accessibility entirely on user-facing screens

These are not model failures. They happen because the model is following the path of least resistance: write code, say it's done, move on.

**The problem Dharma solves:** AI-assisted development needs the same structural discipline that good engineering teams apply — classification before action, design before code, tests before implementation, evidence before completion. Without this, speed becomes liability.

---

## The Core Principles (Decide These First)

Before building any skill, decide on your non-negotiable principles. These will shape every decision.

The five principles Dharma was built on:

**1. Evidence over assertion**
The framework will never allow "done" without proof. This principle alone rules out hundreds of lazy patterns — skipping test runs, claiming tests pass from memory, saying "should work."

**2. Specialization over generalization**
Each skill has one primary responsibility and explicit boundaries on what it does NOT own. This prevents scope creep and makes the framework predictable.

**3. Gate before advancing**
Phases are sequential. A phase cannot start until the previous phase has exit evidence. This makes quality a structural requirement, not a suggestion.

**4. Governance before complexity**
When you have many skills, the failure mode shifts from "not enough capability" to "capability applied incorrectly." Build governance last — you need the skills before you can define their boundaries.

**5. AI features are production systems**
LLM-powered features have unique failure modes. They require their own economics, safety gates, observability, and governance. Do not treat them as ordinary features.

Write these principles down before building. They will prevent bad decisions when individual skill design gets ambiguous.

---

## Phase 1: Build the Orchestrator Skeleton First

**Why first:** Everything else depends on the orchestrator. It is the control tower — without it, you have a collection of skills with no routing logic.

### What the orchestrator needs at minimum

The orchestrator skeleton requires:

1. **Work type taxonomy** — A complete list of what types of work exist (new-product, new-feature, bug-fix, refactor, performance, security, integration, release, etc.). Be exhaustive here. Missing a work type means that type of work gets misrouted.

2. **Route table** — Map each work type to a letter (Route A, B, C...). The routes are not arbitrary — they reflect genuinely different phase sequences and evidence requirements.

3. **Phase sequence** — Define the phases. Dharma uses 6: Intent → Design → Plan → Build → Verify → Finish. The names matter less than the principle: each phase has entry criteria and exit evidence.

4. **Completion language** — Define exactly 5 valid ways to claim something is done. Constrained completion language is one of the highest-leverage design decisions in the framework.

### What NOT to build yet

At this stage, do not build governance files (routing decision tree, ownership boundaries, evidence ledger). You do not know what to govern until you have the skills. Build the skeleton; fill in governance in Phase 6.

### Files to create

```
00-lifecycle-orchestrator/
  SKILL.md              ← master orchestrator
  routing-matrix.md     ← route → skills → evidence
  phase-gates.md        ← entry/exit criteria per phase
  evidence-contract.md  ← what counts as valid evidence
  escalation-rules.md   ← when to stop and escalate
  skills-inventory.md   ← functional name → actual skill file
```

---

## Phase 2: Engineering Discipline Layer

**Why second:** Before you can build execution methodology, you need to define how engineers should think. The discipline layer answers: what makes an engineer approach a problem correctly?

These are the hardest skills to write because they are about restraint, not capability. An AI assistant needs to be told what NOT to do as much as what to do.

### The 4 disciplines to encode

**Think before coding** — Surface all assumptions before touching code. What are we assuming about the data model? About the API contract? About the user's behavior? Assumptions that go unstated become bugs.

**Simplicity first** — Start with the minimum implementation that could work. Do not add abstractions, helpers, or future-proofing until you need them. Three similar lines is better than a premature abstraction.

**Surgical changes** — Minimize blast radius. Every change should touch the minimum number of files and functions required. A bug fix that also refactors unrelated code is two changes — do them separately.

**Karpathy discipline** — A master skill that combines all four principles attributed to Andrej Karpathy: avoid complexity, avoid dependencies, start simple, write tests. This is the umbrella; the other three are specializations.

### How to write discipline skills

Discipline skills need three things:
1. A positive statement of the principle ("start simple — implement the minimum that works")
2. A negative statement of what it forbids ("do not add abstractions before you have three concrete cases")
3. Anti-patterns with specific examples — "this is what it looks like to violate the rule"

Without the negative statements and anti-patterns, discipline skills become aspirational rather than actionable.

---

## Phase 3: Execution Methodology Layer

**Why third:** You have principles (discipline). Now you need process. The execution methodology layer defines how work moves from idea to shipped code.

### The design insight

The key insight in designing this layer: **execution methodology is not a single skill — it is a family of phase-specific skills.** One master skill (`superpowers`) defines the overall 6-phase cycle. Each phase gets its own specialist sub-skill.

This matters because a bug-fix task does not need the brainstorm skill. A refactor does not need the debug skill. By splitting the methodology into phase-specific sub-skills, the orchestrator can invoke only what's relevant.

### The 8 sub-skills and what each resolves

| Sub-skill | Phase | What it resolves |
|---|---|---|
| `superpowers-brainstorm` | Pre-Phase 2 | The "we jumped straight to implementation" problem |
| `superpowers-write-plan` | Phase 2 | The "we started coding without a plan" problem |
| `superpowers-tdd` | Phase 3 | The "tests written after code don't prevent bugs" problem |
| `superpowers-execute` | Phase 3 | The "sequential execution when parallel is possible" problem |
| `superpowers-debug` | Phase 0 | The "we fixed the symptom, not the root cause" problem |
| `superpowers-verify` | Phase 4 | The "done means I believe it works" problem |
| `superpowers-finish` | Phase 5 | The "code is done but nothing is merged" problem |

### The most important skill in this layer

`superpowers-verify` is the most important skill in the framework. It encodes the principle that evidence precedes any completion claim. Every time the framework is tempted to say "done", this skill fires. It demands:

1. Name the exact command that proves your assertion
2. Run it fresh
3. Read the full output
4. Validate that the output actually supports the claim
5. Report with the evidence

Without this skill, the entire framework can be bypassed by confident-sounding assertions.

---

## Phase 4: Product & Planning Layer

**Why fourth:** You might expect this layer to come first — isn't planning before execution obvious? In practice, build the execution machinery first. When you design planning skills, you need to know what the execution layer can absorb and act on. Planning skills that produce outputs the execution layer can't consume are useless.

### The 5 planning sub-skills

**`churney-os`** — The founder-level framework. It answers the deepest questions before any engineering starts: What is the problem? Who has it? Why do they have it? What is the solution? What does success look like? This is Phase 0 for new products.

**`goal-driven-execution`** — For existing products adding features. Scoped to a single feature: what is the goal, what are the success criteria, what is explicitly out of scope, and how will we verify we achieved it?

**`pm-prd`** — Produces an 8-section product requirements document. Use when stakeholders need formal documentation of requirements.

**`pm-user-stories` / `pm-job-stories`** — Acceptance criteria in two formats: user-role-based stories ("As a clinic manager, I want to...") or job-to-be-done format ("When I have patients who keep missing appointments, I want to..."). Both are valid; choose based on what resonates with your team.

**`pm-prioritization`** — Opportunity Score, ICE, or RICE scoring for feature prioritization. Use when you have a backlog and need a structured way to sequence work.

### The key design rule for this layer

Planning skills produce artifacts — goals, criteria, requirements, stories. These artifacts must be written in a format that the execution layer can consume directly. Do not design planning outputs that require translation before implementation can begin.

---

## Phase 5: Experience Quality Layer

**Why fifth:** You have a working framework for backend and API work. Now add the UX layer. This layer is the most expensive to skip — user-facing quality failures are visible to every user.

### Why this layer requires 10 skills

UX quality is not one concern — it is a stack of distinct concerns that are easy to conflate:

```
What to build (UX intent)           → uiux-designer
How it should look (visual)         → uiux-design-intelligence
What components to use (system)     → uiux-frontend-design-system
Can everyone use it (accessibility) → uiux-accessibility-review
Does it work on all screens (size)  → uiux-responsive-review
How does it feel to use (motion)    → uiux-interaction-review
Is the copy correct (language)      → uiux-audit
Does it match the design (QA)       → uiux-design-qa
Is the React code correct           → uiux-react-patterns
```

Combining these into a single "do good UX" skill produces a skill that is too vague to be actionable and too broad to have clear exit criteria. Each skill needs its own pass/fail definition.

### The UX gate rule

The most important architectural decision in this layer: **Phase 1 is mandatory for all user-facing work.** Not recommended. Not conditional. Mandatory.

This rule prevents the most common UX failure mode: implementation begins without defined states. What does the empty state look like? The loading state? The error state? Without Phase 1 forcing these questions before code is written, empty states get shipped as blank screens and error states get shipped as raw exception messages.

### The ownership discipline in this layer

Because there are 10 related skills, the ownership boundaries are critical here. The key rules:
- `uiux-accessibility-review` owns WCAG and keyboard navigation — NOT responsive layout
- `uiux-responsive-review` owns breakpoints — NOT accessibility
- `uiux-interaction-review` owns state transitions and motion — NOT visual direction
- `uiux-audit` handles copy and label quality — NOT deep a11y or responsive QA

When a skill discovers an issue outside its boundary, it reports it as a follow-up or risk — it does not absorb it.

---

## Phase 6: Governance Layer (Build This Last)

**Why last:** You cannot define boundaries until you have the things to bound. The governance layer is the hardest to design and the most important to get right.

### The four governance controls and why each exists

**1. Routing Decision Tree**

The routing matrix tells you what each route looks like once selected. The routing decision tree tells you HOW to select a route deterministically.

Without a decision tree, routing is a judgment call. Judgment calls are inconsistent. The decision tree converts routing into a 7-step algorithm with a defined first-match winner. The most important design decision: **risk surface area comes first.** If a task touches auth, payments, AI, or compliance — that check happens before anything else, regardless of work type.

**2. Ownership Boundaries**

As your skill count grows, the failure mode shifts. The risk is no longer "we don't have a skill for this" — it's "this skill absorbed responsibility that belongs to another skill, creating gaps and overlaps."

Ownership boundaries solve this with two columns: what a skill Owns and what it Does NOT Own. The "Does NOT Own" column is the innovation. Most frameworks only define what skills do. Defining what they explicitly do not do prevents scope creep.

**3. Evidence Ledger**

The evidence contract (Phase 1 orchestrator file) defines what counts as valid evidence. The evidence ledger makes that contract mandatory per task, not just aspirational.

The ledger has two forms:
- **Full ledger** — for medium/high risk tasks: task classification, route receipt, gate-by-gate status, code/runtime/UX/risk evidence, completion status
- **Lightweight ledger** — for low-risk, easily reversible tasks: one-line classification, command run, evidence cited, completion status

The lightweight form prevents ledger overhead from being the reason teams skip it.

**4. Golden Examples**

Rules tell the orchestrator what is allowed. Examples show it what a correct decision looks like.

Include examples that stress-test the governance:
- A high-risk feature (tests the risk-first rule in the decision tree)
- A refactor touching dangerous surfaces (billing — tests stop conditions)
- A release (tests the minimum viable release checklist)
- A feature that touches multiple routes (tests the tie-breaker rule)

8 examples is enough. More than 10 adds noise without adding coverage.

---

## Phase 7: AI & Economics Layer

**Why seventh:** This layer is optional until you are shipping AI features. When you are, it becomes mandatory. Do not build it before you have production AI features to govern — the skills will be too abstract to design well.

### The conflict-prevention work

Before building any skill in this layer, explicitly resolve the overlaps with existing skills:

**Overlap 1:** `inference-economics` (Phase 2, plan the cost envelope) vs `ai-safety-eval` Step 6 (Phase 3, validate that built system meets cost constraint). Same topic, different jobs. Resolve by phase: economics sets the ceiling; safety eval validates it. Document this split in `ownership-boundaries.md` before writing either skill.

**Overlap 2:** `benchmark-framework` (post-ship, scheduled regression tracking) vs `ai-safety-eval` Step 4 (pre-ship, one-time hallucination gate). Same metric, different cadence. Resolve by timing: safety eval is a snapshot; benchmarks are a trend. Document this split before writing.

If you write these skills without resolving the overlaps first, teams will use whichever skill they encounter first and skip the other — creating inconsistent coverage.

### The build order within this layer

```
1. ai-safety-eval     → build first; it is the pre-ship gate that all other skills reference
2. inference-economics → Phase 2 dependency; needed when designing any AI feature
3. prompt-optimization → Phase 3 dependency; needed when preparing prompts for production
4. ai-observability   → Phase 5 dependency; needed before any AI feature goes live
5. model-governance   → build when 2+ AI features are live
6. benchmark-framework → build when 3+ AI features are live
```

Do not build model-governance and benchmark-framework until you have the live features to govern. Building them too early produces skills designed for hypothetical scenarios rather than real production systems.

---

## How to Extend the Framework

The pattern for adding a new skill without breaking existing ones:

### Step 1: Define the scope precisely

Before writing any content, answer:
- What problem does this skill solve that no existing skill covers?
- What does it own?
- What does it explicitly NOT own? (Name the existing skill that owns adjacent concerns.)

If you cannot answer all three questions clearly, do not add the skill. The problem may be covered by extending an existing skill.

### Step 2: Check for conflicts

Search `ownership-boundaries.md` for any skill that might overlap with the new skill's scope. Resolve conflicts by phase, timing, or responsibility — and update `ownership-boundaries.md` before writing the new skill file.

### Step 3: Write the SKILL.md

Every skill file follows the same structure:
1. **Frontmatter** — name, description (when it triggers), license, metadata
2. **Core rule** — one sentence that states the non-negotiable principle
3. **The process** — numbered steps with concrete outputs at each step
4. **What "done" looks like** — an example of correct output with evidence
5. **When to skip** — explicit statement that there is no when-to-skip (or the rare exceptions)
6. **Anti-patterns** — what violations of this skill look like

The "When to skip" section is the most important part of a safety or gate skill. If it says "when pressed for time, you can skip step 3", the skill will always be skipped under time pressure. State the skip conditions explicitly and narrowly.

### Step 4: Register the skill

Update three files:
- `skills-inventory.md` — add the functional name → actual skill mapping
- `routing-matrix.md` — add the skill to the routes where it applies
- `ownership-boundaries.md` — add the skill's ownership row

### Step 5: Add a golden example

If the new skill introduces a non-obvious routing decision or ownership boundary, add a golden example to `examples/`. The example should show a scenario that would be misclassified without the new skill.

---

## What You End Up With

Following this 7-phase build sequence, you arrive at:

| Component | Count | Purpose |
|---|---|---|
| Skill layers | 5 | Product planning, engineering discipline, execution methodology, experience quality, AI & economics |
| Skills | 33 | Specialist capabilities invoked at specific phases |
| Routes | 8 | Deterministic work-type-to-skill-sequence mappings |
| Governance files | 7 | Routing decision tree, ownership boundaries, phase gates, evidence contract, evidence ledger, escalation rules, golden examples |
| Golden examples | 8 | Reference scenarios covering the full risk spectrum |

The framework is complete when:
- Every work type has a route
- Every route has a skill sequence and evidence requirements
- Every skill has defined ownership and explicit non-ownership
- Every task produces a Route Receipt before work begins
- Every completion claim is backed by cited evidence

---

## The Design Mistake to Avoid

The most common failure mode when building a framework like this: **adding skills to solve problems that governance would solve better.**

When you notice a quality problem — UX skills being used for accessibility work, or planning skills being used for technical architecture — the instinct is to add a new skill. Usually the right answer is to update `ownership-boundaries.md` and the routing decision tree.

More skills increase the burden of skill selection. Better governance makes skill selection deterministic. When in doubt: can a governance file fix this? If yes, use governance. If no, add a skill.

---

*This guide was written by reconstructing the decisions made during Dharma's development. The 7-phase build sequence reflects the order in which the framework became internally consistent — not the order in which the best first guess would have built it.*
