---
title: Asana Task Spec — Call Monitoring Router
created: 2026-05-08
type: spec
---

# Asana Task Spec — Call Monitoring Router

Full specification for creating a task in the Asana Call Monitoring project for each flagged call.

## When to create a task

Create a task for every call graded **Pass with comments (2), Fail (3), Fail w/ referral (4), or Severe Fail (5)**. Do not create tasks for Grade 1 (Pass / no findings).

## create_tasks call structure

```json
{
  "default_project": "1213240137041729",
  "tasks": [
    {
      "name": "[Grade label] — [Client/Prospect name] — [YYYY-MM-DD]",
      "project_id": "1213240137041729",
      "section_id": "<department section GID — see CONTEXT.md>",
      "assignee": "<see routing logic in CONTEXT.md>",
      "due_on": "YYYY-MM-DD",
      "followers": "1213006028880034,1212984665985179",
      "custom_fields": "{\"1213240170325716\":\"<recording consent option GID>\",\"1213240170325723\":\"<call purpose>\",\"1213240170325728\":\"<issues summary>\",\"1213240170325733\":\"<training gap>\",\"1213240170325738\":\"<actions>\"}",
      "html_notes": "<body>...</body>"
    }
  ]
}
```

## html_notes template

Construct the `html_notes` field as valid XML with a single `<body>` root. Use the structure below, substituting values from the Fireflies transcript and the Evaluator's findings.

```xml
<body>
<h1>Call Details</h1>
<ul>
  <li><strong>Client / Prospect:</strong> [Client or prospect company name]</li>
  <li><strong>Call date:</strong> [YYYY-MM-DD HH:MM]</li>
  <li><strong>Duration:</strong> [MM] minutes</li>
  <li><strong>Fireflies link:</strong> [paste Fireflies meeting URL]</li>
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
    <em>Regulation:</em> [e.g. CBI MCC 2017 — regulated activity by unqualified person; CPC 2025 Part 3 — clear/fair/not misleading]<br/>
    <em>Severity:</em> High / Medium / Low
  </li>
</ul>

<h1>Training / Gap</h1>
<p>[What training or process change would prevent recurrence — e.g. "Script-pathway rep deviated to cover detail; script requires update and rep needs refresher on MCC regulated activity definition."]</p>

<h1>Actions Required</h1>
<ol>
  <li>[Specific action, owner, deadline — e.g. "Trevor to review call recording and confirm script deviation by YYYY-MM-DD"]</li>
  <li>[Additional action if needed]</li>
</ol>

<hr/>
<p>
  For action: <a data-asana-gid="[ASSIGNEE GID]"/>
  CC: <a data-asana-gid="1212984665985179"/> (Trevor Gardiner — MCC Supervisor)
  [If Simon Ellis escalation applies:] <a data-asana-gid="1213214965151657"/> (Simon Ellis)
</p>
</body>
```

## Custom fields — values to populate

### Recording Consent
- Set to `1213240170325717` (Yes) if a valid recording disclosure was given at the start of the call.
- Set to `1213240170325718` (No) if HF-06 or HF-07 was triggered, or if no opener was found in the first 60 seconds.

### Call Purpose
One-line description of what the call was about, e.g.:
- `Pension scheme setup — new client onboarding`
- `PMI renewal — existing client`
- `Health insurance demo — prospect`
- `Operational — cover query`

### Issues
Comma-separated list of triggered criterion IDs and one-line descriptions, e.g.:
- `HF-01 (explicit recommendation at 04:23), HF-08 (absolute certainty claim at 11:47), SF-12 (emotive marketing language x2)`

### Training Opportunity/Gap
Describe the competency or process gap revealed by the findings, e.g.:
- `Rep on script pathway described PMI cover details — not permitted under MCC. Requires re-training on regulated activity definition and script boundaries.`
- `No recording consent given — opener script must be followed on every call.`

### Actions
Numbered remediation steps, e.g.:
- `1. Trevor to review recording and confirm findings. 2. Rep to be reminded of script boundaries. 3. Call to be discussed in next MCC supervision session.`

## Department → section mapping

| Kota staff role | Department | Section GID |
|---|---|---|
| Account Executive, BDR, Market Expansion Lead, GTM Lead | GTM | `1213240137041732` |
| Benefits Co-ordinator, Benefits Sales Lead, Head of Insurance Distribution | Benefits | `1213240137041734` |
| Customer Success, Customer Support, CS Co-ordinator | CS/CX | `1213240137041733` |
| Mixed / unclear | GTM (default) | `1213240137041732` |

## Escalation: when to @-mention Simon Ellis

Add `1213214965151657` as a follower and include `<a data-asana-gid="1213214965151657"/>` in the html_notes when **any** of:
- Grade 4 (Fail w/ referral) or Grade 5 (Severe Fail)
- ES-01 (customer distress / complaint)
- ES-02 (claim or coverage dispute)
- ES-03 (out-of-scope commitment made by Kota staff)
- HF-03 (firm capability or regulatory status misrepresented)
- HF-00 triggered for an **unregistered** speaker (Kate Fullen, or any unrecognised name)

## Grade label reference

| Grade | Label to use in task name |
|---|---|
| 5 | `Severe Fail` |
| 4 | `Fail` |
| 3 | `Fail` |
| 2 | `Pass with comments` |

## Full worked example

**Scenario**: GTM call with Karl O'Brien (script pathway) who described PMI dental cover limits to a prospect, and gave no recording disclosure.

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
      "custom_fields": "{\"1213240170325716\":\"1213240170325718\",\"1213240170325723\":\"PMI demo — new prospect\",\"1213240170325728\":\"HF-00 (unqualified speaker describing cover details at 06:12), HF-06 (no recording consent opener), HF-10 (cover details by script-pathway rep)\",\"1213240170325733\":\"Karl is on script pathway and described specific PMI dental cover limits — not permitted under MCC. Needs refresher on regulated activity boundary.\",\"1213240170325738\":\"1. Trevor to review recording by 2026-05-09. 2. Karl to be reminded of script boundaries. 3. Discuss at next MCC supervision.\"}",
      "html_notes": "<body><h1>Call Details</h1><ul><li><strong>Client / Prospect:</strong> Prospect Corp Ltd</li><li><strong>Call date:</strong> 2026-05-08 10:30</li><li><strong>Duration:</strong> 24 minutes</li><li><strong>Department:</strong> GTM</li></ul><h1>Participants</h1><ul><li><strong>Kota staff:</strong> Karl O'Brien — Account Executive — Script pathway (unqualified)</li><li><strong>Customer / Prospect:</strong> Jane Smith, Prospect Corp Ltd</li></ul><h1>Compliance Findings</h1><ul><li><strong>HF-06 — No recording disclosure — 00:00</strong><br/>No consent opener given in first 60 seconds.<br/><em>Regulation:</em> CPC 2025; IDR S.I. 229/2018 Reg. 23<br/><em>Severity:</em> Medium</li><li><strong>HF-10 — Cover details by unqualified speaker — 06:12</strong><br/><em>Transcript:</em> \"The cash plan covers dental up to €500 per year and optical up to €150.\"<br/><em>Speaker:</em> Karl O'Brien (Script pathway — unqualified)<br/><em>Regulation:</em> CBI MCC 2017 — provision of information on retail financial product by unqualified person<br/><em>Severity:</em> High</li></ul><h1>Training / Gap</h1><p>Karl is on the prescribed script pathway and described specific PMI cover limits to a prospect. This is a MCC-regulated activity that requires an APA (PMI) or QFA qualification. Script requires immediate review to ensure this information is not included in unqualified rep flow.</p><h1>Actions Required</h1><ol><li>Trevor Gardiner to review recording and confirm findings by 2026-05-09.</li><li>Karl to be reminded of script boundaries and MCC regulated activity definition.</li><li>Discuss at next MCC supervision session; document in supervision log.</li></ol><hr/><p>For action: <a data-asana-gid=\"1214070419259752\"/> (Matthew Brennan)<br/>MCC Supervisor: <a data-asana-gid=\"1212984665985179\"/> (Trevor Gardiner)</p></body>"
    }
  ]
}
```
