---
name: ai-observability
description: |
  Post-ship monitoring setup for AI features. Triggers when:
  - An AI/LLM feature is about to ship to production (set up monitoring before go-live)
  - An AI feature is already live and has no monitoring in place
  - An AI incident occurs (hallucination spike, latency regression, cost overrun)
  - Asking "how is our AI feature performing in production?"

  THE NON-NEGOTIABLE RULE: No AI feature ships to production without a monitoring plan.
  ai-safety-eval gates pre-ship quality. ai-observability owns everything after.

  Does NOT own: pre-ship testing (ai-safety-eval), prompt engineering, model selection.
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# AI Observability

**Core rule: You cannot manage what you cannot see. Pre-ship testing tells you it worked once. Observability tells you it keeps working.**

---

## The 5-Layer Observability Stack

Set up all 5 layers before an AI feature goes live.

### Layer 1: Latency Monitoring

Track response time at every percentile that matters:

| Metric | What it tells you | Alert threshold |
|---|---|---|
| `p50` (median) | Typical user experience | Baseline from load test |
| `p95` | What most users actually experience | 2× your p50 baseline |
| `p99` | Worst-case experience | 3× your p50 baseline |
| `p99.9` | Outliers — often reveals timeouts | Absolute max you'd tolerate |

```
Implementation:
- Log request_start_time and response_end_time for every AI call
- Emit to your metrics system (Datadog, Grafana, Vercel Analytics, etc.)
- Dashboard: p50/p95/p99 as time-series, 24h and 7d windows
- Alert: p95 > threshold for 5 consecutive minutes → PagerDuty/Slack
```

### Layer 2: Error Rate Monitoring

Track every failure mode:

| Error Type | Example | Threshold |
|---|---|---|
| **Hard failures** | API timeout, rate limit hit, network error | <0.5% of requests |
| **Soft failures** | Model returned empty response, malformed JSON | <1% of requests |
| **Safety refusals** | Model refused to answer (expected) | Track, don't alert |
| **Application errors** | Prompt template bug, context overflow | 0% tolerance |

```
Implementation:
- Wrap every AI call in try/catch, classify the error type
- Log: {error_type, model, prompt_version, user_id (hashed), timestamp}
- Alert: hard_failure_rate > 0.5% over 10 minutes → immediate alert
- Alert: soft_failure_rate > 1% over 1 hour → warning alert
```

### Layer 3: Cost Monitoring

Track spend in real time — cost overruns happen fast with AI:

| Metric | What to track | Alert |
|---|---|---|
| **Cost per request** | Tokens in + tokens out × model price | >2× your inference-economics baseline |
| **Daily spend** | Total $ spent today | >120% of daily budget |
| **Cost per user** | Spend per active user | Trending upward week-over-week |
| **Token distribution** | Input vs output token ratio | Unexpected shifts signal prompt issues |

```
Implementation:
- Log token counts from every API response (usage.input_tokens, usage.output_tokens)
- Calculate cost: tokens × model_price_per_token
- Emit daily spend to dashboard
- Alert: daily_spend > budget × 1.2 → notify founder immediately
```

### Layer 4: Quality Signal Monitoring

Track output quality continuously — not just at ship time:

| Signal | How to measure | Frequency |
|---|---|---|
| **Thumbs up/down** | In-product feedback on AI responses | Real-time |
| **Correction rate** | How often users edit AI-generated content | Daily |
| **Abandonment rate** | Users who start an AI flow and abandon | Daily |
| **Repeat rate** | Users who regenerate the same request | Weekly |

```
Implementation:
- Add minimal feedback widget to every AI output: 👍 / 👎
- Log: {feedback, model_version, prompt_version, feature, timestamp}
- Dashboard: rolling 7-day thumbs up % per feature
- Alert: thumbs_up_rate drops >10% week-over-week → investigate prompt or model
```

### Layer 5: Drift Detection

Models and data change. What worked at launch may degrade silently:

| Drift Type | What changes | How to detect |
|---|---|---|
| **Model drift** | Provider updates the model | Compare benchmark scores before/after provider update |
| **Prompt drift** | Context or system prompt was changed | Version prompts; log which version each request used |
| **Input distribution shift** | User queries shift to new topics | Track topic clustering week-over-week |
| **Output distribution shift** | Response length, tone, confidence changes | Track avg output tokens, sentiment week-over-week |

```
Implementation:
- Every prompt has a version identifier (v1, v2, v3)
- Log prompt_version on every request
- Run weekly: compare this week's quality signals vs last week
- If benchmark-framework is installed: trigger weekly benchmark run on model updates
```

---

## Pre-Ship Observability Checklist

Before any AI feature goes live, confirm all 5 layers are wired up:

```
Observability Setup Checklist
─────────────────────────────────────────────
Feature: [feature name]
Model: [model used]
Prompt version: [v1]

[ ] Layer 1 — Latency: p50/p95/p99 logging active; baseline established from load test
[ ] Layer 2 — Errors: hard/soft failure classification; alert thresholds configured
[ ] Layer 3 — Cost: per-request cost logging; daily budget alert set
[ ] Layer 4 — Quality: feedback widget deployed; 7-day rolling dashboard live
[ ] Layer 5 — Drift: prompt versioning in place; weekly comparison scheduled

Runbook:
  High latency: [who to page, what to check first]
  Cost spike:   [who to notify, automatic circuit breaker?]
  Quality drop: [who investigates, rollback procedure]

Status: [ ] Ready to ship  [ ] Gaps remaining: [list]
─────────────────────────────────────────────
```

Do not mark as ready to ship if any layer is missing. A gap here means a blind spot in production.

---

## Incident Response: AI Feature Degradation

When an AI feature is misbehaving in production:

### Step 1: Classify the incident
| Symptom | Classification | First action |
|---|---|---|
| Latency spike | Performance incident | Check model provider status page |
| Cost spike | Economics incident | Check token count — prompt may have grown |
| Quality drop (sudden) | Model or prompt incident | Check for model version change from provider |
| Quality drop (gradual) | Drift incident | Run benchmark comparison |
| Hard failures | Reliability incident | Check API key, rate limits, network |

### Step 2: Contain
- If quality drop: roll back to previous prompt version
- If cost spike: add hard token limit as circuit breaker
- If latency spike: add timeout + fallback response
- If reliability: switch to backup model (if configured)

### Step 3: Investigate
- Pull logs for the affected time window
- Compare: prompt version, model version, input distribution
- Identify: when did the metric first degrade? What changed at that time?

### Step 4: Recover
- Apply fix (prompt rollback, model pin, token limit)
- Verify metrics return to baseline
- Document: what happened, why, what the fix was

### Step 5: Prevent
- Add the failure mode to `ai-safety-eval` adversarial test suite
- Add monitoring for the specific signal that was missing

---

## What "Observability Complete" Looks Like

```
AI Observability: Patient Summary Feature

Layer 1 — Latency: ✅ p50=0.8s, p95=1.4s, p99=1.8s logged; alert at p95>3s
Layer 2 — Errors: ✅ Hard failures <0.1%, soft failures <0.3%; alerts configured
Layer 3 — Cost: ✅ Avg $0.0089/summary; daily budget alert at $15/day
Layer 4 — Quality: ✅ 👍 rate = 87% over first 7 days; weekly review scheduled
Layer 5 — Drift: ✅ Prompt versioned at v1; weekly benchmark scheduled

Runbook: documented in Notion (link)
On-call: Dilip — Slack alert for cost/quality issues

Status: ✅ Observability complete — ready to ship
```

---

## When to Escalate

Stop and escalate to the team when:
- Hard failure rate exceeds 2% for more than 15 minutes
- Daily cost exceeds 150% of budget
- Quality thumbs-up rate drops below 70% (or your defined minimum)
- You cannot identify the root cause of a quality regression within 30 minutes
