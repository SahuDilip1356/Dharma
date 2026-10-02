## Q1

Files read: SKILL.md, model-deltas.md, snippets.md

**Step 0: Target**
```
Model:    claude-sonnet-5
Surface:  API feature (RAG Q&A bot)
Failure:  new prompt
```
From the Sonnet 5 row in model-deltas.md: it is terse by default, follows instructions literally and has thinking on by default. So the prompt states the length and format explicitly, gives the reason behind every rule, and leaves out any "be thorough" or "MUST" emphasis.

**System prompt**
```text
You are SaralPrivacy's DPDPA assistant. You help owners of small and medium Indian
businesses understand what the Digital Personal Data Protection Act, 2023 and its Rules
ask of them, in plain language.

<context>
The people asking are usually founders, shop owners or ops managers, not lawyers. They
want to know what a requirement means and what to do next. Every answer you give must
come only from the wiki passages in <documents>. Those passages are reviewed by our
privacy team. Your general knowledge of DPDPA may be out of date or wrong, so do not use
it.
</context>

<instructions>
1. Read the user's question and the passages in <documents>.
2. Copy the passages that are relevant into <quotes>, each one with its index number.
3. Answer in <answer>, using only what those quotes support. Cite the passage index
   after each claim, like [2].
4. If the passages do not cover the question, say plainly that our guidance doesn't
   cover it yet, and suggest they contact the SaralPrivacy team or a qualified privacy
   lawyer. Do not fill the gap from memory, because a confident wrong answer about a
   legal duty can cost a business a penalty.
5. Explain what the law requires and what businesses generally do about it. Do not tell
   a specific business whether it is compliant, whether it is liable, or what it should
   do in a dispute, notice or breach investigation. That is legal advice, and we are not
   a law firm. When a question asks for that, explain the general rule from the
   passages and recommend that they consult a lawyer for their specific situation.
</instructions>

<format>
Write 80–200 words of plain, warm prose for a non-lawyer. Use short paragraphs and no
headings. Use a short numbered list only when you are giving steps. Define each legal
term the first time it appears (e.g. "Data Fiduciary — the business that decides why
and how personal data is used"). End with one line: "This is general guidance, not
legal advice."
</format>

<examples>
  <example> [covered question → quotes, cited answer] </example>
  <example> [not covered → honest "not in our guidance" + referral] </example>
  <example> [asks "am I liable for X?" → general rule + lawyer referral] </example>
  <example> [Hinglish / informal question → same plain-English answer] </example>
</examples>
```
User turn, where the documents go first and the query goes last:
```xml
<documents>
  <document index="1"><source>{{wiki_slug}}</source>
    <document_content>{{chunk}}</document_content></document>
  ...
</documents>
<question>{{user_question}}</question>
```
Your app should show only what's inside `<answer>`.

**API config:** `thinking={"type":"adaptive"}` and `output_config={"effort":"low"}`. Q&A grounded in retrieved passages doesn't need deep reasoning. Raise the effort only if your evals show it misses nuance in the passages. `max_tokens` around 1024. Don't use prefill.

**I'd like you to confirm:** (a) the exact wording of the disclaimer, which your counsel should approve; (b) whether you want answers in Hindi when the user writes in Hindi; (c) the escalation contact. To keep the copy on-brand, apply the `saralprivacy-brand` voice rules to the examples.

```
Prompt Spec
─────────────────────────────────────────────
Target model: claude-sonnet-5     Surface: API
Problem addressed: new
Structure applied:
  Role: SaralPrivacy DPDPA assistant for SMB owners
  XML tags: context, instructions, format, examples, documents, quotes, answer
  Examples: 4, tagged (to be filled from real wiki Q&As)
  Long-context layout: docs-top + query-last
Steering blocks: [x] verbosity  [x] formatting policy  [x] hallucination guard
Model calibration:
  Thinking config: adaptive + effort: low
  Removed for this model: emphasis/MUST language, prefill
  Added for this model: explicit length target, reasons on every rule
Verified: not yet. Next, run a set of covered, uncovered and legal-advice-bait
  questions, then use shipping-ai-features for regression scoring before launch.
─────────────────────────────────────────────
```

## Q2

Files read: SKILL.md, snippets.md, model-deltas.md

**Questions first:** Which model ID is the agent on? Can you paste the current system prompt? Does the agent touch shared systems, like git push, databases or messages to other people?

Below I assume **claude-opus-5** with an inherited prompt. Both symptoms match that model's row in model-deltas.md. Opus 5 already checks its own work, so any leftover "verify/double-check" instruction makes it over-verify. "Suggest" behaviour usually comes from the verbs in the prompt or an advice-first default.

**What I'd change in the prompt:**

1. **Remove** every self-check line, such as "Before you finish, verify…", "double-check your work", "be thorough" or "re-run tests to confirm". The skill says to take these out for Opus 5.
2. **Remove** anti-laziness emphasis ("CRITICAL: you MUST use…") and any "if in doubt, use [tool]" lines. Rewrite them as plain conditionals, e.g. "Use the test runner when a change affects behaviour."
3. **Reword** advice verbs: "suggest/recommend/propose changes" becomes "make the change." Delete any `<do_not_act_before_instructions>` block.
4. **Add** the action default:
```text
<default_to_action>
By default, implement changes rather than only suggesting them. If the user's intent is
unclear, infer the most useful likely action and proceed, using tools to discover any
missing details instead of guessing.
</default_to_action>
```
5. **Add** a single explicit verification bound to replace the removed lines:
```text
Run the relevant tests once after your change. If they pass, report and stop. Re-verify
only if a later edit touches the same code.
```
6. **Add** conciseness, since Opus 5 runs long:
```text
Keep responses as short as the task allows. State the result, then stop.
```
7. If it touches shared systems, also paste the **autonomy vs. reversibility** block so it asks before it pushes, deletes or sends anything. It still edits local files freely.

**Fallback:** if it still over-verifies after these prompt changes, lower `output_config.effort` by one level.

**Test:** replay 5–10 recent sessions where it only suggested or verified three times. Count edits made vs. suggestions, and verification calls per task. Then use `shipping-ai-features` for regression scoring.

If the model turns out to be Opus 4.6 instead, keep steps 3–4. Instead of removing the self-check, add the "stop revisiting decisions" block and make the tool defaults conditional. Over-exploring is that model's failure mode.

## Q3

Files read: SKILL.md, model-deltas.md

There are two separate 400s here. Both changed starting with 4.6/4.7 (model-deltas.md, sections 2–3).

**1. `budget_tokens` returns 400 on 4.7 and later.** Switch to adaptive thinking with `effort`, and use `max_tokens` as the hard ceiling:
```python
# Before
thinking={"type": "enabled", "budget_tokens": 10000}
# After
thinking={"type": "adaptive"},
output_config={"effort": "high"},   # low / medium / high
max_tokens=16000,
```
Note that thinking is **on by default** on Opus 5 / Sonnet 5, and always on for Fable/Mythos. If your old prompt assumed it was off, retest output length and latency.

**2. Prefill on the final assistant turn returns 400.** Assistant messages earlier in the conversation are fine. What you replace it with depends on why you prefilled:

| You prefilled to… | Replace with |
|---|---|
| Force JSON / `{` | Structured Outputs, or just ask for the schema |
| Force a label | A tool with an enum field, or structured outputs |
| Skip preamble ("Here is the summary:") | "Respond directly without preamble. Do not start with 'Here is…', 'Based on…'." Strip anything left over in post-processing |
| Continue an interrupted reply | Put it in the user turn: "Your previous response was interrupted and ended with `[…]`. Continue from where you left off." |
| Hold a persona/role | Put reminders in the user turn, or hydrate through tools |
| Avoid refusals | Usually not needed anymore. Clear wording in the user message is enough |

**What I need from you:** what the prefill contained. Tell me that and I'll write the exact replacement.

While you're migrating, also check the rest of the migration list. Soften "MUST use tool" language. Remove "if in doubt, use [tool]". If you're targeting Opus 5, remove self-verification instructions and state conciseness explicitly. Then run your eval set before you ship.
