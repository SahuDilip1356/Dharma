# Lead Agent Final Evaluation

The CEO-pattern: a final-evaluation role that synthesizes outputs from all sub-agents (skills) used in a task and makes the explicit go/no-go call before "done" can be claimed. Closes Gap #4 from `agent-architecture.md` — the Multi-Agent Architecture's "Lead Agent (CEO) Final Evaluation" component.

> **Reframe of an existing capability.** The orchestrator already validates evidence-contract compliance at task end. This file makes that step explicit, names it, and gives it a structured output. Same work, formal protocol.

---

## Why this exists

A multi-agent system without a designated final-evaluator suffers from "everyone signed off, no one looked at the whole." Each skill verifies its own piece. No skill steps back to ask: *did the work as a whole meet the original goal?*

The Lead Agent role:

- **Synthesizes** — reviews outputs across every skill in the chain, not piece-by-piece
- **Validates** — confirms each evidence-contract requirement is met
- **Cross-checks** — looks for inconsistencies between skill outputs (e.g., plan said X, executed Y)
- **Decides** — explicit GO / CONDITIONAL GO / NO-GO with rationale
- **Records** — writes the final evaluation entry to the evidence ledger

The Lead Agent does NOT do the work. It evaluates that the work was done correctly.

---

## When the Lead Agent runs

The orchestrator invokes the Lead Agent at:

| Trigger | Phase |
|---|---|
| All planned skills in the route have produced exit evidence | End of Phase 4 (Verify) |
| All applicable release gates have passed (G6, G6.5, G7) | End of Phase 5.5/5.7 |
| User asks "is this done?" or "ship it" | Any time, on demand |
| Before any commit message claims feature complete | Pre-commit hook (when this skill is wired in) |

The Lead Agent is the LAST step before any "done" claim leaves Dharma's mouth.

---

## What the Lead Agent reads

To evaluate, the Lead Agent reads:

```
1. The original Route Receipt (Phase 0 output)
   - Original goal, success criteria, scope, risk classification

2. The full evidence ledger for this task
   - Every skill's exit evidence (per skill in the route)
   - G6/G6.5/G7 gate results if applicable
   - Block conditions encountered (and how they resolved)

3. The active project memory
   - decisions.md entries created during this task
   - learnings.md entries created during this task
   - STATE.md current state

4. The artifacts produced
   - Code files changed (paths only, not full content unless flagged inconsistent)
   - Documents written
   - Configuration changes
```

---

## Evaluation Protocol

### Step 1: Reconfirm the original goal

Open the Route Receipt. State the goal in one sentence. If you cannot restate it cleanly, the goal was unclear from the start — flag this even at evaluation time.

### Step 2: Walk the evidence ledger

For each phase that ran, confirm:

| Phase | Required evidence | Found in ledger? | Notes |
|---|---|---|---|
| 0 — Intent | Goal/success/risk/reversibility recorded | ✅/❌ | |
| 1 — UX (if user-facing) | Flow + states + accessibility plan | ✅/❌ | |
| 2 — Plan | Assumptions + files + plan + tests | ✅/❌ | |
| 3 — Build | TDD RED→GREEN + scope note | ✅/❌ | |
| 4 — Verify | Tests + build + UI checks if user-facing | ✅/❌ | |
| 5 — Finish | Summary + remaining risks + next step | ✅/❌ | |
| 5.5 — G6 | `/review` clean | ✅/❌/N/A | |
| 5.5 — G6.5 | `/ultrareview` clean (if high-risk) | ✅/❌/N/A | |
| 5.7 — G7 | SME approval written (if regulated content) | ✅/❌/N/A | |

### Step 3: Cross-skill consistency check

Look for these failure modes that single-skill verification cannot catch:

- **Plan-execution drift:** Does the executed work match the plan? Files in plan = files actually changed?
- **Goal-output drift:** Does the final output achieve the original goal? Or did the goal silently shift?
- **Evidence-claim mismatch:** Does any skill's evidence contradict another's? (e.g., verify says tests pass but build evidence shows failures)
- **Scope creep:** Were files modified that weren't in the plan? Justified or not?
- **Surface-area drift:** Did the implementation touch surfaces not classified at Phase 0? (e.g., classified `internal` but actually touched user-facing code)

### Step 4: Make the call

Output ONE of these verdicts with explicit rationale:

```
✅ GO — Ship it
   - All evidence present
   - All gates passed
   - No cross-skill inconsistencies
   - Goal achieved as stated

⚠️ CONDITIONAL GO — Ship with documented limitations
   - All critical evidence present
   - One or more gates produced findings that were accepted with rationale
   - Specific risks remain and are documented
   - User has explicitly accepted the conditions

⏳ HOLD — Not ready to ship
   - Specific evidence missing: [list]
   - Specific gate failed: [list]
   - Specific inconsistency found: [list]
   - Required action before re-evaluation: [list]

❌ NO-GO — Should not ship in current state
   - Critical evidence missing or conflicting
   - Critical gate failed without acceptable resolution
   - Goal NOT achieved
   - Required redirection: [back to Phase X / replan / abandon]
```

### Step 5: Write the Final Evaluation entry

Append to `[project]/memory/decisions.md`:

```markdown
## [YYYY-MM-DD] Final Evaluation: [task name]

**Verdict:** ✅ GO | ⚠️ CONDITIONAL | ⏳ HOLD | ❌ NO-GO
**Goal:** [from Route Receipt]
**Outcome:** [one sentence — what was actually built/changed]

**Evidence summary:**
- Phase 0–5 evidence: [✅ complete | ❌ gaps in: list]
- Release gates: [G6 ✅ | G6.5 ✅/N/A | G7 ✅/N/A]
- Cross-skill consistency: [✅ clean | findings: list]

**Conditions or limitations** (if conditional):
- [list]

**Rationale:** [2-3 sentences — why this verdict]

**Lead Agent:** [orchestrator OR named human reviewer if final sign-off required]
```

---

## When the Lead Agent escalates to a human

The orchestrator-as-Lead-Agent works for most tasks. ESCALATE to a human Lead Agent (typically Dilip himself or a designated approver) when:

| Condition | Escalation reason |
|---|---|
| Risk level = `critical` from Phase 0 | Critical decisions need human sign-off |
| Verdict is CONDITIONAL with material conditions | Human must accept conditions explicitly |
| Cross-skill inconsistency found | Judgment call — automated logic isn't enough |
| First-time deployment to production | Pre-flight human gate |
| Public-facing release at scale | PR/comms judgment beyond technical evaluation |

When escalating, the Lead Agent produces the same evidence summary but ends with:

```
🔼 ESCALATED to: [human name]
Required action: [explicit ask — review the bundle, sign off in writing, accept conditions]
Awaiting response.
```

---

## Lead Agent vs. orchestrator vs. SME

Three distinct evaluation roles, each with a different question:

| Role | Question answered | Scope |
|---|---|---|
| **Orchestrator** | "Did each skill do its job?" | Per-skill correctness |
| **Lead Agent** | "Did the work as a WHOLE meet the goal?" | End-to-end across the chain |
| **SME (G7)** | "Is this domain-correct?" | Domain-specific (legal, medical, etc.) |

Each catches a different class of failure. None replaces the others.

---

## What Lead Agent does NOT do

- **Re-do the work.** It evaluates; it does not redirect, refactor, or rewrite.
- **Override SME findings.** If G7 says no, Lead Agent cannot say yes.
- **Skip evidence requirements.** It enforces them; it does not waive them.
- **Make subjective design calls.** It checks evidence and consistency; subjective preferences belong to the user/founder.

---

## Common failure modes (and how this role prevents them)

| Failure | Without Lead Agent | With Lead Agent |
|---|---|---|
| Each skill signed off, but no one read the whole | Result diverges from goal silently | Lead Agent re-grounds against goal |
| Plan said 3 files, build touched 12 | Scope creep accepted as fait accompli | Cross-skill check surfaces drift |
| Tests pass but goal not achieved | "Done" claimed prematurely | HOLD verdict; redirect to plan |
| Conditional gate findings ignored | Conditions silently dropped | Conditional verdict requires explicit acceptance |
| Critical risk classification but no human approval | Auto-shipped | Escalation to human Lead Agent |

---

## Integration with existing files

| File | How Lead Agent uses it |
|---|---|
| `routing-decision-tree.md` | Reads original Route Receipt to recall goal + classification |
| `phase-gates.md` | Walks evidence per phase; checks every gate's exit criteria |
| `evidence-contract.md` | Confirms evidence types match contract requirements |
| `evidence-ledger-template.md` | Writes Final Evaluation as a row in the ledger |
| `escalation-rules.md` | Knows when to escalate to human Lead Agent |
| `sme-review-gate.md` | Confirms G7 evidence if applicable; does NOT replace it |
| `tool-access-matrix.md` | Audits whether tool calls stayed within declared access |

---

## Why this role exists

A multi-agent system needs a final synthesizer. Without one, the system can produce technically-correct sub-outputs that don't add up to the right whole. Lead Agent is the last check that the work actually achieved what was asked, not just that each skill did its piece.

This is why Kedar's framework names the Lead Agent (CEO) explicitly: in human organizations, the executive role isn't to do the work — it's to evaluate that the work was done correctly. Same principle applies in multi-agent product systems.

---

*Last updated: 2026-05-04*
*Maintained alongside the rest of the orchestrator governance files. Lead Agent runs at end-of-task; routes to human escalation when criteria warrant it.*
