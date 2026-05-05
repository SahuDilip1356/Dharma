# Evidence Contract

Defines what counts as valid evidence per work type and phase.
The orchestrator enforces this contract before any completion claim is accepted.

---

## The Rule

**Never say:** done / fixed / complete / working / production-ready

**Unless one of these applies:**

| Language | Condition |
|----------|-----------|
| `Implemented and verified with [evidence].` | Evidence provided below |
| `Implemented but not runtime-verified — [what's missing].` | Code change made, runtime check not possible |
| `Planned only; no code changed.` | Research or planning output only |
| `Partially complete; remaining risks: [list].` | Known gaps acknowledged explicitly |
| `Blocked: [specific blocker].` | Prerequisite missing |

---

## Evidence Types by Category

### Code Evidence
| Evidence | How to Provide |
|----------|---------------|
| Unit tests passing | `npm test` / `pytest` output — pass count + 0 failures |
| Integration tests | Same — with scope note (which integration) |
| E2E tests | Test runner output |
| TypeScript typecheck | `tsc --noEmit` — exit code 0 |
| Lint | `eslint` / `biome` — exit code 0 |
| Build success | `npm run build` — exit code 0, no errors |

### Runtime Evidence
| Evidence | How to Provide |
|----------|---------------|
| Manual test | Steps taken + what was observed (not "it worked") |
| API response | Status code + response body excerpt |
| Browser console | "No errors in console" + screenshot or log |
| Network requests | Request/response captured from DevTools |
| Logs | Relevant log lines, not full dump |

### UI Evidence
| Evidence | How to Provide |
|----------|---------------|
| Screenshot review | Screenshots at 375px, 768px, 1280px |
| Accessibility check | `uiux-accessibility-review` findings (pass or findings list) |
| Keyboard navigation | Tab order tested, focus visible, Escape works |
| State coverage | Each state triggered and verified: empty / loading / error / success |
| Color contrast | Contrast ratios checked for text + interactive elements |

### Performance Evidence
| Evidence | How to Provide |
|----------|---------------|
| Timing baseline | Before measurement (method + value) |
| Timing result | After measurement (same method + value) |
| Bundle size | Before and after `npm run build` output |
| Lighthouse | Score before and after (same URL, same conditions) |
| Query timing | DB query time before and after |

### Security Evidence
| Evidence | How to Provide |
|----------|---------------|
| Permission checks | Test cases covering auth + unauth paths |
| Secret handling | Confirm no secrets in code, logs, or responses |
| Input validation | Tests for malformed input, XSS, injection paths |
| Audit logging | Confirm sensitive actions are logged |
| Rollback plan | Stated: how to revert if needed |

### Release Gate Evidence (G6, G6.5, G7)
| Evidence | How to Provide |
|----------|---------------|
| G6 `/review` clean | Command output + finding count by severity + resolution log |
| G6.5 `/ultrareview` clean | Command output + critical/high/medium counts + resolution log |
| G7 SME review | Named SME + credentials + date + written approval link + condition resolution status |

### Final Evaluation Evidence (Lead Agent)
| Evidence | How to Provide |
|----------|---------------|
| Lead Agent verdict | GO / CONDITIONAL / HOLD / NO-GO with rationale |
| Goal achievement | Restate Phase 0 goal + state achievement (yes / partial / no) |
| Cross-skill consistency | Plan vs. execution check + scope drift check + surface area check |
| Conditions resolution | If CONDITIONAL: list each condition + how it was resolved + sign-off |
| Human escalation | If escalated: human name + decision + date |

---

## Evidence Requirements by Route

| Route | Minimum Evidence |
|-------|-----------------|
| A (New product) | Tests + screenshots + a11y + responsive + PR summary |
| B (New feature) | Tests + acceptance criteria met + UI screenshots if user-facing |
| C (Bug fix) | Reproduction test (RED before fix) + GREEN after + suite passing |
| D (UI/UX design) | Screenshots at breakpoints + a11y findings + state coverage |
| E (Refactor) | Suite passing before + suite passing after + minimal diff |
| F (Performance) | Before/after metric (same method) + risk note |
| G (Security) | Auth test coverage + secret handling confirmed + rollback note |
| H (Release) | Suite passing + known risks + deploy/rollback notes |

---

## Forbidden Evidence

These do not count:

| Claim | Why It Fails |
|-------|-------------|
| "It should work" | Prediction, not evidence |
| "I believe it's correct" | Opinion, not verification |
| "Tests probably pass" | Not run |
| "Looks good to me" | Not measured |
| "Same as before" | Not verified |
| "The build ran last time" | Stale — must be fresh |
| "I tested it manually" | Acceptable only with explicit steps + observations |

Manual verification is acceptable **only if** you state:
1. What you did (exact steps)
2. What you observed (exact outcome)
3. What device / browser / environment
