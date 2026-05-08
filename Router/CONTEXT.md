# Router — Context

## Role
Receive flagged calls from the Evaluator and create tasks in the Asana **Call Monitoring** project. Each task captures who was on the call, the client/prospect, the department involved, when the breach occurred in the call, the exact regulatory requirement breached, and @-mentions the relevant executive for follow-up.

## Asana — Call Monitoring Project

**Project GID**: `1213240137041729`

### Sections (map to department)
| Department | Section name | Section GID |
|---|---|---|
| GTM (Go-to-Market) | Go-to-Market | `1213240137041732` |
| CS / CX (Customer Success) | Customer Success | `1213240137041733` |
| Benefits | Benefits | `1213240137041734` |

### Custom fields
| Field | Type | GID | Options |
|---|---|---|---|
| Recording Consent | Enum | `1213240170325716` | Yes: `1213240170325717` · No: `1213240170325718` |
| Call Purpose | Text | `1213240170325723` | Free text |
| Issues | Text | `1213240170325728` | Free text — paste compliance findings |
| Training Opportunity/Gap | Text | `1213240170325733` | Free text |
| Actions | Text | `1213240170325738` | Free text — remediation steps |

### Executive users
| Name | Role | GID | Email |
|---|---|---|---|
| Trevor Gardiner | CF7 · Head of Insurance Distribution · MCC Supervisor | `1212984665985179` | trevor@kota.io |
| Matthew Brennan | GTM Lead (CF4 New Entrant) | `1214070419259752` | matthew@kota.io |
| Simon Ellis | COO (PCF42) | `1213214965151657` | simon.ellis@kota.io |
| Sola Olaniyan | Compliance Manager | `1213006028880034` | sola@kota.io |

## Routing logic

### Task assignee
| Condition | Assign to |
|---|---|
| Department = Benefits | Trevor Gardiner |
| Department = CS / CX | Trevor Gardiner (supervises all script-pathway CS staff) |
| Department = GTM | Matthew Brennan |

### Followers (always add both)
- Sola Olaniyan (`1213006028880034`) — Compliance Manager, always on all tasks
- Trevor Gardiner (`1212984665985179`) — always on all tasks as MCC supervisor

### When to @-mention Simon Ellis
Add Simon Ellis as follower and @-mention him in the task body when **any** of:
- Grade 4 (Fail) or Grade 5 (Severe Fail)
- Any ES-01 / ES-02 / ES-03 escalation signal is present
- Breach involves misrepresentation of firm capability or scope (HF-03)
- Unregistered speaker conducting regulated activity (HF-00 + Kate Fullen / unknown speaker)

## Task structure

**Task name format**: `[Grade label] — [Client/Prospect name] — [YYYY-MM-DD]`
Examples:
- `Fail — Acme Corp — 2026-05-08`
- `Severe Fail — TechStart Ltd — 2026-05-08`
- `Pass with comments — GlobalHR Inc — 2026-05-08`

**Due date**: same day as the call (so it appears in the daily view immediately)

See `Router/spec-asana-task.md` for the full task body template and `html_notes` format.
