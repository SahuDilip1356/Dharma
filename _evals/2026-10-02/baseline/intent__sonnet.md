## Q1

Files read: SKILL.md

Invoking /intent as P0 Intent. This is a new, non-trivial feature, so the skill applies. The request already names a solution (CSV export), so I would flag that /office-hours could reframe it first. I'll go on with /intent and treat the framing as an assumption to test. I would not write any files. The output is the contract below, plus the short questions I'd put to Dilip.

**Clarifying questions I'd ask (answers assumed below if unanswered):**
1. Who exactly asks for the export: the SMB owner, their DPO, or an external auditor?
2. What do auditors ask for today, and how do owners hand it over now?
3. Which fields are non-negotiable for an auditor?

**Contract (under stated assumptions):**

```
FOR (persona/context):   SMB owner/founder in India (10-200 staff) who must show a DPDPA auditor
                         or enterprise customer proof of consent. Used rarely, under time pressure.
PROBLEM (their words):   ASSUMED, to be verified: "The auditor wants proof we collected consent.
                         I can't pull it out of the tool without asking someone."
SUCCESS (observable):    Within 30 days of release, 60% of SMB accounts that open an audit or
                         customer-diligence flow export a consent-log CSV with no support ticket.
                         Median time from click to downloaded file is under 60 seconds for up to
                         100k rows.
OUT OF SCOPE:            PDF or signed audit reports; auditor login or sharing portal;
                         scheduled or emailed exports; editing or deleting logs;
                         other formats (XLSX, JSON); cross-tenant export.
ASSUMPTIONS (>=3):       1. Auditors accept a CSV and don't need a tamper-evident or signed artifact.
                         2. Existing consent records already hold the fields an auditor needs
                            (timestamp, purpose, notice version, channel, withdrawal status).
                         3. SMB owners, not auditors, will operate the export.
                         4. Volumes stay small enough for a synchronous download.
                         5. The CSV can lawfully include personal identifiers (this needs a
                            privacy review).
ROLLBACK:                Ship behind a feature flag for a subset of accounts. If the success
                         metric isn't met in 30 days, or a data-exposure issue appears, turn the
                         flag off. The export is read-only and adds no schema changes, so
                         turning it off is low-risk.
```

**Exit gate:** all six answers are present, five assumptions are logged, and the success criterion is observable. A full 8-section PRD isn't needed yet because this is a clear feature, not a new product, so I did not open prd-template.md. Handoff: `/plan-eng-review`. If the owners' real need turns out to be "prove compliance" rather than "get a CSV", go to `/office-hours` or `/plan-ceo-review` instead.

## Q2

Files read: SKILL.md, prd-template.md

A PRD for investors is a "full PRD for stakeholder review", which is the case SKILL.md points to prd-template.md for. I read it. The template says to ask its questions one at a time and stop when I can write with confidence. I have no real project data for SubSense, so I would ask:

1. Problem: who forgets renewals, and what does it cost them (in money or cancellations)?
2. Users: which segment, and what do they do today (calendar, email)?
3. Success: which SMART metric, with what baseline?
4. Constraints, market, and scope: v1 versus later.

Under stated assumptions, I'd first emit the six-answer intent contract (ends with 3 or more assumptions), then expand it into the 8-section PRD at `docs/PRD-subsense-renewal-reminders.md` (the template's output path). I'd write it to the file only in a real run.

**Intent contract (assumed):**
```
FOR:          Individuals and households paying for 10+ recurring subscriptions.
PROBLEM:      ASSUMED: "I got charged for an annual plan I forgot I had."
SUCCESS:      By day 90, 30% of active users enable reminders and 15% of reminders lead to
              a cancel or downgrade (baseline 0%, measured in-app).
OUT OF SCOPE: Auto-cancel; negotiating prices; bank-feed detection; SMS.
ASSUMPTIONS:  1. Users know their renewal dates or can import them.
              2. Push or email reminders lead to action, not fatigue.
              3. The renewal date is reliably captured.
ROLLBACK:     Feature flag, with reminders default-off for existing users.
```

**PRD skeleton (all 8 sections):**
1. Summary: 2-3 sentences using the template's fill-in sentence.
2. Contacts: table with PM, Eng, Design and Stakeholder rows. Names are marked TBD, not invented.
3. Background: context, trigger, prior work.
4. Objective: goal, business benefits, SMART metrics table with baseline/target/timeline/how measured, and non-goals.
5. Market segments: defined by problem, not demographics.
6. Value propositions: JTBD (functional, emotional, social jobs), gains and pains.
7. Solution: P0 reminder at N days before renewal; P1 snooze and channel choice; P2 calendar sync. Includes assumptions with validation methods and open questions.
8. Release: v1/v2 table, staged rollout, dependencies, and a risks table.

I would run the template's Quality Check before sharing it. An investor audience means the PRD must be readable by a non-technical reader, with no undefined jargon and a SMART metric with a baseline. Where I have no real data, I'd mark baselines and numbers as "ASSUMPTION, to be confirmed" so that nothing invented reaches investors as fact.

Handoff: `/plan-ceo-review` if scope is fuzzy; otherwise `/plan-eng-review`.

## Q3

Files read: SKILL.md

I would not invoke /intent. Its trigger is "any new product, feature, or non-trivial change". Fixing the typo "recieve" to "receive" on the SaralPrivacy pricing page is trivial and has no scope, success criterion or rollback to define. Running six forcing questions and a PRD contract for a one-word fix would be overhead.

What I'd do directly: grep the pricing page source for `recieve`, change it to `receive` with a minimal edit (touching nothing else), and check that no other occurrences remain. Because this is a dry run, I'm not running anything. I would apply the SaralPrivacy brand skill only if I were rewriting copy, which isn't the case here.

Response to user: "That's a trivial copy fix, so I'm skipping /intent. Fixing 'recieve' to 'receive' on the pricing page now."
