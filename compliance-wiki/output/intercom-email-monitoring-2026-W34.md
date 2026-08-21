---
title: "Intercom Email Monitoring — Week 34 (17–21 Aug 2026)"
type: source
tags:
  - compliance/conduct
  - compliance/complaints
  - compliance/risk-management
  - process/incident
  - regulation/cbi
created: 2026-08-21
updated: 2026-08-21
status: active
source_file: Intercom (support@kota.io shared inbox, email channel)
---

# Intercom Email Monitoring — Week 34 (17–21 Aug 2026)

Monitoring sweep of the Intercom email channel for the week beginning Monday
17 August 2026. Scope: all conversations with `source.type = email` created
between 2026-08-17 00:00 UTC and 2026-08-21 12:37 UTC.

**Population: 434 conversations (complete — 5 pages, all retrieved, no sampling).**

> [!note] Scope note
> Gmail was also swept for correspondence *from* Intercom as a vendor
> (`intercom.io`, `send.intercom.com`, `hq.intercom.com`, `intercom-mail.com`).
> **Nil returns for the last 21 days.** No vendor notices, no DPA or
> sub-processor change notifications, no security advisories. The last
> substantive vendor item remains the 17 March 2026 note from the Intercom
> account manager moving Insights out of beta into the paid "Performance Pro"
> add-on.

## Key Takeaways

1. **SLA performance is the dominant finding — 164 of 283 SLA-tracked
   conversations were missed (58%).** The Embed P0 tier (1-hour first response)
   missed 97 of 117 (83%). The 30-minute Urgent tier missed 14 of 19 (74%).
2. **71 conversations remain open with an already-missed SLA**, 53 of them on
   Urgent or Embed P0 tiers. These are live, not historic.
3. **Three provider complaints ran through the channel this week** (CM-143628,
   CM-143362, CM-143443). Two received final response letters.
4. **Both final response letters signpost the UK Financial Ombudsman Service**,
   not the Irish FSPO. Raised below as an open question, not a finding.
5. **A confirmed fraud case** (Allianz, three policies) is in a 7-day appeal
   window that expires **24 August 2026**.
6. **25 automated "employee was deleted by their Employer" alerts** in five
   days — a material data-retention and deletion-trigger volume.
7. **87 conversations tagged `wrong-team-redirect` (20%)** — one in five inbound
   emails reaches the wrong queue first.

## Volume and Distribution

| Day | Conversations |
|---|---|
| Mon 17 Aug | 81 |
| Tue 18 Aug | 87 |
| Wed 19 Aug | 96 |
| Thu 20 Aug | 69 |
| Fri 21 Aug (to 12:37) | 101 |
| **Total** | **434** |

**State:** 247 closed · 141 open · 46 snoozed
**Fin (AI agent) participated:** 257 of 434 (59%)
**Unassigned:** 0 — every conversation reached a team or admin.

**Counterparties (top senders):** kota.io internal/automated 178 ·
Allianz (`e.allianz.com`) 101 · Deel 34 · Irish Life (incl. `cbcomms`) 37 ·
Remote 18 · Irish Life Health 12 · Bupa 7 · Zurich 5 · Vitality 5.

**By user type:** Provider 155 · Client (Embed) 66 · Internal 41 · Employer 24 ·
Employee 8 · New Customer 2 · unclassified 138.

**By provider:** General/none 114 · Allianz 106 · Irish Life 75 · Sanitas 12 ·
Vitality 8 · Zurich 6 · Bupa 6 · ONVZ 4 · Freedom 4 · Smart Pension 3 · DSS 3.

## SLA Performance

| Tier | Hit | Missed | Active | Cancelled | Miss rate |
|---|---|---|---|---|---|
| EM: P0 — Embed (FRT 1h / NRT 1h / TTR 8h) | 10 | **97** | 9 | 1 | **83%** |
| All: Urgent (FRT 30m / NRT 30m / TTR 2h) | 5 | **14** | 0 | 0 | **74%** |
| BenOps: P1 — Operational (FRT 8h / TTR 16h) | 23 | 39 | 13 | 3 | 63% |
| PL: P3 — Tier 3 SME (FRT 8h / TTR 24h) | 50 | 13 | 4 | 0 | 21% |
| PL: P2 — Tier 2 SME | 1 | 0 | 0 | 0 | 0% |
| All: P1 — BO Internal | 0 | 1 | 0 | 0 | 100% |
| **Total (SLA applied)** | **89** | **164** | **26** | **4** | **58%** |

151 conversations had no SLA applied at all.

The pattern is not uniform degradation. The P3 SME tier, on an 8-hour first
response target, performs acceptably at 21% missed. The failure concentrates
almost entirely in the tightest tiers: the 1-hour Embed P0 and the 30-minute
Urgent tier. This is consistent with the tight-target tiers being unresourced
rather than the team being uniformly overloaded.

> [!warning] Live exposure
> **71 conversations are still open with a missed SLA**, of which **53 sit on
> Urgent or Embed P0**. The oldest reaches back to Monday 17 August.

Examples of open, past-target items:

- `[ACTION REQUIRED] DSS Employee policy creation — Remote Technology Aps in DK`
  (Embed P0, opened 17 Aug 00:00)
- `Complaint - CM-143628 [#116402935]` (Embed P0, opened 17 Aug 08:10, reopened
  19 Aug)
- `Re: Re: Re: Internal Audit Error Corrections [#116313802]` (Embed P0, 17 Aug)
- `Re: Name Update Request Across all policies — Pautsch [#116403164]`
  (BO Internal P1, 17 Aug)
- `Re: Coverage Clarification — High Priority Executive level prospective
  (Anthropic) [#116404166]` (Embed P0, 18 Aug)
- `#1952172 - URGENT - Medical Claim` (Remote, Urgent tier, snoozed 21 Aug)

## Complaints

Three complaint references moved through the channel.

### CM-143628 — newborn dependent start date (open)

Allianz Care notified Kota on 17 August that a member complained about the
effective start date of a newborn dependent, added by Gsec with effect from
11 August 2026, under policy P005152345. Allianz asked Kota to confirm the
correct start date with Deel.

The thread was replied to on 18 and 20 August but **reopened on 19 August and
is open again as at 21 August, on an Embed P0 tier with a missed SLA**. This is
the one complaint still requiring action.

### CM-143362 — declined claim, cover cancellation (closed)

Complaint received by Allianz 07 August, final response issued. Claim C36217155
was initially declined on the basis that treatment took place after cancellation
of cover (out of force since 31 March 2026). On review Allianz reprocessed and
paid the claim under settlement C37437783 on 13 August, reimbursing KES 4,610.

### CM-143443 — delayed claim payment (closed)

Complaint received 11 August, final response issued 19 August. Payment of claim
C36208763 failed and was returned twice with reason "BENE ACCOUNT BENE NAME NOT
MATCH". Allianz has asked for corrected beneficiary bank details to reissue.

> [!question] Open question — ombudsman signposting
> Both final response letters direct the complainant to **the UK Financial
> Ombudsman Service** (Exchange Tower, London E14 9SR) within six months, and
> both are issued by Allianz Care from Park West, Dublin 12, over an Irish
> helpline (+353 1 514 8456). Neither letter mentions the Irish **Financial
> Services and Pensions Ombudsman**.
>
> These are the provider's letters, not Kota's, so the primary obligation sits
> with Allianz. But Kota is the distributor in the chain and these letters reach
> members through our channel. Whether UK FOS signposting is correct depends on
> the underwriting entity and the member's location — CM-143362 concerns a
> member reimbursed in Kenyan shillings, which is neither. Worth putting to
> Allianz and confirming the position before it recurs. Flagged as a question;
> not asserted as a breach.

## Fraud Case — Appeal Window Closes 24 August 2026

On 17 August Kota (Isabel) notified Deel that **Allianz has confirmed a proven
fraud case** relating to EOR member Abraham Scoth, covering policies
**P005252604, P004776649 and P004847354**. A report was attached.

Per Allianz's terms and Kota's, the member's cover **must be removed**. Kota
committed to actioning removal **after 7 days** to allow an appeal — a window
that **expires Monday 24 August 2026**. Deel was asked to notify the relevant
parties, as Deel owns the employer/employee relationship.

The forwarded Allianz internal correspondence (Claims Risk Unit, Health) records
that the policyholder has confirmed willingness to cooperate and repay the sum
due in instalments, and asks whether the policy — expiring November 2026 — will
be renewed under the group.

**The Kota-side thread is snoozed.** Two things need confirming before Monday:
that no appeal was received, and that the renewal question has been answered.

## Automated Data-Change Alerts

Automated `[Needs Attention]` notifications from `noreply@kota.io`:

| Alert type | Count |
|---|---|
| An employee was deleted by their Employer | **25** |
| An employee has their country changed | 3 |
| An Employee Salary Changed | 1 |

**Employee deletions — 25 in five working days.** Each is an employer-initiated
deletion flowing through HRIS into the Kota platform. This connects directly to
[[Data Retention]] and the CPC 2025 retention position: deletion by an employer
is a retention trigger, and at five per working day the volume is high enough
that the handling needs to be a defined process rather than case-by-case. Most
were closed quickly; three remain open (17 Aug 12:34, and two from 19 Aug 16:47).

**Country changes — 3.** ES→PT, DE→CH (×2). Each is a cross-border change that
may alter which regulatory regime and which product applies to that member. The
two logged at 21 Aug 12:36 are open. The DE→CH change is the notable one:
Switzerland is outside the EEA, so freedom-of-services passporting does not
carry across.

## Operational Finding — Misrouting

**87 conversations (20%) carry the `wrong-team-redirect` tag.** Concentrated in:
Allianz `client.services` 21 · Kota automated 9 · Irish Life (various) 21
combined · Allianz `group.admin` 7 · Bupa 4 · Allianz `disability.services` 4.

One in five inbound emails lands in the wrong queue and must be redirected
before work starts. On tiers with a 30-minute or 1-hour first-response target,
a redirect hop is likely a direct contributor to the miss rates above. The two
findings should be read together.

A further 3 conversations are tagged `BenOps - Deel - Bad Ticket`.

## Recommended Actions

| # | Action | Owner | By |
|---|---|---|---|
| 1 | Confirm no appeal received on the Allianz fraud case; action cover removal on P005252604 / P004776649 / P004847354; answer Allianz's renewal question | BenOps / Isabel | **24 Aug** |
| 2 | Close out complaint CM-143628 — confirm newborn dependent start date with Deel | BenOps | 25 Aug |
| 3 | Work the 53 open Urgent/Embed-P0 conversations that are already past target | Support leads | 25 Aug |
| 4 | Put the UK FOS vs FSPO signposting question to Allianz in writing | Compliance | 28 Aug |
| 5 | Root-cause the 83% Embed P0 miss rate — resourcing, target realism, or the redirect hop | Support leads + Compliance | 31 Aug |
| 6 | Review the 20% misrouting rate; fix inbound routing rules for Allianz and Irish Life senders | Support ops | 31 Aug |
| 7 | Define and document the retention/deletion process behind the 25 employee-deletion alerts | Compliance | 31 Aug |
| 8 | Confirm regulatory treatment of the DE→CH member change (non-EEA) | Compliance | 31 Aug |

## Method and Limitations

- Source: Intercom `search_conversations`, filtered `source_type=email`,
  `created_at > 1786924800` (2026-08-17 00:00 UTC). All 5 pages retrieved;
  434 unique conversation IDs, matching Intercom's reported `total_count`.
- Classification of complaints, fraud and data-change items is based on
  **subject lines and the opening message body** of each conversation. Full
  reply chains were not read for all 434. A conversation whose compliance
  relevance only emerges in a later reply would not be caught by this sweep.
- SLA figures are Intercom's own `sla_applied.sla_status` values, not
  recalculated independently.
- Keyword scanning covered: complaint, GDPR, data subject/protection/breach,
  DSAR, erasure, deletion, access request, privacy, consent, vulnerable,
  ombudsman, FSPO, regulator, escalation, legal, solicitor, fraud, dispute,
  mis-sold, misrepresentation. **No DSARs, no GDPR/data-protection requests and
  no personal-data breaches surfaced this week.**
- Member names, policy numbers and claim references are reproduced here because
  they are needed to action items 1 and 2. Per the wiki's confidentiality
  convention this report sits in `output/` and should not be propagated into
  wiki entity or concept pages in identifiable form.
