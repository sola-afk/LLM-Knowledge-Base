---
title: Intercom CX Compliance Eval — Dry Run (sample of 10)
created: 2026-08-04
type: eval
channel: intercom
run_type: dry-run
population: CX (team 5690482 · PL-CX Customer Ticket) · source_type=email
conversations_pulled: 10
conversations_excluded: 1
assessed_full_transcript: 1
conversations_flagged: 1
---

# Intercom CX Compliance Eval — Dry Run (sample of 10)

First live-data test of the pipeline in `IntercomEvaluator/CONTEXT.md`. Purpose was to check
whether the pipeline runs end-to-end and whether the criteria catch anything real — **not** to
produce a graded daily run. Grading is still gated (see § Blockers confirmed).

**Result: the pipeline works, it found a material breach on the first conversation assessed in
full, and it exposed six spec defects.**

## Method and its limits

- Pulled 10 conversations via `search_conversations` (`team_assignee_id: 5690482`,
  `source_type: email`). 4,443 match those filters in total.
- Ran Steps 1–5 (pull, exclude, preprocess, lane, authorisation) plus the deterministic triage
  over all 10.
- Ran **full-transcript content assessment on 1** — the highest-risk conversation by triage.
- The other 9 are **triaged, not assessed**. Nine `Pass` lines below would be unearned; they are
  reported as `not assessed` instead.

## Triage — all 10

| # | Conversation | Topic | Provider | User | Issue type | SLA | Parts | Triage |
|---|---|---|---|---|---|---|---|---|
| 1 | `215475238289349` | EE: Benefit - General | Smart Pension | Employee | Request / Change | hit | 51 | **ASSESSED — FAIL** |
| 2 | `215475247328292` | ER: Benefit - Pension | — | Employer | **Complaint / Escalation** | **missed** | 38 | High — complaints, ungradeable |
| 3 | `215475059251979` | — | Bupa | Employer | Question | **missed** | 117 | High — renewal |
| 4 | `215475334414810` | ER: Benefit - Pension | Irish Life | Employer | Question | hit | 41 | High |
| 5 | `215475333248118` | Benefit - Health | Freedom | Employer | Request / Change | hit | 36 | Medium |
| 6 | `215475212312217` | — | Smart Pension | Employer | Request / Change | **missed** | 47 | Medium — no topic set |
| 7 | `215475257104537` | ER: Billing & Finance | — | Employer | Question | **missed** | 48 | Low — billing |
| 8 | `215475348734758` | FinOps & Admin | — | Employer | Request / Change | active | 23 | Low |
| 9 | `215475218550022` | — | Bupa | Employee | Bug / Technical | **missed** | 113 | Low — technical |
| 10 | `215475348632123` | Benefit - Health | — | **Internal** | Other / Internal | hit | 30 | **EXCLUDED** — system notification (`noreply@kota.io`) |

Exclusion rule worked: #10 is an automated "[Needs Attention] An employee was deleted" notice
sitting inside the `PL-CX` ticket type, correctly dropped.

Triage prioritisation also worked — #1 was ranked highest on metadata alone (employee-authored,
pension scheme exit, named provider) and turned out to carry the breach.

---

## Conversation 1 — `215475238289349` — FAIL

**Subject**: Request to Leave Pension Scheme and Refund Contributions
**Inbound**: employee, personal email address, direct to `support@kota.io`
**Kota author**: **Michael Nikeenok** — **not on the MCC register** → fail-closed, unqualified
**Internal reviewer asked**: Claudia Correa — **script pathway, also unqualified**
**Bot**: Kota AI authored two customer-facing comments
**Lane**: 3-bespoke (and 1-fin for the bot closure)
**Permalink**: https://app.intercom.com/a/apps/euajb704/conversations/215475238289349
**Grade**: **Fail** — Grade 3/4, creates an Asana task

### Findings

| Criterion | Severity | Author | Verbatim (customer-facing, `part_id=50457227319`) |
|---|---|---|---|
| **HF-05 confirmed** | **High** | M. Nikeenok (unregistered) | "since you've been enrolled for less than two years, you're eligible to request a refund of your own contributions" |
| HF-10 | High | M. Nikeenok | "Preservation of benefits – you become a deferred member and the funds accumulated to date are held for you until retirement." |
| HF-12 | High | M. Nikeenok | "you can transfer your accumulated funds to a PRSA, a new employer's pension scheme, a personal retirement bond, or an overseas scheme" |
| HF-13 | Medium | M. Nikeenok | "(fees may apply depending on the option)" |
| HF-26 | High | Kota AI (bot) | "Everything on your request has been taken care of, so we'll go ahead and close the case." |

### Why HF-05 is confirmed rather than light

**The sent reply contradicts the author's own internal draft on the same fact.**

Internal note (`part_type: note`, never sent):
> "I've checked your enrollment date in our system, and it looks like you joined this pension
> scheme in June 2023. A refund of member contributions is only available if you've been in the
> scheme for less than two years, since you've been enrolled for just over three years, this
> option isn't available to you in this case."

Sent to the customer (`part_type: comment`):
> "since you've been enrolled for less than two years, you're eligible to request a refund of
> your own contributions."

One of these is wrong. If the June 2023 enrolment date in Kota's system is correct, the customer
has been told he qualifies for a short-service refund when he does not — a specific statement of
pensions law applied to a named individual, contradicting the firm's own record. He asked for that
refund and has been told he is eligible.

The rule cited is real (Irish short-service refund, under two years' qualifying service). The
**application to this member** is what fails. Per R3 this is HF-05 **confirmed**, not light: wrong
eligibility threshold applied to a specific person, with a material consequence.

### Mitigation on the record

> "We'd recommend seeking independent financial advice before deciding which option is right for
> you, as we're not able to advise on this ourselves."

Genuinely good — the inverse of SF-14, actively directing the customer to authorised advice. It
does **not** cure HF-10/HF-12, because information is itself a regulated activity under MCC 2017,
but it is real mitigation and belongs in the grade rationale.

### Supervision gap

The author asked **Claudia Correa** to review the reply. Claudia is script-pathway — unqualified.
An unqualified author asking an unqualified colleague to check regulated content produces no valid
sign-off. Neither person could authorise this content, and the contradiction survived the review.

### Note on the inbound message

The customer's opening email contains full name, DOB, home address, and mobile number, sent
unprompted to `support@kota.io`. Customer-initiated, so **not** an HF-06 breach by Kota. It does
confirm the redaction problem: this content cannot go into an Asana `Issues` field verbatim.

---

## Conversations 2–9 — not assessed

Triaged only. **#2 is the one to assess next**: platform-classified `Complaint / Escalation`,
pension topic, `sla_status: missed`, still open after 38 parts. It is exactly the HF-23/HF-24 case
— and exactly what cannot be graded yet.

---

## Blockers confirmed

| # | Blocker | Status after this run |
|---|---|---|
| 1 | Complaints deadlines unverified | **Still blocking.** #2 is a live complaint with a missed SLA and cannot be graded. Highest-priority Researcher task |
| 2 | Internal notes vs customer replies | **RESOLVED** — `part_type` is `note` (internal) vs `comment` (customer-facing). Reliable, and it worked first time |
| 3 | MCC register coverage for CX staff | **Confirmed as a real gap.** Michael Nikeenok is not on the register; nor is any Kota AI entry. Compliance must add CX staff or every CX conversation fails closed |
| 4 | CX / CS team ID list | Partially resolved — `5690482` = `PL: CX Platform- Customer`. Other CS teams still unenumerated |

---

## Spec defects found

Six, four of which would have caused wrong results in production.

**1. "Fin is dormant in CX" was wrong — HF-25/26 are live.**
`ai_agent_participated: true` on **10/10**, and Kota AI authored customer-facing comments. The
earlier dormant call came from two chat conversations and did not generalise. Two conversations is
not a basis for a scope conclusion.

**2. Kota staff appear as `author.type: user` — false-negative risk.**
Conversations 7 and 8 are authored by `user / paul.ohanlon@kota.io` and `user / simon@kota.io`.
Paul O'Hanlon is on the register as fully qualified (QFA & APA PMI). The rule "only `admin` parts
are Kota conduct" would silently skip Kota staff content. **Fix: resolve identity by email domain,
not by `author.type` alone.**

**3. `Brand` and `ticket_type` can disagree — no precedence rule.**
Conversation 9 is `Brand: Kota: BenOps` but `ticket_type: PL-CX: Customer Ticket` on the CX team.
The spec says filter on brand *and* team *and* ticket type without saying which wins. **Fix:
`team_assignee_id` + `ticket_type` govern; `Brand` is advisory.**

**4. `PL:Topic` is unset on 3/10 — topic filtering has holes.**
HF-26's regulated-topic filter depends on it. **Fix: unset topic must fail closed (assess), never
skip.**

**5. Internal notes must be read as context, not merely excluded.**
The HF-05 finding was **only** visible by comparing the unsent note against the sent comment.
Excluding notes from *grading* is right; excluding them from *reading* would have hidden the
strongest finding in the sample.

**6. Both proposed new criteria below came out of one conversation.**

---

## Proposed new criteria

Continuing the shared sequence. Researcher to confirm before use.

**HF-27 — Draft/sent divergence on a regulated-product fact.** An internal draft and the sent
reply state materially different facts about the same regulated matter. Evidences that the firm
held the correct position and communicated the incorrect one — which is worse than a simple error,
because the record shows the author knew better. Detected by diffing `note` against subsequent
`comment` content by the same author.

**HF-28 — Regulated content reviewed by an unqualified colleague.** A request for review or
sign-off on regulated-product content, directed to someone who is script-pathway, unregistered, or
absent from the register. Creates the appearance of supervision without its substance. Detected on
`note` parts containing a review request plus an @-mention or named colleague.

Both are `applies_to: intercom` initially. HF-27 likely generalises to email once drafts are
visible there; HF-28 does not apply to calls.

---

## Findings withdrawn after reassessment

Per R5 — mandatory section.

| Conversation | Original finding | Why withdrawn | Reassessment date |
|---|---|---|---|
| _(none — first run)_ | | | |

---

## Open questions for the Designer

1. **`part_type` filtering must be explicit in the prompt.** The distinction carried the whole
   assessment. It should not be left implicit.
2. **How should bot closures grade?** Kota AI asserting "everything has been taken care of" on a
   conversation containing a material error is HF-26, but the bot did not author the error.
   Recommend: grade on the conversation, route to systemic (ES-05), do not coach the human for the
   bot's line.
3. **Payload size is a real constraint.** A 10-conversation search exceeded the context limit, and
   a single 51-part conversation was 65KB. The runtime must extract fields server-side rather than
   loading whole conversations. Conversations 3 and 9 run to 117 and 113 parts.
4. **Does the mitigation disclaimer affect the grade?** "We're not able to advise on this
   ourselves" is the criteria's own negative-example pattern, yet the same reply breaches HF-10 and
   HF-12. Recommend it moves the grade within Fail rather than out of it — but that is Compliance's
   call, and it will recur constantly in CX.
