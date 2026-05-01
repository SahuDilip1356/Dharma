---
name: webapp-testing
description: |
  Browser-level UI verification using Playwright (Python). Triggers at Phase 4 (Verify)
  when:
  - A user-facing feature is built and needs functional UI verification before ship
  - A bug fix touches UI and needs before/after browser proof
  - A UI redesign needs state verification (loading, error, empty, success all tested)
  - superpowers-execute is running multi-agent verification and needs a browser specialist

  Part of the Dharma multi-agent verification pattern:
    superpowers-execute delegates in parallel →
      webapp-testing     (browser functional verification)
      superpowers-tdd    (unit + integration tests)
      uiux-design-qa     (visual fidelity)
      uiux-accessibility-review (a11y on live UI)

  Does NOT own: visual design fidelity screenshots (that is uiux-design-qa);
  unit/integration tests (that is superpowers-tdd);
  post-ship production monitoring (that is ai-observability).

  Source: https://github.com/anthropics/skills/tree/main/webapp-testing
license: MIT
metadata:
  author: Anthropic (adapted for Dharma by Dilip Sahu)
  version: "1.0.0"
---

# Web Application Testing

**Core rule: Screenshots and console logs are evidence. DOM inspection before `networkidle` is not.**

This skill produces browser-level functional evidence for `superpowers-verify` to cite.
It does not replace unit tests (`superpowers-tdd`) or visual QA (`uiux-design-qa`) —
it fills the gap between them: does the UI actually work in a real browser?

---

## Dharma Phase Placement

| Phase | Role |
|---|---|
| Phase 4 — Verify | Primary phase for this skill |
| Phase 3 — Build | Optional: use for rapid UI feedback during development |

**Mandatory for:** all user-facing features (Routes A, B, D)
**Conditional for:** bug fixes with a UI component (Route C), releases with UI changes (Route H)

---

## Decision Tree: Choosing Your Approach

```
Is the app static HTML?
    ├─ Yes → Read HTML directly, write Playwright script using file:// URL
    │
    └─ No (dynamic: React, Next.js, Vue) → Is the dev server already running?
        ├─ Yes → Reconnaissance-then-action:
        │         1. Navigate + wait for networkidle
        │         2. Screenshot + DOM inspect
        │         3. Identify selectors from rendered state
        │         4. Execute actions + capture evidence
        │
        └─ No → Use scripts/with_server.py to manage server lifecycle
                 Then write simplified Playwright automation script
```

---

## Helper Script

**`scripts/with_server.py`** — manages server lifecycle automatically.

Run `--help` first before reading the source. Use it as a black box.

```bash
# Single server (Next.js / React)
python scripts/with_server.py --server "npm run dev" --port 3000 -- python your_test.py

# Multiple servers (backend + frontend)
python scripts/with_server.py \
  --server "cd backend && node server.js" --port 4000 \
  --server "cd frontend && npm run dev" --port 3000 \
  -- python your_test.py
```

---

## Reconnaissance-Then-Action Pattern

Every dynamic app test follows this sequence:

**Step 1 — Inspect**
```python
page.goto('http://localhost:3000')
page.wait_for_load_state('networkidle')   # CRITICAL — never skip this
page.screenshot(path='/tmp/inspect.png', full_page=True)
content = page.content()
buttons = page.locator('button').all()
```

**Step 2 — Identify selectors** from the screenshot and DOM output

**Step 3 — Execute + capture evidence**
```python
page.click('text=Book Appointment')
page.wait_for_selector('[data-testid="confirmation"]')
page.screenshot(path='/tmp/after_action.png', full_page=True)
```

---

## Dharma Evidence Standard

This skill must produce at least one of these evidence types for `superpowers-verify`:

| Evidence Type | How to produce |
|---|---|
| **Screenshot — before action** | `page.screenshot(path='/tmp/before.png', full_page=True)` |
| **Screenshot — after action** | `page.screenshot(path='/tmp/after.png', full_page=True)` |
| **DOM state** | `page.content()` or `page.locator('...').inner_text()` |
| **Console log** | `page.on("console", handler)` — capture errors and warnings |
| **Network errors** | `page.on("requestfailed", handler)` — catch failed API calls |

Minimum evidence for a passing verify gate:
- Before screenshot (initial state)
- Action performed (described)
- After screenshot (result state)
- Console log (no unexpected errors)

---

## State Coverage Requirement

For any user-facing feature, test all four states:

| State | What to verify |
|---|---|
| **Loading** | Spinner or skeleton renders; UI does not show stale data |
| **Empty** | Empty state renders correctly; no blank white screen |
| **Error** | Error message renders; user can recover (retry button, etc.) |
| **Success** | Happy path completes; confirmation visible |

---

## Multi-Agent Integration (superpowers-execute)

When running as a subagent in a parallel verification run:

```python
# webapp-testing agent receives:
#   - local server URL or start command
#   - list of flows to verify
#   - evidence output path

# webapp-testing agent produces:
#   - screenshots per flow saved to output path
#   - console.log file
#   - pass/fail summary per state tested

# superpowers-verify synthesizes all subagent outputs into final evidence claim
```

The orchestrating agent (`superpowers-execute`) should:
1. Start server once (shared across all browser subagents)
2. Delegate flows to browser agents in parallel
3. Collect evidence files
4. Pass to `superpowers-verify` for synthesis

---

## Ownership Boundary

| Owns | Does NOT Own |
|---|---|
| Functional state verification (does the button work, does the form submit) | Visual design fidelity (that is `uiux-design-qa`) |
| Console error detection | Unit and integration test logic (that is `superpowers-tdd`) |
| Browser-level DOM and network inspection | Post-ship production monitoring (that is `ai-observability`) |
| Before/after functional screenshots | Design-to-implementation comparison screenshots (that is `uiux-design-qa`) |

**Screenshot disambiguation:** `webapp-testing` screenshots prove functional states.
`uiux-design-qa` screenshots prove visual fidelity against the design spec.
Both can run in the same verification pass — they answer different questions.

---

## Common Pitfall

❌ **Don't** inspect the DOM before `networkidle` on dynamic apps — you will get partial renders
✅ **Do** always call `page.wait_for_load_state('networkidle')` before any inspection or action

---

## Reference Files

- `scripts/with_server.py` — server lifecycle manager
- `examples/element_discovery.py` — discover buttons, links, inputs on a running page
- `examples/static_html_automation.py` — automate static HTML via `file://` URL
- `examples/console_logging.py` — capture and save browser console output
