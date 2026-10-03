## Q1
Files read: SKILL.md, references/intent.md, references/spec.md, references/plan.md, references/write-plan-method.md

**Routing (step 1):** The ask is a clear feature, so it gets the full chain. It sends email to subscribers, which is PII/consent under DPDPA, so every affected task gets `risk: tier1`. The framing is a feature and not a solution-shaped pain, so I would not run `/office-hours` first. Success criteria and assumptions are thin, so I'd ask these questions (intent.md interview, stopping once I have enough):

1. How many subscribers are there now, and where is the list stored?
2. What do they read in the morning today? That tells us the real pain.
3. How will we know it worked within two weeks (open rate, unsubscribe rate, retention)?
4. Where do the 5 bullets come from: human-curated or auto-generated?
5. What would make us turn it off?

**Assumptions I proceed under:** subscribers have given consent that covers the daily email, and the content for the bullets already exists upstream. Both are listed as A1 and A2 in intent.md and are marked unvalidated.

**Files to write:** `specs/dpdpa-daily-brief-email/{intent,spec,plan}.md`.

`intent.md` (no implementation nouns):
```markdown
# Intent — Daily Brief email
Status: draft | Owner: <TBD> | Date: 2026-10-02
## Problem
Subscribers must open the site to learn what changed in DPDPA each day, so many miss important updates.
## Goals
### G1 — Subscribers get a 5-point summary each morning
### G2 — Only consenting subscribers are emailed, and they can opt out in one step
## Non-goals
### NG1 — Personalisation per subscriber (not this cycle)
### NG2 — Other channels, e.g. WhatsApp (different problem)
## Assumptions
### A1 — Consent covers daily email. validate_by: audit the consent records before build. if_wrong: re-consent flow becomes a prerequisite.
### A2 — Source content exists daily. validate_by: check the last 30 days for gaps. if_wrong: define the skip-day behaviour.
### A3 — 7:00 IST is the right time. validate_by: compare opens in a 2-week A/B. if_wrong: make the time configurable.
## Success criterion
>=35% unique open rate and <=1% unsubscribe rate on the daily send within 14 days of launch.
## Rollback
Disable the send with a feature flag. No data migration involved.
```

`spec.md` (excerpt):
- AC1 (G1): given a published brief with >=5 items, when it is 07:00 IST, then each active subscriber gets one email with exactly 5 bullets, delivered by 07:15.
- AC2 (G1): given fewer than 5 items, then no email is sent and a log line `brief_skipped` is written. This is the empty state.
- AC3 (G1): given a provider outage or timeout, then the send is retried 3 times and an alert is raised. This is the error state.
- AC4 (G1): given the job fires twice (retry/double trigger), then no subscriber gets a duplicate. This is the concurrency case.
- AC5 (G2): given an unsubscribed or consent-withdrawn user, then no email is sent and a `send_suppressed` audit row is written.
- AC6 (G2): every email has a one-click unsubscribe that takes effect before the next send.
- Contract: error shapes enumerated, including the DST-free IST schedule `0 7 * * *` Asia/Kolkata. The spec states the behaviour, not the library.

`plan.md` (tasks):
- T1 subscriber/consent suppression query. Implements AC5. Risk tier1. Verify: `pytest tests/test_suppression.py -q`
- T2 brief selection and 5-bullet formatter. Implements AC1, AC2. Risk tier2.
- T3 idempotent send ledger. Implements AC4. Depends on T1. Risk tier1.
- T4 provider send with retry and alert. Implements AC3. Depends on T2, T3. Risk tier1.
- T5 unsubscribe endpoint and link. Implements AC6. Risk tier1.
- T6 07:00 IST scheduler wiring. Implements AC1. Depends on T4.
Each task is at most 5 files and size S/M, with a runnable `verify`.

**Validate:**
```bash
python3 ~/.claude/skills/spec-chain/scripts/validate_chain.py specs/dpdpa-daily-brief-email/
```
This should pass: every G* is covered, every task has an AC, and there are no dependency cycles. I'd then hand off T1, T2 and T5 in parallel.

## Q2
Files read: SKILL.md, references/plan.md, references/write-plan-method.md

**Routing:** Payments is a tier1 area (`payments/`), so the full chain applies and every task is `risk: tier1`. The user asked only for tasks, but the skill says "No task without a criterion". plan.md cannot validate unless spec.md has ACs, and spec.md needs intent.md. So I would not write a bare task list. I would draft the three files at least as a stub.

**Questions I'd ask:**
1. One-time or subscription billing, and which plans and prices?
2. Hosted Checkout or embedded Elements?
3. Where is entitlement stored, and what is the stack?
4. Is there an existing spec/intent for SubSense?

**Assumptions:** Stripe-hosted Checkout, subscription mode, webhooks as the source of truth, TypeScript/Next.js. I would put these in intent.md as A1-A3. If a spec exists, I'd read it first.

**Stub ACs (spec.md):** AC1 session created for an authenticated user. AC2 `checkout.session.completed` activates the entitlement. AC3 a duplicate webhook is idempotent. AC4 a bad webhook signature gets 400 and no state change. AC5 cancel/abandoned checkout leaves no entitlement. AC6 a payment failure is surfaced to the user. AC7 a user cannot buy for another tenant.

**plan.md tasks** (sequence: schema, contracts, core logic, edges, surface, observability):
```markdown
### T1 — Add subscriptions table and entitlement model
- implements: AC2, AC3
- depends_on: none
- files: migrations/0001_subscriptions.sql, tests/migrations/test_0001.py
- risk: tier1
- size: S
- verify: pytest tests/migrations/test_0001.py -q
- notes: forward-only, with a down-migration in the same file

### T2 — Create Checkout Session endpoint
- implements: AC1, AC5, AC7
- depends_on: T1
- files: src/billing/checkout.ts, tests/billing/checkout.test.ts
- risk: tier1
- size: M
- verify: npm test -- tests/billing/checkout.test.ts

### T3 — Verify webhook signature
- implements: AC4
- depends_on: none
- verify: npm test -- tests/billing/signature.test.ts

### T4 — Handle checkout.session.completed idempotently
- implements: AC2, AC3
- depends_on: T1, T3

### T5 — Handle invoice.payment_failed
- implements: AC6
- depends_on: T4

### T6 — Checkout button and success/cancel pages
- implements: AC1, AC5
- depends_on: T2
- verify: manual — Stripe test card 4242... flow, tier1
```
T3 and T1 run in parallel; T2 and T4 follow. The validator is then run, and each task is ticked `status: done` after its verify passes.

## Q3
Files read: SKILL.md (no references needed)

**Routing:** This is a bug fix touching one file with an obvious cause, so the table says **skip the chain**. No intent.md, spec.md or plan.md is written. The date util does not touch auth, payments, migrations or PII, so there is no tier1 escalation.

I'd do it test-first. No project exists in this dry run, so I would not run anything here. In a real repo I would first read `utils/date.ts` and its existing tests, then:

1. Write a failing test (name and style adjusted to the repo's test runner):
```ts
it("does not throw on empty string", () => {
  expect(() => parseDate("")).not.toThrow();
  expect(parseDate("")).toBeNull(); // match whatever the existing null contract returns
});
```
Run: `npx vitest run utils/date.test.ts` (or the repo's runner). Expected: 1 failure.

2. Fix, in the same file only. The likely cause is that the guard checks `value == null` and misses `""`, so the code goes on to parse `""`. The change would be:
```ts
if (value == null || value.trim() === "") return null;
```
Without seeing the file, I'd mention that this is my guess at the cause.

3. Re-run the test and the whole suite. Expected: all pass. I would touch nothing else.

I'd ask one thing before choosing the empty-string return value: should it be `null`, `undefined`, or a thrown validation error for callers? I'd assume `null`, consistent with the existing null handling, and say so in the summary.
