---
title: "Email Monitoring — Intercom — 29 Aug to 15 Sep 2026 (catch-up)"
type: source
tags:
  - compliance/conduct
  - compliance/data-protection
  - regulation/cbi
  - process/audit
created: 2026-09-15
updated: 2026-09-15
status: active
source_file: Intercom email channel (support@kota.io / benops@kota.io)
---

# Email Monitoring — Intercom — 29 Aug to 15 Sep 2026

Third run. **This is a catch-up covering 18 days, not a weekly** — the last
review ran to 28 August, so weeks 36 and 37 had no coverage and week 38 is
partial. Criteria unchanged from Call Monitoring.

**Population: 1,484 email conversations. Complete — 10 pages, reconciled
against Intercom's own count.**

## Headline

The programme is starting to show its value in both directions. **Two of the
four prior escalations demonstrably changed behaviour.** One was correctly
overturned on evidence. But the pension-transfer failure **recurred within a
week of being fixed**, which is the more important signal.

## Follow-up on the four prior escalations

| Item | Raised | Outcome |
|---|---|---|
| **Ctrl Alt** — MyFutureFund answered without qualification (W34) | 21 Aug | **Behaviour changed.** Same topic recurred 14 Sep (Paligo) and was handled correctly — routed, no interpretation offered. |
| **Definely** — renewal campaign email (W34) | 21 Aug | Closed as False Positive |
| **Ramp** — misdelivered renewal letter (W35) | 28 Aug | **Correctly overturned.** Verified: *"Naoise confirmed that he was only listed as an admin on the account. Trevors actual details were not shared."* Conversation closed 1 Sep. |
| **Diarmuid Egan** — pension transfer, no reply (W35) | 28 Aug | **Fixed, then repeated.** First reply 2 Sep. The same failure recurred 8 Sep with a different member. |

> [!note] On the Ramp overturn
> This is the process working. The finding was raised with an explicit
> "not verified — read the PDF first" caveat; the PDF was checked; the letter
> named the individual only as an account admin, not as an insured member; the
> finding was closed with a recorded rationale. That is the right outcome and
> the audit trail is sound.

## Volume and SLA

| | W34 | W35 | **W36–38** |
|---|---|---|---|
| Conversations | 434 | 594 | **1,484** (18 days) |
| Weekly run-rate | 434 | 594 | **~580** |
| Overall miss rate | 58% | 55% | **56%** |
| `wrong-team-redirect` | 20% | 23% | **18%** |

By tier — this is where it has moved:

| Tier | Hit | Missed | Miss rate | W35 |
|---|---|---|---|---|
| **All: Urgent (30m)** | 1 | 30 | **94%** | 80% |
| **PL: P1 — Tier 1 SME (1h)** | 1 | 6 | **86%** | 100% (n=1) |
| EM: P0 — Embed (1h) | 35 | 260 | **75%** | 69% |
| BenOps: P1 (8h) | 79 | 229 | **64%** | 52% |
| PL: P3 — Tier 3 SME (8h) | 226 | 76 | **24%** | 30% |

> [!warning] The Urgent tier has effectively stopped functioning
> **30 of 32 Urgent conversations missed their 30-minute target.** One was hit.
> This tier has degraded every period: 74% → 80% → **94%**. At this rate the
> tier is not a control, and its existence overstates what the channel actually
> delivers.

Two new tags appeared this period: `sla-breach-provider` (10) and a larger
`BenOps - Deel - Bad Ticket` count (17) — see the second escalation below.

## Sample

3 assessed from the 105 customer-facing conversations. Risk-weighted.

| Handler | Client | Subject | Grade |
|---|---|---|---|
| — (unassigned) | Marje Cruz | Pension transfer, no reply 7 days | **3 = Fail** |
| Clara Hughes | Deel / Natasha Hargan | Data correction closed as "bad ticket" | **3 = Fail** |
| Michael Nikeenok | Paligo | MyFutureFund double-deduction risk | 2 = Pass with comments |

## Escalated 1 — Pension transfer failure has recurred

A member wrote on 8 September, apologising for her own delay and supplying
exactly what Kota had asked for. **No reply in seven days.** Both SLA targets
breached. Still open.

Same BenOps subtopic (*Pension: Transfer In*), same team, same assignee, same
outcome as the week 35 escalation.

**The week 35 case was fixed. The cause was not.** Diarmuid Egan got a first
reply on 2 September, about 40 working hours after the flag — so escalation
works on the individual case. But the next one through the same queue failed the
same way six days later.

The week 35 recommendation — review why Fin escalates queries it holds approved
content for (art. 9145103 answers this question directly) — does not appear to
have been actioned.

## Escalated 2 — Data correction closed on a technicality

Deel wrote on 9 September: *"we've confirmed a genuine residence-country
discrepancy... Our internal record currently shows Spain... while the address on
file shows Great Britain... so her enrollment record reflects the right
country-specific plan."*

**No reply was sent.** Tagged `BenOps - Deel - Bad Ticket` and closed 87 minutes
later. The internal note explains why: *"Deel created a ticket to Kota as a
response to a Kota request. The Support team appears to have not checked who the
original request was from."*

The complaint about ticket hygiene may be entirely fair. But two live issues
went with it:

1. **Data accuracy** — a confirmed wrong country of residence on a benefits record.
2. **Possible cover detriment** — if the member is on a Spanish plan while resident in the UK, her cover may not respond where she lives. Nobody established whether that is so.

> [!important] New category with no handling standard
> **Five "Personal Data Correction" requests** arrived this period — three from
> Deel, one from Remote, one here. All on the Embed P0 tier. **All five missed
> SLA.** Whether these are being treated as Article 16 rectification requests,
> with the deadline that implies, is not evident from how they are worked.

## The one that went right

**Paligo, 14 September.** An employer asked why an employee with a company
pension had been enrolled in My Future Fund, flagging **double deduction** risk.

This is the week 34 Ctrl Alt topic exactly. This time Michael did not answer the
statutory question — he routed it to Benefits and said so. No interpretation
offered. **The MCC boundary point from week 34 has landed.**

The service outcome is weaker: the customer chased on 15 September with a payroll
cut-off *"by the end of this week"*. The SLA reads as hit because the
acknowledgement was prompt, but the substantive answer is outstanding against a
live deadline, and if it is missed an employee is deducted twice.

This also re-surfaces an unresolved week 34 question: **does the €20,000
auto-enrolment threshold apply per employment or to aggregate earnings**, and is
art. 14470927 complete on exemption mechanics? Never settled; now recurring with
a member's pay at stake.

## Actions

| # | Action | Owner | By |
|---|---|---|---|
| 1 | Reply to Marje Cruz | BenOps | **today** |
| 2 | Answer Paligo before the payroll cut-off, or tell them it won't be ready so they can hold the deduction | BenOps | **this week** |
| 3 | Establish Natasha Hargan's correct country and whether her plan matches it | BenOps | 18 Sep |
| 4 | Review all open items under *Pension: Transfer In* — two for two on failure | BenOps lead | 18 Sep |
| 5 | Agree a handling standard for "Personal data corrections": Article 16 or not, deadline, escalation route | Compliance / DPO | 22 Sep |
| 6 | Root-cause the Urgent tier — 94% missed makes it a nominal control | Support leads | 22 Sep |
| 7 | Action the outstanding W35 item on Fin escalating queries it has content for | Support ops | 22 Sep |
| 8 | Settle the €20,000 threshold question and update art. 14470927 | Compliance | 25 Sep |
| 9 | Review whether "Bad Ticket" tagging is closing substantive issues | BenOps lead | 25 Sep |

## Still carried over, now three periods running

- Opt-out consequences-of-cancellation disclosure question (a third Flatpay opt-out landed 2 Sep)
- Regulatory footer absent from CX Platform outbound

## Method and Limitations

- Criteria unchanged from Call Monitoring; Recording Consent remapped to Regulatory Disclosure.
- **Coverage gap:** weeks 36 and 37 were not reviewed contemporaneously. This
  catch-up covers them, but findings surfaced up to two weeks after the fact —
  the Natasha Hargan item was closed on 9 September and is only being seen now.
- Sample of 3 from 1,484. Risk-weighted, not random; no basis for a channel-wide
  pass rate.
- Full reply chains read for the 3 assessed threads and for the 4 prior escalations.
- SLA figures are Intercom's own `sla_applied.sla_status`.
