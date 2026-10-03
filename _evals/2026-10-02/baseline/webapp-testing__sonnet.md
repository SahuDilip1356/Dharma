## Q1

Files read: SKILL.md, examples/console_logging.py, examples/element_discovery.py

This is a functional browser check of a user-facing feature before ship, so webapp-testing applies. The server is already running at localhost:3000, so I use the reconnaissance-then-action path and skip with_server.py. I have not seen the form yet, so I don't know its selectors or what it submits.

Clarifying questions (I proceed under assumptions below):
- What does a successful save look like (toast, persisted on reload, API call)?
- Is there a login, and is there a test account?
- Which API route does it submit to?

Assumptions: no auth is needed, the form has checkboxes or toggles plus a Save button, and a POST to something like /api/consent is made on save.

Step 1, reconnaissance (adapted from examples/element_discovery.py):

```python
page.goto('http://localhost:3000/settings')
page.wait_for_load_state('networkidle')   # before any inspection
page.screenshot(path='/tmp/evidence/q1_00_recon.png', full_page=True)
# list buttons, inputs and checkboxes, then pick selectors from the rendered DOM
```

Step 2, the real test. I attach console and requestfailed listeners before goto, as in console_logging.py. I also add a `page.on("response")` hook for the save call, to record status codes. The script covers all four required states:

```python
logs = []
page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
page.on("requestfailed", lambda r: logs.append(f"[network-error] {r.method} {r.url} {r.failure}"))
page.on("response", lambda r: logs.append(f"[resp] {r.status} {r.url}") if "/api/" in r.url else None)

page.goto(URL); page.wait_for_load_state('networkidle')
page.screenshot(path='before.png', full_page=True)          # evidence: before

# Loading: delay the GET for saved prefs and assert skeleton/spinner, then no stale data
page.route("**/api/consent*", lambda r: (time.sleep(1.5), r.continue_()))

# Success: toggle a consent box, click Save, wait for the confirmation
page.get_by_label("Marketing emails").check()
page.get_by_role("button", name="Save").click()
page.wait_for_selector('[role="status"], text=Saved')
page.screenshot(path='after_success.png', full_page=True)  # evidence: after
page.reload(); page.wait_for_load_state('networkidle')
assert page.get_by_label("Marketing emails").is_checked()   # persistence

# Error: page.route(..., lambda r: r.fulfill(status=500)) -> error message visible, Save re-enabled, retry works
# Empty: fulfill GET with no stored prefs -> sensible defaults, no blank screen
```

Because this is a consent form, I also check that defaults are not pre-ticked for non-essential consent, and that the withdraw (uncheck) path persists as well as the grant path.

Command: `python q1_consent_test.py`. Server lifecycle is not needed, but if it were down I would use `python scripts/with_server.py --server "npm run dev" --port 3000 -- python q1_consent_test.py`. I would run `--help` on with_server.py first, as the skill says.

Evidence to collect: before and after screenshots per state, `/tmp/evidence/console.log`, the network responses for the save call, and a pass/fail line per state (loading, empty, error, success). The gate passes only if all four states pass and the console has no unexpected errors. Otherwise I report which state failed and attach the log.

Scope: this proves function only. Visual fidelity is for reviewing-ui, and unit tests for the form validation belong to superpowers-tdd.

## Q2

Files read: SKILL.md, examples/console_logging.py (read for the Q1 request, reused here)

This is a UI bug fix (Route C, conditional), so browser proof applies. The key point is that a "fix works" claim needs a before and after pair. A passing run on the fixed code alone does not prove the fix, because it never showed the bug.

Questions: which billing URL and account state, what should Save do (API call, toast, persisted value), and which commit holds the fix? I assume /billing, a Save that PUTs billing details, and that the fix is uncommitted or on a branch.

Plan:
1. Reproduce the bug on the pre-fix code. I run `git stash` (or check out the parent commit) and start the server with `python scripts/with_server.py --server "npm run dev" --port 3000 -- python q2_billing_save.py`. If the app is already running I skip the helper. Output is saved as `before_fix/`.
2. Run the same script on the fixed code and save to `after_fix/`.

Script (shared by both runs):

```python
page.on("console", ...); page.on("requestfailed", ...)
reqs = []
page.on("request", lambda r: reqs.append(r) if r.method in ("POST","PUT","PATCH") else None)
page.goto('http://localhost:3000/billing'); page.wait_for_load_state('networkidle')
page.screenshot(path=f'{OUT}/01_before_click.png', full_page=True)
page.get_by_label("Company name").fill("Test Co")      # make the form dirty
page.get_by_role("button", name="Save").click()
page.wait_for_timeout(1500)   # or wait for the success selector on the fixed build
page.screenshot(path=f'{OUT}/02_after_click.png', full_page=True)
print("save requests fired:", len(reqs))
page.reload(); page.wait_for_load_state('networkidle')
print("persisted value:", page.get_by_label("Company name").input_value())
```

Expected evidence:
- Pre-fix: 0 save requests, no confirmation, value lost on reload, and possibly a console error that explains the cause (this is the root-cause clue).
- Post-fix: 1 request with a 2xx status, confirmation visible, value persisted, and a clean console.

I also test the error and double-click states around Save (a 500 is shown to the user, the button is disabled while saving), since a fix often regresses these. For regression protection I recommend a unit or integration test via superpowers-tdd. This browser run is the end-to-end proof for superpowers-verify to cite.

If I cannot reproduce the original bug on the old code, I report that. I do not claim the fix is proven in that case.

## Q3

Files read: SKILL.md (no other files needed)

This request is out of scope for webapp-testing. SKILL.md's description and ownership boundary say visual fidelity and design-to-implementation comparison belong to `reviewing-ui`. "On-brand" and "matches Figma" are both visual-design questions. This skill's screenshots only prove functional states.

What I would do:
- Route the main request to `reviewing-ui` (and `designing-ui` or the brand skills for brand rules), and say so in one line.
- Ask for the Figma link or exported frames, the brand guide, and which breakpoints matter. I can't pull Figma without that link, and the Figma MCP requires authorization first.
- Offer what webapp-testing can contribute as a supporting step: a Playwright script that loads the pricing page after `networkidle` and takes full-page screenshots at 1440, 768 and 375 widths. Those give reviewing-ui a live-render input.

```python
for w in (1440, 768, 375):
    page.set_viewport_size({'width': w, 'height': 900})
    page.goto('http://localhost:3000/pricing'); page.wait_for_load_state('networkidle')
    page.screenshot(path=f'/tmp/evidence/pricing_{w}.png', full_page=True)
```

I would not give a pass or fail verdict on brand or Figma match from this skill. Doing so would be opinion presented as evidence. I could also check pricing page function here (toggle monthly/annual, CTA clicks, console errors) if the user wants that.
