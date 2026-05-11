---
title: Asana Task Spec — Call Monitoring Queue Manager
created: 2026-05-08
updated: 2026-05-08
type: spec
---

# Asana Task Spec — Call Monitoring Queue Manager

Full specification for creating a task in the Asana Call Monitoring project for each flagged call.

## When to create a task

**Only Grade 3 (Fail), Grade 4 (Fail w/ referral), and Grade 5 (Severe Fail) generate tasks.** Grade 1 (Pass) and Grade 2 (Pass with comments) do **not** create tasks — they live in the Evaluator's report only. Asana is the triage queue for second-line compliance; passes do not need triage.

## Quote-fidelity rule (Issues field)

Every finding listed in the `Issues` custom field must include the **EXACT verbatim transcript quote**. No paraphrasing, no AI summaries, no "the speaker said something like". The quote is the search key: compliance pastes it into the Fireflies search bar to jump to the moment in the recording. If the transcript renders a word oddly (e.g. "Boop" for "BUPA", "Booba" for "BUPA"), preserve that exact rendering — it's what the Fireflies search will match. Per-second timestamps are unreliable through the current MCC transcript tools, so the verbatim quote is the source of truth.

## Assignee rule

**Do not assign a task on creation.** Second-line compliance owns the triage decision and routes the task themselves. Auto-assigning would short-circuit that step. The task lands in the appropriate section (department-based, or Escalated for Severe Fail / ES-01/02/03 / HF-03), with followers and @-mentions set per the rules below — but the `assignee` field is left unset.

## create_tasks call structure

```json
{
  "default_project": "1213240137041729",
  "tasks": [
    {
      "name": "[Grade] — [Client/Prospect name] — [YYYY-MM-DD]",
      "project_id": "1213240137041729",
      "section_id": "<section GID — see routing below>",
      "due_on": "YYYY-MM-DD",
      "followers": "1213006028880034,1212984665985179",
      "custom_fields": "{\"1213240170325716\":\"<grade option GID>\",\"1213240170325723\":\"<call purpose>\",\"1213240170325728\":\"<verbatim-quote findings, see below>\",\"1213240170325733\":\"<regulatory reference>\",\"1213240170325738\":\"<fireflies URL>\",\"1214635377742250\":\"<kota staff name + MCC status>\",\"1214635377742252\":\"<prospect/client company name>\"}",
      "html_notes": "<body>...</body>"
    }
  ]
}
```

> Note: `assignee` field is intentionally omitted.

## Section routing

| Condition | Section name | Section GID |
|---|---|---|
| Severe Fail OR ES-01/02/03 fired | **Escalated** (overrides department) | `1213240137041730` |
| Department = GTM | Go-to-Market | `1213240137041732` |
| Department = CS / CX | Customer Success | `1213240137041733` |
| Department = Benefits | Benefits | `1213240137041734` |

## Followers (always set)

- Sola Olaniyan (`1213006028880034`) — Compliance Manager
- Trevor Gardiner (`1212984665985179`) — MCC supervisor
- Add Simon Ellis (`1213214965151657`) when escalation conditions fire (see below)

## Custom field values

### Grade (`1213240170325716`)
| Audit grade | Asana option | Option GID |
|---|---|---|
| 2 — Pass with comments | Pass | `1213240170325717` |
| 3 — Fail | Fail | `1214635377742249` |
| 4 — Fail w/ referral | Fail | `1214635377742249` |
| 5 — Severe Fail | Severe Fail | `1213240170325718` |

### Call Purpose (`1213240170325723`) — text
One-line description of the call's purpose, e.g.:
- `Pension scheme setup — new client onboarding`
- `PMI renewal — existing client`
- `Health insurance demo — prospect`

### Issues (`1213240170325728`) — text
One block per criterion. Each block names the criterion ID, a short label, and the **EXACT verbatim transcript quote** that triggered it. The quote is the search key — compliance pastes it into the Fireflies search bar to jump to that moment. Do not paraphrase, do not summarise, do not "clean up" the transcript. If Fireflies transcribed "BUPA" as "Boop" or "Booba", preserve that exact rendering — that's what the Fireflies search will match.

Format (newline-separated blocks):
```
HF-01 (explicit recommendation): "I would recommend setting employer contribution to 1.5%"

HF-08 (absolute certainty claim): "everything's covered, full stop"

SF-12 (emotive marketing): "this is a wild west market right now"
```

Optional: include a `~MM:SS` timestamp anchor at the end of each block when the Fireflies summary tool exposes one (e.g. via `fireflies_get_summary` action-items or topic ranges). But the quote, not the timestamp, is the authoritative search key.

### Requirement Breached (`1213240170325733`) — text
The specific regulation(s) breached. Use the references from `Researcher/req-detection-criteria.md`. Examples:
- `CBI Minimum Competency Code 2017 — provision of information on retail financial product by unqualified person`
- `CBI Consumer Protection Code 2025 Part 3 — clear, fair, accurate, not misleading`
- `IDR S.I. 229/2018 Reg. 23(1)(e) — disclosure of whether advice is given`
- `FCA COBS 9 / PERG 8.24–8.30 — personal recommendation perimeter`
- `IDD Art. 17(2) / ICOBS 2.2.2R — communications fair, clear, not misleading`

If multiple regulations apply, separate with semicolons.

### Recording Link (`1213240170325738`) — text
Direct Fireflies URL to the meeting recording, e.g.:
`https://app.fireflies.ai/view/<meeting-id>`

### Kota Staff (`1214635377742250`) — text
Name and MCC/authorisation status of the Kota-side speaker(s) on the call, e.g.:
- `Karl O'Brien (Script pathway)`
- `Matthew Brennan (New Entrant — supervised by Trevor Gardiner)`
- `Paul O'Hanlon (Qualified — APA PMI)`

If multiple Kota staff were on the call, separate with semicolons.

### Prospect/Client (`1214635377742252`) — text
Company name of the prospect or client, e.g.:
- `Prospect Corp Ltd`
- `Acme HR Solutions`

## html_notes template

Construct as valid XML with a single `<body>` root.

```xml
<body>
<h1>Call Details</h1>
<ul>
  <li><strong>Client / Prospect:</strong> [Client or prospect company name]</li>
  <li><strong>Call date:</strong> [YYYY-MM-DD HH:MM]</li>
  <li><strong>Duration:</strong> [MM] minutes</li>
  <li><strong>Department:</strong> [GTM / Benefits / CS/CX]</li>
</ul>

<h1>Participants</h1>
<ul>
  <li><strong>Kota staff:</strong> [Name — Role — MCC status (Qualified / New Entrant / Script / Unregistered)]</li>
  <li><strong>Customer / Prospect:</strong> [Name, Company]</li>
</ul>

<h1>Compliance Findings</h1>
<ul>
  <li>
    <strong>[Criterion ID] — [Criterion name] — [HH:MM:SS]</strong><br/>
    <em>Transcript:</em> "[exact quote from transcript]"<br/>
    <em>Speaker:</em> [Name] ([MCC status])<br/>
    <em>Regulation:</em> [matches the Requirement Breached field]<br/>
    <em>Severity:</em> High / Medium / Low
  </li>
</ul>

<h1>Training / Gap</h1>
<p>[What training or process change would prevent recurrence]</p>

<h1>Actions Required</h1>
<ol>
  <li>[Specific action, owner, deadline]</li>
</ol>

<hr/>
<p>
  For action: <a data-asana-gid="[ASSIGNEE GID]"/><br/>
  MCC Supervisor: <a data-asana-gid="1212984665985179"/> (Trevor Gardiner)
  [If escalation applies:] <br/>Escalated to: <a data-asana-gid="1213214965151657"/> (Simon Ellis)
</p>
</body>
```

## Escalation: when to @-mention Simon Ellis

Add `1213214965151657` as a follower and include `<a data-asana-gid="1213214965151657"/>` in the html_notes when **any** of:
- Grade = `Severe Fail` (Asana option `1213240170325718`)
- ES-01 (customer distress / complaint)
- ES-02 (claim or coverage dispute)
- ES-03 (out-of-scope commitment made by Kota staff)
- HF-03 (firm capability or regulatory status misrepresented)
- HF-00 triggered for an **unregistered** speaker (Kate Fullen, or any unrecognised name)

Note: when these escalation conditions fire, also place the task in the **Escalated** section (`1213240137041730`) instead of the department section.

## Full worked example

**Scenario**: GTM call with Karl O'Brien (script pathway) who described PMI dental cover limits to a prospect. Graded Fail (3). No assignee — compliance triages.

```json
{
  "default_project": "1213240137041729",
  "tasks": [
    {
      "name": "Fail — Prospect Corp Ltd — 2026-05-08",
      "project_id": "1213240137041729",
      "section_id": "1213240137041732",
      "due_on": "2026-05-08",
      "followers": "1213006028880034,1212984665985179",
      "custom_fields": "{\"1213240170325716\":\"1214635377742249\",\"1213240170325723\":\"PMI demo — new prospect\",\"1213240170325728\":\"HF-10 (unqualified speaker describing cover details): \\\"The cash plan covers dental up to €500 per year and optical up to €150.\\\"\",\"1213240170325733\":\"CBI Minimum Competency Code 2017 — provision of information on retail financial product by unqualified person\",\"1213240170325738\":\"https://app.fireflies.ai/view/abc123\",\"1214635377742250\":\"Karl O'Brien (Script pathway)\",\"1214635377742252\":\"Prospect Corp Ltd\"}",
      "html_notes": "<body><h1>Call Details</h1><ul><li><strong>Client / Prospect:</strong> Prospect Corp Ltd</li><li><strong>Call date:</strong> 2026-05-08 10:30</li><li><strong>Duration:</strong> 24 minutes</li><li><strong>Department:</strong> GTM</li></ul><h1>Participants</h1><ul><li><strong>Kota staff:</strong> Karl O'Brien — Account Executive — Script pathway (unqualified)</li><li><strong>Customer / Prospect:</strong> Jane Smith, Prospect Corp Ltd</li></ul><h1>Compliance Findings</h1><ul><li><strong>HF-10 — Cover details by unqualified speaker</strong><br/><em>Verbatim transcript quote (paste into Fireflies search):</em> \"The cash plan covers dental up to €500 per year and optical up to €150.\"<br/><em>Speaker:</em> Karl O'Brien (Script pathway — unqualified)<br/><em>Regulation:</em> CBI MCC 2017 — provision of information on retail financial product by unqualified person<br/><em>Severity:</em> High</li></ul><h1>Training / Gap</h1><p>Karl is on the prescribed script pathway and described specific PMI cover limits to a prospect. This is a MCC-regulated activity that requires an APA (PMI) or QFA qualification.</p><hr/><p>MCC Supervisor: <a data-asana-gid=\"1212984665985179\"/> (Trevor Gardiner)</p></body>"
    }
  ]
}
```

**Severe Fail variant**: same call but graded 5 (e.g. customer was misled on firm capability) — change `section_id` to `1213240137041730` (Escalated) and the Grade option GID to `1213240170325718`. Add Simon Ellis to the followers list and @-mention him in the body. Assignee still omitted.
