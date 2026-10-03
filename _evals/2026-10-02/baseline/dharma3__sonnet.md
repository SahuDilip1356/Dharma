## Q1

Files read: SKILL.md, phase-plan.md, state-schema.md

**Dharma3 — PLAN phase (`new`)**

Parsed: subcommand `new`. SKILL.md says to read `memory/STATE.md` first. In this dry run there is no `memory/STATE.md` in the project root, so this is a fresh project. Nothing to resume.

Per phase-plan.md, step 1 is to interrogate and wait for answers. I do not write the PRD yet. Questions I would ask:

1. **Pain.** Which pain are you solving, and for whom? Is it no-shows, phone and WhatsApp booking chaos, or receptionist workload? Who is the buyer (doctor-owner) and who is the user (receptionist, patient)?
2. **Evidence.** Have you talked to any clinics? What do they use today (paper register, WhatsApp, Practo, Excel)?
3. **Done.** What measurable success looks like in the first 90 days. For example: 10 paying clinics, no-show rate down by 30%, bookings made without a phone call above 40%.
4. **Out of scope.** For example EMR/prescriptions, billing, telemedicine, insurance, multi-branch hospitals.
5. **Smallest version that proves value.** For example a WhatsApp or SMS booking link plus a receptionist calendar plus reminders.

Because this is health data for India, I would also ask now whether patient records are in scope. That triggers DPDPA consent and data-residency obligations, and I'd flag it as a risk in the PRD.

**Stated assumptions, so I can show the next steps (you can correct them):**
- Pain: no-shows and phone-based booking at 1-5 doctor clinics.
- Success: 10 paying clinics and a 30% no-show reduction in 90 days.
- Out of scope: EMR, billing, telemedicine.
- MVP: booking link, day calendar, WhatsApp/SMS reminders.

**What I would write after answers (step 2):** `plans/PRD.md` from `templates/PRD_TEMPLATE.md`. SKILL.md and phase-plan.md don't say where that file lives. I'd check the skill folder first, then `~/.dharma3/templates/PRD_TEMPLATE.md`, which exists. Sections: Problem, Target user, Job stories, Success metrics, Non-goals, Risks (DPDPA health-data consent, WhatsApp Business API cost and approval, low digital literacy at the clinic desk).

**Draft roadmap (step 3), lean MVP first:**

| Phase | Goal | Status |
|---|---|---|
| 1 | Booking link + receptionist calendar + clinic onboarding | todo |
| 2 | Reminders (WhatsApp/SMS) + no-show tracking | todo |
| 3 | Payments/deposits + multi-doctor schedules | todo |

**STATE.md (step 4):** I would create `memory/STATE.md` per state-schema.md:

```markdown
# STATE — Clinic Booking SaaS (India)
_Last updated: 2026-10-02 · /dharma3 new_
## Now
- Active phase: 1 — Booking MVP
- Active wave: —
- Next action: Run /dharma3 plan 1
## Roadmap
(table above)
## Dependency graph (current phase)
| Task | Depends on | Wave | Status | Evidence |
## Decisions (durable)
- Health data in scope: pending answer — 2026-10-02
## Open loops
| Opened | Loop | Next action |
| 2026-10-02 | DPDPA consent approach | Decide before plan 1 |
```

Step 5: I stop and recommend `/dharma3 plan 1`. I write no code.

---

## Q2

Files read: SKILL.md (no phase file; routing table says `govern` needs none)

**Dharma3 — `govern gate`**

The routing table gives `govern <gate|report>` no file to read. The only instruction is to run `~/.dharma3/scripts/govern.py`, and SKILL.md says to run scripts, not read them. I would first check `memory/STATE.md` for the active phase and wave, since the gate runs before a wave.

I would run (I'm not running it in this dry run):

```bash
python3 ~/.dharma3/scripts/govern.py gate
```

The usage line says "budget gate", with ai_runners as the target. I can't see the script's arguments, such as `--phase`, `--budget` or a config path. SKILL.md doesn't document them. If the call fails with a usage error, I would run `python3 ~/.dharma3/scripts/govern.py --help` and use that output. I would not open the source.

How I would handle the result:
- **Exit 0 (pass):** report "budget gate passed" with the numbers printed, and say it is safe to run `/dharma3 execute <phase>`.
- **Non-zero (over budget):** do not dispatch the wave. Show the figures, add an entry to STATE.md "Open loops" (opened date, "budget gate failed", next action: raise the budget or shrink the wave), and ask you to decide.

Gaps I would tell you about: SKILL.md doesn't say what `gate` takes as input (which phase or wave), where the budget is configured, or what "ai_runners" is beyond a directory name at `~/.dharma3/ai_runners`.

---

## Q3

Files read: SKILL.md, state-schema.md

**Dharma3 — `status` (resume)**

"Where were we" is a trigger phrase. It maps to `status`, which reads `memory/STATE.md` and prints the current phase, waves, dependencies and open loops (state-schema.md). It also resumes from where STATE.md says you are.

Problem: "SubSense" is ambiguous in this workspace. Under Product Dev there are `SubSense`, `Subsense.in` (a Next.js app), `AISubSense` and `SubSavvy`. I looked for `memory/STATE.md` in each of those four and found none. The Product Dev root's `memory/` folder holds MEMORY.md, decisions.md and similar files, but no STATE.md. So I can't truthfully say where you were. I won't invent a phase or a next action.

What I would say:

> I can't find a Dharma3 STATE.md for SubSense, so I have no recorded phase, wave or next action. Which of these is the project: Subsense.in (the Next.js app), AISubSense, SubSense or SubSavvy? Is there a STATE.md elsewhere?

Fallback offers, in order:
1. Read `Subsense.in/CLAUDE.md` and its `docs/` plus `memory/decisions.md` at the Product Dev root, and give a best-effort summary. I'd label it "reconstructed, not from STATE.md".
2. Or run `/dharma3 new` or `/dharma3 prd` to bootstrap STATE.md so later sessions can resume cold.

If STATE.md did exist, the output would use the schema: Now (phase, wave, single next action), Roadmap table, Dependency graph table, Decisions, Open loops. It would then suggest the one next command (for example `/dharma3 plan N` or `execute N`).
