## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

Step 0: Model: claude-sonnet-5 (assumed; "Claude Sonnet" with no version, so I read it as the Sonnet 5 row). Surface: API, RAG Q&A system prompt. Failure: new prompt. Questions I would ask: is it Sonnet 5 or 4.6, and what should the bot do when a user asks something that needs a lawyer? Proceeding on the Sonnet 5 assumption.

Design notes: retrieved chunks change per request, so they go in the user turn (documents first, question last), not in the static system prompt. The system prompt carries the role, the reason for the no-legal-advice rule, grounding rules and examples. Sonnet 5 is terse and literal, so I state the length target and avoid anti-laziness language.

```text
You are the DPDPA compliance guide for SaralPrivacy, answering questions from owners of small and mid-sized Indian businesses who are not lawyers.

<why_this_matters>
Your answers help owners understand India's Digital Personal Data Protection Act. You explain what the law and SaralPrivacy's wiki say. You do not advise on what a specific business should do in its specific situation, because that depends on facts you cannot verify and a wrong answer could expose the owner to penalties. So you explain, and for case-specific decisions you point to a qualified lawyer.
</why_this_matters>

<how_to_answer>
Each user message contains retrieved wiki chunks inside <documents>, followed by the owner's question.
1. In <quotes> tags, copy the passages that bear on the question, each with its source.
2. Then write the answer in <answer> tags, using only what those quotes support.
3. If the chunks do not answer the question, say so plainly in <answer>: "Our wiki doesn't cover this yet." Offer the closest related topic you do have. Do not fill the gap from memory.
</how_to_answer>

<style>
Write in plain, warm English that a shop owner can follow. Define a legal term the first time you use it. Use short flowing paragraphs, with no headings or bullets unless the owner asks for steps. Aim for 80 to 150 words. Cite the wiki article title you relied on at the end.
</style>

<legal_advice_boundary>
Explain what the Act or wiki says and give general examples. When a question asks "should I", "am I liable", "will I be fined" or asks you to judge a particular contract, breach or dispute, give the general rule from the wiki, state that applying it to their case needs a lawyer, and stop there. Do not predict outcomes or penalties for their situation. One sentence of referral is enough; do not repeat disclaimers in every answer.
</legal_advice_boundary>

<examples>
<example>
<question>Do I need consent to email my customers about offers?</question>
<answer>Under the DPDPA, you generally need a customer's consent before using their personal data, and for marketing the consent should be clear and specific to that purpose. Our wiki says the request must say what data you collect and why, and customers must be able to withdraw consent as easily as they gave it. Source: "Consent under DPDPA".</answer>
</example>
<example>
<question>We had a data leak last week. Will we be fined?</question>
<answer>I can explain the rules but cannot say whether you will be fined, since that depends on the facts of your case. The wiki says a breach must be reported to the Data Protection Board and affected people. Because penalties turn on specifics, please speak with a lawyer today. Source: "Breach notification".</answer>
</example>
<example>
<question>What is the penalty for cross-border transfers to Mars?</question>
<answer>Our wiki doesn't cover this yet. The closest topic I have is "Cross-border transfers", which I can summarise if useful.</answer>
</example>
</examples>
```

Prompt Spec
Target model: claude-sonnet-5. Surface: API.
Problem addressed: new prompt.
Structure applied: Role one line; XML tags why_this_matters, how_to_answer, style, legal_advice_boundary, examples; Examples 3 tagged; Long-context layout: docs-top + query-last in user turn.
Steering blocks: quote-grounded answering [x], verbosity (explicit length) [x], markdown policy (positive prose instruction) [x], hallucination guard (not-in-docs fallback) [x]. Others n/a.
Model calibration: Thinking config adaptive, effort low or medium (simple Q&A; Sonnet 5 defaults thinking on). Removed: any "CRITICAL/MUST" emphasis. Added: explicit length, reasons.
Verified: not run (dry run). Next, shipping-ai-features for regression set (advice-seeking questions, out-of-wiki questions) before production.

## Q2

Files read: SKILL.md, model-deltas.md, snippets.md

Step 0: Model: not stated. Surface: agent loop. Failure: suggests instead of acting; verifies everything three times. Question I would ask: which model id? Assumption: Opus 5 (the row where over-verification is documented). If it is Sonnet 5 or older, the verification fix differs slightly (see below).

Diagnosis. Two causes. First, the verb: if the prompt or users say "can you suggest / review / look at", Claude suggests. The verb decides the behavior. Second, inherited "double-check", "be thorough", "verify before finishing" lines, which current models layer on top of their own self-verification, giving repeated checks.

Fix, in three edits to the system prompt:

1. Add the action default (snippets.md):

```text
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is unclear, infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing. Try to infer the user's intent about whether a tool call (e.g., file edit or read) is intended or not, and act accordingly.
</default_to_action>
```

2. Delete every inherited "double-check your work", "verify three times", "re-read before answering" instruction. On Opus 5 the Self-check snippet is explicitly removed because it self-verifies. If the target is Sonnet 5 or 4.6, keep one bounded check instead of deleting everything:

```text
Verify once, against the stated acceptance criteria, before reporting done. Do not re-run checks that already passed unless you changed something afterwards.
```

3. If it still over-explores, add the commitment block and lower effort:

```text
When you're deciding how to approach a problem, choose an approach and commit to it. Avoid revisiting decisions unless you encounter new information that directly contradicts your reasoning.
```

Also check: remove "CRITICAL / MUST / if in doubt" phrasing near tools, since it causes overtriggering. Rewrite any user-facing task templates from "Can you suggest changes to..." to "Change X so that...". If the agent touches shared systems, add the reversibility block so acting-by-default stays safe. Since Opus 5 runs long, add the conciseness block. If the loop still re-verifies, lower `output_config.effort`.

Prompt Spec
Target model: assumed claude-opus-5. Surface: agent loop.
Problem addressed: advice-not-action; over-verification.
Steering blocks: action-vs-advice [x], autonomy and reversibility [x if shared systems], verbosity [x]; self-check removed.
Model calibration: Thinking adaptive; effort: lower one level if needed. Removed: double-check instructions, anti-laziness wording. Added: default_to_action.
Verified: not run. Test on the failing transcripts, then shipping-ai-features for regression scoring.

## Q3

Files read: SKILL.md, model-deltas.md

Step 0: Model: a newer Claude model (exact id not given; I would ask). Per model-deltas, both changes cause a 400 on 4.6+ for prefill and 4.7+ for budget_tokens. Surface: API. Failure: 400 error.

Two separate causes, two fixes.

1. budget_tokens. It is deprecated on Opus 4.6 / Sonnet 4.6 and returns 400 on 4.7 and later. Use adaptive thinking plus effort; use max_tokens as the hard ceiling.

```python
# Before
thinking={"type": "enabled", "budget_tokens": 10000}

# After
client.messages.create(
    model="claude-opus-5",  # or your target
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[...],
)
```

Also check the thinking default: Opus 5 and Sonnet 5 have thinking on when the parameter is omitted (Fable/Mythos always on, adaptive only), while 4.6 to 4.8 default off. Opus 5 can only be disabled at effort high or lower.

2. Prefill. A partial assistant message on the last turn returns 400. Assistant messages elsewhere in the conversation are fine. Replace by what the prefill did:

- Forcing JSON or a schema: use Structured Outputs, or just ask in the prompt (current models match schemas reliably; add retries).
- Classification labels: a tool with an enum field, or structured outputs.
- Killing preamble such as "Here is the summary:": add "Respond directly without preamble. Do not start with 'Here is...', 'Based on...'." Or have the output go in XML tags or a tool call, and strip stragglers in post-processing.
- Steering around refusals: delete it; clear phrasing in the user message is enough.
- Continuing an interrupted response: move it to the user turn ("Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off."), or retry.
- Role consistency or context hydration: inject reminders into the user turn, hydrate via tools, or handle in compaction.

Tell me which of these your prefill did and I will write the exact replacement. Since you are migrating, also run the checklist: soften "MUST use tool" language, drop "if in doubt, use tool", and remove self-verification lines if the target is Opus 5.

Prompt Spec
Target model: newer model (id to confirm). Surface: API.
Problem addressed: 400 on prefill and budget_tokens.
Model calibration: Thinking config adaptive + effort high (starting point). Removed: prefill, budget_tokens. Added: no-preamble instruction or structured output.
Verified: not run; re-send the failing request, then regression-score via shipping-ai-features.
