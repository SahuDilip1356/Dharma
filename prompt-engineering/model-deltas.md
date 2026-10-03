# Model Deltas — What Changes Per Model

## Contents

- [1. Behavior Deltas](#1-behavior-deltas)
- [2. Thinking & Effort Configuration](#2-thinking--effort-configuration)
- [3. Prefill Is Gone (4.6+ and Mythos Preview)](#3-prefill-is-gone-46-and-mythos-preview)
- [4. Migration Checklist (any older model → current)](#4-migration-checklist-any-older-model--current)
- [5. Model Self-Knowledge](#5-model-self-knowledge)

Read the row for the model you are calling before writing or migrating a prompt.
Model IDs: `claude-fable-5`, `claude-mythos-5`, `claude-opus-5`, `claude-opus-4-8`,
`claude-sonnet-5`, `claude-haiku-4-5-20251001`.

---

## 1. Behavior Deltas

| Model | Runs long / short by default | Prompt changes that matter |
|---|---|---|
| **Fable 5 / Mythos 5** | — | Thinking always on, adaptive only. Watch effort levels, long-run progress claims (may overstate progress on long tasks — ask for fact-based status), memory-system scaffolding, and the `reasoning_extraction` refusal category |
| **Opus 5** | **Longer** than prior models | Prompt explicitly for conciseness — effort does *not* reliably change visible length. **Remove inherited self-verification instructions** (over-verifies). Damp subagent delegation. More self-correcting; less need for progress-narration prompts. Do not carry over "be thorough" scaffolding |
| **Opus 4.8** | Terser | Calibrate effort/thinking depth; tool-use triggering; literal instruction following; subagent control; design/frontend defaults |
| **Opus 4.6** | Terser | Over-explores at high effort — replace blanket tool defaults with conditional ones and remove "if in doubt" phrasing. Strong subagent predilection. Add the reversibility block for anything touching shared systems |
| **Opus 4.5** | Terser | Overengineers (extra files, abstractions, unrequested flexibility) — include the overengineering guard. With thinking off, avoid the word "think"; use *consider* / *evaluate* / *reason through*. Improved vision — a crop/zoom tool measurably lifts image evals |
| **Sonnet 5** | Terser | Response length, effort and thinking-depth calibration, tool-use triggering, literal instruction following, design/frontend defaults. Has context awareness |
| **Sonnet 4.6** | Terser | Adaptive thinking; context awareness |
| **Haiku 4.5** | Terser | Context awareness |

**Applies to every current model:** more direct, grounded progress reports (not
self-celebratory); more conversational; may skip post-tool-call summaries entirely.
Ask for a summary if you need the visibility.

---

## 2. Thinking & Effort Configuration

| Model | Default when `thinking` omitted | Config | Can disable? |
|---|---|---|---|
| Fable 5 / Mythos 5 | **On** — always | Adaptive only, regardless of the parameter | No |
| Opus 5 | **On** | `{type: "adaptive"}` + `output_config.effort` | Only at effort `high` or lower |
| Sonnet 5 | **On** | `{type: "adaptive"}` + effort | Yes |
| Opus 4.6 – 4.8, Sonnet 4.6 | **Off** | `{type: "adaptive"}` + effort | Yes (omit the parameter) |
| Older models | Off | Extended thinking with `budget_tokens` | Yes |

Rules:
- `budget_tokens` is **deprecated** on Opus 4.6 / Sonnet 4.6 and returns a **400 error on
  4.7 and later**. Use `effort` for depth and `max_tokens` for a hard ceiling.
- Adaptive thinking calibrates on two inputs: the `effort` parameter and query
  complexity. Easy queries get a direct answer.
- Use adaptive thinking for agentic work — multi-step tool use, complex coding,
  long-horizon loops.
- Thinking frequency is promptable. Large or complex system prompts increase it; the
  "respond directly" snippet dials it back.
- **Opus 5 with thinking disabled** can leak internal XML tags into visible output.
  Prefer keeping thinking on at a lower effort over manual `<thinking>`/`<answer>` CoT.
- Lower `effort` is the fallback for any model that keeps over-exploring after
  prompt changes.

Migration shape:

```python
# Before — extended thinking, manual budget (older models)
client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "..."}],
)

# After — adaptive thinking + effort
client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[{"role": "user", "content": "..."}],
)
```

If you were not using extended thinking, no change is required — but check the
default-on column above, because 4.8-and-earlier prompts assumed thinking was off.

---

## 3. Prefill Is Gone (4.6+ and Mythos Preview)

A partial assistant message on the **last** turn returns **400**. Assistant messages
elsewhere in the conversation are unaffected. Migrations by use case:

| Prefill was used for | Replacement |
|---|---|
| Forcing JSON/YAML/schema | **Structured Outputs**. Or just ask — current models match complex schemas reliably, especially with retries |
| Classification labels | Tool with an enum field, or structured outputs |
| Killing preamble (`"Here is the summary:\n"`) | Instruction: "Respond directly without preamble. Do not start with 'Here is…', 'Based on…'." Or output inside XML tags / a tool call. Strip stragglers in post-processing |
| Steering around bad refusals | Not needed — refusal behavior is much better. Clear phrasing in the user message suffices |
| Continuations after interruption | Move it to the user turn: "Your previous response was interrupted and ended with `[previous_response]`. Continue from where you left off." Or just retry if there is no UX penalty |
| Context hydration / role consistency | Inject reminders into the user turn; hydrate through tools; or handle it during context compaction |

Do not port parameter names from other providers: Claude's Messages API has no
`response_format`. Look up the current structured-outputs parameter in the Claude API
docs (or use a tool with an `input_schema`) rather than guessing.

---

## 4. Migration Checklist (any older model → current)

```
[ ] Thinking config: budget_tokens removed → adaptive + effort
[ ] Thinking default checked (on vs. off when the parameter is omitted)
[ ] Prefill on the final assistant turn removed
[ ] Anti-laziness / "MUST use tool" language softened to plain phrasing
[ ] "If in doubt, use [tool]" removed
[ ] Blanket tool defaults → conditional ("when it would help because…")
[ ] Self-check / verification instructions: kept, except REMOVED for Opus 5
[ ] Conciseness stated explicitly if the target is Opus 5
[ ] Subagent damping added if the target is Opus 4.6 or Opus 5
[ ] Animations / interactive elements requested explicitly (not assumed)
[ ] Quality modifiers added where "above and beyond" is wanted
[ ] Reversibility block added if the loop touches shared systems
```

---

## 5. Model Self-Knowledge

When the app must state its own identity or emit model strings:

```
The assistant is Claude, created by Anthropic. The current model is Claude Opus 5.
```

```
When an LLM is needed, default to Claude Opus 5 unless the user requests otherwise.
The exact model string for Claude Opus 5 is claude-opus-5.
```

Default new AI application work to the latest, most capable Claude model.
