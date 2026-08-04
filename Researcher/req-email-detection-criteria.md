---
title: Detection Criteria — Email Monitoring Agent v1
created: 2026-08-04
updated: 2026-08-04
type: requirements
channel: email
derived_from:
  - Researcher/req-detection-criteria.md
  - Researcher/research-mcc-fitness-probity.md
  - Researcher/research-prescribed-scripts.md
status: draft
---

# Detection Criteria — Email Monitoring Agent v1

What the email monitoring agent must detect. This document is a **delta** against
`Researcher/req-detection-criteria.md` (the call criteria), not a replacement. The call
criteria remain in force for the call channel and are unchanged by this document.

Read this document alongside the call criteria, not instead of it. Anything not stated
here follows the call criteria.

## Relationship to the call criteria — shared ID space

Criterion IDs are a **single shared space across channels**. `HF-01` means the same thing
in an email as it does on a call. Every criterion carries an `applies_to` value:

| Value | Meaning |
|---|---|
| `both` | Detected in calls and email, same substance |
| `call` | Call channel only |
| `email` | Email channel only |

The reason for one space rather than a parallel `EF-` series: Compliance needs to be able
to ask "all HF-01 breaches this quarter, all channels" without reconciling two taxonomies.
Channel is an attribute of the finding, not of the rule.

New email-only hard rules continue the existing numbering from **HF-16**. New email-only
soft signals continue from **SF-16**. No existing ID is redefined, renumbered, or retired.

## Master frame — same anchor, one addition

The regulatory anchor is unchanged: **CBI Minimum Competency Code 2017**, the **Fitness &
Probity** regime (S.I. 60/2011 + IAF 2024) for IE staff, **FCA SYSC 28 + SM&CR** for UK
staff. Information remains a regulated activity, not just advice. Speaker identity remains
an input, and the agent still **fails closed** on unrecognised senders.

One addition specific to this channel:

**Writing is durable, forwardable, and attributable to the firm.** A sentence in an email
differs from the same sentence on a call in four ways that matter to a regulator:

1. The customer **keeps** it and can rely on it indefinitely.
2. It was **reviewable before sending** — the "spoke off the cuff" mitigation is unavailable.
3. It carries the firm's identity — domain, signature block, regulatory footer — so it reads
   as a **firm communication**, not one person's remark.
4. It can constitute a **financial promotion** in a way speech generally does not
   (FSMA s. 21 and FCA COBS 4 for UK activity; CPC 2025 advertising requirements for Irish
   activity — *specific CPC part to be confirmed by Researcher against the source text*).

> [!important] Grading decision required
> Consequence 2 and 3 imply that an identical breach may warrant a higher grade in email
> than on a call. **This document does not decide that.** It is a Compliance decision
> (Sola Olaniyan + Trevor Gardiner) and must be recorded explicitly in
> `Evaluator/spec-email-eval-daily-run.md` before the first live run. Leaving it implicit
> means two channels grading the same conduct differently by accident rather than by policy.

---

## Two-lane architecture

Email volume is dominated by templated and HubSpot-sequenced sends. Those are not assessed
the same way as bespoke human mail, because the risk sits in a different place.

### Lane 1 — Automated / templated sends
**Unit of analysis**: the **template version**, not the message.
**Cadence**: at template approval and at every template change — *not* daily per-send.
**Rationale**: a non-compliant template is one breach replicated N times. Reviewing 400
sends of the same approved copy produces 400 identical findings and no new information.
**Mechanism**: normalise and hash the message body; match against the approved-template
register (`Researcher/research-approved-email-templates.md` — to be created). A clean hash
match against an approved, in-date template is a **documented pass**, not an unassessed gap.

### Lane 2 — Bespoke human mail
**Unit of analysis**: the message, assessed in thread context.
**Cadence**: daily, directly analogous to the call eval run.
**Population**: anything that is not a clean match to an approved template — including
**partial** matches (see HF-16).

### Lane routing is deterministic, and that matters
Lane assignment is a hash comparison, not a model judgement. This is deliberate: it means
the "what did we skip?" question has an auditable answer. A keyword or LLM pre-filter would
make Lane 1 a blind spot. A hash register does not.

**Required control**: the eval report must state the Lane 1 / Lane 2 split with counts, and
sample-audit a small number of Lane 1 passes per run to confirm the register is honest. A
template that has drifted in the register itself would otherwise be invisible.

---

## Preprocessing — mandatory before any detection runs

These are not detections. They are input-hygiene steps, and skipping them will generate the
email equivalent of the R1 false-positive family (`Designer/CONTEXT.md`, calibration rules).

1. **Strip quoted history.** Quoted prior messages must be separated from the sender's new
   content and marked read-only-context. **The single most likely false-positive source in
   this channel is attributing quoted text — often the customer's own words — to the Kota
   sender.** A finding may only cite text the sender actually authored in that message.
2. **Strip signature blocks and standard footers.** Boilerplate is assessed separately
   (HF-20), never as message content.
3. **Strip legal disclaimers and confidentiality notices.** Same reasoning.
4. **Resolve sender against the MCC register.** Use `From:` — an authenticated identity, so
   materially more reliable than Fireflies speaker labels. Look up
   `Researcher/research-mcc-fitness-probity.md`. Fail closed on unrecognised senders,
   subject to R7 (learner/observer capacity) which applies unchanged.
5. **Resolve shared-inbox and on-behalf-of sends.** Where `From:` is a shared mailbox
   (`benefits@`, `support@`) or the signature names a different person than the sender,
   authorisation attaches to **the human who authored the content**. If that cannot be
   established from the metadata, flag as an evidencing gap — do not guess, and do not
   silently pass.
6. **Extract and parse attachments.** Attachment content is in scope (HF-06, SF-16).

### Thread-state requirement
Unlike a call, a thread is re-read on every run. The agent must maintain a per-thread
watermark of the last assessed message ID, so that:
- new replies are assessed as a **delta**, with prior messages as read-only context;
- a thread already flagged does not regenerate the same finding on every subsequent run.

Without this the queue fills with duplicates within days.

---

## Exclusions — do not assess

> [!warning] Hard exclusions
> These are out of the agent's perimeter entirely. This is a privacy boundary, not a
> precision optimisation.
>
> - **Personal / non-work correspondence** in a work mailbox.
> - **HR, occupational-health, and employee-relations mail.**
> - **Legally privileged mail** — anything to or from external counsel.
> - **Internal-only threads** (all participants `@kota.io`, no external recipient) —
>   mirrors the call rule excluding internal meetings.
> - **Automated transactional mail** — no-reply, system notifications, calendar invites,
>   Intercom/platform notifications.

**Recording-consent criteria do not apply.** HF-08 and the recording-consent exclusion in the
call criteria are call-channel artefacts. There is no email analogue and no criterion ID
should be assigned to one.

> [!warning] Prerequisite — lawful basis
> Email monitoring has **no equivalent of the pre-call booking-form consent** that covers
> call recording. Before any live run over colleagues' mailboxes, the following must exist:
> a documented lawful basis (legitimate interests assessment), an employee-facing monitoring
> notice, and — on the current reading — an **Art. 35 DPIA**. This is a prerequisite to
> deployment, not a parallel workstream. Owner: Sola Olaniyan.

---

## Criteria carried over unchanged — `applies_to: both`

These transfer with no change of substance. Wording examples in the call criteria that
reference speech ("says", "tells the customer") read as "writes" in this channel.

| ID | Criterion | Note on the email form |
|---|---|---|
| HF-00 | Unqualified sender conducting MCC-regulated activity | Sender resolution is *more* reliable here (authenticated `From:`) |
| HF-01 | Explicit or implicit personal recommendation | Institutional "we recommend" framing is especially common in written follow-ups |
| HF-02 | Comparative value judgement on regulated products | — |
| HF-03 | Misrepresented firm role, capability, or regulatory status | Interacts with HF-20; a wrong footer plus a wrong claim is one compounded finding |
| HF-04 | Cross-selling or arranging without authorisation | "I'll get a quote for you" in writing is a firmer offer to arrange than the spoken form |
| HF-05 | Tax / social-welfare / pensions-law guidance, or incorrect public-law statement | Ports **verbatim**, including the AE source-of-truth comparison, the R2 charitable-interpretation pass, and the confirmed/light severity ladder. Works *better* here — written statements are precise and there is no transcription noise to argue about |
| HF-07 | Regulatory-circumvention or "ways around" language | — |
| HF-09 | Inducement / commission framed promotionally | Pairs with HF-19 — promotional framing *plus* a missing remuneration schedule |
| HF-10 | Unqualified sender describes product mechanics, cover, or terms | Includes the AE carve-out unchanged |
| HF-11 | Unqualified sender compares plans | — |
| HF-12 | Unqualified sender discusses changing cover or alternatives | — |
| HF-13 | Unqualified sender discusses pricing, premiums, pricing trends | — |
| HF-14 | Disclosure of confidential client, partner, or third-party information | Gains a major new trigger — see HF-22 |
| HF-15 | Discussion of fund or product performance / returns | — |
| SF-10 | Absolutes about coverage, premium, or outcome | — |
| SF-11 | Specific penalty/figure claims for regulator behaviour | — |
| SF-12 | Emotive or marketing language in regulated comms | **Character change** — see below |
| SF-13 | Disparagement of competitors, partners, providers, clients | — |
| SF-14 | Discouraging regulated advice | — |
| SF-15 | Behavioural nudge to a contribution / opt-out outcome | — |

All calibration rules **R1–R7** in `Designer/CONTEXT.md` apply unchanged in substance. R1
(speaker-content binding) is strengthened by the preprocessing requirement above: the
finding must cite text the sender authored, in a message they sent.

---

## Criteria that change character in email

### HF-06 — Unsecured handoff of customer personal data
`applies_to: both` — **but the trigger moves from intent to completed act.**

On a call, HF-06 fires on a *proposal*: "send me the spreadsheet by email". The breach is
prospective and coachable.

In email, the agent is looking at the artefact in which the transfer **actually happened**.
The attachment is present. The PPS numbers are in it. The data has left the secure flow.

**Consequences:**
- This is no longer a coaching finding. It is a **potential personal-data breach** with a
  GDPR Art. 33 72-hour notification clock attached.
- It must **not** sit in the ordinary Asana triage queue waiting for second-line review. It
  needs a separate, faster escalation path direct to the Data Protection lead.
- Severity floor: **Severe Fail** where the data is special-category (health) or includes
  PPS numbers / financial identifiers.

**Note on scope**: `req-detection-criteria.md` places post-call emailed spreadsheets
explicitly **out of scope** for the call agent ("the agent's perimeter is the transcript
only"). This channel closes exactly that gap. The call agent's declared blind spot is this
agent's core detection.

**Trigger families**: employee census spreadsheets; PPS numbers, DOB, salary, address, or
health data in a body or attachment; password-protected file with the password in the same
thread; personal data pasted inline "for speed".

**Regulation**: GDPR Art. 5(1)(f), Art. 32, Art. 33, Art. 28; DPC guidance on insurance-quote
data. See [[Data Retention]].

### SF-12 — Emotive or marketing language
`applies_to: both` — **promotes to a hard rule under one condition.**

On a call, emotive language is tone-only and rarely a standalone breach. In a written
communication that is promotional in nature **and** lacks the disclosures required when a
regulated product is described, the same language sits inside financial-promotion territory.

**Rule**: SF-12 remains soft in bespoke correspondence. Where the message is promotional and
HF-19 (missing required disclosure) also fires, treat the pair as a **hard** finding.

---

## New email-only criteria — Tier 1, hard rules

### HF-16 — Template drift: modified approved copy sent as approved
`applies_to: email` · **Priority: High**

**Description**: A sender takes an approved template and edits it before sending. The result
is neither approved copy nor recognised bespoke mail: it *structurally resembles* the
approved version, so a naive matcher waves it through, while the edited passage is
unreviewed free text going out under the credibility of approved copy.

**Why High**: This is the highest-risk population in the whole channel. Approved templates
carry implicit compliance sign-off. An edit inherits that authority without earning it, and
by construction it evades a same/different hash check.

**Trigger logic** (Designer to implement):
- Normalise the body (strip signature, footer, quoted history, merge-field values).
- Diff against the registered approved template.
- Exact match → Lane 1, documented pass.
- **Any** delta beyond permitted merge fields → route the delta to full Lane 2 detection and
  raise HF-16 alongside whatever the delta itself triggers.
- Permitted merge fields must be enumerated in the template register, not inferred.

**Positive example (flag)**: an approved PMI renewal template where the rep has inserted
"honestly the Bronze tier is plenty for a team your size" into the third paragraph.
**Negative example (don't flag)**: the same template sent with only `{{first_name}}`,
`{{company}}`, and `{{renewal_date}}` populated.

**Regulation / risk mapping**: MCC 2017 (unreviewed regulated-product information);
CPC 2025 Part 3 (clear, fair, accurate, not misleading); FCA COBS 4.2.4R; Kota internal
template-approval policy.

---

### HF-17 — Merge-field or mail-merge failure
`applies_to: email` · **Priority: High**

**Description**: A templated send fails at the data layer. Two distinct forms:
1. **Unpopulated tokens** — raw `{{first_name}}` / `%%company%%` reaching the customer.
2. **Cross-contaminated data** — merge fields populated from the **wrong record**, so one
   client's figures, scheme details, or contribution rates appear in another client's email.

**Why High**: Form 1 is a "clear, fair, not misleading" failure and an obvious competence
signal. Form 2 is materially worse — it is a **confidentiality and personal-data breach**,
and it simultaneously gives the recipient incorrect information about their own arrangement.

**Trigger logic**: pattern-match unresolved token delimiters; and cross-check that any
client-identifying values in the body (company name, scheme reference, figures) are
consistent with the recipient's own record. Inconsistency → flag.

**Positive example**: renewal email to Company A quoting Company B's employer contribution rate.
**Negative example**: correctly populated merge fields consistent with the recipient's record.

**Regulation / risk mapping**: GDPR Art. 5(1)(f), Art. 32, Art. 33; CPC 2025 Part 3;
IDD Art. 17(2). Form 2 engages HF-14 concurrently.

**Note**: fully deterministic to detect. Should be a cheap structural check, not an LLM pass.

---

### HF-18 — Automated sequence continued after a vulnerability or complaint signal
`applies_to: email` · **Priority: High**

**Description**: A HubSpot (or equivalent) sequence continues to fire after the customer's
reply contained a signal that should have halted it. The automation is context-blind: step 3
sends regardless of what the customer said in reply to step 2.

Halting signals — the escalation triggers, applied to inbound mail:
- **ES-01 equivalent**: redundancy, bereavement, illness, financial difficulty, mental-health
  reference, or an explicit request to stop.
- **ES-02 equivalent**: reference to a complaint to CBI, FCA, FOS, or FSPO, or to litigation.

**Why High**: This is the firm continuing to market at a customer who has **disclosed a
vulnerability**. It is systemic rather than individual, it repeats until someone notices, and
it is difficult to characterise as an honest slip. On the current reading this is graver than
most single-message findings, because the failure is in the firm's controls rather than one
person's judgement.

**Trigger logic**: for any thread containing an automated send, check whether an inbound
message preceding it carried an ES-01/ES-02 signal. If yes and the sequence continued → flag.

**Positive example**: customer replies "I've been made redundant, please take me off this";
sequence sends two further steps.
**Negative example**: same reply, sequence suppressed, human follow-up within one working day.

**Regulation / risk mapping**: CPC 2025 — vulnerable-customer provisions and best-interest
duty (*specific CPC part to be confirmed by Researcher against the source text*);
IDD Art. 17(1); FCA Consumer Duty (PRIN 2A) — consumer support and avoiding foreseeable harm.

**Routing**: always escalate. Never resolved as coaching.

---

### HF-19 — Regulated product described without required disclosure or documentation
`applies_to: email` · **Priority: High**

**Description**: The message describes, quotes, or promotes a regulated product without the
documentation or disclosure the regulations require to accompany it — most commonly a
missing **IPID**, or a missing **schedule of fees and remuneration** where commission is
mentioned.

**Why High**: These are affirmative, itemisable obligations rather than judgement calls. In
writing they are also **checkable** — either the IPID is attached or it is not — which makes
this one of the few criteria the agent can assess with near-certainty.

**Trigger families**:
- Insurance product described / quoted, no IPID attached or linked.
- Commission or remuneration mentioned, no fees-and-remuneration schedule.
- Pre-contractual information obligations engaged, nothing provided.

**Positive example**: rep emails PMI tier detail and pricing with no IPID and no link to one.
**Negative example**: same email with the current IPID attached and the fees schedule linked.

**Regulation / risk mapping**: IDR S.I. 229/2018 Reg. 27 (IPID); Reg. 23(1)(h) and
IDD Art. 19(1)(d)–(e) (remuneration); Reg. 26 (pre-contractual information); CPC 2025 Parts
3–4. Cross-reference [[Insurance Distribution]].

---

### HF-20 — Missing or incorrect firm regulatory identification
`applies_to: email` · **Priority: Medium-High**

**Description**: The signature block or footer misstates, or omits, Kota's regulatory status.

**The fact box** (from HF-03 in the call criteria): Kota is **FCA-regulated** as a broker for
UK activities and **CBI-regulated** as an insurance intermediary for Irish activities. A
footer naming only one regulator, on a message about activity governed by the other, is at
best imprecise and at worst misleading.

**Why Medium-High**: A structural, deterministic check — the strongest signal-to-noise ratio
of any criterion in this document. It is also systemic: a wrong footer is wrong on every
message that person sends until it is fixed, so a single finding implies a population.

**Trigger families**: no regulatory status line; wrong regulator for the activity; a
regulated-entity statement that does not match the CBI/FCA registers; missing firm
identification required by IDR Reg. 23(1)(a)–(d).

**Positive example**: UK broker mail whose footer names only the Central Bank of Ireland.
**Negative example**: footer stating both authorisations with the correct scope for each.

**Regulation / risk mapping**: IDR S.I. 229/2018 Reg. 23(1)(a)–(d); IDD Art. 18;
CPC 2025 Part 3; FCA financial-promotion identification requirements.

---

### HF-21 — Misdirected recipient / cc-bcc disclosure
`applies_to: email` · **Priority: High**

**Description**: Personal or confidential information disclosed to a recipient not entitled
to it, through a recipient-field error rather than through the message content.

**Why High**: One of the most frequent real-world personal-data breach classes, with no call
analogue whatsoever, and — like HF-06 — it engages an Art. 33 notification clock.

**Trigger families**:
- `cc` used instead of `bcc` on a multi-client or multi-employee send, disclosing the
  recipient list.
- A recipient from a different organisation on a thread containing another client's data.
- An employee's personal data visible to colleagues with no need to know.
- Reply-all extending a thread to recipients outside the original perimeter.

**Positive example**: benefits renewal notice sent to 40 employees with all addresses in `cc`.
**Negative example**: same notice sent individually, or via `bcc` with a neutral body.

**Regulation / risk mapping**: GDPR Art. 5(1)(f), Art. 32, Art. 33, Art. 34.

**Routing**: same fast path as HF-06 — Data Protection lead, not ordinary triage.

---

### HF-22 — Outward forwarding of internal or third-party content
`applies_to: email` · **Priority: High**

**Description**: An internal thread, or a thread concerning a different client, is forwarded
to an external recipient with the prior content still attached — exposing internal commentary,
another client's information, or candid assessments never intended to leave the firm.

**Why High**: This is HF-14 (confidentiality) with a new and probably very common mechanism.
Forwarding is a one-click action and the quoted history is easy to forget. The exposed content
is frequently the *most* damaging kind: internal frankness about a client, a partner, or a
provider.

**Trigger families**:
- Internal thread forwarded outward with quoted history intact.
- Quoted history naming another client or containing their figures.
- Internal candid commentary about the recipient, a partner, or a provider now visible to them.
- Forwarded chain containing a colleague's personal data.

**Positive example**: rep forwards a prospect the pricing thread, with an internal line
reading "they'll never pay that, but try it" still quoted below.
**Negative example**: rep composes a fresh message with only the relevant content.

**Regulation / risk mapping**: GDPR Art. 5(1)(f); CPC 2025 Part 3; Standards for Business
(S.I. 60/2011 — act with integrity); Kota MSA confidentiality clauses. Cross-flag HF-14 where
a client is named.

---

## New email-only criteria — Tier 3, soft signals

### SF-16 — Unapproved attachment or collateral
`applies_to: email`

**Description**: An attachment or linked document that is not in the approved-collateral
register — an old deck, a personally-built comparison spreadsheet, a screenshot of a quote.

**Why Soft**: often benign (a genuinely helpful summary), but it is unreviewed material
carrying the firm's name. Becomes hard when it describes a regulated product and HF-19 fires,
or when the attachment contains personal data (HF-06).

**Trigger families**: attachment absent from the collateral register; a document version
older than the current approved one; a self-built comparison table.

**Regulation / risk mapping**: CPC 2025 Part 3; FCA COBS 4.2.4R; Kota internal collateral
approval policy.

### SF-17 — Link to unapproved or outdated external resource
`applies_to: email`

**Description**: A link to a third-party page, a superseded gov.ie URL, or an internal
document not intended for customers.

**Why Soft**: a link is not a claim. But a link presented as authority for a regulated-product
statement functions as one, and a stale gov.ie AE link is a live HF-05 risk vector.

**Note for calibration**: links to *approved* collateral must **not** be flagged. This is
an anticipated false-positive family — see the calibration section.

---

## Lane 1 — Template library audit findings

These are findings against the **register**, not against any message. They surface in a
periodic library audit rather than a daily run, and they do not create per-send tasks.

| ID | Finding | Why it matters |
|---|---|---|
| `LIB-01` | Template in active use, never compliance-reviewed | Unreviewed copy at scale |
| `LIB-02` | Template approved against a superseded version of the detection criteria | Approval no longer means what it meant |
| `LIB-03` | Template containing a criterion breach (any HF/SF) | One breach replicated across every send |
| `LIB-04` | Template with no named approver or approval date | Approval unevidenced |
| `LIB-05` | Sequence with no vulnerability-signal suppression rule | Root cause of HF-18 |
| `LIB-06` | Template in the register but no longer matching what the tool actually sends | Register has drifted from reality |

**This may be the highest-leverage part of the whole build.** If templated and sequenced mail
dominates the channel, auditing a small library thoroughly beats auditing a large volume of
traffic — and `LIB-02` and `LIB-05` are systemic findings that per-message monitoring would
never surface.

---

## Escalation triggers

**ES-01, ES-02, ES-03 apply unchanged in substance**, with one addition: in email they are
detected on **inbound** customer messages as well as outbound Kota messages, because an
inbound signal creates an obligation (see HF-18). On a call there was only one artefact; here
the customer's own words are part of the monitored record.

Two new fast-path escalations that bypass ordinary triage:

- **ES-04 — Suspected personal-data breach.** Any HF-06, HF-17 (form 2), or HF-21 finding.
  Routes to the Data Protection lead within the working day, because of the Art. 33 72-hour
  clock. Must not queue behind ordinary compliance triage.
- **ES-05 — Systemic / population finding.** Any finding whose cause is a template, sequence,
  or footer rather than one person's judgement (HF-16 at volume, HF-18, HF-20, any `LIB-*`).
  Routes to template governance, not to individual coaching — coaching the sender of a
  template-caused breach fixes nothing.

---

## Anticipated false-positive families — calibration starting point

R1–R7 are artefacts of *call* failure modes (diarisation, observer capacity, BDR discovery).
This channel will have its own. Predicted, to be confirmed against the first live runs and
then written up as `Evaluator/calibration-<date>-email-false-positives.md`:

1. **Quoted history attributed to the Kota sender** — the customer's own words, or a
   forwarded third party's, read as the sender's. Expected to be the dominant family, and the
   direct analogue of R1. Mitigated by preprocessing step 1, but expect leakage.
2. **Signature blocks and disclaimers read as content** — a footer naming a regulator flagged
   as an HF-03 claim.
3. **Approved template copy re-flagged on every send** — the reason the template register is a
   prerequisite rather than an enhancement. This is the direct analogue of
   `research-prescribed-scripts.md` for calls.
4. **Links to approved collateral read as claims** — see SF-17.
5. **Internal threads with a single external cc** treated as customer-facing correspondence.
6. **Scheduling and logistics mail** with incidental product nouns ("re: your PMI renewal
   call") flagged as product discussion.

---

## Out of scope for v1

- **Inbound customer mail as a monitored population in its own right.** Assessed only for
  ES-01/ES-02 signals and thread context, not graded.
- **Calendar invites, meeting notes, and Intercom conversations.** Separate channels.
- **Chat / Slack.** Separate channel.
- **Tone and sentiment analysis** beyond SF-12 — same exclusion as the call criteria.
- **Sender-level pattern tracking across messages.** Compliance tracks this from the queue,
  as with calls. `LIB-*` findings are the exception, being systemic by definition.
- **Non-English mail** — escalate per ES-03.
- **Attachment contents beyond text extraction** — no image OCR or embedded-object parsing in
  v1. An unparseable attachment is an **evidencing gap**, not a pass.

---

## Output requirements — handoff to Designer

Per finding, in addition to the call criteria's seven fields:

1. **Criterion ID** — shared space (HF-00…HF-22, SF-10…SF-17, ES-01…ES-05, LIB-01…LIB-06)
2. **`channel`** — `email` (so cross-channel queries resolve)
3. **`lane`** — `1-templated` | `2-bespoke` | `library-audit`
4. **Severity** — High / Medium / Low / Escalate
5. **Hard or Soft**
6. **Sender** — email address, resolved name, authorisation status, product scope
7. **Evidence quote** — verbatim, and **from the sender's own authored text only**, never from
   quoted history
8. **`message_id` + permalink** — see below
9. **`thread_id`** — for deduplication against existing Asana tasks
10. **Recommended action** — "Coach (language)", "Coach (perimeter)", "Refer to compliance",
    "Escalate to SME", **"Refer to template governance"** (new — for ES-05 / `LIB-*`),
    **"Refer to Data Protection"** (new — for ES-04)

### Navigation key — a simplification worth taking deliberately

The call criteria make the **verbatim quote the search key** because Fireflies MCP does not
expose per-sentence `start_time`, so timestamps are unusable for navigation.

**That constraint does not exist here.** Every email has a stable, permanent `message_id` and
a Gmail permalink. Compliance clicks straight to the message.

So: keep the verbatim quote as **evidence** — it is still what demonstrates the breach — but
it is **no longer load-bearing for navigation**. The permalink is. Do not port the
quote-as-search-key workaround into a channel that does not need it. In the Asana task, the
`Recording Link` field becomes a **message permalink**.

---

## Dependencies — what must exist before the first live run

| # | Dependency | Owner | Blocking? |
|---|---|---|---|
| 1 | **Mailbox access at domain scope.** The current Gmail connector is authenticated as a single user. Compliance's own mailbox does not contain GTM's outbound mail — the population this agent exists to monitor. Domain-wide coverage needs Workspace domain-wide delegation, a Google Vault export, or a mail-gateway journal rule. | Sola Olaniyan + IT | **Yes — hard blocker** |
| 2 | **Lawful basis, monitoring notice, DPIA.** No booking-form-consent equivalent exists for email. | Sola Olaniyan | **Yes — hard blocker** |
| 3 | **Approved-template register** (`research-approved-email-templates.md`) with normalised body hashes, permitted merge fields, approver, approval date, and criteria version. Without it every send is Lane 2 and the volume argument collapses. | Researcher + GTM Ops | **Yes** |
| 4 | **Approved-collateral register** — attachment and link allowlist for SF-16 / SF-17. | Researcher + GTM Ops | No — degrades precision |
| 5 | **HubSpot sequence inventory** — which sequences exist, their steps, and whether each has a reply/vulnerability suppression rule (`LIB-05`). | GTM Ops | No — `LIB-05` unassessable without it |
| 6 | **Written-medium grading decision** — does an identical breach grade higher in writing? | Sola Olaniyan + Trevor Gardiner | **Yes — needed to grade at all** |
| 7 | **Asana destination** — does email share the Call Monitoring project (GID `1213240137041729`) or get its own? Affects section GIDs and custom fields. | Sola Olaniyan | **Yes — needed to file tasks** |
| 8 | **Data Protection escalation route** for ES-04. The existing Escalated section loops in the COO; an Art. 33 clock may need a different recipient. | Sola Olaniyan | Yes, before first ES-04 |

Shared, already in place, and **read-only** for this workspace — do not fork or duplicate:
- `research-mcc-fitness-probity.md` — the MCC register
- `source-of-truth-ae-myfuturefund.md` — AE baseline for HF-05
- `research-call-supervision-audit.md` — breach patterns and reviewer rubric
- `research-prescribed-scripts.md` — the structural model for the template register

---

## Open questions for Compliance

1. **Written-medium uplift** — dependency 6. Recorded here so it is not decided by default.
2. **Is HF-20 (footer) a per-message finding or a one-off remediation?** A wrong footer is
   wrong on every send. Filing one task per message would flood the queue; the population is
   the finding. Recommend: one `LIB`-style systemic task per affected sender, not per message.
3. **Does HF-18 apply retrospectively** to sequences already sent before the agent goes live?
   There may be live vulnerability signals sitting unactioned in existing threads.
4. **Attachment retention** — the `Issues` field convention is verbatim quotes. Email bodies
   and attachments carry far more personal data per line than a transcript span. A redaction
   rule is needed that calls never required.
