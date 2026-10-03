---
name: inference-economics
description: |
  Model selection, token budget design, and cost architecture for AI features.
  Triggers at Phase 2 (planning) when:
  - Designing an AI feature and choosing which model to use
  - Setting cost constraints before building
  - Evaluating whether a feature is economically viable at scale
  - Deciding whether to cache, stream, or batch AI requests

  THE NON-NEGOTIABLE RULE: Model selection and cost ceilings must be decided at
  Phase 2 — before the first line of AI code is written. Changing models post-build
  is expensive. Discovering cost overruns post-ship is worse.

  Does NOT own: cost/latency validation against constraints (that is ai-safety-eval Step 6);
  post-ship cost monitoring (that is ai-observability Layer 3).
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Inference Economics

**Core rule: Every AI feature is also a cost commitment. Design the economics before writing the prompt.**

---

## Step 1: Define the Cost Envelope

Before choosing a model, define what you can afford per request:

```
Cost Envelope Definition
─────────────────────────────────────────────
Feature: [feature name]
Requests per day (estimated): [N]
Acceptable cost per request: $[X]
Monthly budget ceiling: $[Y]

Calculation:
  Daily cost = requests/day × cost/request
  Monthly cost = daily cost × 30

Check: Does monthly cost fit within $Y budget? If not, reduce scope or choose cheaper model.
─────────────────────────────────────────────
```

If you cannot define acceptable cost per request, stop. Ask the product owner before proceeding.

---

## Step 2: Model Selection Matrix

Choose the right model for the job. Do not default to the most capable model.

| Task Type | Recommended Model Tier | Why |
|---|---|---|
| Simple classification, tagging, routing | Haiku (smallest/fastest) | Low complexity, high volume — cost dominates |
| Summarization, extraction, formatting | Haiku or Sonnet | Depends on quality requirement |
| Reasoning, multi-step analysis, complex generation | Sonnet | Balanced quality + cost |
| Complex code generation, nuanced judgment, novel reasoning | Opus | Reserve for tasks where quality is critical and volume is low |
| Real-time user-facing responses | Sonnet with streaming | Latency perception matters more than raw speed |
| Batch processing (non-realtime) | Haiku or batch API | Latency doesn't matter — cost does |

### Decision Framework

Ask these questions in order:

```
1. What is the minimum quality that makes this feature useful?
   → If "basic but correct" suffices: Haiku
   → If "high quality" is required: Sonnet
   → If "expert-level" is required: Opus

2. What is the request volume?
   → High volume (>1000/day): pressure toward cheaper model
   → Low volume (<100/day): quality can justify higher cost

3. What is the latency requirement?
   → Real-time (<2s): streaming Sonnet
   → Near-real-time (2–10s): standard Sonnet or Haiku
   → Batch (minutes acceptable): Haiku batch

4. Is this decision reversible?
   → Start with Sonnet if unsure — easier to downgrade than to explain quality degradation
```

---

## Step 3: Token Budget Design

Tokens are the unit of cost. Design token usage before writing prompts.

### Token Budget Template

```
Token Budget
─────────────────────────────────────────────
Feature: [feature name]
Model: [chosen model]

System prompt (estimated): [N] tokens
  → Keep under 500 tokens; every request pays this cost

User input (estimated):    [N] tokens
  → What is the typical input size? What is the maximum?

Context/RAG (estimated):   [N] tokens
  → How much retrieved context will be injected?
  → Can context be truncated without quality loss?

Output (estimated):        [N] tokens
  → Output tokens cost 3–5× more than input tokens (model-dependent)
  → Can output be constrained with instructions? ("Respond in under 100 words")

Total per request:         [input + output] tokens
Cost per request:          [total_tokens × price_per_token]
─────────────────────────────────────────────
```

### Token Reduction Techniques

Apply before finalizing the prompt design:

| Technique | Savings | When to apply |
|---|---|---|
| **Constrain output length** | 30–60% output reduction | Always — "respond in under N words" |
| **Truncate context** | Varies | When RAG context exceeds 2K tokens |
| **Remove examples from system prompt** | 20–40% input reduction | When few-shot examples are >3 |
| **Use structured output** | Reduces hedging tokens | When output is JSON/structured data |
| **Cache system prompt** | 90% reduction on repeat calls | When system prompt is stable across requests |
| **Batch similar requests** | Up to 50% cost reduction | For non-realtime processing |

---

## Step 4: Caching Strategy

Cache decisions eliminate redundant inference cost entirely.

| Scenario | Cache Strategy | Implementation |
|---|---|---|
| Same question asked by many users | **Semantic cache** — cache by query embedding | Redis + cosine similarity threshold |
| Same document summarized multiple times | **Content hash cache** — cache by input hash | Simple key-value cache |
| System prompt never changes per session | **Prompt prefix caching** | Anthropic prompt caching API |
| Batch reports run nightly | **Result cache** — cache output for 24h | Standard cache with TTL |
| Real-time personalized responses | **No cache** — each response is unique | N/A |

```
Cache Decision:
  Is the input likely to repeat? [yes / no / sometimes]
  Is the output deterministic for the same input? [yes / no]
  Is the output time-sensitive? [yes / no]

  If yes/yes/no → cache it
  If no or yes (time-sensitive) → do not cache
```

---

## Step 5: Viability Check

Before approving the feature for build, confirm it passes economic viability:

```
Economic Viability Check
─────────────────────────────────────────────
Feature: [feature name]
Model selected: [model]
Cost per request: $[X]
Estimated daily requests: [N]
Estimated monthly cost: $[Y]

Budget ceiling: $[Z]
Status: [✅ Under budget | ⚠️ Close to ceiling | ❌ Exceeds budget]

At 10× growth: $[Y × 10]/month
Status at scale: [✅ Still viable | ⚠️ Needs redesign at scale | ❌ Unviable at scale]

Decision: [✅ Approved to build | ⚠️ Approved with cost controls | ❌ Requires redesign]
─────────────────────────────────────────────
```

If the feature exceeds budget at current or projected scale, stop. Redesign options:
- Use a cheaper model (quality trade-off)
- Add caching (reduces effective request count)
- Reduce context size (reduces tokens per request)
- Restrict feature to paid tier only (reduces request volume)
- Make the feature async/batch (unlocks cheaper batch pricing)

---

## Output Format

At the end of Phase 2, this skill produces:

```
Inference Economics Summary
─────────────────────────────────────────────
Feature: [name]

Model: [model name]
  Reason: [why this model was chosen over alternatives]

Token budget:
  Input: ~[N] tokens (system: [X] + user: [Y] + context: [Z])
  Output: ~[N] tokens
  Total: ~[N] tokens/request
  Cost: ~$[X]/request

Caching:
  Strategy: [none | prompt prefix | semantic | content hash | result]
  Expected cache hit rate: [%]
  Effective cost after cache: ~$[X]/request

Monthly projection:
  [N] requests/day × $[X]/request × 30 = $[Y]/month
  At 10× growth: $[Y × 10]/month — [viable / needs redesign]

Cost ceiling set: $[X]/request (feeds into ai-safety-eval Step 6 as the constraint to validate)
─────────────────────────────────────────────
```

This summary is the input that `ai-safety-eval` Step 6 validates against. The economics skill sets the ceiling; the safety eval confirms the built system meets it.
