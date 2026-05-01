---
name: find-skills
description: |
  Skill gap resolver for the Dharma orchestrator. Activates when the Route Receipt
  identifies a specialized domain need that no installed Dharma skill covers.
  Searches the open agent skills ecosystem (skills.sh), verifies quality, and
  recommends installation or falls back gracefully to general capability.

  Triggers when:
  - skills-inventory.md lookup returns no match for a functional need
  - Orchestrator identifies a domain gap during route construction
  - User explicitly asks "is there a skill for X" or "find a skill for X"
  - A task requires specialized knowledge outside Dharma's 36-skill inventory

  Does NOT trigger when:
  - A Dharma skill already covers the domain (check skills-inventory.md first)
  - The gap is trivially covered by general LLM capability
  - The request is too novel or niche for the ecosystem

  Source: https://github.com/vercel-labs/skills (adapted for Dharma by Dilip Sahu)
license: MIT
metadata:
  author: vercel-labs (adapted for Dharma)
  version: "1.0.0"
---

# Find Skills — Dharma Skill Gap Resolver

**This skill fills gaps. It does not replace installed skills. Always check `skills-inventory.md` before invoking.**

---

## Dharma Phase Placement

This skill sits between **Route Receipt output** and **Phase 0 start** — it is a pre-execution resolver, not a phase skill.

```
Route Receipt output
        ↓
  Gap detected? ─── No ──→ Phase 0 begins normally
        ↓ Yes
  find-skills activates
        ↓
  Skill found + installed ──→ Update Route Receipt → Phase 0 begins with new skill
        ↓ Not found
  Gap noted in Route Receipt → Phase 0 begins with general capability + gap flag
```

---

## When the Orchestrator Invokes This Skill

**Trigger condition:** During Step 2 (Select Route) in the orchestrator, a functional skill name is identified that does not resolve in `skills-inventory.md`.

**Examples of gaps find-skills resolves:**

| Gap domain | Example request | Likely ecosystem skill |
|---|---|---|
| Changelog generation | "Create release notes from commits" | `changelog-generator` |
| PR review automation | "Review this PR for issues" | `pr-review` |
| Documentation | "Generate API docs from code" | `api-docs` |
| Data pipeline | "Parse and transform this CSV" | `data-pipeline` |
| CI/CD | "Set up GitHub Actions workflow" | `github-actions` |
| Docker/Kubernetes | "Containerize this app" | `docker-skills` |

---

## Resolution Protocol

### Step 1: Check the Skills Leaderboard

Before any search, check [skills.sh/leaderboard](https://skills.sh/) for the domain.

Top trusted sources (prefer in this order):
1. `anthropics/skills` — 100K+ installs; official Anthropic skills
2. `vercel-labs/agent-skills` — 100K+ installs; Vercel engineering skills
3. Other sources with 1K+ installs and known-good reputation

### Step 2: Search if Leaderboard Miss

```bash
npx skills find [domain-keyword]
```

Examples:
- Gap in testing methodology → `npx skills find testing playwright`
- Gap in data processing → `npx skills find data csv transform`
- Gap in CI/CD → `npx skills find github actions deploy`

### Step 3: Verify Quality Before Recommending

**Never recommend a skill based solely on search results.** Verify:

| Signal | Threshold | Action if below |
|---|---|---|
| Install count | ≥ 1,000 | Treat with caution; note in Route Receipt |
| Source reputation | Known org or 100+ GitHub stars | Flag as unverified |
| Skill scope | Covers the exact gap | Don't stretch a partial match |

### Step 4: Report to Orchestrator

Output one of three outcomes:

**Outcome A — Skill found, recommend install:**
```
🔍 Skill Gap Resolved
Gap domain: [domain]
Recommended: [skill-name] by [source] ([install count] installs)
Install: npx skills add [owner/repo@skill] -g -y
Action: Awaiting user approval to install. If approved, will add to skills-inventory.md.
```

**Outcome B — Skill found, quality concern:**
```
⚠️ Skill Gap — Low-Confidence Match
Gap domain: [domain]
Candidate: [skill-name] by [source] ([install count] installs — below threshold)
Risk: Low install count; source unverified.
Recommendation: Proceed with general capability for this task. Revisit skill ecosystem later.
```

**Outcome C — No skill found:**
```
❌ No Ecosystem Skill Found
Gap domain: [domain]
Searched: skills.sh for "[query]"
Result: No skills found with ≥1,000 installs covering this domain.
Action: Proceeding with general capability. Gap noted in Route Receipt.
```

---

## After Installation

If user approves installation:

1. Run: `npx skills add [owner/repo@skill] -g -y`
2. Add to `skills-inventory.md` under appropriate layer with status `✅ Installed (ecosystem)`
3. Update the Route Receipt with the newly resolved skill
4. Continue to Phase 0

If no install (Outcome B or C):
1. Note the gap in the Route Receipt under `Skill Gaps`
2. Proceed with general capability for the gap domain
3. Flag quality or coverage limitations in the evidence ledger

---

## Ownership Boundaries

| Owns | Does NOT Own |
|---|---|
| Discovering ecosystem skills that fill genuine Dharma gaps | Installing skills without user approval |
| Quality verification (install count, source reputation) | Executing the installed skill's logic |
| Updating skills-inventory.md after install | Deciding whether a gap matters (that is the orchestrator's call) |
| Graceful fallback reporting when no skill exists | Modifying routing-matrix.md unilaterally |

---

## Dharma Skill Creation (Last Resort)

If no ecosystem skill exists and the gap recurs frequently, suggest creating a Dharma skill:

```bash
npx skills init [skill-name]
```

This is a last resort. Prefer general capability for one-off gaps. Only propose a new Dharma skill when:
- The gap appears in 3+ different tasks
- No ecosystem skill covers it
- The domain is core to the product being built
