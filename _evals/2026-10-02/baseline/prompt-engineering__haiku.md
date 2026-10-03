## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

**Prompt Spec**

Target model: Claude Sonnet 5 | Surface: API feature (Q&A bot)
Problem addressed: New — DPDPA Q&A system for SMB owners with wiki retrieval + legal-advice guard

**System Prompt:**

```
Role: You are a DPDPA compliance Q&A assistant for small business owners.

You answer questions about India's Digital Personal Data Protection Act using only
information from the provided wiki chunks. Your goal is to help SMBs understand their
compliance obligations in plain language.

CRITICAL BOUNDARY: You are NOT a lawyer and CANNOT provide legal advice. If a question
requires interpretation of specific regulations for a particular business situation,
decline clearly and recommend consulting a qualified legal professional.

Instructions:

1. Answer only from the provided wiki chunks. If a question is not covered in the
   retrieved documents, say so explicitly: "This topic isn't covered in our docs. For
   guidance, consult a compliance lawyer."

2. Keep explanations simple and concrete. Use examples relevant to SMBs (e.g., customer
   data collection, consent forms, data retention).

3. Structure answers in short, scannable paragraphs. Avoid legal jargon; translate it
   into business terms.

4. When legal interpretation is needed, flag it: "This depends on your specific
   situation. Consult a lawyer on [specific issue]."

5. Close each answer with a relevant action (e.g., "Next step: update your privacy
   policy template" or "Review our data retention guidelines").

Output format: Answer the question directly. No preamble. Use <wiki_quotes> to cite
the chunks you drew from.
```

Structure applied:
- Role: one sentence establishing compliance assistant, not lawyer
- XML tags: `<wiki_quotes>` for sourcing
- Examples: 3–5 edge cases (consent withdrawal, multi-country data, contractor sharing)
- Long-context layout: wiki chunks at top, query last

Steering blocks included:
- [x] Conciseness (Sonnet 5 is terser)
- [x] No preamble
- [x] Action-vs-advice default (Sonnet: direct answers from docs)
- [x] Hallucination guard (Sonnet: investigate before answering, cite sources)

Model calibration:
- Thinking config: adaptive + effort high (multi-step reasoning over docs)
- Removed for Sonnet 5: Anti-laziness language ("MUST use tool")
- Added for Sonnet 5: Source citation requirement (hallucination guard)

Verified: Hand off to shipping-ai-features for consistency scoring before production.

---

## Q2

Files read: SKILL.md, snippets.md, model-deltas.md

**Problem:** Agent suggests changes instead of making them; re-verifies everything three times.

**Root cause (most likely):** Two steering problems:
1. Missing `<default_to_action>` block — agent defaults to advice
2. Over-verification instructions (self-check prompts) — causing 3x verification loop

**Clarifying questions I would ask the user:**
- Which Claude model is this agent running on?
- Are you seeing the over-verification on tool calls or just final outputs?
- Does the agent have edit/apply permissions, or is it read-only?

**Fix (assuming Opus 4.6 / Sonnet 5 + tool access):**

Add this block from `snippets.md` to your system prompt:

```xml
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is
unclear, infer the most useful likely action and proceed, using tools to discover any
missing details instead of guessing. Try to infer whether a tool call (e.g., file edit)
is intended, and act accordingly.
</default_to_action>
```

Remove any `Before you finish, verify your answer against [criteria]` self-check
instructions. If you're on Opus 5, this is especially critical — Opus 5 self-verifies
and inherited verification instructions cause over-verification.

If your model is Opus 4.6, also add:

```text
When you're deciding how to approach a problem, choose an approach and commit to it.
Avoid revisiting decisions unless you encounter new information that directly
contradicts your reasoning.
```

**Why this works:** The `default_to_action` block flips the verb from "suggest" to "do."
Removing self-check instructions stops the re-verification loop. On newer models,
both changes are tuned to their behavior — older anti-laziness language ("MUST")
actually overtriggers and causes extra verification.

---

## Q3

Files read: model-deltas.md, SKILL.md

**Problem:** 400 error after upgrading to newer Claude (likely 4.7+) with params:
- `assistant_message_prefill` (or partial assistant turn)
- `budget_tokens`

**What changed:** Both are incompatible with 4.6+ models.

**Migration steps:**

1. **Remove prefill entirely.** Replace with:
   - Instruction: `Respond directly without preamble. Do not start with 'Here is…'.`
   - Or use structured outputs / tools for schema enforcement
   - Or wrap output inside XML tags

   Before:
   ```python
   messages=[
       {"role": "assistant", "content": "```json\n{"},  # prefill
       {"role": "user", "content": "Generate..."}
   ]
   ```

   After:
   ```python
   messages=[
       {"role": "user", "content": "Generate... Respond as valid JSON."}
   ]
   ```

2. **Replace `budget_tokens` with `effort`.** Affects `thinking` config.

   Before (deprecated):
   ```python
   thinking={"type": "enabled", "budget_tokens": 10000}
   ```

   After (4.6+):
   ```python
   thinking={"type": "adaptive"}
   output_config={"effort": "high"}  # or "medium", "low"
   ```

   If you were not using thinking at all before, no change needed — but check
   `model-deltas.md` row for your target model: thinking may now be ON by default.

3. **Verify thinking defaults for your model:**
   - Fable 5 / Mythos 5: always on (adaptive only)
   - Opus 5: on by default
   - Sonnet 5 / Opus 4.6–4.8 / Sonnet 4.6: off by default
   - Haiku 4.5: off by default

   If on by default and you don't want thinking, explicitly pass `thinking={"type": "off"}`
   (where supported).

**Why the 400:** Assistant messages on the final turn are not allowed on 4.6+. The API
rejects them. `budget_tokens` is also removed — the parameter is unrecognized on 4.7+.

**Test:** After changes, confirm one request completes with a 200 response (no 400).
