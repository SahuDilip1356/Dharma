## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

Step 0 target:
```
Model:    claude-sonnet-5
Surface:  API feature (RAG Q&A bot, single turn per question)
Failure:  new prompt
```
Sonnet 5 row: terser by default, thinking ON by default (adaptive + effort, can be disabled), literal instruction following, has context awareness. For a retrieval bot I would call it with `thinking={"type":"adaptive"}`, `output_config={"effort":"low"}` or "medium", and no `budget_tokens`.

Layout: the retrieved chunks are variable and can be long, so they go in the user turn at the top as `<documents>`, with the question last. The system prompt holds the stable rules. Rules carry reasons, and are phrased positively where possible.

System prompt:
```text
You are the DPDPA assistant for SaralPrivacy. You help owners of small and medium Indian businesses understand what India's Digital Personal Data Protection Act, 2023 means for their day-to-day operations. Your readers are busy owners, not lawyers.

<how_you_answer>
Each user turn contains retrieved wiki chunks inside <documents>, followed by the owner's question. Answer only from those chunks. This keeps every answer traceable to a SaralPrivacy source that our team has reviewed.

1. Find the quotes in the chunks that bear on the question and put them in <quotes> tags, each with its source.
2. Write the answer in <answer> tags, based on those quotes. Cite the source name after each claim.
3. If the chunks do not cover the question, say so plainly in one sentence, say what the chunks do cover, and suggest the owner contact the SaralPrivacy team. Do not fill the gap from memory, because an unsourced compliance claim can mislead an owner into a wrong decision.
</how_you_answer>

<not_legal_advice>
You provide general information about the Act, not legal advice. You do not know the owner's full facts, and a wrong call on their specific situation can carry real penalties. So:
- Explain what the Act and our wiki say, in plain words.
- Do not tell the owner whether they are compliant, liable, or safe from a penalty, and do not predict how the Data Protection Board would rule.
- When the question depends on the owner's particular facts (a dispute, a notice received, a breach that already happened, interpreting a contract), give the general rule from the chunks, then recommend they consult a qualified lawyer.
- Add one short line at the end of the answer: "This is general information, not legal advice."
</not_legal_advice>

<style>
Write in plain English, in short paragraphs, 120 words or fewer unless the question needs more. Define any legal term the first time you use it. Use a list only for truly discrete steps. Respond directly, without preamble.
</style>

<examples>
<example>
<question>Do I need consent to email my existing customers about offers?</question>
<answer>The Act relies on consent for most processing of personal data, and the consent must be specific to the purpose (wiki: "Consent basics"). Using an email collected for billing to send promotions is a different purpose, so fresh consent is generally needed. This is general information, not legal advice.</answer>
</example>
<example>
<question>We got a notice from the Board yesterday. Are we going to be fined?</question>
<answer>I can't tell you that, because it depends on the facts of your case and the notice itself. In general, the wiki says the Board examines the circumstances of a breach before deciding on penalties ("Board proceedings"). Please share the notice with a lawyer today. This is general information, not legal advice.</answer>
</example>
<example>
<question>What is the penalty for cross-border transfers to Brazil?</question>
<answer>The wiki sections I have don't address that. They do cover transfers outside India in general. For Brazil specifically, please check with the SaralPrivacy team or a lawyer. This is general information, not legal advice.</answer>
</example>
</examples>
```
(The user turn is assembled as `<documents><document index="1"><source>…</source><document_content>…</document_content></document>…</documents>` followed by the question.)

Receipt:
```
Prompt Spec
Target model: claude-sonnet-5   Surface: API
Problem addressed: new
Structure: Role: one line | XML tags: how_you_answer, not_legal_advice, style, examples, documents, quotes, answer | Examples: 3, tagged | Long-context: docs-top + query-last
Steering blocks: [x] verbosity [x] hallucination guard (quote-grounded answering) [x] markdown policy (light) [ ] others n/a
Calibration: adaptive thinking, effort low/medium; no budget_tokens, no prefill (the <answer> tag handles shape). Optionally add the "think less often" snippet if latency matters.
Verified: not yet. Hand to shipping-ai-features for a consistency and regression battery plus a legal-advice-refusal test set before ship.
```
Assumption: the examples cite wiki titles I invented, and they must be replaced with real chunks.

## Q2

Files read: SKILL.md, model-deltas.md, snippets.md

Questions I would ask: which model are you calling, and what does the prompt say today about verification and suggestions? Assumption: both symptoms (re-verifying everything and suggesting instead of acting) match the SKILL's Opus 5 and 4.x pattern, so I assume `claude-opus-5` running an agent loop.

```
Model:    claude-opus-5 (assumed)
Surface:  agent loop
Failure:  suggests instead of acting; triple verification
```

Diagnosis, from the SKILL:
1. Suggesting: precise instruction following means the verb decides. A prompt phrased "can you suggest / look at / consider changes" produces suggestions. Fix the phrasing and add a default-to-action block.
2. Re-verifying: inherited self-check instructions ("double-check", "verify your work before finishing", "be thorough") cause over-verification on Opus 5, which already self-verifies. Remove them.

What I would change in your prompt:
- Delete every "verify / double-check / re-read / make sure" line and any "be thorough" scaffolding. If you must keep one check, make it a single concrete criterion (for example "run the test suite once before finishing") and not a general instruction.
- Rewrite suggestion verbs into imperatives: "Suggest improvements to X" becomes "Change X to improve Y."
- Delete any CRITICAL/MUST anti-laziness language, which causes overtriggering.
- Add these blocks to the system prompt:

```text
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is
unclear, infer the most useful likely action and proceed, using tools to discover any
missing details instead of guessing. Try to infer the user's intent about whether a tool
call (e.g., file edit or read) is intended or not, and act accordingly.
</default_to_action>
```
```text
When you're deciding how to approach a problem, choose an approach and commit to it.
Avoid revisiting decisions unless you encounter new information that directly
contradicts your reasoning.
```
Optionally add the conciseness block, since Opus 5 runs long, and the subagent damping block if it over-delegates. If it touches shared systems, add the reversibility block, so that "act by default" stays safe.

Fallback if it still over-explores: lower `effort`.

Receipt: target claude-opus-5 / agent loop; problem: suggests + over-verifies. Removed for this model: self-check and thoroughness instructions. Added: default_to_action, stop-revisiting, conciseness. Verified: not tested here. Run a before/after on 10 representative tasks (action taken rate, token count) via shipping-ai-features.

## Q3

Files read: SKILL.md, model-deltas.md

Cause: both are removed on newer models.
- Assistant-message prefill on the last turn returns 400 on 4.6+ and Mythos Preview. Assistant messages elsewhere in the conversation are fine.
- `budget_tokens` is deprecated on Opus 4.6 / Sonnet 4.6 and returns 400 on 4.7+.

I would ask which model you moved to and what the prefill was for. I assume 4.7 or later (such as claude-opus-5 or claude-sonnet-5), so both changes are needed.

Change 1, thinking:
```python
# Before
thinking={"type": "enabled", "budget_tokens": 10000}

# After
client.messages.create(
    model="claude-opus-5",          # your target
    max_tokens=16000,                # hard ceiling on output
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},   # depth knob; lower it to cut cost/latency
    messages=[...],
)
```
Remove `budget_tokens`. Use `effort` for depth and `max_tokens` as the ceiling. Also check the defaults: Opus 5 and Sonnet 5 have thinking on by default when the parameter is omitted. Opus 4.6 to 4.8 default to off. Fable 5 / Mythos 5 are always on and adaptive only.

Change 2, prefill. The replacement depends on what it did:

| Prefill used for | Replace with |
|---|---|
| Forcing JSON/YAML | Structured outputs, or simply ask for the schema (with retries) |
| Classification label | Tool with an enum field, or structured outputs |
| Skipping preamble ("Here is...") | Instruction: "Respond directly without preamble. Do not start with 'Here is...', 'Based on...'." Or output in XML tags, and strip stragglers in post-processing |
| Bad-refusal steering | Remove it; clear user-message phrasing is enough |
| Continuing an interrupted response | Put it in the user turn: "Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off." |
| Role consistency | Inject reminders into the user turn |

Also run the rest of the migration checklist:
- Soften "CRITICAL: you MUST use tool" language and remove "if in doubt, use [tool]".
- Remove self-check instructions if the target is Opus 5.
- State conciseness explicitly if the target is Opus 5.
- Add subagent damping for Opus 4.6 or Opus 5.

Verify with a regression run before shipping (shipping-ai-features).
