---
title: Detection Criteria — Intercom Monitoring Agent v1
created: 2026-08-04
updated: 2026-08-05
type: requirements
channel: intercom
derived_from:
  - Researcher/req-detection-criteria.md
  - Researcher/req-email-detection-criteria.md
  - Researcher/research-mcc-fitness-probity.md
status: active
---

# Detection Criteria — Intercom Monitoring Agent v1

What the Intercom monitoring agent must detect. Like the email criteria, this is a **delta**
— it adds what is specific to Intercom and references rather than repeats what is already
defined for calls and email.

Read in this order: `req-detection-criteria.md` (the base) → `req-email-detection-criteria.md`
(written-medium rules) → this document.

## Population in scope

**Customer Service / CX only.** Established by direct inspection of the connector on 2026-08-04:

| Attribute | In scope | Out of scope |
|---|---|---|
| `Brand` | `Kota` | `Kota: BenOps` |
| Team | `PL: CX Platform- Customer` (and other `PL:` CX/CS teams) | `BenOps: *` |
| Ticket type | `PL-CX: Customer Ticket` | `BenOps: Client, Customer & Provider` |
| Route in | `support@kota.io` + in-app live chat | `benops@kota.io` |
| Product line | Platform (`PL`) | Embed |

**Both source types are in scope**: `source_type: conversation` (in-app chat) and
`source_type: email` (mail to `support@kota.io`). They land in the same `PL-CX` ticket type and are
the same conduct in two media — brand and team scope this channel, not source type.

> [!warning] Precedence rule — these attributes disagree
> The dry run found a conversation tagged `Brand: Kota: BenOps` while carrying
> `ticket_type: PL-CX: Customer Ticket` on the CX team. **`team_assignee_id` and `ticket_type`
> govern; `Brand` is advisory.** Where they conflict, treat the conversation as CX and note the
> discrepancy — a mis-branded conversation is still CX conduct, and excluding on brand alone would
> drop real traffic.

> [!warning] `PL:Topic` is unreliable — fail closed
> Unset on 3 of 10 sampled conversations. Any topic-based filter (notably HF-26's regulated-topic
> gate) must **assess** when the topic is unknown, never skip. An absent topic is missing metadata,
> not evidence that a conversation is unregulated.

**BenOps / Embed is explicitly out of scope** (Compliance direction, 2026-08-04). It is the
larger population — 31,483 email-sourced conversations against 3,523 for CX — but it is a
specialist operations function dealing with partner support desks, and monitoring priority sits
with the customer-facing functions instead.

### Why CX is the right target

- **Access already works.** App-level integration, not a personal mailbox grant. The
  domain-delegation blocker that stops the email channel does not apply, so this channel is
  buildable now.
- **`support@kota.io` routes here, not into Gmail.** Customer service email *is* this channel.
  `EmailEvaluator/` is therefore effectively the sales/GTM channel.
- **Direct retail-customer contact.** Sampled authors include an employer contact and an
  individual employee on a personal address, with `Type of user: Employer | Employee`. No
  partner intermediary. These are Kota's retail customers, so the MCC perimeter applies without
  qualification — see Resolved question 1 below.
- **Regulated-product subject matter, already classified.** `PL:Topic: "ER: Benefit - General"`,
  `Provider: Irish Life`. The platform's own topic taxonomy identifies the regulated
  conversations for free.
- **CX staff are unlikely to hold MCC qualifications**, and they are answering product questions
  from customers directly. Check the register rather than assuming.
- **Complaints and vulnerability signals land here first**, not on calls or in sales email.

## Scope decisions taken

Recorded so they are visible as decisions rather than oversights:

| Decision | Rationale |
|---|---|
| **CX / CS only; BenOps excluded** | Compliance direction. Monitoring priority is the customer-facing functions — sales, customer service, customer success |
| **Complaints handling is in scope** — new criteria below | Complaints arrive here and there is no existing detection for them in any channel |
| **Automated-agent conduct is in scope and live** | Corrected 2026-08-04. An earlier draft called it dormant off two chat conversations; the 10-conversation email sample shows `ai_agent_participated: true` on **10/10**, with the bot ("Kota AI") authoring customer-facing replies including case closures. HF-25/26 are live criteria |
| **No dedicated special-category-data criterion** | HF-06 already covers personal data including health, and applies here unchanged |
| **No partner-mediated-communication criterion** | Conduct attributes to the **Kota-side author** regardless of counterparty. Largely moot now that BenOps is out of scope — CX contact is direct |
| **Intercom platform notifications remain excluded** | Transactional noise — unchanged from the email criteria |

## What is structurally different from email

| Dimension | Email | Intercom |
|---|---|---|
| Unit of analysis | Message, in thread context | **Conversation** (`conversation_parts`) — closer to a call transcript than to a message |
| Identity | `From:` header | `admin_id` / teammate ID → map to the MCC register. Also authenticated, and additionally gives **team** and **brand** |
| Template analogue | HubSpot template / sequence | **Saved replies / macros**, plus **Fin content sources** (help-centre Articles) |
| Automation | Sequences (HF-18) | **Fin AI agent** — answers rather than merely sends, which is a different and larger risk |
| Footer / signature | Present (HF-20) | Largely absent in chat; present on email-delivered replies. HF-20 applies only to the latter |
| Free metadata | Little | Rich — `ticket_type`, `state`, `sla_applied`, `PL: Issue Type`, `PL:Topic`, `Provider`, `Type of user`, `ai_agent_resolution_state`. **Much of the triage is free** |

### Metadata is a first-class input
Unlike Fireflies or Gmail, Intercom hands over structured classification with every
conversation. `PL: Issue Type: Complaint / Escalation`, `sla_status: missed`, and
`Fin AI Agent resolution state` are directly usable — they make several detections below
deterministic rather than model-judged. Use them; do not re-derive by inference what the
platform already asserts.

---

## Three lanes

| Lane | Population | Assessment |
|---|---|---|
| `1-fin` | Fin authored a substantive `comment` | Assess the **Fin turn** against HF-25/HF-26 — a permanently unqualified speaker. **Common in CX** — present in 10/10 sampled conversations |
| `2-macro` | Reply matches an approved saved reply / macro | Documented pass on hash match; delta → Lane 3 (HF-16 applies unchanged) |
| `3-bespoke` | Free-text human reply | Full detection run. **The main lane for this channel** |

Lane 2 reuses the email template-register mechanism and normalisation rules verbatim
(`research-approved-email-templates.md`). Macros are registered in the same file, distinguished
by `sending_tool: intercom-macro`.

---

## Preprocessing

The email preprocessing steps apply, with three changes:

1. **Split on `part_type` before anything else** — `comment` is customer-facing, `note` is an
   internal teammate note. **Only `comment` parts are graded.** Confirmed working on live data
   2026-08-04. Ignore the remaining part types (`assignment`, `close`, `snoozed`,
   `conversation_attribute_updated_by_admin`, `operator_workflow_event`, and similar) — they are
   state changes, not communication.

   **But `note` parts must still be *read* as context.** The strongest finding in the dry run —
   an HF-05 confirmed — was only visible by comparing an unsent internal draft against the sent
   reply. Excluding notes from grading is correct; excluding them from reading would have hidden
   it. See HF-27.

2. **Resolve identity by email domain, not by `author.type`.** Kota staff appear as
   `author.type: user` when they are recorded as a contact — the dry run found conversations
   authored by `user / paul.ohanlon@kota.io` and `user / simon@kota.io`, and Paul O'Hanlon is a
   registered QFA holder. **Treating `admin` as the only Kota conduct silently skips staff
   content.** Rule: any `@kota.io` author is Kota conduct regardless of `author.type`; `bot` is
   always unqualified; everyone else is the customer.

3. **Ticket-body scraping** — the initial message may arrive as a structured form dump (ticket ID,
   country, provider, product, free-text details). Parse the **free-text detail field** separately;
   form fields are not authored prose.

4. **Author-type routing is mandatory** — every finding records `admin` / `bot` / `user`, plus the
   resolved MCC status for Kota authors.

---

## Criteria carried over

All `applies_to: both` criteria from the call document apply, plus the written-medium rules
from the email document. Specifically unchanged: **HF-00** through **HF-15**, **SF-10**–**SF-15**,
**HF-06** (personal data — expect frequent firing given health data volume), **HF-16**
(macro drift), **HF-19** (missing disclosure), **HF-21** (misdirected recipient),
**HF-22** (outward forwarding), **SF-16**, **SF-17**, and calibration rules **R1–R7**.

**HF-20** (regulatory footer) applies **only** to email-delivered Intercom replies, not to
in-app chat, where no footer is expected.

**HF-18** (sequence ignoring vulnerability signal) applies to Intercom **Series** exactly as
written for HubSpot sequences.

`applies_to` for every criterion below is `intercom` unless stated.

---

## New — Complaints handling

> [!note] Deadlines now populated — `research-complaints-handling.md` (2026-08-04)
> HF-23 and HF-24 are gradeable. Day counts are sourced from CBI guidance, firms' published CPC
> complaints procedures, and the FCA Handbook, and are consistent across independent sources.
> **Not yet line-checked against the CPC 2025 statutory text (S.I. 81/2025)** — see that note's
> confidence caveat before any regulator-facing escalation.

### HF-23 — Complaint not recognised or logged as a complaint
**Priority: High**

**Description**: The customer expresses dissatisfaction meeting the regulatory definition of a
complaint, and the conversation is not classified, tagged, or routed as one. The obligation
attaches to the **substance** of what the customer said, not to whether they used the word.

**Why High**: An unlogged complaint is invisible to every downstream control — the complaints
register, the timeline obligations, the root-cause analysis, and the complaints data that
Delegated Regulation 2017/2358 Art. 10 requires distributors to feed back to manufacturers. One
missed classification defeats all of them at once.

**Trigger logic**:
- Detect complaint substance in `user`-authored parts: explicit ("I am writing to formally raise
  a complaint", "please treat this as a formal complaint"), or implicit (unresolved issue over
  an extended period, dissatisfaction with service or outcome, a request for escalation or
  formal review).
- Cross-check the platform's own classification — `PL: Issue Type`, ticket type, tags.
- Substance present **and** classification absent → flag.

**Positive example**: customer asks that the matter be treated as a formal complaint and for the
escalation process; conversation remains typed as a routine request.
**Negative example**: same message, classified `Complaint / Escalation` and routed accordingly.

**Regulation / risk mapping**:
- CPC 2025 — complaints-handling requirements (*specific part and definition to verify*)
- FCA **DISP** — complaint definition and handling obligations (*specific section to verify*)
- Delegated Regulation (EU) 2017/2358 Art. 10 — distributor obligation to share complaints data
  with manufacturers. See [[Product Governance]]
- CBI Standards for Business — act fairly and professionally

**Note**: partially deterministic. Where the platform has *already* classified a conversation as
a complaint, that is ground truth — no inference needed. The detection is for the cases where it
has not.

---

### HF-24 — Complaint acknowledgement or resolution outside the required timeline
**Priority: High**

**Description**: A conversation recognised as a complaint breaches an acknowledgement, update,
or final-response deadline.

**Why High**: These are absolute, dated obligations rather than judgement calls — the most
mechanically checkable criteria in any of the three channels. Intercom supplies every timestamp
needed (`first_admin_reply_at`, `last_admin_reply_at`, `first_close_at`) plus its own
`sla_applied` / `sla_status`.

**Trigger logic**:
- For any conversation classified as a complaint (by the platform or by HF-23), compute elapsed
  time to acknowledgement, to each update, and to final response.
- Compare against the regulatory deadlines:

  | Stage | Ireland (CPC) | UK (FCA DISP) |
  |---|---|---|
  | Written acknowledgement | **5 business days** | **Prompt** (no fixed count) |
  | Electronic complaint (chat / email) | **Immediate**, same medium | — |
  | Regular written update | every **20 business days** from receipt | keep complainant informed |
  | Final response / resolution | **40 business days** | **8 weeks** |
  | Ombudsman signposting | FSPO, on final response | FOS, on final response |

- Flag any breach. Route by activity: Irish activity → CPC clock; UK activity → DISP clock. Where
  the applicable regime is unclear, apply the **stricter** deadline and note the ambiguity.
- Report the platform's own `sla_status` alongside, but **never substitute it**. The sampled CX SLA
  (`FRT 8h / NRT 8h / TTR 24h`) is far tighter than the CPC deadlines, so `missed` does **not**
  imply a regulatory breach — and `hit` does **not** imply compliance, because the SLA measures
  first response, not acknowledgement-as-a-complaint or final response. **This is the most likely
  source of HF-24 false positives.**

**Positive example**: complaint acknowledged well outside the required window, `sla_status: missed`.
**Negative example**: acknowledged within the window, updates issued on schedule.

**Regulation / risk mapping**: CPC 2025 complaints handling (*deadlines to verify*);
FCA DISP 1 (*deadlines to verify*); FCA Consumer Duty (PRIN 2A) — consumer support.

---

### SF-18 — Unacknowledged dissatisfaction below the complaint threshold
**Soft signal**

**Description**: Dissatisfaction that does not meet the complaint definition, closed out without
acknowledgement.

**Why Soft**: individually a service-quality matter, not a breach. A pattern is a Consumer Duty
concern and a product-governance signal (complaints data being a required POG input). Flag at
N≥2 in a conversation, or on a recurring pattern for one teammate or topic.

**Regulation / risk mapping**: FCA PRIN 2A; CPC 2025 Standards for Business;
Delegated Reg. 2017/2358 Art. 10.

---

## New — Automated agent (Fin) conduct

> [!important] Live in CX — corrected 2026-08-04
> An earlier draft marked these dormant on the basis of two chat conversations showing
> `ai_agent_participated: false`. **That did not generalise.** The 10-conversation email dry run
> found `ai_agent_participated: true` on **10/10**, with the bot ("Kota AI") authoring
> customer-facing `comment` parts including case-closure assertions. HF-25 and HF-26 are live
> criteria in this channel, not contingency ones.
>
> "Kota AI" is not on the MCC register and cannot be. Every regulated-product answer it gives is
> unqualified by construction.

### HF-25 — Automated agent providing regulated-product information or advice
**Priority: High**

**Description**: Fin (or any automated agent) answers a customer question about a regulated
product — cover, exclusions, eligibility, premiums, claims mechanics, contribution rules,
comparisons, or suitability.

**Why High**: This is **HF-00 with the fail-closed default permanently engaged**. Under MCC 2017,
*information* on a retail financial product is a regulated activity requiring a qualified person.
An automated agent is not on the MCC register and cannot be — there is no route by which it
becomes qualified. Every regulated-product answer it gives is therefore outside authorisation, at
machine scale and without the mitigations a human turn carries (hedging, escalation instinct,
recognising confusion).

The R7 learner/observer carve-out **does not apply**. Fin is not observing or researching; its
output goes directly to the customer as an answer.

**Trigger logic**:
- Identify parts where `author.type == bot`, or `ai_agent_participated == true` with
  `ai_agent.last_answer_type` indicating an answer was given.
- Classify the answer against the four MCC product families.
- Any regulated-product content → flag. No qualification lookup required; the answer is
  unqualified by construction.
- Record `ai_agent.content_sources` — the Article the answer derived from is the **root cause**,
  and fixing the Article fixes every future instance. See LIB-07.

**Positive example**: Fin answers a customer asking whether a named therapy provider is covered
under their EAP benefit.
**Negative example**: Fin replies that it cannot answer benefit-cover questions and routes to the
Benefits team, adding no product content.

**Regulation / risk mapping**:
- MCC 2017 — information on a retail financial product is a regulated activity
- CPC 2025 Part 3 — clear, fair, accurate, not misleading
- IDD Art. 17(2)
- FCA Consumer Duty (PRIN 2A) — consumer understanding
- Kota internal: `Financial Product Information to Customers`

**Routing**: **ES-05 (systemic)**, always. A Fin answer is never an individual coaching finding —
no human made a judgement call. Route to whoever owns Fin's configuration and content sources.

---

### HF-26 — Automated resolution of a regulated-product conversation without qualified human review
**Priority: High**

**Description**: A conversation on a regulated-product topic is closed with
`ai_agent_resolution_state: resolved` (or equivalent) and **no qualified human ever participated**.

**Why High**: Distinct from HF-25. HF-25 is about what Fin *said*; this is about the absence of a
qualified human anywhere in the loop. Even a correct answer leaves the firm unable to evidence
that a qualified person conducted the regulated activity — which is what the MCC and F&P regimes
require. It is an evidencing failure as much as a conduct one, and it is invisible in any per-message
review because the finding is a *negative*: something that never happened.

**Trigger logic**:
- Filter conversations on a regulated-product topic (use `PL:Topic` and `Provider` where set — e.g. `ER: Benefit - General` with a named provider; exclude `EE: Technical Issues`).
- Check whether any participating `admin` is qualified for that product per the register.
- Resolution state `resolved` **and** no qualified participant → flag.
- Escalation to a qualified human → not a finding. Escalation to an unqualified human → HF-00 on
  that human, assessed normally.

**Positive example**: eligibility question answered by Fin, marked resolved, no Benefits teammate
ever in the conversation.
**Negative example**: Fin gathers context, escalates to a QFA holder, who answers.

**Regulation / risk mapping**: MCC 2017 — qualification requirement and the firm's obligation to
evidence it; Fitness & Probity (S.I. 60/2011 + IAF 2024); FCA SYSC 28.

**Routing**: ES-05 (systemic).

---

### SF-19 — Automated agent answered before escalating
**Soft signal**

**Description**: Fin gave a substantive answer and *then* escalated. The escalation is correct, but
the customer already has the unqualified answer.

**Why Soft**: escalation shows the control partly worked. It is not a clean pass, because a
subsequent correct answer does not retract the first one — and the customer may act on either.
Promotes to **hard** (HF-25) where the pre-escalation answer contained regulated-product content.

**Trigger logic**: `resolution_state: escalated` **and** a substantive `bot`-authored answer
precedes the escalation. Distinguish from escalation via a workflow rule with no answer given —
the sampled conversations show `source_type: workflow` escalations that gave no answer at all, and
those are clean.

---

## New — proposed from the 2026-08-04 dry run

Both emerged from a single conversation in the 2026-08-04 dry run; see
`IntercomEvaluator/eval-intercom-2026-08-04-daily.md` for the source evidence. **Live as of
2026-08-05** — grounded in observed conduct rather than hypothesised risk, which is the same
evidentiary basis as the HF-00–HF-15 series.

### HF-27 — Draft/sent divergence on a regulated-product fact
**Priority: High**

**Description**: An internal draft (`note`) and the sent reply (`comment`) state materially
different facts about the same regulated matter.

**Why High**: worse than a simple error. The record shows the firm held the correct position
internally and communicated the incorrect one — so it is not a knowledge gap but a control failure,
and it is far harder to defend to a regulator.

**Trigger logic**: diff `note` content against subsequent `comment` content by the same author on
the same regulated fact. Flag material divergence — eligibility, figures, entitlement, timing.
Ignore tone and length differences.

**Observed instance**: draft stated a member had been enrolled "just over three years" and was
therefore **not** eligible for a short-service contribution refund; the sent reply stated they had
been enrolled "less than two years" and **were** eligible. See the eval report for verbatim.

**Regulation / risk mapping**: CPC 2025 Part 3 (clear, fair, accurate, not misleading); MCC 2017;
CBI Standards for Business — due skill, care and diligence.

### HF-28 — Regulated content reviewed by an unqualified colleague
**Priority: Medium-High**

**Description**: A request for review or sign-off on regulated-product content, directed to someone
who is script-pathway, unregistered, or absent from the register.

**Why Medium-High**: creates the appearance of supervision without its substance. In the observed
instance the review request did not catch a material contradiction, because the reviewer was no more
qualified than the author. Under MCC the supervisory relationship only means something if the
supervisor holds the relevant qualification.

**Trigger logic**: detect review/sign-off requests in `note` parts ("can you check", "please
review", "@name thoughts?"), resolve the named colleague against the register, flag if they are not
qualified for the product in question.

**Observed instance**: an unregistered author asked a script-pathway colleague to check a reply
containing pension transfer and refund-eligibility content.

**Regulation / risk mapping**: MCC 2017 — supervision requirements for script-pathway staff;
Fitness & Probity (S.I. 60/2011 + IAF 2024) — competence and capability; FCA SYSC 28.

### SF-20 — Customer attributes advice or a recommendation to Kota staff
**Soft signal** · *added from the 2026-08-05 run*

**Description**: A `user`-authored part states that a Kota staff member advised, suggested, or
recommended something on a regulated-product matter.

**Why Soft, and why it matters anyway**: this is **not a finding against the staff member** — R1
requires that a finding cite Kota-authored text, and a customer's characterisation is not that.
But it is strong evidence that regulated conduct occurred **somewhere the agent cannot see**: a
call, a linked conversation, or direct email. Without this signal that conduct is invisible.

**Trigger families**: "as you suggested", "as advised", "you recommended", "you told me to",
"per your advice", "[name] said I should" — naming a Kota staff member, on a regulated-product
matter.

**Observed instance** (`215475247328292`): customer wrote "Claudia has reviewed the Clonbio Group
contributions, and I have made the necessary changes to Kota for August **as she suggested**".
Claudia Correa is script-pathway. Contribution changes are HF-12 territory, but the underlying
communication is not in the assessed artefact.

**Action**: "Refer to compliance" for a cross-channel look — check calls and email for the same
staff member and customer in the surrounding period. Escalate if the named person is unqualified
for the product. **Never** coach on the customer's wording alone.

**Regulation / risk mapping**: MCC 2017; CPC 2025 Part 3. Evidentiary rather than substantive —
it establishes that a regulated activity may have occurred, not that it breached.

---

## Linked and split conversations

> [!warning] Open gap — a Pass on a fragment is provisional
> CX conversations get cross-referenced and handling moves between them. The 2026-08-05 run found a
> conversation whose internal note read "This is managed here: 119503246" — the substantive handling
> had moved elsewhere, so the assessment graded a **fragment** and returned Pass.
>
> Two mechanisms, neither yet implemented:
> 1. **`linked_objects`** — structured, present on the conversation object. Follow it.
> 2. **Free-text conversation-ID references in notes** — unstructured. Parse notes for bare
>    conversation IDs and follow them.
>
> Until both exist, a Pass on a conversation containing an outbound reference must be reported as
> **Pass-with-comments — linked set not assessed**, never a clean Pass. Assess a linked set as one
> unit once implemented.

---

## Content-governance findings — `LIB-07` onward

Extends the email `LIB-*` series. These are findings against the **content layer**, not against
any conversation, and they surface in a periodic audit rather than a daily run.

| ID | Finding | Why it matters |
|---|---|---|
| `LIB-07` | Help-centre Article describing a regulated product, never compliance-reviewed | Published customer-facing product information at scale |
| `LIB-08` | Article used as a Fin content source containing a criterion breach | **The root cause of HF-25.** One bad Article becomes every future wrong answer |
| `LIB-09` | Article approved against a superseded version of the detection criteria | Approval no longer means what it meant |
| `LIB-10` | Regulated-product Article with no named approver or approval date | Approval unevidenced |
| `LIB-11` | Fin configured to answer on a regulated-product topic with no escalation rule | Systemic HF-25 generator |
| `LIB-12` | Saved reply / macro containing a criterion breach | One breach replicated across every use |

**`LIB-08` and `LIB-11` are the highest-leverage findings in this document.** Fin's answers derive
from its content sources, so auditing a bounded Article library and the escalation rules prevents
breaches that per-conversation monitoring can only detect after they have reached customers.

The Article library is enumerable via the connector, so this audit is achievable now — unlike the
email template register, which is blocked on GTM Ops supplying an inventory.

---

## Escalation triggers

ES-01, ES-02, ES-03 apply unchanged. ES-04 (data breach) and ES-05 (systemic) apply as defined in
the email criteria, with two notes:

- **ES-01 will fire far more often here** than on calls or in GTM email. Health, bereavement,
  financial difficulty, and distress are routine in a benefits support queue. Expect volume, and
  do not tune it down — the correct response is triage capacity, not a higher threshold.
- **ES-02 overlaps HF-23.** A complaint reference is both an escalation trigger and a
  classification obligation. Fire both: the escalation gets it to a human, HF-23 gets it into the
  complaints register. One does not substitute for the other.

---

## Anticipated false-positive families

Predicted; confirm against the first live runs and write up as
`IntercomEvaluator/calibration-<date>-intercom-false-positives.md`.

1. **Form-dump fields assessed as authored prose** — the structured ticket header (provider,
   product, country) is not a statement by anyone. Preprocessing step 2.
2. **Customer statements attributed to Kota.** CX conversations are opened by employers and
   employees who describe their own cover, quote figures back, and speculate about eligibility.
   `user` parts are **never** Kota conduct. This is the dominant risk in this channel — the direct
   analogue of email's quoted-history problem, though `conversation_parts` make it structurally
   avoidable.
3. **Provider quotes relayed by Kota staff** — a teammate quoting the insurer's answer verbatim is
   pass-through, closer to the MCC brochure carve-out than to advice. Needs a calibration rule;
   expect to get this wrong initially.
4. **Platform support answered as product questions.** A large share of CX traffic is genuinely
   technical — login failures, sync errors, missing access (`PL:Topic: "EE: Technical Issues"`).
   Platform mechanics are not regulated. Do not let a `Provider` attribute on the conversation
   pull a technical exchange into product scope.
5. **Fin workflow escalations with no answer given** — clean, per SF-19.
6. **Internal notes** — Intercom notes are teammate-to-teammate, not customer-facing. Confirm the
   API distinguishes notes from replies before assessing any part; if it does not, that is a
   blocking gap, because internal candour would otherwise be graded as customer communication.

---

## Out of scope for v1

- **BenOps / Embed** — `Brand: Kota: BenOps`, `benops@kota.io`, `BenOps: *` teams. The larger
  population, deliberately excluded. Criteria would apply if it is ever brought in scope.
- **Phone, SMS, WhatsApp, social** source types.
- **Inbound content as a graded population** — assessed for ES-01/ES-02 and context only.
- **Attachment contents beyond text extraction** — an unparseable attachment is an evidencing gap,
  not a pass.
- **Non-English conversations** — `Language` attribute is available; escalate per ES-03.

---

## Output requirements

As for email, plus:

1. **`channel`** — `intercom`
2. **`lane`** — `1-fin` | `2-macro` | `3-bespoke` | `content-audit`
3. **`conversation_id`** and the `ticket.url` permalink (`https://app.intercom.com/a/apps/.../conversations/<id>`)
4. **`part_id`** — the specific conversation part the finding attaches to
5. **`author_type`** — `admin` | `bot` | `user`, and for `admin` the resolved MCC status
6. **`fin_content_source`** — where the finding is HF-25, the Article the answer derived from.
   Without this the root cause cannot be fixed and the same wrong answer recurs indefinitely
7. **Platform classification** — `PL: Issue Type`, `ticket_type`, `sla_status`, and
   `ai_agent_resolution_state`, carried through so a reviewer can see what the platform already knew

---

## Dependencies

| # | Dependency | Owner | Blocking? |
|---|---|---|---|
| 1 | ~~Complaints-handling deadlines~~ — **RESOLVED 2026-08-04**, see `research-complaints-handling.md`. Residual: line-check against S.I. 81/2025 before regulator-facing escalation | Researcher | No |
| 2 | ~~Internal notes vs customer-facing replies~~ — **RESOLVED 2026-08-04**. `part_type` is `note` vs `comment`, verified on live data | Designer | No |
| 3 | **MCC register coverage for CX / CS teammates.** The existing register is oriented to GTM and Benefits; CX staff may be absent entirely, in which case fail-closed makes every conversation a finding — noise rather than signal | Researcher + Compliance | **Yes** |
| 4 | **CX / CS team ID list**, mapped to Asana department sections. Needed to scope the pull and route the output | Researcher + CS Ops | **Yes** |
| 5 | **Who owns Fin's configuration and content sources?** ES-05 routing has no destination without a named owner. **Now urgent** — Fin is active in CX and authoring customer-facing replies | Compliance | **Yes, before first HF-25** |
| 5 | **Macro / saved-reply inventory** — Lane 2 gate | GTM Ops / CS Ops | No — degrades to all-Lane-3 |
| 6 | **Lawful basis.** Lighter than mailbox monitoring (this is a firm system of record for customer service, not personal correspondence), but the monitoring notice should still cover it | Compliance | Confirm before live run |
| 7 | **Asana destination** — same open question as email | Compliance | Yes, to file tasks |

Shared and **read-only** from this workspace: `research-mcc-fitness-probity.md`,
`source-of-truth-ae-myfuturefund.md`, `research-approved-email-templates.md`.

---

## Resolved

1. **Retail-customer perimeter — resolved in favour of full MCC application.** CX conversations are
   between Kota and its own customers directly: employer contacts and individual employees, the
   latter on personal email addresses (`Type of user: Employer | Employee`). No partner
   intermediary. An employee asking about their own pension or health cover is a retail customer
   receiving information about a retail financial product, so the HF-00 family applies without
   qualification. This was an open question while BenOps was in scope; excluding BenOps removes it.

## Open questions

1. **Which teams beyond `PL: CX Platform- Customer` count as CS / Customer Success?** The Asana
   project has separate Go-to-Market, Customer Success, and Benefits sections, so the department
   split already exists downstream. The Intercom team list needs enumerating and mapping to those
   sections, or routing will guess.
2. **What is Fin actually permitted to answer in CX?** Resolved that it *is* active (10/10 sampled).
   Open question is its topic perimeter: the cleanest control is preventing Fin from answering on
   regulated-product topics at all rather than detecting bad answers afterwards. Establish whether
   that is configurable before investing further in HF-25 detection.
3. **Retrospective scope.** 3,523 CX conversations exist, many long-running and still open (sampled
   conversations ran to 54 and 90 parts). Does monitoring start from go-live, or is there a
   backward-looking review? Unlogged complaints and unactioned vulnerability signals may be sitting
   in the open and closed sets.
4. **Are sales conversations also in Intercom?** The `SDR Success Counted` custom attribute appears
   on CX conversations, which suggests some sales-qualified traffic passes through. If inbound sales
   conversations land here rather than only in HubSpot, part of the sales population is reachable
   now instead of waiting on mailbox access. Worth checking before investing in the email channel.
