# Example: New Feature — Google OAuth

**Request:** "Add Google OAuth login as an alternative to email/password."

---

## Routing Decision Tree

**Step 1 — High-risk surface area?**
Yes — authentication is explicitly listed as high-risk.
→ Classify as `risk: high`. Apply Route G checks alongside primary route.

**Step 2 — User-facing?**
Yes — login is the primary entry point for all users.
→ Phase 1 UX Gate mandatory.

**Steps 3–5 — Broken? New feature? New product?**
Not broken. Adding capability to existing product.
→ Primary route: **B (New Feature)**

**Tie-breaker:** Primary intent = new feature (Route B) + high-risk auth (Route G supplement)

---

## Route Receipt

```
Route Receipt
─────────────────────────────────────────────
Request:        Add Google OAuth login alongside email/password
Classification: new-feature | auth | user-facing | high | hard
Primary route:  B — New Feature
Supporting:     G — Security (auth surface area, hard reversibility)

Skills selected:
  Phase 0: goal-driven-execution + think-before-coding
  Phase 1: uiux-designer + uiux-accessibility-review + uiux-responsive-review
  Phase 2: superpowers-write-plan + karpathy-discipline
  Phase 3: superpowers-tdd + surgical-changes
  Phase 4: superpowers-verify + uiux-design-qa
  Phase 5: superpowers-finish

Skills intentionally skipped:
  churney-os — reason: existing product, not new MVP
  pm-prd — reason: scope is well-defined, not a new product requirement cycle

Evidence required:
  - OAuth flow tested end-to-end in dev environment
  - No regression on email/password login
  - Rollback procedure documented
  - Token storage security confirmed (not localStorage)
  - Tests covering: happy path, token expiry, denied access, duplicate account

Stop conditions:
  ⚠️ Stop if: token storage method is localStorage — escalate to security review
  ⚠️ Stop if: existing session logic must be modified — requires explicit approval
  ⚠️ Stop if: user account merging logic is required — out of scope, define separately
─────────────────────────────────────────────
```

---

## Phase Sequence

**Phase 0 — Intent Gate** → `goal-driven-execution` + `think-before-coding`
```
Goal: Let users sign in with Google — reduce friction for new signups, retain
      email/password for existing users.
User: All users at login/signup screen
Success: Google OAuth works in production; zero regression on email/password path;
         no duplicate accounts created from same email via both methods
Out of scope: Apple Sign-In, GitHub OAuth, SSO (v2 features)

Assumptions:
  - Google Cloud project and OAuth credentials already configured (or will be created)
  - Users may have existing accounts with the same Google email → account merging required
  - Sessions handled via httpOnly cookies, not localStorage
  - NextAuth.js is the library of choice (already in package.json or will be added)

Unknowns:
  - What happens when Google email matches existing email/password account?
  - Is account merging in scope or out of scope?
  → Decision: account merging is out of scope for this task; show "email already registered,
    use email/password" error if conflict detected
```

**Phase 1 — UX Gate** → `uiux-designer` + `uiux-accessibility-review` + `uiux-responsive-review`
```
User flow:
  New user → Login page → "Continue with Google" button → Google consent screen →
    redirect back → account created → dashboard

  Existing user (email/password) → Login page → "Continue with Google" →
    Google email matches existing account → error: "This email is registered with
    email/password — use that to sign in"

  Returning OAuth user → Login page → "Continue with Google" → instant redirect → dashboard

States:
  - Default: Google button visible alongside email/password form
  - Loading: button disabled, spinner visible, "Signing in with Google..."
  - Error (conflict): "Account already exists with this email. Sign in with your password."
  - Error (OAuth denied): "Google sign-in was cancelled. Try again or use email/password."

Accessibility:
  - Button has visible focus ring
  - Loading state announced via aria-live
  - Error messages associated with the form via aria-describedby

Responsive:
  - 375px: Google button full width, above email form
  - 768px+: Google button full width at top of login card
```

**Phase 2 — Planning Gate** → `superpowers-write-plan` + `karpathy-discipline`
```
Files affected:
  - app/api/auth/[...nextauth]/route.ts (add Google provider)
  - components/LoginForm.tsx (add Google button)
  - lib/auth.ts (configure NextAuth options)
  - .env.local (GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
  - app/login/page.tsx (layout update for Google button placement)

Plan:
  Task 1: Configure NextAuth with Google provider → verify: auth callback route responds
  Task 2: Add Google button to LoginForm → verify: button renders, focus state correct
  Task 3: Handle email conflict case → verify: test confirms error message shown
  Task 4: Verify email/password login unaffected → verify: regression test passes
  Task 5: Responsive + a11y review → verify: audit findings resolved

Security checklist (Route G):
  - Tokens stored in httpOnly cookies (not localStorage)
  - CSRF protection via NextAuth state parameter
  - Redirect URI validated against allowlist in Google Cloud Console
  - No sensitive data logged during OAuth flow
  - Rollback: remove Google provider config; existing sessions unaffected
```

**Phase 3 — Build** → `superpowers-tdd` + `surgical-changes`
```
Tests written first (failing):
  - "Google button renders on login page" → FAIL before component update
  - "Google OAuth happy path creates session" → FAIL before provider config
  - "Email conflict shows correct error" → FAIL before conflict handler
  - "Email/password login still works after OAuth added" → FAIL if regression introduced

Files touched: 5 (listed in plan above)
Files NOT touched: patient data, appointment logic, billing, analytics
```

**Phase 4 — Verification** → `superpowers-verify` + `uiux-design-qa`
```
Tests: 13 passed / 0 failed
Build: ✅
Typecheck: ✅
Security: tokens in httpOnly cookies confirmed ✅
Manual: OAuth flow tested — created new account via Google, signed out, signed back in ✅
Regression: email/password login tested after OAuth config added ✅
Conflict: tested Google sign-in with email already registered → error shown ✅
Responsive: 375px ✅, 768px ✅, 1280px ✅
Accessibility: keyboard navigation to Google button ✅, error announced ✅
```

**Phase 5 — Finish** → `superpowers-finish`
```
Summary: Google OAuth added via NextAuth — new users can sign in with Google;
         existing email/password accounts show conflict error; no regression
Verified: 13 tests, manual OAuth flow, regression confirmed, security checklist cleared
Rollback: remove Google provider from lib/auth.ts; no DB migration to revert
Remaining risks: Account merging not implemented — document as known limitation in PR
Next: PR → security review → merge → monitor OAuth error rate in logs for 48h
```
