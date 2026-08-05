---
title: Complaints Handling — CPC (Ireland) and FCA DISP (UK)
created: 2026-08-04
type: research
tags:
  - compliance/complaints
  - regulation/cbi
  - regulation/fca
sources:
  - Central Bank of Ireland — Consumer Protection Code (complaints resolution provisions)
  - CPC 2012 Guidance Ch. 8 "Errors and complaints resolution" (carried into CPC 2025)
  - FCA Handbook DISP 1.4, 1.5, 1.6
  - A&L Goodbody — Consumer Protection Code Review briefing
status: active
---

# Complaints Handling — CPC (Ireland) and FCA DISP (UK)

Written to unblock **HF-23** and **HF-24** in `req-intercom-detection-criteria.md`, which carried
`{{TO VERIFY}}` placeholders and could not grade. The 2026-08-04 Intercom dry run surfaced a live
`Complaint / Escalation` with `sla_status: missed` that had to be reported as ungradeable.

Kota is **CBI-regulated** as an insurance intermediary (Irish activity) and **FCA-regulated** as a
broker (UK activity), so both regimes apply depending on the activity. The CX conversations sampled
were Irish customers, so the CPC timeline is the primary one.

> [!warning] Confidence and provenance
> Day counts below are drawn from CBI guidance and firms' published CPC complaints procedures,
> which recite the Code's requirements, plus the FCA Handbook. They are consistent across multiple
> independent sources. **They have not been checked against the CPC 2025 statutory text
> (S.I. 81/2025) line by line.** Before these criteria escalate anything to a regulator-facing
> outcome, Compliance should confirm against the Code itself — in particular whether CPC 2025
> renumbered or altered the CPC 2012 Chapter 10 sequence, and whether the "immediately acknowledge
> electronic complaints" provision creates a separate, shorter deadline for chat and email.

## Ireland — CPC complaints timeline

Applies to complaints from consumers about a regulated activity.

| Stage | Deadline | Notes |
|---|---|---|
| **Written acknowledgement** | **5 business days** from receipt | Must be in writing |
| **Electronic complaints** | **Immediate** acknowledgement, same medium | CPC 2025 addition — gives the consumer a record of submission. **Directly relevant to in-app chat and `support@kota.io`** |
| **Regular written updates** | at intervals **no greater than 20 business days** | Counted from the date the complaint was received, not from the last update |
| **Resolution / final response** | **40 business days** from receipt | If unresolved at 40 days, the firm must issue a final response letter setting out the steps taken and the anticipated timeframe for resolution |
| **FSPO signposting** | On final response | Complainant must be told of the right to refer to the Financial Services and Pensions Ombudsman |

At 40 business days without resolution or a final response, the complainant may ask the FSPO to
intervene — so the deadline has an external consequence, not merely an internal one.

## UK — FCA DISP

| Stage | Deadline | Reference |
|---|---|---|
| **Acknowledgement** | **Prompt** written acknowledgement — no fixed day count | DISP 1.6.1R |
| **Final response** | **8 weeks** from receipt; or a written response explaining why a final response is not yet possible | DISP 1.6.2R |
| **Payment services / e-money** | **15 business days** | Narrower regime; unlikely to apply to Kota's activity |
| **Summary resolution** | Complaints resolved by close of business on the **3rd business day** after receipt, where the complainant has indicated acceptance, may use a lighter summary resolution communication | DISP 1.5 |
| **FOS signposting** | On final response and on summary resolution communication | DISP 1.6 |

DISP uses "prompt" rather than a fixed acknowledgement deadline, so the Irish 5-business-day rule is
the stricter and more mechanically checkable of the two.

## What counts as a complaint

The obligation attaches to **substance, not vocabulary** — a consumer need not use the word
"complaint". Both regimes define it broadly as an expression of dissatisfaction, whether justified
or not, about the provision of or failure to provide a financial service.

Practical markers observed or expected in the CX channel:
- Explicit: "I am writing to formally raise a complaint", "please treat this as a formal complaint",
  a request for the escalation process or a formal review
- Implicit: an unresolved issue persisting over weeks, dissatisfaction with an outcome or with
  service quality, a request for escalation to a manager, a reference to the FSPO/FOS or to
  litigation
- A reference to the regulator or ombudsman is **always** at least a complaint marker, and also
  fires ES-02

> [!important] Internal SLA ≠ regulatory deadline
> Intercom's `sla_applied` / `sla_status` fields are commercial targets set by Kota, not regulatory
> deadlines. The sampled CX SLA (`PL: P3 - Tier 3 SME - FRT (8h) / NRT (8h) / TTR (24h)`) is far
> **tighter** than the CPC deadlines, so `sla_status: missed` does **not** imply a regulatory breach
> — and a `hit` SLA does not imply compliance, because the SLA measures first response, not
> acknowledgement-as-a-complaint or final response. **Report both; never substitute one for the
> other.** This is the single most likely source of false positives in HF-24.

## Interaction with product governance

Complaints data is not only a conduct matter. Under **Delegated Regulation (EU) 2017/2358 Art. 10**,
distributors must provide manufacturers with information including complaints data, and Art. 7
requires manufacturers to take complaints into account in product review. The EIOPA 2023 POG peer
review found this feedback loop was often weak or non-existent.

So an unlogged complaint (HF-23) has a second-order effect: it is missing from the data Kota owes its
manufacturers, and from its own product-review inputs. See
`compliance-wiki/wiki/concepts/product-governance.md`.

## Cross-references

- `Researcher/req-intercom-detection-criteria.md` — HF-23, HF-24, SF-18
- `compliance-wiki/wiki/concepts/product-governance.md` — Art. 10 complaints-data obligation
- **Gap**: `compliance-wiki/wiki/concepts/complaints.md` does not exist. The `compliance/complaints`
  tag is reserved in the wiki schema but unpopulated. Recommend creating it and filing this note
  into `wiki/sources/` per the wiki's own ingest workflow.

## Open questions

1. **Does CPC 2025 change the 5/20/40 sequence?** Sources recite the CPC 2012 Chapter 10 timeline.
   CPC 2025 applies from 24 March 2026 and is in force now, so the exact provisions must be
   confirmed against S.I. 81/2025.
2. **Does the "immediately acknowledge electronic complaints" provision create a separate deadline?**
   If so, a chat complaint may need same-session acknowledgement rather than 5 business days — which
   would make this the tightest deadline in the channel and change HF-24's arithmetic materially.
3. **Which regime applies to a UK employee of an Irish client, or vice versa?** Determines whether
   the 40-business-day or 8-week clock governs. Needs a routing rule keyed on something the agent
   can actually observe.
4. **Is there a complaints register today, and does the agent get read access?** HF-23 detects
   complaints absent from Intercom's classification, but the authoritative test is absence from the
   complaints register.
