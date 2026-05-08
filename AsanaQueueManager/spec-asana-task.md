---
title: Asana Task Spec — Call Monitoring Queue Manager
created: 2026-05-08
updated: 2026-05-08
type: spec
---

# Asana Task Spec — Call Monitoring Queue Manager

Full specification for creating a task in the Asana Call Monitoring project for each flagged call.

## When to create a task

Create a task for every call graded **Pass with comments (2), Fail (3), Fail w/ referral (4), or Severe Fail (5)**. Do not create tasks for Grade 1 (clean Pass / no findings).

## create_tasks call structure

```json
{
  "default_project": "1213240137041729",
  "tasks": [
    {
      "name": "[Grade] — [Client/Prospect name] — [YYYY-MM-DD]",
      "project_id": "1213240137041729",
      "section_id": "<section GID — see routing below>",
      "assignee": "<assignee GID — see routing below>",
      "due_on": "YYYY-MM-DD",
      "followers": "1213006028880034,1212984665985179",
      "custom_fields": "{\"1213240170325716\":\"<grade option GID>\",\"1213240170325723\":\"<call purpose>\",\"1213240170325728\":\"<criterion IDs + spans>\",\"1213240170325733\":\"<regulatory reference>\",\"1213240170325738\":\"<fireflies URL>\"}",
      "html_notes": "<body>...</body>"
    }
  ]
}
```

## Section routing

| Condition | Section name | Section GID |
|---|---|---|
| Severe Fail OR ES-01/02/03 fired | **Escalated** (overrides department) | `1213240137041730` |
| Department = GTM | Go-to-Market | `1213240137041732` |
| Department = CS / CX | Customer Success | `1213240137041733` |
| Department = Benefits | Benefits | `1213240137041734` |

## Assignee routing

| Section | Assignee | GID |
|---|---|---|
| Go-to-Market | Matthew Brennan | `1214070419259752` |
| Customer Success | Trevor Gardiner | `1212984665985179` |
| Benefits | Trevor Gardiner | `1212984665985179` |
| Escalated | Simon Ellis | `1213214965151657` |

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
Comma-separated list of triggered criterion IDs with timestamp + brief context, e.g.:
- `HF-01 (explicit recommendation at 04:23: "I would recommend setting employer contribution to 1.5%"), HF-08 (absolute certainty claim at 11:47), SF-12 (emotive marketing language x2)`

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

**Scenario**: GTM call with Karl O'Brien (script pathway) who described PMI dental cover limits to a prospect, and gave no recording disclosure. Graded Fail (3).

```json
{
  "default_project": "1213240137041729",
  "tasks": [
    {
      "name": "Fail — Prospect Corp Ltd — 2026-05-08",
      "project_id": "1213240137041729",
      "section_id": "1213240137041732",
      "assignee": "1214070419259752",
      "due_on": "2026-05-08",
      "followers": "1213006028880034,1212984665985179",
      "custom_fields": "{\"1213240170325716\":\"1214635377742249\",\"1213240170325723\":\"PMI demo — new prospect\",\"1213240170325728\":\"HF-00 (unqualified speaker describing cover details at 06:12), HF-06 (no recording consent opener), HF-10 (cover details by script-pathway rep)\",\"1213240170325733\":\"CBI Minimum Competency Code 2017 — provision of information on retail financial product by unqualified person; CPC 2025 Part 3 — recording consent\",\"1213240170325738\":\"https://app.fireflies.ai/view/abc123\"}",
      "html_notes": "<body><h1>Call Details</h1><ul><li><strong>Client / Prospect:</strong> Prospect Corp Ltd</li><li><strong>Call date:</strong> 2026-05-08 10:30</li><li><strong>Duration:</strong> 24 minutes</li><li><strong>Department:</strong> GTM</li></ul><h1>Participants</h1><ul><li><strong>Kota staff:</strong> Karl O'Brien — Account Executive — Script pathway (unqualified)</li><li><strong>Customer / Prospect:</strong> Jane Smith, Prospect Corp Ltd</li></ul><h1>Compliance Findings</h1><ul><li><strong>HF-06 — No recording disclosure — 00:00</strong><br/>No consent opener given in first 60 seconds.<br/><em>Regulation:</em> CPC 2025; IDR S.I. 229/2018 Reg. 23<br/><em>Severity:</em> Medium</li><li><strong>HF-10 — Cover details by unqualified speaker — 06:12</strong><br/><em>Transcript:</em> \"The cash plan covers dental up to €500 per year and optical up to €150.\"<br/><em>Speaker:</em> Karl O'Brien (Script pathway — unqualified)<br/><em>Regulation:</em> CBI MCC 2017 — provision of information on retail financial product by unqualified person<br/><em>Severity:</em> High</li></ul><h1>Training / Gap</h1><p>Karl is on the prescribed script pathway and described specific PMI cover limits to a prospect. This is a MCC-regulated activity that requires an APA (PMI) or QFA qualification.</p><h1>Actions Required</h1><ol><li>Trevor Gardiner to review recording and confirm findings by 2026-05-09.</li><li>Karl to be reminded of script boundaries and MCC regulated activity definition.</li><li>Discuss at next MCC supervision session; document in supervision log.</li></ol><hr/><p>For action: <a data-asana-gid=\"1214070419259752\"/> (Matthew Brennan)<br/>MCC Supervisor: <a data-asana-gid=\"1212984665985179\"/> (Trevor Gardiner)</p></body>"
    }
  ]
}
```

**Severe Fail variant**: same call but graded 5 (e.g. customer was misled on firm capability) — change `section_id` to `1213240137041730` (Escalated), `assignee` to `1213214965151657` (Simon Ellis), and the Grade option GID to `1213240170325718`. Keep Matthew Brennan and Trevor Gardiner as followers and add Simon Ellis to the followers list.
