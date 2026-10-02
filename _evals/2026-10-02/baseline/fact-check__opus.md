## Q1
Files read: SKILL.md, educational-tips.md

**Mode:** The request says "fact check this" about a single sentence, but the sentence holds three separate factual claims, so it is complex enough for **Mode 1 (full card)**. In real use I would generate the self-contained HTML fact-check card. Its content is below. No live web access in this dry run, so everything is **based on knowledge through mid-2026, not live-verified**, and confidence is lowered one level.

**Step 1: Claim decomposition**
- **C1 (F):** Every company must appoint a Data Protection Officer (DPO).
- **C2 (F):** The deadline is 2025.
- **C3 (S):** Non-compliance means a ₹500 crore fine.
- **I (implied):** One DPDPA penalty covers "not having a DPO".

**Step 2/3: Searches I would run and what each would establish**
1. `site:meity.gov.in DPDP Act 2023 text` and the eGazette PDF (Tier 2, primary text). Checks Section 10 (DPO duty) and the Schedule (penalties).
2. `DPDP Rules 2025 notified phased timeline` on MeitY / PIB (Tier 2). Checks commencement dates.
3. `"500 crore" DPDP draft 2022` on PIB, Reuters, Economic Times and Medianama (Tier 3/6). Traces where the ₹500 cr figure came from.
4. Commentary from law firms and IAPP (Tier 5) for cross-checking.

**Per-claim verdicts (provisional)**
- **C1: FALSE.** Section 10 requires a DPO only from **Significant Data Fiduciaries**, which the government designates based on volume and sensitivity of data, risk and similar factors. Ordinary Data Fiduciaries only need to publish a contact person who can answer data-principal questions (Sec 8(9)).
- **C2: FALSE.** The DPDP Rules were notified in November 2025 with a phased roll-out. Most substantive obligations take effect about 18 months later (around May 2027), not "by 2025".
- **C3: MISLEADING.** ₹500 crore was the cap in the **2022 draft bill**. The enacted 2023 Act's Schedule sets the highest single penalty at **₹250 crore**, for failing to take reasonable security safeguards. Missed SDF obligations, which include the DPO duty, carry up to ₹150 crore. Penalties are imposed per instance by the Data Protection Board, and they are maximums, not automatic amounts.

**Overall verdict: FALSE** · **Confidence: Medium.** The statute text is unambiguous, but this was not live-verified and timelines can be amended.

**MFS ≈ 63 (Problematic)**
- CFS = (10+10+7)/30 × 100 = **90**
- MTS: B2 uncited claim (Moderate 4) + D1/D7 old draft figure presented as current law (Moderate 4) + A3 deadline urgency (Minor 1) = 9/24 → **38**
- SCD: unattributed claim (Tier 8 → 10) → 10/30 × 100 = **33**
- MFS = 45 + 11.3 + 6.7 = **63**

**Origin trace:** this is likely a mutated version of 2022 draft coverage, where "₹500 crore" was the headline figure. Two things got distorted: the SDF-only DPO duty widened to "every company", and the phased dates collapsed into "2025".

**Counterfactual:** If the claim were true, we would expect a gazette notice requiring DPOs at every entity, MeitY FAQs about a 2025 deadline, and enforcement news. None of these exist.

**Learn the technique (D1, old content as new):** "Before you share, check the date and the first appearance." Penalty figures from a draft are not the law. Check the enacted text (eGazette) and not a summary of it.

**Share-safe summary:** "Under DPDPA, only Significant Data Fiduciaries must appoint a DPO. Most obligations phase in by about 2027. The maximum penalty is ₹250 cr per instance, not ₹500 cr."

*AI-assisted analysis, not a definitive fact-check. For critical decisions consult professional fact-checkers and primary sources. Verify key findings independently.* This is not legal advice. Confirm your company's obligations with counsel.

## Q2
Files read: SKILL.md, educational-tips.md

**Mode 4 (Quick Check).** This is a single question about whether a source is reliable. Not live-verified (knowledge through mid-2026).

**Verdict: Source UNRELIABLE · Claim UNVERIFIED, very likely FALSE · Confidence: Medium**

**Why:** An announcement that WhatsApp is leaving a market of more than 500 million users would come from Meta itself and would be on Reuters, PTI and every Indian outlet within hours. A lone, anonymous `.biz` blog is a Tier 7–8 source. "WhatsApp is shutting down in India" is a recurring rumor. It feeds on a real event: in 2024 WhatsApp told the Delhi High Court it would leave India if it were forced to break encryption under the IT Rules' traceability clause. That was a conditional legal argument, not an announced exit.

**What I would search (Step 2/3):**
1. Meta / WhatsApp newsroom and @WhatsApp official posts (Tier 2). Would establish whether any exit announcement exists.
2. `WhatsApp India shutdown` on Reuters / PTI / The Hindu (Tier 3). If none of them report it, the claim fails.
3. `WhatsApp shutting down India fact check` on BOOM, Alt News, Factly and AFP India, all IFCN-certified (Tier 1). These would likely turn up earlier debunks.
4. Lateral read on the domain: WHOIS age, About page, author names, other posts. Would establish whether it is a content farm or ad-driven site.

**Confidence factors:** It is down from High because I could not check live news, and "next month" is recent by definition. The absence of any Tier 1–4 corroboration within my knowledge still counts strongly against it.

**Tip (lateral reading):** You cannot judge a site from inside the site. STOP, open a new tab, search the domain name plus "fact check", and find better coverage of the claim itself. The urgency of "next month" (A3) is meant to make you forward it before you check.

**Share-safe summary:** "No credible outlet or WhatsApp itself has announced an India shutdown. The only source is an anonymous .biz blog. Don't forward it."

*AI-assisted analysis, not a definitive fact-check. Verify key findings independently.*

## Q3
Files read: SKILL.md

This is a creative request. The fact-check skill says it is not for opinion or creative content, so I would not run the pipeline. I would just write the poem:

**What Stays Mine**

I left my footprints in the snow
of every form I filled,
a name, a date, a place I go,
a quiet that was spilled.

The cookies crumble, crumbs remain,
the maps recall my street,
my heartbeat logged, my search for rain,
the strangers that I meet.

But there's a room no cursor finds,
a drawer without a key,
the half-said thoughts, the private minds
of who I choose to be.

So let me lock the door and draw
the curtain, soft and wide.
Not every truth is meant for law,
some truths just live inside.
