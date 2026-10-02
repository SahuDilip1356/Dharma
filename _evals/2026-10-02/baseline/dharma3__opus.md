## Q1

Files read: SKILL.md, phase-plan.md

**Dharma3: `new`, Phase 1 PLAN**

First step: I read `memory/STATE.md` to make sure no project is already active. *(Dry run: assumed absent, so this is a fresh project.)*

We don't write a PRD until intent and success criteria are clear. Your idea arrives as a solution ("appointment booking SaaS"), so I want to start from the pain. Please answer these before I continue:

1. **Pain, and who has it?** What hurts today, and for whom? Possible answers: the receptionist juggling phone calls and a paper register, the doctor losing time to no-shows, or the patient waiting 2 hours in a queue. Which one do you mean? Do you have evidence, such as conversations with clinics?
2. **What "done" looks like.** What measurable result would prove this works? For example: "10 clinics take more than 50% of their bookings through it within 60 days" or "no-shows drop 30%".
3. **Out of scope.** Which of these are excluded from v1: EMR/patient records, billing/GST invoicing, telemedicine, insurance, pharmacy, multi-branch chains?
4. **Smallest version that proves value.** Would a WhatsApp booking link plus a token/queue view for one doctor be enough?
5. **Context.** Who is the target clinic (single GP, dental, specialist; Tier 1 or Tier 2/3 city)? Who pays, and what can they afford per month?

I'll wait for your answers before writing anything.

---
*Proceeding under stated assumptions (to show the next steps):*
- Pain: single-doctor clinics in Tier 2 cities lose patients and time to phone-based booking and long, unpredictable waits.
- Success: 5 pilot clinics, at least 40% of appointments booked digitally, and a 25% drop in no-shows within 8 weeks.
- Out of scope: EMR, billing, telemedicine, payments, multi-branch.
- Smallest version: a WhatsApp/web booking link, a live token queue and SMS/WhatsApp reminders.

**Step 2: write `plans/PRD.md`** (from `templates/PRD_TEMPLATE.md`):
- Problem / target user (clinic owner-doctor, receptionist, patient)
- Job stories, e.g. "When a patient calls during a consultation, I want them to self-book, so I'm not interrupted."
- Success metrics (as above)
- Non-goals (as above)
- Risks:
  - **DPDPA 2023**: health data is personal data, so consent and notice are needed. This is the riskiest assumption to validate.
  - Clinics adopting a new tool at all
  - WhatsApp Business API cost
  - Low-bandwidth Android usage

**Step 3: roadmap**

| Phase | Goal | Status |
|---|---|---|
| 1 | Doctor schedule + patient self-booking via link + reminders | todo |
| 2 | Live token queue / wait-time display | todo |
| 3 | Clinic dashboard (no-shows, volume), multi-doctor | todo |
| 4 | Pilot onboarding + pricing | todo |

**Step 4: write `memory/STATE.md`**

```markdown
# STATE — ClinicBook
_Last updated: 2026-10-02T00:00Z · /dharma3 new_
## Now
- Active phase: 1 — Booking MVP
- Active wave: —
- Next action: Run /dharma3 plan 1
## Roadmap
(table above)
## Dependency graph (current phase)
| Task | Depends on | Wave | Status | Evidence |
## Decisions (durable)
- Single-doctor Tier-2 clinics first; EMR/billing out of scope — 2026-10-02
## Open loops
| 2026-10-02 | Validate DPDPA consent flow for health data | Research in plan 1 |
```

**Done for this step.** Next: `/dharma3 plan 1`.

## Q2

Files read: SKILL.md

**Dharma3: `govern gate`**

1. Read `memory/STATE.md` to find the active phase and the next wave. *(Dry run: no real STATE.md exists. If it were missing, I would stop here and tell you there's no active project to gate.)*
2. Run the budget gate before the next wave executes:

```bash
python3 ~/.dharma3/scripts/govern.py gate
```

(If the script needs the phase or wave, I'd pass it from STATE.md, e.g. `govern.py gate --phase 1 --wave W2`. SKILL.md doesn't document the script's arguments, so I'd run `govern.py --help` first rather than guess.)

3. Read the result:
   - **Pass (exit 0):** report the projected cost against the remaining budget, then recommend `/dharma3 execute <phase>`.
   - **Fail (non-zero):** do not run the wave. Report which limit was exceeded (cost, tokens, latency or drift), and add an Open loop to STATE.md: `| <date> | Budget gate failed for W<n> | Reduce wave scope or raise budget (human decision) |`.

Evidence rule: I report the script's actual output only, never "should be within budget."

**Note:** if `~/.dharma3/scripts/govern.py` isn't present, the framework isn't installed. Run `install.sh` first.

Which phase/wave do you want gated? I'll default to the next todo wave in STATE.md.

## Q3

Files read: SKILL.md, state-schema.md

This triggers "where were we", which I treat as `/dharma3 status`.

1. Read `memory/STATE.md` (normally injected automatically at session start). Check that its title says `# STATE — SubSense`. If the STATE.md in this project root belongs to a different project, or doesn't exist, I'll tell you so and ask where SubSense lives. I won't invent a status.

*(Dry run: there is no real STATE.md, so I can't report actual SubSense progress. The output format would look like this.)*

```
SubSense — status (from memory/STATE.md, last updated <timestamp> by <source>)

Now
  Phase:        <N — name>
  Wave:         <id>
  Next action:  <the single concrete next step>

Roadmap
  1 <goal> ............ done
  2 <goal> ............ in-progress
  3 <goal> ............ todo

Current phase tasks
  <task> | deps | wave | status | evidence

Open loops
  <date> — <loop> → <next action>

Recent decisions
  <decision> — <why>
```

2. Recommend the next command based on where the project stands:
   - plans with no WAVES.json → `/dharma3 route <phase>`
   - waves pending → `/dharma3 execute <phase>`
   - tasks done but no evidence → `/dharma3 verify <phase>`
   - verified → `/dharma3 ship <phase>`

**Question for you:** I don't see SubSense's STATE.md in the current directory. What's the project path? Or should I search for `memory/STATE.md` files that mention SubSense?
