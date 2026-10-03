---
name: shipping-ai-features
description: |
  Lifecycle discipline for LLM-powered features: model choice and cost ceilings at
  planning, prompt versioning and token efficiency, adversarial safety evaluation before
  ship, production monitoring, quality regression benchmarks, and model version
  governance. Use when designing, shipping, or operating any feature that calls an LLM;
  when costs, quality, or latency drift; or when a provider deprecates a model.
license: MIT
metadata:
  author: Dilip Sahu
  version: "2.0.0"
---

# Shipping AI Features

Pick the stage you're at and read only that file.

| Stage | When | Read |
|---|---|---|
| Plan | Choosing a model, setting a cost ceiling, deciding cache/stream/batch | [inference-economics.md](inference-economics.md) |
| Build | Prompt changes, versioning, token cost over budget, inconsistent output | [prompt-optimization.md](prompt-optimization.md) |
| Pre-ship gate | Any AI feature about to merge — adversarial, hallucination, bias tests | [ai-safety-eval.md](ai-safety-eval.md) |
| Post-ship | Monitoring plan before go-live, or an AI incident | [ai-observability.md](ai-observability.md) |
| Operate (3+ live AI features) | Scheduled quality regression; before/after model or prompt changes | [benchmark-framework.md](benchmark-framework.md) |
| Operate (2+ live AI features) | Model deprecations, version alignment, audit trails | [model-governance.md](model-governance.md) |

For writing the prompt itself, use `prompt-engineering`.

## Gates that always apply

- Model and cost ceiling are decided before the first line of AI code.
- No AI feature ships without a completed safety evaluation.
- No AI feature ships without a monitoring plan.

The test-case counts and thresholds in these files (e.g. hallucination <5% for critical
claims) are starting defaults. Adjust them to the feature's risk level and record why.
