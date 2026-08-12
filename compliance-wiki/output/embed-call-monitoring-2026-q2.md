---
title: "Embed Call Monitoring Review — Q2 2026"
created: 2026-08-12
updated: 2026-08-12
type: output
tags:
  - compliance/conduct
  - compliance/insurance-distribution
  - compliance/product-governance
  - compliance/data-protection
  - process/audit
  - regulation/idd
  - regulation/fca
status: draft
---

# Embed Call Monitoring Review — Q2 2026

**Document owner:** Compliance Team, [[Kota]]
**Reviewer:** Sola Olaniyan
**Date of review:** 12 August 2026
**Period covered:** June 2026 (Q2 2026)
**Source:** Google Drive — `Monitoring and Testing / Embed Call Monitoring` ([folder](https://drive.google.com/drive/folders/1pjUqYY0wZvdpe2dXT5hNH7m43JfZEmHL))
**Population:** 5 recordings
**Reviewed:** 1 of 5 (see [Coverage](#coverage-and-limitation))
**Classification:** Internal — Confidential

> [!warning] Coverage limitation
> Only 1 of the 5 recordings in the folder could be reviewed. The other 4 exist as audio only, with no transcript available to Compliance and no way to retrieve the audio through the tooling available (see [Coverage](#coverage-and-limitation)). This is itself a control gap — recorded as **Finding G1**.

---

## Coverage and Limitation

| # | Recording | Date of call | Kota attendee(s) | Counterparty | Status |
|---|-----------|--------------|------------------|--------------|--------|
| 1 | Kota X Smart \| Pilot Cohort & Success Criteria | 10/06/2026 | John Higgins | Smart Pension | **Reviewed** |
| 2 | Kota X Smart Pension — Contractual Terms | 15/06/2026 | John Higgins (assumed) | Smart Pension | Not reviewed — no transcript |
| 3 | John / Rachna — Regroup | 11/06/2026 | John Higgins | Rachna (unidentified) | Not reviewed — no transcript |
| 4 | Kota x Justworks — Weekly Touchpoint | 17/06/2026 | John Higgins (assumed) | Justworks | Not reviewed — no transcript |
| 5 | Kota — Follow-up Technical Session | 17/06/2026 | John Higgins (assumed) | Smart Pension (assumed) | Not reviewed — no transcript |

**Why 4 of 5 could not be reviewed.** Recording 1 was uploaded to Fireflies by the meeting owner and is therefore transcribed and searchable. Recordings 2–5 exist only as `.mp3` files in Drive owned by `john@kota.io`. They are not in Fireflies (searched by title, participant, organiser and content across June–August 2026 — no match), no Google Meet transcript or Gemini notes were generated, and the files are 29–55 MB, above the 10 MB ceiling on Drive content retrieval, so the audio cannot be pulled for transcription either.

Attendee and counterparty details for recordings 2–5 are inferred from the filenames and are marked "assumed" — they have not been verified.

---

## Rating Key

| Rating | Definition |
|--------|-----------|
| **C** | Compliant — no issue identified |
| **PC** | Partially Compliant — gap identified, remediation needed |
| **NC** | Non-Compliant — requirement not met |
| **N/A** | Not applicable to this call |

Priority and Impact are rated **High / Medium / Low**, consistent with the `Call Monitoring 2026` register.

---

## Call 1 — Kota X Smart | Pilot Cohort & Success Criteria

| Field | Detail |
|-------|--------|
| **Date of call** | 10 June 2026, 09:00 UTC |
| **Duration** | 32 minutes |
| **Kota attendee** | John Higgins |
| **Counterparty** | Smart Pension — Rosie Crowley, James Briginshaw, Nikki Moss |
| **Call type** | Embed partner — commercial / pilot design |
| **Consumer present** | No |
| **Recording consent requested** | **No** |
| **Recording** | [Fireflies transcript](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA) (privacy: owner-only) |
| **Overall rating** | **PC** |

### Purpose

Defining the cohort of Smart Pension employers for the initial 12-month Embed pilot, and the commercial success criteria that trigger continuation into years two and three. Insurance would be presented to, and taken out by, employers within Smart Pension's master trust book — described on the call as "insured through Smart, AKA Kota, embedded within Smart" ([04:39](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=279)).

### Scoping note — which conduct regime applies

Smart Pension is a UK master trust, the figures discussed were sterling, and the cohort is UK employers. The pilot therefore sits primarily in the **UK** perimeter (FCA — ICOBS, PROD, Consumer Duty, and Kota's appointed representative permissions), not only the Irish CBI/IDD framework. Findings below cite both; the UK analysis should be treated as the operative one and confirmed with Legal. Regulatory references marked *(confirm)* need to be checked against the source instrument before they are relied on externally.

### What was done well

- Professional, straightforward tone throughout; no pressure tactics.
- **No advice or product recommendation given** — no [[Minimum Competency Code]] exposure on this call. This is a marked contrast with the Q1 2026 findings against sales calls.
- Modelling assumptions were explicitly labelled as assumptions rather than presented as fact — "I'll list all the assumptions out" ([21:34](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=1294)).
- The pilot was framed as a reversible experiment with an explicit review gate rather than an open-ended commitment.
- Selection bias was actively resisted when designing the cohort — Smart declined to cherry-pick on data quality "because... one of the learnings we want to have is actually like, can this work?" ([13:15](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=795)). Good testing discipline.

### Findings

#### F1 — No consent requested before recording | Data Protection | PC
**Priority: Medium · Impact: Medium**

The call opens directly with greetings; consent to record is never requested, and the recording was subsequently processed by a third-party AI transcription provider (Fireflies) without any notice to the three external participants on the call.

- **Reference:** GDPR Art.6 (lawful basis), Art.13 (information at collection); [[Data Retention]] for retention of the resulting records.
- **Why it is escalating:** this is the **third consecutive quarter** the same issue has been raised. It was logged in the Q1 2026 register twice — 23/01/2026 ("No request to record the call. This will inhibit our ability to implement our AI processes involving customer biometric data") and 30/04/2026. Q1 rated it Low/Low; the repeat, plus the AI-processing dimension, justifies Medium/Medium now.
- **Note:** the register's Q1 summary already records "Improvements in asking for consent to record the call" as a positive for customer-facing calls. The gap is specifically on **partner-facing** calls, which sit outside the sales script.

#### F2 — Volume-linked revenue share agreed in principle with no conflicts assessment | Conduct / Insurance Distribution | PC
**Priority: High · Impact: Medium**

The commercial structure discussed is a commission share that **increases as insurance sales volume increases**: "your commission is 15 and then we get 50 of that" ([09:32](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=572)), rising on a sliding scale — "by year two... you hit certain volumes, it goes to 60 rev share to you guys, [70] the next one" ([24:11](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=1451); the transcript renders this as "770", read as 70%).

A distribution arrangement that pays the introducing partner a **higher** share the more insurance is sold is precisely the arrangement type that requires a documented conflicts-of-interest and remuneration assessment before it is contracted. Compliance holds no such assessment.

- **Reference:** IDD Art.17(3) — remuneration arrangements must not conflict with the duty to act in the customer's best interests; IDD Art.24 — conflicts of interest management; Commission Delegated Regulation (EU) 2017/2358, Art.8 and Art.10 — distribution channels and distribution arrangements; FCA ICOBS 2.3 (inducements) and SYSC 10 *(confirm)*. See [[Insurance Distribution]], [[Product Governance]].
- **Timing:** the contract has not been executed. This is fixable pre-signature and should be a condition of signature.

#### F3 — Target market absent from cohort design | Product Governance | PC
**Priority: High · Impact: Medium**

The cohort was defined entirely on commercial and operational grounds — employer size bands (5–150, then 25–150 employees), back book versus net new, data quality, and conversion modelling. The manufacturer's **target market** for the products to be distributed was never referenced. The discussion concluded with distribution opened to all new business irrespective of size: "anyone coming in new can access this. So I don't really care about your company size. Let's just offer it across the board" ([15:34](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=934)).

As distributor, Kota must obtain the manufacturer's target market and operate distribution arrangements that deliver the product to it — a cohort defined by commercial upside alone does not evidence that.

- **Reference:** S.I. No. 229/2018, Reg.38(6)–(8) — distributor obligations; IDD Art.25(3)–(4); Commission Delegated Regulation (EU) 2017/2358, Art.10; FCA PROD 4.3 (distributor responsibilities) *(confirm)*. See [[Product Governance]].
- **Context:** EIOPA's 2023 POG peer review found target market definitions across the market were too broad to give distributors meaningful guidance, and that distributor feedback loops were weak — see [[EIOPA Peer Review on Product Oversight and Governance — 2023]]. POG supervision extends to all insurance products from 2026.

#### F4 — Change in data-sharing scope relied on second-hand privacy clearance | Data Protection | PC
**Priority: High · Impact: High**

The scope of member data available to the pilot was reported as having been widened by a privacy decision taken on a call Compliance was not party to: "you weren't kind of on the calls with Joanne in terms of privacy. They've confirmed that we can actually, based on kind of where they got to with the data sharing, we can include whoever we want. Now we're not tied to kind of new business or current back book" ([07:44](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=464)).

The population in scope is material — Smart's book was described as 2 million members of whom roughly 400,000 are active lives ([22:39](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=1359)), with the modelled pilot cohort at ~156,000 active lives. Presenting insurance to an existing pension back book is direct marketing to data subjects who joined for a different purpose.

Compliance holds no record of the clearance referred to, no data sharing agreement for the pilot, no DPIA, and no confirmed lawful basis or transparency position for back-book marketing.

- **Reference:** GDPR Art.6 (lawful basis), Art.13–14 (transparency, including indirect collection), Art.28/26 (processor/joint controller arrangements), Art.35 (DPIA — large-scale processing); UK PECR Reg.22 for electronic marketing to the UK book, S.I. No. 336/2011 Reg.13 in Ireland *(confirm which applies per channel)*.

#### F5 — Smart Pension's regulatory permissions not addressed | Insurance Distribution | PC
**Priority: High · Impact: High**

The arrangement places insurance in front of employers inside Smart Pension's platform, with Smart remunerated by a volume-linked share of Kota's commission. Whether that makes Smart an **introducer** or an **insurance distributor in its own right** — and therefore whether it needs FCA authorisation or appointed representative status — was not raised on the call. The volume-linked remuneration in **F2** cuts against a pure unremunerated-introducer analysis.

- **Reference:** IDD Art.2(1)(1) (definition of insurance distribution) and Art.3 (registration); FCA PERG 5 (insurance distribution activities perimeter) and ICOBS *(confirm)*; S.I. No. 229/2018 registration requirements for Irish-perimeter activity *(confirm exact regulation)*.
- **Action:** legal determination required before the pilot goes live, not before it scales.

#### F6 — Success criteria are sales-volume only | Conduct | PC
**Priority: Medium · Impact: Medium**

The contractual success criteria are gross written premium and attachment rate, with an explicit walk-away trigger: "if we haven't hit that, then it's like, that's complete grounds. Walk away here" ([30:05](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=1805)). No customer-outcome measure — claims experience, complaints, lapse or cancellation rates, evidence that cover suited the employers who bought it — forms any part of the criteria.

A partnership whose only continuation test is premium volume creates conduct pressure in both directions and gives the POG review obligation nothing to feed on.

- **Reference:** CPC 2025 Standards for Business — Core Standard, securing customers' interests; CBI Guidance on Securing Customers' Interests; FCA Consumer Duty PRIN 2A.2 and the outcomes monitoring obligation *(confirm)*; Delegated Regulation (EU) 2017/2358 Art.7 and Art.10 (monitoring and review).

#### F7 — NDA coverage for commercially sensitive exchange not confirmed on call | Governance | C (observation)
**Priority: Low · Impact: Low**

Both sides exchanged confidential commercial data — Smart's book economics and its £4m by 2030 cross-sell revenue target ([11:08](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=668)), Kota's commission rate and conversion assumptions. No issue is alleged; the action is simply to confirm the executed NDA covers the pilot workstream. Rated C on the basis that an NDA is likely already in place given the parallel contractual-terms workstream.

#### F8 — Key-person dependency over the handover period | Governance | C (observation)
**Priority: Low · Impact: Low**

Kota's lead was going on two weeks' paternity leave with a handover to Luke prepared the previous day ([03:00](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=180), [05:32](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=332)). Not a compliance issue. Noted only because the regulatory pre-conditions in F2–F5 must appear on the handover alongside the commercial actions, or they will not survive the gap.

### Category summary — Call 1

| Category | C | PC | NC | N/A |
|----------|---|----|----|-----|
| Consumer Protection / Conduct | – | 2 (F2, F6) | – | – |
| Minimum Competency Code | 1 | – | – | – |
| Product Governance | – | 1 (F3) | – | – |
| Data Protection | – | 2 (F1, F4) | – | – |
| Insurance Distribution / Perimeter | – | 1 (F5) | – | – |
| Governance | 2 (F7, F8) | – | – | – |
| **Total** | **3** | **6** | **0** | **0** |

**Overall rating: PC.** No consumer detriment occurred and no advice was given. The findings are pre-contractual design gaps: the commercial shape of the pilot was settled on this call while the conduct, product governance, data protection and perimeter questions it raises were not.

---

## Programme-Level Finding

#### G1 — Compliance cannot reach 80% of the Embed call population | Governance / Monitoring | NC
**Priority: High · Impact: High**

Four of the five recordings in the monitoring folder cannot be reviewed. The cause is structural, not incidental: recordings of Embed partner calls are saved as raw audio to Drive under the meeting owner's account, and only reach Fireflies if that person uploads them individually. Where they do reach Fireflies, transcript privacy defaults to owner-only.

Call monitoring that can only sample the fifth of the population that happens to have been uploaded is not an effective control, and the sample is self-selected by the person being monitored.

**Recommended remediation:**
1. Put the notetaker on **all** Embed partner calls automatically via the calendar integration, rather than relying on manual upload.
2. Set transcript privacy for partner calls to a level that gives Compliance standing access, or add Compliance to a dedicated Fireflies channel for Embed calls.
3. Where audio-only recordings are retained in Drive, store them in a location Compliance can retrieve, and note that files above 10 MB cannot be pulled programmatically.
4. Retrospectively obtain transcripts for recordings 2–5 and complete this review.

---

## Register Rows — paste into `Call Monitoring 2026`

Columns follow the existing register. `Date of Compliance review` = 12/08/2026 for all rows.

| Date of Compliance review | Date of call | Kota Attendees | Client/Prospect | Call purpose | Recording Consent | Issues | Training Opportunity/Gap | Actions | Responses from management | FactFind done and sent to client | SOS done and sent to client |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 12/08/2026 | 10/06/2026 | John Higgins | Smart Pension (Embed) | Pilot cohort & commercial success criteria | No | 1. No consent requested before recording; recording processed by third-party AI (Fireflies) with no notice to external participants — third consecutive quarter. 2. Volume-linked sliding-scale rev share (50%→60%→70%) agreed in principle with no conflicts-of-interest or remuneration assessment. 3. Pilot cohort defined on commercial grounds only — manufacturer's target market never referenced; distribution then opened to all new business regardless of size. 4. Widened member data-sharing scope relied on a second-hand privacy clearance; no DSA, DPIA or confirmed lawful basis for marketing to a ~156k active-life pension back book. 5. Smart Pension's own regulatory permissions (introducer vs distributor; FCA authorisation / AR status) not addressed. 6. Success criteria are GWP/attachment only, with a walk-away trigger and no customer-outcome measure. No advice given — no MCC issue. | Pre-contract compliance checklist for partner-facing commercial calls: consent to record, target market, remuneration & conflicts, data sharing, partner permissions | Conditions of contract signature: conflicts/remuneration assessment; target market documented for pilot cohort; DSA + DPIA + lawful basis confirmed; legal determination of Smart's perimeter status; customer-outcome metrics added to success criteria. Escalate to HOB & GM. | | N/A | N/A |
| 12/08/2026 | 15/06/2026 | Not verified | Smart Pension (Embed) | Contractual terms | Unknown | Not reviewed — audio only, no transcript available to Compliance | | Obtain transcript and complete review; see G1 | | | |
| 12/08/2026 | 11/06/2026 | John Higgins | Rachna (not identified) | Regroup | Unknown | Not reviewed — audio only, no transcript available to Compliance | | Obtain transcript and complete review; see G1 | | | |
| 12/08/2026 | 17/06/2026 | Not verified | Justworks (Embed) | Weekly touchpoint | Unknown | Not reviewed — audio only, no transcript available to Compliance | | Obtain transcript and complete review; see G1 | | | |
| 12/08/2026 | 17/06/2026 | Not verified | Smart Pension (Embed), assumed | Follow-up technical session | Unknown | Not reviewed — audio only, no transcript available to Compliance | | Obtain transcript and complete review; see G1 | | | |

### Areas for improvement — Q2 2026 summary block

| Areas for improvement | Priority | Impact | Category | Commentary |
|---|---|---|---|---|
| No consent requested before recording partner calls | Medium | Medium | Data Protection | Repeat of a Q1 finding, now compounded by third-party AI processing of the recording. Sales-call consent has improved; partner calls sit outside the script and have not. |
| Volume-linked partner remuneration not assessed for conflicts | High | Medium | Insurance Distribution | Sliding-scale rev share rising with sales volume. Fixable pre-signature; make it a condition of signature. |
| Target market not applied when defining a distribution cohort | High | Medium | Product Governance | Cohort defined on commercial grounds; distribution then opened across the board. |
| Data sharing scope widened on second-hand privacy clearance | High | High | Data Protection | ~156k active lives in scope. No DSA, DPIA or documented lawful basis held by Compliance. |
| Partner's own regulatory permissions not determined | High | High | Insurance Distribution | Introducer vs distributor question unresolved before pilot launch. |
| Pilot success criteria carry no customer-outcome measure | Medium | Medium | Consumer Protection Code | Premium volume as sole continuation test; nothing for the POG review obligation to feed on. |
| Compliance cannot access 4 of 5 recordings in the monitoring population | High | High | Governance / Monitoring | Structural — manual upload and owner-only transcript privacy. Sample is self-selected by the person monitored. |

---

## Actions

| # | Action | Owner | Due | Links to |
|---|--------|-------|-----|----------|
| A1 | Add consent-to-record and AI-notetaker notice to the opening of all partner-facing call scripts | Compliance + GTM | Before next Embed partner call | F1 |
| A2 | Complete conflicts-of-interest and remuneration assessment on the sliding-scale revenue share; make it a condition of contract signature | Compliance, with John Higgins / Luke | Before signature | F2 |
| A3 | Obtain and document the manufacturer's target market for each product in the pilot, and the distribution arrangements that deliver to it | Compliance + Benefits | Before pilot launch | F3 |
| A4 | Obtain written confirmation of the privacy clearance referenced on the call; execute a data sharing agreement; complete a DPIA; confirm lawful basis and transparency position for back-book marketing | Compliance / DPO | Before any member data flows | F4 |
| A5 | Legal determination of Smart Pension's status — introducer vs insurance distributor — and any FCA authorisation or AR requirement | Compliance + external counsel | Before pilot launch | F5 |
| A6 | Add customer-outcome metrics to the pilot success criteria alongside GWP and attachment rate | Compliance, with John Higgins / Luke | Before signature | F6 |
| A7 | Confirm the executed NDA covers the pilot workstream | Compliance | Q3 2026 | F7 |
| A8 | Ensure A2–A5 appear on the handover to Luke, not only the commercial actions | John Higgins | Immediate | F8 |
| A9 | Automate notetaker coverage of all Embed partner calls and give Compliance standing transcript access; retrospectively obtain transcripts for recordings 2–5 | Compliance + Ops | Q3 2026 | G1 |

---

## Cross-References

- [[Insurance Distribution]] — intermediary disclosure, remuneration and conflicts framework
- [[Product Governance]] — distributor obligations, target market, monitoring and review
- [[Data Retention]] — retention of call recordings and transcripts
- [[Kota]] — regulatory status and permissions
- `output/embed-hub-sampling-review-template.md` — the parallel Embed hub review, Q1 2026

---

## Sign-Off

| Role | Name | Date |
|------|------|------|
| Reviewer | Sola Olaniyan | 12/08/2026 |
| Head of Compliance | | |
