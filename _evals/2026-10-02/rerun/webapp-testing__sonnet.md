## Q1
Files read: SKILL.md, examples/element_discovery.py, examples/console_logging.py

Dynamic app, server already running on :3000, so I use the Reconnaissance-then-Action path (no with_server.py). The skill's core rule applies: wait for `networkidle` before inspecting the DOM.

**Step 1 - Recon** (`/tmp/recon.py`, based on element_discovery.py):
```bash
python /tmp/recon.py   # goto localhost:3000/settings, wait networkidle, screenshot, list inputs/buttons/checkboxes
```
Evidence: `/tmp/page_discovery.png` plus the list of consent checkboxes/toggles and the Save button. I pick selectors from the rendered output. I have not seen the real form, so I will not guess them.

**Step 2 - Test script** (`/tmp/test_consent.py`). Console and requestfailed handlers are attached before `goto`, as in console_logging.py. It also logs responses with status >= 400.
```python
page.on("console", ...); page.on("requestfailed", ...)
page.goto('http://localhost:3000/settings'); page.wait_for_load_state('networkidle')
page.screenshot(path='/tmp/consent_before.png', full_page=True)
# Success: toggle a preference, click Save, wait for confirmation
page.get_by_label('Marketing emails').check()
page.get_by_role('button', name='Save').click()
page.wait_for_selector('[role=status], text=Saved')
page.screenshot(path='/tmp/consent_success.png', full_page=True)
# Persistence: reload and assert the toggle is still checked
page.reload(); page.wait_for_load_state('networkidle')
assert page.get_by_label('Marketing emails').is_checked()
```

**Step 3 - Cover all four states** (required for a user-facing feature):
- Loading: `page.route('**/api/consent*', lambda r: (time.sleep(2), r.continue_()))`. Screenshot a skeleton or spinner and confirm there is no stale data.
- Empty: route returns no preferences. Check that the empty or default state renders and the page is not blank.
- Error: `route.fulfill(status=500)`. Check that an error message shows and the user can retry. Then retry and confirm success.
- Success: the happy path above.

**Run:**
```bash
python /tmp/test_consent.py   # server already up; otherwise: python scripts/with_server.py --help first, then wrap it
```

**Evidence for superpowers-verify:** before and after screenshots per state, `/tmp/console.log` (errors/warnings/network-error), DOM assertions, and a pass/fail line per state.

**Gate:** if `console.log` has unexpected errors, I do not report the gate as passed.

**Limits:** headless Playwright proves behavior, not visual polish (that is reviewing-ui). Backend persistence is only checked via reload. I make no claim about legal wording of the consent text.

## Q2
Files read: SKILL.md, examples/console_logging.py

This is a UI bug fix, which the skill covers with before/after proof. Honest framing: "prove the fix works" means showing the bug on the old code and a pass on the new code, not just a pass on the new code.

**Before (bug reproduction):** I need the pre-fix state. I would ask: "Is the pre-fix code available (branch, commit, or stash)?" If so, `git stash` or `git checkout <pre-fix-sha>`, restart the server, and run the same script. If not, I state plainly that I can only show the after state and cannot prove the regression, and I label it that way.

**Same script, run twice:**
```python
page.on("console", ...); page.on("requestfailed", ...)
page.on("response", lambda r: r.status >= 400 and logs.append(f"[http {r.status}] {r.url}"))
reqs = []
page.on("request", lambda r: r.method in ("POST","PUT","PATCH") and reqs.append(r.url))
page.goto('http://localhost:3000/billing'); page.wait_for_load_state('networkidle')
page.screenshot(path=f'/tmp/billing_{tag}_before_click.png', full_page=True)
page.get_by_role('button', name='Save').click()
page.wait_for_timeout(1500)   # or wait for the success toast
page.screenshot(path=f'/tmp/billing_{tag}_after_click.png', full_page=True)
print(tag, "save requests:", reqs)
```
Run with `tag=prefix` on the old build and `tag=postfix` on the fixed build.

**What counts as proof:**
- Pre-fix: no PUT/POST, no visible change, possibly a console error. This reproduces "did nothing".
- Post-fix: a request fires and returns 2xx, a confirmation is visible, and a reload shows the saved value persisted.
- Console log: no new unexpected errors.

**Also test the four states** on the Save flow: loading (button disabled or spinner during the request), error (mock a 500 and see a message and recovery), empty/invalid form, and success. A fix that only works on the happy path is not proven.

**Evidence handed to superpowers-verify:** 4 screenshots (prefix and postfix, before and after click), the request logs, `console.log`, and a before-vs-after summary table.

## Q3
Files read: SKILL.md

This is a visual-fidelity question, which SKILL.md excludes ("Not for ... visual fidelity (reviewing-ui)"). webapp-testing's screenshots prove functional states and cannot judge brand or Figma match. So I do not run a functional test here. I route to `reviewing-ui` (and `design:design-critique` as an option).

What I would tell the user:
- "On-brand" and "matches the Figma" need a reference: the Figma file or frame link, plus brand tokens (colors, type, spacing). I would ask for them. I cannot read Figma without the Figma connector being authorized, so I would say that if it is not connected.
- Plan for reviewing-ui: capture the pricing page screenshots at desktop and mobile widths and compare them side by side with the Figma frames. Check tokens: font family and size, colors, spacing, and component states.

Where webapp-testing can still help: a small recon script can capture the page's screenshots and computed styles so reviewing-ui has consistent inputs, and a check that pricing CTAs work and the page has no console errors:
```python
page.goto('http://localhost:3000/pricing'); page.wait_for_load_state('networkidle')
page.screenshot(path='/tmp/pricing_desktop.png', full_page=True)
```
I would not claim "on-brand" or "matches Figma" from this skill's output.
