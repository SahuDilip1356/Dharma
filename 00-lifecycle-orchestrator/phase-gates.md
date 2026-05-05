# Phase Gates

Entry criteria and exit evidence for each phase.
A phase cannot start until the previous phase's exit evidence exists.

---

## Phase 0: Intent Gate
**Purpose:** Establish what we're building and why before anything else.
**Applies to:** All work types.

### Entry Criteria
- A request exists (any form — idea, ticket, complaint, instruction)

### Checklist
- [ ] User identified (who is affected or benefits)
- [ ] Problem identified (what pain or gap exists)
- [ ] Desired outcome defined (what success looks like)
- [ ] Non-goals stated (what this will NOT do)
- [ ] Success criteria defined (measurable, not vague)
- [ ] Risk level classified
- [ ] Reversibility classified

### Exit Evidence
```
Goal: [one sentence]
User: [who]
Success: [measurable criteria]
Out of scope: [explicit cuts]
Risk: [low | medium | high | critical]
Reversibility: [easy | moderate | hard]
```

### Block Condition
Do not advance to Phase 1 if:
- Goal is contradictory or undefined
- Risk is `critical` without explicit user approval
- Destructive action requested without confirmation

---

## Phase 1: UX Gate
**Purpose:** Define user experience intent before design or code.
**Applies to:** All user-facing work (mandatory). Optional for internal/backend-only.

### Entry Criteria
- Phase 0 exit evidence exists

### Checklist
- [ ] User flow defined (steps the user takes)
- [ ] Primary action identified (the one thing the screen/feature must do well)
- [ ] Information hierarchy clear (what's most important, what's secondary)
- [ ] All states designed: empty / loading / error / success / disabled
- [ ] Accessibility concerns identified (contrast, keyboard, ARIA, semantic HTML)
- [ ] Responsive behavior planned (mobile / tablet / desktop breakpoints)
- [ ] Visual direction selected (style, colors, fonts via `uiux-design-intelligence`)

### Exit Evidence
```
User flow: [steps or screen names]
Primary action: [one thing]
States covered: empty ✅ / loading ✅ / error ✅ / success ✅
Accessibility notes: [key concerns]
Responsive plan: [behavior at 375 / 768 / 1280px]
Visual direction: [style name + color + font]
```

### Block Condition
Do not advance to Phase 2 if:
- User-facing feature has no defined states (empty/error/success)
- Accessibility has not been considered at all
- No visual direction has been chosen (no style + color decision)

---

## Phase 2: Planning Gate
**Purpose:** Produce a verifiable implementation plan before writing code.
**Applies to:** All work types except `release` and `research-only`.

### Entry Criteria
- Phase 0 exit evidence exists
- Phase 1 exit evidence exists (if user-facing)

### Checklist
- [ ] Assumptions listed (all implicit choices named)
- [ ] Files / components likely affected identified
- [ ] Risks listed (what could go wrong)
- [ ] Implementation steps defined (2–5 min each, independently verifiable)
- [ ] Test approach defined (what tests will prove this works)
- [ ] Dependencies identified (what must exist before this can run)

### Exit Evidence
```
Assumptions: [list]
Files affected: [list]
Risks: [list]
Plan: [numbered steps with verify: checks]
Test approach: [unit | integration | e2e | manual]
```

### Block Condition
Do not advance to Phase 3 if:
- No implementation plan exists for non-trivial work
- High-risk work has no test approach defined

---

## Phase 3: Build Gate
**Purpose:** Enforce discipline during implementation.
**Applies to:** All work types that produce code or design output.

### Entry Criteria
- Phase 2 exit evidence exists (plan)

### Checklist
- [ ] Smallest viable change — no over-engineering
- [ ] No speculative abstractions added
- [ ] No unrelated code modified (surgical changes)
- [ ] Existing behavior preserved unless explicitly changing it
- [ ] TDD followed: failing test written before production code
- [ ] User-facing changes follow design direction from Phase 1
- [ ] React patterns followed for frontend work

### Exit Evidence
```
Changed files: [list]
TDD status: RED seen ✅ / GREEN achieved ✅
Scope note: [what was deliberately not changed]
```

### Block Condition
Do not advance to Phase 4 if:
- Production code was written without a failing test first (TDD violation)
- Unrelated files were modified without justification

---

## Phase 4: Verification Gate
**Purpose:** Require evidence before claiming work is done.
**Applies to:** All work types.

### Entry Criteria
- Phase 3 exit evidence exists

### Checklist

**Code verification:**
- [ ] Unit/integration tests run — pass count recorded
- [ ] Build passes (no compile errors)
- [ ] Typecheck passes (if TypeScript)
- [ ] Lint passes

**UI verification (if user-facing):**
- [ ] Accessibility audit run (`uiux-accessibility-review`)
- [ ] Responsive behavior checked at 375 / 768 / 1280 / 1440px
- [ ] All states verified: empty / loading / error / success
- [ ] Keyboard navigation tested (Tab, Enter, Escape)
- [ ] Focus states visible

**Performance verification (if performance work):**
- [ ] Before metric recorded
- [ ] After metric recorded (same method)
- [ ] Improvement confirmed

### Exit Evidence
```
Tests: [N passed / M failed]
Build: ✅ / ❌
Typecheck: ✅ / ❌
UI checks: [accessibility ✅ | responsive ✅ | states ✅]
Screenshots: [attached or described]
Known risks: [list or "none"]
```

### Block Condition
Do not advance to Phase 5 if:
- Tests are failing
- Build is broken
- User-facing work has not been accessibility-checked

---

## Phase 5: Finish Gate
**Purpose:** Clean close — summary, risks stated, next step clear.
**Applies to:** All work types.

### Entry Criteria
- Phase 4 exit evidence exists

### Checklist
- [ ] Summary written (what changed and why)
- [ ] Remaining risks stated (or confirmed none)
- [ ] Next step identified (merge / PR / monitor / follow-up)
- [ ] Worktree / branch cleaned up if applicable
- [ ] memory-sync triggered if decisions were made

### Exit Evidence
```
Summary: [what was built / fixed / changed]
Verified: [evidence reference]
Remaining risks: [list or "none"]
Next: [merge | PR | monitor | follow-up task]
```

---

## Phase 5.5: Release Review Gates

**Purpose:** External code review before merge — bugs caught here are 10× cheaper than bugs caught after release.
**Applies to:** All changes that produce a PR or merge candidate.

### Gate G6: Standard Code Review (`/review`)
**Mandatory for:** Every meaningful change before merge.
**Skip only when:** Pure documentation edit, single-typo fix, or `risk: low` + `reversibility: easy` + `surface area: internal` (all three).

**Entry Criteria**
- Phase 5 Finish Gate evidence exists
- A PR or merge candidate exists

**Action**
- Run `/review` against the current branch or PR
- Wait for results — do not merge in parallel

**Exit Evidence**
```
Command: /review
Findings: [count of issues by severity]
Resolved: [list of fixes applied]
Re-run: ✅ (after fixes) or N/A (no findings)
```

**Block Condition**
- Any finding flagged `bug` or `critical` — must be resolved and re-run
- Cannot merge until G6 returns clean

---

### Gate G6.5: High-Risk Deep Review (`/ultrareview`)
**Mandatory for:** Any change matching the High-Risk Trigger list below.
**Optional for:** Lower-risk changes where the team wants extra confidence.

**High-Risk Trigger List** (any one triggers G6.5)
- Auth, RBAC, session, or identity changes
- Payment flow or financial transaction changes
- Database migrations (schema, data transforms, drops)
- Security-sensitive code (input validation, crypto, secrets handling)
- AI safety changes (model swap, prompt change to user-facing AI feature)
- Production infrastructure (deploy config, networking, IAM)
- Compliance-critical paths (DPDPA, GDPR, HIPAA, PCI, SOC2)

**Entry Criteria**
- G6 (`/review`) has passed
- Risk level from Step 0 classification = `high` or `critical`

**Action**
- Run `/ultrareview` (cloud-based parallel multi-agent deep review)
- Allow time — this is comprehensive, not fast

**Exit Evidence**
```
Command: /ultrareview
Critical findings: [count or "none"]
High findings:     [count or "none"]
Medium findings:   [count or "none"]
Resolved: [list of fixes applied]
Re-run: ✅ (after fixes) or N/A (no findings)
```

**Block Condition**
- ANY critical finding — halt the release; resolve and re-run G6 + G6.5
- High findings — must be either resolved or explicitly accepted with documented rationale in the decision log
- Medium findings — log them for follow-up; do not block release

---

## Phase 5.7: SME Review Gate (G7)

**Purpose:** Domain-expert review for regulated content. See `sme-review-gate.md` for full protocol.
**Applies to:** Changes that touch legal/regulatory, medical, financial, brand-sensitive, or specialized-technical content.

### Gate G7: Human SME Review (`domain expert sign-off`)
**Mandatory for:** Any change matching the SME Trigger list below.
**Distinct from G6/G6.5:** Code review checks engineering quality. SME review checks domain correctness. Both can be required for the same change.

**SME Trigger List** (any one triggers G7)
- Legal/regulatory: privacy policies, ToS, compliance docs (DPDPA, GDPR, HIPAA, PCI, etc.), contracts
- Medical/clinical: any medical claim, dosage, diagnostic content, healthcare data handling
- Financial: investment advice, tax calculations, audit findings, lending decisions
- Brand/PR/Crisis: sensitive public-facing copy, crisis comms, breach disclosures
- Specialized technical: cryptography, safety-critical systems, public AI safety claims

**Entry Criteria**
- G6 (`/review`) has passed
- G6.5 (`/ultrareview`) has passed if applicable
- The work matches at least one SME Trigger above

**Action**
- Package the work for SME review (plain-English summary, specific questions, highlighted concerns)
- Deliver to a NAMED, credentialed SME via documented channel
- Wait for WRITTEN approval (verbal not sufficient)

**Exit Evidence**
```
G7 SME Review:
  SME name + credentials: [name + cert/license]
  Domain: [legal | medical | financial | brand | technical]
  Submitted: YYYY-MM-DD
  Approved: YYYY-MM-DD
  Status: [approved | approved-with-conditions | rejected]
  Conditions resolved: [yes/no]
  Written approval link: [email/doc/ticket URL]
```

**Block Condition**
- Rejected — halt release, address rejection reason, re-submit
- Approved-with-conditions — conditions MUST be resolved before release
- No written approval — cannot pass with verbal-only approval
- For solo founders without in-house SME: see `sme-review-gate.md` for acceptable substitutes (external SME hire, vetted marketplace, or explicit risk acceptance for low-stakes content only)

---

## Phase 5.8: Lead Agent Final Evaluation (G8)

**Purpose:** End-to-end synthesis across all skills used in the task — the CEO-pattern final go/no-go call. See `lead-agent-evaluation.md` for full protocol.
**Applies to:** Every task before "done" can be claimed.

### Gate G8: Lead Agent Final Evaluation
The orchestrator (or designated human escalation target) evaluates that the work as a WHOLE met the original goal — not just that each skill did its piece. Catches plan-execution drift, goal-output drift, scope creep, and evidence-claim mismatches that single-skill verification misses.

**Entry Criteria**
- All planned skills have produced exit evidence
- All applicable release gates have passed (G6, G6.5, G7)

**Action**
- Reconfirm the original goal from Route Receipt (Phase 0)
- Walk the evidence ledger; check every phase + gate
- Cross-skill consistency check (plan vs. execution, goal vs. output, scope, surface area)
- Make the call: GO / CONDITIONAL GO / HOLD / NO-GO with rationale

**Exit Evidence**
```
Final Evaluation:
  Verdict: [✅ GO | ⚠️ CONDITIONAL | ⏳ HOLD | ❌ NO-GO]
  Goal achieved: [yes | partially | no]
  Phase 0–5 evidence: [✅ complete | gaps: list]
  Release gates: [G6 ✅ | G6.5 ✅/N/A | G7 ✅/N/A]
  Cross-skill consistency: [✅ clean | findings: list]
  Conditions (if any): [list]
  Lead Agent: [orchestrator | escalated to: name]
```

**Block Condition**
- HOLD or NO-GO — cannot claim "done"; address gaps and re-evaluate
- CONDITIONAL with material conditions — escalate to human Lead Agent for explicit acceptance
- Risk = `critical` from Phase 0 — automatic escalation to human regardless of verdict

**Escalation triggers (orchestrator → human Lead Agent):**
- Risk level = `critical`
- Verdict is CONDITIONAL with material conditions
- Cross-skill inconsistency found
- First-time production deployment
- Public-facing release at scale
