---
name: prompt-optimization
description: |
  Prompt versioning, quality improvement, and token efficiency for production AI features.
  Triggers when:
  - A prompt has been in production and needs review
  - Token costs are higher than the inference-economics budget
  - Output quality is inconsistent across similar inputs
  - A prompt change is being considered (version management)
  - Preparing a prompt for the first production deployment

  Does NOT own: safety thresholds or quality gates (that is ai-safety-eval);
  post-ship monitoring of prompt performance (that is ai-observability).
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Prompt Optimization

**Core rule: Prompts are code. They need versioning, testing, and review before they change in production.**

---

## Step 1: Prompt Audit

Before optimizing, understand the current state. For every prompt in the feature:

```
Prompt Audit
─────────────────────────────────────────────
Feature: [feature name]
Prompt ID: [unique identifier, e.g. patient-summary-v1]
Current version: [v1 / v2 / etc.]
Last changed: [date]
Changed by: [who]

Token count:
  System prompt: [N] tokens
  Average user input: [N] tokens
  Average output: [N] tokens
  Total average: [N] tokens

Quality signals (from ai-observability):
  Thumbs up rate: [%]
  Correction rate: [%]
  Regeneration rate: [%]

Issues observed:
  [ ] Inconsistent output format
  [ ] Output too long / too short
  [ ] Hallucination in specific input types
  [ ] Tone/style drift
  [ ] Excess tokens in system prompt
  [ ] Instruction conflicts (prompt contradicts itself)
─────────────────────────────────────────────
```

---

## Step 2: Token Efficiency Analysis

Find waste before adding optimization. Tokens cost money on every request.

### System Prompt Audit

Read the system prompt and apply these checks:

| Check | Find and fix |
|---|---|
| **Redundant instructions** | Same constraint stated twice in different words → keep one |
| **Unnecessary examples** | >3 few-shot examples → reduce to 1–2 highest-value ones |
| **Verbose phrasing** | "Please make sure that you always..." → "Always..." |
| **Defensive hedging** | "If possible, try to..." → "Always..." or remove |
| **Dead rules** | Instructions for scenarios that never occur in production → remove |
| **Format over-specification** | Detailed formatting instructions that the model ignores anyway → simplify |

### Output Constraint Check

Is the model outputting more tokens than needed?

```
Test: run 10 representative inputs
Measure: average output token count
Compare: what is the minimum tokens needed to be useful?

If avg output >> minimum useful:
  Add explicit length constraint: "Respond in under [N] words"
  Or: "Return JSON only — no explanation"
  Or: "Three bullet points maximum"
```

---

## Step 3: Consistency Testing

A prompt that works on one input but not another is a broken prompt.

### Consistency Test Battery

Run these 5 test types before declaring a prompt stable:

| Test | How to run | Pass condition |
|---|---|---|
| **Paraphrase test** | Same question, 5 different phrasings | Equivalent outputs (±10% variance) |
| **Edge case test** | Empty input, very short input, very long input | Graceful handling, no crash or refusal |
| **Adversarial test** | Input designed to confuse the prompt | Model stays on task |
| **Format stability test** | Same input, 10 runs | Same output structure every time |
| **Regression test** | All inputs from previous version's test suite | No degradation vs. previous version |

```
Consistency Score = (tests passed / total tests) × 100

≥90%: Stable — prompt is production-ready
70–89%: Conditional — document known failure modes, add fallback handling
<70%: Unstable — do not ship; redesign the prompt
```

---

## Step 4: Prompt Versioning

Every prompt that enters production must be versioned. No exceptions.

### Version Naming Convention

```
[feature-name]-[component]-v[N]

Examples:
  patient-summary-system-v1
  patient-summary-system-v2   (after first optimization)
  appointment-rec-extraction-v1
```

### Version Control Rules

```
Rule 1: Never edit a prompt in-place if it's live in production.
        Create a new version and deploy via a controlled process.

Rule 2: Keep all previous versions — never delete.
        A rollback is the fastest incident response.

Rule 3: Log the prompt version on every AI request.
        Without this, you cannot debug quality regressions.

Rule 4: Changes to the system prompt require a new version.
        Changes to user input formatting require a new version.
        Changes to output parsing only (no prompt change) do not.

Rule 5: A/B testing two prompt versions requires both to be versioned
        and logged — never ship an unnamed variant.
```

### Version Changelog Format

```
Prompt: patient-summary-system
─────────────────────────────────────────────
v3 — 2026-04-27 — Dilip
  Change: Reduced system prompt from 420 to 280 tokens by removing 4 redundant rules
  Reason: Cost reduction — avg $0.012 → $0.008/request
  Test result: Consistency score 94% (vs 91% on v2)
  Quality signal: Thumbs up 88% → 89% (no degradation)

v2 — 2026-03-15 — Dilip
  Change: Added explicit JSON output constraint
  Reason: Parser errors on 3% of v1 outputs
  Test result: Consistency score 91% (vs 78% on v1)

v1 — 2026-02-20 — Dilip
  Initial production version
─────────────────────────────────────────────
```

---

## Step 5: Prompt Change Process

Before changing any production prompt:

```
Prompt Change Checklist
─────────────────────────────────────────────
Proposed change: [describe what you're changing and why]
Prompt ID: [name]-v[N] → v[N+1]

Pre-change:
[ ] Current version logged and backed up
[ ] Quality baseline recorded (thumbs up %, consistency score)
[ ] Test suite from previous version saved

New version:
[ ] Change made and documented in changelog
[ ] Token count comparison: v[N] = [X] tokens → v[N+1] = [Y] tokens
[ ] Consistency test battery run: [score]%
[ ] Regression test vs. previous version: [pass / fail list]
[ ] ai-safety-eval adversarial tests re-run on new version: [pass / fail]

Decision:
[ ] ✅ Ship v[N+1] — quality maintained or improved, tokens reduced
[ ] ⚠️ Ship with monitoring — minor quality trade-off, watch 48h
[ ] ❌ Revert to v[N] — quality degraded or tests failing
─────────────────────────────────────────────
```

---

## Anti-Patterns

Never do these:

| Anti-Pattern | Why it fails |
|---|---|
| **Editing the live prompt directly** | No rollback path if quality drops |
| **Adding more instructions to fix a broken prompt** | Longer prompts cost more and often make consistency worse |
| **Shipping a prompt without a consistency test** | Quality looks fine on your test case, fails on edge cases in production |
| **Removing instructions without testing** | What seems redundant may be covering a specific failure mode |
| **Optimizing token count at the expense of output quality** | Saving $0.002/request is not worth a 10% quality drop |

---

## Output Format

At the end of prompt optimization work:

```
Prompt Optimization Summary
─────────────────────────────────────────────
Feature: [name]
Prompt: [id] — v[old] → v[new]

Token change: [X] → [Y] tokens ([+/-Z]%)
Cost change: $[A]/request → $[B]/request

Consistency score: [old]% → [new]%
Quality signals: thumbs up [old]% → [new]%

Changes made:
  1. [change description]
  2. [change description]

Test results: [N] passed / [M] failed
  Failures: [list any, with plan to address]

Rollback: v[old] is pinned and available for instant rollback

Status: ✅ Ready for production / ⚠️ Conditional / ❌ Blocked
─────────────────────────────────────────────
```
