# Example: Production Incident

**Request:** "URGENT — subscribers stopped receiving daily briefing emails since 2am. Revenue-critical."

---

## Classification
```
Work type:    incident
Surface area: backend + api (email delivery + cron)
User impact:  revenue-critical (paid subscribers not receiving core product value)
Risk level:   critical
Reversibility:moderate (cron can be re-triggered; missed emails cannot be retroactively sent)
Route:        C (Bug Fix) with critical-risk escalation
```

## Escalation
```
⚠️ CRITICAL ESCALATION — Stop and state scope before proceeding

Trigger: Revenue-critical production failure affecting paid subscribers
Risk: Continued failure = subscriber churn, refund requests, trust damage
Data scope: Subscriber records, email delivery logs, cron execution history
Rollback: Re-trigger cron manually for missed window; revert any recent deploy
Action: Proceeding with incident protocol — no code changes until root cause confirmed.
```

---

## Incident Protocol (Route C Compressed for Speed)

**Phase 0 — Root Cause First (no fixes yet)**

```
Step 1: Check cron execution logs
  → Was the cron job scheduled? Did it fire at 2am?
  → Check: Vercel cron logs / server logs for 2am IST

Step 2: Check for recent deploys
  → git log --since="24 hours ago"
  → Any deploy between midnight and 2am?

Step 3: Check email service status
  → Resend / SendGrid / Postmark status page
  → Delivery failure rate in provider dashboard

Step 4: Reproduce locally
  → Trigger the briefing send manually for one subscriber
  → Observe: does it succeed, fail silently, or throw?

Step 5: Form hypothesis
  Evidence collected: [what was observed at each step]
  Root cause: [specific — not "email isn't working"]
```

**Hypothesis (example output after investigation):**
```
Root cause: Resend API key rotated by team member at 1:47am — environment variable
not updated in Vercel production. Cron fires at 2am, API call fails with 401 Unauthorized.
Emails fail silently — no error surfaced to monitoring.

Evidence:
  - Cron fired at 02:00:03 IST (confirmed in Vercel logs)
  - Resend dashboard: 847 delivery failures starting 02:00 IST
  - Local test with old API key: 401 Unauthorized
  - Local test with new API key: delivery succeeds
```

**Phase 3 — Minimum Fix**

```
Fix: Update RESEND_API_KEY in Vercel production environment
  → Settings → Environment Variables → Update → Redeploy

NOT doing: any code changes, schema changes, or refactors during incident

Surgical scope: one environment variable. Nothing else.
```

**Phase 4 — Verification**

```
Fix applied: ✅ RESEND_API_KEY updated in Vercel
Redeploy: ✅ Deployed at [time]
Manual test: Triggered briefing send for 1 subscriber → delivered ✅
Resend dashboard: delivery rate returning to normal ✅

Missed window: 2am–[fix time] — 847 subscribers did not receive briefing
Decision needed: Re-send missed briefing? (Separate user decision — not auto-acted on)
```

**Phase 5 — Finish**

```
Summary: Production incident — email delivery failed 2am–[time] due to rotated API key
  not propagated to Vercel environment. 847 briefings undelivered.
Root cause: Missing process for propagating secret rotation to production env.
Fix: API key updated in Vercel. Delivery restored.
Remaining risks:
  - 847 subscribers missed today's briefing (communication / re-send decision pending)
  - No alerting exists for email delivery failures (monitoring gap)
Next steps:
  1. Decide on re-send for affected subscribers
  2. Add Resend delivery failure alert to monitoring
  3. Document secret rotation runbook
```

---

## Incident Principles

1. **Diagnose before touching anything.** A wrong fix in production is worse than the incident.
2. **Minimum scope.** Fix the one broken thing. Refactor later.
3. **State what you're not doing.** "I am not changing X during incident recovery."
4. **Surface the monitoring gap.** Every incident reveals a missing alert. Log it.
5. **Separate the fix from the follow-up.** Restore service first. Improve process second.
