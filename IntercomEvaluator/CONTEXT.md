# Intercom Evaluator — Context

## Current Project
Pull **Customer Service / CX** conversations from Intercom for a given date, split them into the
three assessment lanes, and assess against `Researcher/req-intercom-detection-criteria.md` and the
MCC register in `Researcher/research-mcc-fitness-probity.md`. Produce a daily eval report and a
periodic content-governance audit over help-centre Articles.

## Population — CX only, BenOps excluded

| Attribute | In scope | Out of scope |
|---|---|---|
| `Brand` | `Kota` | `Kota: BenOps` |
| Team | `PL: CX Platform- Customer` and other `PL:` CX/CS teams | `BenOps: *` |
| Ticket type | `PL-CX: Customer Ticket` | `BenOps: Client, Customer & Provider` |
| Route in | `support@kota.io` + in-app chat | `benops@kota.io` |

**BenOps / Embed is out of scope** by Compliance direction (2026-08-04) — the larger population
(31,483 vs 3,523) but a specialist operations function. Monitoring priority is the customer-facing
functions: sales, customer service, customer success.

`support@kota.io` routes into Intercom rather than Gmail, so **customer service email is this
channel**. `EmailEvaluator/` is effectively the sales/GTM channel.

Third channel alongside `/Evaluator` (calls) and `/EmailEvaluator` (email). Shares the criteria
ID space, the MCC register, the AE source-of-truth, and the template/macro register. Nothing in
this workspace modifies the call or email pipelines.

## Status — buildable now

Unlike the email channel, this one is **not blocked on access**. The Intercom integration is
app-level rather than a personal mailbox grant, and reads the BenOps inbox today.

Four things still gate a *grading* run:
1. **Complaints deadlines unverified** — HF-24 carries `{{TO VERIFY}}` placeholders and HF-23
   needs the regulatory complaint definition. Researcher task.
2. **Internal notes vs customer replies** — if the API does not distinguish them, internal
   candour would be graded as customer communication. Must be confirmed before any run.
3. **MCC register coverage for CX / CS staff** — the register is oriented to GTM and Benefits. If
   CX teammates are absent, fail-closed makes every conversation a finding, which is noise
   rather than signal.
4. **CX / CS team ID list** — needed to scope the pull and to route output to the right Asana
   department section.

Everything else can be built and dry-run against live data now.

## Primary Workflow: Daily Intercom Evaluation

### Step 1 — Pull conversations
`search_conversations` with `created_at` or `updated_at` bounded to the target date. Paginate via
`pages.next.starting_after` until exhausted — **do not** assume one page is the day's full set.

**Both source types are in scope**: `source_type: conversation` (in-app chat) and `email` (mail to
`support@kota.io`). They land in the same `PL-CX` ticket type and are the same conduct in two media.

Scope by **brand and team, not by source type** — the connector's `team_assignee_id` filter is the
reliable gate. Filter to CX/CS teams and exclude `BenOps: *`. Verify against `Brand` and
`ticket_type` on each result, since team assignment can change mid-conversation.

### Step 2 — Fetch full conversations
`get_conversation(id)` for each. The search response carries only the opening message; findings
need the full `conversation_parts` history.

### Step 3 — Apply exclusions
- **BenOps brand / teams** — belt and braces on the Step 1 filter
- Intercom platform notifications and system-generated conversations
- Conversations with no `admin`-authored part (nothing for Kota to be accountable for)
- Test and internal-only conversations

Record excluded counts by reason.

### Step 4 — Preprocess
1. **Split parts by `author.type`** — `admin` (Kota staff), `bot` (Fin), `user` (customer or
   partner). This determines which criteria apply at all, and it is structural rather than
   inferred — a real advantage over the email channel.
2. **Separate the ticket form dump from free-text prose.** Opening messages often arrive as a
   structured header (client ticket ID, country, provider, product) plus a free-text detail
   field. Only the free text is authored prose. The header is not a statement by anyone.
3. **Identify internal notes** and exclude them from customer-facing assessment — see gate 2 above.
4. **Extract and parse attachments.**

### Step 5 — Assign lane
| Condition | Lane |
|---|---|
| `bot`-authored substantive answer present | `1-fin` |
| `admin` reply hash-matches an approved macro | `2-macro` |
| Free-text `admin` reply | `3-bespoke` |

A conversation can occupy more than one lane — assess each qualifying part. Lane 2 reuses the
email register and normalisation rules verbatim (`research-approved-email-templates.md`,
`sending_tool: intercom-macro`).

### Step 6 — Resolve teammate authorisation
Map `admin_id` / teammate ID to the MCC register. Authenticated identity, so more reliable than
Fireflies labels. Fail closed on unrecognised teammates, subject to **R7**.

**Fin needs no lookup** — it is unqualified by construction and can never be registered. That is
the point of HF-25.

### Step 7 — Apply detection criteria
Per `Researcher/req-intercom-detection-criteria.md`. Run the deterministic checks first — they
are cheap and the platform has already done most of the work:

| Check | Source |
|---|---|
| HF-23 complaint not logged | complaint substance in `user` parts vs `PL: Issue Type` / ticket type |
| HF-24 timeline breach | `first_admin_reply_at`, `last_admin_reply_at`, `first_close_at` vs the regulatory deadlines |
| HF-26 no qualified human | participating `admin` list vs register, plus `ai_agent_resolution_state` |

Then the model-judged criteria (HF-00 family, HF-25, SF-*) over the authored prose.

**Use the platform's own classification as ground truth where it exists.** If Intercom already
says `Complaint / Escalation`, do not re-infer it. Report `sla_status` alongside HF-24 but never
*as* HF-24 — an internal SLA is a commercial target, the regulatory deadline is a legal one.

### Step 8 — Deduplicate against conversation state
A conversation reopens and accretes parts across days. Maintain a per-conversation watermark of
the last assessed `part_id`; assess only newer parts, with earlier ones as read-only context.
Sampled conversations run to 40–70 parts, so without this the same finding regenerates every run.

### Step 9 — Write the report
`IntercomEvaluator/eval-intercom-YYYY-MM-DD-daily.md`.

### Step 10 — Route escalations
- **ES-04** (data breach) — same working day, Data Protection lead, ahead of ordinary triage.
- **ES-05** (systemic) — **all HF-25 and HF-26 findings**, plus any `LIB-*`. Route to whoever
  owns Fin configuration and content sources. Never coach an individual for a Fin answer; no
  human made a judgement call.
- **ES-01** will fire often. Health, bereavement, and financial difficulty are routine in a
  benefits support queue. The correct response is triage capacity, not a higher threshold.

## Eval Report Template

```markdown
---
title: Daily Intercom Compliance Eval — YYYY-MM-DD
created: YYYY-MM-DD
type: eval
channel: intercom
run_type: live | dry-run
conversations_pulled: N
conversations_excluded: N
lane_1_fin: N
lane_2_macro: N
lane_3_bespoke: N
conversations_flagged: N
---

# Daily Intercom Compliance Eval — YYYY-MM-DD

## Summary
| Pulled | Excluded | Fin | Macro | Bespoke | Flagged | Hard | Soft | Clean |
|---|---|---|---|---|---|---|---|---|

## Complaints
Separate section — complaints carry dated obligations and must not be buried among conduct findings.

| Conversation | Complaint substance? | Platform classified? | Ack elapsed | Within deadline? | Finding |
|---|---|---|---|---|---|

## Automated agent (Fin)
| Conversation | Fin answered? | Regulated content? | Content source | Qualified human involved? | Finding |
|---|---|---|---|---|---|

Group by **content source**, not by conversation — the Article is the root cause, and one bad
Article produces many findings that share a single fix.

## Per-Conversation Results

### [Title] — [conversation_id] — [YYYY-MM-DD HH:MM]
**Kota participants**: Name (MCC status), … | **Fin participated**: yes/no
**Counterparty**: client / partner support / end employee
**Lane(s)**: 1-fin / 2-macro / 3-bespoke
**Platform**: `PL: Issue Type` · `ticket_type` · `sla_status` · `ai_agent_resolution_state`
**Permalink**: <ticket.url>
**Grade**: Pass / Pass-with-comments / Fail / Severe Fail

#### Findings
| Criterion | Severity | Author (type) | Verbatim quote | part_id | Regulation |
|---|---|---|---|---|---|

#### Notes

---

## Systemic findings (ES-05)
Findings whose cause is Fin configuration, a content source, or a macro — not one person's
judgement.

## Fast-path escalations (ES-04)
| Criterion | Conversation | Routed to | Date routed |
|---|---|---|---|

## Cross-conversation patterns

## Findings withdrawn after reassessment
Per **R5** — mandatory section, empty is fine.

| Conversation | Original finding | Why withdrawn | Reassessment date |
|---|---|---|---|

## Open questions for the Designer
```

## Secondary Workflow: Content Governance Audit

Assesses the content layer against `LIB-07`–`LIB-12`; writes
`IntercomEvaluator/audit-content-YYYY-MM-DD.md`. Runs on content change and periodically
(recommend monthly).

Enumerate help-centre Articles via `list_articles`, fetch bodies via `get_article`, and assess
each against the full criteria set as if it were a customer-facing communication — because it is
one, published permanently and at scale.

**`LIB-08` and `LIB-11` are the highest-leverage findings available in this channel.** Fin's
answers derive from its content sources, so a breach in an Article is a breach in every future
answer drawn from it. Fixing the Article prevents what per-conversation monitoring can only
detect after it has reached customers.

Unlike the email template register, this audit is **not blocked** — the Article library is
enumerable through the connector today.

## What good looks like
- Every finding records `author_type` and attaches to a specific `part_id`.
- Only `admin`-authored parts are treated as Kota conduct; `user` and `bot` parts are never
  attributed to staff.
- Deterministic checks (HF-23, HF-24, HF-26) run structurally, using platform metadata rather
  than re-inferring what Intercom already asserts.
- Complaints are reported in their own section with elapsed-time arithmetic shown.
- HF-25 findings are grouped by content source, so the fix is visible.
- All Fin findings route to systemic (ES-05), never to individual coaching.
- Clean conversations are documented as negatives.

## What to avoid
- Don't attribute a customer's words to Kota staff. CX conversations are opened by employers and
  employees who describe their own cover and speculate about eligibility. **This is the dominant
  false-positive risk in this channel.** Only `admin` parts are Kota conduct.
- Don't pull BenOps traffic. Filter on brand and team, and verify per result.
- Don't treat platform support as product discussion. Much CX traffic is genuinely technical —
  login failures, sync errors, missing access. A `Provider` attribute on the conversation does not
  make a technical exchange regulated.
- Don't assess the structured ticket header as authored prose.
- Don't grade internal notes as customer communication.
- Don't substitute `sla_status` for a regulatory deadline.
- Don't coach an individual for a Fin answer.
- Don't grade HF-23/HF-24 until the `{{TO VERIFY}}` deadlines are populated. Flag them as
  unassessable rather than guessing.
- Don't assume one page of search results is the day's full population.
- Don't tune ES-01 down because it fires often.

## Key source files
- `Researcher/req-intercom-detection-criteria.md` — criteria, lanes, dependencies
- `Researcher/req-email-detection-criteria.md` — written-medium rules, ES-04/ES-05, `LIB-*` base
- `Researcher/req-detection-criteria.md` — base criteria, HF-00 family
- `Researcher/research-mcc-fitness-probity.md` — MCC register (shared, read-only)
- `Researcher/research-approved-email-templates.md` — macro register (`intercom-macro`)
- `Designer/CONTEXT.md` — calibration rules R1–R7
