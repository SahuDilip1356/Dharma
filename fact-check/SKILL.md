---
name: fact-check
description: |
  Evidence-first fact-checking and disinformation detection. Decomposes content
  into checkable claims, investigates sources with SIFT + CRAAP + lateral
  reading, scores manipulation, assigns a calibrated verdict, and teaches the
  user to recognize the technique next time (prebunking). Use when the user says
  "fact check this", "verify this claim", "is this true", "check this source",
  "debunk this", or "how reliable is this"; when a claim, screenshot, article, or
  URL is submitted for verification; when a claim surfaced in deep research needs
  vetting; for side-by-side source credibility comparisons; or to brief on false
  narratives circulating on a topic. Not for pure opinion/creative content or
  summary-only requests.
---

# Fact-Check Skill

Evidence-first verification. Combines **SIFT** (Stop, Investigate the source,
Find better coverage, Trace claims), the **CRAAP test** (Currency, Relevance,
Authority, Accuracy, Purpose), **prebunking/inoculation science**, and
**claim decomposition**. Goal: not just a verdict, but transparent reasoning and
a durable skill the reader keeps.

Skip when a prior fact-check verdict in this thread already covers the claim.

Source: https://github.com/petar-nauka/fact-check-skill (Petar Nauka, MIT
licensed, v2.1) — generalized to be region/language-neutral by Dilip Sahu.

## Operating modes

- **Mode 1 — Standard:** full 11-step pipeline, HTML fact-check card output.
- **Mode 2 — Comparison:** two sources analyzed side-by-side.
- **Mode 3 — Prebunking briefing:** active false narratives on a topic + defenses.
- **Mode 4 — Quick Check:** abbreviated pipeline (Steps 1, 2, 6, 7), short text
  reply with verdict badge, confidence, key sources, one educational tip.

**Mode detection:** infer from the request. Comparative language
("compare", "which is more reliable") → Mode 2. "What false claims circulate
about X" → Mode 3. A single yes/no question, or invocation mid deep-research →
Mode 4. Ambiguous or "give me the full card" → Mode 1.

## Use inside deep research (primary use case)

When invoked during a deep-research run to vet a surfaced finding:
1. Default to **Quick Check (Mode 4)** — do not derail the research thread.
2. Return inline: `VERDICT · confidence · 2–3 tiered sources · 1 red flag (if any)`.
3. If the claim is load-bearing for the synthesis and the verdict is MIXED /
   UNVERIFIED / MISLEADING / FALSE, say so explicitly and recommend dropping or
   caveating it.
4. Escalate to the full card (Mode 1) only if the user asks, or if the claim is
   central and complex (multiple sub-claims with conflicting verdicts).

## The 11-step pipeline

### Step 1 — Claim decomposition
Classify content into units: **F** factual (verifiable), **O** opinion,
**P** prediction, **U** unfalsifiable, **I** implied (extract the hidden factual
assumption), **S** statistical (extra scrutiny). Number factual claims C1, C2…
For multi-claim content ask whether to check all or focus — skip the question
for obvious disinformation, single-claim content, or non-interactive contexts.

### Step 2 — Source investigation (SIFT + CRAAP)
Web-search the claim. **Source priority hierarchy:**
1. IFCN-certified fact-checkers (Snopes, PolitiFact, AFP Fact Check, FullFact, etc.)
2. Official institutions (WHO, CDC, EMA, statistical offices, government agencies)
3. Major wire services / quality journalism (Reuters, AP, BBC, DW)
4. Peer-reviewed publications (PubMed, Cochrane, Nature, The Lancet)
5. Domain experts (IPCC, IAEA, specialized NGOs)
6. Credible media with editorial standards
7. Blogs, personal sites, social media (low)
8. Anonymous / unattributable (very low)

**Triangulation:** seek ≥3 independent Tier 1–4 sources; lower confidence if
fewer. Run **CRAAP** per source (Currency, Relevance, Authority, Accuracy,
Purpose). *Optional:* if the claim likely originated in another language,
search that language too — not a default.

### Step 3 — Lateral reading (deep source evaluation)
For every key source:
- **3a Site-level:** ownership, mission, editorial/corrections policy, funding,
  ad model → rate Established & Transparent / Credible but Limited /
  Questionable / Unreliable / Cannot Assess.
- **3b Author-level:** named author? relevant credentials? track record? real person?
- **3c Evidence/citations:** primary sources cited? citations accurate? evidence
  type (peer-reviewed > institutional > expert > anecdotal)? data contextualized?
  → Strong / Moderate / Weak / Fabricated.
- **3d Cross-reference:** *leave the page.* Search independently for the claim,
  the author, the site's reputation (Media Bias/Fact Check, Wikipedia,
  independent journalists). If the claim appears ONLY in Tier 7–8 sources, that
  is itself a finding.
- **3e Summary table:** per source — URL, site rating, author/credentials,
  evidence quality, tier, lateral-check finding, key finding.

### Step 4 — Origin tracing
First online appearance (date-restricted search), original language, mutation
tracking (numbers inflated, hedging removed, context stripped, dates/places
shifted), known-campaign association. Output a brief origin summary.

### Step 5 — Red-flag detection
Check six categories: **A** emotional manipulation, **B** source/attribution,
**C** logical fallacies, **D** temporal/contextual (old-as-new, stripped context,
study misrepresentation), **E** coordinated/structural, **F** health-specific.
Full 40+ marker catalog with codes: [red-flags.md](red-flags.md). Record each flag:
code, quoted location, severity (Minor / Moderate / Serious).

### Step 6 — Verdict + Manipulation & Falsehood Score (MFS)

| Verdict | Color | VP | Meaning |
|---|---|---|---|
| CONFIRMED | green | 0 | Multiple reliable Tier 1–4 sources support |
| MOSTLY TRUE | lime | 1 | Core accurate; minor imprecision |
| MIXED | yellow | 3 | Both true and false elements |
| UNVERIFIED | orange | 4 | Cannot confirm or deny |
| MISLEADING | red-orange | 7 | True elements arranged to mislead |
| FALSE | dark red | 10 | Contradicted by reliable evidence |

```
MFS = (CFS × 0.50) + (MTS × 0.30) + (SCD × 0.20)        # 0–100
CFS = (Σ VP across claims) / (claims × 10) × 100
MTS = min(100, flag_points / expected_max × 100)  [Serious=8, Moderate=4, Minor=1]
SCD = (penalty_points / claims × 10) × 100  [T1-2=0, T3-4=1, T5-6=3, T7=6, T8=10]
```
Interpretation: 0–10 Reliable · 11–25 Mostly Reliable · 26–45 Caution ·
46–65 Problematic · 66–85 Highly Misleading · 86–100 Disinformation.
Always show the CFS/MTS/SCD breakdown so the reader sees *where* the problem is.

### Step 7 — Confidence calibration
State High / Medium / Low with reasons. Increasing: independent agreement,
official data, peer review, expert consensus. Decreasing: geographic/source
concentration, no peer-reviewed studies, claim recency, conflicting evidence,
few sources address it.

### Step 8 — Chain of reasoning (non-obvious verdicts)
What we searched → what we found (for/against) → how conflicting evidence was
weighed → why this verdict → one-line conclusion.

### Step 9 — Counterfactual (for MISLEADING / UNVERIFIED / FALSE)
"If this were true we would expect: [evidence/records/institutional responses
that should exist]. [None exist / only partial / evidence points the other way]."

### Step 10 — Educational component (teach the user to fish)
Per detected red flag, a mini-lesson: technique name+code · what happened here
(quote) · how to spot it in the wild · the cognitive bias it exploits · one
defense habit. Plus: lateral-reading method (STOP → leave the page → check what
independent sources say → find better coverage); the 5 source-credibility
questions; a known-narrative alert *only* for documented recurring patterns; one
memorable prebunking "vaccine" per technique; domain guidance for health
(PubMed/Cochrane/WHO; "reporting ≠ causation"; consensus vs. "a study found") and
political/geopolitical claims (primary legislative sources; state-media ID;
news vs. editorial). Reference: [educational-tips.md](educational-tips.md).

### Step 11 — Output generation
Mode 1 → self-contained HTML card. Mode 4 → inline text. Always include a
copy-ready share-safe summary and the disclaimer.

## HTML fact-check card (Mode 1)
Build it from the section list and design rules in [html-card.md](html-card.md).

## Mode 2 — Comparison
Decompose both sources independently → cross-reference (agreed facts,
contradictions, exclusive claims) → investigate contradictions (which source is
more reliable) → comparison card: side-by-side claims, agreement matrix,
per-source credibility, overall assessment with reasoning.

## Mode 3 — Prebunking briefing
Pipeline: Search → Document → Educate → Output. Find 3–7 active false narratives
on the topic (web search, fact-check explorers, recent debunks). Per narrative:
core false claim, techniques (red-flag codes), spread level, counter-evidence
(tiered). Deduplicate techniques, then educational section (≤5 strongest). No
MFS (no single artifact to score).

## Mode 4 — Quick Check
Steps 1, 2, 6, 7 only. Output text: verdict badge + confidence · 1–2 sentence
explanation · brief confidence factors · 2–3 tiered sources · one educational
tip · share-safe summary · one-line disclaimer. No MFS. Upgrade to Mode 1 if the
user asks for a card or the claim turns out complex.

## Guidelines

**Epistemic honesty:** "Unverified" is a valid verdict. Never manufacture
confidence. Distinguish "no evidence found" from "evidence contradicts." Be
transparent about paywalls, recency, language barriers. Note when science is
still forming. Don't dismiss a claim solely for being non-mainstream, but flag
when it contradicts strong scientific consensus.

**Bias awareness:** search multiple sides of contested issues; don't let the
source's framing bias your queries; flag your own limitations as an AI.

**Health claims:** adverse-event databases (VAERS/EudraVigilance) = reporting,
NOT causation — always clarify. Prefer Cochrane/PubMed systematic evidence.
peer-reviewed > preprint > blog. Put a prominent safety notice on claims that
could lead to refusing treatment, self-medicating, or delaying care.

**Blocked/paywalled sources:** never silently skip — note it, try cached
versions / secondary reporting / search snippets, mark "Access: blocked —
evaluated via snippet/secondary", and lower confidence slightly if a key
Tier 1–2 source is inaccessible with no alternative.

**This skill cannot:** verify deepfakes with certainty (flag indicators;
recommend reverse image search, TinEye, InVID, FotoForensics); read paywalled
papers (use abstracts/secondary); measure live virality; give medical/legal/
financial advice; replace human fact-checkers for high-stakes calls; guarantee
100% accuracy — it is a starting point, not a final authority.

**No web tools available:** use training-data knowledge, state
"based on knowledge through [cutoff], not live-verified", lower confidence one
level, and turn Step 3 into a "here's what you should search yourself" teaching
moment. Steps 5 and 10 work fully offline.

Disclaimer to include in every output: *"AI-assisted analysis, not a definitive
fact-check. For critical decisions consult professional fact-checkers and
primary sources. Verify key findings independently."*
