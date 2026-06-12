---
title: Daily Compliance Eval — 2026-06-09
created: 2026-06-12
type: eval
run_type: live-fireflies
date_range: "2026-06-09"
calls_assessed: 14
customer_facing_consumer: 4
calls_flagged: 1
grade_5: 0
grade_4: 0
grade_3: 0
grade_2: 1
grade_1: 13
---

# Daily Compliance Eval — 2026-06-09

## Summary
| Calls assessed | Consumer-facing | Calls flagged | Grade 5 | Grade 4 | Grade 3 | Grade 2 | Grade 1 |
|---|---|---|---|---|---|---|---|
| 14 | 4 | 1 | 0 | 0 | 0 | 1 | 13 |

> Busy day: 14 recordings reviewed (one duplicate skipped). Of these, the majority are **partner/supplier** calls (Deel, Pacific Prime, Unisure, Scaith, Payfit) or **internal-affiliate** calls (Yonder) with **no retail consumer present**, so consumer-facing MCC criteria do not bite — graded 1 and documented. Four calls are genuinely consumer/prospect-facing (365 Finance, LearnUpon #1, Lloyds List Intelligence, Exile). Only one call produced a finding: **LearnUpon #1**, where Simon Ward (script pathway, unqualified) described occupational-pension contribution mechanics during an enrolment-ops call — **HF-10 (light), Grade 2 / Pass-with-comments**. No Grade 3+ breaches, no ES escalations, no HF-03/HF-05 confirmed.

> **Note on Paul O'Hanlon AE statement (365 Finance):** Paul stated the "3.5% between employer and employee, otherwise they fall into a government scheme" rule. Paul is **fully qualified (QFA, all products)**, so HF-10/HF-11/HF-13 do not apply. Against the AE source-of-truth, "3.5% total, employer + employee" matches the **Pensions Authority occupational-scheme exemption standard** (3.5% total gross pay, min 1.5% employer) — which is exactly the rule an employer setting up a scheme to be exempt from AE must meet. Under the R2 charitable-interpretation pass this reading is **correct** (it is an occupational-scheme exemption statement, not an AE-total statement, so the State 0.5% is correctly absent). **No HF-05.** Documented as a watch item only — same ambiguous-framing pattern previously logged for Karl O'Brien (India, 2026-05-08).

---

## Per-Call Results

### Kota / 365 Finance - Employee Benefits Demo & IE — 01KT46MDNSQGDAG0XC7S9VKF14 — 2026-06-09 08:30
**External**: Denise Kendall (365 Finance, IE/UK prospect — consumer-facing)
**Kota speaker(s)**: Paul O'Hanlon — ✅ Fully Qualified (QFA + APA PMI, all products)
**Department**: Benefits / GTM
**Duration**: 18 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KT46MDNSQGDAG0XC7S9VKF14

#### Findings
No hard-rule breaches. Paul is fully qualified for pensions, life and PMI, so his discussion of Irish health-insurance mechanics (BIK calculation, budget/employee-top-up, dependant cover, newborn cover period), life/IP group-minimum-of-10 rule, pension contribution-matching and tax relief at source is **all within scope**.

#### Notes
- Paul correctly declines to answer the newborn-cover question off the cuff (*"first time I've been asked that question, so I don't want to give an answer"*) and commits to confirming — good practice.
- **AE statement** (~16:00): *"the only rule is that there has to be a minimum of like 3.5% going into the pension between employer and employee. Otherwise they fall into a government scheme."* Assessed against source-of-truth: matches the Pensions Authority occupational-scheme exemption standard (3.5% total, min 1.5% employer). **Correct under charitable reading — no HF-05.** Watch item: framing does not state explicitly that this is the occupational-exemption threshold vs AE total.
- *"I was trying to find a way around this, but we can't at the moment"* (re Irish group life requiring 10+ employees) — read in context this is Paul explaining a provider rule he **cannot** circumvent, not circumvention advice. Not SF-10.
- **Escalation**: No.

---

### Kota / LearnUpon #1 — 01KT44Y0K0N61P2K89SA5118HN — 2026-06-09 09:00
**External**: Sophie Peyron, Andrew O'Leary (LearnUpon — existing client, onboarding/enrolment ops)
**Kota speaker(s)**: Simon Ward — ❌ Script pathway (Customer Success, unqualified); John Hayes (john.hayes@kota.io) — unknown speaker, **fail-closed unqualified** (largely silent)
**Department**: CS/CX
**Duration**: 12 min
**Grade**: **2 — Pass with comments**
**Fireflies**: https://app.fireflies.ai/view/01KT44Y0K0N61P2K89SA5118HN

#### Findings
| Criterion | Severity | Speaker (status) | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|---|
| HF-10 (light) | Medium | Simon Ward (Script/unqualified) | ~04:30 | "only to enroll the employees this week, suppress the invites and then build out their contribution levels based on what you've shared with us. Can you remind me again the change in the employer contribution? Is that based on tenure?" — followed by confirming "anyone that is director level or above, they can be matched up to 8%. Anyone below, they're matched to 4%." | MCC 2017 (information on a retail financial product — occupational pension contribution mechanics); Kota `Financial Product Information to Customers` |

#### Notes
- This is principally an **operational enrolment call** (SSO, email-whitelisting/SPF-DKIM-DMARC, billing, comms, Aviva enrolment setup). Most of it is clearly out of MCC scope (platform/IT ops).
- The HF-10 (light) flag is for Simon (unqualified, script) **discussing and confirming the occupational pension employer-contribution tiers** (Aviva scheme: 8% for director-level+, 4% below) and "building out their contribution levels." Reading charitably, he is **executing the client's own instruction** for an enrolment config rather than advising on it — which is why this is graded **light / Grade 2** rather than HF-00/Grade 3. He does not recommend, compare, or value-judge; he reflects back the employer's stated rule. Still, a script-pathway speaker articulating pension contribution mechanics sits on the perimeter and should be coached.
- Simon appropriately defers regulated questions: *"if anyone has any questions or needs to speak to like a pension advisor or anything like that, we'll be there to sort"* (on-site presence plan) — good deferral signal.
- **No AE statement** made on this call (contrast with prior LearnUpon #2, 2026-05-15). No HF-05.
- **HF-03 not fired** — no firm-capability misstatement.
- **John Hayes** is a Kota speaker not on the register snapshot → treated fail-closed unqualified; his contribution is limited to comms-sample logistics (out of MCC scope). No finding.
- **Escalation**: No. (Grade 2 → documented only, no Asana task per queue rules.)

---

### Deel <> KOTA - GP referrals weekly — 01KTKCH4DFT4SYPVKJ0J65MZWC — 2026-06-09 09:00
**External**: Carlos Lorente Panadero (Deel — **PARTNER**, GP referral ops)
**Kota speaker(s)**: Paul O'Hanlon — ✅ Fully Qualified
**Department**: GTM / Partnerships
**Duration**: 25 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTKCH4DFT4SYPVKJ0J65MZWC

#### Findings
No findings. Partner referral-tracking ops (spreadsheet/Salesforce reconciliation, deal pipeline). No retail consumer present. Mentions of "medical history disregarded" plans, MHD/underwriting, premium-at-close are **partner-to-partner commercial context**, not consumer information. Paul is fully qualified regardless.

#### Notes
No consumer-facing MCC activity. **Escalation**: No.

---

### Emma Kavanagh and Paul O'Hanlon — 01KTNVFF3JX3AG4755VSE32A52 — 2026-06-09 09:30
**External**: Emma (Europa Worldwide — misdirected enquiry)
**Kota speaker(s)**: Paul O'Hanlon — ✅ Fully Qualified
**Department**: GTM
**Duration**: 12 min (much shorter actual)
**Grade**: **1 — Pass** (model negative)
**Fireflies**: https://app.fireflies.ai/view/01KTNVFF3JX3AG4755VSE32A52

#### Findings
No findings. Caller wanted **cross-border tax advice** (Hong Kong/Dubai employee tax split). Paul correctly identifies it as out of scope and declines: *"Unfortunately I can't help with that"* — textbook perimeter handling. Exemplary negative-class call.

#### Notes
**Escalation**: No. ES-03 not triggered — Paul refused the out-of-scope action rather than agreeing to it.

---

### Kota & Unisure — 01KTH9J1Q36N452ETX34K92N49 — 2026-06-09 09:30
**External**: Peter Taylor (Unisure Solutions — **INSURER/SUPPLIER**); Ceri Thomas (Yonder — Kota-affiliated)
**Kota speaker(s)**: Colin Pon — ✅ Qualified APA PMI only (pensions/life out of scope)
**Department**: Benefits / Partnerships
**Duration**: 45 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTH9J1Q36N452ETX34K92N49

#### Findings
No findings. Supplier-onboarding/contracting call with an insurer. Extensive discussion of non-admitted vs admitted structures, group life/IP/medical mechanics, A-vs-B financial-strength ratings, fronting/captive cells — all **insurer-to-intermediary commercial diligence**, no retail consumer present. Colin's APA-PMI-only scope is not exceeded in a consumer-facing sense because there is no consumer.

#### Notes
Pension talk (international pensions intro to Zurich contact) is exploratory partner-sourcing, not consumer advice. **Escalation**: No.

---

### Matthew - Askin Catch Up — 01KTK81ZP7F7TADBWQ9012T4KF — 2026-06-09 10:00
**External**: Askin Nur Kale (Three.ie — prospect, benefits-portal/HRIS evaluation)
**Kota speaker(s)**: Matthew Brennan (matthew@yonder.app) — ✅ Fully Qualified (Pensions & Life + PMI NE)
**Department**: GTM
**Duration**: 25 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTK81ZP7F7TADBWQ9012T4KF

#### Findings
No findings. Pure discovery/ops: HRIS integration, admin-panel reporting, procurement process, timeline, Aon cost comparison. No regulated product mechanics, advice, or comparison. Matthew is fully qualified regardless.

#### Notes
**Escalation**: No.

---

### Meet – Nicky <> Kota Intro — 01KTNY1MJMXB8XY3V7XYRS82X7 — 2026-06-09 10:14
**External**: Nicky Brocklehurst (Slice Mobile — networking/intro)
**Kota speaker(s)**: Paul O'Hanlon — ✅ Fully Qualified; Henry Godson — ❌ Script pathway (BDR, unqualified)
**Department**: GTM
**Duration**: 13 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTNY1MJMXB8XY3V7XYRS82X7

#### Findings
No findings. Pure relationship/dinner-event intro; no product discussed at all. **Henry Godson (script)** speaks only social pleasantries (BBC building history) — no regulated activity, so no HF-00. Good negative example of a script-pathway speaker staying within bounds.

#### Notes
**Escalation**: No.

---

### PP UAE/Kota - GP and EOR Opportunities — 01KTGXN6CWMSM5SD4YYDG7BYJZ — 2026-06-09 10:30
**External**: Jude Dassouki, "Dave", "Micheal" (Pacific Prime — **PARTNER/BROKER**); Ceri (Yonder)
**Kota speaker(s)**: Colin Pon — ✅ APA PMI; Paul O'Hanlon — ✅ Fully Qualified
**Department**: GTM / Partnerships
**Duration**: 24 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTGXN6CWMSM5SD4YYDG7BYJZ

#### Findings
No findings. Partner triage of UAE/Singapore GP/EOR opportunities with an insurance broker. FMU vs MHD underwriting discussion is **broker-to-broker** technical context (led mostly by Pacific Prime's Micheal). No retail consumer present. Paul appropriately notes data-handling care: *"we can't like take clients data in some of these markets... I need to check with our compliance team."*

#### Notes
**Escalation**: No.

---

### Kota & Exile - Employee Benefits — 01KTK1VV8Z0Y1F60SQKS9QDSH6 — 2026-06-09 14:00
**External**: Sarah Garrigan (Exile Group — prospect, UK; consumer-facing)
**Kota speaker(s)**: Paul O'Hanlon — ✅ Fully Qualified
**Department**: Benefits / GTM
**Duration**: 31 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTK1VV8Z0Y1F60SQKS9QDSH6

#### Findings
No findings. Platform demo + benefits/pension discussion. Paul is fully qualified, so PMI/life/IP/cash-plan/pension talk is in scope. Notably, Paul **declines to compare pension providers**: *"On the pension front for the moment, because we only work with smart, we don't really get involved in like comparing, contrasting"* and *"I can't sit here and say that it's going to have a better [management charge]"* — correct restraint on Royal London vs Smart Pension charges/performance.

#### Notes
- Platform fee quoted (£6 PEPM) — **not in scope** (platform charge, not regulated product price).
- Sarah disparages her own external broker (*"maybe not the most responsive broker"*) — this is the customer's statement about a third party, not a Kota staff utterance; **not SF-13/HF-14**.
- **Escalation**: No.

---

### Lloyds Intelligence x Kota — 01KT46XGTBXDZ4RDTNQVFKCWZA — 2026-06-09 14:00
**External**: Anna Edwards, Ellie Pyne, Nick Courtney (Lloyds List Intelligence — prospect, consumer-facing)
**Kota speaker(s)**: Callum Pearse — ✅ APA Pensions + PMI(NE); Matthew Brennan (matthew@yonder.app) — ✅ Fully Qualified; Dan McAvinue (dan@kota.io, silent on transcript)
**Department**: GTM
**Duration**: 42 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KT46XGTBXDZ4RDTNQVFKCWZA

#### Findings
No findings. Platform/pricing/TRS demo. All discussion is about the **Coda platform** (HRIS/BambooHR sync, total-reward statement, salary-sacrifice management/compliance layer, brokerage model, one-fee-PEPM pricing, integrations) — not regulated product advice or mechanics. Provider names (Vitality/Bupa/Aviva/Smart Pension) referenced only as **panel/integration breadth**, no performance or comparative value claims (no HF-02/HF-11/HF-15). Firm regulatory status stated correctly by Matthew: *"we're regulated by the Central Bank of Ireland, the FCA"* — accurate (no HF-03).

#### Notes
- Callum operating within his pension scope and platform remit; Matthew fully qualified. No perimeter issue.
- **Escalation**: No.

---

### Ultimo x Kota: Fixing the HRIS Sync — 01KTKPZ8EWMHJVNQA7MY7SN1MP — 2026-06-09 14:30
**External**: Zoë Kroeze, Megan Hubregtse (Ultimo — existing client, onboarding ops)
**Kota speaker(s)**: Simon Ward — ❌ Script pathway (unqualified); Callum Pearse (callum@kota.io, organiser, not speaking on transcript)
**Department**: CS/CX
**Duration**: 27 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTKPZ8EWMHJVNQA7MY7SN1MP

#### Findings
No findings. Entirely **HRIS-sync/onboarding ops** (HiBob field mapping, contractor exclusion, date-of-birth/NI permissions, employee comms, invite flow). Simon (script) **explicitly defers pension and group-risk to qualified parties**: on Smart Pension — *"I believe that we're introing you to Smart Pension directly... I can pick that up at Megan then later"*; group life/IP noted as "paused." UK PMI handled as a setup/quote-retrieval admin task, not a product description. Clean negative example for a script-pathway speaker doing legitimate CS work.

#### Notes
**Escalation**: No.

---

### Scaith/Kota - Demo and next steps — 01KTHK23FC4ENDXF99WT00PZYK — 2026-06-09 15:00
**External**: Cassio Giometti (Sciath, Brazil — **PARTNER/BROKER**); Ceri (Yonder)
**Kota speaker(s)**: Colin Pon — ✅ APA PMI
**Department**: Partnerships
**Duration**: 58 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTHK23FC4ENDXF99WT00PZYK

#### Findings
No findings. Broker partnership demo/diligence with a Brazilian broker. Discussion of Brazil medical mechanics (network/out-of-network claims, COBRA-style contribution liabilities, underwriting/waiting periods, commission %, revenue-share) is **broker-to-broker commercial**, no retail consumer present. Colin's APA-PMI scope is not exceeded in a consumer sense.

#### Notes
The product-mechanics knowledge transfer flows largely **from** the Brazilian broker **to** Colin. Commission/revenue-share negotiation (50/50 vs 20% net) is partner commercial, not consumer inducement (SF-11 n/a — no consumer). **Escalation**: No.

---

### Payfit Integration Feedback Call — 01KTHATD1T0R1EDPBTX8M39Z50 — 2026-06-09 15:15
**External**: Chloe Pease, Megan Jevtic (Payfit — **PARTNER**); Yonder-affiliated: Kate Fullen (kate@yonder.app), Deepak Baliga (deepak@goyonder.io), Patrick (patrick@goyonder.io)
**Kota speaker(s)**: Stewart Cartwright (stewart@kota.io), Oleg (oleg@kota.io), Ella (ella@kota.io) — unknown speakers, **fail-closed unqualified**
**Department**: Partnerships / Product
**Duration**: ~45 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTHATD1T0R1EDPBTX8M39Z50

#### Findings
No findings. Product/UX feedback call on the Coda↔Payfit embed (quote-flow copy, opt-in/opt-out, broker-switch UX, account-manager tagging, support routing). No retail consumer present — partner integration discussion. References to "advisor", "free quote", "indicative pricing" are about **product-flow copy design**, not statements made to a consumer.

#### Notes
- **Kate Fullen is on this call** (kate@yonder.app). Per the register she is **Unregistered / cannot conduct regulated activity**. On this transcript she acts only as a meeting facilitator for the partner product-feedback session and does **not** conduct any consumer-facing regulated activity, so no HF-00 fires here. **However**, her continued presence on Kota-related calls remains the open compliance-gap item flagged in `research-mcc-fitness-probity.md` (April 2026 action log) — surface to Compliance for the standing register review, not as a call-specific breach.
- Unknown Kota speakers (Stewart/Oleg/Ella) treated fail-closed; all utterances are product/ops. No finding.
- **Escalation**: No.

---

### Kota / Glean — 01KTMER2KF2946KJ0498K3Z4P5 — 2026-06-09 15:30
**External**: Natasha Bhat (Glean — existing client, onboarding ops)
**Kota speaker(s)**: Simon Ward — ❌ Script pathway (unqualified); Callum Pearse (callum@kota.io, not speaking on transcript)
**Department**: CS/CX
**Duration**: 12 min
**Grade**: **1 — Pass**
**Fireflies**: https://app.fireflies.ai/view/01KTMER2KF2946KJ0498K3Z4P5

#### Findings
No findings. Pure data-sync/payroll admin (HRIS export, NI/PPS/postcode field mapping, Smart Pension upload before payroll cutoff). Simon instructs the client to *"just run those as normal through payroll"* for existing standard contributions — operational, not advisory. No product mechanics, no AE statement. Clean.

#### Notes
- **PII handling watch (not a breach):** Simon asks for an HRIS **export** into a shared sheet to manually update NI numbers/postcodes — he is using the in-product HRIS-sync path and a sheet for missing fields, and explicitly does *not* ask Natasha to email PII to him (*"don't... just pop me a message"*). Does not meet HF-06 (no agreement to receive PII by unprotected channel). Noted for awareness only.
- **Escalation**: No.

---

## Cross-Call Patterns

1. **Partner/supplier dominance.** 7 of 14 calls are partner/supplier/affiliate calls with no retail consumer (Deel, Unisure, Pacific Prime, Scaith, Payfit + the two Yonder-affiliate-heavy calls). Consumer-facing MCC criteria structurally do not apply; documented as negatives.
2. **Script-pathway speakers stayed largely in bounds.** Simon Ward appears on 3 calls (LearnUpon #1, Ultimo, Glean). On Ultimo and Glean he correctly confined himself to HRIS/payroll ops and deferred pension to Smart Pension/qualified colleagues. Only on LearnUpon #1 did he edge onto pension-contribution mechanics (HF-10 light). Henry Godson (script) on the Nicky intro spoke only pleasantries. **Coaching point for Simon:** when articulating occupational-pension contribution tiers during enrolment, frame strictly as executing the client's instruction and avoid restating the mechanics himself.
3. **Paul O'Hanlon AE framing recurs.** The "3.5% between employer and employee / otherwise government scheme" framing (365 Finance) is the same ambiguous occupational-exemption-vs-AE-total framing seen before (Karl O'Brien, India). Correct under charitable reading, but a candidate for a standard scripted phrasing so qualified staff disambiguate "occupational exemption 3.5%" from "AE total 3.5% incl. State."
4. **No HF-03 / no HF-05 confirmed / no ES escalations** across the day. Firm regulatory status was stated correctly where it came up (Lloyds — Matthew).

## Open Questions for the Designer
1. **HF-10 vs operational enrolment execution.** Where an unqualified CS rep restates an employer's own contribution-tier rule to configure enrolment (LearnUpon #1, Simon Ward), is that "information on a regulated product" (HF-10) or out-of-scope back-office execution? Recommend the criteria explicitly carve out "reflecting back the employer's stated enrolment configuration" from HF-10, distinct from describing how the product works.
2. **AE 3.5% disambiguation.** Add a source-of-truth helper note distinguishing the two 3.5% figures (Pensions Authority occupational-exemption total vs AE Year 1–3 split incl. State) so the agent doesn't false-positive qualified staff who use the occupational-exemption reading.

## Asana
**One Grade-2 call (LearnUpon #1).** Per the queue rules in `AsanaQueueManager/spec-asana-task.md`, **Grade 2 (Pass-with-comments) does not generate an Asana task** — documented in this eval for coaching only. **No Asana tasks created.** All other calls Grade 1.

**Standing item (not a call task):** Kate Fullen's presence on the Payfit call should feed the existing register-level compliance-gap review, not a per-call Asana task.

---

## Exclusions / Duplicates
- `01KTNSS860G5ASRXJMGM1M6H8T` — "Meet – Deel <> KOTA - GP referrals weekly" (09:00) — **DUPLICATE** of call #3 (`01KTKCH4DFT4SYPVKJ0J65MZWC`). Skipped, not double-counted.
