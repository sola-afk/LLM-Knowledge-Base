# Email Monitoring — programme definition

Compliance supervision of the **Intercom email channel**, applying the Call
Monitoring programme's assessment criteria to email.

> [!important] Where the record lives
> **The [Email Monitoring Asana project](https://app.asana.com/1/1211257642526605/project/1217717281350976) is the system of record.**
> Findings, grades, evidence links and management responses live there — not in
> this repo. This directory holds the *method* only, so a run is reproducible.
>
> Decided 30 Sep 2026. The reasoning is about where the work is *used*, not
> about durability: escalations are triaged, commented on and closed by the
> compliance team in Asana, so that is where the live state of a finding
> actually is. A markdown report in git is a snapshot that goes stale the
> moment someone responds to a finding.
>
> Written reports under `compliance-wiki/output/` remain useful as the
> period narrative — volumes, SLA rates, cross-run trends — which Asana
> cannot express. They are commentary on the record, not the record.

---

## 1. Scope — what this programme covers

| | Call Monitoring | **Email Monitoring** |
|---|---|---|
| Channel | GTM / sales calls | Intercom email (`support@kota.io`, `benops@kota.io`) |
| Population | Sales conversations | CX Platform + BenOps support email |
| People | Karl O'Brien, Paul O'Hanlon, Charlie Blake, Simon Ward, Dan McAvinue | Michael Nikeenok, Clara Hughes, Michelle Jenei, Isabel Brooks, Simon Ward |
| Dominant risk | Advice-giving by unqualified staff (MCC) | Service failure, data protection, consent |

These are **different populations with different risk profiles**. The only
deliberate overlap is the grading vocabulary, kept so findings compare across
channels.

### Not in scope
- Provider back-office traffic (Allianz claims admin, Irish Life scheme ops) — high volume, low conduct risk
- Automated `noreply@kota.io` platform notifications, except as a volume signal
- Intercom-as-vendor correspondence (swept separately in Gmail; nil returns to date)

---

## 2. Assessment criteria

Carried across **unchanged** from the `Call Monitoring 2026` sheet and the
`☎️ Call Supervision Audit` Notion database.

| Call monitoring field | Email equivalent |
|---|---|
| Date of compliance review | Same |
| Date of call | Date of email |
| Kota attendees | Kota handler(s) |
| Client/Prospect | Same |
| Call purpose | Email purpose |
| **Recording consent** | **Regulatory disclosure** — was the CBI/FCA footer on the outbound? |
| Issues | Same |
| Training opportunity / gap | Same |
| Actions | Same |
| Responses from management | Same |
| FactFind done and sent | Same (rarely applicable — email sample is not advised sales) |
| SOS done and sent | Same |

**Recording consent has no email analogue.** Regulatory disclosure is the
equivalent channel check and is the only substituted field.

### Risk categories (unchanged)
`Consumer Protection Code` · `Minimum Competency Code` · `Data Protection`

---

## 3. Grading

Two scales are in play. Use the Notion 1–5 scale in written assessment; record
the Asana enum in the project.

| Notion / assessment | Asana `Grade` field | Section |
|---|---|---|
| 1 = Pass | *(blank)* | Resolved/False Positives |
| 2 = Pass with comments | Minor Correction | Resolved/False Positives |
| 3 = Fail | Fail | Escalated |
| 4 = Fail with referral | Fail | Escalated |
| 5 = Severe Fail | Severe Fail | Escalated |
| — | False Positive | Resolved/False Positives |

> [!note] Two known gaps in the Asana enum
> It has **no Pass option**, so a clean review reads as blank — fine for triage,
> weak as an audit record of *what was reviewed and found clean*.
> It has **no "Fail with referral"**, so a 4 displays as plain `Fail`. Put the
> distinction in the task body.

**False Positive requires a recorded rationale** in a task comment. Precedent:
the 27 Aug misdelivered-letter finding was closed as FP with *"Naoise confirmed
that he was only listed as an admin on the account. Trevors actual details were
not shared."* That is the standard — a grade change without a reason is not a
closed finding.

---

## 4. Running a sweep

### 4.1 Pull the population

Intercom `search_conversations`, filtered to email, from the last review date:

```
source_type: "email"
created_at:  { operator: ">", value: <unix ts of period start> }
per_page:    150
```

Page through with `starting_after` from `pages.next.starting_after` until
exhausted. **Reconcile the row count against `total_count`** — a run that
doesn't match is not a full sweep.

Responses exceed the tool's token limit and auto-save to file. Work from those
files, not from context.

### 4.2 Build the digest

```bash
for i in $(seq 1 N); do
  jq -r '.conversations[] | [
    .id, (.created_at|todate), (.source.author.email // "?"), (.source.author.type // "?"),
    .state, ((.tags.tags // []) | map(.name) | join("|")),
    (.sla_applied.sla_name // "-"), (.sla_applied.sla_status // "-"),
    (.custom_attributes["Type of user"] // "-"),
    (.custom_attributes["Provider"] // "-"),
    (.custom_attributes["PL: Issue Type"] // "-"),
    ((.source.subject // "") | gsub("<[^>]*>";"") | gsub("[\r\n\t]";" ") | .[0:130])
  ] | @tsv' pages/p$i.json
done | sort -u -t$'\t' -k1,1 > digest.tsv
```

### 4.3 Select the sample

Filter to **customer-facing**: `Type of user` in `Employer`, `Employee`,
`New Customer`, excluding `noreply@kota.io`. Then risk-weight towards:

- Pension transfers, auto-enrolment / My Future Fund, contribution changes
- Cancellations, opt-outs, enrolments the member doesn't recall
- Anything tagged `Complaint / Escalation`
- Personal data corrections, access or deletion requests
- Outbound campaigns and lifecycle templates

Scan subject lines for: `complain|GDPR|data correction|DSAR|erasure|rectif|breach|consent|vulnerab|ombudsman|FSPO|escalat|fraud|mis-sold|transfer|advice|recommend|opt out|cancel`

**The sample is risk-weighted, not random.** It never supports a channel-wide
pass rate — say so in every report.

### 4.4 Read the threads

`get_conversation` per thread. Most parts are bot noise; extract human content
with `extract.jq` (see `scripts/`).

### 4.5 Cross-reference before escalating

Any finding that says someone gave a wrong or unqualified answer **must** be
checked against approved content first. This has twice changed the finding:

| Source | Where |
|---|---|
| Intercom Help Centre articles | `search_articles` / `get_article` — the source Fin and CX use |
| Approved script library | Notion, under `MCC Supervision` |
| Irish AE content | Notion "AutoEnrolment in Ireland"; Help Centre art. 14470927 |
| Pension transfer-in | Help Centre art. 9145103 |
| Renewals | Notion "Health Insurance Renewals SOP" + "Renewals checklist" |
| Incident handling | Notion "Mixed employees data incident" (Dec 2025); Cybersecurity page |

The question is always: **was the answer on script, off script, or contradicting
script?** Off-script and contradicting are different findings with different
fixes — one needs a script written, the other needs a correction issued.

### 4.6 Follow up on prior escalations

Before writing anything new, check what happened to the last run's escalations.
Re-pull those conversations and read the Asana comments.

This has been the most valuable part of the programme. It has shown findings
that **worked** (the MCC boundary point held), findings **correctly overturned**
(the misdelivered letter), and findings **fixed for the case but not the cause**
(pension transfers failed again within a week).

---

## 5. Deploying a run

1. **One Asana task per assessed thread.** Name as
   `<Handler> — <Client> — <Purpose> (DD/MM)`, handler first so it survives
   truncation in the list view.
2. Populate the **`Link`** field with the Intercom permalink
   (`https://app.intercom.com/a/apps/euajb704/conversations/<id>`) and the
   **`Grade`** field.
3. Body carries the assessment in the call-monitoring column order, ending with
   an empty **Response from management**.
4. Place in `Escalated` or `Resolved/False Positives` — the project runs two
   sections only.
5. Post the run summary as a **project status update**, linking the escalated
   tasks by GID.

### Asana reference

| | |
|---|---|
| Project | `1217717281350976` |
| Section — Escalated | `1217717006901149` |
| Section — Resolved/False Positives | `1217717316141114` |
| Field — Link (text) | `1217724491347342` |
| Field — Grade (enum) | `1217724491347344` |
| Grade: False Positive / Severe Fail / Fail / Minor Correction | `…345` / `…346` / `…347` / `…348` |

---

## 6. Known limitations

- **Sample is risk-weighted**, never random. No channel-wide pass rate.
- Classification of unsampled threads rests on subject lines and opening
  messages; relevance emerging later in a chain is not caught.
- SLA figures are Intercom's own `sla_applied.sla_status`, not recalculated.
- Attachments are not opened. Where a finding depends on one, say so and grade
  conservatively until it's read.
- Reviews have run 18 days late. Gaps are themselves a finding — a late review
  surfaces items already closed.

---

## 7. Run history

| Period | Population | Assessed | Escalated |
|---|---|---|---|
| W34 — 17–21 Aug 2026 | 434 | 9 | 2 |
| W35 — 24–28 Aug 2026 | 594 | 5 | 2 |
| 29 Aug – 15 Sep 2026 (catch-up) | 1,484 | 3 | 2 |

Per-period reports, with volumes, SLA rates by tier and the trend narrative:

- `compliance-wiki/output/intercom-email-monitoring-2026-W34.md`
- `compliance-wiki/output/intercom-email-monitoring-2026-W35.md`
- `compliance-wiki/output/intercom-email-monitoring-2026-W36-38.md`

The findings themselves, with grades and current triage state, are in the
Asana tasks.
