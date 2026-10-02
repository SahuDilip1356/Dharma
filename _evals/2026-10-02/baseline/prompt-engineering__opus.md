## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

**Step 0, the target**
```
Model:    claude-sonnet-5 (assumed. "Claude Sonnet" could also mean 4.6, so please confirm)
Surface:  API feature (single-turn RAG Q&A)
Failure:  new prompt
```
Sonnet 5 notes from model-deltas: terser by default, follows instructions literally, has thinking ON by default, and has context awareness. One question for you: what should the bot do when the retrieved chunks don't answer the question? I've assumed it says so and points the user to a human expert.

**System prompt (draft)**
```text
You are SaralPrivacy's DPDPA assistant. You help owners of small and mid-sized Indian
businesses understand what the Digital Personal Data Protection Act, 2023 and its Rules
require of them, in plain language they can act on.

<scope>
You give general compliance information drawn only from the SaralPrivacy wiki excerpts
provided in each request. You do not give legal advice. Users are business owners who may
act on your words, and a confident answer about their specific legal position could expose
them to penalties if it is wrong. So explain what the law and the wiki say in general, and
when a question depends on the facts of their own business (whether they are a
Significant Data Fiduciary, whether a specific incident is a reportable breach, how to
respond to a notice from the Data Protection Board), say that the answer depends on their
facts and recommend they confirm with a qualified privacy lawyer.
</scope>

<grounding>
Answer only from the documents in <wiki_chunks>. First find the passages relevant to the
question and place them in <quotes> tags with their chunk index. Then write the answer in
<answer> tags based only on those quotes. If the chunks do not cover the question, say
"Our guides don't cover this yet" and suggest talking to a privacy professional. Do not
fill gaps from memory, because DPDPA Rules and deadlines change and an outdated detail
reads as authoritative.
</grounding>

<style>
Write in short, plain-English paragraphs for a non-lawyer. Use a numbered list only for
steps the owner must take in order. Cite the chunk you relied on as [Source: <title>].
Keep answers under 200 words unless the user asks for detail. Respond directly without
preamble.
</style>

<examples>
  <example> (general question answered from chunks: "Do I need consent to send
  WhatsApp order updates?") </example>
  <example> (fact-specific question: "We got a notice from the Board, what do we
  reply?" leads to general process plus a recommendation to consult a lawyer) </example>
  <example> (question not covered by the chunks leads to "Our guides don't cover
  this yet") </example>
</examples>
```

**User turn layout.** Documents go first and the question goes last:
```xml
<wiki_chunks>
  <document index="1"><source>{{title}}</source><document_content>{{chunk}}</document_content></document>
  ...
</wiki_chunks>
<question>{{user_question}}</question>
```

**API config.** Use `thinking: {type: "adaptive"}` with `effort: "low"`, and add the "think less often" snippet if latency matters. I left out `budget_tokens` and prefill on purpose. Before you ship, fill in the three examples with real wiki Q&A pairs.

```
Prompt Spec
Target model: claude-sonnet-5        Surface: API
Problem addressed: new
Role: SaralPrivacy DPDPA assistant for SMB owners
XML tags: scope, grounding, style, examples, wiki_chunks, quotes, answer
Examples: 3 (placeholders, tagged)
Long-context layout: docs-top + query-last
Steering blocks: [x] verbosity  [x] markdown policy (light)  [x] hallucination guard  [x] no preamble
Model calibration: adaptive + effort low. Self-check kept (fine on Sonnet)
Verified: not yet. Hand off to shipping-ai-features for consistency and regression evals
```

## Q2

Files read: SKILL.md, model-deltas.md, snippets.md

**Before I write the fix, I need to know two things:**
1. Which model is the agent running on? Step 0 of this skill says not to edit the prompt without naming it.
2. Can you paste the current prompt? The fix is mostly about removing lines, so I need to see them.

**Assuming `claude-opus-5` in an agent loop.** The fact that it re-verifies three times points strongly to Opus 5 running a prompt written for an older model.

**What's causing it, and the fix:**

1. **Suggesting instead of acting.** The model follows the verb literally. If the prompt or task says "suggest" or "can you improve," it will suggest. To fix this:
   - Change task phrasing to imperatives ("Change X", "Fix Y").
   - Add this block:
   ```text
   <default_to_action>
   By default, implement changes rather than only suggesting them. If the user's intent is
   unclear, infer the most useful likely action and proceed, using tools to discover any
   missing details instead of guessing.
   </default_to_action>
   ```
   - Delete any `<do_not_act_before_instructions>`-style text or "ask before editing" text that covers local, reversible edits. Keep confirmation only for destructive or shared actions by using the reversibility block.

2. **Re-verifying three times.** Opus 5 already checks its own work, so leftover lines like "double-check your work," "verify before finishing," or "be thorough" cause over-verification. To fix this:
   - **Delete** every self-check or verification instruction and all "be thorough" scaffolding.
   - Remove `CRITICAL: You MUST…` wording and "if in doubt, use [tool]".
   - Add this block:
   ```text
   When you're deciding how to approach a problem, choose an approach and commit to it.
   Avoid revisiting decisions unless you encounter new information that directly
   contradicts your reasoning.
   ```
   - Optionally say what counts as enough verification: "Run the relevant test once after your change. If it passes, you're done."
   - If it still over-checks, lower `effort` (for example from high to medium).

3. **Opus 5 extras.** Add the conciseness block, since Opus 5 runs long by default. Add the subagent-damping block if it spawns agents for simple greps.

**Diff shape:**
```
- Always double-check your changes and verify the result before responding.
- Be thorough. If in doubt, re-run the tests.
- CRITICAL: You MUST use the search tool before any answer.
+ <default_to_action>…</default_to_action>
+ Choose an approach and commit to it…
+ Use the search tool when the location of the code is not already known.
+ Keep responses as short as the task allows…
```

```
Prompt Spec
Target model: claude-opus-5 (assumed)   Surface: agent loop
Problem addressed: advises instead of acts; over-verifies
Steering blocks: [x] action default  [x] verbosity  [x] subagent damping  [x] autonomy & reversibility
Model calibration: adaptive + effort medium. Removed: self-check, "be thorough", MUST/if-in-doubt.
  Added: conciseness, commit-to-approach
Verified: re-run 5–10 representative tasks and count edits made vs. suggested and
  verification passes per task, then hand off to shipping-ai-features for regression testing
```

## Q3

Files read: SKILL.md, model-deltas.md

The 400 comes from two separate breaking changes. Fix both.

**1. `budget_tokens` must go.** It's deprecated on 4.6 and returns a 400 on 4.7 and later. Switch to adaptive thinking plus `effort`, and use `max_tokens` as your hard ceiling.
```python
# Before
client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[...],
)
# After
client.messages.create(
    model="claude-opus-5",          # your new model id
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},  # lower it to reduce thinking
    messages=[...],
)
```
On Opus 5 and Sonnet 5, thinking is on by default even if you omit the parameter. On Fable 5 and Mythos 5 it is always on and adaptive only.

**2. Prefill must go.** A partial assistant message as the **last** turn returns a 400 on 4.6+ and Mythos Preview. Earlier assistant turns in the history are fine. What to use instead depends on what the prefill was doing:

| Prefill was for | Replace with |
|---|---|
| Forcing JSON (`{`) | Structured Outputs, or just ask for the schema |
| Classification labels | A tool with an enum field, or structured outputs |
| Skipping preamble | "Respond directly without preamble. Do not start with 'Here is…' or 'Based on…'." Strip any leftovers in post-processing |
| Continuing a cut-off reply | Put it in the user turn: "Your previous response was interrupted and ended with `[…]`. Continue from where you left off." |

**Also check while you're migrating:**
- Soften "MUST use tool" wording, and remove "if in doubt" lines.
- On Opus 5, remove self-check instructions and add an explicit conciseness instruction.

Which model are you moving to, and what was the prefill doing? Tell me and I'll give you the exact replacement.

```
Prompt Spec
Target model: [new model id]   Surface: API
Problem addressed: 400 from budget_tokens + final-turn prefill
Model calibration: adaptive + effort (replaces budget_tokens). Removed: prefill.
  Added: no-preamble instruction or structured outputs
Verified: confirm the call returns 200 and the output format matches the old outputs on a
  sample set, then run regression via shipping-ai-features
```
