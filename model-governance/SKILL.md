---
name: model-governance
description: |
  Model versioning, deprecation management, audit trails, and change control for
  production AI features. Triggers when:
  - An AI provider announces a model deprecation or version change
  - Multiple AI features use different model versions and need alignment
  - A regulated product (healthcare, compliance, financial) requires audit trails
    for AI-generated outputs
  - A model is being upgraded or swapped in a live feature
  - Asking "which model version is each feature using?"

  Activate after 2+ AI features are live. Before that, ai-safety-eval and
  ai-observability are sufficient.

  Does NOT own: safety evaluation (ai-safety-eval); cost analysis (inference-economics);
  prompt versioning (prompt-optimization).
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.0.0"
---

# Model Governance

**Core rule: In production, "the AI" is not a black box. You must know exactly which model version generated which output, and be able to reproduce or audit any decision.**

---

## The Model Registry

Every production AI feature must have a model registry entry. This is the source of truth for what is running where.

### Registry Format

```
Model Registry
─────────────────────────────────────────────
Feature               Model                  Version     Pinned?   Since
─────────────────────────────────────────────────────────────────────────
patient-summary       claude-sonnet-4-6      latest      No        2026-02-20
appointment-rec       claude-haiku-4-5       20251001    Yes       2026-03-01
dpdpa-report-gen      claude-sonnet-4-6      latest      No        2026-03-15
─────────────────────────────────────────────
```

### Pinned vs. Latest

| Strategy | When to use | Risk |
|---|---|---|
| **Pinned** (specific version ID) | Regulated features, audit-critical outputs, financial decisions, medical outputs | Provider may deprecate the version |
| **Latest** (always current) | Non-critical features, internal tools, low-stakes generation | Behavior may change without warning when provider updates |

**Rule:** Any feature where a user acts on the AI output (books an appointment, submits a form, receives a recommendation) should be pinned. Use `latest` only for features where output quality is observed by a human before action is taken.

---

## Model Change Management

When a model needs to change — either because you're upgrading or because the provider is deprecating:

### Step 1: Impact Assessment

```
Model Change Impact Assessment
─────────────────────────────────────────────
Change: [old model/version] → [new model/version]
Reason: [upgrade / deprecation / cost / quality]

Features affected:
  [feature-1] — impact: [low/medium/high] — reason: [why]
  [feature-2] — impact: [low/medium/high] — reason: [why]

Estimated behavior change: [none expected / minor / significant]
Test requirement: [quick spot check / full ai-safety-eval re-run]

Rollback: [old version still available? until when?]
─────────────────────────────────────────────
```

### Step 2: Test Before Switching

For each affected feature:
- Run the prompt-optimization consistency test battery on the new model
- Run ai-safety-eval adversarial tests on the new model
- Compare output quality signals (use existing benchmark if benchmark-framework is installed)

Pass criteria before switching in production:
- Consistency score ≥ current version
- ai-safety-eval: no new failures
- Quality spot check: no degradation on 10 real-world inputs

### Step 3: Staged Rollout

Do not switch all features simultaneously.

```
Rollout sequence:
  1. Switch lowest-risk feature first (internal tool, low volume)
  2. Monitor for 48h — check ai-observability signals
  3. Switch next feature only if no degradation detected
  4. Continue until all features migrated
  5. Decommission old model version reference after all features migrated + 7 day soak
```

### Step 4: Update Registry

After each feature migrates, update the model registry immediately.

---

## Audit Trail Requirements

For regulated products (healthcare, DPDPA compliance, financial services), every AI-generated output that influences a user decision must be auditable.

### Minimum Audit Log Entry

```typescript
{
  request_id: "uuid",
  timestamp: "ISO-8601",
  feature: "patient-summary",
  model: "claude-sonnet-4-6",
  model_version: "20250219",
  prompt_version: "patient-summary-system-v3",
  input_hash: "sha256 of input (not the raw input)",
  output_hash: "sha256 of output",
  user_id: "hashed — never raw PII",
  tokens_used: { input: 1240, output: 380 },
  latency_ms: 1240,
  cost_usd: 0.0089
}
```

**What to store:**
- Hashes of input and output (not the raw content, unless required by compliance)
- Model and prompt version identifiers
- Timestamp and request ID
- Cost and token usage

**What NOT to store:**
- Raw patient data, personally identifiable information
- Sensitive business data
- API keys or credentials

### Retention Policy

| Product Type | Minimum Retention | Reason |
|---|---|---|
| Healthcare | 7 years | HIPAA / clinical records |
| DPDPA compliance | 3 years | Regulatory audit window |
| General SaaS | 90 days | Incident investigation |

---

## Deprecation Playbook

When a provider announces a model deprecation:

```
Deprecation Response Checklist
─────────────────────────────────────────────
Model being deprecated: [model name/version]
Deprecation date: [date]
Features using this model: [list from registry]
Days until deprecation: [N]

Week 1 (immediately):
[ ] Identify all features using the deprecated model
[ ] Identify candidate replacement model
[ ] Run side-by-side quality comparison (10 real-world inputs per feature)
[ ] Flag for ai-safety-eval re-run if quality differs materially

Week 2–3:
[ ] Run full test suite on replacement model
[ ] Update model registry with new version
[ ] Deploy to staging environment
[ ] Run ai-observability baseline on staging

Week 4 (at least 1 week before deprecation):
[ ] Staged rollout to production (lowest-risk feature first)
[ ] Monitor for 48h per feature
[ ] Complete migration before deprecation date

Post-migration:
[ ] Update registry — mark old version as deprecated
[ ] Update prompt-optimization changelog if prompts were adjusted
[ ] Document any quality changes in model registry notes
─────────────────────────────────────────────
```

Never wait until the deprecation date. Start at Week 1 immediately.

---

## Governance Review Cadence

| Review | Frequency | What to check |
|---|---|---|
| **Registry review** | Monthly | Are all entries current? Any features using deprecated versions? |
| **Audit log review** | Quarterly | Are logs complete? Retention policy followed? No PII leaked? |
| **Deprecation watch** | On provider announcement | Immediate response per playbook above |
| **Cost review** | Monthly | Are model choices still economically optimal? (Hand off to inference-economics) |

---

## Output Format

After any model governance action, document:

```
Model Governance Summary
─────────────────────────────────────────────
Action: [new registration / version change / deprecation response / audit review]
Date: [date]

Registry state (after action):
  [feature] → [model] [version] [pinned/latest]

Changes made:
  [description]

Test results:
  [consistency score, ai-safety-eval pass/fail, quality comparison]

Audit trail: [✅ logging active | ⚠️ gaps: list | ❌ not configured]

Next review: [date or trigger]
─────────────────────────────────────────────
```
