---
name: prompt-engineering
description: |
  Authors and calibrates prompts for current Claude models (Fable, Mythos, Opus, Sonnet,
  Haiku) — structure, examples, formatting control, thinking/effort config, tool-call
  steering, and agentic-loop design. Use when writing or rewriting a system prompt for a
  Claude-powered feature; when output is the wrong shape (too long, too formal, too much
  markdown); when the model suggests instead of acting, over-explores, or over-verifies;
  when migrating a prompt to a newer Claude model (or hitting a 400 on prefill /
  budget_tokens); or when designing an agent that spans multiple context windows.
license: MIT
metadata:
  author: Dilip Sahu
  version: "1.1.0"
  source: Anthropic — Prompt engineering best practices
---

# Claude Prompt Engineering

**Core rule:** a prompt is a spec for a specific model. Write the spec, then calibrate it
to the model in the call. Guidance tuned for an older model misfires on a newer one
(anti-laziness prompting becomes overtriggering; verification instructions become
over-verification).

Not this skill: prompt versioning, regression testing, model selection, cost ceilings and
pre-ship gates. Those belong to `shipping-ai-features`.

Companion files:
- [model-deltas.md](model-deltas.md) — per-model behavior, thinking/effort config, prefill removal, migration checklist
- [snippets.md](snippets.md) — paste-ready system-prompt blocks for each steering problem below

---

## Step 0: Name the target

```
Model:    [exact model id]
Surface:  [API feature / agent loop / Claude Code skill / one-off task]
Failure:  [what is wrong today — or "new prompt"]
```

If the model is not decided, stop and hand off to `shipping-ai-features`.
Then read the model's row in `model-deltas.md`. Most prompt bugs are last-generation
guidance applied to a current model.

## Step 1: Write the spec

Test: would a colleague with no context understand it? If not, neither will Claude.

| Do | Instead of |
|---|---|
| State the output format and constraints explicitly | Hoping the model infers house style |
| Numbered steps when order or completeness matters | A paragraph of intent |
| Explain *why* a rule exists | A bare prohibition — Claude generalizes from the reason |
| Ask for "above and beyond" explicitly when you want it | Expecting effort from a vague prompt |
| Say what to do | Saying what not to do |

```
Weak:   NEVER use ellipses
Strong: Your response will be read aloud by a text-to-speech engine, so never use
        ellipses — the engine cannot pronounce them.
```

Set a one-sentence role in the system prompt.

## Step 2: Structure it

- **XML tags** separate instructions, context, examples and variable input. Use consistent,
  descriptive names.
- **Examples** are the strongest formatting/tone lever: 3–5 in `<example>` tags inside
  `<examples>`, relevant to the real use case and diverse enough to cover edge cases.
- **Long context (20k+ tokens):** documents at the top, query at the end (up to ~30% better
  on complex multi-document inputs), each wrapped as `<document index="n">` with
  `<source>` + `<document_content>`. For grounded answers, have Claude quote the relevant
  passages into `<quotes>` first, then answer only from them — and say what to do when the
  answer isn't in the documents.

## Step 3: Control the output shape

In order of effectiveness:
1. **Positive instruction** — "Write in flowing prose paragraphs," not "no markdown."
2. **XML format indicator** — "Write the answer in `<prose_answer>` tags."
3. **Style mirroring** — markdown in the prompt produces markdown in the response.
4. **Explicit formatting policy** — the anti-markdown block in `snippets.md`.

State length targets explicitly. Default verbosity differs by model — see `model-deltas.md`.

## Step 4: Steer action vs. advice

The verb decides the behavior: "Can you suggest changes…" → suggestions;
"Change this function…" → edits. Encode the default you want with `<default_to_action>`
or `<do_not_act_before_instructions>` from `snippets.md`.

- Drop anti-laziness emphasis ("CRITICAL: You MUST use this tool…") — it causes
  overtriggering on current models. Plain "Use this tool when…" is enough.
- Make tool defaults conditional ("Use [tool] when it would improve your understanding"),
  and delete "if in doubt, use [tool]".
- Bound exploration and verification explicitly when a model over-does them; remove
  inherited "double-check your work" instructions on models that self-verify
  (per-model notes in `model-deltas.md`).

## Step 5: Configure thinking

Thinking is an API setting, not prose. Use adaptive thinking sized with `effort`; cap with
`max_tokens` or lower effort. `budget_tokens` is deprecated and returns a 400 on newer
models, and so does assistant-message prefill — replacements for both are in
`model-deltas.md` (sections 2–3).

Within thinking: prefer "think thoroughly" over a hand-written step plan, use `<thinking>`
tags in few-shot examples to teach a reasoning style, and ask for reflection after tool
results in agent loops.

## Step 6: Agentic design (only if it runs in a loop)

| Concern | Practice |
|---|---|
| State | Structured JSON (`tests.json`) + freeform `progress.txt`; git for checkpoints |
| First vs. later windows | Window 1 builds the framework (tests, `init.sh`); later windows iterate a todo list |
| Restarting | Prefer a fresh window with a prescriptive orientation ("review progress.txt, tests.json, git log; run the integration test first") |
| Test integrity | "It is unacceptable to remove or edit tests." |
| Early stopping | Tell the model what the harness does when context fills, or it wraps up early |
| Verification | Give it a way to check its own work (browser automation, computer use) |
| Shared systems | Include the reversibility block from `snippets.md` |
| Research loops | Success criteria, cross-source verification, competing hypotheses in a notes file |

Subagent over-delegation and context-awareness differ by model — see `model-deltas.md`.

## Anti-patterns not covered above

| Anti-pattern | Why it fails |
|---|---|
| Reusing a prompt across a model upgrade unread | Steering overtriggers, verification over-verifies, thinking config may 400 |
| Letting an agent loop run with no state file | No recovery, no resume, no evidence |
| Accepting default "AI slop" frontend output | Purple-on-white, Inter/Roboto, predictable layouts — commit to an aesthetic |

## Output format

Close prompt work with this receipt:

```
Prompt Spec
─────────────────────────────────────────────
Target model: [id]        Surface: [API / agent loop / skill]
Problem addressed: [what was wrong, or "new"]

Structure applied:
  Role: [one-line role, or none]
  XML tags: [list]
  Examples: [N, tagged / none]
  Long-context layout: [docs-top + query-last / n/a]

Steering blocks included (from snippets.md):
  [ ] verbosity / conciseness      [ ] markdown & formatting policy
  [ ] action-vs-advice default     [ ] parallel tool calls
  [ ] thinking frequency           [ ] overengineering guard
  [ ] subagent damping             [ ] autonomy & reversibility
  [ ] context-budget persistence   [ ] anti-hardcoding
  [ ] hallucination guard          [ ] frontend aesthetics

Model calibration (from model-deltas.md):
  Thinking config: [adaptive / off / always-on] + effort: [level]
  Removed for this model: [...]
  Added for this model: [...]

Verified: [how the change was tested — then shipping-ai-features for
           consistency + regression scoring before production]
─────────────────────────────────────────────
```
