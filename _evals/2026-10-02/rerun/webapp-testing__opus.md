## Q1
Files read: SKILL.md, examples/element_discovery.py, examples/console_logging.py

I'll verify the consent-preference form in a real browser with Playwright and give you evidence, not just a "looks fine".

**Quick questions (I'll proceed on the assumptions shown if you don't answer):**
1. Is the dev server already running on :3000? *Assume yes.* If not, I'll wrap the run in `scripts/with_server.py --server "npm run dev" --port 3000` (after checking `--help`).
2. What should "Save" do: call an API (which endpoint?) and show a toast? *Assume a POST/PUT to a preferences endpoint and a visible confirmation.*
3. Does the page need a logged-in session? *Assume a seeded test user or no auth locally.*

**Step 1: Recon.** The app is dynamic (localhost:3000), so I start with reconnaissance-then-action: navigate, `wait_for_load_state('networkidle')`, full-page screenshot, then list buttons, inputs and checkboxes (the `element_discovery.py` pattern) so I pick selectors from the rendered DOM rather than guessing.

**Step 2: Flow script** (`verify_consent.py`):
```python
from playwright.sync_api import sync_playwright
logs, failed = [], []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); page = b.new_page()
    page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
    page.on("requestfailed", lambda r: failed.append(f"{r.method} {r.url} {r.failure}"))
    page.goto("http://localhost:3000/settings"); page.wait_for_load_state("networkidle")
    page.screenshot(path="/tmp/q1/before.png", full_page=True)
    # selectors confirmed during recon
    page.get_by_label("Marketing emails").check()
    with page.expect_response(lambda r: "preferences" in r.url and r.request.method in ("POST","PUT")) as resp:
        page.get_by_role("button", name="Save").click()
    assert resp.value.ok, resp.value.status
    page.get_by_text("saved", exact=False).wait_for()
    page.screenshot(path="/tmp/q1/after_save.png", full_page=True)
    page.reload(); page.wait_for_load_state("networkidle")
    assert page.get_by_label("Marketing emails").is_checked()   # persisted
    page.screenshot(path="/tmp/q1/after_reload.png", full_page=True)
    b.close()
open("/tmp/q1/console.log","w").write("\n".join(logs+failed))
```

**Step 3: Cover all four states**, since this is a user-facing feature:
| State | How I force it | Pass condition |
|---|---|---|
| Loading | `page.route("**/preferences*", delayed handler)` | Skeleton/spinner shows, no stale toggles, Save disabled |
| Empty | Route GET to return `{}` (new user) | Sensible defaults shown, no blank screen |
| Error | Route the save call to return 500 | Error message shown, toggles keep the user's choice, retry works |
| Success | Real flow above | Confirmation shown, value persists after reload |

I'll also do a keyboard-only pass (tab to each toggle, Space to change it, Enter on Save), because consent controls must be operable without a mouse.

**What you'll get:** before, after-save and after-reload screenshots, plus one screenshot per forced state; `/tmp/q1/console.log`; the save request's status code; and a pass/fail line for each state. I'll only call it ship-ready if every state passes and the log has no unexpected errors or failed requests. If something fails I'll report exactly what broke. I won't patch it as part of this check.

## Q2
Files read: SKILL.md, examples/console_logging.py

For a UI bug fix, this skill asks for **before/after proof**: the same script fails on the old code and passes on the fixed code.

**What I need (assumptions in brackets):**
- The billing page URL and how to sign in locally [`http://localhost:3000/billing`, seeded test user].
- What "Save" should do [send a PATCH to a billing endpoint, then show a "Saved" confirmation].
- The ref from before your fix [`HEAD~1`; your fix is the working tree or the latest commit].

**Repro/verify script** (`verify_billing_save.py`, one script for both runs):
```python
import sys; from playwright.sync_api import sync_playwright
tag = sys.argv[1]  # "before" | "after"
logs, reqs = [], []
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); page = b.new_page()
    page.on("console", lambda m: logs.append(f"[{m.type}] {m.text}"))
    page.on("requestfailed", lambda r: logs.append(f"[network-error] {r.url} {r.failure}"))
    page.on("request", lambda r: reqs.append(f"{r.method} {r.url}") if r.method != "GET" else None)
    page.goto("http://localhost:3000/billing"); page.wait_for_load_state("networkidle")
    page.get_by_label("Billing email").fill("billing+qa@example.test")
    page.screenshot(path=f"/tmp/q2/{tag}_pre_click.png", full_page=True)
    page.get_by_role("button", name="Save").click()
    page.wait_for_load_state("networkidle")
    page.screenshot(path=f"/tmp/q2/{tag}_post_click.png", full_page=True)
    saved = page.get_by_text("Saved", exact=False).is_visible()
    page.reload(); page.wait_for_load_state("networkidle")
    persisted = page.get_by_label("Billing email").input_value() == "billing+qa@example.test"
    b.close()
open(f"/tmp/q2/{tag}_console.log","w").write("\n".join(logs+reqs))
print(tag, "write_request:", bool(reqs), "confirmation:", saved, "persisted:", persisted)
```

**Runs** (the old code goes in a separate worktree so your working tree isn't touched):
```bash
git worktree add /tmp/billing-before HEAD~1
python scripts/with_server.py --server "cd /tmp/billing-before && npm run dev" --port 3000 -- python verify_billing_save.py before
python scripts/with_server.py --server "npm run dev" --port 3000 -- python verify_billing_save.py after
```

**Proof I'll report:**
- **Before:** no write request, no confirmation, and the value doesn't persist. This reproduces "did nothing". If the old code *doesn't* fail, the script isn't testing the real bug, and I'll say so instead of claiming the fix works.
- **After:** one write request with a 2xx response, confirmation visible, value persists after reload, and no new console errors.
- Side-by-side screenshots of `before_post_click.png` and `after_post_click.png`, plus both console logs.
- An extra check of the error and loading states on the fixed code: force a 500 to confirm an error message appears, and add a delay to confirm the button disables so a double-click can't send two saves. Fixes like this often add an unhandled rejection that would otherwise go unseen.

Afterwards I'll remove the temporary worktree (`git worktree remove /tmp/billing-before`).

## Q3
Files read: SKILL.md

This one is outside what this skill does. webapp-testing checks whether the UI *works* (behavior, states, console and network errors). Its description says it is "not for visual fidelity (reviewing-ui)". Checking brand and Figma match is a visual-fidelity review, so the right skill is **`reviewing-ui`**, with brand rules coming from your design system or `design-md`.

**What I'd suggest:**
- Run `reviewing-ui` on the pricing page. It needs the Figma frame link (or an exported PNG) and your brand tokens (colors, type scale, spacing).
- If you also want functional coverage, I can use webapp-testing alongside it, for example: plan toggle (monthly/annual) updates prices, CTAs route correctly, no console errors, and loading/error states render. That gives functional screenshots, but they don't prove Figma fidelity.

**Questions before handing off:**
1. Can you share the Figma frame URL or export? (The Figma connector currently needs authorization.)
2. Which breakpoints matter: desktop only, or mobile and tablet too?
3. Is the pricing page on localhost:3000/pricing?

If useful, I can capture consistent full-page screenshots at 1440, 768 and 375 widths after `networkidle` so `reviewing-ui` can compare them with Figma. The on-brand judgment itself belongs to that skill, so I won't give a verdict on it here.
