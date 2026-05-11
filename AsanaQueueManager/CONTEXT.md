# Asana Call Monitoring Queue Manager — Context

## Role
Receive flagged calls from the Evaluator and create tasks in the Asana **Call Monitoring** project. Each task captures who was on the call, the client/prospect, the department involved, when the breach occurred in the call, the exact regulatory requirement breached, and @-mentions the relevant executive for follow-up.

## Asana — Call Monitoring Project

**Project GID**: `1213240137041729`

### Sections
| Section | Used for | Section GID |
|---|---|---|
| Go-to-Market | GTM department calls | `1213240137041732` |
| Customer Success | CS / CX department calls | `1213240137041733` |
| Benefits | Benefits department calls | `1213240137041734` |
| Escalated | Severe Fail and any ES-01/02/03 escalation — Simon Ellis loop-in | `1213240137041730` |

### Custom fields
| Field | Type | GID | Used for |
|---|---|---|---|
| Grade | Enum | `1213240170325716` | Severity rating — see options below |
| Call Purpose | Text | `1213240170325723` | One-line description of what the call was about |
| Issues | Text | `1213240170325728` | Criterion IDs + transcript spans, comma-separated |
| Requirement Breached | Text | `1213240170325733` | Regulatory reference (e.g. CBI MCC 2017, CPC 2025 Part 3, FCA COBS 9) |
| Recording Link | Text | `1213240170325738` | Fireflies recording URL |
| Kota Staff | Text | `1214635377742250` | Name and MCC status of Kota staff on the call, e.g. `Karl O'Brien (Script pathway)` |
| Prospect/Client | Text | `1214635377742252` | Prospect or client company name |

#### Grade enum options
| Label | GID | Maps to audit grade |
|---|---|---|
| Pass | `1213240170325717` | Grade 2 (Pass with comments) |
| Fail | `1214635377742249` | Grade 3 or Grade 4 |
| Severe Fail | `1213240170325718` | Grade 5 |

> No task is created for Grade 1 (clean Pass / no findings).

### Executive users
| Name | Role | GID | Email |
|---|---|---|---|
| Trevor Gardiner | CF7 · Head of Insurance Distribution · MCC Supervisor | `1212984665985179` | trevor@kota.io |
| Matthew Brennan | GTM Lead (CF4 New Entrant) | `1214070419259752` | matthew@kota.io |
| Simon Ellis | COO (PCF42) | `1213214965151657` | simon.ellis@kota.io |
| Sola Olaniyan | Compliance Manager | `1213006028880034` | sola@kota.io |

## Routing logic

### When to create a task
**Only Grade 3 (Fail), Grade 4 (Fail w/ referral), and Grade 5 (Severe Fail) generate Asana tasks.** Asana acts as a triage queue for second-line compliance to resolve issues. Grade 1 (Pass) and Grade 2 (Pass with comments) are documented in the Evaluator report only — they do not create tasks.

### Section
| Condition | Section |
|---|---|
| Department = GTM | Go-to-Market |
| Department = CS / CX | Customer Success |
| Department = Benefits | Benefits |
| Severe Fail OR ES-01/02/03 fired | Escalated (overrides the department section) |

### Task assignee
**No assignee is set on creation.** Second-line compliance triages each task in the queue, decides whether it warrants escalation, and assigns to the appropriate executive themselves. Pre-assigning would short-circuit triage.

### Followers (always add both)
- Sola Olaniyan (`1213006028880034`) — Compliance Manager
- Trevor Gardiner (`1212984665985179`) — MCC supervisor

### When to @-mention Simon Ellis in the task body (still automatic)
Add Simon Ellis as follower and include `<a data-asana-gid="1213214965151657"/>` in the task body when **any** of:
- Grade = `Severe Fail`
- Any ES-01 / ES-02 / ES-03 escalation signal is present
- Breach involves misrepresentation of firm capability or scope (HF-03)
- Unregistered speaker conducting regulated activity (HF-00 + Kate Fullen / unknown speaker)

The @-mention surfaces the case to Simon for awareness; the assignment decision still sits with second-line compliance.

## Task structure

**Task name format**: `[Grade] — [Client/Prospect name] — [YYYY-MM-DD]`
Examples:
- `Fail — Acme Corp — 2026-05-08`
- `Severe Fail — TechStart Ltd — 2026-05-08`

(No `Pass — ...` tasks — those never reach Asana.)

**Due date**: same day as the call (so it appears in the daily view immediately).

**Issues field — exact verbatim quotes only.** Every finding in the `Issues` custom field must include the EXACT verbatim transcript quote (not a paraphrase, not an AI summary). The quote is the search key: compliance pastes it into the Fireflies search bar to jump to the moment. Timestamps are unreliable through the current MCP transcript tools — the verbatim quote is the source of truth.

The Kota staff member's name + MCC status goes in the task **html_notes** body (no dedicated custom field), under a "Participants" section. See `AsanaQueueManager/spec-asana-task.md` for the full task body template and `html_notes` format.
