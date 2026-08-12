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
**Reviewed:** 2 of 5 (see [Coverage](#coverage-and-limitation))
**Classification:** Internal — Confidential

> [!warning] Coverage limitation
> Only 2 of the 5 recordings in the folder could be reviewed. The remaining 3 exist as audio only, with no transcript available to Compliance and no way to retrieve the audio through the tooling available (see [Coverage](#coverage-and-limitation)). This is itself a control gap — recorded as **Finding G1**.

---

## Coverage and Limitation

| # | Recording | Date of call | Kota attendee(s) | Counterparty | Status |
|---|-----------|--------------|------------------|--------------|--------|
| 1 | Kota X Smart \| Pilot Cohort & Success Criteria | 10/06/2026 | John Higgins | Smart Pension | **Reviewed** |
| 2 | Kota X Smart Pension — Contractual Terms | 15/06/2026 | John Higgins (assumed) | Smart Pension | Not reviewed — no transcript |
| 3 | John / Rachna — Regroup | 11/06/2026 | John Higgins | Rivermate / Hightekers (EOR) | **Reviewed** |
| 4 | Kota x Justworks — Weekly Touchpoint | 17/06/2026 | John Higgins (assumed) | Justworks | Not reviewed — no transcript |
| 5 | Kota — Follow-up Technical Session | 17/06/2026 | John Higgins (assumed) | Smart Pension (assumed) | Not reviewed — no transcript |

**Why 3 of 5 could not be reviewed.** Recording 1 was uploaded to Fireflies by the meeting owner and is therefore transcribed and searchable. Recording 3 was reviewed from a transcript supplied directly by the Head of Compliance on 12 August 2026. Recordings 2, 4 and 5 exist only as `.mp3` files in Drive owned by `john@kota.io`. They are not in Fireflies (searched by title, participant, organiser and content across June–August 2026 — no match), no Google Meet transcript or Gemini notes were generated, and the files are 29–55 MB, above the 10 MB ceiling on Drive content retrieval, so the audio cannot be pulled for transcription either.

Attendee and counterparty details for recordings 2, 4 and 5 are inferred from the filenames and are marked "assumed" — they have not been verified.

**Transcript quality caveat — Recording 3.** The supplied transcript is an unedited automated transcription with substantial garbling: entity names appear variously as "high-takers"/"Hitek"/"high-careers" (read as Hightekers), "the meat"/"Rivermay" (read as Rivermate), "survey"/"Surveyor" (an acquired entity), "safe-tillings"/"safety wings" (read as SafetyWings). One long passage is corrupted by a repeated loop. Quotes below are reproduced as transcribed; where a reading is inferred it is marked. Any finding intended for escalation should be confirmed against the audio before it is put to the individual.

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

Kota's lead was going on two weeks' planned leave, with a handover to Luke prepared the previous day ([05:32](https://app.fireflies.ai/view/01KTRC5GZGKXS354TDMMQRA6SA?t=332)). Not a compliance issue, and no comment is made on the leave itself. Noted only because the regulatory pre-conditions in F2–F5 must appear on the handover alongside the commercial actions, or they will not survive the gap.

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

## Call 2 — John / Rachna Regroup

| Field | Detail |
|-------|--------|
| **Date of call** | 11 June 2026 |
| **Kota attendee** | John Higgins |
| **Counterparty** | Rivermate / Hightekers — Rachna (benefits lead) |
| **Call type** | Embed partner — EOR benefits partnership, discovery and commercial |
| **Consumer present** | No — but EOR employees are the ultimate insured lives |
| **Recording consent requested** | **No** |
| **Recording** | Drive mp3; transcript supplied to Compliance 12/08/2026 |
| **Overall rating** | **PC** |

### Purpose

Understanding the counterparty's global benefits strategy following a four-way merger, and positioning Kota as its benefits infrastructure — starting with an EMEA IPMI plan and a referral-fee commercial model. The counterparty currently sources cover market-by-market through local brokers and providers, with SafetyWings used for international plans in APAC.

### What was done well

- **Genuinely good process discovery.** John walked the incumbent process end to end — how a request arrives, how quotes are sourced, who signs off, who enrols, who owns renewals, whether the HR advisors are the counterparty's own staff. That is the right groundwork for a distribution arrangement and it produced a clear picture.
- **Offered an aggregate alternative to employee-level data**, and narrowed the ask when pressed: *"if you can't pull this data, then... just this market data, so like how many employees let's say in Spain"* and later *"it's gender age... where their location, they're the main things"*. Data minimisation instinct is there.
- **Raised an NDA unprompted** — *"we're happy to sign NDA's if need be to do this"*.
- **Did not over-promise on migrating existing insured members** — *"it depends on the plan... it depends on the contract like you'd have to kind of guide us on that"*, and said he would bring the benefits team into the follow-up.
- Identified that anti-selection rules bear on introducing a new plan, which is the right consideration to raise even if it was stated loosely.

### Findings

#### F9 — Legal conclusion asserted about the counterparty's existing practice | Conduct / Competence | PC
**Priority: High · Impact: Medium**

John told the counterparty that a common EOR practice is unlawful, and named the offence: *"they're putting 10, I say 10, 20% on top of the premium and taking that... ultimately that is illegal. I just be direct and honest, it's called price manipulation, because these are insurance products, you're not allowed to do that with insurance products, it's not like a normal consumer product, it's not a re-selling product."*

Whether or not the underlying point is directionally right, a commercial lead should not be delivering a legal conclusion on the lawfulness of a third party's pricing to that third party. It is outside competence, it is unverified, and it is being used as a sales argument against the counterparty's incumbent arrangement.

- **Reference:** CPC 2025 Standards for Business — acting professionally and with competence; [[Minimum Competency Code]] where the statement touches the regulated product; IDD Art.17(1)–(2) — fair, clear and not misleading communication.
- **Action:** the correct position on premium mark-up versus service fees needs to be settled by Compliance/Legal and put into the partner script, so it is stated accurately or not at all.

#### F10 — Fee-stacking model explained without a fair value or disclosure position | Conduct / Product Governance | PC
**Priority: High · Impact: High**

Immediately after calling premium mark-up illegal, John set out the model other partners use and quantified the return: a management fee of *"anywhere between 15 to 25 euro per month... per employee per month"*, producing *"300 euro per annum just by having the benefits"*, **on top of** the €50 per policy per year referral fee out of Kota's own 10–20% commission.

The result is three layers of cost — insurer premium, Kota commission, partner referral fee, plus a partner management fee borne by the employer or employee. The distinction between an unlawful premium mark-up and a lawful service fee turns entirely on whether the fee buys genuine services and is disclosed. Neither point was addressed, and Compliance holds no fair value assessment for this structure.

- **Reference:** S.I. No. 229/2018, Reg.23(1)(h) and IDD Art.19(1)(d)–(e) — remuneration disclosure to the customer; CPC 2025 Part 3 and Part 4; FCA Consumer Duty PRIN 2A.4 (price and value) for UK lives *(confirm)*; Delegated Regulation (EU) 2017/2358 Art.7 and Art.10; value-for-money direction of travel in [[EIOPA Peer Review on Product Oversight and Governance — 2023]] and the [[EU Retail Investment Strategy — Product Governance Changes (Dec 2025)]] "undue costs" concept.
- **Link:** this is the same conflicts-and-remuneration gap as **F2** on Call 1, in a second partnership. See [Repeat and Cross-Call Themes](#repeat-and-cross-call-themes).

#### F11 — Counterparty's regulatory perimeter status not addressed | Insurance Distribution | PC
**Priority: High · Impact: High**

On the model discussed, the counterparty's own HR advisors would present plans, enrol members, add dependants, and cancel policies — *"they're going to send directly to that specific broker or specific provider... we have so many enrollments for this month or we have X, Y, Z who are [lapsed]. So we are going to cancel the policy"* — while the counterparty earns a per-policy referral fee and a per-employee management fee.

That combination of activity and remuneration needs a perimeter determination: is the counterparty an introducer, an ancillary insurance intermediary, or an insurance distributor requiring registration? The ancillary exemption has conditions that were never tested on the call.

- **Reference:** IDD Art.2(1)(1) (insurance distribution), Art.2(1)(4) and Art.1(3) (ancillary insurance intermediary exemption and its conditions), Art.3 (registration); S.I. No. 229/2018 registration requirements *(confirm exact regulation)*; FCA PERG 5 for UK-perimeter activity *(confirm)*.
- **Link:** identical open question to **F5** on Call 1.

#### F12 — Named partner's commercial data disclosed to a prospect | Confidentiality | NC
**Priority: High · Impact: Medium**

John disclosed a named existing partner's plan size and revenue: *"We have like a European international plan for the likes of remote. There's about 10,000 on the plan... you can see how they're booking close to four million in this one plan for the Europe alone."* He also named Deel and Remote and relayed their internal commentary — *"they came to us and said... we wish you found you two years ago"*.

This is client-confidential commercial information given to a third party with no NDA in place — John confirmed on the same call that an NDA had not yet been signed.

- **Reference:** contractual confidentiality obligations to the named partners; CPC 2025 Standards for Business; [[Kota]] internal confidentiality policy.
- **Why NC rather than PC:** the disclosure has already occurred and cannot be remediated by a control change. This is a repeat of a Q1 2026 finding of the same type ("Sharing of confidential client information", 09/03/2026; and the 30/04/2026 Aikido call, where the same three partner relationships were disclosed). Third occurrence in two quarters, now involving revenue figures.

#### F13 — Employee-level personal data requested before an NDA or data processing terms were in place | Data Protection | PC
**Priority: High · Impact: Medium**

The census data requested was identifiable at member level — *"the member reference, the status, date of birth, age, gender, nationality, country of work"* — for the purpose of shopping the risk to carriers (Bupa, Vitality, AXA were named as targets). At the point of the request there was no NDA and no data processing agreement; the counterparty said she would need to check the NDA position with her colleague before providing the second dataset.

John did offer an aggregate fallback and narrowed the fields, which mitigates this. But the sequence should be the other way round: agreement first, aggregate data for indicative quoting, member-level data only once terms are executed.

- **Reference:** GDPR Art.5(1)(c) (minimisation), Art.6 (lawful basis), Art.13–14 (transparency to the affected employees), Art.28 (processor terms), Art.44 et seq. where LatAm or APAC lives are included in scope.
- **Note:** nationality is not an Art.9 special category but is a proxy for racial or ethnic origin, and health-insurance census data can imply health status. Both warrant a higher bar than a pre-NDA email.

#### F14 — Kota described as "the broker" in non-UK markets | Consumer Protection / Regulatory Status | PC
**Priority: Medium · Impact: Medium**

Kota was described as *"one broker, aka tech platform, that is ourselves"* and *"we are the broker"*, in a conversation expressly about Portugal, Spain, France, LatAm and APAC. Regulatory status was asserted only in the vague form *"we are financially regulated"*, without identifying the regulator or the scope of the permission.

- **Reference:** S.I. No. 229/2018, Reg.23(1)(a)–(d) — identify the intermediary and disclose regulatory status accurately; IDD Art.18(a)(i).
- **Why it matters here:** this is a direct repeat of the 09/03/2026 Q1 finding — *"He said we're a broker, but we can only describe ourselves as that in the UK"* — and of the 12/01/2026 finding against a different individual for the same error. The term is still in use, now by the Embed lead.

#### F15 — Product and market facts asserted from memory | Product Knowledge | PC
**Priority: Low · Impact: Low**

Group-size minimums and market rules were stated conversationally — *"markets like Spain, if you don't have five, you're not getting a [local] plan"*, *"I don't think they've got minimums of like three in Portugal"*, *"the UK... they have anti-selection kind of laws"*. Reasonably hedged, and not wrong on their face, but this is the same pattern as the Q1 Cubic finding, where a product was described as available on the platform when it was not.

- **Training gap:** product and market reference material that partner-facing staff can check mid-call, rather than recalling.

#### F16 — Competitor product disparaged without evidence | Conduct | PC
**Priority: Medium · Impact: Low**

The counterparty's incumbent international provider was characterised as poor value: *"we're taking a lot of business from [them] because ultimately the coverage isn't much and it's quite expensive because they're having to do the ultimate aggregator."*

Comparative claims about a named competitor's coverage and price must be fair, accurate and substantiated. No comparison had been run at this point — the census data needed to quote had not yet been provided.

- **Reference:** IDD Art.17(2) — fair, clear and not misleading; CPC 2025 Part 3 (accuracy of information).
- **Link:** same category as the Q1 finding against a colleague for diagnosing an incumbent insurer as a wrong fit early in a call.

#### F17 — No consent requested before recording | Data Protection | PC
**Priority: Medium · Impact: Medium**

As with Call 1, the call opens directly into conversation with no request for consent to record. Same finding as **F1**; not double-counted in the totals below, but it is now evidenced on both reviewed calls.

### Category summary — Call 2

| Category | C | PC | NC | N/A |
|----------|---|----|----|-----|
| Consumer Protection / Conduct | – | 3 (F9, F10, F16) | – | – |
| Product Governance | – | (F10, also counted above) | – | – |
| Data Protection | – | 2 (F13, F17) | – | – |
| Insurance Distribution / Perimeter | – | 2 (F11, F14) | – | – |
| Confidentiality | – | – | 1 (F12) | – |
| Product Knowledge | – | 1 (F15) | – | – |
| **Total (distinct findings)** | **0** | **8** | **1** | **0** |

**Overall rating: PC**, with one NC. No consumer was on the call and no advice was given to a retail customer. The concerns are that a commercial lead ran an unscripted partner call in which he delivered a legal conclusion, coached a fee model with no fair value position behind it, disclosed a named partner's revenue with no NDA in place, requested member-level personal data before terms existed, and used a regulatory descriptor the compliance team has already corrected twice this year.

---

## Repeat and Cross-Call Themes

Both reviewed calls are partner-facing and both sit outside the scripted sales process. The pattern across them, and back into Q1 2026, is consistent.

| Theme | Call 1 | Call 2 | Q1 2026 precedent |
|-------|--------|--------|-------------------|
| No consent requested before recording | F1 | F17 | 23/01/2026; 30/04/2026 |
| Volume-linked partner remuneration, no conflicts or fair value assessment | F2 | F10 | — (new in Q2) |
| Partner's own perimeter status undetermined | F5 | F11 | — (new in Q2) |
| Target market / distribution arrangements not applied | F3 | F10, F11 | — |
| Named client or partner information disclosed | F7 (observation only) | F12 (NC) | 09/03/2026; 30/04/2026 |
| "Broker" used outside the UK; vague regulatory status | — | F14 | 12/01/2026; 09/03/2026 |
| Product or market facts asserted without verification | — | F15 | 23/03/2026 (Cubic / Sanitas) |
| Statements shading into advice or evaluative recommendation | — | F9, F16 | 09/03/2026; 19/03/2026; 29/04/2026 |

**The structural point for the management report.** Q1's remediation was aimed at customer-facing sales calls — a formal script for individuals not MCC-qualified, induction slides on Skillcast, and a rule that one named individual should not take calls alone. Those controls have worked where they were applied: neither reviewed call gave advice to a consumer. The same failure modes have simply reappeared on **partner and commercial calls**, which no script covers, conducted by senior staff who were not the subject of the Q1 remediation. The control needs extending to partner-facing conversations, not tightening further on sales.

---

## Programme-Level Finding

#### G1 — Compliance cannot reach most of the Embed call population | Governance / Monitoring | NC
**Priority: High · Impact: High**

Three of the five recordings in the monitoring folder still cannot be reviewed. The cause is structural, not incidental: recordings of Embed partner calls are saved as raw audio to Drive under the meeting owner's account, and only reach Fireflies if that person uploads them individually. Where they do reach Fireflies, transcript privacy defaults to owner-only. Of the two calls reviewed this quarter, one was reachable only because it had been uploaded, and the other only because a transcript was passed to Compliance by hand.

Call monitoring that depends on individual uploads or manual hand-off is not an effective control, and the reachable sample is self-selected by the people being monitored. Note also that the two calls that could be reviewed produced sixteen distinct findings between them, including one NC — so the unreachable population cannot be assumed to be clean.

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
| 12/08/2026 | 11/06/2026 | John Higgins | Rivermate / Hightekers (Embed, EOR) | Regroup — global benefits partnership, EMEA IPMI plan | No | 1. Told the counterparty its incumbent premium mark-up practice is "illegal... price manipulation" — a legal conclusion outside competence, used as a sales argument. 2. Set out the partner fee-stacking model (€15–25 per employee per month management fee, ~€300 p.a., on top of a €50 per policy referral fee out of Kota's 10–20% commission) with no fair value or customer-disclosure position behind it. 3. Counterparty's own perimeter status not addressed although its HR advisors would enrol members, add dependants and cancel policies for a per-policy fee. 4. **Disclosed a named partner's plan size and revenue ("the likes of Remote... about 10,000 on the plan... close to four million") to a prospect with no NDA in place** — third disclosure finding of this type in two quarters. 5. Requested member-level census data (member reference, DOB, gender, nationality, country of work) before any NDA or data processing terms existed. 6. Described Kota as "the broker" in a conversation about Portugal, Spain, France, LatAm and APAC; regulatory status given only as "we are financially regulated". 7. Characterised the incumbent international provider as poor value and expensive with no comparison yet run. Mitigants: strong process discovery, offered aggregate data alternative, raised NDA unprompted, did not over-promise on migrating existing members. | Partner-call script and pre-contract checklist; confidentiality refresher for partner-facing staff; correct form of words for Kota's regulatory status outside the UK; product/market reference material checkable mid-call | Escalate F12 (confidentiality) to HOB & GM. Settle the premium mark-up vs service fee position in writing before it is stated on any further call. Perimeter determination and fair value assessment before contracting. Confirm whether census data was in fact sent pre-NDA. | | N/A | N/A |
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
| Named partner's commercial data disclosed to a prospect with no NDA | High | Medium | Confidentiality | Third finding of this type in two quarters, now involving a partner's plan size and revenue. Cannot be remediated after the fact — rated NC. |
| Legal conclusions and fee models stated on partner calls without a settled position | High | High | Consumer Protection Code / Minimum Competency Code | Premium mark-up called illegal, then a management-fee model quantified, in the same passage. Needs a written position before it is said again. |
| Member-level personal data requested before NDA or processing terms | High | Medium | Data Protection | DOB, gender, nationality, country of work sought for carrier shopping. Aggregate-first should be the default. |
| "Broker" still used outside the UK; regulatory status stated vaguely | Medium | Medium | Consumer Protection Code | Corrected twice in Q1 against two individuals; recurring in Q2 at Embed lead level. |
| Compliance cannot access 3 of 5 recordings in the monitoring population | High | High | Governance / Monitoring | Structural — manual upload and owner-only transcript privacy. Reachable sample is self-selected by the people monitored, and the two reachable calls produced 15 findings. |
| Q1 remediation covered sales calls only | High | Medium | Governance | Scripts, induction and the two-on-a-call rule were aimed at customer-facing sales. The same failure modes have reappeared on unscripted partner calls run by senior staff. |

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
| A9 | Automate notetaker coverage of all Embed partner calls and give Compliance standing transcript access; retrospectively obtain transcripts for recordings 2, 4 and 5 | Compliance + Ops | Q3 2026 | G1 |
| A10 | Escalate the confidentiality disclosure to HOB and GM; establish whether the named partners' agreements required notification, and whether the census data was in fact sent before an NDA was executed | Compliance | Immediate | F12, F13 |
| A11 | Settle in writing the position on premium mark-up versus partner service fees, with the fair value and customer-disclosure analysis, and put it in the partner script | Compliance + Legal | Before next partner commercial call | F9, F10 |
| A12 | Perimeter determination for the EOR partner — introducer, ancillary insurance intermediary, or distributor requiring registration | Compliance + external counsel | Before contracting | F11 |
| A13 | Issue the approved form of words for Kota's regulatory status and permitted self-description by market; add to induction and the partner script | Compliance | Q3 2026 | F14 |
| A14 | Extend the Q1 remediation package — script, checklist, two-on-a-call where appropriate — to partner-facing and commercial calls, including senior staff | Compliance + GTM | Q3 2026 | Cross-call themes |
| A15 | Build a product and market reference sheet (group-size minimums, market availability, anti-selection rules) that partner-facing staff can check mid-call | Benefits + Compliance | Q3 2026 | F15 |

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
