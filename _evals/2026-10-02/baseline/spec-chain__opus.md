# spec-chain dry run (opus)

## Q1
Files read: SKILL.md, references/intent.md, references/spec.md, references/plan.md, references/write-plan-method.md

**Route:** This is a clear feature, so it gets the full chain. Subscriber email addresses are personal data, so any task that touches the subscriber store or sending gets `risk: tier1`.

**Quick questions (assumptions below if you don't answer):**
1. Where do the 5 bullets come from: an editor, AI summaries of DPDPA news, or both? Does a human approve them before send?
2. What should happen on a day with no news: skip the send, or send a "no updates" email?
3. Do signup and unsubscribe already exist, or are they in scope?
4. How will we know it worked within two weeks: open rate, unsubscribe rate, or something else?

**Assumed:** AI-drafted bullets from a fixed source list. Existing subscribers. Signup is out of scope. Unsubscribe is in scope because the law requires it.

I would write these to `specs/dpdpa-daily-brief/`:

**intent.md (excerpt)**
```markdown
## Goals
### G1 — Subscribers get the day's DPDPA developments before work starts
Each subscriber receives one brief by 07:15 IST, every day.
### G2 — The brief can be read in under a minute
Exactly 5 bullets, each with a source link.
### G3 — Subscribers can leave in one click
## Non-goals
### NG1 — Signup flow and landing page (already exist / separate cycle)
### NG2 — Per-subscriber personalisation
## Assumptions
### A1 — There are enough source items for 5 bullets on most days
- validate_by: count qualifying items/day over the last 30 days, week 1
- if_wrong: allow 3–5 bullets, or skip the send on quiet days
### A2 — AI summaries are accurate enough to send without review
- validate_by: founder reviews 10 drafts before launch
- if_wrong: add a human-approve step and move send time to 08:00
### A3 — Subscriber list < 5k, so one batch fits provider limits
- validate_by: check provider rate limit against list size
- if_wrong: send in chunks starting at 06:45
## Success criterion
≥95% of active subscribers receive the brief by 07:15 IST on 13 of the first 14 days; open rate ≥35%.
## Rollback
Feature flag `daily_brief_send` off; no schema change to undo.
```

**spec.md (ACs)**
```markdown
### AC1 — Daily send — traces: G1
given an active subscriber; when the clock reaches 07:00 IST; then one email is sent and a send row is logged (subscriber_id, brief_date, status=sent)
### AC2 — Exactly five bullets — traces: G2
then the body contains 5 bullets, each ≤40 words with a source URL
### AC3 — Not enough items — traces: G1, G2
given <5 qualifying items; then no email is sent and `brief.skipped reason=insufficient_items` is logged
### AC4 — No double send — traces: G1
given the job is retried after partial success; then nobody gets a second email for that brief_date
### AC5 — Provider failure — traces: G1
given the email provider returns 5xx; then retry 3× with backoff, then status=failed and alert
### AC6 — Unsubscribe — traces: G3
when the one-click link is used; then the subscriber is marked inactive and gets no further sends
### AC7 — Inactive excluded — traces: G3
```
Non-functional: all sends finish by 07:15 IST. The schedule is pinned to Asia/Kolkata and does not use server time.

**plan.md (tasks)**
```markdown
### T1 — Bullet generator returns exactly 5 sourced bullets or a skip
- implements: AC2, AC3 · depends_on: none · risk: tier1 (prompt) · size: M
- verify: npm test -- brief/generate.test.ts
### T2 — Idempotent send log keyed on (subscriber_id, brief_date)
- implements: AC1, AC4 · depends_on: none · risk: tier1 (migration, PII) · size: S
- verify: npm test -- brief/sendlog.test.ts
### T3 — Send job with retry/backoff and alert
- implements: AC1, AC5, AC7 · depends_on: T1, T2 · risk: tier1 · size: M
- verify: npm test -- brief/send.test.ts
### T4 — One-click unsubscribe endpoint
- implements: AC6 · depends_on: T2 · risk: tier1 · size: S
- verify: npm test -- brief/unsubscribe.test.ts
### T5 — 07:00 IST schedule
- implements: AC1 · depends_on: T3 · risk: tier2 · size: S
- verify: npm test -- brief/schedule.test.ts (asserts cron resolves to 01:30 UTC)
```
For each task's internal steps, I'd follow write-plan-method: failing test first, then implementation, then verify, then commit.

**Validate before handing off:**
```bash
python3 ~/.claude/skills/spec-chain/scripts/validate_chain.py specs/dpdpa-daily-brief/
```
T1 and T2 have no dependencies, so they can run in parallel. After that come T3 and T4, then T5.

## Q2
Files read: SKILL.md, references/plan.md, references/write-plan-method.md, references/adoption.md, references/intent.md, references/spec.md

**Route:** This touches payments, so it gets the full chain and **every payments task is `risk: tier1`** with a named human reviewer.

First I'd check whether `specs/subsense-stripe-checkout/spec.md` exists (`ls specs/`). The rule is no task without an AC. If there's no spec, I can't write honest tasks. I'd draft intent.md and spec.md first, then the plan.

**Questions:**
1. Is this a recurring subscription (Stripe Checkout in `subscription` mode) or one-time payments? Which plans and prices?
2. Currency: INR only? Indian cards need e-mandates for recurring payments, which affects the design.
3. What is the source of truth for "user is paid": webhooks or the redirect?
4. Are failed payments and cancellation in scope?

**Assumed:** monthly and annual subscriptions in INR, a hosted Checkout page, webhooks as the source of truth, and cancellation through the Customer Portal.

**spec.md ACs (short form)**
- AC1: Signed-in user picks a plan → redirected to Stripe Checkout with the correct price (G1)
- AC2: `checkout.session.completed` webhook → subscription marked active, entitlement granted (G1)
- AC3: Webhook with an invalid signature → 400, no state change (malicious)
- AC4: The same event delivered twice → processed once (concurrent)
- AC5: User returns to the success URL before the webhook arrives → "activating…" state, no false "paid" (loading)
- AC6: User cancels at checkout → back on pricing, no subscription row (error)
- AC7: `invoice.payment_failed` → status past_due, user notified (error)
- AC8: Already-subscribed user starts checkout → sent to the portal instead (boundary)

**plan.md**
```markdown
### T1 — Subscription + processed-event tables
- implements: AC2, AC4 · depends_on: none · files: migrations/00xx_subscriptions.sql, tests/… · risk: tier1 · size: S
- verify: npm test -- migrations/subscriptions.test.ts
- notes: down-migration in same file; not reversible by git revert
### T2 — Create-checkout-session endpoint
- implements: AC1, AC6, AC8 · depends_on: T1 · files: payments/checkout.ts, tests/payments/checkout.test.ts · risk: tier1 · size: M
- verify: npm test -- payments/checkout.test.ts
### T3 — Webhook handler: signature check + idempotency
- implements: AC3, AC4 · depends_on: T1 · risk: tier1 · size: S
- verify: npm test -- payments/webhook.signature.test.ts
### T4 — Webhook: activate on completed, past_due on failed
- implements: AC2, AC7 · depends_on: T3 · risk: tier1 · size: M
- verify: npm test -- payments/webhook.events.test.ts && stripe trigger checkout.session.completed (test mode)
### T5 — Success page pending/active states
- implements: AC5 · depends_on: T2 · risk: tier2 · size: S
- verify: npm test -- app/checkout-success.test.tsx
```
T2 and T3 can run in parallel once T1 lands. I'd run `validate_chain.py specs/subsense-stripe-checkout/`, confirm that every task's `risk:` agrees with the CI path glob (`payments/`, `migrations/` → tier1), and then dispatch the tasks in dependency order. Only Stripe test-mode keys are used.

## Q3
Files read: SKILL.md

**Route:** This is a bug fix in one file with an obvious cause, so I'd **skip the chain**. The skill says to write the test and fix it, without creating intent/spec/plan files.

One question: should an empty string be treated like null (return `null`), or should it throw a clear validation error? I'll assume it's treated like null, since that matches what the null check is for.

What I'd do:
1. Read `utils/date.ts` to find the guard. The likely cause is `if (value === null || value === undefined)` letting `""` through to the date parsing, which then throws on `Invalid Date`.
2. Write a failing test first:
```ts
// utils/date.test.ts
it("returns null for empty string instead of throwing", () => {
  expect(() => parseDate("")).not.toThrow();
  expect(parseDate("")).toBeNull();
});
it("returns null for whitespace-only string", () => {
  expect(parseDate("   ")).toBeNull();
});
```
Run `npm test -- utils/date.test.ts` and expect it to fail.
3. Make the smallest fix, changing only the guard:
```ts
if (value == null || value.trim() === "") return null;
```
4. Run `npm test -- utils/date.test.ts && npm run typecheck`. Everything should be green.
5. Commit: `fix(date): treat empty string like null in parseDate`.

(I'd use the real function name from the file. `parseDate` is a placeholder.)
