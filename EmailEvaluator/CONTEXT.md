# Email Evaluator — Context

## Current Project
Pull customer-facing email for a given date, split it into the two assessment lanes, and
assess the bespoke lane against `Researcher/req-email-detection-criteria.md` and the
speaker-authorisation register in `Researcher/research-mcc-fitness-probity.md`. Produce a
daily eval report and a periodic template-library audit.

This workspace is the email counterpart to `/Evaluator` (calls). The two run independently
and share their criteria ID space, their MCC register, and their AE source-of-truth. Nothing
in this workspace modifies the call pipeline.

## Status — not yet runnable

> [!warning] Two hard blockers before any live run
> 1. **Mailbox access is out of scope.** The Gmail connector is authenticated as a single
>    user (sola@kota.io). Compliance's mailbox does **not** contain GTM's outbound mail —
>    the population this agent exists to monitor. Needs Workspace domain-wide delegation, a
>    Vault export, or a mail-gateway journal rule.
> 2. **No lawful basis yet.** Unlike call recording (covered by the pre-call booking form),
>    email monitoring has no consent artefact. Needs a legitimate-interests assessment, an
>    employee-facing monitoring notice, and an Art. 35 DPIA.
>
> See `Researcher/req-email-detection-criteria.md` § Dependencies. Until both clear, work in
> this workspace is design and dry-run only — do not run over live mailboxes.

## Primary Workflow: Daily Email Evaluation

### Step 1 — Pull messages for the target date
Query the mail source for messages sent on the target date. Retain, per message:
`message_id`, `thread_id`, `From`, `To`/`cc`/`bcc`, subject, body, attachment list, permalink,
and whether the send was automated (sequence/template tooling) or human.

### Step 2 — Apply exclusions
Drop, before any assessment (see criteria § Exclusions — this is a privacy boundary, not a
precision optimisation):
- internal-only threads (all participants `@kota.io`, no external recipient)
- automated transactional mail (no-reply, system notifications, calendar invites)
- personal / non-work correspondence
- HR, occupational-health, employee-relations mail
- legally privileged mail

Record the excluded count by reason. An exclusion is a documented decision, not a silent drop.

### Step 3 — Preprocess (mandatory)
Per criteria § Preprocessing:
1. Strip quoted history — separate the sender's authored text from quoted prior messages.
2. Strip signature blocks and footers (assessed separately under HF-20).
3. Strip legal disclaimers.
4. Extract and parse attachments.

**The most likely false-positive source in this channel is attributing quoted text — often the
customer's own words — to the Kota sender.** A finding may only cite text the sender authored
in the message being assessed.

### Step 4 — Assign lane
Normalise the body (strip signature, footer, quoted history, merge-field values) and hash it.
Compare against `Researcher/research-approved-email-templates.md`.

| Result | Lane | Action |
|---|---|---|
| Exact match to an approved, in-date template | `1-templated` | Documented pass — no detection run |
| Partial match (delta beyond permitted merge fields) | `2-bespoke` | Raise **HF-16** + assess the delta |
| No match | `2-bespoke` | Full detection run |

Lane assignment is a **hash comparison, not a model judgement** — deliberately, so that "what
did we skip?" has an auditable answer.

### Step 5 — Resolve sender authorisation
Look up `From:` against `Researcher/research-mcc-fitness-probity.md`. Unlike Fireflies speaker
labels, `From:` is an authenticated identity — this step is materially more reliable than its
call equivalent. Fail closed on unrecognised senders, subject to **R7** (learner/observer
capacity), which applies unchanged.

Where `From:` is a shared mailbox (`benefits@`, `support@`) or the signature names someone
other than the sender: authorisation attaches to **the human who authored the content**. If
that cannot be established, record an evidencing gap — do not guess, do not silently pass.

### Step 6 — Apply detection criteria (Lane 2 only)
Evaluate against `Researcher/req-email-detection-criteria.md`:
- **HF** — flag on any match; cite sender, verbatim authored quote, `message_id`, permalink.
- **SF** — note; flag at N≥2 in the same message, or co-occurring with a hard rule.
- **`[Speaker-scoped]`** logic applies as on calls.
- **R1–R7** calibration rules apply unchanged in substance.
- Deterministic checks (HF-17 merge fields, HF-20 footer, HF-21 recipient fields) should run
  as structural checks, not LLM passes.

### Step 7 — Deduplicate against thread state
Read the per-thread watermark (last assessed `message_id`). Assess only messages after it,
with prior messages as read-only context. Update the watermark on completion.

Without this the queue fills with duplicates within days — a thread is re-read on every run,
unlike a call, which is seen exactly once.

### Step 8 — Write the report
`EmailEvaluator/eval-email-YYYY-MM-DD-daily.md`, per the template below.

### Step 9 — Route fast-path escalations
**Before** filing ordinary tasks, check for ES-04 (suspected personal-data breach — any HF-06,
HF-17 form 2, or HF-21). These carry a **GDPR Art. 33 72-hour clock** and must not queue
behind ordinary compliance triage. Route to the Data Protection lead the same working day.

## Eval Report Template

```markdown
---
title: Daily Email Compliance Eval — YYYY-MM-DD
created: YYYY-MM-DD
type: eval
channel: email
run_type: live | dry-run
messages_pulled: N
messages_excluded: N
lane_1_templated: N
lane_2_bespoke: N
messages_flagged: N
---

# Daily Email Compliance Eval — YYYY-MM-DD

## Summary
| Pulled | Excluded | Lane 1 (templated) | Lane 2 (bespoke) | Flagged | Hard | Soft | Clean |
|---|---|---|---|---|---|---|---|
| N | N | N | N | N | N | N | N |

### Exclusions by reason
| Reason | Count |
|---|---|
| Internal-only | N |
| Automated transactional | N |
| Personal / HR / privileged | N |

### Lane 1 sample audit
Templates sampled this run, and whether the register matched what was actually sent.
Required every run — a template that has drifted **in the register itself** is otherwise
invisible.

| Template | Sends | Sampled | Register accurate? |
|---|---|---|---|

## Per-Message Results

### [Subject] — [message_id] — [YYYY-MM-DD HH:MM]
**Sender**: Name <email> — [Qualified / New Entrant / Script / Unregistered / Unrecognised]
**Recipient org**: Company
**Lane**: 1-templated / 2-bespoke
**Permalink**: <url>
**Grade**: Pass / Pass-with-comments / Fail / Severe Fail

#### Findings
| Criterion | Severity | Authored quote (verbatim) | Regulation |
|---|---|---|---|
| HF-01 | High | "what I'd recommend is setting employer contribution to 1.5%" | MCC 2017 / CPC 2025 |

#### Notes
Context; why a finding may be borderline.

---

## Fast-path escalations (ES-04 / ES-05)
| Criterion | Message | Routed to | Date routed |
|---|---|---|---|

## Systemic findings
Findings whose cause is a template, sequence, or footer rather than one person's judgement.
Route to template governance — coaching the sender of a template-caused breach fixes nothing.

## Cross-message patterns
Recurring phrasing or senders across multiple messages with the same breach type.

## Findings withdrawn after reassessment
Per **R5** — mandatory section, empty is fine on a clean run.

| Message | Original finding | Why withdrawn | Reassessment date |
|---|---|---|---|

## Open questions for the Designer
```

## Secondary Workflow: Template Library Audit

Runs on template change and periodically (recommend monthly) — **not** daily. Assesses the
register itself against `LIB-01`…`LIB-06`, and writes
`EmailEvaluator/audit-templates-YYYY-MM-DD.md`.

**This is likely the highest-leverage work in the channel.** If templated and sequenced mail
dominates, auditing a small library thoroughly beats auditing a large volume of traffic. A
non-compliant template is one breach replicated across every send, and `LIB-02` (approved
against superseded criteria) and `LIB-05` (sequence with no vulnerability suppression) are
systemic findings that per-message monitoring will never surface.

## What good looks like
- Every finding cites the **sender's own authored text**, verbatim, with `message_id` and
  permalink — never quoted history, never a paraphrase.
- Lane assignment is stated per message and the Lane 1/2 split is reported with counts.
- Exclusions are counted by reason, not silently dropped.
- Lane 1 is sample-audited every run, so the register's honesty is evidenced rather than assumed.
- Clean messages are documented as negatives.
- Deterministic checks (HF-17, HF-20, HF-21) are run structurally, not left to a model.
- ES-04 findings are routed the same working day, ahead of ordinary triage.
- Systemic findings are separated from individual ones, and routed to governance not coaching.

## What to avoid
- Don't attribute quoted history, signature blocks, or footers to the sender as content.
- Don't assess internal-only threads, or anything in the hard-exclusion list.
- Don't run over live mailboxes before dependencies 1 and 2 clear.
- Don't collapse findings into a single "flagged" label — preserve the criterion ID and HF/SF split.
- Don't re-flag approved template copy; if it recurs, the register is wrong — fix the register.
- Don't file one task per message for a footer or template fault. The population is the
  finding; see criteria § Open questions Q2.
- Don't port the call agent's quote-as-search-key workaround. Email has stable permalinks —
  the quote is evidence, the permalink is navigation.

## Key source files
- `Researcher/req-email-detection-criteria.md` — criteria, lanes, exclusions, dependencies
- `Researcher/req-detection-criteria.md` — call criteria; the `applies_to: both` rules live there
- `Researcher/research-mcc-fitness-probity.md` — MCC register (shared, read-only)
- `Researcher/source-of-truth-ae-myfuturefund.md` — AE baseline for HF-05 (shared, read-only)
- `Researcher/research-approved-email-templates.md` — template register (**to be created**)
- `Designer/CONTEXT.md` — calibration rules R1–R7
