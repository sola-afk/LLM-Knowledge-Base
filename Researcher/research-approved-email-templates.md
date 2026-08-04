---
title: Approved Email Template Register
created: 2026-08-04
updated: 2026-08-04
type: register
channel: email
status: draft — schema defined, not yet populated
owner: Researcher + GTM Ops
---

# Approved Email Template Register

The Lane 1 / Lane 2 gate for the email monitoring agent. This register is what makes the
channel tractable: a message matching an approved, in-date template is a **documented pass**
rather than an unassessed gap, so the expensive detection pass runs only over bespoke mail.

Structural model: `Researcher/research-prescribed-scripts.md`. That register does the same job
for script-pathway speakers on calls — a speaker delivering approved scripted content is not
breaching. This is the written equivalent.

> [!warning] Not yet populated
> Until GTM Ops supplies the template inventory, **every send falls into Lane 2** and the
> volume argument for the whole channel collapses. This is dependency 3 in
> `req-email-detection-criteria.md` § Dependencies, and it is blocking.

## Why this register is load-bearing

Three separate mechanisms depend on it:

1. **Lane assignment** (`EmailEvaluator/CONTEXT.md` Step 4) — hash match against this register
   decides whether a message is assessed at all. Deliberately deterministic, so "what did we
   skip?" has an auditable answer rather than a model's opinion.
2. **HF-16 template drift** — the diff baseline. Without a registered original there is nothing
   to diff against, and edited approved copy becomes undetectable.
3. **False-positive family 3** (`req-email-detection-criteria.md` § Anticipated false positives)
   — without this register the agent re-flags the same compliance-approved copy on every send,
   which is the fastest way to lose the team's trust in the tool.

## Register schema

One row per template **version**. Versions are never edited in place — a changed template is a
new row, and the previous row is marked superseded. Same discipline as the Designer's prompt
versioning.

| Field | Type | Notes |
|---|---|---|
| `template_id` | string | Stable ID from the sending tool (HubSpot template ID or equivalent) |
| `name` | string | Human-readable |
| `version` | int | Increments on any change to the body |
| `body_hash` | string | SHA-256 of the **normalised** body — see normalisation rules below |
| `permitted_merge_fields` | list | Enumerated explicitly. **Anything outside this list is a delta and triggers HF-16.** Never inferred |
| `sending_tool` | enum | `hubspot-sequence` / `hubspot-template` / `gmail-template` / other |
| `sequence_id` | string | If part of a sequence; null otherwise |
| `sequence_step` | int | Position in the sequence; null otherwise |
| `has_suppression_rule` | bool | Does the sequence halt on customer reply? **False is `LIB-05`** |
| `describes_regulated_product` | bool | If true, HF-19 disclosure requirements apply to the template itself |
| `attachments` | list | Attached/linked collateral, cross-referenced to the collateral register |
| `approved_by` | string | Named person. **Empty is `LIB-04`** |
| `approved_date` | date | **Empty is `LIB-04`** |
| `criteria_version_at_approval` | string | Which version of the detection criteria it was reviewed against. **Stale is `LIB-02`** |
| `status` | enum | `approved` / `superseded` / `withdrawn` / `never-reviewed` (= `LIB-01`) |
| `notes` | text | Known limitations, scope conditions |

### Body normalisation rules

The hash must be stable across sends of the same template, so normalise before hashing —
in this order:

1. Strip the signature block.
2. Strip the regulatory footer and legal disclaimer (assessed separately under HF-20).
3. Strip quoted history.
4. Replace **populated** merge-field values with their token form
   (`Hi Sarah,` → `Hi {{first_name}},`).
5. Collapse whitespace runs to a single space; normalise line endings.
6. Lowercase.
7. Strip tracking parameters from URLs (query strings vary per recipient and would otherwise
   break every hash).

Step 4 is the one to get right. If populated values are not reverted to tokens, every send
hashes differently and the register never matches anything.

## Register

<!-- POPULATE FROM GTM OPS TEMPLATE INVENTORY. One row per template version. -->

| template_id | name | version | body_hash | permitted_merge_fields | sending_tool | sequence_id | step | suppression | regulated_product | approved_by | approved_date | criteria_version | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _(empty)_ | | | | | | | | | | | | | |

## Sequence inventory

Separate from templates, because `LIB-05` is a property of the **sequence**, not of any single
step. A sequence that fires step 3 regardless of what the customer said in reply to step 2 is
the root cause of **HF-18** — the firm continuing to market at someone who has disclosed a
vulnerability.

| sequence_id | name | steps | halts on reply? | halts on vulnerability signal? | owner | notes |
|---|---|---|---|---|---|---|
| _(empty)_ | | | | | | |

> "Halts on reply" and "halts on vulnerability signal" are different controls. Most tools
> support the first natively. The second generally needs explicit configuration, and its
> absence is what HF-18 detects at the message level. Record both.

## Maintenance

**On any template change**: add a new row, mark the previous version `superseded`, re-hash.
Never edit a row in place — the old hash is needed to recognise mail already in flight.

**On any detection-criteria change**: every row whose `criteria_version_at_approval` predates
the change becomes `LIB-02` and needs re-review. This is the audit trail that makes "approved"
mean something specific rather than "someone looked at it once".

**Periodically (recommend monthly)**: reconcile the register against what the sending tool
actually contains. A template edited directly in HubSpot without a register update is
`LIB-06` — and it is invisible to the daily run, because the hash simply fails to match and
the message silently falls into Lane 2. That degrades quietly rather than failing loudly,
which is why the reconciliation has to be scheduled rather than incidental.

## Open questions

1. **Can HubSpot template IDs be recovered from sent mail?** Lane assignment currently relies
   on body hashing alone. If the sending tool stamps an identifiable header, matching becomes
   far more robust and drift detection gets cheaper. Worth checking before building the hasher.
2. **Do reps have edit rights on templates at send time?** If yes, HF-16 is a high-volume
   finding and the diff path is the main event rather than an edge case. If no, it is rare and
   Lane 1 carries most of the traffic. This materially changes the expected finding mix.
3. **Who owns template approval today?** `LIB-04` presumes a named approver exists. If approval
   is currently informal, populating `approved_by` retrospectively may be impossible and the
   register starts with most rows at `never-reviewed`.
