---
title: "Email Monitoring — Intercom — Week 35 (24–28 Aug 2026)"
type: source
tags:
  - compliance/conduct
  - compliance/data-protection
  - regulation/cbi
  - process/audit
  - process/breach
created: 2026-08-28
updated: 2026-08-28
status: active
source_file: Intercom email channel (support@kota.io / benops@kota.io)
---

# Email Monitoring — Intercom — Week 35 (24–28 Aug 2026)

Second run of the email supervision programme, applying the Call Monitoring
criteria unchanged. Method as week 34: full population sweep, risk-weighted
sample, script/procedure cross-reference on escalated items.

**Population: 594 email conversations, 24–28 Aug. Complete — 6 pages, all
retrieved, matching Intercom's own count.**

## Headline

> [!warning] One item needs action before Monday
> A **health scheme renewal letter for a Kota staff member was posted to a
> client's office**. It was not treated as a personal data incident. The
> Article 33 clock ran from 27 August.

## Volume and SLA — week on week

| | Week 34 | Week 35 | |
|---|---|---|---|
| Conversations | 434 | **594** | +37% |
| Open at review | 141 | **220** | +56% |
| SLA missed | 164 | **215** | |
| Miss rate (of SLA-tracked) | 58% | **55%** | slightly better |
| `wrong-team-redirect` | 87 (20%) | **135 (23%)** | worse |

By tier:

| Tier | Hit | Missed | Miss rate | vs W34 |
|---|---|---|---|---|
| EM: P0 — Embed (1h) | 17 | 121 | **69%** | 83% → improved |
| All: Urgent (30m) | 3 | 12 | **80%** | 74% → worse |
| BenOps: P1 (8h) | 22 | 49 | **52%** | |
| PL: P3 — Tier 3 SME (8h) | 68 | 32 | **30%** | 19% → worse |
| PL: P1 — Tier 1 SME (1h) | 0 | 1 | 100% | new tier |

Volume rose 37% while the overall miss rate held roughly flat. The tightest
tiers remain the problem, and the P3 tier — solid last week — has degraded.

## Sample

**5 threads assessed** from the 32 customer-facing conversations (Employer,
Employee, New Customer). Risk-weighted, not random.

| Handler | Client | Subject | Grade |
|---|---|---|---|
| Michael Nikeenok | Ramp Network | Renewal letter misdelivered | **4 = Fail with referral** |
| — (unassigned) | Diarmuid Egan | Pension transfer-in, no reply | **3 = Fail** |
| Michael Nikeenok | Onboard Retail | Enrolment employee doesn't recall | 2 = Pass with comments |
| Michael Nikeenok | Ineffable Intelligence | Dependant age eligibility | 2 = Pass with comments |
| Michael Nikeenok | Flatpay | Opt out of all benefits | 1 = Pass |

## Escalated 1 — Misdelivered renewal letter (Data Protection)

Ramp Network's People and Talent Operations Manager wrote on 27 August:
*"I received a letter sent to our Ireland offices addressed to a 'Trevor
Gardiner' about his health scheme being renewed. This name is unfamiliar to us
and is certainly not an active employee."*

Michael replied: *"Trevor is one of ours, I can confirm that. This appears to be
a mailing error."* Trevor Gardiner is Kota personnel — he appears in the Call
Supervision Audit and Documentation Audit person lists.

So an identifiable individual's health insurance correspondence was disclosed to
a third-party company.

**It was not treated as an incident.** Labelled a mailing error, snoozed until
the next day, then snoozed again until the following Monday. No breach
assessment, no DPO escalation, no incident log, no Article 33 clock.

A secondary point: confirming to the client that Trevor is Kota personnel was
itself an unnecessary disclosure. "I'll look into this" would have sufficed.

### Procedure cross-reference

Kota has handled a comparable incident before — the Notion page *"Mixed
employees data incident"* (Dec 2025), where an employee could see another
employee's address in the app and the employer raised concerns about exposure of
sensitive personal data. The Cybersecurity page commits Kota to *"collaborate
with customers, data Controllers, and regulators to fulfill all obligations in
the event of an incident or data breach."*

Precedent and commitment both exist. Neither was applied. This is a
**recognition failure, not a knowledge gap** — the handler did not identify a
misdelivered health letter as a reportable event.

> [!important] Not verified
> The letter is an attachment ("Scanned Document.pdf") this review could not
> open. Whether it contained health data beyond the fact of cover determines
> whether this stays a 4 or becomes a 5. **Read the PDF before concluding.**

### This is the second renewal defect in two weeks

- **Week 34** — renewal campaign email sent to a client with no Irish employees since June
- **Week 35** — renewal letter posted to the wrong company entirely

Same process, an addressing and data-quality problem that now looks systemic
rather than incidental. The week 34 finding recommended fixing suppression on
cancelled schemes; this widens it to the mailing file itself.

## Escalated 2 — Pension transfer query, no reply (CPC)

An employee wrote on 26 August: *"I am looking to transfer pension funds from a
previous employer to my current scheme, how may I go about this?"*

**No reply of any kind.** Both SLA targets breached. Still open and unanswered
two days later. No advice was given, so there is no MCC issue — the failure is
silence on a time-sensitive request.

### Script cross-reference

This is sharper than it first appears. An approved Help Centre article answers
the question directly: **"Can I transfer my existing pension into my new pension
scheme with Kota?"** (art. 9145103, published, tagged `geo:ireland`,
`user:employee`, `product:pension`).

The query is almost verbatim the article title. This needed no specialist input
and no judgement — it was a same-hour reply from published content. Fin
escalated it out under "Exit after attribute detection" rather than serving the
article, and it then sat unassigned.

**That makes this a Fin configuration and triage finding, not a handler one.**

## The other three

**Onboard Retail** — good handling (22-minute reply, escalated, no advice), but
the employer's actual words were that the employee *"has no recollection of
enrolling in the health plan"* and asks to reverse the charges. That is a
possible mis-enrolment and consent issue with a redress question attached. It
was processed as a routine cancellation and nothing was flagged to Compliance.

**Ineffable Intelligence** — the reply is a good example of the right instinct.
Michael did not assert the eligibility rule; he wrote *"we've found information
suggesting the age restriction may not reflect Bupa's current policy"* and
escalated. But it points at a **possible product defect**: if the platform
enforces an under-18 dependant rule that doesn't match Bupa's, eligible
dependants are being refused cover — this member was told no by the product, and
others may have been silently. Also a Tier 1 (1h) SLA answered in 15 hours.

**Flatpay** — clean. Routed, no advice, no retention attempt.

## Recurring themes

| Theme | W34 | W35 |
|---|---|---|
| Regulatory footer absent on CX Platform outbound | ✓ | ✓ |
| Snoozing used in place of responding | ✓ | ✓ (4 of 5 sampled) |
| Renewal communications going to wrong recipients | ✓ | ✓ |
| Opt-out disclosure question unresolved | ✓ | ✓ |

The opt-out disclosure question and the missing footer are now outstanding from
two consecutive weeks.

## Actions

| # | Action | Owner | By |
|---|---|---|---|
| 1 | **Article 33 assessment on the misdelivered letter.** Read the PDF, notify DPO, log the incident, notify Trevor Gardiner, ask Ramp to confirm destruction | Compliance / DPO | **31 Aug** |
| 2 | Root-cause the renewal mailing file address; check whether other letters in the run went astray | Support ops | 31 Aug |
| 3 | Reply to Diarmuid Egan using art. 9145103 | BenOps | **today** |
| 4 | Review why Fin escalates queries it holds approved content for | Support ops | 4 Sep |
| 5 | Establish how Anthony Carson was enrolled and whether consent is evidenced | BenOps / Compliance | 4 Sep |
| 6 | Confirm Bupa's dependant age rule against what the platform enforces; quantify refusals | Product / Benefits | 4 Sep |
| 7 | Settle the opt-out consequences-of-cancellation disclosure question | Compliance | 4 Sep |
| 8 | Add the regulatory footer to CX Platform outbound | Support ops | 4 Sep |

## Method and Limitations

- Criteria unchanged from the Call Monitoring programme. Recording Consent
  remapped to Regulatory Disclosure, as in week 34.
- Sample of 5 from 594. **Risk-weighted, not random** — it does not support a
  channel-wide pass rate. A random sample alongside would be needed for that.
- Full reply chains read for all 5 assessed threads.
- SLA figures are Intercom's own `sla_applied.sla_status`.
- The misdelivered letter's contents were not inspected; that limits the grading
  of the most serious item this week.
- **Grade note:** the week 34 Ctrl Alt item was graded 4 = Fail with referral by
  Compliance and has since been recorded in Asana as Minor Correction. Left as
  amended; the management view belongs in that column.
