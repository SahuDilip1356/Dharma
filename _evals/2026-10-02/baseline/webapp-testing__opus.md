## Q1
Files read: SKILL.md, examples/element_discovery.py, examples/console_logging.py

This is a user-facing feature, so before ship it needs browser evidence: before and after screenshots, the action I performed, a clean console, and coverage of all four states.

**Quick questions (I'll proceed on the assumptions in brackets):**
1. Is the dev server already running on :3000? [Assume yes. If not, I wrap the run in `scripts/with_server.py --server "npm run dev" --port 3000`.]
2. What should a successful save look like: a toast, a "Saved" message, or a persisted reload? [Assume a confirmation message and that the state is still there after a reload.]
3. Does /settings require login? [Assume the dev session is already authenticated. If it isn't, I'll ask you for test credentials from the seed data.]

**Step 1. Recon after networkidle.** I'd run the element_discovery pattern against `/settings` to list every checkbox, toggle and button, and save `/tmp/consent/inspect.png`. I'd pick selectors from that rendered state, not by guessing.

**Step 2. Flow script** (`/tmp/consent/test_consent.py`):
```python
from playwright.sync_api import sync_playwright
logs, OUT = [], '/tmp/consent'
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); page = b.new_page()
    page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
    page.on("requestfailed", lambda r: logs.append(f"[network-error] {r.method} {r.url} {r.failure}"))
    page.goto('http://localhost:3000/settings'); page.wait_for_load_state('networkidle')
    page.screenshot(path=f'{OUT}/before.png', full_page=True)
    page.check('input[name="marketing"]'); page.uncheck('input[name="analytics"]')  # from recon
    with page.expect_response(lambda r: '/consent' in r.url and r.request.method != 'GET') as resp:
        page.click('button:has-text("Save")')
    print('API status:', resp.value.status)
    page.wait_for_selector('text=Saved')
    page.screenshot(path=f'{OUT}/after_save.png', full_page=True)
    page.reload(); page.wait_for_load_state('networkidle')
    assert page.is_checked('input[name="marketing"]') and not page.is_checked('input[name="analytics"]')
    page.screenshot(path=f'{OUT}/after_reload.png', full_page=True)
    b.close()
open(f'{OUT}/console.log','w').write('\n'.join(logs))
```

**Step 3. State coverage** (separate test cases using `page.route` to stub the consent API):
- **Loading:** delay the GET by 2s and screenshot. I expect a spinner or skeleton, and no default or stale toggle values.
- **Empty:** a user with no saved preferences. Defaults should render, with no blank panel.
- **Error:** return 500 on save. An error message should appear, the toggles should keep the user's choices, and a retry should succeed.
- **Success:** the main flow above.

**Report I'd return:** a pass or fail line for each state, with the screenshot paths, the API status codes, and the error and warning counts from console.log. Any console error or failed request blocks "ship-ready" until it's explained. This report is functional evidence for `superpowers-verify`. Unit tests (`superpowers-tdd`) and visual fidelity (`reviewing-ui`) are separate checks.

## Q2
Files read: SKILL.md, examples/console_logging.py

This is a bug fix with a UI component. To prove it, I need to show the broken behaviour before the fix and the working behaviour after it, using the same script both times.

**Questions [assumptions]:** What is the billing page URL? [`http://localhost:3000/billing`] What should Save produce? [A PUT/POST to a billing endpoint, a success message, and data that survives a reload.] Is the fix on a branch? [Yes. I'd check out the pre-fix commit for the baseline run.] Billing pages often have card fields. I'd only change a non-payment field such as company name or billing email, using test values, and run against local or stubbed APIs only.

**Script** (`/tmp/billing/verify_save.py`, takes a label argument `before` or `after`):
```python
import sys; from playwright.sync_api import sync_playwright
tag, logs, reqs = sys.argv[1], [], []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); page = b.new_page()
    page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
    page.on("requestfailed", lambda r: logs.append(f"[network-error] {r.url} {r.failure}"))
    page.on("request", lambda r: reqs.append(f"{r.method} {r.url}") if r.method in ("POST","PUT","PATCH") else None)
    page.goto('http://localhost:3000/billing'); page.wait_for_load_state('networkidle')
    page.fill('input[name="companyName"]', 'Acme Test Co')
    page.screenshot(path=f'/tmp/billing/{tag}_before_click.png', full_page=True)
    page.click('button:has-text("Save")'); page.wait_for_load_state('networkidle')
    page.screenshot(path=f'/tmp/billing/{tag}_after_click.png', full_page=True)
    page.reload(); page.wait_for_load_state('networkidle')
    print(tag, 'persisted:', page.input_value('input[name="companyName"]') == 'Acme Test Co')
    print(tag, 'mutations:', reqs); b.close()
open(f'/tmp/billing/{tag}_console.log','w').write('\n'.join(logs))
```
Run it with `python scripts/with_server.py --server "npm run dev" --port 3000 -- python /tmp/billing/verify_save.py before` on the pre-fix commit, then again with `after` on the fix branch. (I'd run `with_server.py --help` first.)

**Evidence that proves the fix:**
- Before: no mutation request, no confirmation, the value is not persisted. This confirms the script reproduces the bug. If the baseline passes, the test proves nothing.
- After: one mutation request with status 2xx, a confirmation is visible, the value persists after reload, and there are 0 console errors.
- I'd also check the error state (stub the endpoint to return 500 and confirm an error message appears) and that a double-click doesn't send two saves.

I'd report the side-by-side screenshots, the request logs and the console logs. I wouldn't claim it's fixed without the "after" run.

## Q3
Files read: SKILL.md

This request is outside webapp-testing. This skill checks functional behaviour: does it work, are the states covered, are there console or network errors. It explicitly does **not** own visual design fidelity or comparing a design to the implementation. That belongs to **`reviewing-ui`**, and I'd run this request through that skill.

What I'd need for that review: the Figma frame link or an export of the pricing page, the brand or design tokens, the breakpoints to check, and the local URL of the pricing page.

What webapp-testing can add next to it: a functional pass on the pricing page. That means the page loads after networkidle, the CTA buttons and monthly/annual toggle work, prices update, there are no console errors, and loading and error states render. Those screenshots would be labelled as functional evidence, not fidelity evidence. Should I run that functional pass as well, or just hand off to `reviewing-ui`?
