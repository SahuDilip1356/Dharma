# Prompt Engineering Skill Dry-Run Responses

## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

**Target Model:** `claude-sonnet-5` | **Surface:** API feature (Q&A bot) | **Failure:** new

**System Prompt Spec:**

```xml
You are a DPDPA compliance advisor for small business owners. You answer questions about
India's Digital Personal Data Protection Act using retrieved wiki context, but you do not
provide legal advice.

<role>
Answer compliance questions about DPDPA requirements for SMBs, grounded in wiki documentation.
</role>

<instructions>
1. Answer the user's question directly using only the wiki chunks provided. If the answer
   isn't in the context, say so explicitly: "This specific scenario isn't covered in the
   available documentation."

2. Distinguish between "compliance guidance" (explaining what the law says) and "legal
   advice" (interpreting the law for their specific business situation). You provide only
   the former.

3. Include a disclaimer if the question touches business-specific decisions: "This is
   compliance guidance, not legal advice. For your specific situation, consult a lawyer
   licensed in India."

4. Keep answers concise and direct. State the answer, then stop.
</instructions>

<examples>
<example>
<question>Does DPDPA require me to encrypt customer data at rest?</question>
<wiki_context>
DPDPA Schedule 1 requires reasonable security measures proportionate to the sensitivity
and volume of personal data. Encryption is explicitly recommended for sensitive data
categories (health, financial, biometric).
</wiki_context>
<answer>
Yes, DPDPA Schedule 1 requires encryption for sensitive personal data (health, financial,
biometric information). For general contact data, encryption is recommended but not
mandated—you must implement "reasonable security measures" appropriate to your data type.
</answer>
</example>

<example>
<question>What's the penalty if I collect consent but don't store it properly?</question>
<wiki_context>
Failure to maintain consent records can result in penalties up to INR 5 crore under Section
41. Consent records must be retrievable for audit.
</wiki_context>
<answer>
Failing to maintain retrievable consent records can result in penalties up to INR 5 crore
under Section 41. You must keep records proving when and how you obtained consent.

This is compliance guidance. Your exact liability depends on the data volume, breach history,
and enforcement context. Consult a lawyer for your specific risk assessment.
</answer>
</example>

<example>
<question>I have a customer who asked to delete their data. How do I handle international
transfer requests?</question>
<wiki_context>
[Context says: deletion is 30 days; international transfers require explicit consent]
</wiki_context>
<not_legal_advice>
This guidance tells you what the law requires, but applying it to your architecture,
international agreements, and recovery procedures is a business and legal decision beyond
my scope. Consult your legal counsel before designing your deletion/transfer workflow.
</not_legal_advice>
</example>
</examples>

<do_not_act_before_instructions>
Do not jump into implementation or detailed legal interpretation. Provide compliance
information grounded in the wiki context. For questions that require interpreting the law
for the user's specific business, recommend legal counsel rather than guessing.
</do_not_act_before_instructions>
```

**Model Calibration (Sonnet 5):**
- Thinking config: `{"type": "adaptive"}` + `output_config={"effort": "medium"}` (concise answering, not deep reasoning)
- Sonnet 5 is terse by default—explicit conciseness built into examples
- No self-verification block (Sonnet 5 does not over-verify)
- Context awareness enabled; wiki chunks loaded at runtime

**Prompt Spec Receipt**
```
Target model: claude-sonnet-5        Surface: API feature (Q&A bot)
Problem addressed: new

Structure applied:
  Role: DPDPA compliance advisor for SMBs, guidance only—no legal advice
  XML tags: question, wiki_context, answer, instructions, examples
  Examples: 3, showing compliance guidance vs. legal advice distinction
  Long-context layout: wiki chunks injected per-query, n/a for architecture

Steering blocks included:
  [x] action-vs-advice default (research/recommendation)
  [x] conciseness (Sonnet 5 terser by default, reinforced in prompt)
  [x] no preamble / direct answer

Model calibration:
  Thinking config: adaptive + medium effort
  Removed for Sonnet 5: none required
  Added for Sonnet 5: explicit conciseness reinforcement

Verified: prompt structure matches DPDPA bot use case; examples teach distinction
between guidance and legal advice; Sonnet 5 thinking/effort tuned for Q&A latency
```

---

## Q2

Files read: SKILL.md, model-deltas.md, snippets.md

**Problem:** Agent suggests changes instead of making them; re-verifies work 3 times.

**Diagnosis & Fix:**

This sounds like **Opus 5 over-verification + anti-laziness overtriggering**. Per `model-deltas.md`:
> Opus 5 | Longer | **Remove inherited self-verification instructions (over-verifies)**

**What to change:**

1. **Remove all explicit self-check instructions** like:
   ```text
   Before you finish, verify your answer against [criteria].
   ```
   Opus 5 self-verifies automatically; redundant instructions cause triple-verification.

2. **Replace suggestion-mode language with action default.** If your prompt currently has:
   ```xml
   <do_not_act_before_instructions>
   Provide recommendations rather than taking action...
   </do_not_act_before_instructions>
   ```
   
   Switch to:
   ```xml
   <default_to_action>
   By default, implement changes rather than only suggesting them. If the user's intent is
   unclear, infer the most useful likely action and proceed, using tools to discover any
   missing details instead of guessing.
   </default_to_action>
   ```

3. **Drop anti-laziness phrasing** like "CRITICAL: You MUST use this tool." Replace with:
   ```text
   Use [tool] when it would improve understanding.
   ```

4. **Verify your model version:** If you're on Opus 4.6 or older, also add:
   ```text
   When you're deciding how to approach a problem, choose an approach and commit to it.
   Avoid revisiting decisions unless you encounter new information that directly
   contradicts your reasoning.
   ```

**Clarifying question if unsure:** Which model are you using? If Opus 5, remove all "verify your work" language and switch to `<default_to_action>`. If Opus 4.6 or earlier, add the "Stop revisiting decisions" block above.

---

## Q3

Files read: SKILL.md, model-deltas.md

**Problem:** Code using `budget_tokens` and assistant-message `prefill` returns 400 error after model upgrade.

**Root Cause:** Both are removed in Claude 4.7+ and Opus 4.6+. Per `model-deltas.md` section 2 & 3:
> `budget_tokens` is deprecated on Opus 4.6 / Sonnet 4.6 and returns a 400 error on 4.7 and later. Use `effort` for depth and `max_tokens` for a hard ceiling.

**Fix:**

**Before (old model with `budget_tokens`):**
```python
client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "..."}],
)
```

**After (Opus 5 or Sonnet 5):**
```python
client.messages.create(
    model="claude-opus-5",  # or claude-sonnet-5
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # or "medium" / "low"
    messages=[{"role": "user", "content": "..."}],
)
```

**For prefill (assistant-message on final turn):**

**Before:**
```python
messages=[
    {"role": "user", "content": "Summarize this..."},
    {"role": "assistant", "content": "Here is the summary:\n"},  # Prefill
]
```

**After (remove prefill, use instruction instead):**
```python
messages=[
    {"role": "user", "content": "Summarize this...\n\nRespond directly without preamble. Do not start with 'Here is...' or 'Based on...'"},
]
```

Or use **Structured Outputs** if you need a specific schema:
```python
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=4000,
    response_format={"type": "json_schema", "json_schema": {...}},
    messages=[{"role": "user", "content": "..."}],
)
```

**Summary:** Replace `budget_tokens` with `adaptive thinking + effort`, remove final assistant message prefill, and inject output-format instructions into the user message instead.
