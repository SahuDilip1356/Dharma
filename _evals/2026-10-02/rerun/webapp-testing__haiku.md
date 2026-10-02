# Webapp Testing Skill Evaluation

## Q1
Files read: SKILL.md

**Request:** "Verify the new consent-preference form on http://localhost:3000/settings works in the browser before we ship."

**My approach:**

Following the reconnaissance-then-action pattern from SKILL.md:

1. **Reconnaissance** — Navigate to http://localhost:3000/settings and inspect:
   ```bash
   python3 << 'EOF'
   from playwright.sync_api import sync_playwright
   with sync_playwright() as p:
       browser = p.chromium.launch()
       page = browser.new_page()
       page.goto('http://localhost:3000/settings')
       page.wait_for_load_state('networkidle')  # CRITICAL
       page.screenshot(path='/tmp/settings_before.png', full_page=True)
       content = page.content()
       buttons = page.locator('button').all()
       for b in buttons: print(f"Button: {b.inner_text()}")
   EOF
   ```

2. **Identify selectors** — From the screenshot and DOM output, locate form inputs and the consent-preference control (e.g., `[data-testid="consent-preference"]`, `input[type="checkbox"]`).

3. **Test state coverage** — Execute all four states:
   - **Loading:** Verify spinner appears while form initializes
   - **Empty:** Check form renders with default/unchecked consent state
   - **Error:** Trigger validation error (submit without required field) → screenshot error message
   - **Success:** Fill form, click Save, wait for `networkidle` → screenshot confirmation and verify network request succeeded

4. **Capture evidence:**
   - Before screenshot (form initial state)
   - After each action (checkbox toggle, submit, success)
   - Console log output: `page.on("console", handler)` to catch warnings/errors
   - Network errors: `page.on("requestfailed", handler)` to catch failed API calls

**Expected deliverable:** Before/after screenshots, console output with no unexpected errors, network request logs showing successful POST to consent endpoint.

---

## Q2
Files read: SKILL.md

**Request:** "The 'Save' button on the billing page did nothing before my fix. Prove the fix works."

**My approach:**

This is a before/after verification of a specific interaction.

1. **Navigate and screenshot (before state):**
   ```bash
   python3 << 'EOF'
   from playwright.sync_api import sync_playwright
   with sync_playwright() as p:
       browser = p.chromium.launch()
       page = browser.new_page()
       # Capture network and console
       errors = []
       page.on("console", lambda msg: errors.append(f"[{msg.type}] {msg.text}"))
       page.on("requestfailed", lambda req: errors.append(f"[NETWORK] {req.url} failed"))
       
       page.goto('http://localhost:3000/billing')
       page.wait_for_load_state('networkidle')
       page.screenshot(path='/tmp/billing_before.png', full_page=True)
   EOF
   ```

2. **Locate the Save button** — From the screenshot, find selector (likely `button:has-text("Save")` or `[data-testid="save-button"]`).

3. **Execute the fix — Click Save and capture state change:**
   ```bash
   python3 << 'EOF'
   page.click('[data-testid="save-button"]')
   page.wait_for_load_state('networkidle')  # Wait for network response
   page.screenshot(path='/tmp/billing_after.png', full_page=True)
   # Verify success state (e.g., success toast, form disabled, URL change)
   EOF
   ```

4. **Verify the fix worked:**
   - **After screenshot:** Shows confirmation (success toast, "Saved" message, or form state change)
   - **Network logs:** POST request to `/api/billing/save` returned 200 (not 404 or 500)
   - **Console output:** No JavaScript errors; only expected logs
   - **DOM state:** Button is no longer in loading state, form shows saved values

**Expected deliverable:** Before/after screenshots showing button inactive → active → success state, network request log showing 200 response, console output clean of errors.

---

## Q3
Files read: SKILL.md

**Request:** "Does the pricing page look on-brand and match the Figma?"

**Issue — Out of Scope:**

This request falls outside the webapp-testing skill's scope. The skill description explicitly states:

> "Use it in Verify for every user-facing feature and for UI bug fixes (before/after proof); optionally in Build for quick feedback. Its screenshots prove **functional states**; `reviewing-ui` screenshots prove **visual fidelity**; unit tests belong to `superpowers-tdd`."

**Visual fidelity and brand matching are the domain of the `reviewing-ui` skill, not webapp-testing.**

**What I would do instead:**

If the user rephrased this as "Can the pricing page render without errors?", I would:
1. Navigate to pricing page
2. Screenshot initial state
3. Verify no 404 errors, console errors, or network failures
4. Confirm page is interactive (links clickable, forms functional)
5. Report functional status only — not visual/brand alignment

**Clarifying question for the user:**
- Are you asking: (a) "Does the pricing page load and function correctly?" → Use webapp-testing
- Or: (b) "Does the pricing page match the design and brand guidelines?" → Use reviewing-ui skill

**How I'd proceed under stated assumption:**
If the user means (a), I'd proceed as per Q1/Q2 pattern: screenshot, interact, verify no errors.
If the user means (b), I'd recommend they invoke the `reviewing-ui` skill with Figma link and pricing page URL.
