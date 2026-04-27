# Routing Decision Tree

Run these 7 steps in order before selecting any route. Stop at the first match.
Classification must be explicit — never implicit.

---

## Step 1: Is this high-risk by surface area?

Check if the request touches any of these areas:

| Surface Area | Examples |
|---|---|
| **Authentication / authorization** | Login, sessions, OAuth, JWT, roles, permissions |
| **Payments / billing / financial logic** | Stripe, invoices, tax, subscriptions, refunds |
| **AI affecting user decisions** | Recommendations, diagnoses, approvals, scoring |
| **Compliance-critical data** | DPDPA, HIPAA, PCI, GDPR, audit logs |
| **Production data mutation** | Migrations, bulk updates, deletion, anonymization |

**If yes:** Classify as `risk: high` or `risk: critical` regardless of work type.
Apply Route G (Security) checks alongside primary route — they are additive, not substitutes.
Stop and confirm with user before any destructive or irreversible action.

**If no:** Continue to Step 2.

---

## Step 2: Is this user-facing?

Does the output appear in the UI, affect what users see, or change what users can do?

**If yes:**
- User impact = `user-facing` or `revenue-critical`
- Phase 1 UX Gate is **mandatory** — cannot be skipped
- `uiux-designer`, `uiux-accessibility-review`, `uiux-responsive-review`, `uiux-design-qa` are required
- Continue to next applicable step to determine route

**If no (internal tooling, backend-only, data pipeline, infra):**
- User impact = `internal` or `none`
- UX Gate is optional — include only if internal tool has UI stakeholders
- Continue to next applicable step

---

## Step 3: Is something broken?

Is there a reported failure, regression, error, crash, or data integrity issue?

**If yes:**
- Work type = `bug-fix` or `debugging` (if root cause is unknown)
- Route = **C (Bug Fix)**
- First skill: `superpowers-debug`
- If production data is affected: escalate immediately, apply Route G checks

**If no:** Continue to Step 4.

---

## Step 4: Is this adding a capability to an existing product?

A capability that didn't exist before — a new API endpoint, a new user flow, a new integration, a new screen on an existing product.

**If yes:**
- Work type = `new-feature`
- Route = **B (New Feature)**
- If user-facing (from Step 2): add UX Gate
- If high-risk (from Step 1): add Route G checks

**If no:** Continue to Step 5.

---

## Step 5: Is this a new product, MVP, or major module from scratch?

No existing codebase to integrate into — starting from zero, or a completely new subsystem.

**If yes:**
- Work type = `new-product`
- Route = **A (New Product)**
- All phases mandatory including churney-os, design system, and full UX stack

**If no:** Continue to Step 6.

---

## Step 6: Is this improving structure or quality without changing behavior?

Renaming, reorganizing, extracting, simplifying — no new features, no bug fixes. Behavior is identical before and after.

**If yes:**
- Work type = `refactor`
- Route = **E (Refactor)**
- Require: tests passing before refactor starts; same tests passing after
- No behavior change is a hard requirement — any behavior change classifies as `new-feature` or `bug-fix`

**Special cases:**
- Performance improvement without behavior change → Route F (Performance)
- Security hardening without feature change → Route G (Security)

**If no:** Continue to Step 7.

---

## Step 7: Is this preparing a release, PR, or deployment?

Merging, tagging, deploying, writing release notes, cleanup before ship.

**If yes:**
- Work type = `release`
- Route = **H (Release)**
- Minimum: `superpowers-verify` + `superpowers-finish`
- Add `uiux-design-qa` if any user-facing changes are included in the release

---

## Tie-Breaker Rule

When a task matches multiple steps (e.g., a new feature that also fixes a bug in the same area), use this rule:

**Pick the route that matches the primary intent. Inherit risk checks from all other matching routes.**

Example: "Add Google OAuth and fix the existing session bug at the same time."
- Primary intent = new feature → Route B
- Also touches broken auth → inherit Route C verification requirement (failing test before fix)
- Also touches auth surface → inherit Route G checks (rollback notes, threat statement)

The output is Route B with Route C and Route G supplements — not three separate routes.

---

## Route Receipt

Before starting work, output this receipt:

```
Route Receipt
─────────────────────────────────────────────
Request:        [one-line description]
Classification: [work type] | [surface area] | [user impact] | [risk level] | [reversibility]
Primary route:  [letter and name]
Supporting:     [any supplement routes from tie-breaker, or "none"]

Skills selected:
  Phase 0: [skill]
  Phase 1: [skill] [or "skipped — not user-facing"]
  Phase 2: [skill]
  Phase 3: [skill]
  Phase 4: [skill]
  Phase 5: [skill]

Skills intentionally skipped:
  [skill] — reason: [why it doesn't apply]

Evidence required:
  [what must exist before claiming done]

Stop conditions:
  [anything that halts progress and requires explicit approval]
─────────────────────────────────────────────
```

Do not begin Phase 0 until the Route Receipt is output.
