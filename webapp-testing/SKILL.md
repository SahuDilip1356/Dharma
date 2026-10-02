---
name: webapp-testing
description: |
  Verifies user-facing web UI in a real browser with Playwright (Python): functional
  behavior, all states (loading, error, empty, success), console and network errors, and
  before/after screenshots as evidence. Use when a UI feature or UI bug fix needs browser
  proof before ship, or when the user says "test it in the browser", "does the form
  work", or "check the UI end to end". Not for unit tests (superpowers-tdd) or visual
  fidelity (reviewing-ui).
license: MIT
metadata:
  author: Anthropic (adapted for Dharma by Dilip Sahu)
  version: "1.0.0"
---

# Web Application Testing

**Core rule:** screenshots and console logs are evidence. DOM inspection before
`networkidle` is not — always `page.wait_for_load_state('networkidle')` first.

Answers one question: does the UI actually work in a real browser? Use it in Verify for
every user-facing feature and for UI bug fixes (before/after proof); optionally in Build
for quick feedback. Its screenshots prove functional states; `reviewing-ui` screenshots
prove visual fidelity; unit tests belong to `superpowers-tdd`.

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

## Running as a parallel subagent

Receives a server URL (or start command), the flows to verify, and an evidence output
path. Produces per-flow screenshots, a console log file, and a pass/fail summary per
state. The orchestrator (`superpowers-execute`) starts the server once, fans flows out to
browser agents, and hands the evidence to `superpowers-verify`.

## Reference files

- `scripts/with_server.py` — server lifecycle manager (run with `--help`; use as a black box)
- `examples/element_discovery.py` — discover buttons, links, inputs on a running page
- `examples/static_html_automation.py` — automate static HTML via `file://` URL
- `examples/console_logging.py` — capture and save browser console output

Adapted from https://github.com/anthropics/skills/tree/main/webapp-testing.
