## Q1
Files read: SKILL.md

**/intent: P0 Intent for SaralPrivacy consent-log CSV export**

The request names a solution (a CSV export), so I'll first check the pain behind it. Three quick questions:

1. When an auditor asks for consent records today, what does the SMB owner actually do? Screenshots, raw DB pulls, emailing us?
2. Which auditors are these: DPDPA compliance auditors, statutory auditors, or customers' vendor-risk teams? What format and fields do they accept?
3. Roughly how many consent records does a typical account hold (hundreds, or 100k+)?

If the answers show the real need is "prove consent to an auditor" and not "get a file", I'd suggest running `/office-hours` before we lock this. Below is how I'd proceed under stated assumptions.

**Assumptions for this draft:** auditors are DPDPA/data-protection reviewers. Owners currently ask SaralPrivacy support for an export by email. Accounts hold up to about 50k records.

```
FOR (persona/context):   SMB owner or compliance lead on SaralPrivacy who has to hand
                         consent evidence to an external auditor during a DPDPA review
                         or a client's vendor-risk check. Non-technical, under time pressure.
PROBLEM (their words):   "The auditor wants proof of who consented to what and when, and
                         I can't get it out of the dashboard without emailing support."
SUCCESS (observable):    An owner can export a date-filtered consent log as a CSV from the
                         dashboard in under 2 minutes with no support ticket. Consent-export
                         support tickets fall to ~0 within 30 days of launch, and at least
                         one pilot auditor accepts the file without asking for reformatting.
OUT OF SCOPE:            PDF or signed "audit report" output; scheduled or recurring exports;
                         an API endpoint; exporting data-principal PII beyond what the
                         consent record already stores; multi-account or agency rollups;
                         editing or redacting records before export.
ASSUMPTIONS (≥3):        1. Auditors accept CSV, so they don't need a tamper-evident or signed
                            format. (Validate: ask 2-3 auditors or pilot customers.)
                         2. The existing consent log already has the fields auditors need:
                            principal ID, purpose, notice version, timestamp, action
                            (grant/withdraw), channel.
                         3. Synchronous export works at our record volumes; anything above
                            ~50k rows would need an async job and an email link.
                         4. Exporting the file to the owner's machine doesn't create a new
                            DPDPA exposure. The export itself should be access-logged and
                            restricted to the owner or admin role.
ROLLBACK:                Ship behind a feature flag per account. If exports cause load,
                         data-leak concerns or auditor rejection, turn off the flag and fall
                         back to the current support-ticket process. The feature is
                         read-only, so there is no data migration to reverse.
```

**Exit gate check:** all six are answered, 4 assumptions are logged, and the success criterion is observable (time to export, ticket count, auditor acceptance). The gate passes, provisionally on the answers to the questions above.

**Handoff:** this is a clear, bounded feature, so it goes next to `/plan-eng-review` to lock the export pipeline (sync vs async), the field schema, role checks and the access-log entry. If assumption 1 fails and auditors want signed evidence, the scope gets fuzzy. In that case, go to `/plan-ceo-review` first.

## Q2
Files read: SKILL.md, prd-template.md

**/intent → Full PRD: SubSense renewal reminders**

This is going to investors, which counts as a stakeholder review, so I'll expand the 6-line contract into the 8-section PRD. Before I write it, a few questions. I'd normally ask these one at a time, in this order:

1. **Problem:** Who is the reminder for? Is it the consumer tracking their own subscriptions, or a business reminding its customers to renew?
2. **Success:** What metric do investors care about here: retention, avoided unwanted charges, or engagement/DAU?
3. **Constraints:** What's the deadline for the investor update, and what channels already exist (push, email, WhatsApp)?
4. **Scope:** Is this shipped, in beta, or planned? That changes whether the PRD shows actuals or targets.

**Proceeding under assumptions:** SubSense is a consumer subscription tracker. Reminders go to users before a subscription renews. The feature is planned, so v1 has no actuals yet.

**Contract (P0 Intent)**
```
FOR:          Consumers with 5+ recurring subscriptions who lose track of renewal dates
PROBLEM:      "I got charged for something I meant to cancel."
SUCCESS:      ≥40% of reminded users take an action (keep, cancel, snooze) within 7 days
              of the reminder; unwanted-renewal complaints (survey) drop 30% in 90 days
OUT OF SCOPE: In-app cancellation on the user's behalf, price negotiation, bank-feed
              auto-detection changes, B2B dunning
ASSUMPTIONS:  1. Renewal dates in SubSense are accurate enough to remind on
              2. Users want 3-7 days of notice, not same-day notice
              3. Push and email are enough; WhatsApp isn't needed for v1
ROLLBACK:     Feature flag; reminders default off for new cohorts; no data model change
```

**PRD outline I'd write to `docs/PRD-subsense-renewal-reminders.md`:**

1. **Summary:** Renewal Reminders notifies users before a subscription renews so they can keep or cancel it on purpose. It fixes surprise charges. Success means most reminded users act before the charge lands.
2. **Contacts:** PM / Eng Lead / Design / Stakeholder (founder). Names TBD, so you'd need to fill these in.
3. **Background:** Users log subscriptions, but nothing prompts them before a charge. The trigger is support data or reviews showing surprise renewals as the top complaint. *(Needs your real signal. I won't invent one for investors.)*
4. **Objective:** The goal is fewer unwanted renewals and higher weekly active use. SMART metrics table: action rate ≥40% in 7 days; 30-day retention of reminded vs. control users +X pts; complaint rate −30% in 90 days. Baselines are marked "TBD — pull from analytics." Non-goals are as listed in OUT OF SCOPE above.
5. **Market segment:** Primary users are people with many subscriptions who've been hit by a surprise charge. Secondary users are budget-conscious households. Constraint: India-specific UPI AutoPay mandates may need different lead times. *(Confirm.)*
6. **Value proposition:** The functional job is avoiding paying for things I don't use. The emotional job is feeling in control of money. Competitive edge vs. bank alerts: a bank alert arrives *after* the charge, and ours arrives before it.
7. **Solution:** P0: reminders at a configurable 1, 3 or 7 days before renewal; push + email; one-tap "keep / remind later / mark cancelled." P1: weekly digest. P2: price-change alerts. Assumptions each get a validation method, and open questions are listed.
8. **Release:** Internal dogfood → 10% beta → full rollout. Dependencies: an accurate renewal-date field and a notification service. Risk table: notification fatigue (Med/High, mitigated with frequency caps).

**Quality check before it goes to investors:** I'd flag that every baseline, the Background trigger, and the contact names are placeholders. Investor-facing numbers must be real or clearly labelled as targets. Don't let a TBD read as a fact.

**Handoff:** it's a new product surface with fuzzy scope, so `/plan-ceo-review` is next. I'd commit it with `git commit -m "docs: PRD for SubSense renewal reminders"`.

## Q3
Files read: SKILL.md

This doesn't need `/intent`. The skill is for a new product, a feature or a non-trivial change, and a one-word copy fix on the pricing page isn't any of those. Writing a PRD contract with assumptions and a rollback plan for a typo would be ceremony with no value, so I'd just make the fix.

What I'd do:

1. Find every occurrence on the pricing page. I wouldn't assume there's only one.
   ```
   grep -rn "recieve" src/ --include="*.{tsx,jsx,ts,js,html,md,json}"
   ```
   I'd also check i18n/copy files (e.g. `locales/en.json`) and any CMS-sourced pricing content.
2. Change `recieve` → `receive` only in the pricing-page occurrences, with no other edits. If the grep finds the typo elsewhere in the site, I'd list those spots and ask before touching them, because you asked for the pricing page only. Example diff:
   ```diff
   - <p>You'll recieve a GST invoice every month.</p>
   + <p>You'll receive a GST invoice every month.</p>
   ```
3. Verify by loading `/pricing` locally and confirming the corrected text renders. If any snapshot or copy tests reference the string, I'd run those too.
4. Commit: `git commit -m "fix(copy): correct 'recieve' typo on pricing page"`.

If the typo lives in a CMS rather than in code, I can't edit it from the repo. I'd tell you which entry to change.
