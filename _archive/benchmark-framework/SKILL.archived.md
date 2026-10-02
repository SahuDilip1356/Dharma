---
name: benchmark-framework
description: |
  Scheduled quality regression tracking for production AI features. Triggers when:
  - 3+ AI features are live and quality needs continuous monitoring
  - A model version change is planned (run benchmarks before and after)
  - A prompt version change is deployed (run benchmarks to confirm no regression)
  - Asking "is our AI quality getting better or worse over time?"
  - ai-observability quality signals show unexplained degradation

  Activate when 3+ AI features are in production. Before that, ai-safety-eval
  spot checks and ai-observability quality signals are sufficient.

  Does NOT own: pre-ship hallucination gate (that is ai-safety-eval Step 4);
  one-time quality spot checks (that is ai-safety-eval Step 7).
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Benchmark Framework

**Core rule: Quality at launch is a snapshot. Quality over time requires a benchmark. What gets measured gets managed.**

---

## Step 1: Build the Benchmark Suite

A benchmark suite is a fixed set of inputs with known correct outputs. It runs on a schedule and after every significant change.

### Suite Design Principles

```
1. Fixed inputs — the same inputs every run. Never randomize the benchmark set.
2. Known ground truth — for each input, you know what a good output looks like.
3. Representative — covers the distribution of real user inputs (not just easy cases).
4. Small enough to run regularly — 20–50 cases per feature; enough for signal, not so many it's expensive.
5. Version-locked — the suite itself is versioned; when you add cases, create suite-v2.
```

### Suite Template

```
Benchmark Suite: [feature-name]-suite-v1
Created: [date]
Last run: [date]
Cases: [N]

─────────────────────────────────────────────
Case 001
Input: [exact input text or reference to input file]
Expected output type: [structured JSON / free text / classification]
Quality criteria:
  - [criterion 1: e.g. "output contains patient name"]
  - [criterion 2: e.g. "output is under 200 words"]
  - [criterion 3: e.g. "no hallucinated appointments"]
Scoring: [pass/fail per criterion | 0-100 rubric]
─────────────────────────────────────────────
Case 002
...
─────────────────────────────────────────────
```

### How Many Cases?

| Feature Risk Level | Suite Size | Why |
|---|---|---|
| Low (content generation, tagging) | 20 cases | Enough for trend detection |
| Medium (recommendations, summaries) | 30–50 cases | More sensitive to distribution shift |
| High (medical, financial, compliance) | 50+ cases | Statistical confidence required |

---

## Step 2: Define Scoring

Every benchmark case needs a score. Define scoring before running — not after.

### Scoring Options

**Binary (pass/fail)** — use for structured output and hard requirements:
```
Pass: output contains required fields AND meets length constraint AND no forbidden content
Fail: any criterion fails
Suite score = (passes / total cases) × 100%
```

**Rubric (0–100)** — use for free-text quality:
```
Correctness (40%): Is the information accurate?
Relevance (30%):   Does the output answer the question?
Conciseness (20%): Is it an appropriate length?
Safety (10%):      No harmful content?

Case score = weighted average
Suite score = average of all case scores
```

**LLM-as-judge** — use for nuanced quality evaluation at scale:
```
Judge prompt: "Rate this response on a scale of 1-5 for [criterion]. 
               Response: [output]. Context: [input]. 
               Output only the number."

Use a different model than the one being benchmarked.
Run judge 3× per case, take median to reduce variance.
```

---

## Step 3: Establish Baseline

The first benchmark run establishes the baseline. Everything else is measured against it.

```
Baseline Run — [feature-name]-suite-v1
─────────────────────────────────────────────
Date: [date]
Model: [model + version]
Prompt: [prompt-id + version]

Results:
  Cases: [N total]
  Pass rate: [X]%
  Average score: [Y]/100

Per-criterion breakdown:
  [criterion 1]: [score]%
  [criterion 2]: [score]%
  [criterion 3]: [score]%

Baseline locked: ✅
─────────────────────────────────────────────
```

The baseline is frozen. Do not update it unless you are deliberately re-baselining after a major model change (and document why).

---

## Step 4: Run Schedule

Benchmarks must run on a defined schedule, not ad-hoc.

| Trigger | When to run | Who reviews |
|---|---|---|
| **Scheduled** | Weekly — every Monday morning | Automated; founder reviews if alerts fire |
| **Model change** | Before + after switching model version | Compare delta — must not regress |
| **Prompt change** | Before + after deploying new prompt version | Compare delta — must not regress |
| **Quality signal drop** | When ai-observability thumbs up rate drops >10% | Immediate — find the degraded cases |
| **Provider update** | When AI provider announces model changes | Preemptive — test before change takes effect |

---

## Step 5: Regression Detection

A benchmark run is only useful if it triggers action when quality drops.

### Regression Thresholds

| Change | Severity | Action |
|---|---|---|
| Score drops <3% | Noise | Log, no action |
| Score drops 3–10% | Warning | Investigate — which cases degraded? Why? |
| Score drops >10% | Regression | Stop further model/prompt changes; root cause required before proceeding |
| Score drops >20% | Critical | Roll back model or prompt version immediately |

### Regression Analysis Process

When a threshold is breached:

```
1. Identify which cases degraded (compare this run vs. previous run case-by-case)
2. Find the pattern: are the failing cases similar? What do they have in common?
3. Check what changed: model version? prompt version? input distribution?
4. Hypothesize root cause
5. Test the hypothesis: fix the suspected cause and re-run the degraded cases
6. If fixed: deploy fix, re-run full suite to confirm
7. If not fixed: escalate — do not ship further changes until resolved
```

---

## Step 6: Benchmark Report

After every run, produce a report:

```
Benchmark Report — [feature-name]
─────────────────────────────────────────────
Run date: [date]
Suite version: [v1 / v2]
Model: [model + version]
Prompt: [prompt-id + version]

Results vs. baseline:
  Baseline (v1, [baseline date]): [X]%
  This run: [Y]%
  Delta: [+/-Z]%
  Status: [✅ No regression | ⚠️ Warning | ❌ Regression]

Results vs. last run:
  Last run ([date]): [X]%
  This run: [Y]%
  Delta: [+/-Z]%
  Trend: [↑ Improving | → Stable | ↓ Degrading]

Case breakdown:
  Passed: [N] / [total]
  Failed: [N] — cases: [list IDs]
  Notable changes: [any cases that flipped pass→fail or fail→pass]

Action required: [none | investigate: [issue] | rollback: [what]]
Next run: [date]
─────────────────────────────────────────────
```

---

## Suite Evolution

When real-world usage reveals new failure modes, add them to the suite:

```
Adding a case to the suite:
  1. A production incident reveals a failure mode not covered by current cases
  2. Add the failure case to the suite (with the known-bad input and expected good output)
  3. Create suite-v[N+1]
  4. Re-run baseline on suite-v[N+1] — this becomes the new frozen baseline
  5. Document: "suite-v2 adds 3 cases from production incidents on 2026-04-15"

Never remove cases from the suite unless the feature itself has changed scope.
Removing a failing case to make the score look better is data fraud.
```

---

## Integration with Other Skills

| Skill | How benchmark-framework connects |
|---|---|
| `ai-safety-eval` | Safety eval creates the initial hallucination baseline (Step 4); benchmark-framework tracks hallucination rate over time as a trend |
| `ai-observability` | Observability signals a quality drop via thumbs-up rate; benchmark-framework diagnoses which specific inputs are degrading |
| `prompt-optimization` | Every prompt version change must trigger a benchmark run before and after |
| `model-governance` | Every model version change must trigger a benchmark run before and after |
