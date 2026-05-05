# SME Review Gate (G7) — Human Subject-Matter Expert in the Loop

Defines when human domain-expert review is mandatory and how it produces evidence. Closes Gap #3 from `agent-architecture.md` — the Deployment Framework's "Human SME in the Loop" step.

> **Distinct from `/review` and `/ultrareview`:** Code review (G6, G6.5) checks engineering quality. SME review (G7) checks **domain correctness** — legal accuracy, medical safety, financial compliance, brand integrity. A code reviewer cannot validate that a privacy policy is legally compliant; a doctor cannot validate that a payment flow is bug-free. Different gates, different reviewers.

---

## When G7 is mandatory

The orchestrator triggers G7 when ANY of these surfaces appear in the work, regardless of code quality:

### Legal / Regulatory
- Privacy policies, terms of service, cookie consent text
- Compliance documents (DPDPA, GDPR, HIPAA, PCI, CCPA, SOC2 — any regulated domain)
- Contracts, vendor agreements, data processing agreements
- Public claims about regulatory status ("HIPAA-compliant", "DPDPA-ready")
- Data retention, data deletion, consent collection logic that affects user rights

### Medical / Clinical
- Any medical claim, dosage, treatment recommendation
- Healthcare data handling logic
- Clinical decision support features
- Drug interaction or allergy logic
- Diagnostic content shown to patients or providers

### Financial / Investment
- Investment advice, fiduciary content
- Tax calculations or filings
- Audit findings or financial statement language
- Fraud detection thresholds
- Retirement planning recommendations
- Lending or credit decisions

### Brand / PR / Crisis
- Public-facing copy on a sensitive topic (deaths, lawsuits, breaches)
- Crisis communications (data breach disclosures, recall notices)
- Major launch announcements with regulatory implications
- Social media posts in heated contexts
- Founder or executive statements published as company position

### Specialized Technical Claims
- Scientific content presented as authoritative
- Cryptography implementations
- Safety-critical systems (transportation, industrial, medical devices)
- AI safety claims (anti-bias, anti-hallucination guarantees) made publicly

### Compliance-Critical Paths (overlap with G6.5 but G7 is also required)
- Anything that already triggers G6.5 `/ultrareview` AND involves the domains above
- G7 runs IN ADDITION to G6.5, not instead

---

## Who is the SME

G7 requires a **named human reviewer** with verifiable domain credentials. The orchestrator should ask for the reviewer's identity at gate entry — never accept a generic "sent for legal review" without a name.

| Domain | Acceptable SME |
|---|---|
| Legal / Regulatory | Licensed attorney in the relevant jurisdiction; DPDPA/GDPR-trained compliance officer |
| Medical / Clinical | Licensed physician or clinical specialist in the relevant area |
| Financial / Investment | Certified Financial Planner, CPA, registered investment advisor |
| Brand / PR / Crisis | Senior brand director, PR head, or designated crisis-comms lead |
| Specialized Technical | Subject expert with peer-reviewed publications or recognized certification |

**For solo founders:** if no in-house SME exists, the founder must explicitly accept the risk of proceeding without SME review and document that acceptance in the decision log. The default is NOT to proceed.

---

## Gate Protocol

### Entry Criteria
- Phase 5 Finish Gate evidence exists
- G6 (`/review`) has passed
- G6.5 (`/ultrareview`) has passed if applicable
- The work matches at least one G7 trigger above

### Action

```
1. PACKAGE the work for SME review
   - Plain-English summary (no jargon, no code)
   - Specific questions for the SME (not "review this" — be precise)
   - Highlighted areas of legal/medical/financial concern
   - Background context the SME needs to assess correctly

2. DELIVER to the named SME
   - Email, share, or other documented channel
   - Note delivery time and method

3. WAIT for written response
   - SME approval must be in writing (email, signed doc, ticket comment)
   - Verbal approvals are NOT sufficient — re-request in writing
   - Conditional approvals must list specific conditions

4. CAPTURE the response in evidence
   - SME name, credentials, date of review
   - Approval status: approved / approved-with-conditions / rejected / requested-changes
   - Conditions or required changes (if any)
   - Link to the written approval document
```

### Exit Evidence

```
G7 SME Review Evidence
─────────────────────────────────────────────
SME Name:             [full name + credentials]
Domain:               [legal | medical | financial | brand | technical]
Date submitted:       YYYY-MM-DD
Date approved:        YYYY-MM-DD
Approval status:      [approved | approved-with-conditions | rejected]
Conditions:           [list, or "none"]
Conditions resolved:  [yes/no — must be yes before release]
Written approval at:  [link to email, doc, or ticket]
```

### Block Condition

- **Rejected:** Halt the release. Address the rejection reason in collaboration with the SME. Re-submit and re-run G7.
- **Approved-with-conditions:** Conditions MUST be resolved before release. Document the resolution. Re-confirm with SME if material changes were required.
- **No written approval:** Cannot pass G7 with verbal-only approval. Request written.
- **SME refuses to review:** Escalate to a different qualified SME. Do not proceed without one.

---

## Edge Cases

### Solo founder with no in-house SME
This is common for early-stage products. Acceptable resolutions in priority order:

1. **Hire a one-time external SME** — a licensed lawyer for a contract review, a doctor for a clinical claim. Document fee + scope.
2. **Use a vetted SME marketplace** — Justia, UpCounsel, Doximity (medical), etc.
3. **Accept the risk explicitly** — founder signs off in `decisions.md` with rationale: *"No SME review obtained for [scope]. Risk accepted because [reason]. Mitigation: [if any]."* This option is ONLY valid for low-stakes content; never for regulated content (DPDPA, HIPAA, PCI, financial advice given for fee).

### SME unavailable on deadline
Slip the deadline. **Never publish regulated content on time at the cost of skipping G7.** A late publication is recoverable; a regulatory finding is not.

### SME disagrees with a previous SME
- Treat the most-recent qualified SME as authoritative
- Document the disagreement and rationale for the chosen path
- If both SMEs are equally qualified and disagree on a fundamental issue, escalate to a third opinion

### Internal vs external SME
Both are valid. The same evidence requirements apply (named, credentialed, written approval).

---

## Recordkeeping

All G7 evidence is preserved in:

- `[project]/memory/decisions.md` — short entry: domain, SME, date, outcome, link
- `[project]/legal/` (or equivalent) — full SME review documents
- `[project]/memory/episodic/` — session digest noting the SME review pass

**Retention:** Indefinite for regulated domains. SME approvals are evidence in a compliance audit and may be required years after the fact.

---

## How G7 fits with G6 and G6.5

```
Phase 5  Finish Gate              (existing)
Phase 5.5 ─┐
            ├── G6:    /review         every meaningful change
            ├── G6.5:  /ultrareview    high-risk code (auth/payments/migrations/AI/infra)
            └── G7:    SME Review      domain-critical content (legal/medical/financial/brand)
                                       — G7 runs IN ADDITION to G6.5 when both apply
```

A change that touches authentication AND a privacy policy needs both G6.5 (security review) and G7 (legal review). The two gates check different things and both must pass.

---

## Common failure modes (and how this gate prevents them)

| Failure | Without G7 | With G7 |
|---|---|---|
| Privacy policy claims "GDPR-compliant" but isn't | Ships, regulatory action follows | Caught by legal SME, blocked |
| Medical app suggests dosage outside guidelines | Ships, patient harm possible | Caught by clinical SME, corrected |
| Investment app gives advice without disclaimers | Ships, regulatory or fiduciary action | Caught by financial SME, fixed |
| Crisis comms accidentally creates new liability | Published, brand damage | Caught by PR/brand SME, revised |
| AI feature claims "no bias" when it has bias | Published, reputational risk | Caught by AI safety + brand SME |

The pattern: code review catches code bugs; SME review catches DOMAIN bugs that code review cannot see.

---

## Why this gate exists

A skill cannot review a privacy policy for legal accuracy. A code reviewer cannot validate a clinical recommendation. The only way to catch domain errors is to put a qualified human in the loop — and to require evidence of that human's review before release.

Without G7, regulated content ships without regulatory expertise. That is the most expensive class of mistake in product work — far more expensive than a bug.

---

*Last updated: 2026-05-04*
*Maintained alongside `phase-gates.md`. SME Review Gate (G7) is part of the Phase 5 release sequence.*
