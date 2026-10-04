> **⚠ FULLY SUPERSEDED (both tools) by [`spec-notice-pack-builder.md`](spec-notice-pack-builder.md) v3.0**
> — which unifies the Notice Pack, the seam-closing minimal DSAR, the shared infra, and the P1 planning
> reviews. This file is kept for history only. **Build against v3.0.**

# Spec, Privacy Notice Generator + Data Rights Form (DSAR)

**Product:** SaralPrivacy · **Status:** In build (Tool Rail cards 3 & 4)
**Author:** Dilip Sahu · **Date:** 2026-06-20 · **Version:** 0.1 (draft for review)

> These are the two **bridge products** that move SaralPrivacy from advice (Tier 2B)
> to embedded utility, without crossing into runtime CMP/automation (Tier 2A). They
> share one capture/identity/infra layer, so they are specced together.

---

## 0. Shared frame

**Where they sit:** after a user runs Assessment + Discovery and sees their gaps,
these are the first two **artefacts** they can actually produce. Notice Generator
closes the "you have no privacy notice" gap (DPDPA §5). DSAR closes the "you have no
way to receive rights requests" gap (DPDPA §§11-14).

**Strategic guardrails (locked):**
- Ship **English + Hindi first.** Do not block release on all 7 languages.
- **Do not claim automation.** These generate documents and receive requests; they
  do not run live consent or scan systems.
- **Email is the wedge.** Detailed PDF + the hosted DSAR page are the capture points.
  The live preview is ungated; the download/publish is gated. Feeds the OMTM:
  *qualified SMB emails captured per week.*
- Plain English, India-first, no fear theatre. Brand voice non-negotiable.

**One shared infra layer** (build once, both tools use it): email capture + verify,
business profile (`business-slug`), PDF/HTML render service, event log. See §7.

---

# TOOL A, Privacy Notice Generator

> **⚠ Superseded:** Tool A has been expanded into the **Notice Pack Builder** — see
> [`spec-notice-pack-builder.md`](spec-notice-pack-builder.md). The sections below are the
> original lean v0.1 and are kept for history. Build against the Notice Pack spec.

## A1. Problem Statement
Most Indian SMBs have no DPDPA-compliant privacy notice, or have copied a generic US/EU
template that doesn't match what they actually collect. DPDPA §5 requires a notice that
accompanies/precedes consent and states the data collected, the purpose, how to exercise
rights, and how to complain to the Data Protection Board. Writing one feels like a legal
task they can't start, so they don't. The cost: a visible compliance gap that surfaces in
the first enterprise buyer questionnaire or customer complaint.

## A2. Goals
1. A non-legal owner produces a **publishable, §5-aligned notice in under 8 minutes.**
2. **≥ 40% of users who start the wizard reach the preview** (core value moment).
3. **≥ 25% of preview-viewers submit email** to download/publish (wedge conversion).
4. Notice is **specific to what the business selected**, not a fill-in-the-blank template.
5. Output is usable in **3 formats**: live HTML block, copy-paste HTML, downloadable PDF.

## A3. Non-Goals
- **Not** legal certification or sign-off. Output carries an "educational, not legal advice" line.
- **Not** auto-publishing to the user's website (no CMS integration in v1, copy block only).
- **Not** all 7 languages at launch (English + Hindi only; rest are P2).
- **Not** a consent banner / CMP. The notice references how consent is obtained; it doesn't run it.
- **Not** multi-notice management / versioning dashboard (that's a Pro feature, P2).

## A4. User Stories
- As a **clinic/agency owner**, I want to answer plain questions about what data I collect so that
  I get a notice worded for *my* business, not a lawyer's template.
- As an **owner**, I want to preview the full notice before giving my email so that I trust it's real before I commit.
- As an **owner**, I want a copy-paste HTML block so that I can put the notice on my website myself.
- As an **owner**, I want a branded PDF so that I can attach it to proposals and intake forms.
- As a **Hindi-first owner**, I want the notice in Hindi so that my customers actually understand it.
- As an **owner who processes children's data**, I want the notice to include the parental-consent
  language so that I don't miss a high-risk obligation.

## A5. The wizard (8 questions)
Single screen per step, progress bar, "back" preserves answers. All inputs map to §5 elements.

| # | Question | Input type | Maps to |
|---|----------|-----------|---------|
| 1 | Business name, sector, website | text + sector select | Header, fiduciary identity |
| 2 | What personal data do you collect? | multi-select (name, contact, email, phone, address, payment refs, ID docs, health, biometric, location, children's data, other) | §5 "data collected" |
| 3 | Why do you collect it? | multi-select purposes mapped from #2 (service delivery, payments, support, marketing, legal/compliance, recruitment) | §5 "purpose" |
| 4 | Who do you share it with? | multi-select (payment gateway, cloud/hosting, WhatsApp/comms, analytics, recruiters, none) | Disclosure / vendor line |
| 5 | How long do you keep it? | per-category select (until service ends, X months/years, legal minimum, indefinite→flag) | Retention statement |
| 6 | Do you process children's data (under 18)? | yes/no → if yes, parental-consent block | §9 children's data |
| 7 | Grievance contact (name, email, phone) | text | §5 rights mechanism + §13 grievance |
| 8 | Languages needed | English / Hindi (multi) | Output rendering |

→ On finish: **live preview renders immediately (ungated).** Download PDF / copy HTML / publish = email gate.

## A6. Requirements

**Must-Have (P0)**
- 8-step wizard with state preserved across back/forward.
- Deterministic notice template that assembles §5 sections from answers (no LLM dependency required for v1, rules-based assembly so output is predictable and defensible).
- Live HTML preview, ungated.
- Email-gated: copy-as-HTML block + PDF download.
- English output. "Educational, not legal advice" footer + last-generated date.
- Children's-data conditional block (Q6 = yes).
- Mobile-responsive wizard.

*Acceptance:*
- Given a user completes all 8 steps, when they reach the end, then the full notice renders on screen without requiring an email.
- Given a user clicks Download PDF, when they have not submitted email, then the email gate appears; on submit, the PDF downloads and the email is logged with `source=notice-generator`.
- Given Q2 includes "children's data", when the notice renders, then the parental-consent paragraph is present.
- Given Q5 = "indefinite" for any category, when the notice renders, then a soft inline flag suggests setting a retention period.

**Nice-to-Have (P1)**
- Hindi output (toggle on preview).
- "Review my notice" CTA → routes to Advisory lead.
- Save & resume via emailed link.
- Sector-tuned default copy (recruitment / CA / clinic / D2C).

**Future (P2)**
- Remaining 5 languages.
- Saved notices + re-generate on change (Pro dashboard).
- One-line website embed (`<script>`) that always serves the latest notice.

---

# TOOL B, Data Rights Form (DSAR)

## B1. Problem Statement
DPDPA gives every data principal the right to access, correct, erase, and raise grievances
about their data (§§11-14), and businesses must provide a **readily available means** to
exercise them. Most SMBs have no intake channel at all, requests arrive as ad-hoc emails or
WhatsApp messages, get lost, and miss response timelines. The cost: an unanswered rights
request is the cleanest possible complaint to the Data Protection Board.

## B2. Goals
1. Any SMB gets a **working public rights-intake page in under 5 minutes** (`saralprivacy.com/r/[slug]`).
2. **100% of submitted requests produce a tracked record** (Request ID, type, timestamp, status).
3. Business owner is **notified within 1 minute** of a new request.
4. **≥ 30% of businesses that create a page** return to view/manage requests (stickiness).
5. Owner can **export the full request log as CSV** for evidence.

## B3. Non-Goals
- **Not** automated fulfilment. The tool *receives, routes, and tracks*, the human still acts.
- **Not** deep identity verification (KYC) in v1, lightweight email confirmation only.
- **Not** a full ticketing/SLA-automation suite (status is manual in v1).
- **Not** embedded widget in v1 (hosted page first; one-line embed is P2).
- **Not** data discovery/lookup, it does not fetch the requester's data from the business's systems.

## B4. User Stories
- As an **owner**, I want a ready-made public page where people can file data requests so that I have a compliant intake channel without building one.
- As a **data principal** (customer/candidate), I want to submit a request and pick its type so that the business knows exactly what I'm asking for.
- As a **data principal**, I want a Request ID and confirmation so that I have proof I asked.
- As an **owner**, I want an email the moment a request lands so that I don't miss the response window.
- As an **owner**, I want to mark a request received → in progress → closed so that I can track what's open.
- As an **owner**, I want to export all requests as CSV so that I have audit evidence.

## B5. The flow
**Setup (owner):** claim a `business-slug`, set business name + grievance contact + which request
types you accept → page goes live at `saralprivacy.com/r/[slug]`.

**Intake (data principal):** open page → choose request type → enter name + email + details →
lightweight email confirmation → receives Request ID + timestamp.

**Manage (owner):** email notification → list view of requests → status update → CSV export.

**Request types (DPDPA-mapped):**
| Type | DPDPA basis |
|------|-------------|
| Access my data | §11 right to access |
| Correct / update my data | §12 correction & completion |
| Erase my data | §12 erasure |
| Withdraw consent | §6(4)-(6) |
| Raise a grievance | §13 grievance redressal |
| Nominate someone | §14 right to nominate |

## B6. Requirements

**Must-Have (P0)**
- Owner setup → hosted page at `saralprivacy.com/r/[slug]` (unique slug, validated).
- Public intake form: request type, name, email, free-text detail, consent checkbox.
- Lightweight email confirmation to requester (confirm-link to reduce spam/false requests).
- Auto-generated Request ID + timestamp on submit.
- Email notification to owner on new request (< 1 min).
- Owner list view (request id, type, status, date) behind email/magic-link auth.
- Manual status: Received → In progress → Closed.
- CSV export of all requests.
- "Educational, not legal advice" + privacy line on the public page.

*Acceptance:*
- Given an owner completes setup, when they save, then `saralprivacy.com/r/[slug]` resolves to a live form with their business name.
- Given a data principal submits a valid request, when they confirm via email, then a record is created with a unique Request ID, type, timestamp, status=Received, and the requester sees the ID.
- Given a new confirmed request, when it is created, then the owner receives an email notification within 1 minute.
- Given an owner opens their dashboard, when they change a request's status, then the new status persists and appears in CSV export.
- Given a slug is already taken, when an owner tries to claim it, then they are blocked with a clear message.

**Nice-to-Have (P1)**
- Response-due indicator per request (countdown vs. configured target window).
- Internal notes per request.
- Hindi version of the public intake page.
- Branding on the public page (logo, color).

**Future (P2)**
- One-line embed for the business's own site.
- Identity verification step (document/OTP) for higher-assurance requests.
- SLA automation + reminders.
- Saved dashboard with vendor/notice tools unified (Pro).

---

# 7. Shared infrastructure (build once)

| Component | Used by | Notes |
|-----------|---------|-------|
| **Email capture + verify** | Both | Single endpoint; hidden `source` field (`notice-generator` / `dsar` / tool name). Magic-link auth for owner dashboards. This *is* the OMTM pipe. |
| **Business profile / slug** | Both | `business-slug` claimed once, reused for DSAR page + notice branding. |
| **Render service** | Notice (PDF/HTML) | Server-side HTML→PDF; templated, deterministic. |
| **Event log / store** | Both | Captures, requests, status changes. Source of the demand signal (which tool gets most interest). |
| **Notification** | DSAR | Transactional email on new request. |

**Stack alignment:** React front end + Node/PostgreSQL (per house architecture). DSAR records
and email captures are PostgreSQL tables; PDF render is a Node service.

---

# 8. Success Metrics

**Leading (days-weeks)**
- Notice: wizard start → preview rate (target ≥ 40%); preview → email rate (target ≥ 25%).
- DSAR: pages created/week; setup completion rate (target ≥ 60% of starts).
- Shared: **qualified SMB emails captured/week** (the OMTM), segmented by `source`.

**Lagging (weeks-months)**
- % of email-capture users who return / convert to Pro.
- DSAR page → returning owner rate (target ≥ 30%).
- Tool-demand ranking (notice vs. DSAR vs. roadmap notify-me clicks) → informs build order for tools 5-7.

**Measurement:** event log + email source tags. Evaluate at 2 weeks and 6 weeks post-launch each.

---

# 9. Open Questions
- **[Legal]** What exact response-window do we *state* on the DSAR page? DPDPA Rules timelines, confirm against final Rules before we display any number. *(blocking for DSAR P1 due-indicator, not for P0.)*
- **[Legal]** Notice template wording sign-off, who reviews the assembled §5 output once before launch? *(blocking for Notice P0 publish.)*
- **[Product]** Does the Notice wizard need login at all in v1, or is email-at-download enough? *(lean = email-only. Recommend no login.)*
- **[Eng]** Rules-based notice assembly vs. LLM-assisted? *(Recommend rules-based v1 for predictability/defensibility; LLM polish is P2.)*
- **[Eng]** Slug squatting / abuse on public DSAR pages, rate-limit + email-verify enough for v1?
- **[Data]** Confirm the single email-capture schema both tools write to, so segmentation works from day one.

---

# 10. Timeline / Phasing
Aligned to the existing roadmap (Notice = Month 2, DSAR = Month 3):

- **Phase 1, Notice Generator (P0):** wizard + rules-based English notice + ungated preview + email-gated PDF/HTML. Ship English first; Hindi as fast-follow (P1).
- **Phase 2, DSAR (P0):** slug setup + hosted intake + Request ID + owner notification + list view + CSV. Hosted page first; embed is P2.
- **Dependency:** shared email-capture + slug + event-log layer (§7) must land in Phase 1 so DSAR reuses it.
- **Gate before either ships:** one legal pass on the notice template and the DSAR page copy (Open Questions, Legal).

---

*Out of scope by house standard: competitive analysis (lives in product-context).
Output calibration: this is a build spec, full detail intended.*
