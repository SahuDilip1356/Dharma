# Escalation Rules

Defines when to elevate risk level and when to stop for explicit approval.

---

## Risk Level Definitions

| Level | Meaning | Default Action |
|-------|---------|----------------|
| `low` | Isolated, easily reversible, no user impact | Proceed with standard gates |
| `medium` | Moderate scope, some user impact, reversible | Proceed with extra verification |
| `high` | Significant scope, user-facing, hard to reverse | State risk, require plan approval |
| `critical` | Production data, security, compliance, payments | Stop and get explicit approval |

---

## Escalation Triggers

Elevate risk level by one tier when ANY of these are true:

### Escalate to `medium`
- User-facing UI is changed
- New dependency added to the project
- Feature flag or configuration value changed
- New API endpoint exposed
- Test coverage is missing in the affected area

### Escalate to `high`
- Authentication logic touched
- Authorization or role/permission logic touched
- Database migration required (schema change)
- Multiple modules affected by one change
- Large refactor requested (>3 files, >100 lines changed)
- Migration or data transform involved
- AI-generated content affects user decisions

### Escalate to `critical` — Stop and get explicit approval
- Production data could be modified or deleted
- Payment, billing, invoice, tax, or financial logic touched
- Secrets, API keys, or credentials are involved
- DPDPA, HIPAA, PCI, or other compliance-regulated data in scope
- Destructive operation requested (drop table, delete records, purge data)
- Force push to main/master requested
- Irreversible deployment or migration

---

## Stop Conditions (Require Explicit User Approval Before Proceeding)

Stop execution and wait for explicit approval when:

```
1. DESTRUCTIVE ACTION
   Requested: delete, drop, purge, truncate, force-push, reset --hard
   Action: state exactly what will be destroyed, wait for "confirm"

2. PRODUCTION DATA
   Any change that touches live user data, not test/seed data
   Action: state the scope, require explicit "proceed on production"

3. COMPLIANCE SCOPE
   DPDPA personal data, HIPAA PHI, PCI card data, financial records
   Action: state the regulation, require review before proceeding

4. MISSING CREDENTIALS
   Required secret/key/token not available in environment
   Action: state exactly what is missing, do not guess or hardcode

5. CONTRADICTORY GOAL
   The request contradicts itself or contradicts a prior decision in memory
   Action: surface the contradiction, ask for resolution
```

---

## High-Risk Protocol

For `high` risk work, the following are mandatory before implementation:

- [ ] Risk explicitly stated in plain language
- [ ] Scope limited to minimum necessary (surgical-changes enforced)
- [ ] Rollback plan written before first line of code
- [ ] Tests covering the changed paths required (no exceptions)
- [ ] Broad rewrites rejected — isolated changes only
- [ ] Feature flag preferred where applicable (allows instant rollback)

---

## Escalation Output Format

When escalating, output:

```
⚠️ Escalation: [low → medium | medium → high | → critical STOP]

Trigger: [which rule fired]
Risk: [what could go wrong]
Scope: [what is affected]
Rollback: [how to undo if this goes wrong]

[For critical]: Waiting for explicit approval before proceeding.
[For high]: Proceeding with high-risk protocol. Confirm to continue.
```

---

## Financial and Healthcare Special Rules (This Product)

Because this product includes healthcare SaaS and DPDPA compliance work:

**Always escalate to `critical`:**
- Patient data (PHI) of any kind
- Clinic billing or payment records
- Consent records or data processing logs
- Any cross-border data transfer logic
- Any feature that modifies data retention or deletion policy

**Always state for DPDPA work:**
- Whether the change involves a Data Principal (user)
- Whether a Data Fiduciary action is being performed
- Whether consent is required before this data is processed
