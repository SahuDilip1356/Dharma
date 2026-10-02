# Intent Skill Dry-Run Evaluation

## Q1

Files read: SKILL.md, prd-template.md

**Skill response:**

Let's lock down this feature intent. I'm going to walk through the 6 forcing questions—answer each one, even if briefly:

**1. Who is this for?**
SMB compliance/privacy officers who need to demonstrate consent audit trails to external auditors and regulators. What's their context? Are they exporting monthly, quarterly, or on-demand? Are auditors asking for a specific format beyond CSV?

**2. What problem is solved (in their words)?**
"Our auditors ask us to prove who consented and when, and we can't easily pull that data into a format they'll accept" — or something closer to what you're hearing from customers. Help me understand the friction point.

**3. Success criterion — observable, measurable?**
Some options:
- Time to audit-ready export: < 2 minutes
- Audit pass rate (% of audits where CSV is accepted on first try)
- Adoption: % of active SMB customers who export at least once/quarter
- Which one matters most?

**4. Explicitly out of scope — what you will NOT build?**
For example:
- NOT custom export formats (only CSV v1)
- NOT automated scheduling/email delivery of exports
- NOT historical backfill of logs before feature launch
- What else should be off the table for v1?

**5. What might be wrong? (≥3 assumptions)**
- Auditors will accept a CSV dump; they won't demand a specific schema
- SMB owners can locate/interpret consent log fields without training
- Legal/compliance teams won't have new data privacy questions once CSV is available
- (Add more based on your highest-risk unknowns)

**6. Rollback plan — if this is the wrong bet?**
- Hide the export button; logs remain queryable in-app
- Pause feature after 2 months if adoption is <15% of SMBs
- Investigate and pivot to guided audit report instead

**Once you answer these, I'll produce the PRD contract.** What's the strongest signal you have that this is worth building right now?

---

## Q2

Files read: SKILL.md, prd-template.md

**Skill response:**

This is heading to investors, so let's produce a complete, polished PRD. I'll ask the 6 forcing questions first, then expand to the full 8-section template.

**Quick framing questions:**

1. **What triggers this now?** Is this responding to churn data, customer interviews, competitive pressure, or a roadmap slot?
2. **Who is "renewal-reminder"?** Is this targeting admins, end-users, billing contacts—who sees the notification?
3. **What's the success metric?** Reduced churn %? Increased on-time renewals? Faster payment collection?
4. **What version of this are you shipping first?** Email only, in-app banner, both? Calendar integration?
5. **Investor angle:** Are they evaluating this for retention strategy, unit economics impact, or something else?

**Once I have those,** I'll write the full 8-section PRD:
- Summary (one-liner for investor deck)
- Contacts (who owns what)
- Background (why now, what changed)
- Objective (goal + SMART metrics)
- Market Segment (who benefits, how often they renew)
- Value Proposition (JTBD frame: why this moves the needle)
- Solution (timelines, phasing, tech decisions)
- Release (rollout, risks, dependencies)

For an investor update, we need clean metrics (e.g., "Expected to reduce churn by X% and increase renewal velocity by Y days") and clear rollout timing. 

**What's the biggest risk or assumption you want to lock in before writing the deck version?**

---

## Q3

Files read: SKILL.md

**Skill response:**

This request is outside the scope of `/intent`. The skill is designed for **new products, features, or non-trivial changes**—the strategic work cycle. A typo fix on a pricing page is a one-line content correction, not a product decision.

**Better path:** Edit the pricing page directly (find and fix "recieve" → "receive") and commit it. No intent, PRD, or review cycle needed.

**When to use `/intent`:** New feature, new product, significant behavior change, scope ambiguity, stakeholder alignment needed.

**If this typo fix is blocking something else**, let me know the context and we can prioritize it in the right workflow.
