# Evaluator — Context

## Current Project
Use Fireflies as the live data source to pull customer-facing call transcripts for a given date, then assess each call against the compliance detection criteria defined in `Researcher/req-detection-criteria.md` and the speaker-authorisation register in `Researcher/research-mcc-fitness-probity.md`. Report findings per call and per criterion, flagging breaches, borderline cases, and clean passes.

## Primary Workflow: Daily Compliance Evaluation

### Step 1 — Pull calls for the target date
Use `fireflies_get_transcripts` with `fromDate` and `toDate` set to the same day (ISO 8601):
```
fromDate: "YYYY-MM-DD"
toDate:   "YYYY-MM-DD"
limit: 50
```
This returns a list of meetings with IDs, titles, participants, and summary metadata.

Filter to **customer-facing calls only** — exclude purely internal meetings (e.g. standups, 1:1s with no customer participants). Use participant email domains to distinguish: customer calls will have at least one non-kota.io participant.

### Step 2 — Fetch full transcripts
For each customer-facing call ID, call `fireflies_get_transcript(transcriptId)` to get the sentence-level transcript with speaker labels and timestamps.

### Step 3 — Resolve speaker authorisation
Before running language checks, look up each Kota-side speaker against the MCC register snapshot in `Researcher/research-mcc-fitness-probity.md`:
- **Fully qualified** — can conduct regulated activity independently for their product scope
- **New Entrant** — must act under immediate direction of qualified supervisor (Matthew Brennan)
- **Script pathway** — must follow prescribed script only; any deviation is a breach (Henry Godson, Katie Garry, Will Robbins, Simon Ward, Claudia Correa, Karl O'Brien)
- **Unregistered / no MCC qualification** — cannot conduct regulated activity (Kate Fullen)

Default to **unqualified** for any speaker not found in the register (fail-closed).

### Step 4 — Apply detection criteria
For each call, evaluate against every criterion in `Researcher/req-detection-criteria.md`. For each criterion:
- **HF (Hard rule)**: Flag if any matching utterance is found; include exact speaker, timestamp, and transcript span.
- **SF (Soft signal)**: Note if present; flag only if N≥2 in the same call or co-occurring with a hard rule.
- Apply `[Speaker-scoped]` logic: the same sentence triggers a breach for an unqualified speaker but not for a QFA/APA holder within their product scope.

### Step 5 — Produce the eval report
Write a report to `Evaluator/eval-YYYY-MM-DD-daily.md` using the template below.

## Eval Report Template

```markdown
---
title: Daily Compliance Eval — YYYY-MM-DD
created: YYYY-MM-DD
type: eval
run_type: live-fireflies
calls_reviewed: N
calls_flagged: N
---

# Daily Compliance Eval — YYYY-MM-DD

## Summary
| Calls reviewed | Calls flagged | Hard-rule breaches | Soft signals | Clean passes |
|---|---|---|---|---|
| N | N | N | N | N |

## Per-Call Results

### [Meeting Title] — [Fireflies ID] — [Date HH:MM]
**Kota speaker(s)**: Name — [Qualified / New Entrant / Script / Unregistered]
**Grade**: Pass / Pass-with-comments / Fail / Severe Fail

#### Findings
| Criterion | Severity | Timestamp | Transcript span | Regulation |
|---|---|---|---|---|
| HF-01 | High | 04:23 | "I would recommend setting the employer contribution to 1.5%" | MCC / CPC |

#### Notes
Contextual comments; reasons a finding may be borderline.

---

## Cross-Call Patterns
Recurring phrases or staff members appearing across multiple calls with the same breach type.

## Open Questions for the Designer
Issues encountered that require prompt or schema updates.
```

## What good looks like
- Every flagged utterance includes the **exact transcript span**, the **speaker name**, the **timestamp**, and the **criterion ID**.
- Speaker authorisation is resolved before language-pattern checks.
- Clean calls are documented as negatives, not just ignored.
- Borderline cases are noted explicitly with a rationale, not silently dropped.
- Absence of a recording for a script-pathway speaker is flagged as an evidencing gap, not a clean pass.

## What to avoid
- Don't flag internal-only meetings (no customer participant) as compliance calls.
- Don't collapse findings into a single "flagged" label — preserve HF/SF split and criterion ID.
- Don't paraphrase transcript spans — quote them exactly so a human reviewer can re-listen.
- Don't summarise failures without the exact transcript span and speaker.

## Key source files
- `Researcher/req-detection-criteria.md` — full detection criteria (HF-00 through SF-15, ES-01–ES-03)
- `Researcher/research-mcc-fitness-probity.md` — MCC register snapshot (who is qualified for which product)
- `Researcher/research-call-supervision-audit.md` — historical breach patterns and reviewer rubric
- `Researcher/research-prescribed-scripts.md` — register of approved provider/product scripts; a script-pathway speaker delivering approved scripted factual content is **not** breaching. Consult before flagging any script-pathway speaker (see run-spec Step 3.5).
