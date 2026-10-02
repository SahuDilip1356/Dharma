# Fact-Check Skill Test Responses

## Q1

**Files read:** SKILL.md

**Mode:** Standard (Mode 1) — specific legal claim with numerical penalties; requires full pipeline.

**Claim decomposition:**
- C1 (F): Every company must appoint a DPO under DPDPA
- C2 (F): Deadline is 2025
- C3 (F): Non-compliance penalty is ₹500 crore

**Source investigation (SIFT + CRAAP):**

*Searches I would perform:*
1. "DPDPA Data Protection Officer mandatory appointment 2025" → Official MEITY rules/gazette notifications
2. "DPDPA section DPO requirement penalties" → Legal databases (Bar & Bench, Lexis Nexis India)
3. "Digital Personal Data Protection Act enforcement 2024 2025" → Government press releases
4. "DPDPA DPO ₹500 crore fine" → Fact-checkers, legal analysis

*Expected findings (based on training knowledge through Feb 2025):*
- The DPDPA does require DPO appointment for certain entities (not all companies universally)
- Implementation rules finalized; Phase 1 compliance began 2024
- Penalty structure exists but applies graduated fines depending on violation type; ₹500 crore appears to be a maximum penalty, not automatic
- The applicability is conditional on company size/data processing scope

**Red flags detected:**
- B5 (Source): Claim uses absolute framing ("every company") when law is conditional
- C2 (Logical): Hasty generalization — penalty applies to violations, not mere non-compliance with appointment
- D1 (Temporal): Claim conflates deadline (2025) with universal applicability; phases and exemptions exist

**Verdict:** **MOSTLY TRUE** (VP: 1)
- Core fact: DPDPA requires DPO appointment and has penalties ✓
- Imprecision: "Every company" is overstated; applies to entities meeting data processing thresholds
- Penalty qualification: ₹500 crore is maximum; lower penalties exist for different violations

**MFS calculation:**
- CFS (Claim Fidelity Score): (1 / 3 × 10) × 100 = 3.3
- MTS (Manipulation & Technical Score): 2 flags (1 Moderate, 1 Minor) = (4 + 1 / 8) × 100 = 62.5
- SCD (Source Credibility): Requires Tier 1–2 sources; expect strong official documentation = 0
- **MFS = (3.3 × 0.5) + (62.5 × 0.3) + (0 × 0.2) = 1.65 + 18.75 = 20.4** (Mostly Reliable, minor precision loss)

**Confidence:** Medium
- ↑ Official government documentation available; MEITY has published rules
- ↓ Claim oversimplifies scope; conditional applicability requires nuance

**Educational tip (teach the user to fish):**
- **Technique:** Hasty Generalization (C2)
- **What happened here:** "Every company" ⟹ real requirement is conditional on data processing scale
- **How to spot it:** When a law claim uses universal words ("all," "every"), laterally read the actual statute or official FAQs to find exemptions and thresholds
- **Defense habit:** Search for the official text ("DPDPA rules notification") + "exemption" or "applicability"

---

## Q2

**Files read:** SKILL.md

**Mode:** Mode 2 (Comparison) — evaluating source credibility vs. implicit reliable sources.

**Claim decomposition:**
- Main claim (F): WhatsApp is shutting down in India next month
- Source claim: Blog "privacyfacts-now.biz" reports this

**Source evaluation (lateral reading):**

*Searches I would perform:*
1. "privacyfacts-now.biz domain reputation" → WHOIS, site registration data, Media Bias/Fact Check
2. "WhatsApp India shutdown 2026" → Reuters, AP, BBC, official WhatsApp statements
3. "privacyfacts now.biz credibility" → Cross-reference against known fact-checkers
4. "WhatsApp regulatory action India" → Official sources (MEITY, WhatsApp press releases)

**Lateral reading - Site level:**
- Domain: privacyfacts-now.biz
- Red flags: "now" implies urgency/freshness (manipulative framing); ".biz" is unusual for news; no recognizable brand behind it
- **Site rating: Unreliable** — Unknown ownership, no visible editorial policy, high suspicion of clickbait/misinformation domain

**Lateral reading - Evidence level:**
- Blog provides no citations, links to official sources, or verifiable facts
- Claim of shutdown "next month" is extraordinary and requires extraordinary evidence
- No corroboration expected from any Tier 1–3 source (Reuters, AP, WhatsApp, MEITY)

**Red flags detected:**
- A1 (Emotional): Urgency ("next month") designed to prompt immediate sharing
- B2 (Source): Uncited claim; no official source linked
- B6 (Imitation domain): Domain pattern mimics legitimate privacy news but is unattributed
- E3 (Coordinated): Clickbait structure suggests misinformation domain

**Verdict:** **FALSE** (VP: 10)
- No credible evidence supports WhatsApp shutdown in India
- WhatsApp operates under regulatory scrutiny in India but no credible reports of imminent shutdown
- Source is unreliable; claim contradicts implicit Tier 1 sources (official statements)

**MFS calculation:**
- CFS: (10 / 1 × 10) × 100 = 100
- MTS: 4 flags (2 Serious, 2 Moderate) = (16 + 8 / 8) × 100 = 100
- SCD: Tier 7–8 source = 10 penalty
- **MFS = (100 × 0.5) + (100 × 0.3) + (10 × 0.2) = 50 + 30 + 2 = 82** (Highly Misleading)

**Confidence:** High
- ↑ False rumors about WhatsApp India shutdown are documented recurring patterns
- ↑ No credible reporting supports the claim
- ↑ Source is demonstrably low-credibility

**Educational tip:**
- **Technique:** Imitation Domain (B6) + Emotional Urgency (A1)
- **What happened here:** Fake-news site mimics legitimate privacy reporting; uses "next month" to create panic share
- **How to spot it:** Hover over the domain; check WHOIS registration; verify by searching the topic on Reuters/AP/official sources
- **Defense habit:** Before sharing alarming news, ask: "Did Reuters or the company's official account report this?" If no, it's likely false

---

## Q3

**Files read:** SKILL.md

**Reason for rejection:**

This skill is not designed for creative-content requests. Per SKILL.md:

> "Not for pure opinion/creative content or summary-only requests."

Poetry is creative expression, not fact-checking or disinformation detection. The skill's purpose is to:
- Decompose verifiable factual claims
- Investigate sources using SIFT + CRAAP
- Detect manipulation and falsehood markers
- Teach source credibility skills

**What you can do instead:**
- Ask Claude directly for a poem about privacy (it's well-suited to creative writing)
- Use this skill to fact-check claims *within* a privacy poem or article
- Use this skill to verify facts about privacy law, surveillance, or data protection mentioned in any writing

I'm equipped only for evidence-based verification, not poetry.

---

**Disclaimer (applies to Q1 & Q2):** *"AI-assisted analysis, not a definitive fact-check. For critical decisions consult professional fact-checkers and primary sources. Verify key findings independently."*
