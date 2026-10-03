# Spec-Chain Skill Evaluation

## Q1

**Files read:** SKILL.md, references/intent.md, references/spec.md

**Response:**

I would route this as a clear feature (not fuzzy scope, not one-liner bug), so I'd create the full chain. Starting with intent.md:

**specs/dpdpa-daily-brief/intent.md** (draft):
- **Problem:** Subscribers must check the app daily or miss DPDPA updates; they want a frictionless summary in email.
- **G1:** Email arrives every morning at 7am IST to all opted-in subscribers.
- **G2:** Each email contains exactly 5 bullets covering the day's key DPDPA developments.
- **NG1:** Personalization by geography or industry (different cycle).
- **A1 — Database has verified subscriber email addresses.** validate_by: query DB for null/invalid emails (week 1). if_wrong: requires email verification flow first.
- **A2 — Scheduled jobs can reliably run at 7am IST.** validate_by: test cron on staging. if_wrong: use event-driven fallback or offset job.
- **A3 — 5 bullets per day is sufficient signal.** validate_by: ask 3 subscribers what they read. if_wrong: becomes 10 bullets or digest frequency drops to weekly.
- **Success:** 80% open rate within 7 days, or 50% click-through on bullet links.
- **Rollback:** feature flag to disable sends; keep emails in DB for 30 days in case of replay.

**specs/dpdpa-daily-brief/spec.md** (draft):
- **Behavior:** System queries all published DPDPA items from prior 24 hours, ranks by relevance, formats top 5 into bullets with links, sends email via SMTP at 7am IST to all active subscribers.
- **AC1 — Email is delivered at 7am IST ±5 min.** given: subscriber is active. when: clock reaches 07:00:00 IST. then: email sent, log line "email_sent" with subscriber_id, timestamp.
- **AC2 — Email body contains exactly 5 bullet points.** given: ≥5 items published in past 24h. when: job runs. then: email body has 5 `<li>` entries, each with title + link.
- **AC3 — No email is sent if fewer than 2 new items exist.** given: 0–1 items in past 24h. when: job runs. then: no email sent, log "insufficient_content".
- **AC4 — Failed send is retried once after 5 min.** given: SMTP error (timeout, 5xx). when: initial send fails. then: retry queued, retry succeeds or logged as "send_failed_after_retry".
- **Non-functional:** Job must complete within 10 minutes; email <100 KB; SMTP timeout 30 sec.
- **Open questions:** How far back to source items if <2 found in 24h? (PM, needs answer by sprint start). Does this block AC3?

Then run `python3 ~/.claude/skills/spec-chain/scripts/validate_chain.py specs/dpdpa-daily-brief/` to check traceability.

---

## Q2

**Files read:** SKILL.md, references/plan.md

**Response:**

I'm missing project context (is this Stripe Checkout hosted, embedded, or custom?), so I'd ask:
1. Is SubSense a SaaS with per-user subscriptions or one-time purchases?
2. Payment flows: sign-up billing + recurring charge, or just one-time?
3. Existing tables/schema for subscriptions?

Assuming: SubSense is a SaaS with monthly billing; we're integrating Stripe Checkout (hosted); migrations exist.

**specs/subsense-stripe-checkout/plan.md** (sketch):

**Architecture:** Frontend (React) → API `/checkout` → Stripe API → Webhook receiver → subscription fulfillment.

**T1 — Create Stripe test/live credentials and store in config**
- implements: AC_credentials (unstated but assumed)
- depends_on: none
- files: .env.example, config/stripe.ts, tests/stripe.test.ts
- risk: tier1 (credentials)
- size: S
- verify: `grep -q STRIPE_KEY .env.example && npm run typecheck`

**T2 — Add payment intent endpoint `/api/checkout`**
- implements: AC_checkout_creates_session (assumed)
- depends_on: T1
- files: src/api/checkout.ts, tests/api/checkout.test.ts
- risk: tier1 (payments)
- size: M
- verify: `npm test tests/api/checkout.test.ts -q`

**T3 — Add checkout button to UI and wire to endpoint**
- implements: AC_user_sees_button (assumed)
- depends_on: T2
- files: src/components/BillingForm.tsx, tests/BillingForm.test.tsx
- risk: tier2
- size: S
- verify: `npm test tests/BillingForm.test.tsx -q`

**T4 — Add webhook endpoint to handle payment completion**
- implements: AC_subscription_activated_on_success (assumed)
- depends_on: T2
- files: src/api/webhook.ts, tests/api/webhook.test.ts
- risk: tier1 (PCI, webhooks)
- size: M
- verify: `npm test tests/api/webhook.test.ts -q`

**T5 — Add error handling for declined cards and timeouts**
- implements: AC_payment_failed_shows_error (assumed)
- depends_on: T2, T3
- files: src/api/checkout.ts, src/components/BillingForm.tsx, tests/error-scenarios.test.ts
- risk: tier2
- size: S
- verify: `npm test tests/error-scenarios.test.ts -q`

---

## Q3

**Files read:** SKILL.md

**Response:**

Bug fix ≤1 file, obvious → skip the chain. No intent.md, spec.md, or plan.md needed.

**Approach:**

1. **Write failing test** in `tests/utils/date.test.ts`:
```typescript
it('throws on empty string', () => {
  expect(() => parseDate("")).toThrow("Empty string not allowed");
});

it('throws on whitespace-only string', () => {
  expect(() => parseDate("  ")).toThrow("Empty string not allowed");
});
```
Run: `npm test tests/utils/date.test.ts` → expect 2 failures.

2. **Fix `utils/date.ts`:**
```typescript
export function parseDate(val: string): Date {
  if (!val || val.trim() === "") {
    throw new Error("Empty string not allowed");
  }
  return new Date(val);
}
```

3. **Verify:** `npm test tests/utils/date.test.ts` → all pass, no TypeScript errors.

4. **Commit:** `git add utils/date.ts tests/utils/date.test.ts && git commit -m "fix: reject empty strings in parseDate"`

Done. No ceremony needed for a one-file fix with a clear test.
