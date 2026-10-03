# webapp-testing Skill Evaluation

## Q1

Files read: SKILL.md

### Response

**Task:** Verify the new consent-preference form on http://localhost:3000/settings works in the browser before we ship.

**Evidence Collection Plan:**

Since the dev server is already running at localhost:3000, I'll follow the reconnaissance-then-action pattern:

1. **Inspect State** — Create a Playwright script to:
   - Navigate to `http://localhost:3000/settings`
   - Wait for `networkidle` (critical per SKILL.md)
   - Screenshot full page for initial state
   - Inspect DOM to locate form elements (checkboxes, save button, etc.)

2. **Identify Selectors** — From the screenshot and DOM, find:
   - Consent preference checkboxes (or radio buttons)
   - Any toggle switches
   - Form submit/save button
   - Success message or state change indicator

3. **Execute Actions & Capture Evidence**:
   - Toggle each consent preference (e.g., email marketing, analytics)
   - Take screenshot after each toggle
   - Click the Save button
   - Wait for confirmation (DOM state change or success message)
   - Take screenshot of final state
   - Capture console logs to verify no errors

**Script I Would Run:**

```bash
python3 << 'EOF'
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Navigate and wait for network idle
    page.goto('http://localhost:3000/settings')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='/tmp/consent_form_initial.png', full_page=True)
    
    # Discover form elements
    buttons = page.locator('button').all()
    inputs = page.locator('input[type="checkbox"], input[type="radio"]').all()
    print(f"Found {len(buttons)} buttons, {len(inputs)} inputs")
    
    # Click first consent checkbox
    page.click('input[type="checkbox"]')
    page.screenshot(path='/tmp/consent_form_toggled.png', full_page=True)
    
    # Click Save button
    page.click('button:has-text("Save")')
    page.wait_for_selector('[data-testid="success-message"]', timeout=3000)
    page.screenshot(path='/tmp/consent_form_saved.png', full_page=True)
    
    browser.close()
EOF
```

**Evidence I'd Report:**
- Before screenshot (initial form state)
- After toggle screenshot (checkbox changed)
- After save screenshot (success state visible)
- Console logs (should be clean)
- Form state validation (confirm form data persisted if page reloads)

---

## Q2

Files read: SKILL.md

### Response

**Task:** The 'Save' button on the billing page did nothing before my fix. Prove the fix works.

**Evidence Collection Plan:**

This is a bug fix verification. I need to show that the Save button now triggers an action (network request or DOM state change).

1. **Target the Billing Page** — Navigate to the billing page (assuming `http://localhost:3000/billing` or similar)

2. **Capture Initial State** — Screenshot before clicking Save

3. **Test the Fix** — Click the Save button and monitor:
   - Network requests (POST/PATCH to an API endpoint) using Playwright's request tracking
   - DOM state changes (loading spinner, success message, form disabled state)
   - Console errors (should be none)

4. **Capture Final State** — Screenshot showing success confirmation

**Script I Would Run:**

```bash
python3 << 'EOF'
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Track network requests
    requests_made = []
    page.on('request', lambda req: requests_made.append({
        'method': req.method,
        'url': req.url,
        'time': req.timing
    }))
    
    # Navigate to billing page
    page.goto('http://localhost:3000/billing')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='/tmp/billing_before_save.png', full_page=True)
    
    # Make a change to the form (e.g., update payment method)
    page.fill('input[name="cardNumber"]', '4242424242424242')
    
    # Click Save
    page.click('button:has-text("Save")')
    
    # Wait for success state (spinner disappears or success message appears)
    page.wait_for_selector('[data-testid="save-success"]', timeout=5000)
    page.screenshot(path='/tmp/billing_after_save.png', full_page=True)
    
    # Print captured network activity
    print("Network requests made:")
    for req in requests_made:
        if 'billing' in req['url'] or 'payment' in req['url']:
            print(f"  {req['method']} {req['url']}")
    
    browser.close()
EOF
```

**Evidence I'd Report:**
- Before screenshot (form in editable state)
- After screenshot (success message or confirmation visible)
- Network request log (shows POST/PATCH to billing endpoint succeeded)
- No console errors
- Form state change (button disabled during submit, re-enabled after)

---

## Q3

Files read: SKILL.md

### Response

**Task:** Does the pricing page look on-brand and match the Figma?

**Scope Clarification:**

According to SKILL.md, this task **falls outside the scope of webapp-testing**. The skill explicitly states:

> "Not for... visual fidelity (reviewing-ui)."

And in the ownership boundary:

> "visual design fidelity (that is `reviewing-ui`)" — Does NOT own this.

**What I Would Do Instead:**

This request should be routed to the `reviewing-ui` skill, which handles:
- Design-to-implementation comparison screenshots
- Visual design fidelity against design specs (Figma)
- Accessibility and visual polish

**What webapp-testing CAN Do (if you want functional proof):**

If you want to verify the pricing page works functionally (e.g., CTA buttons clickable, pricing data loads, dynamic pricing calculations work), I can test that:

1. Navigate to pricing page
2. Verify all pricing tiers load without errors
3. Click "Buy" or "Start Trial" buttons
4. Confirm no console errors or broken links
5. Screenshot functional states (loading → loaded → CTA clicked)

But for visual alignment with Figma and on-brand verification, use `reviewing-ui` instead.

