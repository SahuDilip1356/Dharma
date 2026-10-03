# Dharma3 Skill Evaluation — Claude Haiku 4.5

## Q1

Files read: `SKILL.md`, `phase-plan.md`

### Response to: `/dharma3 new "Healthcare clinic SaaS: appointment booking for small Indian clinics"`

**Parsing:** Subcommand `new` with intent string. Per SKILL.md subcommand table, load `phase-plan.md` for "Interrogate intent → PRD → roadmap → write STATE.md".

**Action sequence:**

1. **Check memory/STATE.md** — Not found (fresh project). No active project context.

2. **Interrogate intent (forcing questions, per phase-plan.md step 1):**
   - Pain reframe: "What specific friction do small Indian clinic staff face with current booking (paper/phone/Excel)? Cost of cancellations? Patient no-shows? Staff overhead?"
   - Success criteria: "What metrics define success — bookings per staff FTE? No-show reduction % ? Revenue impact? Patient NPS?"
   - Out of scope: "Telemedicine? Insurance billing? Multi-location chains? Analytics/BI?"
   - MVP: "Is MVP single-clinic, single-practitioner, or multi-staff per clinic?"
   
   *Wait for answers before proceeding.*

3. **Write PRD to `plans/PRD.md`** — Using phase-plan.md reference to "templates/PRD_TEMPLATE.md", I would structure:
   - Problem: pain from current booking flow
   - Target user: clinic owner/receptionist at small clinic (10–50 beds)
   - Job stories: "As a receptionist, I want to see open slots so that I can confirm availability without calling the doctor"
   - Success metrics: time-to-book <2min, no-show reduction ≥20%, staff time saved/week
   - Non-goals: telemedicine, billing, multi-location (if out of scope)
   - Risks: SMS/email delivery in rural India, network assumptions, feature creep

4. **Draft roadmap** — Coherent, shippable phases (per phase-plan.md step 3):
   - Phase 1: Core booking (add appointments, view calendar, confirm slot)
   - Phase 2: Patient SMS notifications + no-show reduction
   - Phase 3: Staff scheduling, multi-practitioner
   - Phase 4: Analytics, feedback loops
   
   *Lean MVP = Phase 1 only.*

5. **Initialize `memory/STATE.md`** from `state-schema.md` template:
   ```
   # STATE — Healthcare Clinic Booking SaaS
   
   _Last updated: 2026-10-02 · /dharma3 new_
   
   ## Now
   - Active phase: 1 — Core booking
   - Active wave: —
   - Next action: `/dharma3 plan 1` to decompose Phase 1 into atomic tasks
   
   ## Roadmap
   | Phase | Goal | Status |
   |---|---|---|
   | 1 | Core booking: add appointments, view calendar | todo |
   | 2 | SMS notifications, no-show reduction | todo |
   | 3 | Multi-practitioner, staff scheduling | todo |
   | 4 | Analytics, feedback | todo |
   
   ## Dependency graph (current phase)
   — (awaiting task plans)
   
   ## Decisions
   — (none yet)
   
   ## Open loops
   | Opened | Loop | Next action |
   |---|---|---|
   | 2026-10-02 | Clarify target clinic size / multi-location scope | Answer forcing questions |
   ```

6. **Stop and recommend:** "Next: `/dharma3 plan 1` to decompose Phase 1 into atomic, context-fit tasks."

---

## Q2

Files read: `SKILL.md`

### Response to: `/dharma3 govern gate`

**Parsing:** Subcommand `govern` with argument `gate`. Per SKILL.md line 22 and subcommand table, this is "AI governance: budget gate before a wave or cost/latency report".

**Action:**

Run the standalone tool:
```bash
python3 ~/.dharma3/scripts/govern.py gate
```

**Expected behavior (per SKILL.md):**
- Checks AI cost budget before dispatching a parallel wave
- Blocks execution if budget exceeded or risk threshold tripped
- Returns gate status: pass/fail + cost estimate + credit balance

**What I would do in real execution:**
1. Verify script exists at `~/.dharma3/scripts/govern.py` (per SKILL.md note: "Scripts live in `~/.dharma3/scripts/` — run them, don't read them")
2. Run the script with `gate` argument
3. Parse output: gate status, cost breakdown, any warnings
4. Report gate result to user: "Gate [PASS|FAIL]. Estimated cost: $X. Credits remaining: Y. Proceed? Y/n"
5. If user confirms, resume `/dharma3 execute <wave>`; if fail, escalate or adjust plan

**Note:** This runs outside the PLAN→ROUTE→EXECUTE→VERIFY→SHIP loop as a governance check point, typically invoked before executing a wave.

---

## Q3

Files read: `SKILL.md`, attempt `memory/STATE.md` (not found)

### Response to: `where were we on SubSense?`

**Parsing:** Trigger phrase "where were we" (SKILL.md line 8) → resume project. Per SKILL.md line 62: "Always read `memory/STATE.md` first."

**Action:**

1. **Check `memory/STATE.md`** — File does not exist; no active project state captured.

2. **Response to user:**
   ```
   No active SubSense project found in memory/STATE.md. 
   
   Either:
   - SubSense is not the current project (different project loaded)
   - No session has initialized SubSense yet (no /dharma3 new run)
   - Project was archived/cleared
   
   To resume or start SubSense:
   - `/dharma3 new "SubSense: <intent>"` to begin
   - Or provide the path to the SubSense project's memory/STATE.md if it exists elsewhere
   ```

**Note:** Per SKILL.md, memory loads automatically on SessionStart via hook. If SubSense STATE.md existed, it would be auto-injected. Since it's absent, the project is not tracked in this session.
