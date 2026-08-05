---
title: Intercom CX Compliance Eval — Run 2 (sample of 10, closed conversations)
created: 2026-08-05
type: eval
channel: intercom
run_type: dry-run
population: CX (team 5690482 · PL-CX Customer Ticket) · source_type=email · state=closed
conversations_pulled: 10
complaints_found: 2
complaints_graded: 2
assessed_full_transcript: 1
conversations_flagged: 0
---

# Intercom CX Compliance Eval — Run 2 (sample of 10)

Second run, after the production-readiness amendments. Deliberately a **different slice** from
run 1: `state: closed`, so complaint lifecycles are complete and the HF-24 clock can be computed
end-to-end rather than left running.

**Result: the six fixes from run 1 all hold, HF-24 now grades, the complaints criteria did not
over-fire, and two further defects surfaced — one in the tooling I wrote, one in the spec.**

## What changed since run 1

| Amendment | Status |
|---|---|
| Complaints deadlines researched and populated (`research-complaints-handling.md`) | **HF-23/24 now grade** — 0 `{{TO VERIFY}}` placeholders remain |
| `part_type` split (`comment` graded, `note` context) | Held |
| Identity by email domain, not `author.type` | **Held, and load-bearing — fired on 6/10** |
| `Brand` vs `ticket_type` precedence | Held; no conflicts in this slice |
| `PL:Topic` fail-closed | Held; fired on 1/10 |
| HF-27 / HF-28 promoted from proposed to live | In force |
| `tools/extract.py` field projection | **Replaces ad-hoc jq.** Run 1 was hand-extracted per conversation; this run is reproducible |

## Triage — all 10

`total_count` for these filters: **4,412**.

| Conversation | Issue type | Topic | Provider | User | SLA | Parts | Flags |
|---|---|---|---|---|---|---|---|
| `215475084404001` | Request / Change | ER: Employee Management | — | Employer | missed | 87 | fin · kota-as-user |
| `215475247328292` | **Complaint / Escalation** | ER: Benefit - Pension | — | Employer | missed | 43 | fin · **ASSESSED — Pass** |
| `215474821854757` | **Complaint / Escalation** | EE: Benefit - Pension | Irish Life | Employer | hit | 52 | fin · clock graded |
| `215475031234261` | Request / Change | EE: Benefit - Health | Irish Life | Employee | missed | 87 | fin |
| `215474090892333` | Request / Change | ER: Benefit - Pension | Smart Pension | Employer | — | 34 | kota-as-user |
| `215475286451340` | Other / Internal | — | — | Employer | missed | 35 | fin · **no topic** · kota-as-user |
| `215475126305717` | Question / inquiry | ER: Billing & Finance | — | Employer | missed | 78 | kota-as-user |
| `215474495913394` | Request / Change | ER: Benefit - Pension | Smart Pension | Employer | active | 23 | kota-as-user |
| `215475300729931` | Request / Change | ER: Benefit - Pension | Smart Pension | Employer | active | 14 | kota-as-user |
| `215475300675136` | Request / Change | ER: Benefit - Pension | Smart Pension | Employer | active | 14 | kota-as-user |

**`kota-as-user` fired on 6 of 10.** Under run 1's spec — "only `admin` parts are Kota conduct" —
the majority of this sample would have had its Kota-authored content skipped. This was the most
consequential of the run 1 fixes.

Fin present on 6/10 here, against 10/10 in run 1. Both well above the "dormant" claim the first
draft made off two chat conversations.

---

## Complaints — HF-23 and HF-24 now gradeable

Both complaints in this sample are **platform-classified**, so HF-23 does not fire — the
classification obligation was met. HF-24 computed against the CPC clock:

| | `215475247328292` | `215474821854757` |
|---|---|---|
| Classified as complaint | Yes | Yes |
| Internal SLA | **missed** | hit |
| Acknowledgement | 2 business days | 0 business days (same day) |
| Final response / close | 3 business days | 14 business days |
| **HF-24 (CPC 5 / 20 / 40 bd)** | **ok** | **ok** |

### The SLA trap, demonstrated

`215475247328292` has `sla_status: missed` and is **fully compliant** with the CPC deadlines —
acknowledged in 2 business days against a 5-day requirement, closed in 3 against 40.

The internal SLA it missed is `FRT 8h / NRT 8h / TTR 24h`, which is roughly **40× tighter** than
the regulatory deadline. Reporting `sla_status` as an HF-24 breach would have produced a false
positive on a well-handled complaint. The criteria's warning against substituting one for the
other is now evidenced, not just asserted.

Neither complaint breached. **Recorded as clean passes, not as an absence of findings** — the
criteria not over-firing on two real complaints is the useful result here.

---

## Conversation `215475247328292` — Pass

**Subject**: Re: Kota / Clonbio - Kickoff
**Substance**: employer has reconciled payroll against pension contributions collected by Kota for
Irish Life and found sustained discrepancies across multiple entities ("None are correct at this
stage"), going back to a December 2025 reconciliation. Requests a call to resolve before year end.
**Kota author**: Claudia Correa — script pathway (unqualified)
**Bot-authored graded parts**: 0
**Permalink**: https://app.intercom.com/a/apps/euajb704/conversations/215475247328292
**Grade**: **Pass**

Claudia's only customer-facing (`comment`) content is logistics:

> "I just replied to the other email you sent. Please check it out and we´ll decide how to proceed."

No regulated-product content, no recommendation, no mechanics, no pricing. Correctly a Pass despite
an unqualified author on a pension-topic complaint — which is the discrimination the criteria are
supposed to make.

---

## New defects found

### 1. Tooling bug — falsy-zero on same-day acknowledgement *(fixed this run)*

`extract.py clock` reported **"NO REPLY YET"** for `215474821854757`, whose acknowledgement was
**same-day** — the best possible outcome. `business_days()` returned `0`, which is falsy, so the
truthiness test conflated "replied in zero days" with "never replied".

In production this would have flagged the **fastest-handled** complaints as unacknowledged. Fixed
by testing `is None` rather than truthiness; both conversations re-run and a regression check on the
2-business-day case confirms the fix.

Worth noting it took a real same-day complaint to expose it — no amount of spec review would have.

### 2. Spec gap — linked and split conversations

`215475247328292` contains an internal note reading:

> "This is managed here: 119503246"

The substantive handling **moved to a different conversation**. This assessment therefore saw a
fragment, and graded Pass on a fragment. Any regulated content lives in the linked conversation,
which the pipeline never fetched.

Intercom exposes `linked_objects` on the conversation (empty here — the reference is free text in a
note, not a structured link). **The spec has no handling for either.** Recommended: parse notes for
conversation-ID references, follow `linked_objects`, and assess a linked set as one unit. Until
then, a Pass on a cross-referenced conversation is **provisional** and should be reported as such.

### 3. Detection gap — customer attributes advice the agent cannot see

In the same conversation the customer writes:

> "Claudia has reviewed the Clonbio Group contributions, and I have made the necessary changes to
> Kota for August **as she suggested**."

Claudia is script-pathway. A customer stating that an unqualified staff member *suggested*
contribution changes is strong evidence of HF-12 conduct — but it is in a `user` part, and per the
attribution rule a finding may only cite Kota-authored text. Flagging Claudia on the customer's
characterisation would breach R1.

That discipline is correct, and it leaves a real gap: the advice happened somewhere the agent cannot
see — a call, a linked conversation, or a direct email. Proposing:

**SF-20 — Customer attributes advice or a recommendation to Kota staff.** Soft signal. Trigger:
`user`-authored content containing "as you suggested", "as advised", "you recommended", "you told me
to", naming a Kota staff member, on a regulated-product matter. **Not a finding against the staff
member** — a pointer that regulated conduct occurred outside the assessed artefact, warranting a
cross-channel look. Escalates if the named person is unqualified for the product.

This is the first criterion that is explicitly a *cross-channel* signal, and it is the kind of thing
only a live run surfaces.

---

## Findings withdrawn after reassessment

Per R5.

| Conversation | Original finding | Why withdrawn | Reassessment date |
|---|---|---|---|
| `215474821854757` | HF-24 — acknowledgement missing | Tooling bug, not conduct. Same-day acknowledgement misread as no reply (falsy zero). Fixed in `tools/extract.py` | 2026-08-05 |

---

## Coverage and honesty about it

- **10 triaged**, all in scope, none excluded.
- **2 complaints, both graded** on HF-23 and HF-24 — the criteria that could not run at all in run 1.
- **1 assessed on full content.** The other 9 are triaged only and are **not** recorded as passes.
- Run 1's single Fail (`215475238289349`) remains the only conduct finding across 20 conversations
  triaged. Two runs is not a base rate; both were purposively sampled, not random.

## Remaining blockers

| Blocker | Status |
|---|---|
| MCC register missing CX staff | **Still open, still the binding constraint.** Claudia Correa resolves (script pathway); Michael Nikeenok from run 1 does not appear at all. Until Compliance extends the register, unrecognised CX authors fail closed and generate noise |
| CX / CS team enumeration | Still partial — only `5690482` confirmed |
| Asana destination | Still undecided; nothing can be filed |
| CPC 2025 line-check against S.I. 81/2025 | Deadlines are sourced and consistent but not statute-checked. Fine for dry runs, needed before regulator-facing escalation |
| Linked-conversation handling | New, from this run |

## Open questions for the Designer

1. **Should a cross-referenced conversation block a Pass?** Grading a fragment as Pass is
   optimistic. Recommend Pass-with-comments plus a "linked set not assessed" note until linked
   handling exists.
2. **`business_days()` ignores public holidays.** Fine at 2bd against a 5bd limit; not fine at 39bd
   against 40. Needs an Irish/UK holiday calendar before any near-deadline escalation.
3. **`Other / Internal` issue type with an `Employer` user** (`215475286451340`) — is that
   genuinely internal, or a misclassification? The exclusion rule keys on `Type of user: Internal`,
   which this is not, so it was assessed. Worth a rule.
